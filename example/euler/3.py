from sb import *

start()
push(value=600851475143, stack=1)  # num to get factors
push(value=1, stack=1)      # factor

create_stack(stack=2)       # index
push(value=0, stack=2)

# 1 (1 == 10)
while True:
    increment_top(stack=2)

    duplicate_top2(stack=1)
    m_mod(stack=1)
    push(value=0, stack=1)
    co_eq(stack=1)
    if pop(stack=1):

        duplicate_top(stack=1)
        rotate(stack=1)
        swap(stack=1)
        m_div(stack=1)
        push(value=int(pop(stack=1)), stack=1)
        swap(stack=1)
        pop(stack=2)
        push(value=0, stack=2)
    increment_top(stack=1)

    duplicate_top(stack=2)
    push(value=1000, stack=2)
    co_eq(stack=2)
    if pop(stack=2):
        pop(stack=2)
        pop(stack=1)
        print(pop(stack=1))
        break

end()
