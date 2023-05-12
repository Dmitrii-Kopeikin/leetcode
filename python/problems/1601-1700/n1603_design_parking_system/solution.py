class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            1: [big, 0],  # '1' - key for carType, 'big' - capacity, '0' - cars parked
            2: [medium, 0],
            3: [small, 0],
        }
        

    def addCar(self, carType: int) -> bool:
        parking = self.parking[carType]
        if parking[1] < parking[0]:
            parking[1] += 1
            return True
        return False
