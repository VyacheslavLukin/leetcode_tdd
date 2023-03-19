class Solution:

    def __init__(self, input_string: str) -> None:
        self.str = input_string
        self.substring = ""

    def lengthOfLongestSubstring(self) -> int:
        if not self.str:
            return 0

        dict_text = {}
        for letter in self.str:
            if letter in dict_text.keys():
                dict_text[letter] += 1
            else:
                dict_text[letter] = 1
        
        return max(dict_text.values())
    
    def get_substring(self) -> str:
        return self.substring