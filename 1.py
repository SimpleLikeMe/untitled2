

# �б�����ʽ
list1 = [x for x in range(10)]
iter(list1)

print(next(list1))
for l in list1:
    print(l)




# �Შ�������к���ʽ������
def fun(num):
    a, b = 0, 1
    count = 0

    while count < num:
        yield a
        a, b = b, a + b
        # print(count)
        count += 1


print(next(fun(10)))



