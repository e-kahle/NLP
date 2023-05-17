import nltk
import matplotlib
from matplotlib import pyplot as plt
nltk.download('inaugural')
from nltk.corpus import inaugural
times = [fileid[:4] for fileid in inaugural.fileids()]
cfd = nltk.ConditionalFreqDist((target, fileid[:4])
                               for fileid in inaugural.fileids()
                               for w in inaugural.words(fileid)
                               for target in ['we', 'america', 'you']
                               if w.lower().startswith(target))
cfd.plot()
inDict = []
ids = []
for fileid in inaugural.fileids():
    print(len(inaugural.words(fileid)))
    ids.append(fileid[:4])
    inDict.append(len(inaugural.words(fileid)))

plt.plot(ids, inDict)
plt.xticks(fontsize=5)
plt.margins(x=0, y=0)
plt.xlabel("Year")
plt.title("Inaugural Address Size 1789-2021")
plt.ylabel("Number of Words in Inaugural Address")
plt.show()

print("hi")


