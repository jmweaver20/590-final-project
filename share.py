"""Hello"""

import os
import math

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/

P = 2**31-1 # do we need to change this

def make_shares(input: int, s1FileName: str, s2FileName: str) -> None:
    """Input a number as input to the computation and two output share file names,
    output two files with shares of the number."""

    randBytes = os.urandom(math.ceil(math.log2(P)))

    #produce shares s1 and s2, you need to convert randBytes to an integer mod P
    s1 = int.from_bytes(randBytes, "big") % P
    s2 = (input - s1) % P


    s1Bytes = s1.to_bytes(length=4, byteorder='big')
    s2Bytes = s2.to_bytes(length=4, byteorder='big')

    #write the shares to the given files
    s1File = open(s1FileName, "w")
    s2File = open(s2FileName, "w")
    s1File.write(s1Bytes.hex())
    s2File.write(s2Bytes.hex())
    s1File.close()
    s2File.close()

    return
