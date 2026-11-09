#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 23, 2)
    sunflower = Plant("Sunflower", 80, 2)
    cactus = Plant("Cactus", 50, 2)
    rose.show()
    sunflower.show()
    cactus.show()
