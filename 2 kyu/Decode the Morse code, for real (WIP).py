Part of Series 3/3
This kata is part of a series on the Morse code. Make sure you solve the [first part](/kata/decode-the-morse-code) and the [second part](/kata/decode-the-morse-code-advanced) and then reuse and advance your code to solve this one.

In this kata you have to deal with "real-life" scenarios, when Morse code transmission speed slightly varies throughout the message as it is sent by a non-perfect human operator. Also the sampling frequency may not be a multiple of the length of a typical "dot".
For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may actually be received as follows:

0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000

As you may see, this transmission is generally accurate according to the standard, but some dots and dashes and pauses are a bit shorter or a bit longer than the others.

Note also, that, in contrast to the previous kata, the estimated average rate (bits per dot) may not be a whole number – as the hypotetical transmitter is a human and doesn't know anything about the receiving side sampling rate.

For example, you may sample line 10 times per second (100ms per sample), while the operator transmits so that his dots and short pauses are 110-170ms long. Clearly 10 samples per second is enough resolution for this speed (meaning, each dot and pause is reflected in the output, nothing is missed), and dots would be reflected as 1 or 11, but if you try to estimate rate (bits per dot), it would not be 1 or 2, it would be about (110 + 170) / 2 / 100 = 1.4. Your algorithm should deal with situations like this well.

Also, remember that each separate message is supposed to be possibly sent by a different operator, so its rate and other characteristics would be different. So you have to analyze each message (i. e. test) independently, without relying on previous messages. On the other hand, we assume the transmission charactestics remain consistent throghout the message, so you have to analyze the message as a whole to make decoding right. Consistency means that if in the beginning of a message '11111' is a dot and '111111' is a dash, then the same is true everywhere in that message. Moreover, it also means '00000' is definitely a short (in-character) pause, and '000000' is a long (between-characters) pause.

That said, your task is to implement two functions:

1. Function decodeBitsAdvanced(bits), that should find an estimate for the transmission rate of the message, take care about slight speed variations that may occur in the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. If message is empty or only contains 0's, return empty string. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot. If stuck, check this for ideas.

2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string. If the input is empty string or only contains spaces, return empty string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as MORSE_CODE dictionary, feel free to use it. For C, the function morse_code acts like the dictionary. For C++ and Scala, a map is used. For C#, it's called Preloaded.MORSE_CODE. For Racket, a hash called MORSE-CODE is used.

(hash-ref MORSE-CODE "".-.") ; returns "C"
Of course, not all messages may be fully automatically decoded. But you may be sure that all the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!


Solution:

def decodeBitsAdvanced(bits):
    
    from sklearn.cluster import KMeans
    import numpy as np
    
    #clear front and back of 0s
    bits = bits.strip("0")
    
    if len(bits) == 0:
        return ""
    
    #separate 0s and 1s into list of lists
    previous = "1"
    listify = [[]]
    count = 0
    for i in bits:
        if i != previous:
            count += 1
            listify.append([])
        listify[count].append(int(i))
        previous = i
    
    
    if len(listify) == 1:
        return (".")
    
    
    #length of each list within list of list
    list1 = [len(i) for i in listify]
    
    #prepare list for kmeans clustering
    list1 = np.array(list1)
    list1 = list1.reshape(-1,1)
    
    #sort list length from shortest to longest
    sorted_list1 = np.sort(list1,axis=0)
    
    #kmeans clustering with sorted list, shortest length at the start
    kmeans = KMeans(n_clusters=3,random_state=None)
    kmeans.fit(sorted_list1)
    sorted_predicted = kmeans.predict(sorted_list1)
    
    #find out cluster number of character, shortest to longest
    previous_cluster = 99
    cluster_identity = []
    for i in sorted_predicted:
        if i != previous_cluster:
            cluster_identity.append(i)
        previous_cluster = i
    
    #kmeans cluster unsorted list
    predicted = kmeans.predict(list1)
    
    #change cluster number of unsorted list according to the cluster_identity list
    #shortest will be cluster 0, longest will be 2
    final_predicted = []
    for i in predicted:
        if i == cluster_identity[0]:
            final_predicted.append(0)
        elif i == cluster_identity[1]:
            final_predicted.append(1)
        else:
            final_predicted.append(2)
    
    #count number of clusters in final_predicted list
    num_clusters = len(np.unique(final_predicted))
    
    #first list is 1s, second list is 0s, so on...
    #if list is 0s and shortest then is "", if long then " ", if longest then "   "
    #if list is 1s and long or longest then is "-", otherwise is "."
    dad = ""
    bit_identity = 1

    if num_clusters == 3:
        for i in final_predicted:
            if bit_identity == 0:
                bit_identity = 1
                if i == 0:
                    dad += ""
                elif i == 1:
                    dad += " "
                elif i == 2:
                    dad += "   "
            elif bit_identity == 1:
                bit_identity = 0
                if i == 1 or i == 2:
                    dad += "-"
                else:
                    dad += "."

    elif num_clusters == 2:
        for i in final_predicted:
            if bit_identity == 0:
                bit_identity = 1
                if i == 0:
                    dad += ""
                elif i == 1:
                    #long pause more than five times longer than short pause
                    if min(list1) * 5 < max(list1):
                        dad += "   "
                    else:
                        dad += " "
            elif bit_identity == 1:
                bit_identity = 0
                if i == 1:
                    dad += "-"
                else:
                    dad += "."

    elif num_clusters == 1:
        for i in final_predicted:
            if bit_identity == 0:
                bit_identity = 1
                dad+= ""
            elif bit_identity == 1:
                bit_identity = 0
                dad += "."
    
    return dad

    
def decodeMorse(morse_code):

    #split string into words
    morse_code = morse_code.split("   ")
    #split words into letters
    words = [i.split() for i in morse_code]

    #use dictionary to replace morse code into symbols, add a space after each word
    solution = ""
    for i in words:
        for j in i:
            solution += MORSE_CODE[str(j)]
        solution += " "

    return solution[0:-1]
