from bfbnr import *

init()

move_pointer(loc=1)
store(value=1)
move_pointer(loc=2)
store(value=2)

for _ in range(100):
    move_pointer(loc=3)
    store(value=read_loc(loc=1) + read_loc(loc=2))
    move_pointer(loc=1)
    store(value=read_loc(loc=2))
    print(read())
    move_pointer(loc=2)
    store(value=read_loc(loc=3))

