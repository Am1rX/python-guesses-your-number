import random
import time

time.sleep(0.5)
print("\n\n\n*imagine number between 10 - 100*")
time.sleep(0.5)
print("\nhelp:\nb = my number is bigger\nk = my number is smaller\nd = correct number !")
time.sleep(0.5)

num = random.randint(10,100)
a = 100
b = 10

print('is that your number ?? ((', num , '))\n')
time.sleep(0.5)
javab = input("b / k / d : ")
time.sleep(0.5)

while javab != 'd':
    if javab == 'b':
        b = num
        num = random.randint(b,a)
        print(num)
    elif javab == 'k':
        a = num
        num = random.randint(b,a)
        print(num)
    javab = input("b / k / d : ")

print("\n\noh wow i did it !!")

# Created By AMIRX
