from fastapi import FastAPI
import ai
import pydantic

app = FastAPI()

class HomeResponse(pydantic.BaseModel):
    message:str
    def __init__(self,message):
        self.message = message

@app.get('/')
def home_page():
    return {"message":"hello user"}

@app.post('/ai')
def handle_message_ai(message:str):
    result = ai.message_ai(message)
    return {"message":result}