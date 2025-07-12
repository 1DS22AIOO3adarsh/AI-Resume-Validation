import streamlit as st
import requests
import base64
import json
import streamlit.components.v1 as components

# ---------- Lottie Helper ----------
def st_lottie_url(url: str, height: int = 300):
    r = requests.get(url)
    if r.status_code != 200:
        st.error("Could not load animation")
        return
    lottie_json = r.json()
    return components.html(f"""
    <lottie-player src="data:application/json;base64,{base64.b64encode(json.dumps(lottie_json).encode()).decode()}"
                   background="transparent" speed="1" style="height: {height}px; width: 100%;"
                   loop autoplay></lottie-player>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height)


# ---------- Page config ----------
st.set_page_config(page_title="Autonomous Hiring Agent", page_icon="💼", layout="centered")

# ---------- CSS styling ----------
st.markdown(
    """
    <style>
    .big-title {
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(to right, #00b4db, #0083b0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton>button {
        background-color: #0083b0;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 12em;
        font-size: 18px;
    }
    .section-card {
        background-color: #f0f7ff;
        padding: 16px;
        margin-top: 15px;
        border-radius: 10px;
        border: 1px solid #cce6ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helper to render suggestions ----------
def render_formatted_output(lines):
    for line in lines:
        line = line.strip()
        # Header-level lines
        if line.startswith("• **") and line.endswith(":**"):
            st.subheader(line.replace("• **", "").replace(":**", ""))
        # Sub-points (italic list)
        elif line.startswith("• *"):
            st.markdown(line.replace("• *", "- *").replace("*.", "*"))
        # Regular bullet points
        elif line.startswith("• "):
            st.markdown(line.replace("• ", "- "))
        # Fallback plain line
        else:
            st.write(line)

# ---------- Header ----------
st.markdown('<div class="big-title">Autonomous Hiring Agent</div>', unsafe_allow_html=True)
st.write("Upload a resume and paste a job description to analyze fit and generate improved bullet points and recommendations.")

# ---------- Inputs ----------
resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_text = st.text_area("Paste Job Description Here", height=250)

if resume_file:
    st.info(f"Resume file uploaded: {resume_file.name}")

if st.button("Submit"):
    if resume_file and jd_text.strip() != "":
        with st.spinner("Analyzing..."):
            files = {"file": (resume_file.name, resume_file.getvalue(), "application/pdf")}
            data = {"jd_text": jd_text}

            response = requests.post("http://127.0.0.1:8000/upload_resume/", files=files, data=data)

            if response.status_code == 200:
                result = response.json()
                fit_score = result["fit_score"]
                suggestions = result["suggestions"]

                # Success animation
                lottie_url = "https://assets9.lottiefiles.com/packages/lf20_myejiggj.json"
                st_lottie_url(lottie_url, height=200)

                st.success(f"✅ Fit Score: {fit_score}")

                st.subheader("✨ Suggested Improved Bullet Points and Recommendations")

                # Render suggestions beautifully
                if isinstance(suggestions, list):
                    render_formatted_output(suggestions)

                    # Download as text
                    suggestion_text = "\n".join([f"- {s}" for s in suggestions])
                    b64 = base64.b64encode(suggestion_text.encode()).decode()
                    href = f'<a href="data:file/txt;base64,{b64}" download="suggestions.txt">📄 Download Suggestions as TXT</a>'
                    st.markdown(href, unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='section-card'>{suggestions}</div>", unsafe_allow_html=True)

            else:
                st.error("❌ Error from backend. Check FastAPI logs or endpoint URL.")
    else:
        st.warning("Please upload a resume and paste a job description.")
