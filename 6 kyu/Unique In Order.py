Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]


Solution:

def unique_in_order(iterable):
    solution = []
    for i,j in enumerate(iterable):
        try:
            iterable[i+1]
            if j != iterable[i+1]:
                solution.append(j)
        except:
            solution.append(j)

    return solution