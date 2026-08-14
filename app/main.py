from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title = "ReAct-Agent-RAG",
    description = "Agent 演示项目",
    version = "1.0.0"
)

# 配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 测试接口
@app.get("/")
async def root():
    return {"message": "Welcome to ReAct-Agent-RAG!",
            "docs": "http://localhost:8000/docs"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/text")
async def text_endpoint():
    return {"message": "This is a text endpoint."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)