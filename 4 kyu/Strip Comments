Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
ALGORITHMS STRINGS


Solution:

def solution(string,markers):
    
    #split based on "\n"
    #check each character for markers, add to solution string until marker detected
    #strip solution string
    #add solution string and "\n" to res string
    #reset solution string
    solution = ""
    res = ""
    for i in string.split("\n"):
        for j in i:
            if j not in markers:
                solution += j
            else:
                break

        res += solution.strip()+ "\n"
        solution=""

    return res[:-1]
    for i in solution.split("\n"):
        res += i.strip() + "\n"
        
    return res[:-2]
