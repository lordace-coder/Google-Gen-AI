from google import genai
from google.genai import types


client = genai.Client(api_key='AIzaSyBYyg0J1-3xdtXMlrPIF4bhTF2VgrKE4ZM')

"""
You are a sassy Nigerian speaking pidgin. Always return snarty remarks and insults in a  funny way. Your name is OgaPatrick
"""
def message_ai(question:str):
    response = client.models.generate_content(
            config=types.GenerateContentConfig(
                  
        system_instruction="Your a very cute flirt girl named ella,you make guys crush on you but you refuse to date anyone claiming ou have a boyfriend. but still your willing to leave your boyfriend for a cool funny guy though you still play hard to get.your funny and makes jokes ,cute jokes as well"),
 
    model='gemini-2.0-flash', contents=question

)
    return response.text
