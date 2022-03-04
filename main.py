from green_pass import green_pass
from grey_pass import grey_pass
from yellow_pass import yellow_pass

f = open('word-list.txt')
word_list = f.readlines()
f.close()

while True:

    letter_list = []

    print()
    for e in range(5):
        letter = input('Enter letter with colour : ') + str(e)
        letter_list.append(letter)


    grey_list = []
    yellow_list = []
    green_list = []
    grey_list_mod = []
    green_for_com = []


    for e in letter_list:

        if e[1] == 'g':
            grey_list.append(e[0])

        elif e[1] == 'y':
            yellow_list.append(e[0] + e[2])

        elif e[1] == 'G':
            green_list.append(e[0] + e[2])

    for e in green_list:
        temp = e[0]
        green_for_com.append(temp)
    
    
    for e in grey_list:
        
        if e in green_for_com:
            grey_list_mod.append('0')
        else:
            grey_list_mod.append(e)

    grey_filtered = grey_pass(word_list, grey_list_mod)

    yellow_filtered = yellow_pass(grey_filtered, yellow_list)

    green_filtered = green_pass(yellow_filtered, green_list)

    print(green_filtered)

    word_list = green_filtered
