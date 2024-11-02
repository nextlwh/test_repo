import math

def calculate(x, y, z, r, operation="add"):
    # 코드 품질 문제:
    # - 함수의 목적이 모호하며, 복잡한 로직이 한 곳에 모여 있음
    # - operation에 따라 여러 역할을 수행하는 함수로, 단일 책임 원칙에 위배됨
    if operation == "add":
        return x + y + z + r
    elif operation == "subtract":
        return x - y - z - r
    elif operation == "multiply":
        result = 1
        for value in [x, y, z, r]:
            result *= value
        return result
    elif operation == "divide":
        if y == 0 or z == 0 or r == 0:
            print("Division by zero error")
            return None
        return x / y / z / r
    elif operation == "hypotenuse":
        # Pythagorean theorem for 3D space calculation
        return math.sqrt(x**2 + y**2 + z**2)
    else:
        print("Invalid operation")
        return None

# 중복 코드가 많은 추가 기능 예시
def print_hello(name, age, gender):
    if gender.lower() == 'male':
        print("Hello Mr. " + name + ", you are " + str(age) + " years old.")
    elif gender.lower() == 'female':
        print("Hello Ms. " + name + ", you are " + str(age) + " years old.")
    else:
        print("Hello " + name + ", you are " + str(age) + " years old.")

# 긴 줄, 마법의 숫자, 불필요한 조건
def process_data(data):
    for i in range(len(data)):
        if data[i] == 0 or data[i] == 3 or data[i] == 7 or data[i] == 9:
            data[i] = data[i] * 10
        elif data[i] == 5:
            data[i] = data[i] * 5
        else:
            data[i] = data[i] + 1
    return data

# 함수 호출 예시
print(calculate(5, 3, 2, 0, "divide"))
print_hello("John", 28, "male")
print(process_data([1, 3, 5, 7, 9]))
