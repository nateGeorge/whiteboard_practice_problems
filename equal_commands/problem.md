You are given two lists as an input; the first is a list of paired commands as tuples, and the second is a list of synonyms as tuples.  Check for equivalence of the commands, considering the synonyms.  Each word only has one possibly synonym, and synonyms are only one word long.  Return a list of set(True, False), with one entry for each pair of commands.

Example:
Input:
[('eat some apples', 'consume some apples'), ('eat many apples', 'destroy some apples')]
[('eat', 'consume'), ('many', 'lots')]
Output:
[True, False]

What is the big O complexity of your solution?


After completing that, test for equivalence again, but each word may have more than one synonym (i.e. A=B, B=C, so A=C).  Start by assuming only 2 possible synonyms for each word if you're stuck.

Extra hard bonus:
assume synonyms can be mulitple words long, i.e. 'many' and 'a lot'
