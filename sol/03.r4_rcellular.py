def right(state, idx, i):
    return 0 if idx + i >= len(state) else state[idx + i]


def local(state, idx):
    return (state[idx], right(state, idx, 1), right(state, idx, 2))


def cellular_in_situ(state: list[int]):
    for i in range(len(state)):
        config = local(state, i)
        if config == (1, 0, 0):
            state[i] = 0
        elif config == (0, 1, 0):
            state[i] = 1
        elif config == (0, 1, 1):
            state[i] = 1
        elif config == (1, 0, 1):
            state[i] = 0
        elif config == (1, 1, 1):
            state[i] = 0
