class Cube:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def square(self):
        return self.side_length ** 2

def compare_cubes(cube1, cube2):
    if cube1.square() > cube2.square():
        return "1шысы улкен."
    elif cube1.square() < cube2.square():
        return "2шысы улкен"
    else:
        return "тен"


side_length1 = float(input("быр: "))
side_length2 = float(input("екы "))


cube1 = Cube(side_length1)
cube2 = Cube(side_length2)
