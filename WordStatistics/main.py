
from matplotlib import pyplot as plt
from nltk import regexp_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import os
import nltk
from translate import Translator
import collections
import nltk.corpus
nltk.download('brown')
nltk.download('gutenberg')
from nltk.corpus import brown
translatorGer = Translator(to_lang="ger")
print(brown.words())
print(nltk.corpus.gutenberg.fileids())
md = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
hm = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
cs = nltk.corpus.gutenberg.words('shakespeare-caesar.txt')
bb = nltk.corpus.gutenberg.words('bible-kjv.txt')
mds = ""
for word in md:
    mds += str(word)
    mds +=" "
mobyDick = regexp_tokenize(mds, "\w+")
hms = ""
for word in hm:
    hms += str(word)
    hms += " "
hamlet = regexp_tokenize(hms, "\w+")
css = ""
for word in cs:
    css += str(word)
    css += " "
caesar = regexp_tokenize(css, "\w+")
bbs = ""
for word in bb:
    bbs += str(word)
    bbs += " "
bible = regexp_tokenize(bbs, "\w+")
mobyLens = [len(word) for word in mobyDick]
mobyNum = len(mobyDick)
mobyAvg = 0
mobyMax = 0
mobyBigWord = ""
mobyCommonWord = ""
for length in mobyLens:
    mobyAvg = mobyAvg + length
mobyAvg = mobyAvg / mobyNum
for word in mobyDick:
    g = len(word)
    if g > mobyMax:
        mobyMax = len(word)
        mobyBigWord = word
mobyFreq = collections.Counter(mobyDick)
mobyCommon = max(mobyFreq, key=mobyFreq.get)
print("Moby Dick:" "\n")
print("Number of words: "+ str(mobyNum)+ "\n")
print("Average Word Length: "+ str(mobyAvg) + "\n")
print("Biggest Word: "+ str(mobyBigWord) + " \n")
print("Most Frequent Word/Symbol: " + str(mobyCommon) + "\n")
bibleLens = [len(word) for word in bible]
bibleNum = len(bible)
bibleAvg = 0
bibleMax = 0
bibleBigWord = ""
bibleCommonWord = ""
for length in bibleLens:
    bibleAvg = bibleAvg + length
bibleAvg = bibleAvg / bibleNum
for word in bible:
    g = len(word)
    if g > bibleMax:
        bibleMax = len(word)
        bibleBigWord = word
bibleFreq = collections.Counter(bible)
bibleCommon = max(bibleFreq, key=bibleFreq.get)
print("Bible:" "\n")
print("Number of words: "+ str(bibleNum)+ "\n")
print("Average Word Length: "+ str(bibleAvg) + "\n")
print("Biggest Word: "+ str(bibleBigWord) + " \n")
print("Most Frequent Word/Symbol: " + str(bibleCommon) + "\n")
hamletLens = [len(word) for word in hamlet]
hamletNum = len(hamlet)
hamletAvg = 0
hamletMax = 0
hamletBigWord = ""
hamletCommonWord = ""
for length in hamletLens:
    hamletAvg = hamletAvg + length
hamletAvg = hamletAvg / hamletNum
for word in hamlet:
    g = len(word)
    if g > hamletMax:
        hamletMax = len(word)
        hamletBigWord = word
hamletFreq = collections.Counter(hamlet)
hamletCommon = max(hamletFreq, key=hamletFreq.get)
print("Hamlet:" "\n")
print("Number of words: "+ str(hamletNum)+ "\n")
print("Average Word Length: "+ str(hamletAvg) + "\n")
print("Biggest Word: "+ str(hamletBigWord) + " \n")
print("Most Frequent Word/Symbol: " + str(hamletCommon) + "\n")
caesarLens = [len(word) for word in caesar]
caesarNum = len(caesar)
caesarAvg = 0
caesarMax = 0
caesarBigWord = ""
caesarCommonWord = ""
for length in caesarLens:
    caesarAvg = caesarAvg + length
caesarAvg = caesarAvg / caesarNum
for word in caesar:
    g = len(word)
    if g > caesarMax:
        caesarMax = len(word)
        caesarBigWord = word
caesarFreq = collections.Counter(caesar)
caesarCommon = max(caesarFreq, key=caesarFreq.get)
print("Caesar:" "\n")
print("Number of words: "+ str(caesarNum)+ "\n")
print("Average Word Length: "+ str(caesarAvg) + "\n")
print("Biggest Word: "+ str(caesarBigWord) + " \n")
print("Most Frequent Word/Symbol: " + str(caesarCommon) + "\n")
plt.figure(1)
plt.hist(mobyLens)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
plt.xlabel("Number of letters")
plt.ylabel("Frequency (Moby Dick)")
plt.figure(2)
plt.hist(bibleLens)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
plt.xlabel("Number of letters")
plt.ylabel("Frequency (Bible)")
plt.figure(3)
plt.hist(hamletLens)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
plt.xlabel("Number of letters")
plt.ylabel("Frequency (Hamlet)")
plt.figure(4)
plt.hist(caesarLens)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
plt.xlabel("Number of letters")
plt.ylabel("Frequency (Caesar)")
plt.show()