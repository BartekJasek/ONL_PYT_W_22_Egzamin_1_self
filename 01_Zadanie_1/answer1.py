def check_character(word, letter):
    if letter in word:
        print("Character found")
    else:
        print("Character not found")


print(check_character('Order of the Phoenix', 'o'))
