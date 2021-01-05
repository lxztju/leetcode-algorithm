明年就是找工作了，又要开始刷题了，把之前做过的题目再梳理整理一遍，但愿明年不要那么拉跨，祈祷明年能找到工作，千万不能毕业就失业。

分类别解析leetcode上的一些相关的例题路，代码采用**C++与python**实现。



## 双指针
主要分为如下的三类题目: 对撞指针, 快慢指针, 其他双指针.


### 对撞指针

> 对撞指针的问题,一般是数组首尾各有一个指针,这俩指针往中间移动过,解决相对应的问题

* 167 有序数组的 Two Sum 2 (easy)
* 633 两数的平方和(easy)
* 345 反转元音字符(easy)
* 125 验证回文串(easy)
* 680 回文字符串(easy)
* 344 反转字符串(easy)
*  27 移除元素(easy)
* 11 盛最多水容器(medium)



#### 167 有序数组的 Two Sum 2 (easy)

> 给定一个已按照**升序排列** 的有序数组，找到两个数使得它们相加之和等于目标数。

* 题解思路:
	* 数组是升序排列, 首尾各设置一个指针, 查找两个指针的值的和为target.
	* 当二者之和大于target时,尾指针前移,这两个数的和减小; 小于target时,首指针后移,直到二者数组的和等于target.

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // 首尾指针
        int head = 0, tail = numbers.size() - 1;
        while (head <= tail){
            int point_sum = numbers[head] + numbers[tail];
            if ( point_sum== target)
                return {head + 1, tail + 1};
            // 和小于target,首指针后移
            else if (point_sum < target)
                head++;
            // 和大于target, 尾指针前移
            else
                tail--;
        }
        return {};
    }
};
```

#### 633 两数的平方和(easy)

> 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

* 题解:
	* 与上一题一样, 设定一个数组为[0 ~ int(sqrt(c)) + 1], 设定首尾指针, 首尾指针对应的元素的平方之和为c

```c++
class Solution {
public:
    bool judgeSquareSum(int c) {
        int head = 0;
        int tail = static_cast<int>(sqrt(c)) + 1;
        while (head <= tail){
            long point_sum = pow(head, 2) + pow(tail, 2);
            if (point_sum == c)
                return true;
            else if (point_sum < c)
                head++;
            else    
                tail--;
        }
        return false;
    }
};
```

#### 345 反转元音字符(easy)

> 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

* 题解:
	* 首尾指针, 首先首指针后移,直到找到元音字母,然后尾指针后移找到元音字母,将二者交换

```c++
class Solution {
public:
    string reverseVowels(string s) {
        // 首尾指针
        int head = 0, tail = s.size() - 1;
        // 利用无序的关联容器,存储原因字母表.
        unordered_set<char> vowels({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'});

        while(head < tail){
            // 首指针找到元音字母
            if(vowels.find(s[head]) == vowels.end())
                head++;
            //尾指针找到元音字母
            else if(vowels.find(s[tail]) == vowels.end())
                tail--;
            else{
                // 交换首尾指针对应的元音字母
                swap(s[head], s[tail]);
                // 移动首尾指针的值
                head++;
                tail--;
            }
        }
        return s;
    }
};
```


#### 125 验证回文串(easy)

> 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

```c++
class Solution {
public:
    bool isPalindrome(string s) {
        int head = 0, tail = s.size() -1;
        while (head < tail){
            // isalnum() 数字或者字母时为真.
            if (isalnum(s[head]) && isalnum(s[tail])){
                // 忽略大小写,直接将其都转化为小写进行比较
                if (tolower(s[head]) != tolower(s[tail]))
                    return false;
                else
                    head++; tail--;
            }
            else if (! isalnum(s[head]))
                head++;
            else if (! isalnum(s[tail]))
                tail--;
        }
        return true;
    }
};
```
#### 680 回文字符串(easy)

> 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串

* 题解:
	* 与上边一道题不同的是,可以删除一个字符,然后确定是否为回文串.
	* 那么分为两种情况,   第一种情况: 直接就是回文串
	* 第二种情况: 遇到了不相等的字符,那么要么去掉首指针对应的字符此时中间的子串依然为回文串,或者去掉尾指针此时中间的字符对应的字符依然为回文串.

```c++
class Solution {
public:

    bool palindrome(string& s){
        // 验证一个字符串是否为回文串
        int head = 0, tail = s.size() - 1;
        while (head < tail){
            if (s[head] != s[tail])
                return false;
            else
                head++; tail--;
        }
        return true;
    }

    bool validPalindrome(string s) {
        int head = 0, tail = s.size() - 1;
        while (head < tail){
            if (s[head] == s[tail]) {
                head++; tail--;
                continue;
            }
            else{
                string str1(s, head + 1, tail- head);
                string str2(s, head, tail - head);
                return palindrome(str1) || palindrome(str2);
            }
        }
        return true;
    }
};
```

#### 344 反转字符串(easy)
```c++
class Solution {
public:
    void reverseString(vector<char>& s) {
        int head = 0, tail = s.size() -1;
        while (head < tail){
            swap(s[head], s[tail]);
            head++;
            tail--;
        }
    }
};
```


#### 27 移除元素(easy)

> 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
> 
> 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
> 
> 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素

* 题解
	* 这道题的主要的思路就是  将数值为val的元素移动到数组的末尾
```c++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int head = 0, tail = nums.size() - 1;
        
        while (head <= tail){
            while (head <= tail && nums[tail] == val)
                tail--;
            if (nums[head] == val && head <= tail){
                swap(nums[head], nums[tail]);
                tail--;
            }
            head++;
        }
        return tail + 1;
    }
};
```


#### 11 盛最多水容器(medium)

> 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

* 题解:
	* 这道题依然采用首尾指针, 这个矩形的面积为`长x高`, 长为两个指针之间的距离, 高由两个指针所对应的元素中的最小值决定.
	* 两个指针中高度较小的指针向内移动,找对应的更高的值.例如左边低,那么左指针右移虽然长变小了,但是高可能变高,整体面积才可能变大.  如果右指针左移,那么高永远由左边决定,此时长也变小了,整体的面积更小.
	* 因此只能移动短边对应的指针.

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        // 定义头尾指针
        int head = 0, tail = height.size() - 1;
        // 保存最大的矩形面积
        long maxarea = 0;
        while (head < tail){
            // 左边低, 那么左指针右移找寻更高的 高
            // 如果右指针左移, 那么高还是左指针的值,但是长变小了,只能移动短边
            if (height[head] < height[tail]){
                long area = height[head] * (tail - head);
                maxarea = max(maxarea, area);
                head++;
            }
            // 右边低,右指针左移
            else {
                long area = height[tail] * (tail - head);
                maxarea = max(maxarea, area); 
                tail--;               
            }
        }
        return maxarea;
    }
};
```


