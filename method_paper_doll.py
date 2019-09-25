def paper_doll(text):
    new_text = ''
    for l in text:
        for i in range(0,3):
            new_text = new_text + l
    return new_text
