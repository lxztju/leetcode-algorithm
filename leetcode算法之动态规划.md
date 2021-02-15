今天来盘一盘 **动态规划 ** 这类题目

这是最让我头疼的一类题目，一直不想做这类题目，这里开始学习一下。

使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 动态规划
动规就是**以空间换取时间。**

动态规划常常适用于有**重叠子问题和最优子结构**性质的问题。

一些思考的套路： 递归 （自顶向下）——>  记忆化递归（自顶向下消除重复） ——> 动态规划（自底而上）

1. 斐波那契数列

* 70 爬楼梯（easy）
* 198 打家劫舍（easy）
* 213 打家劫舍 II（medium）

2. 矩阵路径

* 64 最小路径和（medium）
* 62 不同路径（medium）

3. 数组区间

* 303 区域和检索 - 数组不可变（easy）
* 413 等差数列划分（medium）

4. 分割整数

* 343  整数拆分（medium）
* 279 完全平方数（medium）
* 91 解码方法（medium）

5. 最长递增子序列

* 300 最长上升子序列（medium）
* 646 最长数对链（medium）
* 376 摆动序列（medium）

6. 最长公共子序列

* 1143 最长公共子序列（medium）


7. 股票交易

* 121 买卖股票的最佳时机（easy）
* 122 买卖股票的最佳时机II（easy）
* 123 买卖股票的最佳时机 III（hard）
* 188 买卖股票的最佳时机 IV（hard）
* 309 最佳买卖股票时机含冷冻期（medium）
* 714 买卖股票的最佳时机含手续费（medium）


8. 字符串编辑

* 583 两个字符串的删除操作（medium）
* 72  编辑距离（hard）
* 650 只有两个键的键盘（medium）


### 1. 斐波那契数列
这类题目是斐波那契数列是最简单的动态规划的问题，对于这类题目，我会**首先使用递归**直观解决问题， **然后利用记忆化递归**的方法去重，**最后使用动态规划**实现自底而上的方法。

#### 70 爬楼梯（easy）
* 递归
* n-1到n有一种方法，第n-2到n有1种方法。
* 因此到达第n阶楼梯的方法为到达第n-1阶的方法与第n-2阶楼梯的方法和

```c++
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        return climbStairs(n-1) + climbStairs(n-2);
    }
};
```

* 记忆化递归
* 因为在上述递归方法种
* 	例如要求 f(10) = f(9) + f(8)，就要求f(9)与f(8)
				 f(9) = f(8) + f(7)
				f(8) = f(7) + f(6)
从上边的分析，可以看出存在大量的重复计算，随着所求数字的增大，重复计算大量的增加，这里采用map来存储已经计算过的元素，例如在求f(9)时f(8)保存下来，然后遇到求f(8)的位置，不进行往下计算，实现递归树的剪枝

```c++
class Solution {
public:
    unordered_map<int, int> memo;
    int climbStairs(int n) {
        if (n <= 2) return n;
        if (memo.find(n) == memo.end())
            memo.insert(make_pair(n, climbStairs(n-1) + climbStairs(n-2)));
        
        return memo[n];
    }
};
```

* 记忆化递归时自上而下的方法， 动态规划是自下而上的方法

```c++
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        vector<int> dp(n+1, 0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i< n+1; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};
```


#### 198 打家劫舍（easy）

