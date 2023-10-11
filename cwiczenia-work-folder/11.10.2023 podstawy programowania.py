print("Siema")
def cw6():
    print("50",type(50))
    print("149.17",type(149.17))
    print("4*7",type(4*7))
    print("Krakow University of Economics",type(""))
    print("True",type(True))
    print("2>5",type(2>5))

def cw7():
    print("a",3-2+1)
    print("b",5+10*5)
    print("c",4+4/2**2)
    print("d",4%3%2%1)
    print("e",1+2%3**4*5)
    print("f",True!=False)

def cw8():
    number1 = 71
    number2 = 14
    result = number1 + number2
    print("Number 1: ", number1)
    print("Number 2: ", number2)
    print("The result of summation: ", result)

def cw9():
    n1,n2,n3,n4,n5 = 5,1,8,6,3
    print("suma wszystkich wartosci wynosi: ", n1+n2+n3+n4+n5)
    print("suma kwadratów liczb wynosi: ",n1**2+n2**2+n3**2+n4**2+n5**2)
    print("iloraz liczb n3 i n5 wynosi: ",n3*n5)
    if n3==n4:
        print("True")
    else:
        print("False")

def cw10():
    name,age,height = "Jakub",20,195
    print(f"My name is {name}, I am {age} years old, and my height is {height} cm. In 6 years I will be {age+6} years old.")

def cw11():
    father_income = int(input("Enter father's income: "))
    mother_income = int(input("Enter mother's income: "))
    family_size = int(input("Enter number of people in family: "))
    total_income = father_income+mother_income
    income_per_capita = total_income/family_size
    print(f"Total income: {total_income}")
    print(f"Income per person: {income_per_capita}")

def cw12():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last surname: ')
    full_name = first_name + ' ' + last_name
    print(f'Your fullname is {full_name}')

def  cw13():
    cube_s = int(input("Enter cube side: "))
    print(f"The surface area of a cube with side {cube_s} is {cube_s**2*6}")

def cw14():
    pi=3.14
    circle_radius=5
    print(f"Area of the circle equals {pi*circle_radius**2}")
    print(f"Circumference of circle is {2*pi*circle_radius}")

def cw15():
    temp_c=int(input("Temperatura w stopniach Celsjusza: "))
    temp_f = 32+temp_c*5/9
    print(f"The temperature in Fahrenheit is {temp_f}")

def cw18():
    x = 7
    y = 34
    z = 0
    z = x
    x = y
    y = z
    print(x,y)

