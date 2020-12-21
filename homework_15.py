# 1
class Weapon:
    def __init__(self, name, damage, a_range):
        self.name = name
        self.damage = damage
        self.a_range = a_range

    def hit(self, actor, target):
        if target.is_alive():
            c1 = actor.get_coords()
            c2 = target.get_coords()
            distance = ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
            if self.a_range >= distance:
                print(f"target is too far for weapon {self.name}")
            else:
                print(f"enemy was hit from weapon {self.name} damage is {self.damage}")
                target.get_damage(actor.current_weapon.damage)
        else:
            print("the enemy is already defeated")

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        if self.hp <= amount:
            self.hp = 0
        else:
            self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.current_weapon = weapon
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if isinstance(target, MainHero):
            self.current_weapon.hit(self, target)
        else:
            print("i can hit only main hero")

    def __str__(self):
        return f"“enemy is in the position ({self.pos_x}, {self.pos_y}) with weapon {self.current_weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        self.name = name
        self.weapon = []
        self.current_weapon = None
        self.max_hp = 200
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if not self.weapon:
            print("i with weapon")
        elif isinstance(target, BaseEnemy):
            self.current_weapon.hit(self, target)
        else:
            print("i can hit only enemy")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            print(f"picked up {weapon}")
            if not self.current_weapon:
                self.current_weapon = weapon
                self.weapon += [weapon]
            else:
                self.weapon += [weapon]
        else:
            print("it’s not a Weapon")

    def next_weapon(self):
        if not self.current_weapon:
            print("i am unarmed")
        elif len(self.weapon) == 1:
            print("i have one weapon")
        else:
            self.current_weapon += 1
            if self.current_weapon >= len(self.weapon):
                self.current_weapon = 0
            print(f"i take weapon {self.weapon[self.current_weapon]}")

    def heal(self, amount):
        if self.hp + amount >= self.max_hp:
            self.hp = 200
        else:
            self.hp += amount
        print(f"now my health is hp {self.hp}")

# 2


def nums(n):
    for i in range(1, n + 1):
        print(i, end="")


nums(13)
