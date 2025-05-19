class Restaurant:
    def receive_order(self, menu_item):
        print(f"Restaurant: '{menu_item}' 주문을 확인했습니다.")
        return True  # 항상 주문 수락으로 가정


class Delivery:
    def dispatch(self, menu_item):
        print(f"Delivery: '{menu_item}' 배달 요청 수신 → 배달 시작...")
        print("Delivery: 배달 완료")


class Server:
    def __init__(self):
        self.restaurant = Restaurant()
        self.delivery = Delivery()

    def fetch_restaurant_list(self):
        print("Server: 음식점 목록 반환 중...")
        return ["치킨집A", "치킨집B"]

    def process_order(self, menu_item):
        print("Server: 주문 요청 → Restaurant에 전달")
        confirmed = self.restaurant.receive_order(menu_item)
        if confirmed:
            print("Server: 주문이 접수되었습니다.")
            self.delivery.dispatch(menu_item)
            return "SUCCESS"
        else:
            print("Server: 주문 접수 실패")
            return "FAIL"


class App:
    def __init__(self, server):
        self.server = server

    def request_restaurant_list(self):
        print("App: 서버에 음식점 목록 요청")
        return self.server.fetch_restaurant_list()

    def place_order(self, menu_item):
        print(f"App: 서버에 주문 전달 → 메뉴: '{menu_item}'")
        return self.server.process_order(menu_item)


class User:
    def __init__(self, app):
        self.app = app

    def select_menu(self, menu_list):
        print("User: 메뉴 선택 중... (치킨 선택)")
        return "치킨"

    def start_order_flow(self):
        print("User: 메뉴 조회 요청")
        food_list = self.app.request_restaurant_list()

        print("User: 음식점 목록 표시")
        for r in food_list:
            print(f"- {r}")

        selected_item = self.select_menu(food_list)

        print(f"User: '{selected_item}' 주문 요청")
        result = self.app.place_order(selected_item)

        if result == "SUCCESS":
            print("User: 주문이 성공적으로 완료되었습니다!")
        else:
            print("User: 주문에 실패했습니다.")


# ===== 실행 =====
if __name__ == "__main__":
    server = Server()
    app = App(server)
    user = User(app)
    user.start_order_flow()
