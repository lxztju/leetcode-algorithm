今天来盘一盘 **贪心算法 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 贪心算法
贪心算法是指每步都选择最优的策略，以此达到全局的最优。**局部最优—>全局最优**

贪心策略的选择必须具备**无后效性**，也就是说某个状态以前的过程不会影响以后的状态，只与当前状态有关。

* 455 分发饼干  (Easy)
* 121 买卖股票的最佳时机  (Easy)
* 122 买卖股票的最佳时机  II (Easy)
* 605 种花问题  (Easy)
* 665 非递减数列 (Easy)
* 53 最大子序和  (Easy)
* 435 无重叠区间 (Medium)
* 452 用最少数量的箭引爆气球 (Medium)
* 406 根据身高重建队列(Medium)
* 763 划分字母区间  (Medium)


#### 455 分发饼干  (Easy)
* 二者排序之后采用双指针比较。
```c++
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // 分别将二者排序
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int i = 0, j = 0;
        int res = 0;
        while (i < g.size() && j < s.size()){
            if (s[j] >= g[i]){
                i++;
                res++;
            }
            j++;
        }
        return res;
    }
};
```

#### 121 买卖股票的最佳时机  (Easy)

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 暴力法
        // 双重循环，从第i天买入可以获得的最大利润，计算最大值
        int maxprofit = 0;
        for ( int i = 0; i < prices.size() - 1; i++){
            for (int j = i + 1; j < prices.size(); j++){
                int profit = prices[j] - prices[i];
                maxprofit = max(profit, maxprofit);
            }
        }
        return maxprofit;
    }
};
```

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 使用minprice变量保存当前天之前的最低价格， 如果在此之前采用最低价格买入，那么当前卖出的利润最大
        int maxprofit = 0;
        int minprice = INT_MAX;
        for(auto price : prices){
            minprice = min(minprice, price);
            maxprofit = max(maxprofit, price - minprice);
        }
        return maxprofit;
    }
};
```

#### 122 买卖股票的最佳时机  II (Easy)
* 与上一题的主要区别就是，可以多次交易
* 也就是当前只要获利为正就可以交易。


```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {   
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};
```

#### 605 种花问题  (Easy)
```c++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // 贪心的种植， 可以种植的位置，直接众，只要左右联测均为0，就可以种植。
        // 需要考虑首尾的两个元素的特殊情况。将首尾各补上0
        int res = 0;
        for (int i = 0; i< flowerbed.size(); i++){
            int left = (i == 0) ? 0 : flowerbed[i-1];
            int right = (i == flowerbed.size()-1) ? 0 : flowerbed[i+1];
            if (left == 0 && right == 0 && flowerbed[i] == 0){
                // cout<<res<<" " <<i<<endl;
                res++;
                flowerbed[i] = 1;
            }
        }
        return res >= n;
    }
};
```
####  665 非递减数列 (Easy)
* 遇到nums[i]>nums[i+1]需要将nums[i]变小或者nums[i+1]变大
* 如果nums[i + 1] < nums[i - 1]，需要将nums[i+1]变大
* 其他情况下nums[i]变小

```c++
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt = 0;
        for (int i = 0; i < nums.size()-1 && cnt < 2; i++) {
            if (nums[i] > nums[i + 1]) {
                cnt++;
                if (i > 0 && nums[i + 1] < nums[i - 1]) {
                    nums[i + 1] = nums[i];
                } 
                else {
                    nums[i] = nums[i + 1];
                }
            }
        }
        return cnt < 2;
    }
};
```
#### 53 最大子序和  (Easy)
```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // 暴力法
        int maxnum = nums[0];
        int tmp = 0;
        for (int i = 0; i < nums.size(); i++){
            tmp = nums[i];
            maxnum = max(maxnum, tmp);
            for (int j = i+1; j < nums.size(); j++){
                tmp += nums[j];
                maxnum = max(maxnum, tmp);
            }
        }
        return maxnum;
    }
};
```


```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // 动态规划
        int maxnum = nums[0];
        vector<int> dp(nums.size(), 0); // dp表示到i位置的最长子序和。
        dp[0] = nums[0];
        for (int i = 1; i< nums.size(); i++){
            dp[i] = max(nums[i], dp[i-1] + nums[i]);
            maxnum = max(dp[i], maxnum);
        }
        
        return maxnum;
    }
};
```

#### 435 无重叠区间 (Medium)
```c++
class Solution {
public:
    // 按照区间右边界排序
    static bool cmp (const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) return 0;
        sort(intervals.begin(), intervals.end(), cmp);

        int cnt = 0;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < intervals[i - 1][1]) {
                cnt++;
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1]);
            }
        }
        return cnt;
    }
};


```
#### 452 用最少数量的箭引爆气球 (Medium)
```c++
class Solution {
public:
    // 按照区间的右端点排序
    static bool cmp(const vector<int>& a, const vector<int>& b){
        return a[1] < b[1];
    }
    int findMinArrowShots(vector<vector<int>>& points) {
        // 与上一题的最大不重叠区间的问题实际是一样的
        if(points.size() < 2) return points.size();
        sort(points.begin(), points.end(), cmp);
        int cnt = 1;
        for (int i = 1; i < points.size(); i++){
            if (points[i][0] > points[i-1][1])
                cnt++;
            else
                points[i][1] = min(points[i][1], points[i-1][1]);
        }
        return cnt;
    }
};
```
#### 406 根据身高重建队列(Medium)
```c++
class Solution {
public:
    static bool cmp(const vector<int> a, const vector<int> b) {
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] > b[0];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort (people.begin(), people.end(), cmp);
        vector<vector<int>> que;
        for (int i = 0; i < people.size(); i++) {
            int position = people[i][1];
            que.insert(que.begin() + position, people[i]);
        }
        return que;
    }
};
```
#### 763 划分字母区间  (Medium)
```c++
class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    }
    vector<int> partitionLabels(string S) {
        // 这个题目实际上还是求最大的不重合区间的个数
        // 首先遍历字符串S，求出每个字符首次与最后一次出现的次数
        // 这样还是一个不重合区间的个数问题

        vector<vector<int>> boards(26, vector<int>(2, -1));
        for (int i = 0; i < S.size(); i++){
            int index = S[i] - 'a';
            if (boards[index][0] == -1){
                boards[index][0] = i;
                boards[index][1] = i;
            }
            else 
                boards[index][1] = i;
        }

        sort(boards.begin(), boards.end(), cmp);

        vector<int> res;

        int i = 0;
        while (i < 26){
            if (boards[i][1] != -1) break;
            i++;
        }

        int min_board = boards[i][0];
        int max_board = boards[i][1];
        // i++;
        while ( i < 26){
            if ( boards[i][0] > max_board){
                res.push_back(max_board - min_board + 1);
                min_board = boards[i][0];
            }

            max_board = max(max_board,boards[i][1]);
            i++;
        }
        res.push_back(max_board - min_board + 1);
        return res;
    }
};
```





## 更多分类刷题资料

* 微信公众号： 小哲AI

  ![wechat_QRcode](https://img-blog.csdnimg.cn/20210104185413204.jpg)

* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [https://blog.csdn.net/lxztju](https://blog.csdn.net/lxztju)
* 知乎专栏： [https://www.zhihu.com/column/c_1101089619118026752](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[https://www.yanxishe.com/column/109](https://www.yanxishe.com/column/109)