### 快慢指针
> 快慢指针是指两个指针从头开始一个快一个慢指针,  一般就是,  最经典的题目就是针对链表的问题(**快慢指针查找链表的中心点**).

* 141 判断列表是否存在环(easy)
* 283 移动零(easy)
* 26 删除排序数组中的重复项(easy)
* 80 删除排序数组中的重复项 II(medium)



#### 141 判断列表是否存在环(easy)

> 给定一个链表，判断链表中是否有环。
> 
> 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos不作为参数进行传递，仅仅是为了标识链表的实际情况。
> 
> 如果链表中存在环，则返回 true 。 否则，返回 false 。


* 题解:
	* 使用快慢指针,就像赛跑,一个人跑得快一个人跑得慢两个人肯定会相遇.
	* 这道题快慢指针,如果二者相遇之后就说明二者有环,否则快指针就会首先达到链表末尾.

```c++
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return false;
        // 定义快慢指针
        ListNode* slow = head;
        ListNode* fast = head->next;
        // 如果fast指针没有到达链表的结尾,就持续移动快慢指针.
        while (fast != nullptr && fast->next != nullptr){
            // 如果二者相遇,说明有环
            if (fast == slow) return true;
            slow = slow->next;
            fast = fast->next->next;
        }
        // 快指针到达链表的结尾,说明没有环.
        return false;
    }
};
```

#### 283 移动零(easy)

> 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

