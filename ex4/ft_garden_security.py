#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        self.height = 25.0
        if height < 0:
            return print("Error, height can't be negative")

    def set_age(self, age):
        self.age = 30
        if age < 0:
            return print("Error, age can't be negative")

    def get_age() -> int:
        return 
            
    def show(self) -> None:
        h = round(self.height, 1)
        print(f"Height Updated: {round(self.height, 1)}cm")
        print(f"Age Updated: {round(self.age, 1)} days")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    in_name = "rose"
    in_height = 15.0
    in_age = 10
    print(f"Plant created: {in_name}, {in_height}cm, {in_age} days old")
    rose = Plant(in_name, in_height, in_age)
    rose.show()