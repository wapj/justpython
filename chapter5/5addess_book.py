# 주소록 만들기

class Address:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"이름 : {self.name} | 번호 : {self.number}"


class AddressBook:
    addresses = []

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"{self.title}"

    def add(self, address):
        self.addresses.append(address)

    def remove(self, keyword):
        find_addr = self.find(keyword)
        if not find_addr:
            print(f"{keyword}로 삭제할 수 없습니다.")
        else:
            print(f"{find_addr}을 삭제합니다.")
            self.addresses.remove(find_addr)

    def show_list(self):
        if not self.addresses:
            print("주소록에 주소가 없습니다.")
            return

        print("-" * 30)
        for addr in self.addresses:
            print(addr)
        print("-" * 30)

    def find(self, keyword):
        """이름 혹은 번호로 찾기"""
        for addr in self.addresses:
            if addr.name == keyword or addr.number == keyword:
                return addr
        return None


class Main:
    def __init__(self, address_book):
        self.address_book = address_book

    def remove(self):
        keyword = input("[4]주소삭제 | 검색어를 입력해주세요 : ")
        self.address_book.remove(keyword)

    def add(self):
        name = input("[3]주소추가 | 이름을 입력해 주세요 : ")
        number = input("[3]주소추가 | 번호를 입력해 주세요 : ")
        address = Address(name, number)
        self.address_book.add(address)
        print(f"{address}")

    def find(self):
        keyword = input("[2]주소찾기 | 찾을 번호 혹은 이름을 입력하세요 : ")
        address = self.address_book.find(keyword)
        if address:
            print(f"[찾은주소] {address}")
        else:
            print(f"찾을 수 있는 주소가 없습니다.")

    def show(self):
        print("[1]주소보기")
        self.address_book.show_list()

    def run(self):
        menu = "<<메인메뉴>>\n[1]주소보기 [2]주소찾기 [3]주소추가 [4]주소삭제 [5]종료"
        line = '=' * (len(menu) + 1)
        print(f"{line}\n{self.address_book}을 시작합니다.")
        while True:
            print(f"{line}\n{menu}\n")
            cmd = input("명령어를 입력하세요 : ")

            if not cmd.isdigit():
                print("해당하는 명령이 없습니다.")
                continue

            if int(cmd) == 5:
                break
            elif int(cmd) == 4:
                self.remove()
            elif int(cmd) == 3:
                self.add()
            elif int(cmd) == 2:
                self.find()
            elif int(cmd) == 1:
                self.show()
            else:
                print("해당하는 명령이 없습니다.")


if __name__ == '__main__':
    main = Main(AddressBook("승규의 주소록"))
    main.run()
