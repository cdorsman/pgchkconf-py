def ParseConfigFile(filename: str):
    contents = []]
    with open(filename) as fp:
        buffer_list = fp.readlines()

    # initialize two counter to check mismatch between "(" and ")"
    open_bracket_counter = 0
    close_bracket_counter = 0

    # whenever an element deleted from the list length of the list will be decreased
    decreasing_counter = 0

    for number in range(len(buffer_list)):

        # checking if the line contains "#" or not
        if "#" in buffer_list[number-decreasing_counter]:

            # delete the line if startswith "#"
            if buffer_list[number-decreasing_counter].startswith("#"):
                buffer_list.remove(buffer_list[number-decreasing_counter])
                decreasing_counter += 1

            # delete the character after the "#"
            else:
                newline = ""
                for character in buffer_list[number-decreasing_counter]:
                    if character == "(":
                        open_bracket_counter += 1
                        newline += character
                    elif character == ")":
                        close_bracket_counter += 1
                        newline += character
                    elif character == "#" and open_bracket_counter == close_bracket_counter:
                        break
                    else:
                        newline += character
                buffer_list.remove(buffer_list[number-decreasing_counter])
                buffer_list.insert(number-decreasing_counter,newline)

    # remove empty items
    for i in buffer_list:
        i = i.replace(' ','')
        j = i.strip()
        if j:
            contents.append(j)

    return dict(contents)
