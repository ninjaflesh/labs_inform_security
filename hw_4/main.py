def read_file():
    text = ''
    with open('in.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f]).lower()
    return text


def write_file(encrypted_text):
    with open('./out.txt', 'w', encoding='utf8') as f:
        f.write(encrypted_text)


def encrypt_text(text, key):
    content_id = list(map(ord, text))
    key_id = list(map(ord, key))
    key_id_len = len(key_id)
    new_id = []
    for i in range(len(content_id)):
        j = i % key_id_len
        new_id.append(content_id[i] ^ key_id[j])
    return ''.join(list(map(chr, new_id)))


text = read_file()
key = input('key: ')
encrypted_text = encrypt_text(text, key)
write_file(encrypted_text)
