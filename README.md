# Autonomous Hiring Agent

## Overview

The Autonomous Hiring Agent is an AI-powered system designed to help recruiters and candidates analyze, score, and improve résumés based on a specific job description. By leveraging advanced language models (Gemini 2.0 Flash) and an intuitive web interface, this application provides immediate feedback and actionable suggestions to strengthen résumés for targeted roles.

---

## Features

* Upload résumés in PDF format for analysis
* Paste any job description to compare and evaluate fit
* Receive a detailed fit score out of 10
* Get tailored, improved bullet points to enhance the résumé
* Beautiful, interactive web UI built with Streamlit
* Backend powered by FastAPI and Gemini LLM for intelligent content generation
* Live animations and downloadable improvement reports

---

## Tech Stack

* FastAPI (backend API)
* Google Gemini 2.0 Flash (LLM integration)
* Streamlit (frontend interface)
* Python (core language)
* Render (backend deployment)
* Streamlit Cloud (frontend deployment)

---

## Live Demo

* [Live App (Streamlit Frontend)](https://ai-resume-validation-54kmmowripkhxetndr2fib.streamlit.app/)
* [Backend API (FastAPI Docs)](https://ai-resume-validation-1.onrender.com/docs)

---

## How it Works

1. **Upload a Résumé**
   Upload your résumé in PDF format through the Streamlit frontend.

2. **Paste Job Description**
   Copy and paste the job description for the role you are targeting.

3. **Get Score and Suggestions**
   The system evaluates the résumé against the job description using Gemini 2.0 Flash, returns a fit score out of 10, and suggests bullet points to improve alignment.

4. **Download and Apply Changes**
   Download the improvement suggestions as a text file and update your résumé accordingly.

---

## Deployment

### Backend

* Hosted on Render
* URL: [Backend API](https://ai-resume-validation-1.onrender.com/docs)
* Start command:

  ```
  uvicorn app.main:app --host 0.0.0.0 --port 10000
  ```

### Frontend

* Hosted on Streamlit Cloud
* Connects to Render backend via HTTPS

---

## Running Locally

### Backend

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
pip install streamlit requests
streamlit run frontend.py
```

Update `frontend.py` to point to your local backend URL if testing locally.

---

## Folder Structure

```
.
├── app/
│   ├── main.py
│   ├── jd_compare.py
│   ├── parsing_utils.py
│   └── ...
├── frontend.py
├── requirements.txt
├── README.md
└── ...
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.


---

## Acknowledgements

* Google Gemini API for LLM-based content analysis
* Streamlit for rapid UI development
* Render and Streamlit Cloud for smooth deployment experience

---
