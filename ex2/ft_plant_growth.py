#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow(self):
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.age} days old")
        for i in range(7):
            self.height += 0.8
            self.age += 1
            self.show(i)

    def show(self, i):
        print(f"=== Day {i+1} ===")
        print(f"{self.name}: "
              f"{round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.grow()
