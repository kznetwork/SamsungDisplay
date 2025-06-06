while True:
    # 첫 번째 정수 입력
    num1_input = input("첫번째 정수값 >> ")
    if num1_input == 'q!':
        print("프로그램을 종료합니다.")
        break

    # 정수 유효성 검사
    if not num1_input.lstrip('-').isdigit():
        print("⚠️ 정수를 입력하세요.")
        continue
    num1 = int(num1_input)

    # 연산자 입력
    operator = input("연산자 (+, -, *, /) >> ")
    if operator == 'q!':
        print("프로그램을 종료합니다.")
        break

    # 유효한 연산자인지 확인
    if operator not in ['+', '-', '*', '/']:
        print("⚠️ 올바른 연산자를 입력하세요.")
        continue

    # 두 번째 정수 입력
    num2_input = input("두번째 정수값 >> ")
    if num2_input == 'q!':
        print("프로그램을 종료합니다.")
        break

    # 정수 유효성 검사
    if not num2_input.lstrip('-').isdigit():
        print("⚠️ 정수를 입력하세요.")
        continue
    num2 = int(num2_input)

    # 계산 수행
    if operator == '+':
        result = num1 + num2
        operator_str = '더하기'
    elif operator == '-':
        result = num1 - num2
        operator_str = '빼기'
    elif operator == '*':
        result = num1 * num2
        operator_str = '곱하기'
    elif operator == '/':
        if num2 == 0:
            print("⚠️ 0으로 나눌 수 없습니다.")
            continue
        result = num1 / num2
        operator_str = '나누기'

    # 결과 출력
    print("==========================")
    print(f"{num1} {operator_str} {num2}을 계산합니다.")
    print("==========================")
    print(f"{num1} {operator} {num2} = {result}입니다.")

    # 계속 여부 확인
    cont = input("계산을 계속 하시겠습니까? (y/n) >> ")
    if cont.lower() != 'y':
        print("프로그램을 종료합니다.")
        break
