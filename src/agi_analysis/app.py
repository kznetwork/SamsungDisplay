from fastmcp import FastMCP
from pydantic import BaseModel, AnyUrl, HttpUrl
import uvicorn

app = FastMCP(title="My MCP Server")

# 입력 모델
class EchoQuery(BaseModel):
    message: str

# 출력 모델
class EchoResponse(BaseModel):
    echoed: str

# 도구 등록
@app.tool("echo", description="메시지를 그대로 반환합니다.")
def echo_tool(query: EchoQuery) -> EchoResponse:
    return EchoResponse(echoed=f"Echo: {query.message}")

# ✅ 리소스 경로를 실제 URL 형식으로 지정 (핵심 포인트!)
@app.resource("http://example.com/docs", description="API 사용 설명서")
def get_docs():
    return {
        "version": "1.0",
        "tools": ["echo"],
        "usage": "POST /tools/echo",
        "example_input": {"message": "안녕하세요!"}
    }

# 서버 실행
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)