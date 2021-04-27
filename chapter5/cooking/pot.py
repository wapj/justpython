class Pot:
    things = []

    def put(self, thing):
        print(f"{thing}을 넣습니다.")
        self.things.append(thing)

    def boil(self):
        for thing in self.things:
            print(thing, end=" ")
        print("이 들어있는 냄비를 가열합니다.")

