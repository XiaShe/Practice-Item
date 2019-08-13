#####################################
'''1.猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
#解
import random
answer = random.randint(1, 100)
count = 0
while True:
    count += 1
    number = int(input("请输入一个1~100的数字："))
    if number > answer:
        print("大了")
    elif number < answer:
        print("小了")
    else:
        print("牛逼")
        break
if count >= 3:
    print("不过真TM慢")
'''
#####################################
'''2.判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
#解
num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
'''
#####################################
'''3.输出2~99之间的素数
#解
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
'''
#####################################
'''4.输出乘法口诀表(九九表)
#解
for i in range(1,10):
    for n in range(1,i+1):
        print("%d * %d = %d" % (n,i,i*n),end='\t')
    print()
'''
#####################################
'''5.找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
#解
import time
import math

for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
'''
#####################################
'''6.买鸡，1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
#解
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
'''
#####################################
'''7.Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
#解
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:#如果猜对一直执行
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False
print('你破产了, 游戏结束!')
'''
#####################################
'''8.输出斐波那契数列的前20个数
#解
1 1 2 3 5 8 13 21 ...
#8
a = 0
b = 1
for i in range(20):
    a, b = b, a + b
    print(a)
'''
#####################################
'''9.找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
#解
for num in range(100,1000):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if num == a**3 + b**3 + c**3:
        print(num)
'''
