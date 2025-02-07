def how_many_can_construct(s, word_list):
    if len(s) == 0:
        return 1
    result = 0
    for word in word_list:
        if word == s[: len(word)]:
            result = result + how_many_can_construct(s[len(word) :], word_list)
    return result

# O((n ^ m) * m) time | O(m * m) space

print(how_many_can_construct("ab", ["a", "b"])) 
print(how_many_can_construct("ab", ["a", "b", "ab"])) 
print(how_many_can_construct("abc", ["a", "b", "c", "ab", "bc", "abc"])) 
print(how_many_can_construct("applepenapple", ["apple","pen"])) 
print(how_many_can_construct("skateboard", ["bo","rd", "ate", "t", "ska", "sk", "boar"])) 
print(how_many_can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee", 
    ])) 