#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 23, 2)
    sunflower = Plant("Sunflower", 80, 2)
    cactus = Plant("Cactus", 50, 2)
    rose.show()
    sunflower.show()
    cactus.show()
