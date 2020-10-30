> 题目来源： [leetcode官网](https://leetcode-cn.com/problemset/all/)
> 代码语言： c++
> 作者:   小哲
> github: https://github.com/lxztju/leetcode-python

更多python分类刷题题解代码：请参考[github](https://github.com/lxztju/leetcode-python),   [知乎](https://zhuanlan.zhihu.com/c_1218480100364447744)

### [剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)


```c++
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i=1; i< nums.size(); i++)
        {
            if (nums[i] == nums[i-1])
                return nums[i];
        }
        return 0;
    }
};



class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        //hashset
        unordered_set<int> hashset;
        for (int i = 0; i< nums.size(); i++)
        {
            auto findnum = hashset.find(nums[i]);
            if (findnum != hashset.end())
                return nums[i];  
            hashset.insert(nums[i]);
        }
        return 0;
    }
};
```



更多python分类刷题题解代码：请参考[github](https://github.com/lxztju/leetcode-python),   [知乎](https://zhuanlan.zhihu.com/c_1218480100364447744)
