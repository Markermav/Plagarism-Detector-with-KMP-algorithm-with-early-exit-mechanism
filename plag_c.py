from difflib import SequenceMatcher
import re

def KnuthMorrisPrattAlgorithm(pat, txt, placesFound):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while i < N:
        if pat[j].lower() == txt[i].lower():
            i += 1
            j += 1

        if j == M:
            # print ("Found pattern at index " + str(i-j))
            placesFound +=1
            j = lps[j-1]
            

        # mismatch after j matches
        elif i < N and pat[j].lower() != txt[i].lower():
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return placesFound

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


def removeCommonTerms(txt):
    if txt:
        r = re.split(r'[\.\?!\r\n'']', txt)
        return r
    # I will improve this going forward. This process is Tokenizing we can usualy do it by
    # NLP but I am not sure if dependency can be added using pip
  
compareText = open("main_file.txt","r").read()
patternText = open("compare_file.txt","r").read()
s = removeCommonTerms(patternText)
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

if((plagarism_percentage + usingDiffSequenceMatcher)/2) >= 65 : #kept Threshold 65
  print("compare_file is plagiarised : %s%% of its content matches with the main file." % (((plagarism_percentage + usingDiffSequenceMatcher)/2)))

# re is regex
# 1. def steming(): pass need to improve this
# 2 . def tokenizing(): pass need to improve this for better performance altogether

# Python program for KMP Algorithm I took from geeksforgeeks and Modified it, we can't use it without
# modifying it.