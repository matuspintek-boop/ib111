

def lakes(land: list[nat]) -> int:
    water = 0

    # the stack holds the left edges of currently "open" basins
    stack: list[int] = []

    for i in range(len(land)):
        height = land[i]

        bottom = 0
        # closing the basins
        while stack and height >= land[stack[-1]]:
            water += (i - stack[-1] - 1) * (land[stack[-1]] - bottom)
            bottom = land[stack[-1]]
            stack.pop()

        if stack:
            water += (i - stack[-1] - 1) * (height - bottom)

        stack.append(i)

    return water
