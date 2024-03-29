# Numpy -> Numeric Python library for Scientific and mathematical computation
import numpy as np

a = np.array([40, 50, 60])  # similar datatype
b = np.array([10, 20, 30])
c = np.array([15, 52, "98"])

print(a + b)
print(a * b)
print(c)  # convert all  to string

# ================================================================

# arr = np.array(([10, 20, 30, 40]))
# print(arr)
# print(type(arr))  # <class 'numpy.ndarray'> nd= n dimensional array

# arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2)

# Slicing
# arr = np.array(([10, 20, 30, 40]))
# print(arr[0:3]) #upto 3 elements

# arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [25, 45, 65, 75]])
# print(arr[0:2,0:2 ])
# print(arr[0, 1:3])  # 1st array
# print(arr[1, 2:4])  # 2nd array

# print(arr.shape)  #3 row 4 col
# print(arr.size)    #3*4=12
# print(arr.ndim)    #2 dim array
# print(arr.dtype)   #datatype
# print(arr.astype(str))  # convert datatype

# ====================================================================
# Mathematical operation on arrays

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
#
# # print(np.add(arr1, arr2))
# # print((np.subtract(arr2,arr1)))
# # print(np.multiply(arr1,arr2))
#
# arr3 = np.array([3])
# print(np.power(arr1, arr3))
#
# arr4 = np.array([16,25,36,49])
# print(np.sqrt(arr4))

# ========================================================================
# Combining and Splitting array

# arr1 = np.array([30,40,50,60])
# arr2 = np.array([6,7,8])
# print(np.concatenate([arr1,arr2]))

# arr1 = np.array([[30, 40], [50, 60]])
# arr2 = np.array([[6, 7], [8, 9]])
# print(np.concatenate([arr1, arr2],axis = 1)) #Horizontal/vertical concat

# print(np.hstack([arr1, arr2]))   #Hor/vert stack
# print(np.vstack([arr1, arr2]))

# ============================================================================
# Split

# a = np.array([10, 20, 30, 40, 50, 60])
# b = np.array_split(a, 3)  # Split into 3 parts
# print(b)
# print(b[1])

# ==============================================================================
# a = np.array([20,40,60,80])
# print(np.append(a,90))
# print(np.insert(a,1,50))  #array,index,value

# b= np.array([[45,65],[55,75]])
# # print(np.append(b,[25,35]))
# #
# print(np.insert(b,[1,2],[40,50],axis = 0))
#
# print(np.delete(b,1,axis = 0))

# ===============================================================================
# Sort filter search

ar = np.array([45, 8, 91, 53, 17, 6])
# print((np.sort(ar)))
#
# s = np.where(ar == 8)  # s-> index
# print(s)
#
# ss = np.searchsorted(ar, 91)  # index after sorting
# print(ss)


# fa = [True, False, True, False, True, False]  #True-> will come, False-> wont
# new = ar[fa]
# print(new)

# fa = ar > 44
# new2 = ar[fa]
# print(new2)

# ================================================================================
# Aggregate Function

a = np.array([45, 55, 75, 89, 69])

# print((np.sum(a)))
# print((np.min(a)))
# print((np.max(a)))
# print((np.size(a)))
# print(np.mean(a))
# print(np.cumsum(a))   #Cumulative sum
# print(np.cumprod(a))  #cumulative product

# price = np.array([100, 150, 199, 200, 250, 130])
# quantity = np.array([10, 20, 30, 40, 50, 60])
#
# # print(price,"\n", quantity)
# #
# # print(np.sum(price))
#
# print(np.cumprod([price, quantity], axis=0))
# c = (np.cumprod([price, quantity], axis=0))  # [ 1000  3000  5970  8000 12500  7800]]
#
# print(np.sum(c[1]))  # sum 38270
#
#  ================================================================================

# Statistical funcn in array
import statistics as stat

# baked_food = [200, 300, 150, 130, 200, 280, 170, 188]
#
# a = np.array(baked_food)
# print((np.mean(a)))  # 202.25
#
# print(np.median(a))  # 194.0
#
# print((np.sort(a)))  # [130 150 170 188 200 200 280 300]
#
# print(stat.mode(a))  # numpy does not have mode, so import statistics library
#
# print(np.std(a))  # standard deviation
#
# print(np.var(a))  # variance = (std deviation)^2


# tobaco_cons = [30, 50, 40, 30, 40, 10]
# deaths = [100, 120, 70, 100, 120, 112]
#
# print(np.corrcoef([tobaco_cons, deaths]))  # -1 => inversely proportional,
# 1 -> proportional, -> 0-> no relation

# price = [300,100,350,150,200]
# sales = [10,20,7,17,14]
#
# print(np.corrcoef([price,sales]))
# [[ 1.        -0.9968004]
#  [-0.9968004  1.       ]]
# negative means with increase of price the sales are decreasing
