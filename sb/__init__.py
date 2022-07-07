global_stack = {}


def error(body):
    print(f"Error: {body}")
    exit(1)


def push(value, stack):
    if stack < 1:
        error("Cannot push to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    global_stack[stack].append(value)


def pop(stack):
    if stack < 1:
        error("Error: Cannot pop to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) == 0:
        error(f"Stack {stack} doesnt have items")

    return global_stack[stack].pop()


def create_stack(stack):
    if stack < 1:
        error("Error: Cannot create stacks lower than 1")
    elif stack in global_stack:
        error(f"Re create of Stack {stack} which exist")
    global_stack[stack] = []


def duplicate_top(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) == 0:
        error(f"Stack {stack} doesnt have items")
    dup = global_stack[stack].pop()
    global_stack[stack].append(dup)
    global_stack[stack].append(dup)


def compare_eq(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)
    result = v_1 == v_2
    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)
    # push(value=result, stack=stack)
    return result


def compare_neq(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)
    result = v_1 != v_2
    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)
    # push(value=result, stack=stack)
    return result


def compare_gt(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)

    result = v_2 > v_1

    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)

    # push(value=result, stack=stack)
    return result


def compare_gt_eq(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)
    result = v_2 >= v_1
    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)
    # push(value=result, stack=stack)
    return result


def compare_lt(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)

    result = v_2 < v_1

    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)
    # push(value=result, stack=stack)
    return result


def compare_lt_eq(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < 2:
        error(f"Stack {stack} doesnt enough items items")

    v_1 = pop(stack=stack)
    v_2 = pop(stack=stack)
    result = v_2 <= v_1
    push(value=v_2, stack=stack)
    push(value=v_1, stack=stack)
    # push(value=result, stack=stack)
    return result


def end():
    for name, stack in global_stack.items():
        if len(stack) > 0:
            error(f"Error: unhandled data for stack {name}")


def print_top(stack):
    duplicate_top(stack=stack)
    print(pop(stack=stack))


def start():
    create_stack(1)
