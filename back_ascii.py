inp = open("temp__compressed","rb")
outp = open("temp__actcompressed","wb")


while True:
    charr = inp.readline()
    if(len(charr) == 0):
        break
    asc = chr(int(charr))
    #print(asc)
    outp.write(asc)