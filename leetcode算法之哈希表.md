今天来盘一盘 **哈希表** 这类题目


分类别解析leetcode上的一些相关的例题路，代码采用**C++与python**实现。



## 哈希表
哈希表是一种很有用的数据结构,  其作用主要是**以空间换时间**, 在c++中主要是unordered_set与unordered_map,在python中主要是set与dict.


* 1 两数之和   (Easy)
* 217 存在重复元素   (Easy)
* 594 最长和谐子序列   (Easy)
* 128 	最长连续序列   (Hard)
* 349 两个数组的交集（easy）
* 350 两个数组的交集 II（easy）
* 242 有效的字母异位词（easy）
* 202 快乐数（easy）
* 205 同构字符串（easy）
* 451 根据字符出现频率排序（medium）
* 15 三数之和（medium）
* 18 四数之和（medium）
* 454 四数相加 II（medium）
* 49 字母异位词分组（medium）
* 447 回旋镖的数量（easy）
* 219 存在重复元素 II（easy）


#### 1 两数之和   (Easy)

> 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
> 
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍


* 题解:
	* 1. 使用哈希表(unordered_map)存储访问过的元素,这道题需要返回索引,因此键为元素的值,值为其对应的索引.
	* 2. 遍历整个数组,对于nums[i],  如果target-nums[i]存在于哈希表中,那就说明找到了这两个数.
	* 3. 如果target - nums[i]不在哈希表中就将nums[i]存在哈希表中.

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 定义哈希表
        unordered_map<int, int> visited;
        for(int i = 0; i < nums.size(); i++){
            int tmp = target - nums[i];
            if (visited.find(tmp) != visited.end())
                return {i, visited[tmp]};
            else
                visited.insert(make_pair(nums[i], i));
        }
        return {};
    }
};
```


#### 217 存在重复元素   (Easy)

* 题解1:
	* 简单使用哈希表存储访问过的元素,然后依次判断遍历的元素是否被访问过.

* 题解2: 
	* 排序,然后查找是否有相邻的相等元素.

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // 使用unordered_set存储访问过的元素.
        unordered_set<int> visited;
        for (auto num: nums){
            if (visited.find(num) != visited.end())
                return true;
            visited.insert(num);
        }
        return false;
    }
};
```

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.size() < 2) return false;
        // 排序.
        sort(nums.begin(), nums.end());
        for (int i = 1; i< nums.size(); i++){
            if (nums[i] == nums[i-1])
                return true;
        }
        return false;
    }
};
```


#### 594 最长和谐子序列  (Easy)

> 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
> 
> 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度

* 题解:
	* 遍历一遍vector,使用哈希表存储每个数字出现的次数
	* 遍历哈希表,找相邻数字出现次数之和最大.


```c++
class Solution {
public:
    int findLHS(vector<int>& nums) {
        // 遍历一遍存储每个字符出现的次数
        // 判断相邻数目最大的和.
        unordered_map<int, int> numCnt;
        int res = 0;
        for (auto num: nums){
            if (numCnt.find(num) == numCnt.end())
                numCnt.insert(make_pair(num, 1));
            else
                numCnt[num]++;
        }
        for (auto e = numCnt.begin(); e != numCnt.end(); e++){
            if (numCnt.find(e->first+1) == numCnt.end())
                continue;
            else
                res = max(res, e->second + numCnt[e->first+1]);
        }
        return res;
    }
};
```


#### 128 最长连续序列  (Hard)

* 题解1 : 哈希暴力法(超时)
	* 将数组中所有的元素存入unordered_set中
	* 遍历数组,以每个元素作为开头,找寻连续子列的长度
	* 保存最长的长度

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 暴力法.直接以每个数字为开头,遍历所有的元素,找寻最长的子列, 超时
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int max_length = 0;
        for (auto num: nums){
            int length = 0;
            int tmp = num;
            while (nums_set.find(tmp) != nums_set.end()){
                tmp++;
                length++;
            }
            max_length = max(max_length, length);
        }
        return max_length;
    }
};
```

