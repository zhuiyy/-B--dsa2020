# 250201:位查询
总时间限制: 5000ms 内存限制: 65536kB

### 描述
给出N个范围在[0, 65535]的整数，编程支持以下的操作：
（1）修改操作：C d，所有的数都增加d。如果超过65535，把结果模65536。 0 <= d <= 65535
（2）查询操作：Q i，统计在N个正整数中有多少个整数其对应的二进制形式的第i位二进制位为非0。0 <= i <= 15。并且最低位i为0
最后，输出所有查询操作的统计值。

### 输入
输入的第一行为两个正整数N,M,其中N为操作的整数的个数，而M为具体有多少个操作。
输入的第二行为N个正整数，为进行操作的N个正整数。
下面有M行，分别表示M个操作。

N<=100000,M<=200000

### 输出
输出所有查询操作Q的统计值，每一个查询操作统计结果输出为一行。
### 样例输入
```
3 5
1 2 4
Q 1
Q 2
C 1
Q 1
Q 2
```
### 样例输出
```
1
1
2
1
```
### 提示
只输出查询操作Q的统计值。
