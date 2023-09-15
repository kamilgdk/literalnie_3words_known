# script to get all valid polish/english words where only few consecutive letters are known
# the output is validated by sjp.pl dictionary
# position of letters can be adjusted in line 11 (x_AAA_y by default), can be changed to AAA_x_y or x_y_AAA etc

def find_possible_words(input_word):
    a = ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u','v','w','x','y','z','ź','ż']
    output = []

    for letter1 in a:
        for letter2 in a:
            y = letter1 + input_word + letter2
            output.append(y)
    return(output)
    
def dict_check(word):
    input = find_possible_words(word)

   
    #EN
    with open("***/validate_word_incomplete_input/english3.txt", "r") as f: #update your path
    #PL
    # with open("***/validate_word_incomplete_input/slowa.txt", "r") as f: #update your path
        lines = [line.rstrip('\n') for line in f]

    for i in input:
        if i in lines:
            print(i + ' in the dict')

letters = input("Podaj litery / Enter letters: ")
print('Pasujące słowa / Matching words: ')
print(dict_check(letters))