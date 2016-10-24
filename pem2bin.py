#!/usr/bin/python3
import sys

line = ''

def parseField(field):

    global line
    while True:
        if (line != None) and (len(line) > 0) and (line[0] == field):
            break

        line = input().split(':')

    if (field == "publicExponent"):
        return [ line[1].split()[0] ]

    data = []
    while True:
        line = input().split(':')
        if '' in line:
            line.remove('')

        if line == None or not line:
            continue
        # Check if we've finished with current field
        if line[0][0] != ' ':
            break

        data += [ ("0x" + x.strip()) for x in line ]

    return data

def printData(data, skipComma):

    for idx,elem in enumerate(data):
        print(elem, end="")
        if (not skipComma or idx != len(data)-1):
            print(", ", end="")
        if (idx % 16 == 15):
            print("\n", end="")

def pem2bin(fields):

    for idx,field in enumerate(fields):
        data = parseField(field)

        if (field == "publicExponent"):
            continue

        if (field == "prime1") or (field == "prime2") or (field == "exponent1"):
            data = data[1:]

        printData(data, idx == (len(fields)-1))

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == "public"):
        fields = [ "Modulus" ]
    else:
        fields = [ "modulus", "publicExponent", "privateExponent",
                   "prime1", "prime2", "exponent1", "exponent2", "coefficient" ]
    pem2bin(fields)