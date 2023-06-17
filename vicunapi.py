import os, requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from langchain.callbacks import StdOutCallbackHandler
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from pydantic import BaseModel

MODEL_PATH = "/var/tmp/ggml-vic13b-q5_1.bin"

app = FastAPI()

def send_message(prompt: str):
    template = """### Human: {prompt} 
### Assistant: """

    prompt_template = PromptTemplate(template=template, input_variables=["prompt"])
    
    callback = StdOutCallbackHandler()

    model = LlamaCpp(
        model_path=MODEL_PATH, 
        callbacks=[callback],
        verbose=True,
        temperature=0.9,
        max_tokens=800
        )

    llm_chain = LLMChain(prompt=prompt_template, llm=model)

    response = llm_chain.run(prompt)
    print(response)
    return response

class PromptRequest(BaseModel):
    """Request body for prompt."""
    prompt: str

@app.post("/prompt")
def prompt(body: PromptRequest):
    return JSONResponse(send_message(body.prompt), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8000, app=app)