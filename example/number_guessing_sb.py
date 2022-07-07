import random
from sb import *

start()  # init

push(value=random.randint(1, 100), stack=1)  # pushes a random number to stack 1
push(value=int(input("number between 1 - 100 > ")), stack=1)  # get input push to stack 1


while c_neq(stack=1):   # compares(item !=item) the top two item of stack 1
    if c_gt(stack=1):
        print("higher")
    elif c_lt(stack=1):
        print("lower")
    else:
        break
    pop(stack=1)
    push(value=int(input(" > ")), stack=1)  # get input push to stack 1
print(f"The number was {pop(stack=1)}")
pop(stack=1)

end()  # checks
