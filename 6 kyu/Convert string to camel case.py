##Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
##
##Examples
##"the-stealth-warrior" gets converted to "theStealthWarrior"
##"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
##
##ALGORITHMSREGULAR EXPRESSIONSDECLARATIVE PROGRAMMINGADVANCED LANGUAGE FEATURESFUNDAMENTALSSTRINGS


Solution:

def to_camel_case(text):
    
    if len(text) == 0:
        return ""
    
    delimiter_dict = {
    "-": " ",
    "_": " "
    }
    
    solution = ""
    for i in text:
        if i in delimiter_dict:
            solution += delimiter_dict[i]
        else:
            solution += i
            
    solution = solution.split()
    
    res = ""
    res += solution[0]
    for i in solution[1:]:
        res += i.capitalize()
    
    return res
