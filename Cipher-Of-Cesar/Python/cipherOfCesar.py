
setOfAphabetLowerCase = {chr(97+i) : i for i in range(26)}
setOfAphabetUpperCase = {chr(65+i) :  i+26 for i in range(26)}
setOfNumber = {chr(48+i) : i + 52 for i in range(10)}

SetInDict =  setOfAphabetLowerCase | setOfAphabetUpperCase | setOfNumber
SetInList = list(SetInDict)

def cipherOfCesar(s, k, decrypt=False):
    k = k if not decrypt else k * -1
    S = list()
    for c in s:
        if(c in SetInDict):
            item = (SetInDict[c] + k) % len(SetInList)
            S.append(SetInList[item])
        else:
            S.append(c)

    return "".join(S)


msg = cipherOfCesar("I've valid Turing test", 30)
print(f"cipher msg => {msg}")
msg2 = cipherOfCesar(msg, 30, decrypt=True)
print(f"msg decryption => {msg2}")