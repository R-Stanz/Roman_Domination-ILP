def generate_index_label(index):
    if (ord('a') + index <= ord('z')):
        return chr(ord('a') + index)
    elif (ord('A') + index <= ord('Z')):
        return chr(ord('A') + index)
    else:
        return 'Z' + generate_index_label(index - 50)
