a= int(input("podaj pierwszą długość trójkąta"))
b= int(input("podaj drugą długość trójkąta"))
c= int(input("podat trzecią długość trójkąta"))
if a+b>c and a+c>b and b+c>a:
    print("Można zrobić z tego trójkąt")
else:
    print("nie da się zrobić trójkąt")
