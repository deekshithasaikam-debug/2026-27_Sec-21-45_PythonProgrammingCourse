principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
amount = principal * (1 + rate / 100) ** time
compound_intrest = amount - principal - amount
print("Compound Intrest=",compound_intrest)