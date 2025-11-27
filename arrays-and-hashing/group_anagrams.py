from typing import List
from collections import defaultdict

def groupAnagramsASCII(strs: List[str]) -> List[List[str]]:

    group_anagrams = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        
        group_anagrams[tuple(counts)].append(s)
    
    return group_anagrams.values()

def groupAnagramsChar(strs: List[str]) -> List[List[str]]:

    group_anagrams = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        group_anagrams[key].append(word)
    return list(group_anagrams.values())



if __name__ == "__main__":
    input_strs = input("Enter a list of strings separated by spaces: ")
    strs_list = input_strs.split()

    result = groupAnagramsChar(strs_list)
    print("Grouped anagrams:", list(result))