test_list = [-89, None, 56, 56.56, False]

def type_definition(el):
    for el in range(len(test_list)):
        print(type(test_list[el]))
    return

type_definition(test_list)