import string
allowed=set(string.ascii_lowercase+' ');charstr='abcdefghijklmnopqrstuvwxyz '
def charfind(egyes,kettes,jel):
    megoldas= ''
    for a in range(len(egyes):
        j=0;z=0
        while egyes[a]!=charstr[j]:j+=1
        while kettes[a]!=charstr[z]:z+=1
        if jel=='-':megoldas+=charstr[(z-j)%27]
        else:megoldas+=charstr[(j+z)%27]
    return(megoldas)
def rejtjelezes():
    uzenet=str(input('Adja meg az üzenetet! '));key=str(input('Adja meg a kulcsot! '));cipher = ''
    if all((ch in allowed for ch) in uzenet or key)==False:print('Az üzenet vagy kulcs hibás karaktereket tartalmaz');exit(1)
    if len(uzenet)>len(key):print('Hibás adatokat adott meg');exit(1)
    cipher=charfind(uzenet,key,'');print(cipher)
def megfejtes():
    cipher=input('Adja meg a kódot: ');key=input('Adja meg a kulcsot: ')
    if len(key)<len(cipher):print('Hibás adatokat adott meg');exit(1)
    if all(ch in allowed for ch in cipher)==False:print('A kódolt üzenet hibás karaktereket tartalmaz');exit(1)
    if all(ch in allowed for ch in key)==False:print('A kulcs hibás karaktereket tartalmaz');exit(1)
    uzenet=charfind(cipher,key,'-');print(uzenet)
def main():
    a = input('1: titkosítás \n2: deciphering\n')
    if a=='1':rejtjelezes()
    elif a=='2':megfejtes()
    else:print('1-es vagy 2-es opciót válasszon');main()
main()
