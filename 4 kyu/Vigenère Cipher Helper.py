The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).

The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

From Wikipedia:

The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

. . .

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key
Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

Example
var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'
Any character not in the alphabet must be left as is. For example (following from above):

c.encode('CODEWARS'); // returns 'CODEWARS'
ALGORITHMSCIPHERSCRYPTOGRAPHYSECURITYOBJECTSCLASSESBASIC LANGUAGE FEATURESOBJECT-ORIENTED PROGRAMMINGFUNDAMENTALSSTRINGS


Solution:
  
class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet * 2
        
        
    def encode(self, message):
        
        #lengthen key to cover all characters in message
        self.key = self.key * (int(len(message)/len(self.key))+1)
        
        #numerical representation of key using alphabet string
        key_list = []
        for i in self.key:
            key_list.append(self.alphabet.index(i))
        
        #numerical representation of message using alphabet string
        #if not in alphabet string then no change
        message_list = []
        for i in message:
            try:
                message_list.append(self.alphabet.index(i))
            except:
                message_list.append(i)
        
        #add numerical representation of key and message together
        #use alphabet table to find the alphabet
        solution = ""
        for i in range(0, len(message_list)):
            try:
                solution += self.alphabet[message_list[i] + key_list[i]]
            except:
                solution += message_list[i]                
                
        return solution
                
        
    def decode(self, message):
        
        self.key = self.key * (int(len(message)/len(self.key))+1)
        
        #numerical representation of message using alphabet string
        #if not in alphabet string then no change
        message_list = []
        for i in message:
            try:
                message_list.append(self.alphabet.index(i))
            except:
                message_list.append(i)        
        
        #numerical representation of key using alphabet string
        key_list = []
        for i in self.key:
            key_list.append(self.alphabet.index(i))        

        #for each numerical representation of character, message - key + length of alphabet string
        #if not a number, then remain unchanged
        solution = []
        for i in range(0, len(message_list)):
            try:
                solution.append(message_list[i] - key_list[i] + len(self.alphabet)/2)
            except:
                solution.append(message_list[i])
        
        #find out character the number represents with alphabet string
        res = ""
        for i in solution:
            try:
                res += self.alphabet[int(i)]
            except:
                res += i
        
        return res
        
