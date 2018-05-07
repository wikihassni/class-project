"""
def reversenum():
    max=''
    infile = open('waqas.txt', 'r')
    text= infile.read()
    text=text.split()
    for l in text:
        if len(max)<len(l):
            max=l
    print(max)


reversenum()
""""""
import numpy as np
a=np.random.randint(100,size=30)
maxi=np.amax(a)
ind=np.where(a==maxi)


a=np.random.randint(100,size=30)
maximum=np.amax(a)
indexmax=np.where(a==np.amax(a))
print(a)
print(maximum)
print(indexmax)
# programme 1
def F():
    a,b = 0,1
    print(a,b)
    for i in range (0,99):

        a, b = b, a + b
        print(b)

F()

#Morse Code - 101computing.net/morse-code-encoder/

#First let's store the morse code for the alphabet using a dictionary
morseCode = {"A":".-","B":"-...","C":"-.-."}
morseCode["D"] = "-.."
morseCode["E"] = "."
morseCode["F"] = "..-."
morseCode["G"] = "--."
morseCode["H"] = "...."
morseCode["I"] = ".."
morseCode["J"] = ".---"
morseCode["K"] = "-.-"
morseCode["L"] = ".-.."
morseCode["M"] = "--"
morseCode["N"] = "-."
morseCode["O"] = "---"
morseCode["P"] = ".--."
morseCode["Q"] = "--.-"
morseCode["R"] = ".-."
morseCode["S"] = "..."
morseCode["T"] = "-"
morseCode["U"] = "..-"
morseCode["V"] = "...-"
morseCode["W"] = ".--"
morseCode["X"] = "-..-"
morseCode["Y"] = "-.--"
morseCode["Z"] = "--.."

#Retrieve end-user's message and convert it to upper case.
message = input("Type a message to convert in morse code (e.g. \"SOS\"?)").upper()
encodedMessage = ""

#Convert each letter into morse code:
for character in message:
  #Check that the character is in the moreCode dictionary (e.g letter of the alphabet)
  if character in morseCode:
    encodedMessage += morseCode[character] + " "
  else:
    #Replace unrecognised characters with a space
    encodedMessage += " "

#Display the message in morse code:
print("Your message in morse code is:")
print(encodedMessage)
"""""
#https://www.youtube.com/watch?v=iGatZTAUoE0 link for explanation;;;
def largestprime():
    number=600851475143
    factor=2
    primelist=[]
    while number>1:
        if number % factor ==0:
            primelist.append(factor)
            number=number/factor
        else:
            factor+=1
    print(primelist)
largestprime()

