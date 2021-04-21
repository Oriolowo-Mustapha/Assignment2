class Area:
    def __init__(self, length: int, breath: int):
        self.length = length
        self.breath = breath

    def returnArea(self):
        area = self.length * self.breath
        print(area)