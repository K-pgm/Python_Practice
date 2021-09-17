class Car:
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f"{self.model_name}: {self.mileage}")

    def breaks(self):
        print(f"{self.manufacturer}")


if __name__ == "__main__":
    stepwagon = Car("stepwagon", 50, "トヨタ")
    stepwagon.gas()
    stepwagon.breaks()
