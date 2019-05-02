class ucenik():
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def sortDob(self, dob):
        print(dob)

test = ucenik(first_name="Dino", last_name="Filipović", dob=30)
print(test.first_name)
print(test.last_name)
#print(test.dob)
#test.sortDob(test.dob)