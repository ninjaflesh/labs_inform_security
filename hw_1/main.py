def read_file():
    text = ''
    with open('./out.txt', 'r', encoding='utf8') as f:
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


def decrypt_text(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - key) % len(alphabet)
            cipher = cipher + alphabet[new_position]
        else:
            cipher += letter
    return cipher


def write_file(cipher):
    with open('./out_2.txt', 'w', encoding='utf8') as f:
        f.write(cipher)


x = int(input("Шаг:"))
text = read_file()
text = decrypt_text(text, x)
write_file(text)
