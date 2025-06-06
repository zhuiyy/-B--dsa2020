'''
描述
有n堆果子（n<=10000），多多决定把所有的果子合成一堆。

每一次合并，多多可以把两堆果子合并到一起，消耗的体力等于两堆果子数量之和。可以看出，所有的果子经过n-1次合并之后，就只剩下一堆了。多多在合并果子时总共消耗的体力等于每次合并所耗体力之和。

设计出合并的次序方案，使多多耗费的体力最少，并输出这个最小的体力耗费值。

输入
两行，第一行是一个整数n(1<＝n<=10000)，表示果子的种类数。
第二行包含n个整数，用空格分隔，第i个整数ai(1<＝ai<=20000)是第i堆果子的数目。
输出
一行，这一行只包含一个整数，也就是最小的体力耗费值。输入数据保证这个值小于2^31。
样例输入
3 
1 2 9
样例输出
15
提示
哈夫曼编码
'''


n=int(input())
fruits=list(map(int,input().split()))
fruits.sort(reverse=True)
energy=0
for _ in range(n-1):
    t=fruits.pop()
    t+=fruits.pop()
    energy+=t
    fruits.append(t)
    fruits.sort(reverse=True)
print(energy)

