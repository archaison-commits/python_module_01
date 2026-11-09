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

    def grow(self) -> None:
        self._height += 2.1

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
            print(f"{self._name} is blooming beautifully! ")
        elif self._to_bloom == "not bloomed":
            print(f"{self._name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        print("=== Tree")
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"The {self._name} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        print("=== Vegetable")
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = 0

    def age(self) -> None:
            self._age += 1
            self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 25.0, 30, "red")
    rose.show()
    rose.bloom("not bloomed")
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom("blooming")
    print("")
    oak = Tree("oak", 200.0, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    tomate = Vegetable("tomato", 5.0, 10, "april")
    tomate.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomate.grow()
        tomate.age()
    tomate.show()
