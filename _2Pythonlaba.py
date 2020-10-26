from random import randint

while True:
    print("Options:")
    print("Enter '1' for first easy option: ")
    print("Enter '2' for second pro programmer option: ")
    print("Enter '3' to end the program:")
    user_input = input(": ")
    if user_input == "3":
        break

    #Like amateur programmer
    elif user_input == "1":
        symbols='qwertyuiopasdfghjklzxcvbnm0123456789'
        line = input("Enter String: ")
        letters= list(set(line))
        if len(letters) > 3:
            delline = []
            for i in(1,2,3):
                delline.append(letters[i])
            newline = ''
            for i in line:
                if i not in delline:
                    newline+=i
            print('Deleted symbol:  ',delline)
            print('Resulting string : ',newline)
        else:
            n = len(letters)
            while n <4:
                d = symbols[randint(0,len(symbols))]
                if d not in letters:
                    k=randint(0,len(line))
                    line=line[:k]+d+line[k:]
                    n += 1
                print('New string: ')
                print(line)

                #like a pro programmer
    elif user_input =="2":

        symbols='qwertyuiopasdfghjklzxcvbnm0123456789'
        line = input("Enter string: ")
        letters = list(set(line))
        if len(letters) > 3:
            delline=[]
            for i in (1,2,3):
                 delline.append(letters[i])
                 line=line.replace(letters[i],'')
            print('Deleted symbol: ',delline)
            print('Resulting line: ',line)
        else:
             n = len(letters)
             while n < 4:
                  d = symbols[randint(0,len(symbols))]
                  if d not in letters:
                       k=randint(0,len(line))
                       line=line[:k]+d+line[k:]
                       n += 1
             print('New string: ')
             print(line)

        ...
    else:
        print("Unknown input")