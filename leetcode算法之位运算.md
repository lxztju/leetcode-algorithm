今天来盘一盘 **位运算 ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)

## 位运算

* 461 汉明距离 (Easy)
* 136 只出现一次的数字   (Easy)
* 268 	丢失的数字 (Easy)
* 260 只出现一次的数字 III (Medium)
* 190 颠倒二进制位 (Easy)
* 231 	2的幂 (Easy)
* 342 	4的幂 (Easy)
* 693 交替位二进制数  (Easy)
* 476 数字的补数  (Easy)
* 371 两整数之和   (Easy)
* 318 最大单词长度乘积  (Medium)
* 338 	比特位计数 (Medium)


#### 461 汉明距离 (Easy)


```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
    // 统计不同的位数
        auto sx = bitTransfer(x);
        auto sy = bitTransfer(y);
        int cnt = 0;
        for ( int i = 0; i< 32; i++){
            if (sy[i] != sx[i])
                cnt++;
        }
        return cnt;

    }
    string bitTransfer(int x){
        // 将转换为01的二进制字符串
        string s(32, '0');
        if (x == 0) return s;
        int i = 31;
        while ( x > 0){
            int res = x % 2;
            s[i] = (res + '0');
            x /= 2;
            i--;
        }
        return s;
    }
};
```

* 异或操作

```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
    // 利用异或操作，不同的为1， 然后统计1的个数
        int res = x ^ y;
        int cnt = 0;
        while ( res > 0){
            cnt += (res & 1);
            res >>= 1;
        }
        return cnt;

    }

};

```


#### 136 只出现一次的数字   (Easy)
* 相同元素的异或值为0
* 0与任何元素的异或值为其自身
* 因此整个序列所有元素的异或值即为仅仅出现一次的元素

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (auto num:nums){
            res ^= num;
        }
        return res;
    }
};
```

* 这个题也可以排序，然后查找仅仅出现一次的元素

* 也可以利用哈希表来查找。 

#### 268 	丢失的数字 (Easy)
* 方法1： 排序
* 方法2： 哈希表


* 方法3： 位运算
	* 与上一题的处理方法类似，新构建一个0-n的数组6与原来的数组结合形成大数组，缺失的数字就是在新数组中及你进出现一次的数字

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0;
        for ( int i=0; i< nums.size(); i++){
            res ^= (nums[i] ^ i);
        }
        return res ^ nums.size();
    }
};

```

#### 260 只出现一次的数字 III (Medium)

```c++
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        // 整个数组进行异或操作，得到两个单独出现的字符的异或值
        int numXor = 0;
        for (auto num: nums)
            numXor ^= num;

        // 按照这个异或者，将原始数组分为两部分，每个单独出现的数字分别位于其中的一部分。
        int split = 1;
        while ((numXor & split) == 0){
            split <<= 1;
        }
        vector<int> res(2, 0);
        for (auto num : nums){
            if (num & split)
                res[0] ^= num;
            else
                res[1] ^= num;
        }
        return res;
    }
};

```

#### 190 颠倒二进制位 (Easy)

* 直接颠倒


```c++
class Solution {
  public:
  uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0, power = 31;
    while (n != 0) {
      res += (n & 1) << power;
      n >>= 1;
      power -= 1;
    }
    return res;
  }
};
```

#### 231 	2的幂 (Easy)

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        int res = 0;
        int cnt = 0;
        if ( n < 0) return false;
        while ( n != 0){
            if ((n & 1) == 1)
                cnt++;
            n >>= 1;
        }
        return cnt == 1;
    }
};
```


```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return ( n > 0 && (( n & (n - 1) )== 0) );
    }
};
```

#### 342 	4的幂 (Easy)

```c++
class Solution {
public:
    bool isPowerOfFour(int num) {
    	// 2的幂
        if (num > 0 && (num & ( num - 1 )) == 0)
        	// 判断是否是4的幂
            return (num & 0x55555555) == num;
        return false;
    }
};
```

#### 693 交替位二进制数  (Easy)
* 直接模拟整个交替过程，判断是否交替。

```c++
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int tmp1 = n & 1;
        n >>= 1;
        while ( n != 0){
            int tmp2 = n & 1;
            n >>= 1;
            if (tmp1 == tmp2)
                return false;
            tmp1 = tmp2;
        }
        return true;
    }
};
```

#### 476 数字的补数  (Easy)
* 101(5)的补数为111(7)减101

```c++
class Solution {
public:
    int findComplement(int num) {
        long tmp = 1;
        while( tmp <= num){
            tmp <<= 1;
        }
        return tmp - 1 - num;
    }
};

```

#### 371 两整数之和   (Easy)

```c++
class Solution {
public:
    int getSum(int a, int b) {
        return a + b;
    }
};
```

* 题目要求不使用+ -符号
* 使用在数字电子电路中，加法电路的设计方式
* 针对二进制位，进位位为采用两个二进制的与运算， 和为两个二进制的异或运算的结果。

```c++
class Solution {
public:
    int getSum(int a, int b) {

        while (b){
            auto carry = (static_cast<unsigned int> (a & b) )<< 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
};

```

#### 318 最大单词长度乘积  (Medium)
* 使用位运算作为编码来统计出现字母的种类数。

```c++
class Solution {
public:
    int maxProduct(vector<string>& words) {
        // 使用一个整形数字来表每个单词所含有字母的种类。，这个整形数字的后26位，如果某一位为1，说明出现这个字母
        int n = words.size();
        vector<int> code(n, 0);
        for (int i = 0; i < n; i++){
            for (int j=0; j < words[i].size(); j++){
                code[i] |= 1 << (words[i][j] - 'a');
            }
        }
        int res = 0;
        for ( int i = 0; i < n-1; i++){
            for ( int j = i+1; j < n; j++){
                if ((code[i] & code[j]) == 0){
                    int tmp = (words[i].size()) * (words[j].size());
                    res = max(res, tmp);
                }
            }
        }
        return res;
    }
};
```

#### 338 	比特位计数 (Medium)

* 直接统计

```c++
class Solution {
public:
    vector<int> countBits(int num) {
        // 直接统计
        vector<int> res;
        for (int i = 0; i<=num; i++){
            int tmp = 0;
            int tmp1 = i;
            while (tmp1 != 0){
                tmp += (tmp1 & 1);
                tmp1 >>= 1;
            }
            res.push_back(tmp);
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
* 知乎专栏： [https://www.zhihu.com/column/c_1101089619118026752](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[https://www.yanxishe.com/column/109](https://www.yanxishe.com/column/109)

