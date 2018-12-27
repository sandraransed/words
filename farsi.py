import random

class Words:

    def __init__(self, persian_word, swedish_word):
        self.persian_word = persian_word
        self.swedish_word = swedish_word

    def get_persian_word(self):
        return self.persian_word

    def get_swedish_word(self):
        return self.swedish_word

def choose_file():
    print("\nVill du öva ord du kan (1) eller ord du är osäker på (2)?\nFör att avsluta, skriv 'Avsluta'\n")
    while True:
        user_input = input("")
        if user_input == "1":
            return "ordjagkan.txt"
        elif user_input == "2":
            return "ordjagintekan.txt"
        elif user_input.lower() == "avsluta":
            print("Bye!")
            return None
        else:
            print("Skriv in 1 eller 2")

def import_database(user_file_choice):
    read_file = open(user_file_choice, 'r', encoding="utf-8")
    read_file = read_file.readlines()
    return read_file

def create_list_of_words(read_file):
    list_of_words_lines = []
    for i in read_file:
        list_of_words_lines.append(i.replace("\n",''))
    list_of_words = []
    for i in list_of_words_lines:
        list_of_words.append(i.split(':'))
    return list_of_words

def create_words(list_of_words):
    words = []
    for word in list_of_words:
        persian_word = word[0]
        swedish_word = word[1]
        my_words = Words(persian_word, swedish_word)
        words.append(my_words)
    return words

def user_input(words):
    while True:
        random_number = random.randint(0, len(words) - 1)
        user_input = input("Vad betyder {}? \n".format(words[random_number].get_persian_word()))
        if user_input.lower() == words[random_number].get_swedish_word().lower():
            print("\nRätt \n")
        elif user_input.lower() == "avsluta":
            print("Khadafhes!")
            break
        else:
            print("\nFel \nRätt svar är {} \n".format(words[random_number].get_swedish_word()))
            user_input = input("Vad betyder {}? \n".format(words[random_number].get_persian_word()))
            if user_input.lower() == words[random_number].get_swedish_word().lower():
                print("\nRätt \n")
            elif user_input.lower() == "avsluta":
                print("Khadafhes!")
                break
            else:
                print("Jad begir! \n")

def intro_text():
    print("\n \nSkriv in det svenska ordet. \n\n")

def main():
    user_file_choice = choose_file()

    if user_file_choice:
        read_file = import_database(user_file_choice)
        list_of_words = create_list_of_words(read_file)
        words = create_words(list_of_words)
        intro_text()
        user_input(words)

main()
