'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
'''

#This is the first way.
#Counter will change something to a dictionary and supply the missing value.

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctransom = Counter(ransomNote)
        ctmagazine = Counter(magazine)
        for item in ctransom:
            if ctransom[item] > ctmagazine[item]:
                return False
        return True
'''

#This is the second way.
from collections import defaultdict

def canConstruct(ransomNote, magazine):
    ransomdict =defaultdict(int)    #defaultdict supplies the missing value
    for item in ransomNote:
        if item in ransomdict:
            ransomdict[item]+=1
        else:
            ransomdict[item]=1


    magadict =defaultdict(int)

    for item in magazine:
        if item in magadict:
            magadict[item]+=1
        else:
            magadict[item]=1



    for item in ransomdict:
        if ransomdict[item] >magadict[item]:
            return False
    return True

print (canConstruct(ransomNote='abcdsgsfg', magazine='afgbcd'))
