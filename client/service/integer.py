def get_norm_form(count: int, one: str, mid: str, large: str):
    units = count % 10
    if 4 < units < 10 or 10 < count < 21 or units == 0:
        return f"{count} {large}"
    elif 1 < units < 5:
        return f"{count} {mid}"
    return f"{count} {one}"
