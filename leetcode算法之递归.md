今天来盘一盘 **递归 ** 这类题目

这类题目是我一直很头疼的题目, 感觉有点难, 从这篇文章开始,就要开始比较难的一部分了

使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 递归
* 104 二叉树的最大深度  (Easy)
* 110 平衡二叉树 (Easy)
* 543 二叉树的直径 (Easy)
* 226 翻转二叉树  (Easy)
* 617 合并二叉树 (Easy)
* 112 路径总和  (Easy)
* 437 路径总和  III (Easy)
* 572 另一个树的子树   (Easy)
* 101 对称二叉树  (Easy)
* 111 二叉树的最小深度 (Easy)
* 404 左叶子之和  (Easy)
* 687 最长同值路径  (Easy)
* 100 相同的树  (easy)
* 222 完全二叉树的节点个数   (medium)
* 257 二叉树的所有路径  (easy)
* 113 路径总和 II (medium)
* 129 求根到叶子节点数字之和  (medium)





#### 104 二叉树的最大深度  (Easy)
* 题解：递归
	* 对于一棵树，左子树的最大深度l， 左子树的最大深度为r。
	* 那么整个树的最大深度为l与r的较大值加上本身根节点的1.
	* 这里求一棵树的最大深度分别求了左右子树的最大深度，形成递归结构。

```c++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if ( root == nullptr ) return 0;  
        int l = maxDepth(root->left);
        int r = maxDepth(root->right);
        return max(l, r) + 1;
    }
};
```


#### 110 平衡二叉树 (Easy)

* 递归
	* 一棵树为平衡二叉树，那么根节点是平衡二叉树， 左子节点与右右子节点均为平衡二叉树， 形成递归结构
	* 利用上一题的最大深度

```c++
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        return abs( maxDepth(root->left) - maxDepth(root->right) ) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }

    int maxDepth( TreeNode* root){
        // 求一棵树的深度（也就是最大深度）
        if (root == nullptr) return 0;
        int l = maxDepth(root->left);
        int r = maxDepth(root->right);
        return max(l, r) + 1;
    }
};
```


#### 543 二叉树的直径 (Easy)
* 对于某个节点来说其做大的直径为其左子树的最大深度与右子树最大深度之和加1.
* 依然是求最大深度问题
* 只是在每次计算过程中，需要替换最大的直径。


```c++
class Solution {
public:
    int res = 1;  // 保存最大值
    int diameterOfBinaryTree(TreeNode* root) {
        maxDepth(root);
        return res - 1;
    }
    int maxDepth(TreeNode* root){
        if (root == nullptr) return 0;
        int l = maxDepth(root->left);
        int r = maxDepth(root->right);
        res = max(res, l + r + 1);
        return max(l , r) + 1;
    }
};
```


#### 226 翻转二叉树  (Easy)
* 非常简单，遍历整个二叉树，对于一个节点将其左右子树交换即可。

```c++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // 对于一个节点，交换其左右子树的节点
        if (root == nullptr) return nullptr;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```

#### 617 合并二叉树 (Easy)
* 其实就是一个遍历的过程，直接采用前序遍历。


```c++
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {

        if (t1 == nullptr && t2 == nullptr) return nullptr;
        if (t1 == nullptr) return t2;
        if (t2 == nullptr) return t1; 
        TreeNode* root = new TreeNode(t1->val + t2->val);
        root->left = mergeTrees(t1->left, t2->left);
        root->right = mergeTrees(t1->right, t2->right);
        return root;
    }
};
```


#### 112 路径总和  (Easy)
* 如果刚好遍历到叶子节点，并且路径和刚好为targetSum，返回True。

```c++
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr ) return false;
        if(root->left == nullptr && root->right == nullptr && targetSum - root->val == 0) return true;
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
    }
};
```


#### 572 另一个树的子树   (Easy)



```c++
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (s == nullptr && t == nullptr) return true;
        if (s == nullptr || t== nullptr) return false;
		
		// 如果两个节点均存在，如果值相等，判断以这个开始的子树是否相等， 相等返回true，不等的话继续遍历。
        if (s->val == t->val)
            if (equalTree(s, t)) return true;
        return isSubtree(s->left, t) || isSubtree(s->right, t);
    }

    bool equalTree(TreeNode* t1, TreeNode* t2){
    // 判断两棵树是否相等
        if (t1 == nullptr && t2 == nullptr) return true;
        if (t1 == nullptr || t2 == nullptr) return false;
        return t1->val == t2->val && equalTree(t1->left, t2->left) && equalTree(t1->right, t2->right);
    }
};
```


#### 101 对称二叉树  (Easy)

```c++
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;

        return TreeSymmetric(root->left, root->right);
    }
    bool TreeSymmetric(TreeNode* s, TreeNode* t){
        // 判断两颗树是否镜面对称。
        if (s== nullptr && t == nullptr) return true;
        if (s == nullptr || t == nullptr) return false;
        return s->val == t->val && TreeSymmetric(s->left, t->right) && TreeSymmetric(s->right, t->left);
    }
};
```

#### 111 二叉树的最小深度 (Easy)
* 这个题与最大深度的题目不一样，不能直接左右子树的最小值加1.因为其要求到叶子节点的距离
* 如果这棵树是一条仅仅由左子树构成的一条链表式的树， 那么直接左右子树的最小值加1，结果返回就是1.
* 但是此时不满足题意，题目要求到叶子节点。
* 正解需要分情况讨论。见代码中分析。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210130215549768.png)

