def check_character(word, letter):
    answer = []
    for word in word.split():
        for sign in word:
            if sign == letter:
                answer.append(1)
    return len(answer)


print(check_character('Order of the Phoenix', 'o'))
print(check_character('Order of the Phoenix', 'z'))
print(check_character('Order of the Phoenix', 'p'))
print(check_character('Order of the Phoenix', 'P'))
