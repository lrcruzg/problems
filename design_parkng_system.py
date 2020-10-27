
# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.number_of_parking_spaces = [big, medium, small]
    
    # carType
    # 1 -> big
    # 2 -> medium
    # 3 -> small
    def addCar(self, carType: int) -> bool:
        if not self.number_of_parking_spaces[carType - 1]:
            return False
        self.number_of_parking_spaces[carType - 1] -= 1
        return True
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)