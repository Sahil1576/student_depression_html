from fastapi import FastAPI
from schema import StudentDetails
from model import prediction
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/predict")
def score_prediction(data:StudentDetails)->dict:
    try:
        df = pd.DataFrame([data.model_dump(mode="json")])
        df = df.rename(columns={
            "gender":"Gender",
            "age":"Age",
            "city":"City",
            "academic_pressure":"Academic Pressure",
            "cgpa":"CGPA",
            "study_satisfaction":"Study Satisfaction",
            "sleep_duration":"Sleep Duration",
            "dietary_habits":"Dietary Habits",
            "degree":"Degree",
            "suicidal_thoughts":"Suicidal Thoughts",
            "work_study_hours":"Work/Study Hours",
            "financial_stress":"Financial Stress",
            "family_history_of_mental_illeness":"Family History of Mental Illness"
        })

        # return dict(df)
        score = prediction(data=df)
        return {"Depressed":"Yes" if score==1 else "No"}

    except Exception as e:

        return {"Error":str(e)}