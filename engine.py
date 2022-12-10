

# Class that is used as tries Node.
class Node:
    def __init__(self):
        self.children = [None] * 26  # Indicate next letter
        self.endOfWord = False  # Indicated the leaf Node mark as End of Word
        self.pageContains = set()  # Store the web pages that contain word
        self.count = {}


# Class that implement Data Structure
class Trie:

    def __init__(self):
        self.root = self.getNode()

    # Returns new Node
    def getNode(self):
        return Node()

    # Insert Into Tries
    def insert(self, key, file):
        key = key.lower()
        file = file.strip()
        if not key.strip():
            return
        rword = ['a', 'an', 'the', 'above', 'across', 'against', 'along',
                 'among', 'around', 'at', 'before', 'behind', 'below', 'beneath',
                 'beside', 'between', 'by', 'down', 'from', 'in', 'into', 'near', 'of',
                 'off', 'on', 'to', 'toward', 'under', 'upon', 'with', 'within',
                 'i', 'he', 'him', 'you', 'we', 'him', 'her', 'yours', 'theirs', 'someone',
                 'where', 'when', 'yourselves', 'themselves', 'oneself', 'is', 'hers', 'when',
                 'whom', 'whose', 'each other', 'one', 'everyone', 'nobody', 'none',
                 'each', 'anywhere', 'anyone', 'nothing'
                 ]
        if key in rword:  # Checking if key is preposition, pronoun or article
            return
        curNode = self.root
        length = len(key)
        for i in range(length):
            index = ord(key[i]) - ord('a')
            if not curNode.children[index]:
                curNode.children[index] = self.getNode()
            curNode = curNode.children[index]
        curNode.endOfWord = True
        if curNode.endOfWord:
            curNode.pageContains.add(file)
            if curNode.count.get(file, -1) == -1:
                curNode.count[file] = 1
            curNode.count[file] += 1  # Increment Count of Word in file

    # Search a Key into Tries
    def search(self, key):
        curNode = self.root
        length = len(key)
        for i in range(length):
            index = ord(key[i]) - ord('a')
            if not curNode.children[index]:
                return False, [], {}
            curNode = curNode.children[index]
        return (curNode.endOfWord, curNode.pageContains, curNode.count)


# Trie object
t = Trie()

fi = open('input.txt', 'r')
files = fi.readlines()
fi.close()
for file in files:
    fr = open(file.strip(), 'r')
    str = fr.read()
    bracket = False
    word = ""
    for ch in str:
        if bracket and ch == '>':
            bracket = False
            word = ""
        if bracket:
            continue
        elif ch == '<':
            bracket = True
            t.insert(word, file)
            word = ""
        elif ch.isalpha():
            word += ch
        elif ch == ' ':
            t.insert(word, file)
            word = ""
    fr.close()

fo = open('output.txt', 'w')
search = input('Input Search Text: ')
words = search.split()
op = set()
count = {}
for word in words:
    flag, st, cnt = t.search(word.lower())
    if flag:
        if len(op) == 0:
            op.update(st)
        else:
            op = op.intersection(st)
        for i in op:
            key = i.strip()
            if count.get(key, -1) == -1:
                count[key] = 0
            if key in cnt:
                count[key] += cnt[key]

output = []
for i in op:
    output.append((count[i], i))
output.sort(key=lambda x: x[0])
output.reverse()
fo.write('Files That contain all the words!\n\n')
for op in output:
    fo.write('{0}\t\t Number of Times Words Occur: {1}\n'.format(op[1], op[0]))
if len(op) == 0:
    fo.write("Words Not found in any file")
fo.close()
