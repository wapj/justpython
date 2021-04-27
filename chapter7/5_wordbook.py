# 딕셔너리로 단어장 만들기

class WordBook:
    word_dict = {}

    def run(self):
        while True:
            cmd = input("[a]단어추가 | [m]단어수정 | [d]단어삭제 | [f]단어찾기 | [q]종료 : ")
            if cmd == 'q':
                exit()

            if cmd == 'a':
                self.add()
            elif cmd == 'm':
                self.modify()
            elif cmd == 'd':
                self.delete()
            elif cmd == 'f':
                self.find()
            else:
                print("알수 없는 명령입니다.")

    def add(self):
        word = input("단어를 입력해주세요 : ")
        mean = input("뜻을 입력해주세요 : ")

        if not word:
            print("[에러] 단어의 길이는 한 글자 이상이어야합니다.")
        else:
            self.word_dict.setdefault(word, mean)

    def modify(self):
        search = input("수정할 단어를 입력해주세요 : ")
        if self.word_dict.get(search):
            mean = input("수정할 단어의 뜻을 입력해주세요")
            if mean:
                self.word_dict[search] = mean
        else:
            print("단어를 찾지 못했습니다.")

    def delete(self):
        search = input("삭제할 단어를 입력해주세요 : ")
        if self.word_dict.get(search):
            del self.word_dict[search]
            print(f"{search}를 삭제했습니다.")
        else:
            print("단어를 찾지 못했습니다.")


    def find(self):
        search = input("찾으실 단어를 입력해주세요 : ")
        if search == '':
            for k, v in self.word_dict.items():
                print(f"{k} | {v}")
        else:
            mean = self.word_dict.get(search)
            if mean:
                print(f"{search} | {mean}")
            else:
                print("단어를 찾지 못했습니다.")


if __name__ == '__main__':
    word_book = WordBook()
    word_book.run()
