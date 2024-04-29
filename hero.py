class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def get_name(self):
        return self.name
    def double_health_points(self):
        self.health_points *= 2
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)
if __name__ == "__main__":
    hero = SuperHero("The Flash", "Barry Allen", "Moving faster than the speed of light.", 200, "If you don't move, then you don't live.")
    hero_name = hero.get_name()
    print("Hero's name:", hero_name)
    print("Health points before doubling:", hero.health_points)
    hero.double_health_points()
    print("Health points after doubling:", hero.health_points)
    print(hero)
    print("Length of catchphrase:", len(hero))