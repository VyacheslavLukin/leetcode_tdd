import string
from longest_substring import Solution
from hypothesis import given, strategies as st

start_st = "aaabb"
end_st = "aaabbbb"
mid_st = "aaazzzzzzzzbbbb"

def test_should_return_zero_for_empty_string():
    s = Solution("")
    assert s.lengthOfLongestSubstring() == 0

def test_should_return_len_substring_at_start():
    s = Solution(start_st)
    assert s.lengthOfLongestSubstring() == 3 

def test_should_return_len_substring_at_end():
    s = Solution(end_st)
    assert s.lengthOfLongestSubstring() == 4

def test_should_return_len_substring_at_middle():
    s = Solution(mid_st)
    assert s.lengthOfLongestSubstring() == 8

def test_should_return_empty_substring():
    s = Solution("")
    assert s.get_substring() == ""