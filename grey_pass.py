def grey_pass(word_list, grey_letters):
    
    i = 0
    while i < len(grey_letters):

        j = 0
        while j < len(word_list):

            if grey_letters[i] in word_list[j]:
                del(word_list[j])
            else:
                j += 1

        i += 1
 
    return word_list
