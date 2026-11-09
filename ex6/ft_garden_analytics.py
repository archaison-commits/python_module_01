#!/usr/bin/env python3

class Plant:

    class Statistics:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0
            self.__shade_calls = 0

        def grow_counter(self) -> None:
            self.__grow_calls += 1

        def age_counter(self) -> None:
            self.__age_calls += 1

        def show_counter(self) -> None:
            self.__show_calls += 1

        def shade_counter(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            print(f"Stats: {self.__grow_calls} grow, {self.__age_calls} age, {self.__show_calls} show")

        def display_shade(self) -> None:
            print("",self.__shade_calls, "shade")

    @staticmethod
    def check_age(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

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
        self._stats = self.Statistics()

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

    def age(self, aging) -> None:
        self._age += aging
        self._stats.age_counter()

    def grow(self, amount) -> None:
        self._height += amount
        self._stats.grow_counter()

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        self._stats.show_counter()

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self, to_bloom) -> None:
        self._to_bloom = to_bloom
        if self._to_bloom == "blooming":
            print(f" {self._name} is blooming beautifully! ")
        elif self._to_bloom == "not bloomed":
            print(f" {self._name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0
        self._to_bloom = "not bloomed"

    def bloom(self, to_bloom, seed_growing) -> None:
        self._to_bloom = to_bloom
        if self._to_bloom == "blooming":
            self._seeds += seed_growing

    def show(self) -> None:
        super().show()
        if self._to_bloom == "blooming":
            print(f" {self._name} is blooming beautifully! ")
        elif self._to_bloom == "not bloomed":
            print(f" {self._name} has not bloomed yet")
        print(f" Seeds: {self._seeds}")

class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"The {self._name} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide")
        self._stats.shade_counter()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

def display_statistics(plant):
    print(f"[statistics for {plant._name}]")
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print("Is 30 days more than a year? ->", Plant.check_age(30))
    print("Is 400 days more than a year? ->", Plant.check_age(400))
    print("")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.bloom("not bloomed")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.show()
    rose.bloom("blooming")
    display_statistics(rose)
    print("")
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    oak._stats.display_shade()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    oak._stats.display_shade()
    print("")
    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45 , "yellow")
    sunflower.show()
    sunflower.bloom("not bloomed", 0)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom("blooming", 42)
    sunflower.show()
    display_statistics(sunflower)
    print("")
    print("=== Anonymous")
    anonymous_plant = Plant.anonymous()
    anonymous_plant.show()
    display_statistics(anonymous_plant)


