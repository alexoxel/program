import random
class Tiger:
    def __init__(self):
        self.state = "выследить добычу"
        self.successful_attack = 0.5
        self.x, self.y = 0, 0
    def update_state(self, hares):
        if self.state == "выследить добычу":
            print("тигр выслеживает добычу")
            self.move_random()
            if any (self.is_near_hare(hare) for hare in hares):
                self.state = "атаковать добычу"
        elif self.state == "атаковать добычу":
            if random.random()<self.successful_attack:
                print("Тигр успешно атаковал зайца")

                for hare in hares:
                    if self.is_near_hare(hare):
                        hare.to_captured()
                self.state = "бежать домой"
            else:
                print("тигр промахнулся")
        elif self.state == "бежать домой":
            self.x, self.y = 0,0
    def move_random(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(self.x, 4))
        self.y = max(0, min(self.y, 4))
    def is_near_hare(self, hare):
        return abs(self.x - hare.x) <= 1 and abs(self.y - hare.y) <= 1
    def __str__(self):
        return f"тигр:({self.x}, {self.y})"
class Hare:
    def __init__(self, x, y):
        self.x, self.y =x, y
        self.captured = False
    def to_captured(self):
        self.captured = True
    def __str__(self):
        return f"заяц:({self.x}, {self.y})"

def print_field(tiger, hares):
    field = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(".")
        field.append(row)
    field[tiger.x][tiger.y] ="Т"
    for hare in hares:
        if not hare.captured:
            field[hare.x][hare.y] ="З"
    for row in field:
        print(" ".join(row))
    print()

def main():
    tiger = Tiger()
    hare1 = Hare(random.randint(1,4),random.randint(1,4))
    hare2 = Hare(random.randint(1,4),random.randint(1,4))
    hares = [hare1, hare2]
    while tiger.state != "бежать домой":
        print(tiger)
        for hare in hares:
            print(hare)
        print_field(tiger, hares)
        tiger.update_state(hares)
    print(tiger)
    for hare in hares:
        print(hare)
    tiger.update_state(hares)
    print_field(tiger, hares)
    if tiger.state == "бежать домой":
        print("тигр вернулся домой")

if __name__ == "__main__":
    main()