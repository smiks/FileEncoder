__author__ = 'Sandi'

import os
import sys
import platform

class encoder:

    def __init__(self, directory, encode_to = "utf-8", decode_from = None):
        self.directory = directory
        self.encode_to = encode_to
        self.decode_from = decode_from

    def encode(self):
        stripped = "/" if (platform.system() == "Linux" or
                        platform.system() == "Unix") else "\\"

        for fname in os.listdir(self.directory):
            fname = self.directory.strip(stripped) + stripped + fname
            with open(fname, "r", encoding=self.decode_from) as f:
                content = f.read()
            os.remove(fname)
            with open(fname, "w", encoding=self.encode_to) as f:
                f.write(content)




if __name__ == "__main__":
    directory = sys.argv[1]

    argc = len(sys.argv)

    if argc == 2:
        print("\n "
              "Decoding from directory: {0} \n "
              . format(directory))

    elif argc > 2:
        decode_from = sys.argv[2]
        print("\n "
              "Decoding from directory: {0} \n "
              "Decode from: {1} \n "
              . format(directory, decode_from))


    elif argc > 3:
        decode_from = sys.argv[2]
        encode_to = sys.argv[3]
        print("\n "
              "Decoding from directory: {0} \n "
              "Decode from: {1} \n "
              "Encode to: {2} \n" . format(directory, decode_from, encode_to))

    if not os.path.exists(directory):
        print("Directory does not exist")
        exit(1)

    if argc == 2:
        coder = encoder(directory)

    elif argc == 3:
        coder = encoder(directory, decode_from=decode_from)

    elif argc == 4:
        coder = encoder(directory, encode_to=encode_to, decode_from=decode_from)

    try:
        coder.encode()
    except:
        print("Something went wrong :( ")
        exit(1)

    print("Encoding is completed")
