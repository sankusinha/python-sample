def pig_latin(word):
    first_letter = word[0]
    if first_letter == 'a' or first_letter == 'A':
        print(word+'ay')
    elif first_letter == 'e' or first_letter == 'E':
        print(word+'ay')
    elif first_letter == 'i' or first_letter == 'I':
        print(word+'ay')
    elif first_letter == 'o' or first_letter == 'O':
        print(word+'ay')
    elif first_letter == 'u' or first_letter == 'U':
        print(word+'ay')
    else:
        print(word[1:] +'ay')

def pig_latin_m(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return (word + 'ay')
    else:
        return (word[1:] + 'ay')
