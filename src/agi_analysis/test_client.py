import requests
from urllib.parse import quote

BASE_URL = "http://localhost:8000"

# 리소스 이름 인코딩
resource_name = quote("http://example.com/docs", safe="")

print(f"요청 URL: {BASE_URL}/resources/{resource_name}")

# 1. 리소스 요청
res = requests.get(f"{BASE_URL}/resources/{resource_name}")
print(f"리소스 상태코드: {res.status_code}")
print("리소스 응답 내용:", res.text)

# 2. 도구 요청
payload = {"message": "Hello MCP!"}
res = requests.post(f"{BASE_URL}/tools/echo", json=payload)
print(f"도구 상태코드: {res.status_code}")
print("도구 응답 내용:", res.text)
