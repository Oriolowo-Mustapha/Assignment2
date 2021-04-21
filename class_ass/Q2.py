class Student:
    def __init__(self, name: str, roll_number: int, address: str, phone_number: int):
        self.name = name
        self.roll_number = roll_number
        self.address = address
        self.phone_number = phone_number

s1 = Student("Sam", 2, "asero", "07048575749")
s2 = Student("John", 3, "ibadan", "0904844766473")
print(s1.name, s1.roll_number, s1.address, s1.phone_number)
print(s2.name, s2.roll_number, s2.address, s2.phone_number)