class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() #다중 상속 시 super를 사용하면 처음 상속 class만 호출 가능
        Unit.__init__(self)
        Flyable.__init__(self)
#드랍쉽
dropship = FlyableUnit()