# pip安装 fastapi 和 uvicorn
# 执行 "uvicorn main:app --host=localhost --port=8080 --reload" 启动服务端

import json
import requests
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from openai import OpenAI

app = FastAPI()

# 允许前端跨域调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def chat(query, client, model_name):
    completion = client.chat.completions.create(
        model=model_name,
        messages=query,
    )
    return completion.choices[0].message


def chat_with_history(query, history, client, model_name):
    history.append({
        "role": "user",
        "content": query
    })
    result = chat(history, client, model_name)
    history.append({
        "role": "assistant",
        "content": result.content
    })
    return result


# template ---------------------
key_template = "sk-FT00snCEhEo1VEpXC106058961D74894Ae06D369Ad001a79"
history_template = []
client_template = OpenAI(
    api_key=key_template,
    base_url="https://api.linkapi.org/v1",
)


# 阿里千问
@app.post("/qwen")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "qwen-plus")


# 百度千帆
@app.post("/ERNIE")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "ERNIE-4.0-8K")


# 讯飞星火
@app.post("/SparkDesk")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "SparkDesk-v3.5")


# 字节豆包
@app.post("/doubao")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "doubao-pro-128k")


# 清华智谱
@app.post("/glm")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "glm-4")


# kimi
@app.post("/moonshot")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "moonshot-v1-128k")


# gpt4o
@app.post("/chatgpt")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "chatgpt-4o-latest")


# claude
@app.post("/claude")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "claude-3-opus-20240229")


# 谷歌gemini
@app.post("/gemini")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "gemini-pro")


# deepseek
@app.post("/deepseek")
async def test(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return chat_with_history(prompt, history_template, client_template, "deepseek-chat")
