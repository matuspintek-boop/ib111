def subseq(seq: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    candidates: list[list[int]] = [[]]
    subseq_rec(seq, 0, candidates)

    for candidate in sorted(candidates):
        if not res or res[-1] != candidate:
            res.append(candidate)

    return res


def subseq_rec(seq: list[int],
               curr_pos: int,
               res: list[list[int]]) -> None:
    assert curr_pos >= 0 and curr_pos <= len(seq)

    if curr_pos == len(seq):
        return

    to_add = []
    for curr_seq in res:
        if len(curr_seq) == 0 or curr_seq[-1] <= seq[curr_pos]:
            if len(curr_seq) + 1 != len(seq):
                new_seq = curr_seq.copy()
                new_seq.append(seq[curr_pos])
                to_add.append(new_seq)

    res.extend(to_add)
    subseq_rec(seq, curr_pos + 1, res)
