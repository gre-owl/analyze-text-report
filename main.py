# open and create file handlers to get content of file

f = open('file.txt')
content = f.read()


# pass content to imported modules to edit out typos programmatically (built ins)


#makes all the content lower case and stores it in content1
content1 = content.lower()
#print(content1)



# loops through the content1 and replaces all the items in the punctuation list using for loop
punc_list = '''!()-[]{};*:'"\,<>./?@_~'''

for i in content1:
    if i in punc_list:
        content1 = content1.replace(i, "")
        
        
#once formatted split the words into a list to be counted
words = content1.split()
#print(words) to check if it is reading the file



#Number of words in list counted
numwords = len(words)



print("There are " + str(numwords) + " words in the file. \n")
    



#count how many times words occur

from collections import Counter 

word_counts = Counter(words)

#print(word_counts)



#display which words are most common (use the first item in the word count it will always be the highest)

common = word_counts.most_common(1)
print("The most common word in the file is:\n" + str(common) + "\n")





#create a folder 

import os
os.mkdir('Report folder')


# save report in to file of findings 

reportfile = open('report.txt', 'a')

reportfile.write("There are " + str(numwords) + " words in the file. \n The most common word in the file is:\n" + str(common) + "\n")

reportfile.close()




#code needs to report number of words, how many time word occurs, which words are most common, then create a folder and saves the report inside a file (customs)




# $ python main.py file.txt 
# works in spyder 






