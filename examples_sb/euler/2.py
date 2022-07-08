from sb import *


start()

push(value=1, stack=1)
push(value=2, stack=1)
create_stack(stack=2)

push(value=2, stack=2)

# 2 5 5
while True:
    duplicate_top(stack=1)
    rotate(stack=1)
    m_add(stack=1)
    duplicate_top(stack=1)
    push(value=4_000_000, stack=1)
    co_gt(stack=1)
    if pop(stack=1):
        break
    else:
        duplicate_top(stack=1)
        push(value=2, stack=1)
        m_mod(stack=1)
        push(value=0, stack=1)
        co_eq(stack=1)
        if pop(stack=1):
            duplicate_top(stack=1)
            move_top(from_stack=1, to_stack=2)

while stack_length(stack=2) != 1:
    m_add(stack=2)

print(pop(stack=2))


pop(stack=1)
pop(stack=1)

end()
