from sb import *

start()

push(value=1, stack=1)
print_top(stack=1)
push(value=2, stack=1)

for _ in range(100):  # loop 10 times
    print_top(stack=1)
    duplicate_top(stack=1)
    rotate(stack=1)
    m_add(stack=1)

print_top(stack=1)
pop(stack=1)
pop(stack=1)
end()
