
def remove_last_comma(str):
    index = str.find(",", -1)
    list_str = list(str)
    list_str.pop(index)
    str = "".join(list_str)
    return str


# convert waapi data to sqlite data
def data_convert(waapi_data):
    ret = []
    for key, value in waapi_data.items():
        if isinstance(value, type(True)):
            new_value = int(value)
            ret.append(new_value)
            continue
        elif isinstance(value, type({})):
            new_value = value.get("id")
            ret.append(new_value)
            continue
        elif isinstance(value, type([])):
            new_value = ""
            for v in value:
                new_value += v.get("id")
                new_value += ","
            new_value = remove_last_comma(new_value)
            ret.append(new_value)
            continue
        else:
            ret.append(value)
    
    return ret