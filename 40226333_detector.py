from difflib import SequenceMatcher
import math
import re
import sys

#Defining Constants, this can be modified as per the requirements and constraints of the check
class Constants:
    TOKEN_LETTERS = ['!','"','''\n''','''\r''','''\.''','?','#','$','%','&','(',')','*','+','/',':',';','<','=','>','@','[','\\',']','^','`','{','|','}','~','\t',',','-'] 
    STOP_WORDS = ['s', "you've", 'those', "hasn't", 'of', 'were', 'doing', 'when', 'too', 'before', 'more', 'ain', 'won', 'a', 'nor', 'this', "mightn't", 'has', 'have', 'through', 'ourselves', 'if', 'or', "haven't", 'by', 'we', 'these', 'against', 'the', 'should', 'its', "shan't", 'now', 'me', 'haven', 'then', 'am', 'into', 'is', 'll', 'couldn', 'once', 'not', "mustn't", "she's", 'while', 'under', "you'd", 'about', 'an', "that'll", 'you', 'theirs', "wouldn't", 're', "weren't", 'her', 'from', "it's", 'ours', 'how', 'as', 'there', 'which', 'most', 'myself', 'i', "you're", 'own', 'very', "didn't", 'needn', 'shan', "needn't", 'yourself', 'such', 'what', 'to', 'who', 'ma', 'she', 'all', "hadn't", 'on', 'and', 'where', "doesn't", 'their', 'mustn', 'don', "couldn't", 'herself', 'up', 'your', 'over', 'having', 'again', 'each', 'had', 'shouldn', 'both', 'hadn', 'his', 'being', 'doesn', 'because', 'mightn', 'my', "you'll", 'itself', "isn't", 'himself', 'are', "don't", 'some', 'wouldn', 'only', 'in', 'any', 'at', 'whom', 'that', 'yours', 'further', 'after', 'yourselves', 'be', 'will', "should've", "won't", 'weren', 'them', 'themselves', 'few', 'did', 'aren', "aren't", 'o', 'hasn', 'so', 'until', 'off', 'can', 'here', 'didn', 'than', 'during', 'been', 'why', 'same', 'isn', 'below', 'd', 've', 'out', 'hers', "shouldn't", "wasn't", 'it', 'y', 'just', 'our', 'him', 'for','he', 'no', 'do', 'wasn', 'between', 't', 'm', 'was', 'with', 'other', 'down', 'above', 'does', 'they', 'but']
    STEM_WORDS = r'ly|ing|ization|ism|tive|ness|ent|ment|less|ship|ing|les|ly|es|s|ora|ous|ble|tional|ize|ive|ici|al|electromag|fundament|force'
    def get_token(self):
        return self.TOKEN_LETTERS  
    def get_stopWords(self):
        return self.STOP_WORDS
    def get_stemWords(self):
        return str(self.STEM_WORDS)        

def KnuthMorrisPrattAlgorithm(pattern, text, placesFound):
    # Computing the legth of the pattern and txt
    lengthOfThePattern = len(pattern)
    lengthOfTheText = len(text)
    
    # Computing Longest Prefix that is a Suffix LPS[]
    # It's length should be same as of pattern length
    LPS = [0]*lengthOfThePattern
    # Preprocess the pattern (calculate lps[] array)

    LPSArrayImplementation(pattern, lengthOfThePattern, LPS)
    j = 0 # defining pointer for pattern[] & initialising with 0
    i = 0 # defining pointer for text[] & initialising with 0
    while i < lengthOfTheText:
        if pattern[j].lower() == text[i].lower():
            i += 1
            j += 1

        # If there is mismatch after pattern matches
        elif i < lengthOfTheText and pattern[j].lower() != text[i].lower():
            # not zero check cause LPS of -1 can't be found incase first char doesn't match
            if j != 0:
                #this step is done cause our next comparison will start from new j position
                j = LPS[j-1] 
           
            # if first char doesn't match just increment i and compare    
            else:
                i += 1

        if j == lengthOfThePattern:
                # Found a match and place marked, increment placeFound
            placesFound +=1
            #this is done to check all the occurences of the pattern in text
            # reset j to LPS[j-1] nxt comparison will start from new j position 
            j = LPS[j-1]
            break  

    return placesFound

def LPSArrayImplementation(pattern, lengthOfThePattern, LPS):
    len = 0 # length of the previous longest prefix suffix
    i = 1
    LPS[0] = 0
    # the loop calculates lps[i] for i = 1 to lengthOfThePattern-1
    while i < lengthOfThePattern:
        if pattern[i]== pattern[len]:
            # since it is match we have to increment both the pointers len & i
            len += 1
            # put the new incremented len to LPS of i
            LPS[i] = len
            i += 1
        else:
            # when we progressed in len we have to backtrack or else we will loose continuity
            if len != 0:
                len = LPS[len-1]
                # if len is in 1st position of the pattern
            else:
                LPS[i] = 0
                i += 1


# As we can't use external libraries like NLTK, so hardcoded the 
# Tokenization,Stemming & Stopword Removal
#inspired from NLTK package dataset
def TokenizingPatternFile(pattern):
        pattern = pattern.lower() 
        constant = Constants()
        for tokens in constant.get_token(): 
            pattern = pattern.replace(tokens,'') 
        finalPattern = pattern.split() 
        return finalPattern

def TokenizingStopWordRemovalStemming(pattern):  
        finalProcessedPattern = [] 
        constant  = Constants()
        tokens = TokenizingPatternFile(pattern)
        for token in tokens:
            if token not in constant.get_stopWords():
                finalProcessedPattern.append(re.sub(constant.get_stemWords(),'', token))
        return finalProcessedPattern


def main(FILE1, FILE2): 
    compareText = open(FILE1,"r").read()
    patternText = open(FILE2,"r").read()
    s = TokenizingStopWordRemovalStemming(patternText)   
    counter_matched = 0
    counter_total = 0
    placesFound=0
    for i in s:
        i = i.strip()
        if len(i) > 0:
            counter_total +=1
            counter_matched += KnuthMorrisPrattAlgorithm(i, compareText, placesFound)
    plagarism_percentage =  (counter_matched*100/counter_total)         
    print ("Plagarism by Knuth Morris Pratt Algorithm = %s%%" % (plagarism_percentage))

    usingDiffSequenceMatcher = SequenceMatcher(None, compareText, patternText).ratio()*100
    print("Plagarism by Sequence Matcher = " + str(usingDiffSequenceMatcher)+ "%")

    if(int(math.floor(plagarism_percentage))<=41): #kept Threshold 41
        print(0)
    else:
        print(1)    

if __name__ == '__main__':
   try:
       main(sys.argv[1], sys.argv[2])
   except Exception as e:
       print("Hi! you entered wrong command! "+"Error Type:", e.__class__)
       print("Recommended cmd format: make FILE1=<path_to_file1> FILE2=<path_to_file2> run")
