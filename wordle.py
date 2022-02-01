# script to get all valid 5-letter polish words where only 3 consecutive letters are known
# the output is validated by sjp.pl dictionary
# position of letters can be adjusted in line 10 (x_AAA_y by default), can be changed to AAA_x_y or x_y_AAA

def find_possible_words(input_word):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output = []

    for letter1 in a:
        for letter2 in a:
            y = letter1 + input_word + letter2
            output.append(y)
    return(output)


def pl_dict_check(word):
    input = find_possible_words(word)

    with open("/Users/kamil/Desktop/Python1stproject/slowa.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f]

    for i in input:
        if i in lines:
            print(i + ' in the dict')

print(pl_dict_check("ila"))
