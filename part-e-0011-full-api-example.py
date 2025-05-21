from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os


os.environ["OPENAI_API_KEY"] = "add your key"

app = FastAPI()

client = OpenAI()

class TranslationRequest(BaseModel):
    input_str: str


def translate_text(input_str):
    completion = client.chat.completions.create(
        model="o4-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert translator who translates text from English to Turkish in a humor way!",
            },
            {"role": "user", "content": input_str},
        ],
    )


    return completion.choices[0].message.content


@app.post("/translate/") 
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.input_str)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
