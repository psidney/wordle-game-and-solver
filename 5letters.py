
unfilteredWords = []
with open('20k.txt') as f:
    line = f.readline().replace('\n','')
    while line:
        unfilteredWords.append(line)
        line = f.readline().replace('\n','')

filteredWords = []

for word in unfilteredWords:
    if len(word) == 5:
        filteredWords.append(word)


f = open('5letter.txt','w+')
for word in filteredWords:
    f.write(word + '\n')

f.close()