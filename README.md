Project: Search Engine

Description:
Implement the simplified Search Engine described in Section 23.6 (Subsection; Search Engine) for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.

Approach:

I used Tries Data structure to insert and search indexes.

Trie Data Structure:Trie is a sorted tree-based data-structure that stores the set of strings. It has the number of pointers equal to the number of characters of the alphabet in each node. It can search a word in the dictionary with the help of the word's prefix. For example, if we assume that all strings are formed from the letters 'a' to 'z' in the English alphabet, each trie node can have a maximum of 26 points.

Trie is also known as the digital tree or prefix tree. The position of a node in the Trie determines the key with which that node is connected.

We use set data structure for occurrence list.

When index is found in Tries, the program will return 
a list of files that contains search words
and number of times a word occurs in file.

we sort the files based on number of times words occur in files

To run the program use

    $ python engine.py

Requirements/Constraints:

1. All the web files given in input.txt must be present in same directory. 
2. Numbers, special characters or alphanumeric words cannot be searched.

Input/Output:


1. input.txt contains link to the few pages that I have used as input, including some links to your other pages of programs. 
2. output.txt contains output of programs.
3. output files contain filename that contain all the words in search text.