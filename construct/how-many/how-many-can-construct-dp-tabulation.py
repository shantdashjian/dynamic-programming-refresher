def how_many_can_construct(s, word_list):
    table = {}
    for i in range(len(s) + 1):
        table[s[:i]] = 0
    table[""] = 1

    for i in range(len(s) + 1):
        current_key = s[:i]
        if table[current_key] > 0:
            for word in word_list:
                new_key = current_key + word
                if new_key in table:
                    table[new_key] += table[current_key]
    
    return table[s]

# O(n * m * m) time | O(m * m) space

print(how_many_can_construct("ab", ["a", "b"])) 
print(how_many_can_construct("ab", ["a", "b", "ab"])) 
print(how_many_can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) 
print(how_many_can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"])) 
print(how_many_can_construct("purple", ["purp","p", "ur", "le", "purpl"])) 
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