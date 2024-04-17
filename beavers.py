"""File for beaver functions."""

import sys
import os
import math

#biggest prime that fits in 31 bits
P = 2**31-1

def gen_beavers(filename: str):
    #no inputs
    #output shares a_1,b_1,c_1 and a_2,b_2,c_2 in two .txt files
    a1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
    a2 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

    b1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
    b2 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

    c1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

    a = (a1 + a2) % P
    b = (b1 + b2) % P
    c = a * b % P

    c1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
    c2 = c - c1
    if c2 < 0:
        c2 = P + c2

    a1Bytes = a1.to_bytes(length=4, byteorder='big')
    a2Bytes = a2.to_bytes(length=4, byteorder='big')
    b1Bytes = b1.to_bytes(length=4, byteorder='big')
    b2Bytes = b2.to_bytes(length=4, byteorder='big')
    c1Bytes = c1.to_bytes(length=4, byteorder='big')
    c2Bytes = c2.to_bytes(length=4, byteorder='big')

    s1File = open(f"{filename}_abc_1.txt", 'w')
    s2File = open(f"{filename}_abc_2.txt", 'w')

    s1File.writelines([a1Bytes.hex()+"\n", b1Bytes.hex()+"\n", c1Bytes.hex()+"\n"])
    s2File.writelines([a2Bytes.hex()+"\n", b2Bytes.hex()+"\n", c2Bytes.hex()+"\n"])

    s1File.close()
    s2File.close()


def beaver_mask(xFileName: str, yFileName: str, beaverFileName: str, outFileName: str):
    #input 2 share files, a beaver triple file, and output file name
    #output a file containing 2 input shares masked with shares of a, b from the beaver triple file

    xFile = open(xFileName, "r")
    yFile = open(yFileName, "r")
    beaverFile = open(beaverFileName, "r")

    xBytes = bytes.fromhex(xFile.read())
    yBytes = bytes.fromhex(yFile.read())

    aBytes = bytes.fromhex(beaverFile.readline())
    bBytes = bytes.fromhex(beaverFile.readline())

    x = int.from_bytes(xBytes, byteorder='big') % P
    y =  int.from_bytes(yBytes, byteorder='big') % P

    a = int.from_bytes(aBytes, byteorder='big') % P
    b = int.from_bytes(bBytes, byteorder='big') % P

    out1 = x - a
    if out1 < 0:
        out1 = P + out1
        
    out2 = y - b
    if out2 < 0:
        out2 = P + out2

    out1Bytes = out1.to_bytes(length=4, byteorder='big')
    out2Bytes = out2.to_bytes(length=4, byteorder='big')
        
    outFile = open(outFileName, 'w')

    outFile.writelines([out1Bytes.hex()+"\n", out2Bytes.hex()+"\n"])

    outFile.close()

def beaver_compute(xFileName: str, yFileName: str, maskedFileName: str, beaverFileName: str, outFileName: str, partyNum: int):
    #input shares of x, y, a file containing two masked shares from the other party, a beaver triple share, an 
    #output file name, and an input 1 or 2 indicating whether this is the party holding share 1 or share 2 of the messages
    #outputs share of product
        
    xFile = open(xFileName, "r")
    yFile = open(yFileName, "r")
    maskedFile = open(maskedFileName, "r")
    beaverFile = open(beaverFileName, "r")

    #read in the inputs
    xBytes = bytes.fromhex(xFile.read())
    yBytes = bytes.fromhex(yFile.read())
    x = int.from_bytes(xBytes, byteorder='big') % P
    y =  int.from_bytes(yBytes, byteorder='big') % P

    e_0Bytes = bytes.fromhex(maskedFile.readline())
    d_0Bytes = bytes.fromhex(maskedFile.readline())
    e_0 = int.from_bytes(e_0Bytes, byteorder='big') % P
    d_0 = int.from_bytes(d_0Bytes, byteorder='big') % P

    aBytes = bytes.fromhex(beaverFile.readline())
    bBytes = bytes.fromhex(beaverFile.readline())
    cBytes = bytes.fromhex(beaverFile.readline())
    a = int.from_bytes(aBytes, byteorder='big') % P
    b = int.from_bytes(bBytes, byteorder='big') % P
    c = int.from_bytes(cBytes, byteorder='big') % P

    #compute the other half of the masked values
    e_1 = x - a
    if e_1 < 0:
        e_1 = P + e_1
    d_1 = y - b
    if d_1 < 0:
        d_1 = P + d_1
        
    #compute the merged masked values e and d
    e = (e_0 + e_1) % P
    d = (d_0 + d_1) % P

    #compute z
    z = (c + (x * d) + (y * e)) % P

    #compute the -ed/2 part of z
    if partyNum == 1:
        ed = e*d % P
        z = z - ed
        if z < 0:
            z = P + z
            
    outBytes = z.to_bytes(length=4, byteorder='big')
    outFile = open(outFileName, 'w')

    outFile.write(outBytes.hex())

    outFile.close()

gen_beavers("male_comp_professors")
beaver_mask("varun_male_1.txt", "varun_comp_professors_1.txt", "abc_1.txt", "de_1.txt")
beaver_mask("varun_male_2.txt", "varun_comp_professors_2.txt", "abc_2.txt", "de_2.txt")
beaver_compute("varun_male_1.txt", "varun_comp_professors_1.txt", "de_2.txt", "abc_1.txt", "computed_male_gpa_1.txt", 1)
beaver_compute("varun_male_2.txt", "varun_comp_professors_2.txt", "de_1.txt", "abc_2.txt", "computed_male_gpa_2.txt", 2)
