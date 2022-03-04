def green_pass(word_list, green_letters):

    i = 0
    while i < len(green_letters):

        j = 0
        while j < len(word_list):

            if green_letters[i][0] != word_list[j][int(green_letters[i][1])]:
                del(word_list[j])
            else:
                j += 1

        i += 1

    return word_list