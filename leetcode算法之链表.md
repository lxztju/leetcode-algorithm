今天来盘一盘 **链表 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 链表
针对链表这种数据结构,采用指针访问元素,而且指针只可向一个方向移动, 几种主要的操作:
* 快慢指针,找到链表的中点
* 通过pre cur与last三个指针模拟题目中的流程
* 注意**虚拟头节点**(在头节点前边新建一个虚拟节点指向头节点)的使用


* 160 相交链表   (Easy)
* 206 反转链表   (Easy)
* 21 	合并两个有序链表   (Easy)
* 83 删除排序链表中的重复元素   (Easy)
*  234 回文链表 (Easy)
* 19 删除链表的倒数第N个节点  (Medium)
* 24 两两交换链表中的节点  (Medium)
* 445 	两数相加 II   (Medium)
* 725 分隔链表 (Medium)
* 328 奇偶链表   (Medium)



#### 160 相交链表   (Easy)

* 题解: 哈希表
	* 一个链表的指针存储到哈希表
	* 遍历另一个链表,查找元素是否存在于哈希表中,如果存在返回指定的元素, 如果不存在返回nullptr

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 哈希表
        //将一个链表存储到哈希表中, 遍历另一个链表查找是否存在哈希表中
        unordered_set<ListNode*> hashset;
        // 将A链表存储至哈希表中
        while (headA != nullptr){
            hashset.insert(headA);
            headA = headA->next;
        }
        // 遍历查找B链表
        while (headB != nullptr){
            if (hashset.find(headB) != hashset.end())
                return headB;
            headB = headB->next;
        }
        return nullptr;
    }
};
```

* 题解: 双指针
	* 使用两个指针分别指向数组的两个链表的头节点
	* 当headA达到链表A的尾部时,将headA指向B, 当headB达到链表B的尾部时,将headB指向A
	* 当headA与headB相遇时的节点就是相遇节点

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 双指针
        ListNode* pA = headA;
        ListNode* pB = headB;
        while (pA != pB){
            if (pA == nullptr)
                pA = headB;
            else
                pA = pA->next;

            if (pB == nullptr)
                pB = headA;
            else
                pB = pB->next;
        }
        return pA;
    }
};
```


#### 206 反转链表   (Easy)
* 题解: 
	* 直接模拟反转的过程, 使用三个指针, 一个前置指针pre, 一个当前指针cur, 一个后置指针next
	* 反转的过程: cur指向pre, cur后移, pre后移, 直到cur移动到最后一个节点.
	* 最后设置反转后的链表的结尾(head->next = nullptr).


```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 直接模拟反转的过程
        ListNode* pre = head;
        if (head == nullptr ||head->next == nullptr) return head;
        ListNode* cur = head->next;
        while (cur != nullptr){
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        head->next = nullptr;
        return pre;      
    }
};
```


#### 21 	合并两个有序链表   (Easy)

```c++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // 设定一个虚拟的头节点, 比较大小,移动指针.
        ListNode* dummyHead = new ListNode(0);
        ListNode* dummy = dummyHead;
        while (l1 && l2){
            if ((l1->val) >= (l2->val)){
                dummyHead->next = l2;
                l2 = l2->next;
            }
            else{
                dummyHead->next = l1;
                l1 = l1->next;
            }
        dummyHead = dummyHead->next;

        }
        if (l1)
            dummyHead->next = l1;
        else    
            dummyHead->next = l2;
        
        return dummy->next;

    }
};
```

#### 83 删除排序链表中的重复元素   (Easy)
直接模拟题目的执行过程. 所谓删除,就是使用指针跳过相对应的重复元素.

```c++
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // 所谓删除,就是使用指针跳过相对应的重复元素.
        ListNode* pre = head;
        ListNode* cur = head;
        while(cur){
            // 利用pre指向所有的元素
            // 当pre与cur的节点的值相等时, pre不动, cur后移
            if( pre->val == cur->val)
                cur = cur->next;
            // 当二者不等时,pre指向cur, 然后pre cur均后移 
            else{
                pre->next = cur;
                pre = pre->next;
                cur = cur->next;
            }
        }
        if (pre != cur)
            pre->next = nullptr;
        return head;

    }
};
```

####  234 回文链表 (Easy)
* 题解1: 利用数组
	* 直接遍历并取出链表中的元素存入vector中
	* 利用首尾指针遍历元素,判断是否回文

```c++
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> nums;
        while (head){
            nums.push_back(head->val);
            head = head->next;
        }
        int l = 0, r = nums.size() - 1;
        while (l < r){
            if (nums[l] != nums[r])
                return false;
            l++; r--;
        }
        return true;
    }
};
```

* 题解2: 反转后半部分的链表
	* 利用快慢指针,找到链表中点位置
	* 反转后半部分的链表
	* 再次利用快慢指针找到反转后链表的中点位置,然后对比比较两部分的链表内容是否一致.

```c++
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // 找到链表后半部分的头节点
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* lastHeadpre = findLastHead(dummy);

        // 反转链表的后半部分
        ListNode* lastHead = lastHeadpre->next;
        if (lastHead == nullptr) return true;
        ListNode* pre = lastHead;
        ListNode* cur = lastHead->next;
        while (cur){
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        
        lastHead->next = nullptr;
        lastHeadpre->next = pre;

        // 找到中间节点
        ListNode* newlastHeadpre = findLastHead(dummy);
        ListNode* newlastHead = newlastHeadpre->next;
        // 判断是否回文
        while(head && newlastHead && head != newlastHead){
            if (head->val != newlastHead->val)
                return false;
            head = head->next;
            newlastHead = newlastHead->next;
        }
        return true;    
    }


    ListNode* findLastHead(ListNode* head){
        // 找到链表后半部分的头节点的前置节点
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;
    }
```


