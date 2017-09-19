#汉诺塔问题
i=0
def move(n, a, b, c):
    if n == 1:
        global i #函数里要想引用全局变量，前面加global关键字
        i+=1
        print('move', a, '-->', c) #只有一个盘子是直接将初塔上的盘子移动到目的地  
    else:
        move(n-1, a, c, b) #先将初始塔的前n-1个盘子借助目的塔移动到借用塔上
        move(1, a, b, c) #将剩下的一个盘子移动到目的塔上
        move(n-1, b, a, c) #最后将借用塔上的n-1个盘子移动到目的塔上

move(3, 'A', 'B', 'C')
print('step is',i)