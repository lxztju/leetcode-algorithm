今天来盘一盘 **动态规划（背包问题） ** 这类题目

这是最让我头疼的一类题目，一直不想做这类题目，这里开始学习一下。

使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 动态规划（背包问题）
动规就是**以空间换取时间。**

0-1背包是背包问题的一个主要的表现形式，在**01背包**的基础上发展出来的还有**完全背包**以及**多维背包**问题。

### 0-1背包

问题描述为： 存在一个容量为 C 的背包，和N类物品。这些物品分别有两个属性，重量w 和价值 v，每个物品的重量为w[i], 价值为v[i]，**每种物品只有一个**。在不超过背包容量的情况下能够装入最大的价值为多少？（这个背包可以不装满）。

如果采用暴力法，每个物品都有装入与不装入两种情况，复杂度为2的n次幂，复杂度为指数级别的复杂度。如果使用动态规划，时间复杂度会降低至O（N*C）。

```
dp[i][j] 为将前i件物品装进容量为j的背包可以获得的最大价值, 0<=i<=N, 0<=j<=C

dp表为(N+1)x(C+1)维的二维数组
```

* 状态转移方程

```
1. 不装入第i件物品时，dp[i][j] = dp[i-1][j];
2. 装入第i件物品，dp[i][j] = dp[i-1][ j-w[i] ] + v[i];  (j > w[i] 背包的容量大于w[i])
状态转移方程：
	dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])  
```

* base case

```
第0个物品时不存在的，价值为0。
dp[0][:] = 0;
```

* 基本的实现过程：

```
// 定义dp
vector<vector<int>> dp(N+1, vector<int>(C+1, 0))

// 定义base case
for (int j = 0; j < c+1; j++)
	dp[0][j] = 0;
// 执行状态转移
for (int i = 1; i < N+1; i++){
	for (int j = C; j >= 0; j--){
		dp[i][j] = dp[i-1][j];
		if (j >= w[i])
			dp[i][j]  = max(dp[i][j], dp[i-1][j-w[i]] + v[i]);	
	}
}
return dp[N][C];
```


* **优化的实现过程（dp采用一维数组）**

```c++
初始dp[j]均为0
for (int i = 1; i < N+1; i++){
	for (int j = C; j >= 0; j--){
		if (j >= w[i])
			dp[j]  = max(dp[j], dp[j-w[i]] + v[i]);	
	}
}
```


### 完全背包
问题描述为： 存在一个容量为 C 的背包，和N类物品。这些物品分别有两个属性，重量w 和价值 v，每种物品的重量为w[i], 价值为v[i]，**每种物品有无穷多个**。在不超过背包容量的情况下能够装入最大的价值为多少？（这个背包可以不装满）。


```
dp[i][j] 为将前i件物品装进容量为j的背包可以获得的最大价值, 0<=i<=N, 0<=j<=C

dp表为(N+1)x（C+1）维的二维数组
```

完全背包与01背包的思路基本一致，只是每种物品可以有无限多个，因此每次装入第i种物品后，还能继续装入i种物品。


* 状态转移方程

```
1. 不装入第i种物品时，dp[i][j] = dp[i-1][j];
2. 装入第i件物品，dp[i][j] = dp[i][ j-w[i] ] + v[i];  (j > w[i] 背包的容量大于w[i])
状态转移方程：
	dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])  
```

* base case

```
第0个物品时不存在的，价值为0。
dp[0][:] = 0;
```


* 基本的实现过程：

```
// 定义dp
vector<vector<int>> dp(N+1, vector<int>(C+1, 0))

// 定义base case
for (int j = 0; j < c+1; j++)
	dp[0][j] = 0;
// 执行状态转移
for (int i = 1; i < N+1; i++){
	for (int j = 0; j <=C ; j++){
		dp[i][j] = dp[i-1][j];
		if (j >= w[i])
			dp[i][j]  = max(dp[i][j], dp[i][j-w[i]] + v[i]);	
	}
}
return dp[N][C];
```

* **优化的实现过程（dp采用一维数组）**

```c++
初始dp[j]均为0
for (int i = 1; i < N+1; i++){
	for (int j = 0; j <= C; j++){
		if (j >= w[i])
			dp[j]  = max(dp[j], dp[j-w[i]] + v[i]);	
	}
}
```

### 多重背包