* 递归

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        return helper(nums.size() - 1, nums);
    }
    int helper(int n, vector<int>& nums){
        if (n == 0) return nums[0];
        if (n == 1) return max(nums[0], nums[1]);
        // 偷盗第n-1房，与偷盗n房的最值
        return max(helper(n-1, nums), helper(n-2, nums) + nums[n]);
    }
};
```

* 记忆化递归

```c++
class Solution {
public:
    unordered_map<int, int> memo;
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        return helper(nums.size() - 1, nums);
    }
    int helper(int n, vector<int>& nums){
        if (n == 0) return nums[0];
        if (n == 1) return max(nums[0], nums[1]);
        if (memo.find(n-1) == memo.end())
            memo[n-1] = helper(n-1, nums);
        if (memo.find(n-2) == memo.end())
            memo[n-2] = helper(n-2, nums);
        // 偷盗第n-1房，与偷盗n房的最值
        return max(memo[n-1], memo[n-2] + nums[n]);
    }
};
```

* 动态规划

```c++
class Solution {
public:
    unordered_map<int, int> memo;
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i< nums.size(); i++){
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[nums.size() - 1];
    }
};
```


#### 213 打家劫舍 II（medium）
* 这个题与上一题的主要区别在于这里的数组是循环的。
* 直观的思路可以分为两种情况，一种是选择第一间房丢掉最后一间房nums(nums.begin(), nums.end() - 1)，第二种是选择最后一间房丢掉第一间房nums(nums.begin() + 1, nums.end())。在二者中取得最大值即可

* 直接采用动态规划， 懒得用递归了

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp1(nums.size() - 1, 0); //丢掉最后一个 
        vector<int> dp2(nums.size() - 1, 0); // 丢掉第一个元素
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        dp2[0] = nums[1];
        dp2[1] = max(nums[1], nums[2]);
        for (int i = 2; i< nums.size()-1; i++){
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1]);
        }
        return max(dp1[nums.size()-2], dp2[nums.size()-2]);
    }
};
```

### 2. 矩阵路径

这类题目是在一个矩阵中找寻满足题意的路径。

依然采用 递归-> 记忆化递归 -> 动态规划的三种方法来求解这个问题。

#### 64 最小路径和（medium）
* 递归
* 假设f(i,j)为从起始位置到i， j位置的最小路径和，从上边和左边两个方向可以到达i  j 。
* 因此f(i,j) = min(  f(i-1, j), f(i, j-1)  ) + grid[i][j]

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        return pathsum(m-1, n-1, grid);
    }
    int pathsum(int i, int j, vector<vector<int>>& grid){
        if (i == 0 && j == 0) return grid[0][0];
        int left = i-1 >= 0 ? pathsum(i-1, j, grid) : INT_MAX;
        int up = j-1 >= 0 ? pathsum(i, j-1, grid) : INT_MAX;
        return min(left, up) + grid[i][j];
    }
};
```
* 记忆化递归
* 可以直观看出存在大量的重复运算，采用记忆化数组来消除重复计算

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));
        return pathsum(m - 1, n - 1, grid, memo);
    }

    int pathsum(int i, int j, vector<vector<int>>& grid, vector<vector<int>>& memo){
        if (i == 0 && j == 0) return grid[0][0];

        int left = INT_MAX;
        if (i - 1 >= 0){
            if (memo[i-1][j] == -1)
                memo[i-1][j] = pathsum(i-1, j, grid, memo);
            left = memo[i-1][j];
        }

        int up = INT_MAX;
        if (j - 1 >= 0){
            if (memo[i][j - 1] == -1)
                memo[i][j - 1] = pathsum(i, j - 1, grid, memo);
            up = memo[i][j-1];
        }
        return min(left, up) + grid[i][j];
    }
};
```

* 动态规划： 自底而上
```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(grid); // dp[i][j]表示从起始点达到ij的最小的路径和。
        for (int i = 1; i< m; i++){
            dp[i][0] +=dp[i-1][0];
        }
        for (int j = 1; j < n; j++){
            dp[0][j] += dp[0][j-1];
        }
        for (int i = 1; i< m; i++){
            for (int j = 1; j < n; j++){
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
};
```

#### 62 不同路径（medium）
* 直接使用动态规划

```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 1; i< m; i++){
            for (int j = 1; j < n; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```



### 3. 数组区间


#### 303 区域和检索 - 数组不可变（easy）

* 直接使用dp[i][j]保存ij之间的距离, 每次需要的时候直接查找即可。
```c++
class NumArray {

private:
    vector<vector<int>> dp;
public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        dp = vector<vector<int>> (n, vector<int>(n, 0));
        for ( int  i = 0; i < n; i++){
            dp[i][i] = nums[i];
        }
        for (int i = 0; i < n-1; i++){
            for (int j = i+1; j < n; j++){
                dp[i][j] = dp[i][j-1] + nums[j];
            }
        }
    }
    
    int sumRange(int i, int j) {
        return dp[i][j];
    }
};
```


