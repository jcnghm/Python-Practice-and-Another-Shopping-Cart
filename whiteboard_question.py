# Shortest Word
# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Example Input: words = ["bitcoin take over the world maybe who knows perhaps"]
# Example Output: 3
# Example Input: words = ["Brady wins again"]
# Example Output: 4

# def shortest_word(words):
#     """
#     Finds the length of the smallest word as an integer
#     """
#     list_words = words.split()
    
#     set_of_length_of_items = {len(item) for item in list_words}
    
#     min_of_set = min(set_of_length_of_items)
#     print(min_of_set)

# shortest_word('How are you doing today')

# # OR One Liner with list comprehension

# def shortest_word(words):
#     return min({len(word) for word in words.split()}) 

# print(shortest_word("Brady wins again"))




# def solution(string):
#     reversedString=('')
#     index = len(string) 
#     while index > 0: 
#         reversedString += string[ index - 1 ] 
#         index = index - 1 
#         reversedString = ''.join(reversed(string))
#     return str(reversedString)

# print(solution('hello'))

class Person():
    def __init__(self, name, age):
        self.info = self
        self.name = name
        self.age = age
        
        return f"{name}s age is {age}"
        
person = Person('josh', '36')

print(person.name)