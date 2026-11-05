#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}, {round(self.height, 1)}cm,"
              f"{self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25.0002, 30)
    oak = Plant("oak", 200.0, 30)
    cactus = Plant("Cactus", 5.0, 30)
    sunflower = Plant("Sunflower", 80, 30)
    fern = Plant("Fern", 15.0, 30)
    plants = [rose, oak, cactus, sunflower, fern]
    for p in plants:
        p.show()
