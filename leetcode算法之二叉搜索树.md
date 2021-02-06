今天来盘一盘 **二叉搜索树 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)



## 二叉搜索树
二叉搜索树是指 **左子树的节点值均小于根节点的值， 右子树的节点值大于根节点的值（递归的概念，对于每个节点都成立）**

二叉搜索树的**中序遍历是排序数组**


* 235 二叉搜索树的最近公共祖先   (Easy)
* 108 将有序数组转换为二叉搜索树   (Easy)
* 653 两数之和 IV - 输入 BST  (Easy)
* 530 二叉搜索树的最小绝对差  (Easy)
* 501 二叉搜索树中的众数   (Easy)
*  669 修剪二叉搜索树   (medium)
* 230 二叉搜索树中第K小的元素   (Medium)
* 538 把二叉搜索树转换为累加树   (medium)
* 109 有序链表转换二叉搜索树  (Medium)
*  236 二叉树的最近公共祖先   (Medium)



#### 235 二叉搜索树的最近公共祖先   (Easy)

* 如果当前节点值大于pq，那么说明分叉点存在于当前节点的左子树中
* 如果当前节点值小于pq， 那么说明分叉点存在当前节点的右子树中
* 否则，说明找到分叉点。

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) return nullptr;
        // 大于pq，搜索左子树
        if(root->val > p->val && root->val > q->val) 
            return lowestCommonAncestor(root->left, p, q);
        // 小于pq，搜索右子树
        else if (root->val < p->val && root->val < q->val)
            return lowestCommonAncestor(root->right, p, q);
       	// 找到分叉点。
        else    
            return root;
    }
};
```


#### 108 将有序数组转换为二叉搜索树   (Easy)
* 二叉搜索树的**中序遍历是有序数组**
* 根据这个性质，排序数组的中间元素是根节点，左半部分是左子树，右半部分是右子树，递归构建

```c++
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArray2BST(nums, 0, nums.size()-1);
    }
    TreeNode* sortedArray2BST(vector<int>& nums, int left, int right){
        if (left > right) return nullptr;
        int middle = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[middle]);
        root->left = sortedArray2BST(nums, left, middle-1);
        root->right = sortedArray2BST(nums, middle+1, right);
        return root;
    }
};
```



#### 653 两数之和 IV - 输入 BST  (Easy)
* 中序遍历得到排序数组
* 然后双指针

```c++
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        int l = 0, r = nums.size() -1;
        while (l < r){
            int lrSum = nums[l] + nums[r];
            if (lrSum == k)
                return true;
            else if (lrSum > k)
                r--;
            else 
                l++;
        }
        return false;
    }
	//中序遍历
    void inorder(TreeNode* root, vector<int>& nums){
        if (root == nullptr) return;
        inorder(root->left, nums);
        nums.push_back(root->val);
        inorder(root->right, nums);
    }
};
```



#### 530 二叉搜索树的最小绝对差  (Easy)
* 依然利用中序遍历为有序数组的特点。

```c++
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> nums;
        inorder(root, nums);
        int res = nums[1] - nums[0];
        for (int i = 1; i < nums.size(); i++){
            res = min(res, nums[i] - nums[i-1]);
        }
        return res;
    }
	//中序遍历
    void inorder(TreeNode* root, vector<int>& nums){
        if (root == nullptr) return;
        inorder(root->left, nums);
        nums.push_back(root->val);
        inorder(root->right, nums);
    }
};
```

#### 501 二叉搜索树中的众数   (Easy)
```c++
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        // 直接使用unordered_map，没有用到二叉搜索树的特定
        unordered_map<int, int> nodeFreq;
        vector<int> res;
        traversal(root, nodeFreq);
        int freq = 0;
        for (auto e = nodeFreq.begin(); e != nodeFreq.end(); e++){
            freq = max(freq, e->second);
        }
        for (auto e = nodeFreq.begin(); e != nodeFreq.end(); e++){
            if (e->second == freq)
                res.push_back(e->first);
        }
        return res;
    }
    void traversal(TreeNode* root, unordered_map<int, int>& nodeFreq){
        if (root == nullptr) return;
        nodeFreq[root->val]++;
        traversal(root->left, nodeFreq);
        traversal(root->right, nodeFreq);
    }
};
```

如果不使用额外的空间。
* 针对二叉搜索树而言，其中序遍历是一个有序数组， 所有相等的元素均在一起出现
* 利用cnt变量来统计当前元素出现的次数， maxcnt为最大频率的元素出现的次数，res保存众数

```c++
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        int cnt = 1;
        int maxcnt = 1;
        int base;
        inorder(root, cnt, maxcnt, res, base);
        return res;
    }
    void inorder(TreeNode* root, int& cnt, int& maxcnt, vector<int>& res, int& base){
        if (root == nullptr) return;
        
        inorder(root->left, cnt, maxcnt, res, base);

        if (root->val == base){
            cnt++;
        }
        else{
            cnt = 1;
            base = root->val;
        }
        if (cnt > maxcnt){
            res.clear();
            res.push_back(base);
            maxcnt = cnt;
        }
        else if (cnt == maxcnt){
            res.push_back(base);
        }

        inorder(root->right, cnt, maxcnt, res, base);
    }
};
```

#### 669 修剪二叉搜索树   (medium)

```c++
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if(root == nullptr) return nullptr;
        if (root->val < low)
            return trimBST(root->right, low, high);
        else if (root->val > high)
            return trimBST(root->left, low, high);
        else{
            root->left = trimBST(root->left, low, high);
            root->right = trimBST(root->right, low, high);
        }
        return root;
    }
};
```

#### 230 二叉搜索树中第K小的元素   (Medium)

* 最直观的想法，二叉搜索树的中序遍历为排序数组
```c++
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        return nums[k-1];
    }

    //中序遍历
    void inorder(TreeNode* root, vector<int>& nums){
        if (root == nullptr) return;
        inorder(root->left, nums);
        nums.push_back(root->val);
        inorder(root->right, nums);
    }
};
```

#### 538 把二叉搜索树转换为累加树   (medium)
* 反中序遍历
* 从最右侧看，根节点的值为根+=右子树的值
* 左子树的值为左子树的值+=根的值

```c++
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        int val = 0;
        inverseInorder(root, val);
        return root;
    }
    // 反中序遍历
    void inverseInorder(TreeNode* root, int& val){
        if (root == nullptr) return;
        inverseInorder(root->right, val);
        val += root->val;
        root->val  = val;
        inverseInorder(root->left, val);
    }
};
```


#### 109 有序链表转换二叉搜索树  (Medium)
* 有序链表转换为二叉搜索树与数组的转换方式基本一致
* 只需要将链表分为左右两部分分别构成BST的左右子树即可

```c++
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr) return nullptr;
        // 返回链表中间节点的前驱节点
        ListNode* premiddle = premiddleList(head);
        cout<< (premiddle->val) << endl;
        // 链表的中间节点
        int val = 0;
        ListNode* middle = premiddle->next;
        if (middle == nullptr) {
            TreeNode* root = new TreeNode(premiddle->val);
            return root;
        }
        else{
            TreeNode* root = new TreeNode(middle->val);
            premiddle->next = nullptr;
            root->left = sortedListToBST(head);
            root->right = sortedListToBST(middle->next);
            return root;
        }
    }


    // 获得链表的中间节点的前一个节点。
    ListNode* premiddleList(ListNode* head){
        if ( head == nullptr) return nullptr;
        ListNode* slow = head;
        ListNode* pre = slow;
        ListNode* fast = head->next;
        while (fast != nullptr && fast->next != nullptr){
            pre = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        return pre;
    }
};
```


#### 236 二叉树的最近公共祖先   (Medium)
* 直接遍历查找，如果一棵树的左右子树中分别存在p与q，那么直接返回这个结点

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) return nullptr;
        if ( root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if (left != nullptr && right != nullptr) return root;
        else if (left == nullptr)
            return right;
        else if (right == nullptr)
            return left; 
        else return nullptr;
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

