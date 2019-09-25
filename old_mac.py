def old_mac(text):
    i=0
    text_len = len(text)
    new_text = ''
    for letter in text:
        if i == 0 or i == 3:
            letter = text[i].upper()
        new_text = new_text + letter
        i = i+1
    return new_text
