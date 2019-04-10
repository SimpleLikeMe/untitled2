

# 列表生成式
list1 = [x for x in range(10)]
iter(list1)

print(next(list1))
for l in list1:
    print(l)




# 裴波拉契数列函数式生成器
def fun(num):
    a, b = 0, 1
    count = 0

    while count < num:
        yield a
        a, b = b, a + b
        # print(count)
        count += 1


print(next(fun(10)))



