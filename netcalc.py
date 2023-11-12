#!/usr/bin/python3
import re

def binMask(cidr):
    return ('1' * cidr + '0' * (32 - cidr))

def binWcard(cidr):
    return ('0' * cidr + '1' * (32 - cidr))

def addZero(lista):
    if len(lista) != 8:
        leng = 8-len(lista)
        while leng:
            lista.append(0)
            leng-=1
    return lista[::-1]

def bin_frmt(mask_bin):
    binary=[]
    for i in range(0,32,8):
        if i != 24:
            binary.append(str(mask_bin[i:i+8])+".")
        else:
            binary.append(str(mask_bin[i:i+8]))
    bn= ''.join(str(n) for n in binary)
    return bn

def toBin(i):
    l=[]
    if i == 0:
        return 0
    while i:
        l.append(i%2)
        i=i//2
    return l

def getIpCidr():
    ip_cidr = str(input("\n[+] Dame la ip en CIDR: "))
    regex_pattern = r'(\d{1,3}(?:\.\d{1,3}){3})/(\d{1,2})'
    match = re.match(regex_pattern, ip_cidr)
    if match:
        return match
    else:
        print("No se encontró una coincidencia válida.")
        exit(1)

def getBinIp(parts):
    ipb = []
    for i in parts:
        i=int(i)
        ipb = toBin(i)
        ipb = addZero(ipb)
        ip_bin.append(ipb)
    return

def doAnd(mask,ip):
    bi=[]
    maskfand=int(mask,2)
    ipfand=int(ip,2)
    res=maskfand & ipfand
    bi=toBin(res)
    if len(bi) != 32:
        leng = 32-len(bi)
        while leng:
            bi.append(0)
            leng-=1
    bi=bi[::-1]
    return bi

def doOr(wcard,ip):
    bi=[]
    maskfor=int(wcard,2)
    ipfor=int(ip,2)
    res=maskfor | ipfor
    bi=toBin(res)
    if len(bi) != 32:
        leng = 32-len(bi)
        while leng:
            bi.append(0)
            leng-=1
    bi=bi[::-1]
    return bi

def ipdec(ipa_bin):
    res = []
    for i in range(0,32,8):
        if i != 24:
            res.append(str(int(ipa_bin[i:i+8],2))+".")
        else:
            res.append(str(int(ipa_bin[i:i+8],2)))
    resultado = ''.join(str(n) for n in res)
    return resultado

if __name__ == "__main__":
    ip_bin=[]
    match = getIpCidr()
    ip_address, subnet_mask = match.groups()
    print("\n[+] IP Address:", ip_address)
    print("\n[+] Subnet Mask:", subnet_mask)
    getBinIp(ip_address.split('.'))
    ip_binary = ''.join(''.join(str(num) for num in sublist) for sublist in ip_bin)
    ip_bin.clear()
    mask_bin = binMask(int(subnet_mask))
    ip_bin=doAnd(mask_bin,ip_binary)
    ipID=''.join(str(n) for n in ip_bin)
    bn = bin_frmt(mask_bin)
    wcard = binWcard(int(subnet_mask))
    wcardfr = bin_frmt(wcard)
    ip_bin.clear()
    ip_bin=doOr(wcard,ipID)
    ipBc=''.join(str(n) for n in ip_bin)
    ip_bin.clear()
    print("\n[+] IP ID: \n\n    [=] - ", ipdec(ipID))
    print("\n[+] IP Broadcast: \n\n    [=] - ", ipdec(ipBc))
    print("\n[i] La netmask en binario es :\n")
    print("       [=] - ",bn)
    print("\n[i] La netmask en decimal es :\n")
    print("       [=] - ",ipdec(mask_bin),"\n")
    print("\n[i] La wildcard en binario es :\n")
    print("       [=] - ",wcardfr)
    print("\n[i] La netmask en decimal es :\n")
    print("       [=] - ",ipdec(wcard),"\n")
    print("\n[i] Se calculan que tocan este número de hosts :\n")
    print("       [=] - ",(2**(32-int(subnet_mask))-2),"\n")

