def all_the_ways_to_construct(s, word_list):
    if len(s) == 0:
        return [[]]
    all_ways = []
    for word in word_list:
        if word == s[: len(word)]:
            ways = all_the_ways_to_construct(s[len(word) :], word_list)
            for way in ways:
                all_ways.append([word] + way)
    return all_ways

# O((n ^ m) * m) time | O(n ^ m) space

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
print(all_the_ways_to_construct("eeeeeeeeeeee", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee", 
    ])) 