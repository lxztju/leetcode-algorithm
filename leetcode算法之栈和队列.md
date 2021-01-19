今天来盘一盘 **栈以及队列 ** 这两类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 栈和队列

> **栈: 先进先出 
> 队列: 先进后出**

利用这两类数据结构的特性解题.

其中一类非常经典的题目是: **单调栈(leetcode496题, 经典题目)**. 

* **单调递减栈**, 是指针对每一个待遍历的元素x, 将x与栈顶元素相比, 如果大于栈顶元素将栈顶元素出栈, 重新循环对比,直到小于栈顶元素,然后将x入栈. 
* **单调递增栈**: 同理分析

---

* 232 用栈实现队列 (Easy)
* 225 用队列实现栈  (Easy)
* 155 最小栈   (Easy)
* 20 有效的括号   (Easy)
* 1021 删除最外层的括号   (easy)
* 496 下一个更大元素 I   (easy)
* 503 下一个更大元素 II (Medium)
* 739 每日温度   (Medium)



#### 232 用栈实现队列 (Easy)
* 题解: 两个栈实现
	* 栈的特点时先进后出, 而队列是先进先出
	* 使用两个栈实现先进先出
	* stackin控制入队, stackout控制出队
	* 当入队时,直接压入stackin即可
	* 出队时, 当stackout为空时,将stackin中的元素依次弹出压入stackout中, 然后执行stackout的出栈也就是出队操作.

* 示例
先入队[1,2], 然后执行一次出队, 再入队[3,4], 然后执行两次出队

1. 入队之后stackin为[1,2], stackout为空
2. 执行出队时,将stackin中元素依次压入stackout中, 此时stackout为[2,1], 出队1, stackout为[2], stackin为空
3. 再次入队, stackin为[3,4], 此时stackout为[2]
4. 执行第一次出队时, stackout非空直接出队2, 此时stackin为[3,4], stackout为空
5. 当再次执行出队时, stackout为空,与第二步相同.

```c++
class MyQueue {
public:
    stack<int> stackin;
    stack<int> stackout;
    /** Initialize your data structure here. */
    MyQueue() {

    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stackin.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        // 如果stackout为空,将stackin中的元素依次放入stackout
        if(stackout.empty())
            while (!stackin.empty() ){
                int tmp = stackin.top();
                stackin.pop();
                stackout.push(tmp);
            }
        // 返回stackout的栈顶元素
        int tmp = stackout.top();
        stackout.pop();
        return tmp;
    }
    
    /** Get the front element. */
    int peek() {
        // 如果stackout为空,将stackin中的元素依次放入stackout
        if(stackout.empty())
            while (!stackin.empty() ){
                int tmp = stackin.top();
                stackin.pop();
                stackout.push(tmp);
            }
        // 返回stackout的栈顶元素
        return stackout.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if (stackin.empty() && stackout.empty())
            return true;
        else
            return false;
    }
};
```


#### 225 用队列实现栈  (Easy)

* 题解: 两个队列实现
	* 栈是先进后出的, 队列是先进先出的.
	* 使用队列实现栈就是要 将入队的元素,放置在队首. 
	* 这样出栈时, 直接使用队列出队实现.

* q1存储栈中的元素, q2作为入栈时的辅助栈
* 入栈时,先将元素入队到q2, 然后将q1中的元素出队并放入q2中, 此时q2队首的元素即为栈顶元素, 将q1与q2互换, q2始终作为辅助栈.

```c++
class MyStack {
public:
    /** Initialize your data structure here. */
    queue<int> q1;
    queue<int> q2;
    MyStack() {
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q2.push(x);
        while(!q1.empty()){
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int tmp = q1.front();
        q1.pop();
        return tmp;
    }
    
    /** Get the top element. */
    int top() {
        return q1.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty();
    }
};
```

#### 155 最小栈   (Easy)

* 题解: 辅助栈
	* 采用另外的一个辅助栈s2
	* 每次s1入栈出栈时,均在s2的对应位置存入此时对应的最小值
	* 对于辅助栈s2的操作, 对于一个待入栈的元素x, 如果其大于s2的栈顶,就在s2中再次压入栈顶元素, 否则压入x


```c++
class MinStack {
public:
    stack<int> s1;
    stack<int> s2;  // 辅助栈
    /** initialize your data structure here. */

    MinStack() {
    }
    
    void push(int x) {
        s1.push(x);
        if (s2.empty())
            s2.push(x);
        else{
            int tmp = s2.top();
            if (x <= tmp)
                s2.push(x);
            else
                s2.push(tmp);
        }
    }
    
    void pop() {
        s1.pop();
        s2.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return s2.top();
    }
};
```

#### 20 有效的括号   (Easy)
* 题解
	* 最经典的一道使用栈的题目
	* 遇到左括号直接入栈, 遇到右括号,左括号出栈对比

