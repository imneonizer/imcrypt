import imcrypt

#imcrypt.new_key()

text = 'Hello World!'
print(f'Text: {text}')

encrypted = imcrypt.encrypt(text)
print(f'Encrypted: {encrypted}')

decrypted = imcrypt.decrypt(encrypted)
print(f'Decrypted: {decrypted}')

print(f'key: {imcrypt.key()}')