print ("0. The student number is 17181624")

number = 17181624
count = 0
for x in "17181624":
    isPrime = True
    # print("Checking ", x)
    if int(x) > 1:
        for num in range (2, int(x)):
                if int(x) % num == 0:
                    isPrime = False
                    # print (x, " is not a prime")
                    break
    else:
        isPrime = False
    if isPrime:
        count +=1
print ("1. The amount of prime numbers is: ", count)

import random
ranNum = random.randint(25,50)
print ("2. The Random number is: ", ranNum)

dividNum = ranNum//count
print ("3. The number of strings to be generated is: ", dividNum)


print  ("4. List of strings")
print  ("=========================")
import string

alphabet = string.ascii_lowercase
stringList = []
stCount = 0
for st in range (0, dividNum):
    word = ""
    if stCount % 2 != 0:
        letters = 7
    else:
        letters = 5
    word = "".join(random.choice(alphabet)for i in range(letters))
    stringList.append(word)
    stCount += 1
    print (stCount, " - ", word, "(", letters,")")
print  ("=========================")
vList = []
vowels = ["a", "e", "i", "o", "u"]
# comList = [str, int]
for x in stringList:
    vCount = 0
    for let in str(x):
        for v in vowels:
            if let == v:
                vCount+=1
                break
    vList.append(vCount)
    # print(vCount)
    # comList.append("wrd":x, "vwl":vCount)
for i in range(len(vList)-1):
    for j in range (len(vList) - int(i) - 1):
        if vList[j] > vList [j+1]:
            temp = vList[j]
            vList[j] = vList[j+1]
            vList[j+1] = temp
            temp2 = stringList[j]
            stringList[j] = stringList[j+1]
            stringList[j+1] = temp2


print("5. Sorted list")
print  ("=========================")

lCount = 1
for p in range(len(stringList)):
    print(lCount, " - ", stringList[p],"(vowels: ", vList[p] ,")")
    lCount+=1

print  ("=========================")

def reverseList():
    lCount = 0
    print("5. Reverse Sorted list")
    print  ("=========================")
    stringList.reverse()
    vList.reverse()
    for p in range(len(stringList)):
        print(lCount, " - ", stringList[p],"(vowels: ", vList[p] ,")")
        lCount+=1
    print  ("=========================")

reverseList()
