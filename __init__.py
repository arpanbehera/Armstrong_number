#input_number = input("Provide the number:")
input_number = 647
list_digit = str(647)
sum = 0
for x in list_digit:
    sum += int(x)*int(x)*int(x)

if sum == int(input_number):
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong number")


