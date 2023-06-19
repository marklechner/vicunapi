import os, requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from langchain.callbacks import StdOutCallbackHandler
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from pydantic import BaseModel

MODEL_PATH = "/Users/mark.lechner/dev/llm_models/Wizard-Vicuna-13B-Uncensored.ggmlv3.q5_K_S.bin"

app = FastAPI()

def send_message(question: str, temp: float, max_tokens: int):
    template = """HUMAN: {question} ASSISTANT: """

    prompt_template = PromptTemplate(template=template, input_variables=["question"])
    
    callback = StdOutCallbackHandler()

    model = LlamaCpp(
        model_path=MODEL_PATH, 
        callbacks=[callback],
        verbose=True,
        temperature=temp,
        max_tokens=max_tokens,
        streaming=False,
        use_mlock=True,
        n_threads=6,
        n_ctx=2048,
        top_p=1.000000,
        top_k = 12,
        echo=True,
        n_batch = 256,
        repeat_penalty = 1.050000,
        )

    llm_chain = LLMChain(prompt=prompt_template, llm=model)
    print(llm_chain)
    response = llm_chain.run(question)
    print(response)
    return response

class PromptRequest(BaseModel):
    """Request body for prompt."""
    question: str
    temp: float = 0.9
    max_tokens: int = 256

@app.post("/prompt")
def prompt(body: PromptRequest):
    return JSONResponse(send_message(body.question, body.temp, body.max_tokens), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8000, app=app)