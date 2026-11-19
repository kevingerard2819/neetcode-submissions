class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create dictionaries to count the frequency of each character in both strings
        char_count_s = {}
        char_count_t = {}
        
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # Compare the two dictionaries
        return char_count_s == char_count_t

# Example usage:
solution = Solution()
s = "listen"
t = "silent"
print(solution.isAnagram(s, t))  # Output: True
      