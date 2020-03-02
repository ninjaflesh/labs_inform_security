def read_file():
    text = ''
    with open('./in.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f])
    return text


def encrypt_text(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + key) % len(alphabet)
            cipher = cipher + alphabet[new_position]
        else:
            cipher += letter
    return cipher


def write_file(cipher):
    with open('./out.txt', 'w', encoding='utf8') as f:
        f.write(cipher)


text = read_file()
text = encrypt_text(text, 3)
write_file(text)
