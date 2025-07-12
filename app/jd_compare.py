import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def score_resume_against_jd(resume_text, jd_text):
    prompt = (
        f"Given this job description:\n{jd_text}\n\n"
        f"And this résumé text:\n{resume_text}\n\n"
        "1. Provide a fit score out of 10 (for example, 'Fit Score: 7/10').\n"
        "2. Suggest 3 improved bullet points to strengthen this résumé for the given JD."
    )
    try:
        response = model.generate_content(prompt)
        content = response.text

        lines = content.splitlines()
        score = None
        suggestions = []

        for line in lines:
            if "score" in line.lower():
                # Extract score part after colon
                parts = line.split(":")
                if len(parts) > 1:
                    score = parts[1].strip()
                else:
                    score = line.strip()
            elif line.strip():
                suggestions.append(line.strip())

        # Fallback if score was not found
        if score is None:
            score = "N/A"

        return score, suggestions

    except Exception as e:
        print(f"Error from Gemini: {e}")
        return "Error", ["Check Gemini API key and quota."]
