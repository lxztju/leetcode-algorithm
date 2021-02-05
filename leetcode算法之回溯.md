今天来盘一盘 **回溯 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)


## 回溯
**回溯法其实就是暴力法**。经常使用的暴力法就是**多层循环**， 但是面对**树形结构**的话很难采用循环的方式进行遍历。这时就要采用**递归回溯**的方法实现暴力法。

这类题目看似比较难，但是其实时很简单规范的套路性的代码， 下边几道题会有一个**固定的模板套路**， 请耐心体会。

* 17 电话号码的字母组合(medium)
* 93 复原IP地址（medium）
* 131 分割回文串(medium)
* 46 全排列(medium)
* 47 全排列 II(medium)
* 77 组合(medium)
* 39 组合总和(medium)
* 40 组合总和 II
* 216 组合总和 III
* 78 子集(medium)
* 90 子集II(medium)
* 79 单词搜索(medicum)
* 200 岛屿数量（medium）
* 130 被围绕的区域(medium)
* 417 太平洋大西洋水流问题（medium)
* 51 N皇后（hard）
* 52 N皇后 II（hard）
* 37 解数独（hard）


#### 17 电话号码的字母组合(medium)
* 一个树形结构
* 例如输入的数字为“23
* 那么这棵树的第一层有三个节点是 abc， 每个节点的下边有三个节点def。遍历这棵树得到所有的路径。

```c++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // 构建字典映射
        unordered_map<char, string> character2Num({
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        });
        // 定义返回值
        vector<string> res;
        string path;
        backtrace(digits, res, 0, path, character2Num);
        return res;
    }

    void backtrace(string digits, vector<string>& res, int index, string path, unordered_map<char, string>& character2Num){
        // 回溯递归函数
        if (digits.empty()) return ;
        // 如果遍历完成所有的数字，就保存得到的字母组合。
        if (index == digits.size()) {
            res.push_back(path);
            return ;
        }
        // 得到某个数字映射得到的字符串
        auto characters = character2Num[digits[index]];
        // 遍历这个字符串，相当于树形结构中的一层
        for (int i = 0; i < characters.size(); i++){
            path += characters[i];
            // 向树的下一层进行遍历
            backtrace(digits, res, index + 1, path, character2Num);
            // 回溯到上一层的时候，需要去除这一层的元素。
            path.pop_back();
        }   
     }
};
```

#### 93 复原IP地址（medium）
* 这个题也可以直接四层循环来做， 因为限制了最多分为4部分
* 这里依然采用回溯搜索法来处理。这种分割字符串的题目，使用回溯法是一个通用的套路。


```c++
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector< string> res;
        string path;

        backtrace(s, res, path, 0, 0);
        return res;
    }
    void backtrace(string& s, vector<string>& res, string path, int cnt, int startindex){
        // cnt表示分割的部分的数目，一共需要分割为4部分， startindex为接下来这一部分的开始位置
        if (cnt == 4){ 
            if (startindex == s.size())
                res.push_back(path);
            return;
        }
        
        for (int i = startindex; i < s.size(); i++){
            // 每一部分的最长长度为3
            if (i - startindex == 3) break;
            auto prepath = path;
            auto substring = s.substr(startindex, i - startindex + 1);
            // 如果长度部位0， 且开头的数字为0， 不合法的ip
            if ( i - startindex > 0 && s[startindex] == '0') break;

            // 如果大于255直接返回。
            if (stoi(substring) > 255 ) break;
            path += substring;
            if (i != s.size() - 1)
                path += ".";
            backtrace(s, res, path, cnt+1, i + 1);
            path = prepath;
        }
    }
};
```


#### 131 分割回文串(medium)

* 与上一题思路差不多， 没有上一题那么多需要排除的边界条件。

```c++
class Solution {
public:
    vector<vector<string>> partition(string s) {
        // 得到所有的子字符串，判断得到的是否都是回文串。
        vector<vector<string>> res;
        vector<string> palstring;
        string path;

        backtrace(s, res, palstring, 0);
        return res;
    }
    void backtrace(string& s, vector<vector<string>>& res, vector<string>& palstring, int startindex){
        if (startindex == s.size()){
            res.push_back(palstring);
            return ;
        }
        for (int i = startindex; i < s.size(); i++){
            auto substring = s.substr(startindex, i - startindex + 1);
            if ( ! ispalindrome(substring)) continue;
            palstring.push_back(substring);
            backtrace(s, res, palstring, i + 1);
            palstring.pop_back();
        }

    }
    bool ispalindrome(string s){
        int l = 0, r = s.size() - 1;
        while ( l < r){
            if (s[l] != s[r])
                return false;
            l++; r--;
        }
        return true;
    }

};
```


