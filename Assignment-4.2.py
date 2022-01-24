def caesar_encode(fileNameToEncode, encodeKey):
    with open(fileNameToEncode, "r") as fd:
        strToWrite = ""
        fileConetent = fd.read()
        for letter in fileConetent:
            #Small_letters
            if 97 <= ord(letter) <= 122:
                encodeKey = encodeKey % 26
                if ord(letter) + encodeKey > 122:
                    encodeKey -= 26
                    strToWrite += chr(ord(letter) + encodeKey)
                else:
                    strToWrite += chr(ord(letter) + encodeKey)

            #Big_letter
            elif 65 <= ord(letter) <= 90:
                encodeKey = encodeKey % 26
                if ord(letter) + encodeKey > 90:
                    encodeKey -= 26
                    strToWrite += chr(ord(letter) + encodeKey)
                else:
                    strToWrite += chr(ord(letter) + encodeKey)
            # Sing
            else:
                strToWrite += letter

        fileNameToWrite = fileNameToEncode[:-4] + "_copy.txt"
        with open(fileNameToWrite, "w") as fd_write:
            fd_write.write(strToWrite)



def caesar_decode(fileNameToDecode, decodeKey):
    with open(fileNameToDecode, "r") as fd:
        strToWrite = ""
        fileConetent = fd.read()
        for letter in fileConetent:
            # Small_letters
            if 97 <= ord(letter) <= 122:
                decodeKey = decodeKey % 26
                if ord(letter) + decodeKey < 97:
                    decodeKey += 26
                    strToWrite += chr(ord(letter) - decodeKey)
                else:
                    strToWrite += chr(ord(letter) - decodeKey)

            # Big_letter
            elif 65 <= ord(letter) <= 90:
                decodeKey = decodeKey % 26
                if ord(letter) + decodeKey < 65:
                    decodeKey += 26
                    strToWrite += chr(ord(letter) - decodeKey)
                else:
                    strToWrite += chr(ord(letter) - decodeKey)
            # Sing
            else:
                strToWrite += letter

        fileNameToWrite = fileNameToDecode[:-4] + "_copy2.txt"
        with open(fileNameToWrite, "w") as fd_write:
            fd_write.write(strToWrite)





while True:
    user_input = input("Welcome , please choose :\n1)encode\n2)decode\n3)exit\n")

    if user_input == "1":
        filename = input("enter a file :\n")
        key = int(input("enter a key:\n"))
        caesar_encode(filename, key)
    elif user_input == "2":
        filename = input("enter a file:\n")
        key = int(input("enter a key:\n"))
        caesar_decode(filename, key)
    elif user_input == "3":
        print("goodbye")
        break
    else:
        print("enter only number between 1-3 ..")
