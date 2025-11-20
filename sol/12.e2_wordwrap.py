def word_wrap(orig: str, max_line_len: int) -> str:
    chars = list(orig)
    cur_line_len = 0
    last_space = None

    for index in range(len(chars)):
        cur_line_len += 1

        if chars[index] == "\n":
            cur_line_len = 0

        if chars[index] == " ":
            last_space = index

        if cur_line_len > max_line_len:
            if last_space is not None:
                chars[last_space] = "\n"
                cur_line_len = index - last_space

    return "".join(chars)