```c++
class Solution {
public:
    int minDepth(TreeNode* root) {
        // 这个题与最大深度的题目不一样，不能直接左右子树的最小值加1.因为其要求到叶子节点的距离
        // 如果这棵树是一条仅仅由左子树构成的一条链表式的树， 那么直接左右子树的最小值加1，结果返回就是1.
        // 但是此时不满足题意，题目要求到叶子节点。

        if (root == nullptr) return 0;
        int l = minDepth(root->left);
        int r = minDepth(root->right);
        // 如果左子树存在，右子树不存在
        if (root->left != nullptr && root ->right == nullptr)
            return  l+ 1;
        // 如果左子树不存在，右子树存在
        if (root->right != nullptr && root->left == nullptr)
            return r + 1;
        // 左右子树均存在。
        return min(l, r) + 1;
    }
};

```



#### 404 左叶子之和  (Easy)
* 遍历所有的节点， 将所有的左叶子节点求和即可。

```c++

class Solution {
public:
    int res = 0;
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr){
            res += root->left->val;
        }
        sumOfLeftLeaves(root->left);
        sumOfLeftLeaves(root->right);
        return res;
    }
};
```





#### 100 相同的树  (easy)

```c++
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        return (p->val == q->val ) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

#### 257 二叉树的所有路径  (easy)

```c++
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        string path;
        treePaths(root, res, path);
        return res;
    }
    
    void treePaths(TreeNode* root, vector<string>& res, string path){
    // 保存所有路径
        if (root == nullptr) return;
        if(root->left == nullptr && root->right == nullptr) {
            path += to_string(root->val);
            res.push_back(path);
            return;
        }
        path += to_string(root->val);
        path += "->";
        treePaths(root->left, res, path);
        treePaths(root->right, res, path);
    }
};
```


#### 222 完全二叉树的节点个数   (medium)

* 方法1： 不考虑完全二叉树，直接遍历所有的节点

```c++
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        int l = countNodes(root->left);
        int r = countNodes(root->right);
        return (l + r + 1);
    }
};
```


* 方法2： 利用完全二叉树的性质

```c++

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        // 分别求左右两颗子树的高度
        int l = treeDepth(root->left);
        int r = treeDepth(root->right);
        // 如果两颗子树高度相等，说明左子树为满二叉树，右子树不满
        if (l == r){
            return pow(2, l) + countNodes(root->right);
        }
        // 高度不等，说明右子树是满二叉树，左子树不满。
        else
            return pow(2, r) + countNodes(root->left);
    }
    int treeDepth(TreeNode* root){
    //求一棵完全二叉树的高度
        if (root == nullptr) return 0;
        int l = treeDepth(root->left);
        return l + 1;
    }
};
```


#### 687 最长同值路径  (medium)

* 最长同值路径就是过某个节点最长同值路径中的最大值。



```c++
class Solution {
public:
    int res = 0;
    int longestUnivaluePath(TreeNode* root) {
        if (root == nullptr) return 0;
        arrowLength(root);
        return res;
    }
    int arrowLength(TreeNode* root){
    // 以某个节点作为根节点的最长同值路径。
        if (root == nullptr) return 0;
        int l = arrowLength(root->left);
        int r = arrowLength(root->right);
        int left = 0, right = 0;
        if (root->left != nullptr && root->val == root->left->val)
            left = l + 1;
        if (root->right != nullptr && root->val == root->right->val)
            right = r + 1; 
        res = max(res, left + right);
        return max(left, right);
    }
};
```


#### 113 路径总和 II (medium)
* 套路代码


```c++
class Solution {
public:
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int> > res;
        vector<int> path;
        pathsum(root, res, path, targetSum);
        return res;
    }
    void pathsum(TreeNode* root, vector<vector<int>>& res, vector<int> path, int target){
        if (root == nullptr) return;
        if (root->left == nullptr && root->right == nullptr && target == root->val){
            path.push_back(root->val);
            res.push_back(path);
            return ;
        }
        path.push_back(root->val);
        target -= root->val;
        pathsum(root->left, res, path, target);
        pathsum(root->right, res, path, target);
        return ;            
    }
};
```

#### 129 求根到叶子节点数字之和  (medium)
* 先求出所有的路径， 然后求和。

```c++
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        vector<vector<int> > res;
        vector<int> path;
        Path(root, res, path);
        int ans = 0;
        for (int i=0; i < res.size(); i++){
            int tmp = 0;
            for (int j = res[i].size()-1; j >= 0; j--){
                tmp += (res[i][j] * pow(10, res[i].size()-1 - j));
            }
            ans += tmp;
        }
        return ans;
    }

    void Path(TreeNode* root, vector<vector<int>>& res, vector<int> path){
    // 得到所有的路径，保存至vector中
        if (root == nullptr) return;
        if (root->left == nullptr && root->right == nullptr ){
            path.push_back(root->val);
            res.push_back(path);
            return ;
        }
        path.push_back(root->val);
        Path(root->left, res, path);
        Path(root->right, res, path);
        return ;            
    }
};
```


#### 437 路径总和  III (medium)


```c++
class Solution {
public:
    int res = 0;
    int pathSum(TreeNode* root, int sum) {
        if (root == nullptr) return 0;
        // 以根节点开始
        pathsum(root, sum);
        //  遍历整个树
        pathSum(root->left, sum);
        pathSum(root->right, sum);
        return res;
    }
    void pathsum(TreeNode* root, int target){
        // 以某个节点开始一共有多少路径和为target的路径。
        if (root == nullptr) return ;
        target -= root->val;
        if (target == 0){
            res += 1;
        }
        pathsum(root->left, target);
        pathsum(root->right, target);
        return ;
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

