今天来盘一盘 **图 ** 这类题目

这类题目对我来说也是比较难的，比较难搞。

```
有向无环图的拓扑排序（BFS， DFS）

利用并查集处理连通域问题
```

使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 图

### BFS与DFS

* 785 	判断二分图  (Medium)
* 207 课程表 (Medium)
* 210 课程表 II (Medium)

### 并查集

并查集是一种树型的数据结构，主要用于处理连通域的问题，用于处理一些不交集的合并及查询问题。主要的操作有如下的步骤：

Find：确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一子集。
Union：将两个子集合并成同一个集合。

* 684 冗余连接 (Medium)


### BFS与DFS



#### 785 	判断二分图  (Medium)
使用染色法，0代表一种颜色，1代表另外一种颜色， -1表示未染色，相邻的元素不能染成同样的颜色。

* DFS

```c++
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> colors(n, -1);
        for (int i = 0; i< n; i++){
            if (colors[i] == -1){
                if (!dfs(graph, colors, i, 0))
                    return false;
            }
        }
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& colors, int index, int c){
        
        colors[index] = c;
        for (int i = 0; i < graph[index].size(); i++){
            int node = graph[index][i];
            if (colors[node] != -1){
                if (colors[node] == c) return false;
                else continue;
            }
            else    
                if ( ! dfs(graph, colors, node, 1-c))
                    return false;
        }
        return true;
    }
};
```

* BFS

```c++
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> colors(n, -1);
        queue<pair<int, int>> q;
        for (int i = 0; i<n; i++){
            if ( colors[i] != -1) continue;
            q.push(make_pair(i, 0));
            while (! q.empty()){
                auto nodeLevel = q.front();
                int node = nodeLevel.first;
                int level = nodeLevel.second;
                q.pop();
                if (level % 2 == 0){
                    if (colors[node] == 1)
                        return false;
                    colors[node] = 0;
                }
                else{
                    if (colors[node] == 0)
                        return false;
                    colors[node] = 1;
                }
                for (auto node1 : graph[node]){
                    if (colors[node1] == -1)
                        q.push(make_pair(node1, level+1));
                }
            }
        }
        return true;
    }
};
```


#### 207 课程表 (Medium)

* DFS

```c++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 不能有环， dfs
        vector<int> visited(numCourses, -1); // -1表示没有访问过， 0表示被其他节点访问过，1表示被本节点访问过
        vector<vector<int>> edges(numCourses, vector<int>());

        // 构建邻接表
        for (int i = 0; i < prerequisites.size(); i++){
            int start = prerequisites[i][1];
            int end = prerequisites[i][0];
            // cout<<start<<" "<<end<<endl;
            edges[start].push_back(end);
        }

        for( int i = 0; i < numCourses; i++){
            if (visited[i] != -1) continue;
            if (! dfs(edges, visited, i))
                return false;
        }
        return true;
    }

    bool dfs(vector<vector<int>>& edges, vector<int>& visited,int index){
        
        if (visited[index] == 1) return false;
        if (visited[index] == 0) return true;
        visited[index] = 1;
        for (auto node : edges[index]){
            if (! dfs(edges, visited, node))
                return false;
        }
        visited[index] = 0;
        return true;
    }
};
```


* BFS（入度表）


```c++
/*
1. 转换为邻接表并生成入度表
2. 将入度为0的节点入队。
3. 遍历整个队列，如果队列不为空，将队首出列，并将邻接节点的入度减一，将入度为0的节点重新入度。
*/
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 不能有环， dfs
        vector<int> indegrees(numCourses, 0);
        vector<vector<int>> edges(numCourses, vector<int>());

        // 构建邻接表与入度表
        for (int i = 0; i < prerequisites.size(); i++){
            int start = prerequisites[i][1];
            int end = prerequisites[i][0];
            edges[start].push_back(end);
            indegrees[end]++;
        }
        queue<int> q;
        // 将入度为0的节点入队
        for (int i = 0; i < numCourses; i++){
            if (indegrees[i] == 0)
                q.push(i);
        }
        while (!q.empty()){
            int node = q.front();
            q.pop();
            // 将邻接的节点入度数减一，并将入度为0的节点入队
            for (auto j : edges[node]){
                indegrees[j]--;
                if (indegrees[j] == 0)
                    q.push(j);
            }
        }
        // 如果有的节点入度数不为0，那么说明存在环
        for (auto i: indegrees){
            if (i != 0) return false;
        }
        return true;
    }
};
```




#### 210 课程表 II (Medium)

* DFS

```c++

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> edges(numCourses, vector<int>());
        for (int i= 0; i < prerequisites.size(); i++){
            int start = prerequisites[i][1];
            int end = prerequisites[i][0];
            edges[start].push_back(end);
        }

        // for(auto p: edges){
        //     for (auto v:p)
        //         cout<<v<<"  ";
        //     cout<<endl;
        // }

        vector<int> visited(numCourses, -1); // -1表示没有访问过， 0表示被其他节点访问过，1表示被本节点访问过
        vector<int> res;
        for( int i = 0; i < numCourses; i++){
            if (visited[i] != -1) continue;
            if (! dfs(edges, visited, res, i))
                return {};
        }
        reverse(res.begin(), res.end());
        return res;
    }

    bool dfs(vector<vector<int>>& edges, vector<int>& visited, vector<int>& res,  int index){
        
        if (visited[index] == 1) return false;
        if (visited[index] == 0) return true;
        visited[index] = 1;
        for (auto node : edges[index]){
            if (!dfs(edges, visited, res, node))
                return false;
        }
        res.push_back(index);
        visited[index] = 0;
        return true;
    }
};
```

* BFS

```c++
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> edges(numCourses, vector<int>());
        vector<int> indegress(numCourses, 0);
		// 构建邻接表，入度表
        for (int i= 0; i < prerequisites.size(); i++){
            int start = prerequisites[i][1];
            int end = prerequisites[i][0];
            edges[start].push_back(end);
            indegress[end]++;
        }

        queue<int> q;
        vector<int> res;
		// 将入度为0的节点入队
        for (int i = 0; i < numCourses; i++){
            if (indegress[i] == 0)
                q.push(i);
        }
        // 遍历队列
        while (!q.empty()){
            int node = q.front();
            res.push_back(node);
            q.pop();
            // 将邻接节点的入度数减一，并将入度为0的节点入队。
            for (auto i : edges[node]){
                indegress[i]--;
                if (indegress[i] == 0)
                    q.push(i); 
            }
        }
        // 如果存在入度不为0的节点，说明存在一个环
        for (auto i: indegress){
            if ( i != 0) 
                return {};
        }
        return res;
    }
};
```


### 并查集

####  684 冗余连接 (Medium)
经典的并查集的套路代码。

```c++
class Solution {
public:
    int find(vector<int>&parent, int index){
    // 查找一个给定节点的父亲节点。递归的操作。
        if (parent[index] != index)
            parent[index] = find(parent, parent[index]);
        return parent[index];
    }

    void Union(vector<int>& parent, int index1, int index2){
    // index2的父亲节点转换为index1与index2共同的父亲节点。
        parent[find(parent,index1)] = find(parent,index2);
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n+1, 0);
        // 初始化的情况下，每个节点的父亲节点都是自身
        for (int i = 1; i< n+1; i++){
            parent[i] = i;
        }

        for (auto edge: edges){
            int node1 = edge[0], node2 = edge[1];
            // 对于两个节点，如果其父亲节点不一样就融合这两个节点
            if (find(parent, node1) != find(parent, node2))
                Union(parent, node1, node2);
            else
                return edge;
        }
        return {};
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

