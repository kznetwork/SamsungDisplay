from MyModules.ArithmeticOperations import Calculator

num1 = int(input("첫번째 정수값 >> "))
operator = input("연산자 >> ")
num2 = int(input("두번째 정수값 >> "))

calculator = Calculator(num1, operator, num2)
calculator.calculate()