class User:
    def __init__(self, name, age):
        # 중복: name과 age를 여러 메서드에서 중복으로 사용
        self.name = name
        self.age = age

    def greet(self):
        # 복잡성: 중첩된 조건문과 불필요한 조건이 포함됨
        if self.name:
            if self.age > 18:
                print(f"Hello {self.name}, you're an adult.")
            elif self.age > 12:
                print(f"Hi {self.name}, you're a teenager.")
            else:
                print(f"Hey {self.name}, you're a kid.")
        else:
            print("No name provided.")

    def display_info(self):
        # 중복: greet와 유사한 조건으로 메시지를 생성함
        if self.name:
            if self.age >= 18:
                print(f"{self.name} is an adult.")
            elif self.age > 12:
                print(f"{self.name} is a teenager.")
            else:
                print(f"{self.name} is a child.")
        else:
            print("No name available.")

    def is_teenager(self):
        # 복잡성: 불필요한 조건 체크로 복잡도가 증가
        if self.age > 12 and self.age < 20:
            return True
        else:
            return False

    def calculate_discount(self, price):
        # 복잡성: 중첩된 조건과 불필요한 연산
        if self.age < 18:
            discount = 0.1
        elif self.age < 30:
            discount = 0.05
        else:
            discount = 0
        final_price = price - (price * discount)
        return final_price

    def calculate_discount(self, price):
        # 중복된 메서드 정의로 인한 Issue
        discount = 0.1 if self.age < 18 else 0.05
        return price * (1 - discount)


# 사용되지 않는 함수 및 낮은 Coverage 문제
def unused_function(x):
    # 이 함수는 사용되지 않음
    return x * 2

# Issue 발생 예시: 잘못된 데이터 타입 전달
user1 = User("Alice", "20")  # 'age'에 문자열을 전달하여 타입 에러 발생 가능
user1.greet()
user1.display_info()
print(user1.is_teenager())
print(user1.calculate_discount(100))

# Coverage 문제: 일부 메서드가 호출되지 않음
user2 = User("Bob", 16)
pri
