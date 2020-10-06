import hashlib

flag = 0

pass_hash = input('hash: ')
filename = input('password file name: ')

try:
    print('\nReading file...')
    pass_file = open(filename, 'r')
    print('Done!')

except:
    print('File not found')
    input()
    quit()

print('\nFinding Password...')
for password in pass_file:

    enc_pass = password.encode('utf-8')
    digest = hashlib.md5(enc_pass.strip()).hexdigest()

    if pass_hash == digest:
        flag = 1
        print(f'Found! The password is {password[:-1]}')
        break

if flag == 0:
    print("Password isn't in the list")

input()
