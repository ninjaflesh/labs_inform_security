import random
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet += alphabet.lower()


def read_file():
    with open('./in.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f])
    return text


def create_key():
    alphabet_id = list(range(len(alphabet)))
    random.shuffle(alphabet_id)
    key = ''.join([alphabet[i] for i in alphabet_id])
    with open('./key.txt', 'w', encoding='utf8') as f:
        for i in range(len(alphabet)):
            f.write(f'{alphabet[i]} (╯°□°）╯︵ ┻━┻ ---> {key[i]}\n')
    return key


def encrypt_text(text, key):
    key = key + key.lower()
    text = list(text)
    for i in range(len(text)):
        if text[i] in alphabet:
            alphabet_id = alphabet.index(text[i])
            text[i] = key[alphabet_id]
    return ''.join(text)


def decrypt_text(text, key):
    key = key + key.lower()
    text = list(text)
    for i in range(len(text)):
        if text[i] in alphabet:
            alphabet_id = key.index(text[i])
            text[i] = alphabet[alphabet_id]
    return ''.join(text)


def write_file_encrypt(text):
    with open('./encrypt.txt', 'w', encoding='utf8') as f:
        f.write(text)


def write_file_decrypt(text):
    with open('./decrypt.txt', 'w', encoding='utf8') as f:
        f.write(text)


text = read_file()
key = create_key()
encrypt_text = encrypt_text(text, key)
decrypt_text = decrypt_text(encrypt_text, key)
write_file_encrypt(encrypt_text)
write_file_decrypt(decrypt_text)
