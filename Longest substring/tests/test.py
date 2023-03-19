import string
from longest_substring import Solution

start_st = "aaabb"
end_st = "aaabbbb"
mid_st = "aaazzzzzzzzbbbb"

def test_should_return_zero_for_empty_string():
    s = Solution("")
    assert s.length_longest_substring() == 0

def test_should_return_len_substring_at_beginnig():
    s = Solution(start_st)
    assert s.length_longest_substring() == 3 

def test_should_return_len_substring_at_end():
    s = Solution(end_st)
    assert s.length_longest_substring() == 4

def test_should_return_len_substring_at_middle():
    s = Solution(mid_st)
    assert s.length_longest_substring() == 8

def test_should_return_empty_substring():
    s = Solution("")
    assert s.get_substring() == ""

def test_should_return_substring_at_beginning():
    s = Solution(start_st)
    assert s.get_substring() == "aaa"