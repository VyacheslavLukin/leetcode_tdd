from longest_substring import Solution
from hypothesis import given, strategies as st

s = Solution()

def test_should_return_zero_for_empty_string():
    assert s.lengthOfLongestSubstring('') == 0

@given(st.text(min_size=5, max_size=5))
def test_should_return_len_of_string(txt):
    assert len(txt) == 5

def test_should_return_substring_at_string_start():
    st = "aaabb"
    assert s.lengthOfLongestSubstring(st) == 3 

def test_should_return_substring_at_end_start():
    st = "aaabbbb"
    assert s.lengthOfLongestSubstring(st) == 4