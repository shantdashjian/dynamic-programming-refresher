def all_the_ways_to_construct(s, word_list, memo = None):
    if memo == None:
        memo = {}
    if s in memo:
        return memo[s]
    if len(s) == 0:
        return [[]]
    all_ways = []
    for word in word_list:
        if word == s[: len(word)]:
            ways = all_the_ways_to_construct(s[len(word) :], word_list, memo)
            for way in ways:
                all_ways.append([word] + way)
    memo[s] = all_ways
    return all_ways

# O((n ^ m) * m) time | O(m * m) space

print(all_the_ways_to_construct("ab", ["a", "b"])) 
print(all_the_ways_to_construct("ab", ["a", "b", "ab"])) 
print(all_the_ways_to_construct("abc", ["a", "b", "c", "ab", "bc", "abc"])) 
print(all_the_ways_to_construct("applepenapple", ["apple","pen", "penapple"])) 
print(all_the_ways_to_construct("skateboard", ["bo","rd", "ate", "t", "ska", "sk", "boar"])) 
print(all_the_ways_to_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee", 
    ])) 