问题描述为： 存在一个容量为 C 的背包，和N类物品。这些物品分别有三个属性，重量w ，价值 v和数量n，每种物品的重量为w[i], 价值为v[i]，**每种物品分别有n[i]个**。在不超过背包容量的情况下能够装入最大的价值为多少？（这个背包可以不装满）。


与前边的01背包类似，不同之处在于第i件物品的数目为n[i]，这里的分析思路就是针对第i种物品，分别可以装入0，1，2，3, ... ,n[i]件（同时还得满足不能超过背包的容量）。


```
dp[i][j] 为将前i件物品装进容量为j的背包可以获得的最大价值, 0<=i<=N, 0<=j<=C

dp表为(N+1)x（C+1）维的二维数组
```



* 状态转移方程

```
1. 不装入第i种物品时，dp[i][j] = dp[i-1][j];

2. 对于第i种物品， k为装入第i种物品的件数, k <= min(n[i], j/w[i])
dp[i][j] = max{(dp[i-1][j − k*w[i]] + k*v[i]) for i in range(k)}

	dp[i][j] = max(dp[i][j], dp[i][j-k* w[i]]+ k* v[i])  
```

* base case

```
第0个物品时不存在的，价值为0。
dp[0][:] = 0;
```


* 基本的实现过程：

```
// 定义dp
vector<vector<int>> dp(N+1, vector<int>(C+1, 0))

// 定义base case
for (int j = 0; j < c+1; j++)
	dp[0][j] = 0;
	
// 执行状态转移
for (int i = 1; i < N+1; i++){
	for (int j = C; j >=0 ; j--){
		dp[i][j] = dp[i-1][j];
		int tmp = min(n[i], j / w[i]);
		for (int k = 0; k<=tmp; k++){
			dp[i][j]  = max(dp[i][j], dp[i][j-k*w[i]] + k*v[i]);	
		}
	}
}
return dp[N][C];
```


* **优化的实现过程（dp采用一维数组）**

```c++
初始dp[j]均为0
for (int i = 1; i < N+1; i++){
	for (int j = C; j >= 0; j--){
	
		int tmp = min(n[i], j / w[i]);
		
		for (int k = 0; k<=tmp; k++){
			dp[j]  = max(dp[j], dp[j-k*w[i]] + k*v[i]);	
		}
	}
}
```


* 416 分割等和子集（medium）
* 494 目标和（medium）
* 474 一和零（medium）
* 322 零钱兑换（medium）
* 518 零钱兑换 II（medium）
* 139 单词拆分（medium）
* 377 组合总和 Ⅳ（medium）



#### 416 分割等和子集（medium）
* 01背包问题

```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if ( n < 2) return false;
        int numsSum = 0;
        for (auto num: nums) numsSum += num;
        if (numsSum %2 != 0) return false;
        int target = numsSum / 2;
        // 这就是一个01背包问题， 背包的容量为target， 能否恰好装满这个背包
        // nums数组的每个元素就是一种物品，nums[i]即为第i种物品的重量。
        vector<vector<bool>> dp(n+1, vector<bool>(target+1, false));
        dp[0][0] = true;
        for(int i = 1; i <= n; i++){
            for (int j = target; j>=0; j--){
                dp[i][j] = dp[i-1][j];
                if (j >= nums[i-1])
                    dp[i][j] = dp[i][j] || dp[i-1][j-nums[i-1]];
                if (dp[i][target] == true)
                    return true;
            }
        }
        return false;
    }
};
```

* 优化后的一维数组解决方案

```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if ( n < 2) return false;
        int numsSum = 0;
        for (auto num: nums) numsSum += num;
        if (numsSum %2 != 0) return false;
        int target = numsSum / 2;
        // 这就是一个01背包问题， 背包的容量为target， 能否恰好装满这个背包
        // nums数组的每个元素就是一种物品，nums[i]即为第i种物品的重量。
        vector<bool>dp (target+1, false);
        dp[0] = true;
        for(int i = 1; i <= n; i++){
            for (int j = target; j>=0; j--){
                if (j >= nums[i-1])
                    dp[j] = dp[j] || dp[j-nums[i-1]];
                if (dp[target] == true)
                    return true;
            }
        }
        return false;
    }
};
```



#### 494 目标和（medium）
* 01 背包问题， 求方案数目
* sum(P) - sum(N) = target
* sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
* 2 * sum(P) = target + sum(nums)
*  target为计算后的target，找子序列和为target的个数
* 背包容量为target，物品重量为元素的值