* 题解:
	* 使用快慢指针, 快指针向右遍历,快指针指向非零元素,慢指针指向待交换的元素.
	* 右指针向右遍历,如果遇到非零元素,左右指针的值进行交换,然后左右指针同时后移
	* 如果右指针遇到零元素, 那么左指针不变等待交换,右指针后移找寻非零元素.

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // 快慢指针
        int slow=0, fast=0;

        while (fast< nums.size()){
            if (nums[fast] != 0){
                swap(nums[fast], nums[slow]);
                slow++;
            }
            fast++;
        }
    }
};
```

#### 26 删除排序数组中的重复项(easy)

> 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
> 
> 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


* 题解:
	* 使用快慢指针,慢指针指向最终保留的数字,也就是待交换的数字,快指针向后遍历找寻不重复的元素与慢指针的位置进行交换,从而首先将不重复的元素保留在数组的前部.
	* 快指针向后遍历,当快慢指针对应的值不相同的时候,说明出现了一个新的不重复数字,将其进行交换.

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // 快慢指针
        int slow = 0, fast = 0;
        if (nums.size() == 0) return 0;
        while (fast < nums.size()){
            if (nums[fast] != nums[slow]){
                slow++;
                swap(nums[fast], nums[slow]);
            }
                fast++;
        }
        return slow+1;
    }
};
```

#### 80 删除排序数组中的重复项 II(medium)

> 给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
> 
> 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

这道题与上一题相比难在重复的字符可以出现两次.

* 题解:
	* 这里就需要在上一题的基础上加以改进,也就是要判断字符已经保存的次数cnt表示

```c++
class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;
    if (nums.size() == 1) return 1;
    
    int slow = 0, fast = 1;
    int cnt = 1;    //cnt表示某个字符出现的次数

    while (fast < nums.size() ) {
        if (nums[fast] == nums[slow]) {
            // 如果这个字符仅仅出现了一次, 那么慢指针后移并赋值
            if (cnt == 1) {
                slow++;
                nums[slow] = nums[fast];
                cnt++;
            }
            //如果已经出现了两次,就直接快指针后移
        } 
        // 如果不相等,那么直接复制,也就是字符仅仅出现一次
        else {
            slow++;
            nums[slow] = nums[fast];
            cnt = 1;
        }
        fast++;
    }
    return slow + 1;
  }
};
```



### 其他双指针

* 88. 归并有序数组(easy)
* 524. 通过删除字母匹配到字典里最长单词(medium)


#### 88. 归并有序数组(easy)

> 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
> 说明：
> 
> 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

* 题解: 
	* 方法2: 直接另外开辟一个空间,将二者插入新的vector,然后再copy回nums1.这样显然不太合适
	* 方法2: 直接使用insert再nums1的对应位置插入元素,但是这样会造成元素的大量移动操作
	* 方法3: 从后往前复制,先将最大的放置在nums[m+n-1]的位置,然后逐个往前

方法3的代码如下: (也可以采用前两种方法试试,简单题应该也会通过)
```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        int i = m-1, j = n-1, k = 0;
        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]){
                nums1[m + n - k - 1] = nums1[i];
                i--;
            }
            else{
                nums1[m + n - k - 1] = nums2[j];
                j--;                
            }
            k++;
        }
        if (j >= 0){
            for (int s = 0; s <= j; s++){
                nums1[s] = nums2[s];
            }
        }
    }
};
```


#### 524. 通过删除字母匹配到字典里最长单词(medium)

> 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

* 题解:
	* 首先查找所有满足条件的字符串
	* 然后在这些字符串中保留最长的一些字符串(可能相同长度有多个)
	* 找到字典序最小的字符串


```c++
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {

        if (s.empty()) return "";

        vector<string> Words;  // 存储所有满足条件的字串

        for (auto e : d){
            int p1 = 0, p2 = 0;
            while (p1 < e.size() && p2 < s.size()){
                if (e[p1] == s[p2])
                    {p1++;p2++;}
                else
                    p2++;
            }
            if (p1 == e.size())
                Words.push_back(e);
        }

        vector<string> longestWord;   // 保存满足条件的子串中最长的字串

        int maxSize = 0;
        for (auto e : Words){
            if (e.size() == maxSize)
                longestWord.push_back(e);
            else if (e.size() > maxSize){
                longestWord.clear();
                longestWord.push_back(e);
                maxSize = e.size();
            }
        }
        sort(longestWord.begin(), longestWord.end());

        if (longestWord.empty()) return "";
        else return longestWord[0];

    }
};
```

## 更多笔记资料

* 微信公众号： 小哲AI

  ![wechat_QRcode](https://img-blog.csdnimg.cn/20210104185413204.jpg)

* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [https://blog.csdn.net/lxztju](https://blog.csdn.net/lxztju)
* 知乎专栏： [小哲AI](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[小哲AI](https://www.yanxishe.com/column/109)







