class Order:
    def __init__(self, items, quantities, prices):
        # SRP 위반: Order 클래스가 아이템을 저장하고, 가격을 계산하고, 영수증을 출력하는 여러 책임을 갖고 있음
        self.items = items
        self.quantities = quantities
        self.prices = prices

    def calculate_total_price(self):
        # OCP 위반: 할인 등의 새로운 가격 정책을 추가하려면 이 메서드를 수정해야 함
        total = 0
        for i in range(len(self.items)):
            total += self.quantities[i] * self.prices[i]
        return total

    def print_receipt(self):
        # SRP 위반: Order 클래스가 영수증 출력이라는 별도의 책임을 가지고 있음
        print("Receipt:")
        for i in range(len(self.items)):
            print(f"{self.items[i]} x {self.quantities[i]}: ${self.quantities[i] * self.prices[i]}")
        print(f"Total: ${self.calculate_total_price()}")


class User:
    def __init__(self, name, age, address):
        # SRP 위반: 사용자 정보와 주문 처리 기능을 함께 갖고 있음
        self.name = name
        self.age = age
        self.address = address
        self.orders = []

    def place_order(self, items, quantities, prices):
        # LSP 위반: Order 객체가 아닌 항목 리스트만 사용
        order = Order(items, quantities, prices)
        self.orders.append(order)
        order.print_receipt()

    def get_order_count(self):
        return len(self.orders)


class Database:
    # DIP 위반: 상위 모듈이 하위 모듈에 직접적으로 의존하고 있음 (예: 데이터베이스 저장 방식을 결정)
    def save_order(self, order):
        print("Saving order to database...")
        # database save logic here


# 사용 예시
user = User("John Doe", 30, "1234 Elm St")
user.place_order(["Apple", "Banana"], [3, 2], [0.5, 0.3])
