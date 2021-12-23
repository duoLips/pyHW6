# """дз 1"""
#
# list1 = [1, 2, 3, 4, 5]
# tuple1 = tuple(list1)
# print(tuple1)
# print(type(tuple1))

# """дз 2"""
# SampleList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# expected = [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# for i in range(0, 3):
#     SampleList[i] = list(SampleList[i])
#     SampleList[i][2] = 100
# for i in range(0, 3):
#     SampleList[i] = tuple(SampleList[i])
# print(SampleList)
# print(expected)

# """дз 3"""
# nums = [(1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1)]
# expected = (6, 9, 8, 6)
# output = []
# for k in range(0, 4):
#     sum1 = (nums[0][k] + nums[1][k] + nums[2][k])
#     output.append(sum1)
# print(tuple(output))

# """дз 4"""
# set1 = set([0, 1, 2, 3, 4, 5])
# a = int(input())
# for i in set1:
#     if (i == a):
#         print('a exists')

# """дз 5"""
#
# a = {12, "vqq", 4, "w", "3", 20}
# b = {1, "vq", 2, "q", 3, 0}
# if (a & b):
#     print(a & b)
# else:
#     print("No common elements")

# """дз 6"""
# a = {1, "vq", 4, "q", 3, 10}
# b = {1, "vq", 2, "q", 3, 0}
# if (a - b):
#     print(a - b)
# else:
#     print("none")

# """дз 7"""
# a = {1, "vq", 4, "q", 3, 10}
# b = {1, "vqq", 2, "q", 3, 0}
# c = (a & b)
# for i in c:
#     a.discard(i)
# print(a)
