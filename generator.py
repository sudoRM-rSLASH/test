lists = [
    ["None", "list", "int", "bool", "tuple", "dict"],
    [0, 1, 2, 3, 4],
    ["Red", "Green", "Blue"],
]


def generate(data: list[list], variant: int):
    output = []
    for list_ in data:
        if variant > len(list_):
            index = variant % len(list_) - 1
            output.append(list_[index])
        else:
            output.append(list_[variant - 1])
    return output


print(generate(lists, 761))
