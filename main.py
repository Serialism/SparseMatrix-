# -*- coding:utf-8 -*-
# 作者：沈史策
# 创建：2019-11-17
# 稀疏矩阵的乘法运算与存储
class SparseMatrix:
    #定义了一个稀疏矩阵的类
    def _init_(self):
        self.length = None
        self.width = None
        self.ele_loc = None
    #实例化了两个矩阵，分别是SparseMatrixA与SparseMatrixB，都是10*10大小的稀疏矩阵
    #每个矩阵的ele_loc字典代表了矩阵中的非零元素，字典中的key是非零元素的坐标，值是非零元素的具体数值
SparseMatrixA = SparseMatrix()
SparseMatrixA.length = 10
SparseMatrixA.width = 10
SparseMatrixA.ele_loc = {(1,2):3,(1,3):3,(2,4):5}

SparseMatrixB = SparseMatrix()
SparseMatrixB.length = 10
SparseMatrixB.width = 10
SparseMatrixB.ele_loc = {(2,1):4,(3,1):4,(4,2):6,}


print(SparseMatrixA)
print(SparseMatrixA.length)
print(SparseMatrixA.ele_loc)
print(SparseMatrixB)
print(SparseMatrixB.length)
print(SparseMatrixB.ele_loc)

def merge_dict(x,y):#若两个dict1和dict2有相同的key则对应的value相加,用于字典的值合并，在这里用于矩阵乘法之后的加法运算
    for k,v in x.items():
                if k in y.keys():
                    y[k] += v
                else:
                    y[k] = v
    return y
def main(A,B):
    '''
    A,B为相乘的矩阵
    顺序为A*B
    首先通过检验两个矩阵的大小型号来判断两矩阵能否相乘
    '''
    if A.width != B.length:
        print("相乘矩阵规格不符")
    else:
        Multiplier(A,B)

def Multiplier(A,B):
    #矩阵乘法运算的主函数
    result = []#result变量是一个中间变量，用于存储各个元素相乘后的单个结果与该结果所在的位置，之后在通过merge_dict函数将这些结果做加法运算
    #遍历A矩阵每个非零元素的坐标,去和B矩阵的每个非零元素的坐标相比较判断能不能进行乘法,能相乘的计算出结果,并将每个相乘后的结果记录为字典的形式，留待以后相加
    for i in A.ele_loc:
        for j in B.ele_loc:
            if (i[0],i[1])==(j[1],j[0]):
                result.append({(i[0],j[1]):A.ele_loc[i]*B.ele_loc[j]})
    print(result)
    length=len(result)#得到result数组的长度，并将result数组中相同位置的值相加

    a = {}
    for i in range(length):
        a=merge_dict(result[i],a)
    SparseMatrixC = SparseMatrix()
    SparseMatrixC.length = SparseMatrixA.length
    SparseMatrixC.width = SparseMatrixB.width
    SparseMatrixC.ele_loc = a
    print("相乘后的矩阵大小为{}*{}".format(SparseMatrixC.length,SparseMatrixC.width))
    print("相乘后矩阵的非零元素值与位置为{}".format(SparseMatrixC.ele_loc))

if __name__ == '__main__':
    main(SparseMatrixA,SparseMatrixB)









