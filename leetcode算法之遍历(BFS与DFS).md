今天来盘一盘 **遍历 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)


## 遍历
层次遍历（BFS）
* 102 二叉树的层序遍历(medium)
* 637 	二叉树的层平均值   (Easy)
* 513 找树左下角的值   (medium)


深度优先遍历（DFS）
* 144 二叉树的前序遍历   (meidum)
* 145 	二叉树的后序遍历   (hard)
* 94 二叉树的中序遍历  (Medium)


### BFS
宽度优先遍历（BFS）采用**队列**的方式，依次遍历一棵树。

基本的套路代码，就是`102题目`中的代码思路。

#### 102 二叉树的层序遍历(medium)

* 题解   `BFS`
	* 使用队列存储当前节点的指针以及当前节点的层次
	* 循环遍历队列中的元素
	* 对于一个队首节点，如果其左子节点存在就将左子节点入队，如果右子节点存在，将右子节点入队列
	* 按照队首节点的层次数，将节点的值插入vector中对于的位置。

```c++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return {};
        // 使用队列存储节点与节点所对应的层次
        queue<pair<TreeNode*, int>> nodeQ;
        vector<vector<int>> res;
        // 将根节点以及对应的层次0，入队
        nodeQ.push(make_pair(root, 0));
        // 如果队列不为空，就一直遍历队列元素
        while (!nodeQ.empty()){
            // 拿出队首的节点指针以及层次
            auto nodeLevel = nodeQ.front();
            auto nodePoint = nodeLevel.first;
            int level = nodeLevel.second;
            nodeQ.pop();  // 队首元素出队

            if (res.size() <= level){
                res.push_back({});
            }
            res[level].push_back(nodePoint->val);

            // 如果左子树存在，就将左子节点入队
            if (nodePoint->left){
                nodeQ.push(make_pair(nodePoint->left, level+1));
            }
            // 如果右子树存在，就将右子节点入队
            if (nodePoint->right){
                nodeQ.push(make_pair(nodePoint->right, level+1));
            }
        }
        return res;  
    }
};
```

#### 637 	二叉树的层平均值   (Easy)
与上一题一致

```c++
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        if (! root) return {};
        vector<double> nodesum;
        vector<int> cnt;
        queue<pair<TreeNode*, int>> nodeQ;
        nodeQ.push(make_pair(root, 0)); 
        while (!nodeQ.empty()){
            // 拿出队首的节点指针以及层次
            auto nodeLevel = nodeQ.front();
            auto nodePoint = nodeLevel.first;
            int level = nodeLevel.second;
            nodeQ.pop();  // 队首元素出队
            if (nodesum.size() <= level){
                nodesum.push_back(nodePoint->val);
                cnt.push_back(1);
            }
            else{
                nodesum[level] += nodePoint->val;
                cnt[level]++;
            }

            // 如果左子树存在，就将左子节点入队
            if (nodePoint->left){
                nodeQ.push(make_pair(nodePoint->left, level+1));
            }
            // 如果右子树存在，就将右子节点入队
            if (nodePoint->right){
                nodeQ.push(make_pair(nodePoint->right, level+1));
            }
        }
        for (int i = 0; i< nodesum.size(); i++){
            nodesum[i] /= cnt[i];
        }
        return nodesum;
    }
};
```



#### 513 找树左下角的值   (medium)
* 题解： 最左边的值，就是采用层次遍历保存每层开始的第一个值
	* 同样的层次遍历方法。


```c++
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        if (root == nullptr) return {};

        // 使用队列存储节点与节点所对应的层次
        queue<pair<TreeNode*, int>> nodeQ;
        // pair的第一个参数为每层的第一个节点值，第二个参数为层次
        pair<int, int> res(0, -1);
        // 将根节点以及对应的层次0，入队
        nodeQ.push(make_pair(root, 0));
        // 如果队列不为空，就一直遍历队列元素
        while (!nodeQ.empty()){
            // 拿出队首的节点指针以及层次
            auto nodeLevel = nodeQ.front();
            auto nodePoint = nodeLevel.first;
            int level = nodeLevel.second;
            nodeQ.pop();  // 队首元素出队

            // 如果开始了一个新的层次，将在这一层最左侧的元素保存。
            if (level > res.second){
                res.first = nodePoint->val;
                res.second = level;
            }

            // 如果左子树存在，就将左子节点入队
            if (nodePoint->left){
                nodeQ.push(make_pair(nodePoint->left, level+1));
            }
            // 如果右子树存在，就将右子节点入队
            if (nodePoint->right){
                nodeQ.push(make_pair(nodePoint->right, level+1));
            }
        }
        return res.first;  
    }
};
```




### DFS
深度优先遍历（DFS）就是**递归**访问一棵树。

#### 144 二叉树的前序遍历 (meidum)
前序遍历： 根——左——右

```c++
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder(root, res);
        return res;
    }
    void preorder(TreeNode* root, vector<int>& res){
        if (root == nullptr) return;
        res.push_back(root->val);
        preorder(root->left, res);
        preorder(root->right, res);
    }
};

```


#### 145 二叉树的后序遍历  (hard)
后序遍历： 左——右——根

```c++
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorder(root, res);
        return res;
    }

    void postorder(TreeNode* root, vector<int>& res){
        if (root == nullptr) return;
        postorder(root->left, res);
        postorder(root->right, res);
        res.push_back(root->val);
    }
};
```
#### 94 二叉树的中序遍历  (Medium)

中序遍历： 左——根——右

```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        return res;
    }
    void inorder(TreeNode* root, vector<int> & res){
        if (root == nullptr) return ;
        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
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


