class Solution {
public:
    int totalFruit(vector<int>& fruits) 
    {
       unordered_map<int, int> freq;
    int left = 0;
    int best = 0;

    for (int right = 0; right < (int)fruits.size(); right++) {
        freq[fruits[right]]++;

        while ((int)freq.size() > 2) {
            freq[fruits[left]]--;
            if (freq[fruits[left]] == 0) {
                freq.erase(fruits[left]);
            }
            left++;
        }

        best = max(best, right - left + 1);
    }

    return best;
        
    }
};