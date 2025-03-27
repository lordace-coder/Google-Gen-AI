from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ai
import pydantic

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600
)
class HomeResponse(pydantic.BaseModel):
    message:str
    def __init__(self,message):
        self.message = message

@app.get('/')
def home_page():
    return {"message":"hello user"}

class AIRequest(pydantic.BaseModel):
    message: str

@app.post('/ai')
def handle_message_ai(request: AIRequest):
    result = ai.message_ai(request.message)
    return {"message": result}