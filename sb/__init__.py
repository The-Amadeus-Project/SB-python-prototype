global_stack = {}


def error(body):
    print(f"Error: {body}")
    raise


def push(value, stack):
    if stack < 1:
        error("Cannot push to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    global_stack[stack].append(value)


def move_top(from_stack, to_stack):
    for stack in [from_stack, to_stack]:
        if stack < 1:
            error("Error: Cannot pop to stacks lower than 1")
        elif stack not in global_stack:
            error(f"Stack {stack} doesnt exist")
    if len(global_stack[from_stack]) == 0:
        error(f"Stack {stack} doesnt have items")

    push(value=pop(stack=from_stack), stack=to_stack)


def pop(stack):
    if stack < 1:
        error("Error: Cannot pop to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) == 0:
        error(f"Stack {stack} doesnt have items")

    return global_stack[stack].pop()


def drop_all(stack):
    if stack < 1:
        error("Error: Cannot pop to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) == 0:
        error(f"Stack {stack} doesnt have items")

    global_stack[stack] = []


def stack_length(stack):
    if stack < 1:
        error("Error: Cannot pop to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")

    return len(global_stack[stack])


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


def duplicate_top2(stack):
    if stack < 1:
        error("Error: Cannot duplicate to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) == 0:
        error(f"Stack {stack} doesnt have items")
    dup = global_stack[stack].pop()
    dup2 = global_stack[stack].pop()
    global_stack[stack].append(dup2)
    global_stack[stack].append(dup)
    global_stack[stack].append(dup2)
    global_stack[stack].append(dup)


def _get_bare_items(stack, num):
    if stack < 1:
        error("Error: Cannot do Operations to stacks lower than 1")
    elif stack not in global_stack:
        error(f"Stack {stack} doesnt exist")
    elif len(global_stack[stack]) < num:
        error(f"Stack {stack} doesnt enough items items")

    items = []
    for _ in range(num):
        items.append(global_stack[stack].pop())
    return items


def _get_two_items(stack):
    return _get_bare_items(stack, 2)


def swap(stack):
    first, second = _get_bare_items(stack, 2)
    push(value=first, stack=stack)
    push(value=second, stack=stack)


def rotate(stack):
    first, second, third = _get_bare_items(stack, 3)
    push(value=second, stack=stack)
    push(value=first, stack=stack)
    push(value=third, stack=stack)


def co_eq(stack):
    top, before_top = _get_two_items(stack)
    result = top == before_top
    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)
    push(value=result, stack=stack)


def co_neq(stack):
    top, before_top = _get_two_items(stack)
    result = top != before_top
    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)
    push(value=result, stack=stack)
    # return result


def co_gt(stack):
    top, before_top = _get_two_items(stack)

    result = before_top > top

    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)

    push(value=result, stack=stack)
    # return result


def co_gt_eq(stack):
    top, before_top = _get_two_items(stack)

    result = before_top >= top
    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)
    push(value=result, stack=stack)
    # return result


def co_lt(stack):
    top, before_top = _get_two_items(stack)

    result = before_top < top

    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)
    push(value=result, stack=stack)
    # return result


def co_lt_eq(stack):
    top, before_top = _get_two_items(stack)

    result = before_top <= top
    # push(value=before_top, stack=stack)
    # push(value=top, stack=stack)
    push(value=result, stack=stack)
    # return result


def c_eq(stack):
    top, before_top = _get_two_items(stack)
    result = top == before_top
    push(value=before_top, stack=stack)
    push(value=top, stack=stack)
    # push(value=result, stack=stack)
    return result


def c_neq(stack):
    top, before_top = _get_two_items(stack)
    result = top != before_top
    push(value=before_top, stack=stack)
    push(value=top, stack=stack)
    # push(value=result, stack=stack)
    return result


def c_gt(stack):
    top, before_top = _get_two_items(stack)

    result = before_top > top

    push(value=before_top, stack=stack)
    push(value=top, stack=stack)

    # push(value=result, stack=stack)
    return result


def c_gt_eq(stack):
    top, before_top = _get_two_items(stack)

    result = before_top >= top
    push(value=before_top, stack=stack)
    push(value=top, stack=stack)
    # push(value=result, stack=stack)
    return result


def c_lt(stack):
    top, before_top = _get_two_items(stack)

    result = before_top < top

    push(value=before_top, stack=stack)
    push(value=top, stack=stack)
    # push(value=result, stack=stack)
    return result


def c_lt_eq(stack):
    top, before_top = _get_two_items(stack)

    result = before_top <= top
    push(value=before_top, stack=stack)
    push(value=top, stack=stack)
    # push(value=result, stack=stack)
    return result


def m_add(stack):
    top, before_top = _get_two_items(stack)
    result = before_top + top
    push(value=result, stack=stack)


def m_sub(stack):
    top, before_top = _get_two_items(stack)
    result = before_top - top
    push(value=result, stack=stack)


def m_mul(stack):
    top, before_top = _get_two_items(stack)
    result = before_top * top
    push(value=result, stack=stack)


def m_div(stack):
    top, before_top = _get_two_items(stack)
    result = before_top / top
    push(value=result, stack=stack)


def m_mod(stack):
    top, before_top = _get_two_items(stack)
    result = before_top % top
    push(value=result, stack=stack)


def end():
    for name, stack in global_stack.items():
        if len(stack) > 0:
            error(f"Error: unhandled data for stack {name} : {stack}")


def print_top(stack):
    duplicate_top(stack=stack)
    print(pop(stack=stack))


def print_stack(stack):
    if stack not in global_stack:
        error(f"Stack {stack} doesnt exist")

    print(global_stack[stack])


def increment_top(stack):
    [top] = _get_bare_items(stack=stack, num=1)
    top += 1
    push(value=top, stack=stack)


def start():
    create_stack(1)
