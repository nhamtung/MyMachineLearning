Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pandas import DataFrame
>>> table1 = DataFrame({
	'id' : [1,2,3],
	'price' : [50000, 100000, 80000],
	'quantity' : [10, 15, 12]
	})
>>> table1
   id   price  quantity
0   1   50000        10
1   2  100000        15
2   3   80000        12
>>> 
