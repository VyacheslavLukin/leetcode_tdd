class Solution:

    def __init__(self, input_string: str) -> None:
        self.str = input_string
        self.text_dict = {}
        self.substring = self.find_substring() if self.str else ""

    def length_longest_substring(self) -> int:
        if not self.str:
            res = 0
        else: 
            res = len(self.substring)
        return res
    
    def get_substring(self) -> str:
        return self.substring

    def find_substring(self) -> bool:
        def cmp_counter_in_tuple(tup: tuple) -> int:
            return tup[1]

        self.text_dict = {}
        for letter in self.str:
            if letter in self.text_dict.keys():
                self.text_dict[letter] = (self.text_dict[letter][0] + letter, self.text_dict[letter][1] + 1)
            else:
                self.text_dict[letter] = (letter, 1)

        max_key =  max(self.text_dict.values(), key=cmp_counter_in_tuple)
        substring = max_key[0]
        return substring

if __name__ == "__main__":
    s = Solution("aaabb")
    print(s.length_longest_substring())