```c++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for(int &num: nums) sum += num;
        if(S > sum || sum < -S) return 0; 
        if((S + sum) % 2 != 0) return 0; 
        int target = (S + sum) / 2;

        vector<int>dp(target + 1, 0);

        dp[0] = 1;
        for(int i = 1; i <= nums.size(); i++)
            for(int j = target; j >= nums[i-1]; j--)
                dp[j] = dp[j] + dp[j - nums[i-1]];

        return dp[target];
    }
};
```


#### 474 一和零（medium）
* 01背包问题， 二维背包问题
* 背包的容量为m与n
* 每个物品的重量为0的个数与1的个数
* 每个物品的价值均为1， 求价值最大问题。
* dp[j][k] = max(dp[j][k], dp[j-nums[i][0]][k - nums[i][1])

```c++
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> nums(strs.size(), vector<int>(2, 0));
        int num0 = 0, num1 = 0;
        for(int i = 0; i<strs.size(); i++){
            nums[i][0] = count(strs[i].begin(), strs[i].end(), '0');
            nums[i][1] = count(strs[i].begin(), strs[i].end(), '1');
            num0 += nums[i][0];
            num1 += nums[i][1];
        }
        for (auto s: nums)
            cout<<s[0] << "  "<< s[1]<<endl;

        if (num0 == m && num1 == n) return nums.size();

        vector<vector<int>> dp (m+1, vector<int>(n+1, 0));
        for (int i = 0; i < nums.size(); i++){
            for (int j = m; j >= nums[i][0]; j--){
                for (int k = n; k >= nums[i][1]; k--){
                    dp[j][k] = max(dp[j][k], dp[j - nums[i][0]][k - nums[i][1]] + 1);
                }
            }
        }
        return dp[m][n];
    }
};
```


#### 322 零钱兑换（medium）
* 完全背包问题
* 背包容量为amount
* 每件物品的重量为coins[i]， 每件物品的价值为1， 求刚好装满背包的物品的价值最小。
* dp[j] = min(dp[j], dp[j-coins[i-1]]+1)

```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        vector<int> dp(amount+1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i < coins.size() + 1; i++){
            for (int j = coins[i-1]; j <= amount; j++){
                if(dp[j] - 1 > dp[j - coins[i-1]])
                    dp[j] = min(dp[j], 1 + dp[j - coins[i-1]]);   
            }
        }
        return dp[amount]==INT_MAX ? -1 : dp[amount];
    }
};
```


#### 518 零钱兑换 II（medium）
* 完全背包问题
* 背包的容量为amount， 每个物品的重量为coins[i]，求刚好装满背包的方案数
* dp[j] = sum(dp[j] + dp[j-coins[i-1]])

```c++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n = coins.size();
        vector<int> dp(amount+1, 0);
        dp[0] = 1;
        for (int i = 1; i< n+1; i++){
            for (int j = coins[i-1]; j<= amount; j++)
                dp[j] = dp[j] + dp[j- coins[i-1]];
        }
        return dp[amount];
    }
};
```



* 接下来的这两道题，需要考虑输出的顺序，因此循环遍历的顺序与前边几道题不一致，外层遍历背包，内层遍历物品

#### 139 单词拆分（medium）
* 完全背包
* 物品就是单词字典，每个物品可以有无数个， 背包就是字符串， 看能否完全装满背包

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); i++){ // 遍历背包
            for (int j = 0; j < i; j++){  // 遍历物品
                string word = s.substr(j, i - j); // 
                if (wordSet.find(word) != wordSet.end())
                    dp[i] = dp[i] || dp[j];
            }
        }
        return dp[s.size()];
    }
};
```


#### 377 组合总和 Ⅳ（medium）
* 完全背包问题
* 物品的重量为nums[i]，背包容量为target， 刚好装满背包的组合数
* dp[j] = sum(dp[j], dp[j-nums[i-1]])

```c++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> dp(target+1, 0);
        dp[0] = 1;
        for (int i = 0; i < target+1; i++){ // 遍历背包
            for (int j = 1; j < n+1; j++ ){ // 遍历物品
                if ( i >= nums[j-1])
                    dp[i] = (dp[i] >= INT_MAX - dp[i-nums[j-1]]) ? INT_MAX : dp[i] + dp[i-nums[j-1]];
            }
        }
        return dp[target];
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

