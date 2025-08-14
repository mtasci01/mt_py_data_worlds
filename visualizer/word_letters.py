from matplotlib import pyplot as plt


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_map = {}

for i in range(len(alphabet)):
    alphabet_map[alphabet[i]] = i + 1

word = "caesar"
word = word.lower()

xs = []
ys = []

for i in range(len(word)):
    ys.append(alphabet_map[word[i]])
    xs.append(i + 1)

plt.plot(xs,ys, color='blue')
plt.show()   
