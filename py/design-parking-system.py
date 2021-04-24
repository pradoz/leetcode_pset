from typing import List

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spots = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:
        if self.spots[carType] > 0:
            self.spots[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)





def run_test() -> None:
    sol = ParkingSystem(1, 1, 0)
    print(sol.addCar(1))
    print(sol.addCar(2))
    print(sol.addCar(3))
    print(sol.addCar(1))



def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
