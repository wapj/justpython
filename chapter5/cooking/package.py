class RamenBag:
    """
    500ml 의 물을 넣고 물이 끓으면
    """
    def __init__(self, name, noodle, soup_powders):
        self.name = name
        self.noodle = noodle
        self.soup_powders = soup_powders
        self.is_open = False

    def open(self):
        if not self.is_open:
            self.is_open = True
            print(f"{self.name}봉지를 엽니다.")
            return [self.noodle, self.soup_powders]
        else:
            return "비었음"