#### 46 全排列(medium)
* 依然是一个树形结构，标准的回溯法套路代码

```c++
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        unordered_set<int> visited;
        backtrace(nums, res, path, visited, 0);
        return res;
    }
    void backtrace(vector<int>& nums, vector<vector<int>>& res, vector<int>& path, unordered_set<int>& visited, int index){
        if (index == nums.size()){
            res.push_back(path);
            return ;
        }
        for (int i = 0; i< nums.size(); i++){
            if(visited.find(nums[i]) != visited.end()) continue;
            visited.insert(nums[i]);
            path.push_back(nums[i]);
            backtrace(nums, res, path, visited,  index+1);
            visited.erase(nums[i]);
            path.pop_back();
        }
    }
};
```

#### 47 全排列 II(medium)
* 与上一题的不同之处在于，这里存在重复的数字
* 也就是说如果在同一层中出现了相同的数字，那么会出现重复的情况。
* 采用排序的方式去重。

```c++
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> path;
        vector< vector<int> > res;
        unordered_set<int> visited;
        backtrace(nums, res, path, visited, 0);
        return res;
    }
    void backtrace(vector<int>& nums, vector<vector<int>>& res, vector<int>& path, unordered_set<int>& visited, int index){
        if (index == nums.size()){
            res.push_back(path);
            return ;
        }
        for (int i=0; i< nums.size(); i++){
            if (visited.find(i) != visited.end()) continue;
            // 这里采用nums中第i-1个元素如果没有访问过，说明在之后依然会出现，造成重复。
            if (i > 0 && nums[i] == nums[i-1] && visited.find(i - 1) == visited.end()) continue;
            visited.insert(i);
            path.push_back(nums[i]);
            backtrace(nums, res, path, visited, index+1);
            path.pop_back();
            visited.erase(i);
        }
    }
};
```

#### 77 组合(medium)
```c++

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> path;
        baketrace(n, k, 0, res, path);
        return res;
    }
    void baketrace(int n, int k, int index, vector<vector<int>>& res, vector<int>& path){
        if (k == 0){
            res.push_back(path);
            return;
        }
        // 如果剩余的数字不够组成k个数字的组合，那么直接返回
        if (n - index + 1 < k) return ;

        for(int i = 1; i <= n; i++){
            if (i <= index) continue;
            path.push_back(i);
            baketrace(n, k-1, i, res, path);
            path.pop_back();
        }
    }
};
```


#### 39 组合总和(medium)
* 与上一题的主要不同点在于一个元素可以多次选择，因此这里层的起始索引不再是i+1，而是i

```c++
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        
        backtrace(candidates, res, path, target, 0);
        return res;
    }
    void backtrace(vector<int>& candidates, vector<vector<int>>&res, vector<int>& path, int target, int index){
        if (target == 0){
            res.push_back(path);
            return ;
        }
        for (int i = 0; i< candidates.size(); i++){
            if (candidates[i] > target) continue;
            if (i < index) continue;
            path.push_back(candidates[i]);
            backtrace(candidates, res, path, target- candidates[i], i);
            path.pop_back();
        }
    }
};
```

#### 40 组合总和 II

```c++
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    // 每个数字只可以使用一次，并且可能含有重复的数字
    vector<vector<int>> res;
    vector<int> path;
    // 排序去重
    sort(candidates.begin(), candidates.end());
    unordered_set<int> visited;
    backtrace(candidates, res,  path, visited, 0, target);
    return res;
    }
    void backtrace(vector<int>& candidates, vector<vector<int>>&res, vector<int>& path, unordered_set<int>& visited, int index, int target){
        if(target == 0){
            res.push_back(path);
            return;
        }
        for (int i = index; i < candidates.size(); i++){
            
            if (candidates[i] > target) break;
            if ( i > 0 && candidates[i] == candidates[i-1] && visited.find(i-1) == visited.end()) continue;
            path.push_back(candidates[i]);
            visited.insert(i);
            backtrace(candidates, res, path, visited, i+1, target - candidates[i]);
            path.pop_back();
            visited.erase(i);
        }
    }
};
```


