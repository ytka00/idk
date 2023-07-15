import string
allowed = set(string.ascii_lowercase+' ')
charstr = 'abcdefghijklmnopqrstuvwxyz '

def rejtjelezes():
    uzenet = str(input('Adja meg az üzenetet! '))
    key = str(input('Adja meg a kulcsot! '))
    cipher = ''
    if all(ch in allowed for ch in uzenet)==False:
        print('Az üzenet hibás karaktereket tartalmaz')
        exit(1)
    if all(ch in allowed for ch in key)==False:
        print('A kulcs hibás karaktereket tartalmaz')
        exit(1)
    if len(uzenet)>len(key):
        print('Hibás adatokat adott meg')
        exit(1)
    j = 0
    z = 0
    for i in range (len(uzenet)):
        while uzenet[i]!=charstr[j]:
            j+=1
        while key[i]!=charstr[z]:
            z+=1
        cipher+=charstr[(j+z)%27]
        z = 0
        j = 0
    print(cipher)
def megfejtes():
    z=0
    j=0
    uzenet=''
    cipher=input('Adja meg a kódot: ')
    key = input('Adja meg a kulcsot: ')
    if len(key)<len(cipher):
        print('Hibás adatokat adott meg')
        exit(1)
    if all(ch in allowed for ch in cipher)==False:
        print('A kódolt üzenet hibás karaktereket tartalmaz')
        exit(1)
    if all(ch in allowed for ch in key)==False:
        print('A kulcs hibás karaktereket tartalmaz')
        exit(1)
    for i in range (len(cipher)):
        while  cipher[i]!=charstr[j]:
            j+=1
        while key[i]!=charstr[z]:
            z+=1
        uzenet+=charstr[(j-z)%27]
        z=0
        j=0
    print(uzenet)
def main():
    a = input('1: titkosítás \n2: deciphering\n')
    if a=='1':
        rejtjelezes()
    elif a=='2':
        megfejtes()
    else:
        print('1-es vagy 2-es opciót válasszon')
        main()
main()
