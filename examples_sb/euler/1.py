from sb import *

start()

# sd = []
# for i in range(9999):
#     i += 1
#     if i % 3 == 0 or i % 5 == 0 and i not in sd:
#         sd.append(i)
#
# print(sum(sd))

push(value=1, stack=1)
create_stack(stack=2)
for _ in range(9998):
    duplicate_top(stack=1)
    push(1, stack=1)
    m_add(stack=1)


def is_multiple_of():
    m_mod(stack=1)
    push(value=0, stack=1)
    co_eq(stack=1)


def is_multiple_3():
    push(value=3, stack=1)
    is_multiple_of()


def is_multiple_5():
    push(value=5, stack=1)
    is_multiple_of()


while stack_length(stack=1) != 0:
    duplicate_top(stack=1)
    is_multiple_3()
    if pop(stack=1):
        move_top(from_stack=1, to_stack=2)
        continue
    else:
        duplicate_top(stack=1)
        is_multiple_5()
        if pop(stack=1):
            move_top(from_stack=1, to_stack=2)
        else:
            pop(stack=1)

while stack_length(2) != 1:
    m_add(2)


print(pop(stack=2))
end()
