class calculator:
    
    def __init__(self):
        self.numberone= float(input("Enter first number:: "))
        self.numbertwo= float(input("Enter second number:: "))
        print ("1. Divide")
        print ("2. Multiply")
        print ("3. Addition")
        print ("4. Subtract")
        self.choice =input("Your choice::")
    def div(self):
        divide = self.numberone / self.numbertwo
        return divide
    
    def mul(self):
        multiply = self.numberone * self.numbertwo
        return multiply
    
    def add(self):
        addition = self.numberone + self.numbertwo
        return addition
    
    def sub(self):
        subtraction = self.numberone - self.numbertwo
        return subtraction

while True:
    cal = calculator()
    if cal.choice == "1":
        print(cal.div())
    elif cal.choice == "2":
        print(cal.mul())
    elif cal.choice == "3":
        print(cal.add())
    elif cal.choice == "4":
        print(cal.sub())
    else:
        print("Invalid")
    cont = input("Do you want to continue? (y/n): ")
    while cont.lower() not in ["y", "n"]:
        cont = input("Invalid input. Do you want to continue? (y/n): ")
    if cont.lower() == "n":
        break
    elif cont.lower() == "y":
        print(" ok.....")
    else:
        print("Invalid Input....")