#### 216 组合总和 III

```c++
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        if ( k > 9 || n > 45) return {};
        vector<vector<int>> res;
        vector<int> path;
        vector<int> candidates({1,2,3,4,5,6,7,8,9});
        backtrace(candidates, res,  path,  0, n, k);
        return res;
    }
    void backtrace(vector<int>& candidates, vector<vector<int>>&res, vector<int>& path, int index, int target, int depth){
        if(target == 0 && depth == 0){
            res.push_back(path);
            return;
        }
        for (int i = index; i < candidates.size(); i++){
            if (candidates[i] > target) break;
            path.push_back(candidates[i]);
            backtrace(candidates, res, path, i+1, target - candidates[i], depth-1);
            path.pop_back();
        }
    }
};
```

#### 78 子集(medium)

```c++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        backtrace(nums, res, path, 0);
        return res;
    }
    void backtrace(vector<int>& nums, vector<vector<int>>& res, vector<int>& path, int index ){

        res.push_back(path);

        for (int i = index; i < nums.size(); i++){
            path.push_back(nums[i]);
            backtrace(nums, res, path, i+1);
            path.pop_back();
        }
    }
};
```

#### 90 子集II(medium)
```c++

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        // 同一层中不能有相同的元素， 排序去重
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        unordered_set<int> visited;
        backtrace(nums, res, path, visited, 0);
        return res;
    }
    void backtrace(vector<int>& nums, vector<vector<int>>& res, vector<int>& path,unordered_set<int>& visited, int index){
        res.push_back(path);
        for (int i = index; i< nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1] && visited.find(i - 1) == visited.end()) continue;
            visited.insert(i);
            path.push_back(nums[i]);
            backtrace(nums, res, path, visited, i + 1);
            path.pop_back();
            visited.erase(i);
        }
    }
};
```


* **下边的几道搜索的问题，也是一类非常经典的回溯问题。**
#### 79 单词搜索(medicum)
```c++

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<pair<int, int>> offsets({ {-1, 0}, {0, 1}, {1, 0}, {0 ,-1} });
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size(), 0));

        for (int i = 0; i< board.size(); i++){
            for (int j = 0; j< board[0].size(); j++){
                if (board[i][j] == word[0]){
                    if (backtrace(board, word, visited, offsets, i, j, 1))
                        return true;
                }
            }
        }
        return false;
    }

    bool backtrace(vector<vector<char>>& board, string& word, vector<vector<int>>& visited, vector<pair<int, int>>& offsets, int x, int y, int index){
        // if (board[x][y] != word[index]) return false;
        visited[x][y] = 1;

        if (index == word.size()) return true;

        for (auto off :offsets){

            int new_x = x + off.first;
            int new_y = y + off.second;

            if (!inboard(board, new_x, new_y)) continue;

            if (visited[new_x][new_y] == 1) continue;

            if (board[new_x][new_y] != word[index]) continue;

            if (backtrace(board, word, visited, offsets, new_x, new_y, index + 1))
                return true;
        }
        visited[x][y] = 0;
        return false;
    }
    bool inboard(vector<vector<char>>& board, int x, int y){
        return (x >= 0 && x < board.size()) && ( y >= 0 && y < board[0].size());
    }
};
```

#### 200 岛屿数量（medium）

```c++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        vector<pair<int, int>> offsets({ {-1, 0},{1, 0}, {0, 1}, {0, -1} });
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j++){
                if (grid[i][j] == '1'){
                    res++;
                    backtrace(grid, i, j, m, n, offsets);
                }
            }
        }
        return res;
    }
    void backtrace(vector<vector<char>>& grid, int x, int y, int m, int n, vector<pair<int,int>>& offsets){
        grid[x][y] = '0';
        for (auto off: offsets){
            int new_x = x + off.first;
            int new_y = y + off.second;
            if (!inboard(m, n, new_x, new_y) || grid[new_x][new_y] == '0') continue;
            backtrace(grid, new_x, new_y, m, n, offsets);
        }    
    }

    bool inboard(int m, int n, int x, int y){
        return (x >= 0 && x < m) && (y >= 0 && y < n);
    }
};
```


