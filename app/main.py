from fastapi import FastAPI, UploadFile, Form
from app.parsing_utils import extract_text_from_pdf
from app.jd_compare import score_resume_against_jd

app = FastAPI()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile, jd_text: str = Form(...)):
    contents = await file.read()
    with open(f"data/resumes/{file.filename}", "wb") as f:
        f.write(contents)
    
    extracted_text = extract_text_from_pdf(f"data/resumes/{file.filename}")
    score, suggestions = score_resume_against_jd(extracted_text, jd_text)
    
    return {
        "fit_score": score,
        "suggestions": suggestions
    }
