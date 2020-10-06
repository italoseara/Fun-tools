import hashlib

password = input('Password: ')

enc_pass = password.encode('utf-8')
digest = hashlib.md5(enc_pass.strip()).hexdigest()

print('Hash:')
input(digest)
