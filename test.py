f = open('word-list.txt') 
word_list = f.readlines()



while True:
    target = input('Enter targer word : ')

    for e in word_list:
        if e == target + '\n':
            print('FOUND!')
            break

    else:
        print('NOT FOUND!')

