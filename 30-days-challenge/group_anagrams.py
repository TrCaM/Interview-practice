from collections import Counter, defaultdict

A_UNI = ord(a)
TOTAL_LETTERS = 26

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def hash(word):
      counters = [0] * TOTAL_LETTERS
      for c in word:
        counters[ord(c) - A_UNI] += 1

      return counters
    
    words_dict = dict()
    for word in strs:
      key = hash(word)
      if not key in words_dict:
        words_dict[key] = []
      words_dict[key].append(word)

    return list(words_dict.values())

  def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    words_dict = defaultdict(list)
    for word in strs:
      counter = Counter(word)
      key = "#".join([f'{k}{v}' for k, v in sorted(counter.items())])
      words_dict[key].append(word)

    return list(words_dict.values())
