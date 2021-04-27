"""
<Just 할일 관리>
리스트, 추가, 수정, 삭제, 검색, 저장
"""
import json
from copy import copy
from datetime import datetime


class Todo:
    """
    인덱스, 타이틀, 우선순위, 완료여부, 생성일
    """

    priority_dict = {
        "1": "매우높음",
        "2": "높음",
        "3": "보통",
        "4": "낮음",
        "5": "매우낮음",
    }

    def __init__(self, idx, title, priority, is_done=False, created_dt=datetime.now()):
        self.idx = idx
        self.title = title
        self.priority = priority
        self.is_done = is_done
        self.created_dt = created_dt

    def __str__(self):
        done = '미완료'
        if self.is_done:
            done = '완료'

        return f"[{self.idx}| {done}] 제목 : {self.title} | 우선순위 : {self.priority_dict[self.priority]}"

    def to_dict(self):
        return {
            "idx": self.idx,
            "title": self.title,
            "priority": self.priority,
            "is_done": self.is_done,
            "created_dt": self.created_dt.isoformat(),
        }


class TodoList:
    todo_list = []

    def __init__(self):
        self.load()

    def load(self):
        self.todo_list = []
        try:
            with open('todo.json') as f:
                todo_json_data = json.loads(f.read())
                for todo_json in todo_json_data:
                    todo = Todo(todo_json['idx'], todo_json['title'], todo_json['priority'], todo_json['is_done'],
                                datetime.fromisoformat(todo_json['created_dt']))
                    self.todo_list.append(todo)
        except FileNotFoundError:
            # 파일이 없는것도 정상이므로 패스
            pass


    def list(self):
        print("리스트")

        for todo in self.todo_list:
            print(todo)

    def add(self):
        print("<<할일정보(타이틀, 우선순위)를 입력해주세요>>")
        title = input("타이틀 : ")
        priority = input("우선순위(1,2,3,4,5) : ")

        if not priority.isdigit() or int(priority) > 5:
            priority = 5

        todo = Todo(len(self.todo_list) + 1, title, priority)
        self.todo_list.append(todo)

    def modify(self):
        todo = self.find()
        todo_tmp = copy(todo)
        print("수정할 내용을 입력해주세요")
        priority = input("우선순위(1,2,3,4,5) : ")
        is_done = input("완료여부(y/n) : ")

        if priority.isdigit() and int(priority) <= 5:
            todo.priority = priority

        if is_done == 'y':
            todo.is_done = True
        else:
            todo.is_done = False

        print("<< 아래와 같이 수정되었습니다. >>")
        print("수정 전 : ", todo_tmp)
        print("수정 후 : ", todo)

    def delete(self):
        todo = self.find()
        print(todo)
        delete_yn = input("정말로 삭제하시겠습니까? (y/n) : ")
        if delete_yn == 'y':
            self.todo_list.remove(todo)
            print("할일을 삭제하였습니다.")

    def find(self):
        print("인덱스 혹은 타이틀을 입력해주세요. \n타이틀이 같은 경우 가장 최근의 할일이 나오게 됩니다.")
        search = input("인덱스 또는 타이틀 : ")
        for todo in reversed(self.todo_list):
            if todo.title == search or (search.isdigit() and todo.idx == int(search)):
                print("[찾은 할일]", todo)
                return todo
        print("해당 정보가 없습니다.")

    def save(self):
        """
        json 파일로 저장하자. (todo.json)
        문자열 -> dict : json.loads
        dict -> 문자열 : json.dumps
        시간 isoformat fromisoformat
        :return:
        """
        todo_dict_list = []
        for todo in self.todo_list:
            print(todo.to_dict())
            todo_dict_list.append(todo.to_dict())

        with open('todo.json', 'w') as f:
            f.write(json.dumps(todo_dict_list))


class Main:
    todo_list = TodoList()

    commands = {
        "l": todo_list.list,
        "a": todo_list.add,
        "m": todo_list.modify,
        "d": todo_list.delete,
        "f": todo_list.find,
        "s": todo_list.save,
        "e": exit,
    }

    def run(self):
        while True:
            print("=================================================")
            print("[l]리스트 [a]추가 [m]수정 [d]삭제 [f]검색 [s]저장 [e]종료")
            command = input("명령어 입력 : ")

            if command in self.commands.keys():
                self.commands[command]()
            else:
                print("잘못된 명령어입니다.")


if __name__ == '__main__':
    Main().run()
