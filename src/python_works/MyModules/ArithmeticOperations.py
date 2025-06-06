class Calculator:
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2

    def calculate(self):
        if self.operator == '+':
            result = self.num1 + self.num2
            operator_str = '더하기'
        elif self.operator == '-':
            result = self.num1 - self.num2
            operator_str = '빼기'
        elif self.operator == '*':
            result = self.num1 * self.num2
            operator_str = '곱하기'
        elif self.operator == '/':
            result = self.num1 / self.num2
            operator_str = '나누기'
        else:
            print("잘못된 연산자입니다.")
            return

        print("==========================")
        print(f"{self.num1} {operator_str} {self.num2}을 계산합니다.")
        print("==========================")
        print(f"{self.num1} {self.operator} {self.num2} = {result}입니다.")