import os
m2 = 'curiosity killed the cat'
m1 = 'early bird catches the worm'
charstr = 'abcdefghijklmnopqrstuvwxyz '
key = 'valamiloremipsumszovegmertlustavagyok'
found = []
found2 = []
valt=True
def charfind(egyes,kettes,hossz,jel):
    ezaz = ''
    for a in range (hossz):
        j=0
        z=0
        while egyes[a]!=charstr[j]:
            #print(egyes, a)
            j+=1
        while kettes[a]!=charstr[z]:
            z+=1
        if jel=='-': 
            ezaz+=charstr[(z-j)%27]
        elif jel=='+':
            ezaz+=charstr[(j+z)%27]
        else:
            ezaz+=charstr[(j-z)%27]
    return ezaz

def getkey(message, cipher):
    return charfind(message,cipher,len(cipher),'-')
def ciphering(message):
    cipher=charfind(message,key,len(message),'+')
    return(cipher)
def megfejtes(cipher, message, message2):
    key = charfind(message,cipher,len(message),'-')
    idk(message2, key, 'a')
def idk(cm2, key, rs):
    if len(cm2)>len(key):
    #print(len(cm2),len(key))
        mo=charfind(cm2,key,len(key),'')
    #if True:
        tmp2 = []
        tmp = mo.split(' ')
        talalt= False
        for i in range (len(tmp)):
            tmpstr = (tmp[i])
            if len(tmp)>1:
                if i<len(tmp)-1 and tmpstr+'\n' in lines:
                    if i==len(tmp)-2:
                        talalt = True
                if i==len(tmp)-1 and talalt==True:
                    for j in range (len(lines)):
                        if tmpstr == lines[j][:len(tmpstr)]:
                            ra=''
                            for q in range (len(tmp)-1):
                                ra += tmp[q]+' '
                            ra += lines[j][:-1]+' '
                            print(ra, len(ra), len(m2))
                            if (len(ra)<len(m2)+1) and len(rs)<len(m1)+1:
                                found.append(ra)
                                if rs!='a':
                                    print(rs)
                                    found2.append(rs)
                                else:
                                    print(kezd[:-1]+' ')
                                    found2.append(kezd[:-1]+' ')
                                rkey.append(key)
                            if (len(ra)==len(m2)+1) and len(rs)==len(m1)+1:
                                print(' Az első mondat: ',ra,'\n','A második mondat: ',rs,'\n','A kulcs: ',key)
                                global valami
                                valami = True
            else:
                for j in range (len(lines)):
                    if tmpstr == lines[j][:len(tmpstr)]:
                        found.append(lines[j][:-1]+' ')
                        found2.append(kezd[:-1]+' ')
                        rkey.append(key)
        talalt=False
def idk2(cm2, key, adat, ertek, h):
 #   print(cm2, key)
    if len(cm2)>=len(key):
        mo=charfind(cm2,key,len(key),'')
        tmp2 = []
        tmp = mo.split(' ')
        talalt= False
        for i in range (len(tmp)):
            tmpstr = (tmp[i])
            if len(tmp)>1:
                if i<len(tmp)-1 and tmpstr+'\n' in lines:
                    if i==len(tmp)-2:
                        talalt = True
                if i==len(tmp)-1 and talalt==True:
                    for j in range (len(lines)):
                        if tmpstr == lines[j][:len(tmpstr)]:
                            ra=''
                            for q in range (len(tmp)-1):
                                ra += tmp[q]+' '
                            ra += lines[j][:-1]+' '
                            nkey = rkey[h]
                            nkey+=getkey(ra[ertek:],c1[ertek:len(ra)]) 
                            #print(nkey, ra)
                            idk(c2,nkey,ra)
        talalt=False

##########  
c1 = ciphering(m1)
c2 = ciphering(m2)
print(c1,'\n',c2)
f = open("words.txt", "r")
lines = f.readlines()
rkey = []
valt=True
for c in range (len(lines)):
    kezd = lines[c]
    if len(kezd)<len(c1):
        megfejtes(c1,kezd[:len(kezd)-1]+' ',c2)
print(found, found2)
def idkvalamilyenloop():
    for h in range (len(found2)):
        ertek = len(rkey[h])
        if len(found[h])>len(found2[h]):
            ch1=found[h]
            ch2=found2[h]
            y = c2
            x = c1
            lista = 2
        elif len(found[h])<len(found2[h]):
            ch1=found2[h]
            ch2=found[h]
            y= c1
            x =c2
            lista = 1
        else:
            print('a')
        #print(ch1[ertek:],y[ertek:len(ch1)])
        newkey = getkey(ch1[ertek:],y[ertek:len(ch1)])
        rkey[h]+=(newkey)
        ertek=len(rkey[h])
        print(rkey[h])
        idk2(x,rkey[h],lista,ertek,h)
global valami
valami = False
#for i in range(3):
idkvalamilyenloop()
idkvalamilyenloop()
idkvalamilyenloop()
idkvalamilyenloop()
idkvalamilyenloop()
print(found, found2)
