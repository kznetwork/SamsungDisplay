from flask import Flask

app = Flask(__name__)  # __main__


@app.route('/')  # 접속할 주소
def index():
    return 'Hello~~~!!!'  # 브라우저에 보여지는 응답결과


if __name__ == '__main__':
    app.run(debug=True)  # 서버 자동 재실행 debug=True 옵션