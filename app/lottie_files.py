import streamlit as st
import requests
import base64
import json

def st_lottie(url: str, height: int = 300, key=None):
    r = requests.get(url)
    if r.status_code != 200:
        st.error("Could not load animation")
        return None
    return st_lottie_raw(r.json(), height=height, key=key)

def st_lottie_raw(lottie_json: dict, height: int = 300, key=None):
    json_str = json.dumps(lottie_json)  # Correctly convert dict to JSON string
    b64_json = base64.b64encode(json_str.encode()).decode()
    return st.components.v1.html(f"""
        <lottie-player src="data:application/json;base64,{b64_json}"
                       background="transparent" speed="1" style="height: {height}px; width: 100%;"
                       loop autoplay></lottie-player>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height, key=key)
