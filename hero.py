class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def get_name(self):
        return self.name
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True
    def print_true_phrase(self):
        print("True in the True_phrase")
class SkywrathMage(SuperHero):
    location = "Air"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True
    def crit(self):
        return self.damage ** 2
class Earthshaker(SuperHero):
    location = "Earth"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True
    def crit(self):
        return self.damage ** 2
class Invoker(SuperHero):
    location = "Space"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True
    def crit(self):
        return self.damage ** 2
class ShadowFiend(SuperHero):
    people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
    def gen_x(self):
        pass
    def crit(self, target):
        return target.damage ** 2
if __name__ == "__main__":
    skywrath_mage = SkywrathMage("Skywrath Mage", "Dragonus", "Arcane Bolts and Concussive Shots", 120, "By my wings!", 25)
    earthshaker = Earthshaker("Earthshaker", "Raigor Stonehoof", "Echo Slam and Fissure", 180, "The earthshakes beneath my feet!", 35)
    invoker = Invoker("Invoker", "Carl", "Invoke and various spells", 200, "Quas Wex Exort!", 40)
    shadow_fiend = ShadowFiend("Shadow Fiend", "Nevermore", "Necromastery and Requiem of Souls", 150, "Your soul is mine!", 30)

    skywrath_mage.double_health_points()
    earthshaker.double_health_points()
    invoker.double_health_points()

    print(f"Name: {skywrath_mage.name}, Nickname: {skywrath_mage.nickname}, Superpower: {skywrath_mage.superpower}, Health Points: {skywrath_mage.health_points}, Catchphrase: {skywrath_mage.catchphrase}")
    print(f"Name: {earthshaker.name}, Nickname: {earthshaker.nickname}, Superpower: {earthshaker.superpower}, Health Points: {earthshaker.health_points}, Catchphrase: {earthshaker.catchphrase}")
    print(f"Name: {invoker.name}, Nickname: {invoker.nickname}, Superpower: {invoker.superpower}, Health Points: {invoker.health_points}, Catchphrase: {invoker.catchphrase}")
