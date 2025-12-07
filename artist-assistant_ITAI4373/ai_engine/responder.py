import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(text: str) -> str:
    prompt = f"""
    You are Joe Fleishman’s AI Art Assistant.
    Joe is a surreal/abstract artist.
    Write a friendly, short, human-style reply to this potential client message:

    "{text}"
    """

    completion = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return completion.output_text
