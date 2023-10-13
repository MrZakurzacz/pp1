import random as ran
import math

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
    x,y = y,x
    print(x,y)

def cw19():
    a = 4
    print(f"Side of the cube equals {a}. The Cube's volume equals {a**3} and the Cube's surface total area equals {a**2*6}")
def cw20():
    a = 17
    b = 5
    print(f"Division result: {a//b}, the remainder is {a%b}")

def cw21():
    height_n = 195
    height_am = height_n * 0.393701 # inches total
    height_am_inch = round((height_am * 0.083 - int(height_am * 0.083)) * 12, 2) #inches rest
    height_am_feet = int(height_am * 0.083) # feet
    print(f"I am {height_n}cm tall, i.e. {height_am_feet} feet and {height_am_inch} inches")

def cw22():
    a,b = 3,5
    print(f"{a} - {b} = {a-b}")

def cw23():
    area=0
    while area == 0:
        a = float(input("One side of the triangle: "))
        b = float(input("Second side of the triangle: "))
        c = float(input("Third side of the triangle: "))
        s = (a + b + c) / 2  # semiperimeter
        circumference = a + b + c  # cicumference of the triangle
        area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5,2)
        if area == 0:
            print("The triangle is invalid, it couldn't exist with the mentioned lengths, please provide proper information")
    print(f"Triangle area is equal to {area}")
    print(f"Triangle circumference is equal to {circumference}")

def cw24():
    plate = input("Enter vechicle registration number: ")
    plate = plate.upper()
    state = "KR" in plate or "KK" in plate
    print(f"Car from Krakow: {state}")

def cw25():
    age = int(input("Enter age: "))
    print(f"Exemption from paying taxes: {age<=26}")

def cw26():
    number = int(input("Enter number: "))
    print(f"Number is even: {number%2 == 0}")

def cw27():
    number = int(input("Enter number: "))
    number_range = [-10,10]
    print(f"Number in the range <-10, 10>: {min(number_range)<=number<=max(number_range)}")

def cw28():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter you weight in kg: "))
    BMI_index = round(weight/(height/100)**2,1)
    print(f"Correct weight: {18.4<BMI_index<25}")

def cw29():
    roll1, roll2, roll3 = ran.randint(1,6), ran.randint(1,6), ran.randint(1,6)
    print(f"first roll {roll1}, second roll {roll2}, third roll {roll3}, sum of all rolls is {roll1+roll2+roll3}")

def cw29a():
    rolls = [ran.randint(1,6) for _ in range(3)]
    print(f"first roll {rolls[0]}, second roll {rolls[1]}, third roll {rolls[2]}, sum of all rolls is {sum(rolls)}")

def cw30():
    rolled_num = ran.randint(1,6)
    print(rolled_num)
    print(f"Special number: {rolled_num == 1 or rolled_num == 6}")

def cw31():
    rolled_num = ran.randint(1,6)
    guessed_num = int(input(f"Guess the number i have rolled!: "))
    if rolled_num == guessed_num:
        print(f"You have bested me! The number was indeed {rolled_num}")
    else:
        print(f"Better luck next time! The number was {rolled_num}!")

def cw32():
    paid = float(input("Amount paid: "))
    vat = round(paid*0.23,2)
    print(f"The paid amount was {paid} the included VAT was {vat}")

def cw33():
    psw = input("Please enter your password: ")
    print(f"Password is valid: {len(psw)>=8}")

def cw34():
    speed = int(input("Please enter vechicle speed: "))
    print(f"Speed is valid: {40<=speed<=140}")

def cw35():
    tree_circ = float(input("Please enter tree circumference: "))
    print(f"Tree can be cut down: {tree_circ / math.pi >= 50}")

def cw36():
    buy = float(input("EUR buy rate: "))
    sell = float(input("EUR sell rate: "))
    print(f"Spread: {round(sell-buy,4)}")

def cw37():
    #nie chce mi sie kurwa nie lubie slicowania

def cw38():
    #znowu slicing

def cw39():







