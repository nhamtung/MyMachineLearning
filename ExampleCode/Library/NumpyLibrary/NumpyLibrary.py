Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> X1 = numpy.array([[1,2],[3,4]])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    X1 = numpy.array([[1,2],[3,4]])
NameError: name 'numpy' is not defined
>>> import numpy
>>> X1 = numpy.array([[1,2],[3,4]])
>>> X1
array([[1, 2],
       [3, 4]])
>>> X2 = numpy.array([5,6],[7,8])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X2 = numpy.array([5,6],[7,8])
TypeError: data type not understood
>>> X2 = numpy.array([5,6],[7,8]])
SyntaxError: invalid syntax
>>> X2 = numpy.array([[5,6],[7,8]])
>>> X1 +1
array([[2, 3],
       [4, 5]])
>>> X1 + X2
array([[ 6,  8],
       [10, 12]])
>>> X3 = X1*X1
>>> X4 = numpy.sqrt(X3)
>>> X4
array([[1., 2.],
       [3., 4.]])
>>> numpy.sum(X1)
10
>>> numpy.mean(X1)
2.5
>>> numpy.mean(X2,axis = 0)
array([6., 7.])
>>> numpy.mean(X2, asix=1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    numpy.mean(X2, asix=1)
TypeError: mean() got an unexpected keyword argument 'asix'
>>> 
>>> numpy.mean(X2, axis=1)
array([5.5, 7.5])
>>> indexes = (X1 >= 2)&(X2 %2 == 0)
>>> indexes
array([[False,  True],
       [False,  True]])
>>> X1[indexes]
array([2, 4])
>>> 
