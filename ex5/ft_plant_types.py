#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self._name = name.capitalize()
        if height < 0 :
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        print("=== Flower")
        self._color = color
    
    def bloom(self, to_bloom) -> None:
        self._to_bloom = to_bloom
        if self._to_bloom == "blooming":
            print(f"Rose is blooming beautifully! ")
        elif self._to_bloom == "not bloomed":
            print(f"Rose has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        

class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        print("=== Tree")
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"The Oak now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

class Vegetable(Plant):
    def __init__(self, name, height, age, nutritional_value):
        super().__init__(name, height, age)
        print("=== Vegetable")
        self._nutritional_value = nutritional_value
        for i in range(self.age<30):
            self._height += 2.1
            self._age += 1
        print(f"{self._name}: {self._height}cm, d")
        self.harvest_season()

    def harvest_season(self, month) -> None:
        self._month = month
        print(f"Harvest season: {self._month}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 25.0, 30, "red")
    rose.show()
    rose.bloom("not bloomed")
    print("[Asking the rose to bloom]")
    rose.show()
    rose.bloom("blooming")
    print("")
    oak = Tree("oak", 200.0, 365, 5)
    oak.show()
    print("[Asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    tomate = Tree("tomato", 200.0, 365, 5)
    tomate.show()