```c++
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> parentheses = {{'(', ')'}, {'[', ']'}, {'{', '}'}};  // 字典
        stack<char> stack1;
        for (auto s1: s){
            // s1为右括号
            if (parentheses.find(s1) == parentheses.end()){
                // 如果栈为空, 返回false
                if (stack1.empty()) return false;
                else{
                    char tmp = stack1.top();
                    stack1.pop();
                    // 如果栈顶元素与s1不对应, 返回false
                    if (parentheses[tmp] != s1) return false;
                }
            }
            // s1为左括号, 入栈
            else{
                stack1.push(s1);
            }
        }
        //最后栈为空返回true, 否则返回false.
        if (!stack1.empty()) return false;
        else return true;
    }
};
```




#### 1021 删除最外层的括号   (easy)

* 题解
	* 括号的匹配, 要使用栈
	* 遍历字符串
	* 如果遇到左括号直接入栈, 如果此时栈中有超过1个左括号, 说明这个左括号需要保留
	* 如果遇到右括号, 左括号对应出栈, 如果此时栈中依然存在左括号, 那么这个右括号需要保留
	* 否则不保留.

```c++
class Solution {
public:
    string removeOuterParentheses(string S) {
        string res;
        stack<char> stack1;
        for (auto s1: S){
            if (s1 == '('){
                stack1.push(s1);
                if (stack1.size() > 1)
                    res += s1;
            }
            else{
                stack1.pop();
                if (stack1.size() >= 1)
                    res += ')';
            }
        }
        return res;
    }
};
```


#### 496 下一个更大元素 I   (easy)
* 题解: 暴力法
	* 利用map存储nums2中每个元素与索引的位置
	* 对于nums1中的每个元素, 从nums2中与其对应的下一个位置开始查找

```c++
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int, int> nums2Index;
        for (int i = 0; i< nums2.size(); i++){
            nums2Index.insert(make_pair(nums2[i], i));
        }
        // 暴力法
        for(int i = 0; i< nums1.size(); i++){
            bool flag = true;
            for (int j = nums2Index[nums1[i]]; j< nums2.size(); j++){
                if (nums2[j] > nums1[i]){
                    res.push_back(nums2[j]);
                    flag = false;
                    break;
                }
            }
            if (flag) res.push_back(-1);
        }
        return res;
    }
};
```

* 题解2: 单调栈
	* 依次遍历数组nums1, 如果栈为空将nums1[i]入栈
	* 如果nums[i+1] 大于栈顶元素, 就将栈顶出栈, 此时对应栈顶的下一个大的元素就是nums[i+1]
	* 如果nums[i+1] 不大于nums[i], 就将nums[i+1]入栈, 直到找到nums[j]大于栈顶就依次比较出栈.


```c++
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int, int> nums2Index;

        // 单调栈
        stack<int> decendStack;
        for (int i = 0; i < nums2.size(); i++){
            if (decendStack.empty() || decendStack.top() >= nums2[i])
                decendStack.push(nums2[i]);
            else{
                while (!decendStack.empty() && decendStack.top() < nums2[i]){
                    nums2Index[decendStack.top()] = nums2[i];
                    decendStack.pop();
                }
                decendStack.push(nums2[i]);
            }
        }

        // 最终如果栈非空, 那么栈中下一个最大的元素不存在
        while (! decendStack.empty()){
            int tmp = decendStack.top();
            decendStack.pop();
            nums2Index[tmp] = -1;        
        }


        for(int i = 0; i< nums1.size(); i++){
            res.push_back(nums2Index[nums1[i]]);
        }
        return res;
    }
};
```


#### 503 下一个更大元素 II (Medium)


* 题解: 单调栈
	* 循环数组, 那么直接遍历两遍就可以了
	* 还有一个不同点就是,这里可能会出现相同的元素, 因此使用map会导致错误(这里我就搞错了依次)
	* 遍历数组两次，每次pop之前都去更新一下res

```c++
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        stack<int> stk;
        vector<int> res(nums.size(), -1);
        for(int i = 0; i < nums.size() * 2; i++)
        {
            int index = i % nums.size();
            while(!stk.empty() && nums[stk.top()] < nums[index])
            {
                // 如果已经找到了下一个最大的元素, 那么跳过
                if(res[stk.top()] == -1)
                {
                    res[stk.top()] = nums[index];
                }
                stk.pop();
            }
            stk.push(index);
        }
        return res;
    }
};
```

#### 739 每日温度   (Medium)
* 题解: 单调栈
	* 与496题目一样, 找寻下一个最大的元素
	* 不同的是这里需要保存的是索引之间的差值.

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(), 0);
        stack<int> stk;
        // 遍历T
        for (int i = 0; i< T.size(); i++){
            // 如果新的气温大于栈顶的气温, 那么保存需要等待的天数(索引值差)
            // 栈顶出栈
            while(!stk.empty() && T[stk.top()] < T[i]){
                res[stk.top()] = i - stk.top();
                stk.pop();
            }
            stk.push(i);
        }
        return res;
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

