inp = open("temp__compressed","rb")
outp = open("temp__asciicompressed","wb")


while True:
    charr = inp.read(1)
    if(len(charr) == 0):
        break
    asc = ord(charr)
    #print(asc)
    outp.write("%s %s" % (str(asc), "\n"))