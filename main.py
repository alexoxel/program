import random
class Tiger:
    def __int__(self):
        self.state = "выследить добычу"
        self.successful_attack = 0.5
        self.x, self.y = 0, 0
    def update_state(self, hares):
        if self.state == "выследить добычу":
            print("тигр выслеживает добычу")