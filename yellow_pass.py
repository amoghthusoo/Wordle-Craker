def yellow_pass(word_list, yellow_letters):

    i = 0
    while i < len(yellow_letters):

        j = 0
        while j < len(word_list):

            if yellow_letters[i][0] == word_list[j][int(yellow_letters[i][1])]:
                del(word_list[j])
            else:
                j +=1

        i += 1

    return word_list

