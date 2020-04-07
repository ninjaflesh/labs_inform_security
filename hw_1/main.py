def read_file_e():
    text = ''
    with open('./in.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f])
    return text


def encrypt_text(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphere = ""
    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + key) % len(alphabet)
            ciphere = ciphere + alphabet[new_position]
        else:
            ciphere += letter
    return ciphere


def write_file_e(ciphere):
    with open('./out.txt', 'w', encoding='utf8') as f:
        f.write(ciphere)


def read_file_d():
    text = ''
    with open('./out.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f])
    return text


def decrypt_text(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipherd = ""
    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - key) % len(alphabet)
            cipherd = cipherd + alphabet[new_position]
        else:
            cipherd += letter
    return cipherd


def write_file_d(cipherd):
    with open('./out_2.txt', 'w', encoding='utf8') as f:
        f.write(cipherd)


key = int(input("Шаг:"))
text = read_file_e()
text = encrypt_text(text, key)
write_file_e(text)

text = read_file_d()
text = decrypt_text(text, key)
write_file_d(text)
