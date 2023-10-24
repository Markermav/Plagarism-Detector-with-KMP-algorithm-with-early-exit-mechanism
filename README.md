# Plagarism-Detector-with-KMP-algorithm-with-early-exit-mechanism

DETAILS:

I designed my plagiarism detector using the Knuth-Morris-Pratt algorithm, and I have used the 
Longest Common Subsequence (LCS) as a reference or verifier to keep track of or double-check my output 
for any anomalies. But the final output is completely influenced by the implementation of the 
Knuth-Morris-Pratt algorithm.

Reasons to use the Knuth-Morris-Pratt algorithm:

The KMP algorithm is a string matching algorithm that runs in linear time.

INTRODUCTION:

The Knuth-Morris-Pratt Algorithm, also known as the KMP algorithm, is a string searching algorithm
which searches a text for occurrences of a word or pattern in words. It uses the longest prefix &
suffix in order to match a pattern. It will return the matching words or pattern.
a plagiarism percentage, which is then compared with a specific threshold. If the plagiarism
percentage is more than the given threshold, then it will return either 1 (which will determine
plagarism exists) or 0 (there is no plagarism).

IMPLEMENTATION:

Step1: PRE PROCESSING the comparision/pattern File prior to plagarism check.
Preprocessing includes 3 common steps:
1. Tokenizing: This converts the document into a collection of words by entering the words in
an array and separating the punctuations and numbers that aren't important. I have
taken a wide dataset, which is inspired by the nltk.tokenize module.

2. Stopwords Removal : Removal of basics word like: and,he,she,or etc. I have taken
a wide dataset of my own to process and filter my text.

3. Stemming: The process of changing the words that still have the prefix and suffix
such that it becomes a basic word.I have kept the stemming data very limited and used
regex (regular expression) to sort them as per the requirement. It is inspired by
dataset of nltk.stem.

Step 2: KMP Implementation
- KMP relies on 2 concepts prefix and suffix:
prefix: start from the pattern's left side and take a subset of the pattern
suffix: start from the right side of the pattern and find subsets.
- If the beginning part of the pattern appears anywhere else in that pattern, we have
to observe for a match. We generate a pi table or LPS table, which will store the longest
prefix, which is the same as some suffixes.

Example: LPS Table:
index    1    2    3    4    5    6    7    8    9    10    11
 pat    a    b    c    d    e    a    b    f    a    b    c
 LPS    0    0    0    0    0    1    2    0    1    2    3

To check for plagiarism, my algorithm compares two input files, one of which is the root file.
and the other will be the pattern file. Once the pattern file is processed, it moves on to function.
KnuthMorrisPrattAlgorithm(). 
- We initialise an LPS array with 0's up to the length of the pattern array. ([0]*lengthOfThePattern)
The pattern is subsequently matched with each iteration of the index.
in both pattern (iterator j) and text (iterator i). if i == j + 1 then it is a match. If a match
then move j and i both forward and check the same condition again.
- If a mismatch happens, then move the j iterator position to the index of that particular element.
referencing the pi table. Here, only j iterator will move if a mismatch happens and the position
of i will be stagnant. Then the same process is continued till we reach the end of the text.
- The loop scans the entire length of the text, and if the pattern matches, it increments the pointer
i and j. If a mismatch occurs we know already that a bandwidth of element before matched, if
we check the LPS table for the value of the mismatched index, it will give us the length of the
longest suffix from a prefix and we move to that particular index cause before it everything already matched.

LPS Array:
- Here string matching has to be done within the pattern itself, and an iterator must iterate to the end
of the pattern. Variable 'len' will tell us the length of a matching prefix which is also a suffix. Here LPS[0]
will always be 0 as the first character alone doesn't have a suffix or prefix.
* I have added very specific comments in my code for the overall overview.


EFFICIENCY:

Naive Algorithm:
It is more efficient than the Naive algorithm because there is a mismatch in the Naive algorithm.
The algorithm will compare the next index of the root string, which will be a drawback. The 
Repeated,unnecessary backtracking by the iterator will increase the running time, resulting in 
to O(mn). m -> size of Pattern n-> size of text

KMP Algorithm:
KMP uses prefix and suffix concept and it doesn't move backwards which implies for each element
present in the text input we perform constant number of operation including the LPs fucntion.

Time complexity = O(n+m) => O(n) for n>>m  m -> Time complexity of LPS table operation; n-> size of text
Hence, it executes in linear time.
