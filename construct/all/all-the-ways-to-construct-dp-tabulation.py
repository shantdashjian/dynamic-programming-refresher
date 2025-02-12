def all_the_ways_to_construct(s, word_list):
    table = [[] for  i in range(len(s) + 1)]
    table[0] = [[]]

    for i in range(len(table) - 1):
        current_key = s[:i]
        if len(table[i]) > 0:
            for word in word_list:
                next_key = current_key + word
                if len(next_key) < len(table) and next_key == s[:len(next_key)]:
                    for option in table[i]:
                        table[len(next_key)].append(option + [word])
    return table[len(s)]

# O(n ^ m * m) time | O(n ^ m) space


print(all_the_ways_to_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])) 
print(all_the_ways_to_construct("ab", ["a", "b"])) 
print(all_the_ways_to_construct("ab", ["a", "b", "ab"])) 
print(all_the_ways_to_construct("abc", ["a", "b", "c", "ab", "bc", "abc"])) 
print(all_the_ways_to_construct("applepenapple", ["apple","pen", "penapple"])) 
print(all_the_ways_to_construct("skateboard", ["bo","rd", "ate", "t", "ska", "sk", "boar"])) 