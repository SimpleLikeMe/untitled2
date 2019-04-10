from collections.abc import Iterator, Iterable



list1 = [1, 3, 5, 7, 9]
tuple1 = (2, 4, 6, 8, 10)
dict1 = {"name": "lisa", "age": 10, "gender": "女"}
str1 = "hello world"
num = 3

print("list可迭代:", isinstance(list1, Iterable), "\tlist迭代器：", isinstance(list1, Iterator))
print("tuple可迭代:", isinstance(tuple1, Iterable), "\ttuple迭代器：", isinstance(tuple1, Iterator))
print("dict可迭代:", isinstance(dict1, Iterable), "\tdict迭代器：", isinstance(dict1, Iterator))
print("str可迭代:", isinstance(str1, Iterable), "\tstr迭代器：", isinstance(str1, Iterator))
print("int可迭代:", isinstance(num, Iterable), "\tint迭代器：", isinstance(num, Iterator))