* 也可以使用dp[i]保存起始位置到i的序列和
* ij之间的距离采用dp[j] - dp[i]得到

```c++
class NumArray {

private:
    vector<int> dp;
public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        dp =  vector<int>(n, 0);
        if ( n > 0){
            dp[0] = nums[0];
            for ( int  i = 1; i < n; i++){
                dp[i] = dp[i-1] + nums[i];
            }
        }
    }
    
    int sumRange(int i, int j) {
        if (i == 0) return dp[j];
        return dp[j] - dp[i - 1];
    }
};
```


#### 413 等差数列划分（medium）

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        vector<int> dp(A.size(), 0);
        int res = 0;
        for (int i = 2; i< A.size(); i++){
            if (A[i] + A[i-2] == 2 * A[i-1]){
                dp[i] = dp[i-1] + 1;
                res += dp[i];
            }
        }
        return res;
    }
};
```



### 4. 分割整数


#### 343  整数拆分（medium）
* dp[i]表示i拆分后的最值， dp[i]可以拆分为j, i-j， 那么i-j可以选择继续拆分与否，取最值
* 为什么不考虑j是否拆分呢，考虑递归树即可想明白。
* 考虑一棵直观的递归树。 求dp[n]， 可以分为1*dp[n-1],或者2* dp[n-2] ...... (n-1) * dp[1]。
 
```c++
class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(n + 1, 1);
        dp[0] = 0;
        for (int i = 2; i< n+1; i++){
            for (int j = 1; j < i; j++){
                dp[i] = max(dp[i], max(j * dp[i - j], j * (i-j)));
            }
        }
        return dp[n];
    }
};
```

#### 279 完全平方数（medium）
* dp[i]表示i为结尾的完全平方数
* i分为j与i - j*j， 那么dp[i] = dp[i-j*j] + 1

```c++
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        dp[1] = 1;
        for(int i = 2; i< n+1; i++){
            int tmp = sqrt(i);
            for (int j = 1; j < tmp + 1; j++){
                dp[i] = min(dp[i], dp[i - j * j] + 1 );
            }
            // cout<<dp[i]<<endl;
        }
        return dp[n];
    }
};
```


#### 91 解码方法（medium）
* dp[i]表示从开始到i为止的解码方案
* 分为如下的三种情况：
	* 1. s[i]== '0' 那么这个字符只能与前边的匹 配    dp[i] = dp[i-2]
	* 2. s[i] != '0' && 能与前边字符匹配  dp[i] = dp[i-1] + dp[i-2]
	* 3. s[i] != '0' 并且不能与前置字符匹配 dp[i] = dp[i-1]

```c++
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n+1, 0);
        if (n == 0) return 0;
        if (s[0] - '0' == 0) return 0;
        dp[0] = 1;
        dp[1] = s[0] != '0' ? 1 : 0;
        for (int i = 1; i < s.size(); i++){

            if (patch(s, i) && s[i] == '0')
                dp[i + 1] = dp[i-1];
            else if (s[i] != '0' && patch(s, i))
                dp[i+1] = dp[i] + dp[i-1];
            else if (s[i] != '0' && ! patch(s, i))
                dp[i+1] = dp[i];
        }

        return dp[n];
    }
    bool patch(string& s, int i){
        int tmp1 = s[i-1] - '0';
        int tmp2 = tmp1 * 10 + s[i] - '0';
        if (tmp2 >=10 && tmp2 <= 26)
            return true;
        return false;
    }
};
```



### 5. 最长递增子序列



#### 300 最长上升子序列（medium）
* dp[i]表示以第i元素为结尾的最长上升子列的长度
* dp[i] = max(dp[j]) + 1     并且 nums[i] > nums[j],也就是针对所以小于i的dp子数组，如果nums[j] < nums[i] 那么选择其中最大的加一， 如果全部小于nums[i]，那么dp[i] = 1

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        dp[0] = 1;
        for (int i = 1; i < n; i++){
            for (int j = 0; j < i; j++){
                if (nums[i] > nums[j]){
                    dp[i]  = max(dp[i], dp[j]);
                }
            }
            dp[i]++;
        }
    }
};
```


