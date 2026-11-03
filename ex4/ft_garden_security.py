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
        print(f"Current state: {self._name}: {round(self._height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    in_name = "rose"
    in_height = 15.0
    in_age = 10
    rose = Plant(in_name, in_height, in_age)
    print(f"Plant created: {in_name.capitalize()}, {in_height}cm, {in_age} days old\n")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-20)
    print("")
    rose.show()
