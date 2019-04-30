searchName(NAME, STACK)
    DEPTH = 0
    NAMEDEPTH = -1
    while not STACK.isEmpty() do
    X = STACK.pop()
    if X == NAME
        then NAMEDEPTH=DEPTH
            DEPTH = DEPTH + 1
            end while
    if NAMEDEPTH == -1
        then output(NAME + ’not found’)
    else output(NAMEDEPTH)
    endif
end searchName

#benefits of binary search
# 1. takes less time
# 2. less memory since structured
