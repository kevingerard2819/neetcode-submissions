class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        unordered_map<char, int> freq;
        int left = 0 ;
        int best = 0;
        int n = s.size();
        for(int right = 0 ; right < n; right ++)
        {
            freq[s[right]]++;

            while(freq[s[right]] > 1)
            {
                freq[s[left]]--;
                left++;
            }
            
            best = max(best, right - left+1);

        }
        return best;

    }
};
