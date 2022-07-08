from bfbnr import *
import random

init()

move_pointer(loc=2)
store(random.randint(0, 100))

move_pointer(loc=1)
store(value=int(input("number between 1- 100 > ")))

while read_loc(loc=2) != read_loc(loc=1):
    if read_loc(loc=2) > read_loc(loc=1):
        println_string("higher")
    elif read_loc(loc=2) < read_loc(loc=1):
        println_string("lower")
    else:
        break

    move_pointer(loc=1)
    store(value=int(input("number between 1- 100 > ")))

print_string("the number was ")
move_pointer(loc=2)
print_pointed()
