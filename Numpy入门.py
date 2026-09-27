#导包
import numpy as np#给导包起别名

arr1 = np.arange(15).reshape(3,5)
print(arr1)
print(f'numpy的轴:{arr1.ndim}')
print(f'numpy的维度:{arr1.shape}')
print(f'numpy的元素类型:{arr1.dtype}')#int32
print(f'numpy的长度:{arr1.size}')#15
print(f'numpy元素占用字节数:{arr1.itemsize}')#32/8=4
print(f'numpy的元素类型:{type(arr1)}')#ndarray,numpy数组称为ndarray,下标从0开始，元素相同类型

#创建numpy的ndarray对象

#array()函数,把python列表转成ndarray
my_list=[11,22,33,44] #python列表对象
print(type(my_list))#list
arr2=np.array(my_list)
print(type(arr2))#ndattay

#arange()函数创建ndarray对象
#arange(起始，结束，步长，dtype=类型)类似于python中的array()
arr3=np.arange(0,10,2,dtype=np.float32)#包左不包右
print(arr3)
print(type(arr3))
print(arr3.dtype)#元素的类型

#随机数生成ndarray
#random.rand() 生成0.0~1.0之间包左不包右的随机小数矩阵
arr4=np.random.rand(3,5)#3行5列
print(arr4)
print(type(arr4))

#random.randint(起始值，结束值，size=（行，列）) 生成指定范围，包左不包右的，随机整数矩阵
arr5=np.random.randint(3,9,size=(2,6))#3到9之间，2行6列
print(arr5)
print(type(arr5))

#random.uniform(起始，结束，size（行，列）)小数
arr6=np.random.uniform(3,9,size=(2,6))
print(arr6)
print(type(arr6))

#numpy的类型转换astype()
arr7=np.arange (0,10,2,dtype=np.int64)
print(arr7)
print(arr7.dtype)
#把arr7 ndarray对象的元素类型，从int转成float
arr8=arr7.astype(np.float32)
print(arr8)
print(type(arr8.dtype))


#np.logspace等比数列，包左包右    参1：起始值(10的指数) 参2：结束值（10的指数），参3：元素个数
arr9=np.logspace(0,3,5)
print(arr9)
print(arr9.dtype)
#参1：起始值(2的指数) 参2：结束值（2的指数），参3：元素个数,参4：修改底数为2,参5：修改数据类型为int64
arr10=np.logspace(0,3,4,base=2,dtype=np.int64)
print(arr10)
print(arr10.dtype)
#np.linspace等差数列，包左包右     参1：起始值，参2：结束值，参3：个数，参4：是否包含结束值，参5：修改数据类型为int32
arr11=np.linspace(1,10,4,endpoint=False,dtype=np.int32)
print(arr11)
print(arr11.dtype)


#Numpy的常用函数
#1创建标准正太分布的序列
arr12=np.random.randn(3,5)
print(arr12)
#2.测试基本函数
print(np.ceil(arr12)) #向上取整
print(np.floor(arr12))#向下取整
print(np.rint(arr12))#四舍五入
print(np.abs(arr12))#绝对值
print(np.multiply(arr1,arr1))#矩阵乘法，行列数一样
print(arr1*arr1)#效果同上
print(np.divide(arr12,arr12))#矩阵除法
print(np.where(arr12>0,1,-1))#若大于0，转成1，小于0，转成-1

#Numpy的统计函数
print(np.cumsum(arr1))#累加和
print(np.sum(arr1))#所有元素求和
print(np.sum(arr1,axis=0))#列求和
print(np.sum(arr1,axis=1))#行求和

#Numpy的去重函数
arr13=np.array([[1,2,1],[2,3,5]])#两行三列
print(arr13)
arr14=np.unique(arr13)#去重返回新副本，与arr13不一样，arr13不变
print(arr14)

#Numpy排序函数
arr15=np.array([11,33,22,55,66])
print(arr15)
arr16=np.sort(arr15)#返回新副本
print(arr16)
arr15.sort()#直接修改原数组
print(arr15)


#Numpy的矩阵运算
arr16=np.array([10,20,30,40])
arr17=np.arange(4)
print(arr16)
print(arr17)
print(arr16-arr17)#减法
print(arr16+arr17)#加法
#矩阵乘法
arr18=np.array([[1,2,3],[4,5,6]])
arr19=np.array([[1,2,3],[4,5,6]])
print(arr18)
print(arr19)
print(arr18*arr19)#行列数一致
print(np.multiply(arr18,arr19))#行列数一致

arr20=np.array([[1,2,3],[4,5,6]])
arr21=np.array([[9,8],[6,5],[3,2]])
print(arr20)
print(arr21)
print(np.dot(arr20,arr21))#行列数不一致
print(arr20@arr21)#行列数不一致
print(arr20.dot(arr21))#行列数不一致