# brain fudge but not really


strip = []
pointer = 0


def error(body):
    print(f"Error: {body}")
    exit(1)


def init(strip_size: int = 10000):
    global strip
    strip = [0 for _ in range(strip_size)]


def move_pointer(loc: int):
    global pointer
    if loc < 0:
        error("pointer cannot move to negatives")
    elif loc > len(strip):
        error("pointer cannot move to higher than strip length")

    pointer = loc


def read():
    return strip[pointer]


def print_pointed():
    print(strip[pointer])


def print_pointed_as_char():
    print(chr(strip[pointer]))


def store(value: int):
    strip[pointer] = value


def increment_pointed():
    strip[pointer] += 1


def decrement_pointed():
    strip[pointer] -= 1


def read_loc(loc: int):
    move_pointer(loc=loc)
    return read()


def print_string(string: str = ""):
    move_pointer(loc=0)
    for s in string:
        store(ord(s))
        print(chr(strip[pointer]), end="")
        store(0)


def println_string(string: str = ""):
    print_string(string=string)
    print()




