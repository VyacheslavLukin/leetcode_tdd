class Solution:

    def lengthOfLongestSubstring(self, input_string: str) -> int:
        if not input_string:
            return 0

        first_letter = input_string[0]
        dict_text = {}
        for letter in input_string:
            if letter in dict_text.keys():
                dict_text[letter] += 1
            else:
                dict_text[letter] = 1
        
        return max(dict_text.values())