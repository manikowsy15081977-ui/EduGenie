from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI(title="EduGenie by Yalini")

@app.get("/")
def home():
    return {"message": "EduGenie is Running"}

@app.get("/explain/{topic}")
def explain(topic: str):
    return {"topic": topic, "explanation": f"{topic} concept explained in simple way"}
