
def remove_last_comma(str):
    index = str.find(",", -1)
    list_str = list(str)
    list_str.pop(index)
    str = "".join(list_str)
    return str