#### 130 被围绕的区域(medium)
```c++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        //找到与边界联通的O，标记为o，然后将剩余的O变为x，o变为O即可
        if (board.empty()) return ;
        vector<pair<int, int>> offsets({{1, 0},{-1, 0}, {0, 1}, {0, -1}});
        int m = board.size(), n = board[0].size();
        // 遍历边界
        for ( int i = 0; i< m; i++){
            if (board[i][0] == 'O')
                backtrace(board, i, 0, offsets);
            if (board[i][n-1] == 'O')
                backtrace(board, i, n-1, offsets);
        }
        for (int j = 0; j < n; j++){
            if (board[0][j] == 'O')
                backtrace(board, 0, j, offsets);
            if (board[m- 1][j] == 'O')
                backtrace(board, m-1, j, offsets);            
        }
        // 替换内部的O
        for ( int i = 0;i< m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }
        // 将边界的o换回O
        for ( int i = 0;i< m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == 'o')
                    board[i][j] = 'O';
            }
        }
    }

    void backtrace(vector<vector<char>>& board, int x, int y, vector<pair<int, int>>& offsets){
        board[x][y] = 'o';
        for (auto off: offsets ){
            int new_x = x + off.first;
            int new_y = y + off.second;
            if (! inboard(board, new_x, new_y) || board[new_x][new_y] != 'O') continue;
            backtrace(board, new_x, new_y, offsets);
        }
    }

    bool inboard(vector<vector<char>>& board, int x, int y){
        return (x >= 0 && x < board.size()) && ( y >= 0 && y < board[0].size());
    }
};
```

#### 417 太平洋大西洋水流问题（medium)

```c++
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        //使用两个数组分别表示能流到大西洋atlantic与太平洋pacific的位置
        if (matrix.empty()) return {};
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        vector<vector<bool>> pacific(m, vector<bool>(n, false));

        vector<pair<int, int>> offsets({ {-1, 0},{0, -1},{1, 0},{0, 1}});
        vector<vector<int>> res;

        for (int i  = 0; i< m; i++){
            if (! pacific[i][0])
                backtrace(matrix, i, 0, pacific, offsets);
            if (! atlantic[i][n-1])
                backtrace(matrix, i, n-1, atlantic, offsets);
        }
        for (int j  = 0; j< n; j++){
            if (! pacific[0][j])
                backtrace(matrix, 0, j, pacific, offsets);
            if (! atlantic[m-1][j])
                backtrace(matrix, m-1, j, atlantic, offsets);
        }
        for (int i =0; i<m; i++){
            for (int j = 0; j<n; j++){
                if (atlantic[i][j] && pacific[i][j])
                    res.push_back({i, j});
            }
        }
        return res;
    }
    
    void backtrace(vector<vector<int>>& matrix, int x, int y, vector<vector<bool>>& ocean, vector<pair<int, int>>& offsets){
        ocean[x][y] = true;
        for (auto off: offsets){
            int new_x = x + off.first;
            int new_y = y + off.second;
            if (!inboard(matrix, new_x, new_y) || matrix[new_x][new_y] < matrix[x][y] || ocean[new_x][new_y]) continue;
            backtrace(matrix, new_x, new_y, ocean, offsets);
        }
    }

    bool inboard(vector<vector<int>>& matrix, int x, int y){
        return (x >= 0 && x < matrix.size()) && ( y >= 0 && y < matrix[0].size());
    }
};
```

