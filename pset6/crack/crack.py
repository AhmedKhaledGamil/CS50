import sys
import crypt
import string

def main():
    if len(sys.argv) == 2:
        file = open("workfile.txt","w")
        hash = sys.argv[1]
        salt = hash[0:2]
        key = "a"
        one = True
        two = True
        three = True
        four = True
        for n in range (1+26+26):
            for l in range(1+26+26):
                for k in range(26+26+1):
                    for j in range(26+26+1):
                        for i in range(26+26):
                            if i == 0:
                                key = key.replace(key[0],"a")
                            #file.write(f"{key}\n")
                            possible_hash = crypt.crypt(key,salt)
                            #file.write(f"{possible_hash}\n")
                            if hash == possible_hash:
                                print(key)
                                exit(0)
                            new_value = ord(key[0]) + 1
                            new_char = chr(int(new_value))
                            key = key.replace(key[0],new_char,1)
                            if i == 25:
                                #file.write("pause\n")
                                key = key.replace(key[0],"A",1)
                        if j == 0 and one:
                            #file.write("pause\n")
                            key = key + "a"
                            one = False
                        elif j == 26:
                            #file.write("pause\n")
                            key = key.replace(key[1],"A",1)
                        else:
                            #file.write("pause\n")
                            key = key.replace(key[1],chr(int(ord(key[1]) + 1)),1)
                    if k == 0 and two:
                        #file.write("pause\n")
                        key = key + "a"
                        two = False
                    if k == 26:
                        #file.write("pause\n")
                        key = key.replace(key[2],"A",1)
                    elif k != 0 and k !=26:
                        #file.write("pause\n")
                        key = key.replace(key[2],chr(int(ord(key[2]) + 1)),1)
                if l == 0 and three:
                    #file.write("pause\n")
                    key = key + "a"
                    three = False
                if l == 26:
                    #file.write("pause\n")
                    key = key.replace(key[3],"A",1)
                elif l != 0 and l !=26:
                    #file.write("pause\n")
                    key = key.replace(key[3],chr(int(ord(key[3]) + 1)),1)
            if n == 0 and four:
                #file.write("pause\n")
                key = key + "a"
                four = False
            if n == 26:
                #file.write("pause\n")
                key = key.replace(key[4],"A",1)
            elif n != 0 and n !=26:
                #file.write("pause\n")
                key = key.replace(key[4],chr(int(ord(key[4]) + 1)),1)
        #file.close()
    else:
        print("Usage: ./crack hash")
        exit(1)

if __name__ == "__main__":
    main()