* 题解2: 找寻合适开头去重
	* 上边的方法以数组中每个元素均作为开头进行处理,存在大量重复计算
	* 针对数组中的元素, 如果其减一之后的数字,依然存在数组中,说明其不适合作为开头,跳过这个元素.

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 直接采用暴力法以每个字符为开头,期间包含很多重复不必要的工作
        // 因此需要找到一个合适的开头进行扫描,如果元素减一存在于数组中,那么说明不能以这个字符作为开头
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int max_length = 0;
        for (auto num: nums){
            int tmp = num;
            if (nums_set.find(--num) != nums_set.end()) continue;

            int length = 0;
            while (nums_set.find(tmp) != nums_set.end()){
                tmp++;
                length++;
            }
            max_length = max(max_length, length);
        }
        return max_length;
    }
};
```


#### 349 两个数组的交集（easy）
* 题解:  哈希表
	* 将其中较短的数组存入unordered_set中
	* 遍历另一个数组中的元素是否在这个哈希表中,记录存在的元素
	* 如果发现一个元素存在哈希表中需要删除这个元素,防止重复.

```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        if (nums1.size() > nums2.size()){
            unordered_set<int> nums_set(nums2.begin(), nums2.end());
            for (auto num: nums1){
                if (nums_set.find(num) != nums_set.end()){
                    res.push_back(num);
                    nums_set.erase(num);
                }
            }
        }
        else{
            unordered_set<int> nums_set(nums1.begin(), nums1.end());
            for (auto num: nums2){
                if (nums_set.find(num) != nums_set.end()){
                    res.push_back(num);
                    nums_set.erase(num);
                }
            }            
        }
        return res;
    }
};
```

#### 350 两个数组的交集 II（easy）
* 题解:
	* 需要统计重复数字出现的数目,因此采用unordered_map统计数组中的元素数目

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        //使用两个unordered_map分别记录两个数组中出现的次数的最大值.
        unordered_map<int, int> nums1_map;
        unordered_map<int, int> nums2_map;
        vector<int> res;
        for(auto num: nums1)
            nums1_map[num]++;
        for (auto num: nums2)
            nums2_map[num]++;

        for (auto e=nums1_map.begin(); e!= nums1_map.end(); e++){
            if (nums2_map.find(e->first) != nums2_map.end()){
                int cnt = min(nums2_map[e->first], e->second);
                for(int i = 0; i< cnt; i++)
                    res.push_back(e->first);
            }
        }
        return res;
    }
};
```
#### 242 有效的字母异位词（easy）
* 题解:
	* 使用哈希表统计两个字符串中每个字符出现的次数
	* 对比两个哈希表的内容是否相同

```c++

class Solution {
public:
    bool isAnagram(string s, string t) {
        // 直接使用哈希表进行遍历对比即可. 
        // 使用map统计么个字符出现的次数,可以仅仅使用一个map
        if (s.size() != t.size()) return false;
        unordered_map<int, int> scnt;
        for (auto s_substring : s){
            scnt[s_substring]++;
        } 
        for (auto t_substring : t){
            if (scnt[t_substring] < 0) return false;
            scnt[t_substring]--;
        }

        for (auto e=scnt.begin(); e!=scnt.end(); e++){
            if (e->second != 0) return false;
        }
        return true;
    }
};
```
#### 202 快乐数（easy）
* 题解:
	* 使用哈希表保存已经访问过的元素
	* 如果下一个的和,已经出现过,说明出现了死循环,这就不是快乐数

```c++

class Solution {
public:
    bool isHappy(int n) {
        // 使用哈希表保存已经访问过的元素, 防止出现死循环
        unordered_set<int> visited;
        int res = n;
        while (true){
            if (res == 1) return true;
            else if (visited.find(res) != visited.end()){
                return false;
            }
            int dec = res;
            visited.insert(res);
            int sum_values = 0;
            while (dec){
                int re = dec % 10;
                dec /= 10;
                sum_values += pow(re, 2);
                res = sum_values;
            }
        }
    }
    
};
```
#### 205 同构字符串（easy）

