##You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
##
##Examples:
##strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
##
##Concatenate the consecutive strings of strarr by 2, we get:
##
##treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
##folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
##trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
##blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
##abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
##
##Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
##The first that came is "folingtrashy" so 
##longest_consec(strarr, 2) should return "folingtrashy".
##
##In the same way:
##longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
##n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm).
##
##Note
##consecutive strings : follow one after another without an interruption


Solution:

def longest_consec(strarr, k):
    
    #n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm).
    n = len(strarr)
    if  n == 0 or k > n or k <= 0:
        return ""
    
    # concatenate consecutive strings based on the length k, return list of concatenated strings
    count=0
    length_list = []
    for i in strarr:
        length = ""
        try:
            for j in range(k):
                length += strarr[count+j]
            length_list.append(length)
            count+=1
        except:
            pass
    
    #in reversed list, if length of the subsequent number is equal or higher than previous then replace
    length = 0
    solution = ""
    for i in reversed(length_list):
        if len(i) >= length:
            length = len(i)
            solution = i
    
    return solution
