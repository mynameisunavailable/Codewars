Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)

ALGORITHMSSTRINGSFORMATTING


Solution:
  
def justify(text, width):
    
    text = text.strip().split()
    
    text_list = []
    width_alt = width
    text_temp = ""
    for i in text:
        # if the addition of the next word does not make the line lnoger than width
        # width_alt = the characters left till it is equal to width
        # add word and a space to text_temp string
        if width_alt - len(i) >= 0:
            width_alt -= len(i)+1
            text_temp += i + " "
        
        # if addition of another word makes line longer than width
        # append text_temp string to text_list
        # add word and a space, count characters left till line equal to width
        else:
            text_list.append(text_temp[:-1])
            width_alt = width
            text_temp = i + " "
            width_alt -= len(i)+1
    
    # append last line without final space
    text_list.append(text_temp[:-1])

    # for each line except last line
    xxx = ""
    for i in text_list[:-1]:
        # count number of spaces to be filled, count number of spaces between words
        spaces_left = width - len(i)
        spaces = len(i.split()) -1
        
        #Strings with one word do not need gaps ('somelongword\n').
        if spaces == 0:
            xxx += i
        
        else:        
            for k,j in enumerate(i.split()):
                spaces_list = []
                import math
                # minimum number of spaces between words for the line
                min_space = math.floor(spaces_left / spaces)
                # spaces_list for number of spaces between words
                [spaces_list.append(min_space+1) for i in range(0,spaces)]

                # number of spaces to be added to reach width
                spaces_remainder = spaces_left % spaces
                # add 1 space from front to back, for the length of spaces_remainder
                for i in range(0,spaces_remainder):
                    spaces_list[i] += 1
                # add 0 space after last word
                spaces_list.append(0)

                xxx += j + (" " * spaces_list[k])
        # add \n at the end of each line
        xxx += "\n"
    
    # append unmodified last line
    xxx += text_list[-1]
    
    return xxx