```c++

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, char> s2t;
        unordered_map<char, char> t2s;
        int len = s.size();
        for (int i = 0; i < len; ++i) {
            char x = s[i], y = t[i];
            if ((s2t.find(x)!= s2t.end() && s2t[x] != y) || (t2s.find(y) != t2s.end() && t2s[y] != x)) {
                return false;
            }
            s2t[x] = y;
            t2s[y] = x;
        }
        return true;
    }
};
```
#### 451 根据字符出现频率排序（medium）
* 题解:
	* 使用unordered_map保存每个字符出现的次数
	* 将map中对应的pair保存至vector中
	* 根据pair的第二个参数(数字)进行sort排序
	* 保存string结果

```c++

class Solution {
public:
    string frequencySort(string s) {
        // 使用map保存每个字符出现的次数
        // 采用vector保存结果并进行排序
        // 返回string格式的结果
        unordered_map<char, int> snum;
        for (auto chr : s){
            snum[chr]++;
        }
        string res;
        res = sortfreq(snum);
        return res;
    }
    string sortfreq(unordered_map<char, int>& snum){
        vector<pair<char, int>> snumpair;
        string s;
        for (auto e = snum.begin(); e!=snum.end(); e++){
            snumpair.push_back(make_pair(e->first, e->second));
        }
        sort(snumpair.begin(), snumpair.end(), freqdecend);
        for (auto spair: snumpair){
            string c1(spair.second, spair.first);
            s += c1;
        }
        return s;
    }
    // 排序的谓词
    static bool freqdecend(pair<char,int>&s1, pair<char, int>& s2){
        return s1.second > s2.second;
    }
};
```
#### 15 三数之和（medium）
* 题解1:暴力法,  时间复杂度n^3
	*  直接三重循环,找到三个数字
	* 其中需要考虑重复的情况,因此在开始的时候将整个数组排序去重.
```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 暴力法,三层循环
        vector< vector<int> > res;
        if (nums.size() < 3) return {};
        sort(nums.begin(), nums.end());
        for (int i=0; i < nums.size()-2; i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j=i+1; j<nums.size()-1; j++){
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                for (int k=j+1; k<nums.size(); k++){
                    if (k > j+1 && nums[k] == nums[k-1]) continue;
                    if (nums[i] + nums[j] + nums[k] == 0)
                        res.push_back({nums[i], nums[j], nums[k]});
                }
            }
        }
        return res;
    }
};
```

* 题解2: 排序后的双指针

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 哈希表,时间换空间.
        vector< vector<int> > res;
        if (nums.size() < 3) return {};

        sort(nums.begin(), nums.end());

        for (int i=0; i < nums.size()-2; i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int target = -nums[i]; // 这就变成了两数之和为target的问题.
            int l = i+1, r = nums.size() - 1;
            while (l < r){
                // cout<< l<< "  "<< r<<endl;
                if (l > i+1 && nums[l] == nums[l-1]) {
                    l++; 
                    continue;
                }
                if (r < nums.size() - 1 && nums[r] == nums[r+1]){
                    r--;
                    continue;
                }
                if (nums[l] + nums[r] == target){
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++; r--;
                }
                else if (nums[l] + nums[r] < target)
                    l++;
                else
                    r--;
            }

        }
        return res;
    }
};

