Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
ALGORITHMSVALIDATIONUTILITIES


Solution:

def validBraces(string):

    string_dict = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
    }
    
    string_front = []

    for i in string:
        #if left bracket then put in string_front
        if i in string_dict:
            string_front.append(i)
        #if string_front is empty or is corresponding right bracket for the last left bracket
        #remove last left bracket
        elif len(string_front) != 0 and i == string_dict[string_front[-1]]:
            string_front.pop(-1)
        #if character is not corresponding right bracket then is not valid
        else:
            return False
    
    #if final list is empty then is valid
    return len(string_front) == 0