#### 646 最长数对链（medium）
* 与上一题类似

```c++
class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b){
        if (a[1] == b[1]) return a[0] < b[0];
        return a[1] < b[1];
    } 

    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();

        sort(pairs.begin(), pairs.end(), cmp);  

        vector<int> dp(n, 0);
        dp[0] = 1;
        for (int i = 1; i < n; i++){
            for (int j = 0; j < i; j++){
                if ( pairs[i][0] > pairs[j][1] )
                    dp[i] = max(dp[i], dp[j]);
            }
            dp[i]++;
        }

        return *max_element(dp.begin(), dp.end());
    }
};
```


#### 376 摆动序列（medium）
* 与前两题一致， 这里采用dp[i][0]表示以i为结尾的最长的序列最后一个差值为负数
* 										dp[i][1]最后一个差值为正数

```c++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        if ( n < 2) return n;
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 1;
        dp[0][1] = 1;
        for ( int i = 1; i< n; i++){
            for (int j = 0; j < n; j++){
                if (nums[i] - nums[j] > 0){
                    dp[i][1] = max(dp[i][1], dp[j][0]);
                }
                else if (nums[i] - nums[j] < 0){
                    dp[i][0] = max(dp[i][0], dp[j][1]);
                }
                    
            }
            dp[i][0]++;
            dp[i][1]++;
            res = max(res, max(dp[i][0], dp[i][1]));
        }
        return res;
    }
};
```



### 6. 最长公共子序列

#### 1143 最长公共子序列（medium）
* dp[i][j]表示text1的前i个字符， text2的前j个字符中二者的公共子序列的长度
* 如果text[i] == text2[j]   那么 dp[i][j] = dp[i-1][j-1]+1
* 如果text1[i] != text2[j] 那么： dp[i][j] = max(dp[i-1][j], dp[i][j-1])


```c++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size();
        int n=  text2.size();

        vector<vector<int>>dp(m+1, vector<int>(n+1, 0));
        for (int i = 1; i <= m; i++ ){
            for (int j = 1; j<=n; j++){
                if (text1[i-1] == text2[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
```



### 7. 股票交易
对于这类股票交易的问题，可以使用一个同意的模板来解决这类问题。

* 状态方程为：

```
状态转移方程：
状态方程中的 i 表示第i天， k表示剩余的操作次数(这里以购买作为操作次数的记录）， 0表示不持有股票，1表示持有股票
再第i天不持有股票， 那么其最大利润为上一天不持有股票与上一天持有股票卖掉二者的最大值
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
在第i天持有股票，那么其最大利润为上一天持有股票与上一天不持有股票，然后重新购买二者的最大值
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```

* 边界条件：
```
base case：
#时间从第一天开始
dp[0][k][0] = 0
dp[0][k][1] = -prices[0]

# k为0表示不允许交易
dp[i][0][0] = 0
dp[i][0][1] = -infinity
```

当然利用这种方法进行处理并不一定是最优的，有时候会存在大量的冗余， 这里主要引入这种统一的解决思路


#### 121 买卖股票的最佳时机（easy）

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 这里只能交易一次，因此k为1， 这里就只需要定义二维数组
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for (int i=1; i< n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            // 这里由于只能交易1次。dp[i][0][0] = 0;
            dp[i][1] = max(dp[i-1][1], -prices[i]);
        }
        return dp[n-1][0];
    }
};
```


#### 122 买卖股票的最佳时机II（easy）

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 这里可以交易无数次，因此k不做限制， 这里就只需要定义二维数组
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for (int i=1; i< n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]);
        }
        return dp[n-1][0];
    }
};
```