```

#### 18 四数之和（medium）
* 题解:
	* 同上一题一样, 排序加上双指针

```c++

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4) return {};
        vector< vector<int> > res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;

            for (int j = i+1; j < nums.size() - 2; j++){
                if (j > i+1 && nums[j] == nums[j-1]) continue;

                int t = target - nums[i] - nums[j];
                int l = j+1, r = nums.size() -1;
                while (l < r){
                    if (l >j+1 && nums[l] == nums[l-1]){
                        l++;
                        continue;
                    }
                    if (r < nums.size()-1 && nums[r] == nums[r+1]){
                        r--;
                        continue;
                    }
                    if (nums[l] + nums[r] == t){
                        res.push_back({nums[i], nums[j], nums[l], nums[r]});
                        l++;
                        r--;
                    }
                    else if(nums[l] + nums[r] < t)
                        l++;
                    else
                        r--;
                }
            }
        } 
        return res;
    }
};
```
#### 454 四数相加 II（medium）
* 题解:暴力法,超时, 时间复杂度n^4

```c++
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        // 直接暴力法,先试试
        int res = 0;
        for (auto numA : A){
            for (auto numB: B){
                for (auto numC: C){
                    for (auto numD: D){
                        if(numA+ numB + numC+ numD == 0){
                            res++;
                        }
                    }
                }
            }
        }
        return res;
    }
};
```


* 题解:
	* 将AB作为一组,将CD作为一组,
	* 使用map分别保存每个组合的和与对应的数目
	* 最终和为0的总次数由两个map中互为相反数的键的乘积得到.
```c++
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        // 直接暴力法,先试试
        int res = 0;
        unordered_map<int, int> AB_num;
        unordered_map<int, int> CD_num;
        for (auto numA : A){
            for (auto numB: B){
                AB_num[numA+numB]++;
            }
        }
        for (auto numC : C){
            for (auto numD: D){
                CD_num[numC+numD]++;
            }
        }
        
        for (auto e = AB_num.begin(); e!=AB_num.end(); e++){
            res += (e->second) * CD_num[(-(e->first))];
        }
        
        return res;
    }
};
```

#### 49 字母异位词分组（medium）
* 题解:
	* 排序, 然后直接使用map存储对应的string即可.
```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > code2s;
        vector<vector<string>> res;
        for (string& s: strs){
            string key =  s;
            sort(key.begin(), key.end());
            code2s[key].push_back(s);
        }
        for (auto e = code2s.begin(); e!= code2s.end(); e++){
            res.push_back(e->second);
        }
        return res;
    }
};
```
#### 447 回旋镖的数量（easy）
* 题解:
	* 以每个点为起始点, 使用map统计这个点与其他点距离的数目.
	* 同一个距离的回旋镖的数目为n*(n-1), n为距离的数目.


```c++

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int res = 0;
        for (auto p : points) {
            unordered_map<int, int> dist2num;
            for (auto q : points) {
                int dx = p[0]-q[0];
                int dy = p[1]-q[1];
                dist2num[pow(dy, 2)+pow(dx, 2)]++;
            }

            for (auto x : dist2num) {
                res += x.second * (x.second-1);
            }
        }
        return res;
    }
};
```

#### 219 存在重复元素 II（easy）
* 题解:
	* 使用unordered_set存储一个不超过k个元素的序列
	* 如果下一个元素存在于列表中,那就说明存在
	* 如果set中元素超过k个,移除最早的元素.

```c++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // 维护一个哈希表,这个哈希表中最多出现k个元素
        // 如果下一个遍历的元素存在于哈希表中,那么说明存在
        if (nums.size() < 2 || k == 0) return false;
        
        unordered_set<int> knums;
        for (int i =0; i < nums.size(); i++){
            if (knums.find(nums[i]) != knums.end()) 
                return true;
            knums.insert(nums[i]);

            if (knums.size() > k){
                knums.erase(nums[i- k]);
            }
        }
        return false;
    }
};
```











## 更多分类刷题资料

* 微信公众号： 小哲AI

  ![wechat_QRcode](https://img-blog.csdnimg.cn/20210104185413204.jpg)

* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [https://blog.csdn.net/lxztju](https://blog.csdn.net/lxztju)
* 知乎专栏： [小哲AI](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[小哲AI](https://www.yanxishe.com/column/109)

