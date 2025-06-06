# 구구단 출력
for i in range(2, 20):    # 2부터 19까지 반복
    print(f"\n{i}단:")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

# 간단한 계산기 만들기
print("간단한 계산기입니다!")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")

# 사용자로부터 입력 받기
choice = int(input("원하는 연산을 선택하세요 (1-4): "))
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 계산하기
if choice == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("0으로는 나눌 수 없습니다!")
else:
    print("잘못된 선택입니다!")

import random

# 1부터 100까지의 랜덤 숫자 생성
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    # 사용자의 추측 입력 받기
    guess = int(input("숫자를 입력하세요: "))
    attempts += 1
    
    # 추측이 맞았는지 확인
    if guess < secret_number:
        print("더 큰 숫자입니다!")
    elif guess > secret_number:
        print("더 작은 숫자입니다!")
    else:
        print(f"정답입니다! {attempts}번 만에 맞추셨네요!")
        break

# 단어장 만들기
vocabulary = {}

while True:
    print("\n1. 단어 추가")
    print("2. 단어 검색")
    print("3. 단어장 보기")
    print("4. 종료")
    
    choice = int(input("원하는 기능을 선택하세요 (1-4): "))
    
    if choice == 1:
        word = input("새로운 단어를 입력하세요: ")
        meaning = input("단어의 뜻을 입력하세요: ")
        vocabulary[word] = meaning
        print("단어가 추가되었습니다!")
        
    elif choice == 2:
        word = input("찾을 단어를 입력하세요: ")
        if word in vocabulary:
            print(f"{word}: {vocabulary[word]}")
        else:
            print("찾는 단어가 없습니다.")
            
    elif choice == 3:
        print("\n=== 내 단어장 ===")
        for word, meaning in vocabulary.items():
            print(f"{word}: {meaning}")
            
    elif choice == 4:
        print("프로그램을 종료합니다.")
        break

import turtle

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# 사용자로부터 입력 받기
shape = input("그리고 싶은 도형을 선택하세요 (사각형/삼각형/원): ")
color = input("원하는 색상을 입력하세요: ")

# 색상 설정
t.color(color)

# 도형 그리기
if shape == "사각형":
    for _ in range(4):
        t.forward(100)
        t.right(90)
elif shape == "삼각형":
    for _ in range(3):
        t.forward(100)
        t.right(120)
elif shape == "원":
    t.circle(50)
else:
    print("지원하지 않는 도형입니다.")

# 창 유지
turtle.done()

# 할 일 목록 만들기
todo_list = []

while True:
    print("\n=== 할 일 관리 프로그램 ===")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 완료하기")
    print("4. 종료")
    
    choice = int(input("원하는 기능을 선택하세요 (1-4): "))
    
    if choice == 1:
        task = input("새로운 할 일을 입력하세요: ")
        todo_list.append({"task": task, "completed": False})
        print("할 일이 추가되었습니다!")
        
    elif choice == 2:
        print("\n=== 할 일 목록 ===")
        for i, item in enumerate(todo_list, 1):
            status = "완료" if item["completed"] else "미완료"
            print(f"{i}. {item['task']} - {status}")
            
    elif choice == 3:
        if not todo_list:
            print("할 일이 없습니다!")
            continue
            
        print("\n=== 할 일 목록 ===")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item['task']}")
            
        task_num = int(input("완료할 할 일의 번호를 입력하세요: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num-1]["completed"] = True
            print("할 일이 완료되었습니다!")
        else:
            print("잘못된 번호입니다!")
            
    elif choice == 4:
        print("프로그램을 종료합니다.")
        break
