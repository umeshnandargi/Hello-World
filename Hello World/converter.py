class Converters():
    def __init__(self, wt):
        self.wt = wt

    def kg_to_lbs(self):
        return str(self.wt / 0.45) + " lbs"

    def lbs_to_kg(self):
        return str(self.wt * 0.45) + " kg"


a = input("enter 'k' for kg or 'l' for lbs for input weight: ")
con = Converters(int(input('Enter weight: ')))
# print(con.wt)
if a == "k":
    print(con.kg_to_lbs())
elif a == "l":
    print(con.lbs_to_kg())
else:
    print("sorry wrong input")
