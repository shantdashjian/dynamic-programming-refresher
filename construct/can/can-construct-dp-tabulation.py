def can_construct(s, word_list):
    table = {}
    for i in range(len(s) + 1):
        table[s[:i]] = False
    table[""] = True

    for i in range(len(s) + 1):
        current_key = s[:i]
        if table[current_key]:
            for word in word_list:
                new_key = current_key + word
                if new_key in table:
                    table[new_key] = True
    
    return table[s]

# O(n * m * m) time | O(m * m) space

print(can_construct("ab", ["a", "b"])) 
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) 
print(can_construct("applepenapple", ["apple","pen"])) 
print(can_construct("skateboard", ["bo","rd", "ate", "t", "ska", "sk", "boar"])) 
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee", 
    ])) 