#### 123 买卖股票的最佳时机 III（hard）

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 这里最多能够完成两笔交易，因此k = 2，需要定义三维数组
        int n = prices.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(3, vector<int>(2, 0)));
        
        for ( int k = 0; k < 3; k++){
            dp[0][k][0] = 0;
            dp[0][k][1] = -prices[0];
        }
        for (int i = 0; i < n; i++){
            dp[i][0][0] = 0;
            dp[i][0][1] = -INT_MAX;
        }
        for ( int i = 1; i< n; i++){
            for (int k = 1; k <3; k++){
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
            }
        }
        return dp[n-1][2][0];
    }
};
```


#### 188 买卖股票的最佳时机 IV（hard）

```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        // 这里最多能够完成k笔交易，需要定义三维数组
        int n = prices.size();
        if (n ==0 || k == 0) return 0;
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(k+1, vector<int>(2, 0)));
        
        for ( int k1 = 0; k1 < k+1; k1++){
            dp[0][k1][0] = 0;
            dp[0][k1][1] = -prices[0];
        }
        for (int i = 0; i < n; i++){
            dp[i][0][0] = 0;
            dp[i][0][1] = -INT_MAX;
        }
        for ( int i = 1; i< n; i++){
            for (int k1 = 1; k1 <k+1; k1++){
                dp[i][k1][0] = max(dp[i-1][k1][0], dp[i-1][k1][1] + prices[i]);
                dp[i][k1][1] = max(dp[i-1][k1][1], dp[i-1][k1-1][0] - prices[i]);
            }
        }
        return dp[n-1][k][0];
    }
};
```


#### 309 最佳买卖股票时机含冷冻期（medium）

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 可以实现无数次的交易，定义二维数组作为dp
        int n = prices.size();
        if ( n == 0 ) return 0;
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        if (n == 1 ) return 0;
        dp[1][0] = max(0, prices[1] - prices[0]);
        dp[1][1] = max(-prices[0], -prices[1]);
        for (int i = 2; i < n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            // 下次购买的时候只能在i-2天不持有的情况下购买
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]);
        }
        return dp[n-1][0];
    }
};
```


#### 714 买卖股票的最佳时机含手续费（medium）

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        // 这里可以交易无数次，因此k不做限制， 这里就只需要定义二维数组
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for (int i=1; i< n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee);
            
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]);
        }
        return dp[n-1][0];
    }
};
```




### 8. 字符串编辑

#### 583 两个字符串的删除操作（medium）

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        // 实际就是求最长公共子序列， 剩余的部分为即为需要操作的部分
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int i = 1; i <= m; i++){
            for (int j = 1; j <= n; j++){
                if (word1[i-1] == word2[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return m + n-2 * dp[m][n];
    }
};
```


#### 72  编辑距离（hard）
* 设dp[i][j]为word1的前i个字符转换为word2的前j个字符所需要的操作数。
* 当word1[i] == word2[j]时候，dp[i][j] = dp[i-1][j-1]
* 当word1[i] != word2[j]时候
	* 如果此时word1[i-1]与 word[j]已经转换完成， 那么此时删除word1[i]即可 此时dp[i][j] = dp[i-1][j] + 1
	* 如果此时word1[i]与 word[j-1]已经转换完成， 那么此时插入word1[i]即可 此时dp[i][j] = dp[i][j-1] + 1
	* 如果此时word1[i-1]与 word[j-1]已经转换完成， 那么此时替换word1[i]即可 此时dp[i][j] = dp[i-1][j-1] + 1
	* 从这三种情况中取得最小值即可

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));

        // 空字符转换为word2
        for (int j = 1; j <= n; j++)
            dp[0][j] = dp[0][j-1] + 1;
        // word1转换为空字符
        for (int i = 1; i <= m; i++)
            dp[i][0] = dp[i-1][0] + 1;

        for (int i = 1; i <= m; i++){
            for (int j = 1; j <= n; j++ ){
                if (word1[i-1] == word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1])) + 1;
            }
        }
        return dp[m][n];
    }
};
```


#### 650 只有两个键的键盘（medium）

* dp[i]表示打印i个A需要的最小的次数。

```c++
class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[1] = 0;
        for (int i = 2; i <= n; i++){
            for (int j = 1; j < i; j++){
                if ( i % j == 0)
                    dp[i] = min(dp[i], dp[j] + i / j);
            }
        }
        return dp[n];
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

