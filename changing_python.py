
class Car():
    def __init__(self) -> None:
        self.wheels = 7
        self.speed = 0

    def accelarate(self, increase):
        self.speed += increase
        print(f"You have increased thew speed to {self.speed}")


print("Hello")