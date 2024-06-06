class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage


modelX = Vehicle(230, 20)
print(modelX.maxspeed, modelX.mileage)
    