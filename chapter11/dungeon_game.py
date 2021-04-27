import random
import time


class Unit:
    """
    각 유닛(프로그래머, 몬스터 동일)은
    직업, 체력, 공격력, 방어력, 행운을 상태값으로 가짐
    모든 수치의 max값은 300이라고 가정
    공격과 회복 가능
    """

    MAX_HP = 0

    def __init__(self, job, hp, atk, dfs, luk):
        self.job = job
        self.hp = hp
        self.atk = atk
        self.dfs = dfs
        self.luk = luk

        self.MAX_HP = 0

    def get_lucky_weight(self):
        weight = random.randint(self.luk // 3, self.luk)
        return weight

    def attack(self, target):
        damage = self.atk + self.get_lucky_weight()
        damage -= random.randint(0, target.dfs // 2)
        target.hp -= damage
        print(f"{self.job}(이)가 {target.job}을 공격!")

        if target.hp < 0:
            target.hp = 0
        if damage < 0:
            damage = 0
        print(f"{damage}의 피해를 입혔습니다. 남은체력 : {target.hp}")

        if target.hp == 0:
            print(f"{target.job}의 체력이 0이 되었습니다.")


class Programmer(Unit):
    def __init__(self, job, hp, atk, dfs, luk):
        super().__init__(job, hp, atk, dfs, luk)

        self.hp += self.get_lucky_weight()
        self.atk += self.get_lucky_weight()
        self.dfs += self.get_lucky_weight()
        self.MAX_HP = self.hp

    def heal(self):
        heal_hp = self.get_lucky_weight()
        self.hp += heal_hp

        if self.hp > self.MAX_HP:
            self.hp = self.MAX_HP

        print(f"hp를 {heal_hp}만큼 회복했습니다. 현재 hp : {self.hp}")

    def __str__(self):
        return f"직업 : {self.job}, 체력 : {self.hp}, 공격력 : {self.atk}, 방어력 {self.dfs}, 행운 : {self.luk}"


class Monster(Unit):
    def __init__(self, job, hp, atk, dfs, luk):
        super().__init__(job, hp, atk, dfs, luk)


class BattleEndException(Exception):
    pass


class Game:
    job_dict = {
        "1": ["서버개발자", 200, 10, 150, 50],
        "2": ["클라이언트개발자", 150, 200, 100, 50],
        "3": ["데이터사이언티스트", 100, 150, 150, 70],
        "4": ["인공지능개발자", 130, 130, 130, 130],
    }

    monsters = [
        ["슬라임", 30, 50, 50, 0],
        ["고블린", 100, 70, 80, 30],
        ["오크", 200, 100, 200, 10],
        ["늑대", 140, 150, 100, 50],
        ["다크엘프", 140, 300, 200, 100],
    ]

    def create_character(self):
        print("[캐릭터 생성하기]")
        print("[1] 서버개발자 [2] 클라이언트개발자 [3] 데이터사이언티스트 [4] 인공지능개발자 [그외] 평민")
        job = input("직업을 선택하세요 : ")

        if job not in "1234":
            return Unit("평민", 100, 100, 100, 100)
        return Programmer(*self.job_dict[job])

    def battle(self, user, monster):
        # inner function inner method
        def battle_user():
            menu = input("[1] 공격 [2] 회복 : ")
            if menu == "1":
                user.attack(monster)
            else:
                user.heal()
            if monster.hp == 0:
                print(f"{monster.hp} 몬스터를 물리쳤습니다.")
                raise BattleEndException("[전투종료] 쉼터로 돌아갑니다.")

        def battle_monster():
            monster.attack(user)
            if user.hp == 0:
                raise BattleEndException("[전투종료] 유저가 전투불가 상태가 되어 쉼터로 귀환합니다.")

        first_attack = random.choice([1, 2])
        while True:
            try:
                if first_attack == 1:
                    battle_user()
                    battle_monster()
                else:
                    battle_monster()
                    battle_user()
            except BattleEndException as err:
                print(err)
                break

    def go_dungeon(self, user):
        print("던전에 입장합니다.")
        monster_stat = random.choice(self.monsters)
        print(monster_stat)
        monster = Monster(*monster_stat)

        print("[1] 전투 [2] 도망")
        menu = input("행동을 선택해주세요 : ")
        if menu == "1":
            self.battle(user, monster)
        else:
            print("도망쳤습니다.")

    def run(self):
        intro_txt = """
프로그래머 지망생들이 살고 있는 마을에 던전이 생성 되었습니다...
특이하게도 이 던전에는 프로그래머만 들어갈 수 있으며, 
디지털 몬스터와 키보드로 배틀을 하게 된다고 합니다.
던전을 탐험하고 귀한 아이템을 손에 얻으세요!\n"""

        for c in intro_txt:
            print(c, end="")
            time.sleep(.05)

        user = self.create_character()
        print(f"<{user.job}을 생성하였습니다.>")
        print(user)
        while True:
            print("=======================")
            print("[1] 던전탐험 [2] 휴식")
            menu = input("메뉴를 선택해주세요 : ")
            print("\n==================")

            if menu == "1":
                self.go_dungeon(user)
            elif menu == "2":
                user.heal()


if __name__ == '__main__':
    Game().run()