#### 51 N皇后（hard）
```c++
class Solution {
public:
    vector<vector<string>> queues;
    vector<vector<string>> solveNQueens(int n) {
        //主对角线i- j为常数，范围为1-n到n-1
        // 副对角线i+j为常数，范围为0到2*n-2
        vector<int> diag(2*n-1, false); //主对角线，i - j + n - 1为其索引对应的对角线
        vector<int> otherdiag(2*n-1, false); // 副对角线i + j 为其索引对应的对角线。
        vector<int> queue(n, -1); //表示每行放置在哪一列。
        unordered_set<int> cols;  // 表示已经放置的列


        backtrace(n, diag, otherdiag, queue, cols, 0);

        return queues; 

    }
    void backtrace(int n, vector<int>& diag, vector<int>& otherdiag, vector<int>& queue, unordered_set<int> cols, int row){
        if (row == n){
            queues.push_back(generateString(queue, n));
            return ;
        }
        for (int j = 0; j < n; j++){
            if (diag[row-j+n-1] || otherdiag[row+j] || cols.find(j) != cols.end()) continue;
            diag[row-j+n-1] = true;
            otherdiag[row+j] = true;
            cols.insert(j);
            queue[row] = j;
            backtrace(n, diag, otherdiag, queue, cols, row + 1);
            diag[row-j+n-1] = false;
            otherdiag[row+j] = false;
            queue[row] = -1;
            cols.erase(j);
        }
    }
    vector<string> generateString(vector<int>& queue, int n){
        vector<string> res(n, string(n, '.'));

        for (int i=0; i< n; i++)
            res[i][queue[i]] = 'Q';

        return res;
    }
};

```


#### 52 N皇后 II（hard）

```c++
class Solution {
public:
    int totalNQueens(int n) {
        vector<bool> diag(2*n - 1, false); // 主对角线是否占用， i-j+n-1为其主对角线的索引
        vector<bool> otherdiag(2*n-1, false); //副对角线，i+j为其索引
        unordered_set<int> cols; // 保存已经被占用的列
        vector<int> queue(n, -1); //表示每个元素分别放置在第j列的位置。
        int res = 0;
        backtrace(n, diag, otherdiag, cols, queue, res, 0);
        return res;
    }
    void backtrace(int n, vector<bool>& diag, vector<bool>& otherdiag, unordered_set<int>& cols, vector<int>& queue, int& res, int row){
        if (row == n){
            res++;
            return ;
        }
        // 第row行可以放的列的位置，遍历查找
        for (int i=0; i< n; i++){
            if(diag[row - i + n - 1] || otherdiag[row + i] || cols.find(i) != cols.end()) continue;
            diag[row - i + n - 1 ] = true;
            otherdiag[row + i] = true;
            cols.insert(i);
            queue[row] = i;
            backtrace(n, diag, otherdiag, cols, queue, res, row+1);
            diag[row - i + n - 1 ] = false;
            otherdiag[row + i] = false;
            cols.erase(i);
            queue[row] = -1;           
        }
    }
};
```


#### 37 解数独（hard）



```c++
class Solution {
public:
    bool valid = false;
    void solveSudoku(vector<vector<char>>& board) {
        vector<unordered_set<int>> rows(9, unordered_set<int>()); //每行出现过的数字
        vector<unordered_set<int>> cols(9, unordered_set<int>()); //每列出现过的数字
        vector< unordered_set<int> > grids(9, unordered_set<int>()); // 第i个3x3的格子出现过的数字，其索引为（i/3）*3 + j/3
        vector<pair<int, int>> spaces;
        for ( int i = 0; i <9; i++){
            for (int j = 0; j < 9; j++){
                if (board[i][j] == '.')
                    spaces.push_back(make_pair(i, j));
                else{
                    int digit = int(board[i][j] - '0');
                    rows[i].insert(digit);
                    cols[j].insert(digit);
                    grids[(i/3)*3+j/3].insert(digit);
                }
            }
        }
        backtrace(board, rows, cols, grids, spaces, 0);
        return;
    }
    void backtrace(vector<vector<char>>& board, vector<unordered_set<int>>& rows, vector<unordered_set<int>>& cols, vector<unordered_set<int>>& grids, vector<pair<int, int>>& spaces, int index){
        if ( index == spaces.size()) {
            valid = true;
            return ;
        }
        int i = spaces[index].first;
        int j = spaces[index].second;
        // 放置 k 这个数字
        for (int k = 1; k <= 9; k++){
            if (valid) break;
            if ( rows[i].find(k) != rows[i].end() || cols[j].find(k) != cols[j].end() || grids[(i/3)*3+j/3] .find(k) != grids[(i/3)*3+j/3].end() ) 
                continue;
            rows[i].insert(k);
            cols[j].insert(k);
            grids[(i/3)*3+j/3].insert(k);
            board[i][j] = (char) ('0' + k);
            backtrace(board, rows, cols, grids, spaces, index+1);
            rows[i].erase(k);
            cols[j].erase(k);
            grids[(i/3)*3+j/3].erase(k);
            // board[i][j] = '.';
        }
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

