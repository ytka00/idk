import string
import random
found=[];found2=[];f=open("words.txt","r");lines=f.readlines();rkey=[];m1='';m2=''
charstr = 'abcdefghijklmnopqrstuvwxyz '
for i in range(random.randint(2,6):
    m1+=lines[random.randrang(len(lines))][:-1]+' '
    m2+=lines[random.randrang(len(lines))][:-1]+' '
m1=m1[:-1];m2=m2[:-1]
key=''.join(random.choices(string.ascii_lowercase,k=len(m1)*2))
def charfind(egyes,kettes,hossz,jel):
    ezaz = ''
    for a in range (hossz):
        j=0;z=0
        while egyes[a]!=charstr[j]:j+=1
        while kettes[a]!=charstr[z]:z+=1
        if jel=='-':ezaz+=charstr[(z-j)%27]
        elif jel=='+':ezaz+=charstr[(j+z)%27]
        else:ezaz+=charstr[(j-z)%27]
    return ezaz
def getkey(message,cipher):
    return charfind(message,cipher,len(cipher),'-')
def ciphering(message):
    cipher=charfind(message,key,len(message),'+')
    return(cipher)
def megfejtes(cipher, message, message2):
    key = charfind(message,cipher,len(message),'-')
    idk(message2,key,'a')
def idk(cm2,key,rs):
    if len(cm2)>=len(key):mo=charfind(cm2,key,len(key),'')
    else:mo=charfind(cm2,key,len(cm2),'')
    tmp=mo.split(' ');talalt=False
    for i in range(len(tmp)):
        tmpstr=(tmp[i])
        if len(tmp)>1:
            if i<len(tmp)-1:
                if tmpstr+'\n' in lines:
                    if i==len(tmp)-2:talalt=True
                else:break
            if i==len(tmp)-1 and talalt==True:
                for j in range(len(lines)):
                    if tmpstr==lines[j][:len(tmpstr)]:
                        ra=''
                        for q in range(len(tmp)-1):ra+=tmp[q]+' '
                        ra+=lines[j][:-1]+' '
                        if (len(ra)<len(m2)+1) and len(rs)<len(m1)+1:
                            found.append(ra)
                            if rs!='a':found2.append(rs)
                            else:found2.append(kezd[:-1]+' ')
                            rkey.append(key)
                        if (len(ra)==len(m2)+1) or len(rs)==len(m1)+1:
                            found.append(ra);found2.append(rs);rkey.append(key)
                        if (len(ra)==len(m2)+1) and len(rs)==len(m1)+1:
                            print(' Az első mondat: ',ra,'\n','A második mondat: ',rs,'\n','A kulcs: ',key)
                            global valami;valami=True
        else:
            for j in range(len(lines)):
                if tmpstr==lines[j][:len(tmpstr)]:
                    found.append(lines[j][:-1]+' ');found2.append(kezd[:-1]+' ');rkey.append(key)
    talalt=False
def idk2(cm2,key,ertek,h):
    if len(cm2)>=len(key):
        mo=charfind(cm2,key,len(key),'');tmp=mo.split(' ');talalt=False
        for i in range (len(tmp)):
            tmpstr=(tmp[i])
            if len(tmp)>1:
                if i<len(tmp)-1:
                    if tmpstr+'\n' in lines:
                        if i==len(tmp)-2:talalt=True
                    else:break
                if i==len(tmp)-1 and talalt==True:
                    for j in range(len(lines)):
                        if tmpstr==lines[j][:len(tmpstr)]:
                            ra=''
                            for q in range (len(tmp)-1):ra += tmp[q]+' '
                            ra+=lines[j][:-1]+' '
                            nkey = rkey[h];nkey+=getkey(ra[ertek:],c1[ertek:len(ra)]);idk(c2,nkey,ra)
        talalt=False
##########  
c1=ciphering(m1);c2=ciphering(m2)
print('Az első rejtjelezett mondat:',c1,'\n','A második rejtjelezett mondat:',c2)
for c in range(len(lines)):
    kezd=lines[c]
    if len(kezd)<len(c1):
        megfejtes(c1,kezd[:len(kezd)-1]+' ',c2)
def idkvalamilyenloop():
    for h in range(len(found2)):
        newkey=getkey(found[h][len(rkey[h]):],c2[len(rkey[h]:len(found[h])]);rkey[h]+=(newkey)
        idk2(c1,rkey[h],len(rkey[h]),h)
valami=False
while valami==False:idkvalamilyenloop()
