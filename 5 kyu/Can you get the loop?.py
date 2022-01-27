You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 12:


# Use the `next' attribute to get the following node
node.next
Note: do NOT mutate the nodes!

Thanks to shadchnev, I broke all of the methods from the Hash class.

Don't miss dmitry's article in the discussion after you pass the Kata !! 

ALGORITHMSHACKING HOLIDAYS


Solution:
    node_history = []
    
    #check if node.next is in node_history list
    #if yes then length of list minus the index of previously encountered node.next
    #if not then go to next node, then append node to node_history 
    while 1:
        if node.next in node_history:
            return len(node_history) - node_history.index(node.next)
        
        node = node.next
        node_history.append(node)
