def correct():
    f = open('file.txt')
    content = f.read()


    content1 = content.lower()
    
    punc_list = '''!()-[]{};*:'"\,<>./?@_~'''

    for i in content1:
        if i in punc_list:
            content1 = content1.replace(i, "")
            
            words = content1.split()
            
            numwords = len(words)



            print("There are " + str(numwords) + " words in the file. \n")
