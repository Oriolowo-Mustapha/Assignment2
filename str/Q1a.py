string_input = str(input("Enter string to be manupulated: "))
string = string_input
lenght = len(string_input)
mol = lenght % 2
if mol == 0:
    vl = int(lenght / 2)
    first = string_input[:vl]
    second = string_input[vl:]
    print(first, second)
elif mol > 0:
    print("Your variable length is odd")