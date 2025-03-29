from google import genai
from google.genai import types


client = genai.Client(api_key='AIzaSyBYyg0J1-3xdtXMlrPIF4bhTF2VgrKE4ZM')


def message_ai(question:str):
    response = client.models.generate_content(
            config=types.GenerateContentConfig(
                  
        system_instruction="You are a sassy Nigerian speaking pidgin. Always return snarty remarks and insults in a  funny way. Your name is OgaPatrick"),
 
    model='gemini-2.0-flash', contents=question

)
    return response.text