#### 19 删除链表的倒数第N个节点  (Medium)
* 题解: 滑窗 双指针
	* 利用滑窗(双指针), 两个指针之间的距离为n
	* 当后指针达到nullptr(链表结尾)时, 前指针刚好指向倒数第n个节点的前一个节点
	* 利用虚拟头节点,解决删除头节点的问题.

```c++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 利用滑窗(双指针), 两个指针之间的距离为n
        // 当后指针达到nullptr(链表结尾)时, 前指针刚好指向倒数第n个节点的前一个节点
        // 利用虚拟头节点,解决删除头节点的问题.
        if (!head) return nullptr;
        ListNode* dummy = new ListNode(0);
        ListNode* first = dummy;
        ListNode* second = dummy;
        dummy->next = head;
        while (second && n >= 0){
            second = second->next;
            n--;
        }
        while (second){
            first = first->next;
            second = second->next;
        }
        first->next = first->next->next;
        return dummy->next;
    }
};
```

#### 24 两两交换链表中的节点  (Medium)
* 题解: 模拟交换过程
	* 需要四个指针, pre, cur1, cur2, nex
	* 模拟交换的过程,交换cur1与cur2两个节点
    1. pre->next = cur2
    2. cur1->next = nex
    3. cur2->next = cur1
    4. pre = cur1;
        cur1 = cur1->next;

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;

        while (head && head->next){
            ListNode* cur1 = head;
            ListNode* cur2 = head->next;
            ListNode* nex = cur2->next;

            pre->next = cur2;
            cur2->next = cur1;
            cur1->next = nex;

            pre = cur1;
            head = cur1->next;
        }
        return dummy->next;
        
    }
};
```

#### 445 	两数相加 II   (Medium)

* 题解: 反转链表,然后相加

* 题解: 也可以遍历一遍,将结果存储到数组中,然后相加.

```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    	// 反转两个链表
        ListNode* newl1 = reverseListNode(l1);
        ListNode* newl2 = reverseListNode(l2);
        // 新建结果链表
        ListNode* head = new ListNode(0);
        ListNode* res = head;
        int carry = 0;
        while (newl1 || newl2){
            int l1val = newl1 ? newl1->val : 0;
            int l2val = newl2 ? newl2->val : 0;
            long sumval = l1val + l2val + carry;
            int nodeval = sumval % 10;
            carry = sumval / 10;
            head->next = new ListNode(nodeval);
            if (newl1) newl1 = newl1->next;
            if (newl2) newl2 = newl2->next;
            head = head->next;
        }
        if (carry) head->next = new ListNode(carry);
        return reverseListNode(res->next);
    }

    ListNode* reverseListNode(ListNode* head){
    	// 反转链表
        ListNode* pre = head;
        if (head == nullptr) return head;
        ListNode* cur = head->next;
        while ( cur){
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        head->next = nullptr;
        return pre;
    }
};
```




#### 725 分隔链表 (Medium)
* 题解:
	* 统计链表中的节点个数
	* 计算每部分应该有几个节点
	* 分割链表

```c++
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        // 统计链表的节点数目为cnt
        ListNode* head = root;
        int cnt = 0;
        while (head){
            head = head->next;
            cnt++;
        }
        int quotient = cnt / k;  
        int reminder = cnt % k;

        // 那么结果vector中前reminder的元素中存入quotient+1个节点, 后边的存入quotient个节点
        vector< ListNode* > res;
        ListNode* cur = root;
        int count = 0; 
        int vectorNodeSize = quotient==0 ? reminder : k; // vector中仅仅前reminder中存储节点,后边存储null;
        while (count < vectorNodeSize){
            // 子链表的开头
            ListNode* pre = cur;
            //vector中需要保存的节点数目
            int num = count < reminder ?  quotient + 1 : quotient;
            while (num - 1){
                cur = cur->next;
                num--;
            }
            ListNode * tmp = cur->next;
            cur->next = nullptr;
            res.push_back(pre);
            cur = tmp;
            count++;
        }
        // 链表后边补充nullptr
        for (int i = vectorNodeSize; i < k; i++)
            res.push_back(nullptr);

        return res;
    }
};
```

#### 328 奇偶链表   (Medium)

* 题解:
	* 使用两个链表分别保存奇数节点与偶数节点
	* 连接两个链表

```c++
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        //新建两个节点,分别作为奇数与偶数子链表的头节点
        ListNode* oddhead = new ListNode(0);
        ListNode* evenhead = new ListNode(0);

        ListNode* odd = oddhead;
        ListNode* even =evenhead;

        bool flag = true; // 当flag为true时说明此节点为奇数节点, 否则为偶节点
        while (head){
            if(flag){
                ListNode* oddpre = head; // 奇数链表的前置节点
                odd->next = head;
                flag = false;
                odd = odd->next;
            }
            else{
                even->next = head;
                flag = true;
                even = even->next;
            }
            head = head->next;
        }

        // 连接连个链表
        odd->next = evenhead->next;
        even->next = nullptr;
        
        return oddhead->next; 
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

