Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> data = [
(0.50, 0),
(0.75, 0),
(1.00, 0),
(1.25, 0),
(1.50, 0),
(1.75, 0),
(1.75, 1),
(2.00, 0),
(2.25, 1),
(2.50, 0),
(2.75, 1),
(3.00, 0),
(3.25, 1),
(3.50, 0),
(4.00, 1),
(4.25, 1),
(4.50, 1),
(4.75, 1),
(5.00, 1),
(5.50, 1)
]
>>> n = len(data)
>>> X = [datai[i][0] for i in range(0,n)]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    X = [datai[i][0] for i in range(0,n)]
  File "<pyshell#3>", line 1, in <listcomp>
    X = [datai[i][0] for i in range(0,n)]
NameError: name 'datai' is not defined
>>> X = [data[i][0] for i in range(0,n)]
>>> Y = [data[i][1] for i in range(0,n)]
>>> epochs = 1000
>>> lr = 0.01
>>> a = 0
>>> b = 0
>>> for step in range(0,epochs):
	da, db = 0,0
	sse = 0
	for i in range(n)
	
SyntaxError: invalid syntax
>>> for step in range(0,epochs):
	da, db = 0,0
	sse = 0
	for i in range(n):
		x = X[i]
		y = Y[i]
		p = 1/(1+math.exp(-(b+a*x)))
		e = p-y
		da += e*p*(1-p)*x
		db += e*p*(1-p)
		sse += e*e
	a += -lr*da
	b += -lr*db
	rmse = math.sqrt(sse/n)
	print("Step %d: rmse=%0.2f, a=%0.2f, b=%0.2f"%(step, rmse, a, b))

Step 0: rmse=0.50, a=0.03, b=0.00
Step 1: rmse=0.49, a=0.05, b=-0.00
Step 2: rmse=0.49, a=0.07, b=-0.00
Step 3: rmse=0.49, a=0.08, b=-0.01
Step 4: rmse=0.48, a=0.10, b=-0.01
Step 5: rmse=0.48, a=0.11, b=-0.01
Step 6: rmse=0.48, a=0.12, b=-0.02
Step 7: rmse=0.48, a=0.13, b=-0.02
Step 8: rmse=0.48, a=0.14, b=-0.02
Step 9: rmse=0.48, a=0.15, b=-0.03
Step 10: rmse=0.48, a=0.15, b=-0.03
Step 11: rmse=0.47, a=0.16, b=-0.04
Step 12: rmse=0.47, a=0.16, b=-0.04
Step 13: rmse=0.47, a=0.17, b=-0.05
Step 14: rmse=0.47, a=0.17, b=-0.06
Step 15: rmse=0.47, a=0.18, b=-0.06
Step 16: rmse=0.47, a=0.18, b=-0.07
Step 17: rmse=0.47, a=0.18, b=-0.07
Step 18: rmse=0.47, a=0.19, b=-0.08
Step 19: rmse=0.47, a=0.19, b=-0.08
Step 20: rmse=0.47, a=0.19, b=-0.09
Step 21: rmse=0.47, a=0.20, b=-0.10
Step 22: rmse=0.47, a=0.20, b=-0.10
Step 23: rmse=0.47, a=0.20, b=-0.11
Step 24: rmse=0.47, a=0.20, b=-0.11
Step 25: rmse=0.47, a=0.21, b=-0.12
Step 26: rmse=0.47, a=0.21, b=-0.13
Step 27: rmse=0.47, a=0.21, b=-0.13
Step 28: rmse=0.47, a=0.21, b=-0.14
Step 29: rmse=0.47, a=0.21, b=-0.14
Step 30: rmse=0.47, a=0.22, b=-0.15
Step 31: rmse=0.47, a=0.22, b=-0.16
Step 32: rmse=0.46, a=0.22, b=-0.16
Step 33: rmse=0.46, a=0.22, b=-0.17
Step 34: rmse=0.46, a=0.22, b=-0.17
Step 35: rmse=0.46, a=0.23, b=-0.18
Step 36: rmse=0.46, a=0.23, b=-0.19
Step 37: rmse=0.46, a=0.23, b=-0.19
Step 38: rmse=0.46, a=0.23, b=-0.20
Step 39: rmse=0.46, a=0.23, b=-0.20
Step 40: rmse=0.46, a=0.23, b=-0.21
Step 41: rmse=0.46, a=0.24, b=-0.21
Step 42: rmse=0.46, a=0.24, b=-0.22
Step 43: rmse=0.46, a=0.24, b=-0.23
Step 44: rmse=0.46, a=0.24, b=-0.23
Step 45: rmse=0.46, a=0.24, b=-0.24
Step 46: rmse=0.46, a=0.24, b=-0.24
Step 47: rmse=0.46, a=0.25, b=-0.25
Step 48: rmse=0.46, a=0.25, b=-0.26
Step 49: rmse=0.46, a=0.25, b=-0.26
Step 50: rmse=0.46, a=0.25, b=-0.27
Step 51: rmse=0.46, a=0.25, b=-0.27
Step 52: rmse=0.46, a=0.25, b=-0.28
Step 53: rmse=0.46, a=0.26, b=-0.28
Step 54: rmse=0.46, a=0.26, b=-0.29
Step 55: rmse=0.46, a=0.26, b=-0.30
Step 56: rmse=0.46, a=0.26, b=-0.30
Step 57: rmse=0.45, a=0.26, b=-0.31
Step 58: rmse=0.45, a=0.26, b=-0.31
Step 59: rmse=0.45, a=0.26, b=-0.32
Step 60: rmse=0.45, a=0.27, b=-0.32
Step 61: rmse=0.45, a=0.27, b=-0.33
Step 62: rmse=0.45, a=0.27, b=-0.33
Step 63: rmse=0.45, a=0.27, b=-0.34
Step 64: rmse=0.45, a=0.27, b=-0.35
Step 65: rmse=0.45, a=0.27, b=-0.35
Step 66: rmse=0.45, a=0.28, b=-0.36
Step 67: rmse=0.45, a=0.28, b=-0.36
Step 68: rmse=0.45, a=0.28, b=-0.37
Step 69: rmse=0.45, a=0.28, b=-0.37
Step 70: rmse=0.45, a=0.28, b=-0.38
Step 71: rmse=0.45, a=0.28, b=-0.38
Step 72: rmse=0.45, a=0.29, b=-0.39
Step 73: rmse=0.45, a=0.29, b=-0.39
Step 74: rmse=0.45, a=0.29, b=-0.40
Step 75: rmse=0.45, a=0.29, b=-0.41
Step 76: rmse=0.45, a=0.29, b=-0.41
Step 77: rmse=0.45, a=0.29, b=-0.42
Step 78: rmse=0.45, a=0.29, b=-0.42
Step 79: rmse=0.45, a=0.30, b=-0.43
Step 80: rmse=0.45, a=0.30, b=-0.43
Step 81: rmse=0.45, a=0.30, b=-0.44
Step 82: rmse=0.45, a=0.30, b=-0.44
Step 83: rmse=0.45, a=0.30, b=-0.45
Step 84: rmse=0.45, a=0.30, b=-0.45
Step 85: rmse=0.44, a=0.31, b=-0.46
Step 86: rmse=0.44, a=0.31, b=-0.46
Step 87: rmse=0.44, a=0.31, b=-0.47
Step 88: rmse=0.44, a=0.31, b=-0.47
Step 89: rmse=0.44, a=0.31, b=-0.48
Step 90: rmse=0.44, a=0.31, b=-0.48
Step 91: rmse=0.44, a=0.31, b=-0.49
Step 92: rmse=0.44, a=0.32, b=-0.49
Step 93: rmse=0.44, a=0.32, b=-0.50
Step 94: rmse=0.44, a=0.32, b=-0.50
Step 95: rmse=0.44, a=0.32, b=-0.51
Step 96: rmse=0.44, a=0.32, b=-0.52
Step 97: rmse=0.44, a=0.32, b=-0.52
Step 98: rmse=0.44, a=0.32, b=-0.53
Step 99: rmse=0.44, a=0.33, b=-0.53
Step 100: rmse=0.44, a=0.33, b=-0.54
Step 101: rmse=0.44, a=0.33, b=-0.54
Step 102: rmse=0.44, a=0.33, b=-0.55
Step 103: rmse=0.44, a=0.33, b=-0.55
Step 104: rmse=0.44, a=0.33, b=-0.56
Step 105: rmse=0.44, a=0.33, b=-0.56
Step 106: rmse=0.44, a=0.34, b=-0.57
Step 107: rmse=0.44, a=0.34, b=-0.57
Step 108: rmse=0.44, a=0.34, b=-0.58
Step 109: rmse=0.44, a=0.34, b=-0.58
Step 110: rmse=0.44, a=0.34, b=-0.58
Step 111: rmse=0.44, a=0.34, b=-0.59
Step 112: rmse=0.44, a=0.34, b=-0.59
Step 113: rmse=0.44, a=0.35, b=-0.60
Step 114: rmse=0.44, a=0.35, b=-0.60
Step 115: rmse=0.44, a=0.35, b=-0.61
Step 116: rmse=0.44, a=0.35, b=-0.61
Step 117: rmse=0.43, a=0.35, b=-0.62
Step 118: rmse=0.43, a=0.35, b=-0.62
Step 119: rmse=0.43, a=0.35, b=-0.63
Step 120: rmse=0.43, a=0.36, b=-0.63
Step 121: rmse=0.43, a=0.36, b=-0.64
Step 122: rmse=0.43, a=0.36, b=-0.64
Step 123: rmse=0.43, a=0.36, b=-0.65
Step 124: rmse=0.43, a=0.36, b=-0.65
Step 125: rmse=0.43, a=0.36, b=-0.66
Step 126: rmse=0.43, a=0.36, b=-0.66
Step 127: rmse=0.43, a=0.37, b=-0.67
Step 128: rmse=0.43, a=0.37, b=-0.67
Step 129: rmse=0.43, a=0.37, b=-0.68
Step 130: rmse=0.43, a=0.37, b=-0.68
Step 131: rmse=0.43, a=0.37, b=-0.68
Step 132: rmse=0.43, a=0.37, b=-0.69
Step 133: rmse=0.43, a=0.37, b=-0.69
Step 134: rmse=0.43, a=0.37, b=-0.70
Step 135: rmse=0.43, a=0.38, b=-0.70
Step 136: rmse=0.43, a=0.38, b=-0.71
Step 137: rmse=0.43, a=0.38, b=-0.71
Step 138: rmse=0.43, a=0.38, b=-0.72
Step 139: rmse=0.43, a=0.38, b=-0.72
Step 140: rmse=0.43, a=0.38, b=-0.73
Step 141: rmse=0.43, a=0.38, b=-0.73
Step 142: rmse=0.43, a=0.39, b=-0.73
Step 143: rmse=0.43, a=0.39, b=-0.74
Step 144: rmse=0.43, a=0.39, b=-0.74
Step 145: rmse=0.43, a=0.39, b=-0.75
Step 146: rmse=0.43, a=0.39, b=-0.75
Step 147: rmse=0.43, a=0.39, b=-0.76
Step 148: rmse=0.43, a=0.39, b=-0.76
Step 149: rmse=0.43, a=0.39, b=-0.77
Step 150: rmse=0.43, a=0.40, b=-0.77
Step 151: rmse=0.43, a=0.40, b=-0.77
Step 152: rmse=0.43, a=0.40, b=-0.78
Step 153: rmse=0.43, a=0.40, b=-0.78
Step 154: rmse=0.43, a=0.40, b=-0.79
Step 155: rmse=0.42, a=0.40, b=-0.79
Step 156: rmse=0.42, a=0.40, b=-0.80
Step 157: rmse=0.42, a=0.40, b=-0.80
Step 158: rmse=0.42, a=0.41, b=-0.80
Step 159: rmse=0.42, a=0.41, b=-0.81
Step 160: rmse=0.42, a=0.41, b=-0.81
Step 161: rmse=0.42, a=0.41, b=-0.82
Step 162: rmse=0.42, a=0.41, b=-0.82
Step 163: rmse=0.42, a=0.41, b=-0.83
Step 164: rmse=0.42, a=0.41, b=-0.83
Step 165: rmse=0.42, a=0.41, b=-0.83
Step 166: rmse=0.42, a=0.42, b=-0.84
Step 167: rmse=0.42, a=0.42, b=-0.84
Step 168: rmse=0.42, a=0.42, b=-0.85
Step 169: rmse=0.42, a=0.42, b=-0.85
Step 170: rmse=0.42, a=0.42, b=-0.85
Step 171: rmse=0.42, a=0.42, b=-0.86
Step 172: rmse=0.42, a=0.42, b=-0.86
Step 173: rmse=0.42, a=0.42, b=-0.87
Step 174: rmse=0.42, a=0.43, b=-0.87
Step 175: rmse=0.42, a=0.43, b=-0.88
Step 176: rmse=0.42, a=0.43, b=-0.88
Step 177: rmse=0.42, a=0.43, b=-0.88
Step 178: rmse=0.42, a=0.43, b=-0.89
Step 179: rmse=0.42, a=0.43, b=-0.89
Step 180: rmse=0.42, a=0.43, b=-0.90
Step 181: rmse=0.42, a=0.43, b=-0.90
Step 182: rmse=0.42, a=0.44, b=-0.90
Step 183: rmse=0.42, a=0.44, b=-0.91
Step 184: rmse=0.42, a=0.44, b=-0.91
Step 185: rmse=0.42, a=0.44, b=-0.92
Step 186: rmse=0.42, a=0.44, b=-0.92
Step 187: rmse=0.42, a=0.44, b=-0.92
Step 188: rmse=0.42, a=0.44, b=-0.93
Step 189: rmse=0.42, a=0.44, b=-0.93
Step 190: rmse=0.42, a=0.45, b=-0.94
Step 191: rmse=0.42, a=0.45, b=-0.94
Step 192: rmse=0.42, a=0.45, b=-0.94
Step 193: rmse=0.42, a=0.45, b=-0.95
Step 194: rmse=0.42, a=0.45, b=-0.95
Step 195: rmse=0.42, a=0.45, b=-0.95
Step 196: rmse=0.42, a=0.45, b=-0.96
Step 197: rmse=0.42, a=0.45, b=-0.96
Step 198: rmse=0.42, a=0.45, b=-0.97
Step 199: rmse=0.42, a=0.46, b=-0.97
Step 200: rmse=0.42, a=0.46, b=-0.97
Step 201: rmse=0.41, a=0.46, b=-0.98
Step 202: rmse=0.41, a=0.46, b=-0.98
Step 203: rmse=0.41, a=0.46, b=-0.99
Step 204: rmse=0.41, a=0.46, b=-0.99
Step 205: rmse=0.41, a=0.46, b=-0.99
Step 206: rmse=0.41, a=0.46, b=-1.00
Step 207: rmse=0.41, a=0.46, b=-1.00
Step 208: rmse=0.41, a=0.47, b=-1.00
Step 209: rmse=0.41, a=0.47, b=-1.01
Step 210: rmse=0.41, a=0.47, b=-1.01
Step 211: rmse=0.41, a=0.47, b=-1.02
Step 212: rmse=0.41, a=0.47, b=-1.02
Step 213: rmse=0.41, a=0.47, b=-1.02
Step 214: rmse=0.41, a=0.47, b=-1.03
Step 215: rmse=0.41, a=0.47, b=-1.03
Step 216: rmse=0.41, a=0.47, b=-1.03
Step 217: rmse=0.41, a=0.48, b=-1.04
Step 218: rmse=0.41, a=0.48, b=-1.04
Step 219: rmse=0.41, a=0.48, b=-1.04
Step 220: rmse=0.41, a=0.48, b=-1.05
Step 221: rmse=0.41, a=0.48, b=-1.05
Step 222: rmse=0.41, a=0.48, b=-1.06
Step 223: rmse=0.41, a=0.48, b=-1.06
Step 224: rmse=0.41, a=0.48, b=-1.06
Step 225: rmse=0.41, a=0.48, b=-1.07
Step 226: rmse=0.41, a=0.49, b=-1.07
Step 227: rmse=0.41, a=0.49, b=-1.07
Step 228: rmse=0.41, a=0.49, b=-1.08
Step 229: rmse=0.41, a=0.49, b=-1.08
Step 230: rmse=0.41, a=0.49, b=-1.08
Step 231: rmse=0.41, a=0.49, b=-1.09
Step 232: rmse=0.41, a=0.49, b=-1.09
Step 233: rmse=0.41, a=0.49, b=-1.09
Step 234: rmse=0.41, a=0.49, b=-1.10
Step 235: rmse=0.41, a=0.50, b=-1.10
Step 236: rmse=0.41, a=0.50, b=-1.10
Step 237: rmse=0.41, a=0.50, b=-1.11
Step 238: rmse=0.41, a=0.50, b=-1.11
Step 239: rmse=0.41, a=0.50, b=-1.11
Step 240: rmse=0.41, a=0.50, b=-1.12
Step 241: rmse=0.41, a=0.50, b=-1.12
Step 242: rmse=0.41, a=0.50, b=-1.13
Step 243: rmse=0.41, a=0.50, b=-1.13
Step 244: rmse=0.41, a=0.50, b=-1.13
Step 245: rmse=0.41, a=0.51, b=-1.14
Step 246: rmse=0.41, a=0.51, b=-1.14
Step 247: rmse=0.41, a=0.51, b=-1.14
Step 248: rmse=0.41, a=0.51, b=-1.15
Step 249: rmse=0.41, a=0.51, b=-1.15
Step 250: rmse=0.41, a=0.51, b=-1.15
Step 251: rmse=0.41, a=0.51, b=-1.16
Step 252: rmse=0.41, a=0.51, b=-1.16
Step 253: rmse=0.41, a=0.51, b=-1.16
Step 254: rmse=0.41, a=0.52, b=-1.17
Step 255: rmse=0.41, a=0.52, b=-1.17
Step 256: rmse=0.41, a=0.52, b=-1.17
Step 257: rmse=0.41, a=0.52, b=-1.18
Step 258: rmse=0.41, a=0.52, b=-1.18
Step 259: rmse=0.41, a=0.52, b=-1.18
Step 260: rmse=0.41, a=0.52, b=-1.19
Step 261: rmse=0.41, a=0.52, b=-1.19
Step 262: rmse=0.40, a=0.52, b=-1.19
Step 263: rmse=0.40, a=0.52, b=-1.19
Step 264: rmse=0.40, a=0.53, b=-1.20
Step 265: rmse=0.40, a=0.53, b=-1.20
Step 266: rmse=0.40, a=0.53, b=-1.20
Step 267: rmse=0.40, a=0.53, b=-1.21
Step 268: rmse=0.40, a=0.53, b=-1.21
Step 269: rmse=0.40, a=0.53, b=-1.21
Step 270: rmse=0.40, a=0.53, b=-1.22
Step 271: rmse=0.40, a=0.53, b=-1.22
Step 272: rmse=0.40, a=0.53, b=-1.22
Step 273: rmse=0.40, a=0.53, b=-1.23
Step 274: rmse=0.40, a=0.53, b=-1.23
Step 275: rmse=0.40, a=0.54, b=-1.23
Step 276: rmse=0.40, a=0.54, b=-1.24
Step 277: rmse=0.40, a=0.54, b=-1.24
Step 278: rmse=0.40, a=0.54, b=-1.24
Step 279: rmse=0.40, a=0.54, b=-1.25
Step 280: rmse=0.40, a=0.54, b=-1.25
Step 281: rmse=0.40, a=0.54, b=-1.25
Step 282: rmse=0.40, a=0.54, b=-1.25
Step 283: rmse=0.40, a=0.54, b=-1.26
Step 284: rmse=0.40, a=0.54, b=-1.26
Step 285: rmse=0.40, a=0.55, b=-1.26
Step 286: rmse=0.40, a=0.55, b=-1.27
Step 287: rmse=0.40, a=0.55, b=-1.27
Step 288: rmse=0.40, a=0.55, b=-1.27
Step 289: rmse=0.40, a=0.55, b=-1.28
Step 290: rmse=0.40, a=0.55, b=-1.28
Step 291: rmse=0.40, a=0.55, b=-1.28
Step 292: rmse=0.40, a=0.55, b=-1.28
Step 293: rmse=0.40, a=0.55, b=-1.29
Step 294: rmse=0.40, a=0.55, b=-1.29
Step 295: rmse=0.40, a=0.55, b=-1.29
Step 296: rmse=0.40, a=0.56, b=-1.30
Step 297: rmse=0.40, a=0.56, b=-1.30
Step 298: rmse=0.40, a=0.56, b=-1.30
Step 299: rmse=0.40, a=0.56, b=-1.31
Step 300: rmse=0.40, a=0.56, b=-1.31
Step 301: rmse=0.40, a=0.56, b=-1.31
Step 302: rmse=0.40, a=0.56, b=-1.31
Step 303: rmse=0.40, a=0.56, b=-1.32
Step 304: rmse=0.40, a=0.56, b=-1.32
Step 305: rmse=0.40, a=0.56, b=-1.32
Step 306: rmse=0.40, a=0.56, b=-1.33
Step 307: rmse=0.40, a=0.57, b=-1.33
Step 308: rmse=0.40, a=0.57, b=-1.33
Step 309: rmse=0.40, a=0.57, b=-1.33
Step 310: rmse=0.40, a=0.57, b=-1.34
Step 311: rmse=0.40, a=0.57, b=-1.34
Step 312: rmse=0.40, a=0.57, b=-1.34
Step 313: rmse=0.40, a=0.57, b=-1.35
Step 314: rmse=0.40, a=0.57, b=-1.35
Step 315: rmse=0.40, a=0.57, b=-1.35
Step 316: rmse=0.40, a=0.57, b=-1.35
Step 317: rmse=0.40, a=0.57, b=-1.36
Step 318: rmse=0.40, a=0.58, b=-1.36
Step 319: rmse=0.40, a=0.58, b=-1.36
Step 320: rmse=0.40, a=0.58, b=-1.37
Step 321: rmse=0.40, a=0.58, b=-1.37
Step 322: rmse=0.40, a=0.58, b=-1.37
Step 323: rmse=0.40, a=0.58, b=-1.37
Step 324: rmse=0.40, a=0.58, b=-1.38
Step 325: rmse=0.40, a=0.58, b=-1.38
Step 326: rmse=0.40, a=0.58, b=-1.38
Step 327: rmse=0.40, a=0.58, b=-1.39
Step 328: rmse=0.40, a=0.58, b=-1.39
Step 329: rmse=0.40, a=0.58, b=-1.39
Step 330: rmse=0.40, a=0.59, b=-1.39
Step 331: rmse=0.40, a=0.59, b=-1.40
Step 332: rmse=0.40, a=0.59, b=-1.40
Step 333: rmse=0.40, a=0.59, b=-1.40
Step 334: rmse=0.40, a=0.59, b=-1.40
Step 335: rmse=0.40, a=0.59, b=-1.41
Step 336: rmse=0.40, a=0.59, b=-1.41
Step 337: rmse=0.40, a=0.59, b=-1.41
Step 338: rmse=0.40, a=0.59, b=-1.42
Step 339: rmse=0.40, a=0.59, b=-1.42
Step 340: rmse=0.40, a=0.59, b=-1.42
Step 341: rmse=0.40, a=0.59, b=-1.42
Step 342: rmse=0.40, a=0.60, b=-1.43
Step 343: rmse=0.40, a=0.60, b=-1.43
Step 344: rmse=0.40, a=0.60, b=-1.43
Step 345: rmse=0.40, a=0.60, b=-1.43
Step 346: rmse=0.40, a=0.60, b=-1.44
Step 347: rmse=0.39, a=0.60, b=-1.44
Step 348: rmse=0.39, a=0.60, b=-1.44
Step 349: rmse=0.39, a=0.60, b=-1.44
Step 350: rmse=0.39, a=0.60, b=-1.45
Step 351: rmse=0.39, a=0.60, b=-1.45
Step 352: rmse=0.39, a=0.60, b=-1.45
Step 353: rmse=0.39, a=0.60, b=-1.45
Step 354: rmse=0.39, a=0.61, b=-1.46
Step 355: rmse=0.39, a=0.61, b=-1.46
Step 356: rmse=0.39, a=0.61, b=-1.46
Step 357: rmse=0.39, a=0.61, b=-1.47
Step 358: rmse=0.39, a=0.61, b=-1.47
Step 359: rmse=0.39, a=0.61, b=-1.47
Step 360: rmse=0.39, a=0.61, b=-1.47
Step 361: rmse=0.39, a=0.61, b=-1.48
Step 362: rmse=0.39, a=0.61, b=-1.48
Step 363: rmse=0.39, a=0.61, b=-1.48
Step 364: rmse=0.39, a=0.61, b=-1.48
Step 365: rmse=0.39, a=0.61, b=-1.49
Step 366: rmse=0.39, a=0.61, b=-1.49
Step 367: rmse=0.39, a=0.62, b=-1.49
Step 368: rmse=0.39, a=0.62, b=-1.49
Step 369: rmse=0.39, a=0.62, b=-1.50
Step 370: rmse=0.39, a=0.62, b=-1.50
Step 371: rmse=0.39, a=0.62, b=-1.50
Step 372: rmse=0.39, a=0.62, b=-1.50
Step 373: rmse=0.39, a=0.62, b=-1.51
Step 374: rmse=0.39, a=0.62, b=-1.51
Step 375: rmse=0.39, a=0.62, b=-1.51
Step 376: rmse=0.39, a=0.62, b=-1.51
Step 377: rmse=0.39, a=0.62, b=-1.52
Step 378: rmse=0.39, a=0.62, b=-1.52
Step 379: rmse=0.39, a=0.62, b=-1.52
Step 380: rmse=0.39, a=0.63, b=-1.52
Step 381: rmse=0.39, a=0.63, b=-1.53
Step 382: rmse=0.39, a=0.63, b=-1.53
Step 383: rmse=0.39, a=0.63, b=-1.53
Step 384: rmse=0.39, a=0.63, b=-1.53
Step 385: rmse=0.39, a=0.63, b=-1.53
Step 386: rmse=0.39, a=0.63, b=-1.54
Step 387: rmse=0.39, a=0.63, b=-1.54
Step 388: rmse=0.39, a=0.63, b=-1.54
Step 389: rmse=0.39, a=0.63, b=-1.54
Step 390: rmse=0.39, a=0.63, b=-1.55
Step 391: rmse=0.39, a=0.63, b=-1.55
Step 392: rmse=0.39, a=0.63, b=-1.55
Step 393: rmse=0.39, a=0.64, b=-1.55
Step 394: rmse=0.39, a=0.64, b=-1.56
Step 395: rmse=0.39, a=0.64, b=-1.56
Step 396: rmse=0.39, a=0.64, b=-1.56
Step 397: rmse=0.39, a=0.64, b=-1.56
Step 398: rmse=0.39, a=0.64, b=-1.57
Step 399: rmse=0.39, a=0.64, b=-1.57
Step 400: rmse=0.39, a=0.64, b=-1.57
Step 401: rmse=0.39, a=0.64, b=-1.57
Step 402: rmse=0.39, a=0.64, b=-1.58
Step 403: rmse=0.39, a=0.64, b=-1.58
Step 404: rmse=0.39, a=0.64, b=-1.58
Step 405: rmse=0.39, a=0.64, b=-1.58
Step 406: rmse=0.39, a=0.64, b=-1.58
Step 407: rmse=0.39, a=0.65, b=-1.59
Step 408: rmse=0.39, a=0.65, b=-1.59
Step 409: rmse=0.39, a=0.65, b=-1.59
Step 410: rmse=0.39, a=0.65, b=-1.59
Step 411: rmse=0.39, a=0.65, b=-1.60
Step 412: rmse=0.39, a=0.65, b=-1.60
Step 413: rmse=0.39, a=0.65, b=-1.60
Step 414: rmse=0.39, a=0.65, b=-1.60
Step 415: rmse=0.39, a=0.65, b=-1.60
Step 416: rmse=0.39, a=0.65, b=-1.61
Step 417: rmse=0.39, a=0.65, b=-1.61
Step 418: rmse=0.39, a=0.65, b=-1.61
Step 419: rmse=0.39, a=0.65, b=-1.61
Step 420: rmse=0.39, a=0.65, b=-1.62
Step 421: rmse=0.39, a=0.66, b=-1.62
Step 422: rmse=0.39, a=0.66, b=-1.62
Step 423: rmse=0.39, a=0.66, b=-1.62
Step 424: rmse=0.39, a=0.66, b=-1.62
Step 425: rmse=0.39, a=0.66, b=-1.63
Step 426: rmse=0.39, a=0.66, b=-1.63
Step 427: rmse=0.39, a=0.66, b=-1.63
Step 428: rmse=0.39, a=0.66, b=-1.63
Step 429: rmse=0.39, a=0.66, b=-1.64
Step 430: rmse=0.39, a=0.66, b=-1.64
Step 431: rmse=0.39, a=0.66, b=-1.64
Step 432: rmse=0.39, a=0.66, b=-1.64
Step 433: rmse=0.39, a=0.66, b=-1.64
Step 434: rmse=0.39, a=0.66, b=-1.65
Step 435: rmse=0.39, a=0.67, b=-1.65
Step 436: rmse=0.39, a=0.67, b=-1.65
Step 437: rmse=0.39, a=0.67, b=-1.65
Step 438: rmse=0.39, a=0.67, b=-1.66
Step 439: rmse=0.39, a=0.67, b=-1.66
Step 440: rmse=0.39, a=0.67, b=-1.66
Step 441: rmse=0.39, a=0.67, b=-1.66
Step 442: rmse=0.39, a=0.67, b=-1.66
Step 443: rmse=0.39, a=0.67, b=-1.67
Step 444: rmse=0.39, a=0.67, b=-1.67
Step 445: rmse=0.39, a=0.67, b=-1.67
Step 446: rmse=0.39, a=0.67, b=-1.67
Step 447: rmse=0.39, a=0.67, b=-1.67
Step 448: rmse=0.39, a=0.67, b=-1.68
Step 449: rmse=0.39, a=0.67, b=-1.68
Step 450: rmse=0.39, a=0.68, b=-1.68
Step 451: rmse=0.39, a=0.68, b=-1.68
Step 452: rmse=0.39, a=0.68, b=-1.68
Step 453: rmse=0.39, a=0.68, b=-1.69
Step 454: rmse=0.39, a=0.68, b=-1.69
Step 455: rmse=0.39, a=0.68, b=-1.69
Step 456: rmse=0.39, a=0.68, b=-1.69
Step 457: rmse=0.39, a=0.68, b=-1.70
Step 458: rmse=0.39, a=0.68, b=-1.70
Step 459: rmse=0.39, a=0.68, b=-1.70
Step 460: rmse=0.39, a=0.68, b=-1.70
Step 461: rmse=0.39, a=0.68, b=-1.70
Step 462: rmse=0.39, a=0.68, b=-1.71
Step 463: rmse=0.39, a=0.68, b=-1.71
Step 464: rmse=0.39, a=0.68, b=-1.71
Step 465: rmse=0.39, a=0.69, b=-1.71
Step 466: rmse=0.39, a=0.69, b=-1.71
Step 467: rmse=0.39, a=0.69, b=-1.72
Step 468: rmse=0.39, a=0.69, b=-1.72
Step 469: rmse=0.39, a=0.69, b=-1.72
Step 470: rmse=0.39, a=0.69, b=-1.72
Step 471: rmse=0.39, a=0.69, b=-1.72
Step 472: rmse=0.39, a=0.69, b=-1.73
Step 473: rmse=0.39, a=0.69, b=-1.73
Step 474: rmse=0.39, a=0.69, b=-1.73
Step 475: rmse=0.39, a=0.69, b=-1.73
Step 476: rmse=0.39, a=0.69, b=-1.73
Step 477: rmse=0.39, a=0.69, b=-1.74
Step 478: rmse=0.39, a=0.69, b=-1.74
Step 479: rmse=0.39, a=0.69, b=-1.74
Step 480: rmse=0.39, a=0.69, b=-1.74
Step 481: rmse=0.39, a=0.70, b=-1.74
Step 482: rmse=0.39, a=0.70, b=-1.75
Step 483: rmse=0.38, a=0.70, b=-1.75
Step 484: rmse=0.38, a=0.70, b=-1.75
Step 485: rmse=0.38, a=0.70, b=-1.75
Step 486: rmse=0.38, a=0.70, b=-1.75
Step 487: rmse=0.38, a=0.70, b=-1.76
Step 488: rmse=0.38, a=0.70, b=-1.76
Step 489: rmse=0.38, a=0.70, b=-1.76
Step 490: rmse=0.38, a=0.70, b=-1.76
Step 491: rmse=0.38, a=0.70, b=-1.76
Step 492: rmse=0.38, a=0.70, b=-1.76
Step 493: rmse=0.38, a=0.70, b=-1.77
Step 494: rmse=0.38, a=0.70, b=-1.77
Step 495: rmse=0.38, a=0.70, b=-1.77
Step 496: rmse=0.38, a=0.70, b=-1.77
Step 497: rmse=0.38, a=0.70, b=-1.77
Step 498: rmse=0.38, a=0.71, b=-1.78
Step 499: rmse=0.38, a=0.71, b=-1.78
Step 500: rmse=0.38, a=0.71, b=-1.78
Step 501: rmse=0.38, a=0.71, b=-1.78
Step 502: rmse=0.38, a=0.71, b=-1.78
Step 503: rmse=0.38, a=0.71, b=-1.79
Step 504: rmse=0.38, a=0.71, b=-1.79
Step 505: rmse=0.38, a=0.71, b=-1.79
Step 506: rmse=0.38, a=0.71, b=-1.79
Step 507: rmse=0.38, a=0.71, b=-1.79
Step 508: rmse=0.38, a=0.71, b=-1.80
Step 509: rmse=0.38, a=0.71, b=-1.80
Step 510: rmse=0.38, a=0.71, b=-1.80
Step 511: rmse=0.38, a=0.71, b=-1.80
Step 512: rmse=0.38, a=0.71, b=-1.80
Step 513: rmse=0.38, a=0.71, b=-1.80
Step 514: rmse=0.38, a=0.72, b=-1.81
Step 515: rmse=0.38, a=0.72, b=-1.81
Step 516: rmse=0.38, a=0.72, b=-1.81
Step 517: rmse=0.38, a=0.72, b=-1.81
Step 518: rmse=0.38, a=0.72, b=-1.81
Step 519: rmse=0.38, a=0.72, b=-1.82
Step 520: rmse=0.38, a=0.72, b=-1.82
Step 521: rmse=0.38, a=0.72, b=-1.82
Step 522: rmse=0.38, a=0.72, b=-1.82
Step 523: rmse=0.38, a=0.72, b=-1.82
Step 524: rmse=0.38, a=0.72, b=-1.82
Step 525: rmse=0.38, a=0.72, b=-1.83
Step 526: rmse=0.38, a=0.72, b=-1.83
Step 527: rmse=0.38, a=0.72, b=-1.83
Step 528: rmse=0.38, a=0.72, b=-1.83
Step 529: rmse=0.38, a=0.72, b=-1.83
Step 530: rmse=0.38, a=0.72, b=-1.84
Step 531: rmse=0.38, a=0.72, b=-1.84
Step 532: rmse=0.38, a=0.73, b=-1.84
Step 533: rmse=0.38, a=0.73, b=-1.84
Step 534: rmse=0.38, a=0.73, b=-1.84
Step 535: rmse=0.38, a=0.73, b=-1.84
Step 536: rmse=0.38, a=0.73, b=-1.85
Step 537: rmse=0.38, a=0.73, b=-1.85
Step 538: rmse=0.38, a=0.73, b=-1.85
Step 539: rmse=0.38, a=0.73, b=-1.85
Step 540: rmse=0.38, a=0.73, b=-1.85
Step 541: rmse=0.38, a=0.73, b=-1.85
Step 542: rmse=0.38, a=0.73, b=-1.86
Step 543: rmse=0.38, a=0.73, b=-1.86
Step 544: rmse=0.38, a=0.73, b=-1.86
Step 545: rmse=0.38, a=0.73, b=-1.86
Step 546: rmse=0.38, a=0.73, b=-1.86
Step 547: rmse=0.38, a=0.73, b=-1.86
Step 548: rmse=0.38, a=0.73, b=-1.87
Step 549: rmse=0.38, a=0.73, b=-1.87
Step 550: rmse=0.38, a=0.74, b=-1.87
Step 551: rmse=0.38, a=0.74, b=-1.87
Step 552: rmse=0.38, a=0.74, b=-1.87
Step 553: rmse=0.38, a=0.74, b=-1.88
Step 554: rmse=0.38, a=0.74, b=-1.88
Step 555: rmse=0.38, a=0.74, b=-1.88
Step 556: rmse=0.38, a=0.74, b=-1.88
Step 557: rmse=0.38, a=0.74, b=-1.88
Step 558: rmse=0.38, a=0.74, b=-1.88
Step 559: rmse=0.38, a=0.74, b=-1.89
Step 560: rmse=0.38, a=0.74, b=-1.89
Step 561: rmse=0.38, a=0.74, b=-1.89
Step 562: rmse=0.38, a=0.74, b=-1.89
Step 563: rmse=0.38, a=0.74, b=-1.89
Step 564: rmse=0.38, a=0.74, b=-1.89
Step 565: rmse=0.38, a=0.74, b=-1.90
Step 566: rmse=0.38, a=0.74, b=-1.90
Step 567: rmse=0.38, a=0.74, b=-1.90
Step 568: rmse=0.38, a=0.74, b=-1.90
Step 569: rmse=0.38, a=0.75, b=-1.90
Step 570: rmse=0.38, a=0.75, b=-1.90
Step 571: rmse=0.38, a=0.75, b=-1.91
Step 572: rmse=0.38, a=0.75, b=-1.91
Step 573: rmse=0.38, a=0.75, b=-1.91
Step 574: rmse=0.38, a=0.75, b=-1.91
Step 575: rmse=0.38, a=0.75, b=-1.91
Step 576: rmse=0.38, a=0.75, b=-1.91
Step 577: rmse=0.38, a=0.75, b=-1.92
Step 578: rmse=0.38, a=0.75, b=-1.92
Step 579: rmse=0.38, a=0.75, b=-1.92
Step 580: rmse=0.38, a=0.75, b=-1.92
Step 581: rmse=0.38, a=0.75, b=-1.92
Step 582: rmse=0.38, a=0.75, b=-1.92
Step 583: rmse=0.38, a=0.75, b=-1.92
Step 584: rmse=0.38, a=0.75, b=-1.93
Step 585: rmse=0.38, a=0.75, b=-1.93
Step 586: rmse=0.38, a=0.75, b=-1.93
Step 587: rmse=0.38, a=0.75, b=-1.93
Step 588: rmse=0.38, a=0.76, b=-1.93
Step 589: rmse=0.38, a=0.76, b=-1.93
Step 590: rmse=0.38, a=0.76, b=-1.94
Step 591: rmse=0.38, a=0.76, b=-1.94
Step 592: rmse=0.38, a=0.76, b=-1.94
Step 593: rmse=0.38, a=0.76, b=-1.94
Step 594: rmse=0.38, a=0.76, b=-1.94
Step 595: rmse=0.38, a=0.76, b=-1.94
Step 596: rmse=0.38, a=0.76, b=-1.95
Step 597: rmse=0.38, a=0.76, b=-1.95
Step 598: rmse=0.38, a=0.76, b=-1.95
Step 599: rmse=0.38, a=0.76, b=-1.95
Step 600: rmse=0.38, a=0.76, b=-1.95
Step 601: rmse=0.38, a=0.76, b=-1.95
Step 602: rmse=0.38, a=0.76, b=-1.96
Step 603: rmse=0.38, a=0.76, b=-1.96
Step 604: rmse=0.38, a=0.76, b=-1.96
Step 605: rmse=0.38, a=0.76, b=-1.96
Step 606: rmse=0.38, a=0.76, b=-1.96
Step 607: rmse=0.38, a=0.76, b=-1.96
Step 608: rmse=0.38, a=0.77, b=-1.96
Step 609: rmse=0.38, a=0.77, b=-1.97
Step 610: rmse=0.38, a=0.77, b=-1.97
Step 611: rmse=0.38, a=0.77, b=-1.97
Step 612: rmse=0.38, a=0.77, b=-1.97
Step 613: rmse=0.38, a=0.77, b=-1.97
Step 614: rmse=0.38, a=0.77, b=-1.97
Step 615: rmse=0.38, a=0.77, b=-1.98
Step 616: rmse=0.38, a=0.77, b=-1.98
Step 617: rmse=0.38, a=0.77, b=-1.98
Step 618: rmse=0.38, a=0.77, b=-1.98
Step 619: rmse=0.38, a=0.77, b=-1.98
Step 620: rmse=0.38, a=0.77, b=-1.98
Step 621: rmse=0.38, a=0.77, b=-1.98
Step 622: rmse=0.38, a=0.77, b=-1.99
Step 623: rmse=0.38, a=0.77, b=-1.99
Step 624: rmse=0.38, a=0.77, b=-1.99
Step 625: rmse=0.38, a=0.77, b=-1.99
Step 626: rmse=0.38, a=0.77, b=-1.99
Step 627: rmse=0.38, a=0.77, b=-1.99
Step 628: rmse=0.38, a=0.78, b=-1.99
Step 629: rmse=0.38, a=0.78, b=-2.00
Step 630: rmse=0.38, a=0.78, b=-2.00
Step 631: rmse=0.38, a=0.78, b=-2.00
Step 632: rmse=0.38, a=0.78, b=-2.00
Step 633: rmse=0.38, a=0.78, b=-2.00
Step 634: rmse=0.38, a=0.78, b=-2.00
Step 635: rmse=0.38, a=0.78, b=-2.01
Step 636: rmse=0.38, a=0.78, b=-2.01
Step 637: rmse=0.38, a=0.78, b=-2.01
Step 638: rmse=0.38, a=0.78, b=-2.01
Step 639: rmse=0.38, a=0.78, b=-2.01
Step 640: rmse=0.38, a=0.78, b=-2.01
Step 641: rmse=0.38, a=0.78, b=-2.01
Step 642: rmse=0.38, a=0.78, b=-2.02
Step 643: rmse=0.38, a=0.78, b=-2.02
Step 644: rmse=0.38, a=0.78, b=-2.02
Step 645: rmse=0.38, a=0.78, b=-2.02
Step 646: rmse=0.38, a=0.78, b=-2.02
Step 647: rmse=0.38, a=0.78, b=-2.02
Step 648: rmse=0.38, a=0.78, b=-2.02
Step 649: rmse=0.38, a=0.78, b=-2.03
Step 650: rmse=0.38, a=0.79, b=-2.03
Step 651: rmse=0.38, a=0.79, b=-2.03
Step 652: rmse=0.38, a=0.79, b=-2.03
Step 653: rmse=0.38, a=0.79, b=-2.03
Step 654: rmse=0.38, a=0.79, b=-2.03
Step 655: rmse=0.38, a=0.79, b=-2.03
Step 656: rmse=0.38, a=0.79, b=-2.04
Step 657: rmse=0.38, a=0.79, b=-2.04
Step 658: rmse=0.38, a=0.79, b=-2.04
Step 659: rmse=0.38, a=0.79, b=-2.04
Step 660: rmse=0.38, a=0.79, b=-2.04
Step 661: rmse=0.38, a=0.79, b=-2.04
Step 662: rmse=0.38, a=0.79, b=-2.04
Step 663: rmse=0.38, a=0.79, b=-2.05
Step 664: rmse=0.38, a=0.79, b=-2.05
Step 665: rmse=0.38, a=0.79, b=-2.05
Step 666: rmse=0.38, a=0.79, b=-2.05
Step 667: rmse=0.38, a=0.79, b=-2.05
Step 668: rmse=0.38, a=0.79, b=-2.05
Step 669: rmse=0.38, a=0.79, b=-2.05
Step 670: rmse=0.38, a=0.79, b=-2.06
Step 671: rmse=0.38, a=0.79, b=-2.06
Step 672: rmse=0.38, a=0.80, b=-2.06
Step 673: rmse=0.38, a=0.80, b=-2.06
Step 674: rmse=0.38, a=0.80, b=-2.06
Step 675: rmse=0.38, a=0.80, b=-2.06
Step 676: rmse=0.38, a=0.80, b=-2.06
Step 677: rmse=0.38, a=0.80, b=-2.06
Step 678: rmse=0.38, a=0.80, b=-2.07
Step 679: rmse=0.38, a=0.80, b=-2.07
Step 680: rmse=0.38, a=0.80, b=-2.07
Step 681: rmse=0.38, a=0.80, b=-2.07
Step 682: rmse=0.38, a=0.80, b=-2.07
Step 683: rmse=0.38, a=0.80, b=-2.07
Step 684: rmse=0.38, a=0.80, b=-2.07
Step 685: rmse=0.38, a=0.80, b=-2.08
Step 686: rmse=0.38, a=0.80, b=-2.08
Step 687: rmse=0.38, a=0.80, b=-2.08
Step 688: rmse=0.38, a=0.80, b=-2.08
Step 689: rmse=0.38, a=0.80, b=-2.08
Step 690: rmse=0.38, a=0.80, b=-2.08
Step 691: rmse=0.38, a=0.80, b=-2.08
Step 692: rmse=0.38, a=0.80, b=-2.08
Step 693: rmse=0.38, a=0.80, b=-2.09
Step 694: rmse=0.38, a=0.80, b=-2.09
Step 695: rmse=0.38, a=0.81, b=-2.09
Step 696: rmse=0.38, a=0.81, b=-2.09
Step 697: rmse=0.38, a=0.81, b=-2.09
Step 698: rmse=0.38, a=0.81, b=-2.09
Step 699: rmse=0.38, a=0.81, b=-2.09
Step 700: rmse=0.38, a=0.81, b=-2.10
Step 701: rmse=0.38, a=0.81, b=-2.10
Step 702: rmse=0.38, a=0.81, b=-2.10
Step 703: rmse=0.38, a=0.81, b=-2.10
Step 704: rmse=0.38, a=0.81, b=-2.10
Step 705: rmse=0.38, a=0.81, b=-2.10
Step 706: rmse=0.38, a=0.81, b=-2.10
Step 707: rmse=0.38, a=0.81, b=-2.10
Step 708: rmse=0.38, a=0.81, b=-2.11
Step 709: rmse=0.38, a=0.81, b=-2.11
Step 710: rmse=0.38, a=0.81, b=-2.11
Step 711: rmse=0.38, a=0.81, b=-2.11
Step 712: rmse=0.38, a=0.81, b=-2.11
Step 713: rmse=0.38, a=0.81, b=-2.11
Step 714: rmse=0.38, a=0.81, b=-2.11
Step 715: rmse=0.38, a=0.81, b=-2.12
Step 716: rmse=0.38, a=0.81, b=-2.12
Step 717: rmse=0.38, a=0.81, b=-2.12
Step 718: rmse=0.38, a=0.81, b=-2.12
Step 719: rmse=0.38, a=0.82, b=-2.12
Step 720: rmse=0.38, a=0.82, b=-2.12
Step 721: rmse=0.38, a=0.82, b=-2.12
Step 722: rmse=0.38, a=0.82, b=-2.12
Step 723: rmse=0.38, a=0.82, b=-2.13
Step 724: rmse=0.38, a=0.82, b=-2.13
Step 725: rmse=0.38, a=0.82, b=-2.13
Step 726: rmse=0.38, a=0.82, b=-2.13
Step 727: rmse=0.38, a=0.82, b=-2.13
Step 728: rmse=0.38, a=0.82, b=-2.13
Step 729: rmse=0.38, a=0.82, b=-2.13
Step 730: rmse=0.38, a=0.82, b=-2.13
Step 731: rmse=0.38, a=0.82, b=-2.14
Step 732: rmse=0.38, a=0.82, b=-2.14
Step 733: rmse=0.38, a=0.82, b=-2.14
Step 734: rmse=0.38, a=0.82, b=-2.14
Step 735: rmse=0.38, a=0.82, b=-2.14
Step 736: rmse=0.38, a=0.82, b=-2.14
Step 737: rmse=0.38, a=0.82, b=-2.14
Step 738: rmse=0.38, a=0.82, b=-2.14
Step 739: rmse=0.38, a=0.82, b=-2.15
Step 740: rmse=0.38, a=0.82, b=-2.15
Step 741: rmse=0.38, a=0.82, b=-2.15
Step 742: rmse=0.38, a=0.82, b=-2.15
Step 743: rmse=0.38, a=0.82, b=-2.15
Step 744: rmse=0.38, a=0.83, b=-2.15
Step 745: rmse=0.38, a=0.83, b=-2.15
Step 746: rmse=0.38, a=0.83, b=-2.15
Step 747: rmse=0.38, a=0.83, b=-2.16
Step 748: rmse=0.38, a=0.83, b=-2.16
Step 749: rmse=0.38, a=0.83, b=-2.16
Step 750: rmse=0.38, a=0.83, b=-2.16
Step 751: rmse=0.38, a=0.83, b=-2.16
Step 752: rmse=0.38, a=0.83, b=-2.16
Step 753: rmse=0.38, a=0.83, b=-2.16
Step 754: rmse=0.38, a=0.83, b=-2.16
Step 755: rmse=0.38, a=0.83, b=-2.16
Step 756: rmse=0.38, a=0.83, b=-2.17
Step 757: rmse=0.38, a=0.83, b=-2.17
Step 758: rmse=0.38, a=0.83, b=-2.17
Step 759: rmse=0.38, a=0.83, b=-2.17
Step 760: rmse=0.38, a=0.83, b=-2.17
Step 761: rmse=0.38, a=0.83, b=-2.17
Step 762: rmse=0.38, a=0.83, b=-2.17
Step 763: rmse=0.38, a=0.83, b=-2.17
Step 764: rmse=0.38, a=0.83, b=-2.18
Step 765: rmse=0.38, a=0.83, b=-2.18
Step 766: rmse=0.38, a=0.83, b=-2.18
Step 767: rmse=0.38, a=0.83, b=-2.18
Step 768: rmse=0.38, a=0.83, b=-2.18
Step 769: rmse=0.38, a=0.84, b=-2.18
Step 770: rmse=0.38, a=0.84, b=-2.18
Step 771: rmse=0.38, a=0.84, b=-2.18
Step 772: rmse=0.38, a=0.84, b=-2.19
Step 773: rmse=0.38, a=0.84, b=-2.19
Step 774: rmse=0.38, a=0.84, b=-2.19
Step 775: rmse=0.38, a=0.84, b=-2.19
Step 776: rmse=0.38, a=0.84, b=-2.19
Step 777: rmse=0.38, a=0.84, b=-2.19
Step 778: rmse=0.38, a=0.84, b=-2.19
Step 779: rmse=0.37, a=0.84, b=-2.19
Step 780: rmse=0.37, a=0.84, b=-2.19
Step 781: rmse=0.37, a=0.84, b=-2.20
Step 782: rmse=0.37, a=0.84, b=-2.20
Step 783: rmse=0.37, a=0.84, b=-2.20
Step 784: rmse=0.37, a=0.84, b=-2.20
Step 785: rmse=0.37, a=0.84, b=-2.20
Step 786: rmse=0.37, a=0.84, b=-2.20
Step 787: rmse=0.37, a=0.84, b=-2.20
Step 788: rmse=0.37, a=0.84, b=-2.20
Step 789: rmse=0.37, a=0.84, b=-2.20
Step 790: rmse=0.37, a=0.84, b=-2.21
Step 791: rmse=0.37, a=0.84, b=-2.21
Step 792: rmse=0.37, a=0.84, b=-2.21
Step 793: rmse=0.37, a=0.84, b=-2.21
Step 794: rmse=0.37, a=0.84, b=-2.21
Step 795: rmse=0.37, a=0.84, b=-2.21
Step 796: rmse=0.37, a=0.85, b=-2.21
Step 797: rmse=0.37, a=0.85, b=-2.21
Step 798: rmse=0.37, a=0.85, b=-2.22
Step 799: rmse=0.37, a=0.85, b=-2.22
Step 800: rmse=0.37, a=0.85, b=-2.22
Step 801: rmse=0.37, a=0.85, b=-2.22
Step 802: rmse=0.37, a=0.85, b=-2.22
Step 803: rmse=0.37, a=0.85, b=-2.22
Step 804: rmse=0.37, a=0.85, b=-2.22
Step 805: rmse=0.37, a=0.85, b=-2.22
Step 806: rmse=0.37, a=0.85, b=-2.22
Step 807: rmse=0.37, a=0.85, b=-2.23
Step 808: rmse=0.37, a=0.85, b=-2.23
Step 809: rmse=0.37, a=0.85, b=-2.23
Step 810: rmse=0.37, a=0.85, b=-2.23
Step 811: rmse=0.37, a=0.85, b=-2.23
Step 812: rmse=0.37, a=0.85, b=-2.23
Step 813: rmse=0.37, a=0.85, b=-2.23
Step 814: rmse=0.37, a=0.85, b=-2.23
Step 815: rmse=0.37, a=0.85, b=-2.23
Step 816: rmse=0.37, a=0.85, b=-2.24
Step 817: rmse=0.37, a=0.85, b=-2.24
Step 818: rmse=0.37, a=0.85, b=-2.24
Step 819: rmse=0.37, a=0.85, b=-2.24
Step 820: rmse=0.37, a=0.85, b=-2.24
Step 821: rmse=0.37, a=0.85, b=-2.24
Step 822: rmse=0.37, a=0.85, b=-2.24
Step 823: rmse=0.37, a=0.85, b=-2.24
Step 824: rmse=0.37, a=0.86, b=-2.24
Step 825: rmse=0.37, a=0.86, b=-2.24
Step 826: rmse=0.37, a=0.86, b=-2.25
Step 827: rmse=0.37, a=0.86, b=-2.25
Step 828: rmse=0.37, a=0.86, b=-2.25
Step 829: rmse=0.37, a=0.86, b=-2.25
Step 830: rmse=0.37, a=0.86, b=-2.25
Step 831: rmse=0.37, a=0.86, b=-2.25
Step 832: rmse=0.37, a=0.86, b=-2.25
Step 833: rmse=0.37, a=0.86, b=-2.25
Step 834: rmse=0.37, a=0.86, b=-2.25
Step 835: rmse=0.37, a=0.86, b=-2.26
Step 836: rmse=0.37, a=0.86, b=-2.26
Step 837: rmse=0.37, a=0.86, b=-2.26
Step 838: rmse=0.37, a=0.86, b=-2.26
Step 839: rmse=0.37, a=0.86, b=-2.26
Step 840: rmse=0.37, a=0.86, b=-2.26
Step 841: rmse=0.37, a=0.86, b=-2.26
Step 842: rmse=0.37, a=0.86, b=-2.26
Step 843: rmse=0.37, a=0.86, b=-2.26
Step 844: rmse=0.37, a=0.86, b=-2.27
Step 845: rmse=0.37, a=0.86, b=-2.27
Step 846: rmse=0.37, a=0.86, b=-2.27
Step 847: rmse=0.37, a=0.86, b=-2.27
Step 848: rmse=0.37, a=0.86, b=-2.27
Step 849: rmse=0.37, a=0.86, b=-2.27
Step 850: rmse=0.37, a=0.86, b=-2.27
Step 851: rmse=0.37, a=0.86, b=-2.27
Step 852: rmse=0.37, a=0.86, b=-2.27
Step 853: rmse=0.37, a=0.87, b=-2.27
Step 854: rmse=0.37, a=0.87, b=-2.28
Step 855: rmse=0.37, a=0.87, b=-2.28
Step 856: rmse=0.37, a=0.87, b=-2.28
Step 857: rmse=0.37, a=0.87, b=-2.28
Step 858: rmse=0.37, a=0.87, b=-2.28
Step 859: rmse=0.37, a=0.87, b=-2.28
Step 860: rmse=0.37, a=0.87, b=-2.28
Step 861: rmse=0.37, a=0.87, b=-2.28
Step 862: rmse=0.37, a=0.87, b=-2.28
Step 863: rmse=0.37, a=0.87, b=-2.29
Step 864: rmse=0.37, a=0.87, b=-2.29
Step 865: rmse=0.37, a=0.87, b=-2.29
Step 866: rmse=0.37, a=0.87, b=-2.29
Step 867: rmse=0.37, a=0.87, b=-2.29
Step 868: rmse=0.37, a=0.87, b=-2.29
Step 869: rmse=0.37, a=0.87, b=-2.29
Step 870: rmse=0.37, a=0.87, b=-2.29
Step 871: rmse=0.37, a=0.87, b=-2.29
Step 872: rmse=0.37, a=0.87, b=-2.29
Step 873: rmse=0.37, a=0.87, b=-2.30
Step 874: rmse=0.37, a=0.87, b=-2.30
Step 875: rmse=0.37, a=0.87, b=-2.30
Step 876: rmse=0.37, a=0.87, b=-2.30
Step 877: rmse=0.37, a=0.87, b=-2.30
Step 878: rmse=0.37, a=0.87, b=-2.30
Step 879: rmse=0.37, a=0.87, b=-2.30
Step 880: rmse=0.37, a=0.87, b=-2.30
Step 881: rmse=0.37, a=0.87, b=-2.30
Step 882: rmse=0.37, a=0.87, b=-2.30
Step 883: rmse=0.37, a=0.87, b=-2.31
Step 884: rmse=0.37, a=0.88, b=-2.31
Step 885: rmse=0.37, a=0.88, b=-2.31
Step 886: rmse=0.37, a=0.88, b=-2.31
Step 887: rmse=0.37, a=0.88, b=-2.31
Step 888: rmse=0.37, a=0.88, b=-2.31
Step 889: rmse=0.37, a=0.88, b=-2.31
Step 890: rmse=0.37, a=0.88, b=-2.31
Step 891: rmse=0.37, a=0.88, b=-2.31
Step 892: rmse=0.37, a=0.88, b=-2.31
Step 893: rmse=0.37, a=0.88, b=-2.32
Step 894: rmse=0.37, a=0.88, b=-2.32
Step 895: rmse=0.37, a=0.88, b=-2.32
Step 896: rmse=0.37, a=0.88, b=-2.32
Step 897: rmse=0.37, a=0.88, b=-2.32
Step 898: rmse=0.37, a=0.88, b=-2.32
Step 899: rmse=0.37, a=0.88, b=-2.32
Step 900: rmse=0.37, a=0.88, b=-2.32
Step 901: rmse=0.37, a=0.88, b=-2.32
Step 902: rmse=0.37, a=0.88, b=-2.32
Step 903: rmse=0.37, a=0.88, b=-2.32
Step 904: rmse=0.37, a=0.88, b=-2.33
Step 905: rmse=0.37, a=0.88, b=-2.33
Step 906: rmse=0.37, a=0.88, b=-2.33
Step 907: rmse=0.37, a=0.88, b=-2.33
Step 908: rmse=0.37, a=0.88, b=-2.33
Step 909: rmse=0.37, a=0.88, b=-2.33
Step 910: rmse=0.37, a=0.88, b=-2.33
Step 911: rmse=0.37, a=0.88, b=-2.33
Step 912: rmse=0.37, a=0.88, b=-2.33
Step 913: rmse=0.37, a=0.88, b=-2.33
Step 914: rmse=0.37, a=0.88, b=-2.34
Step 915: rmse=0.37, a=0.89, b=-2.34
Step 916: rmse=0.37, a=0.89, b=-2.34
Step 917: rmse=0.37, a=0.89, b=-2.34
Step 918: rmse=0.37, a=0.89, b=-2.34
Step 919: rmse=0.37, a=0.89, b=-2.34
Step 920: rmse=0.37, a=0.89, b=-2.34
Step 921: rmse=0.37, a=0.89, b=-2.34
Step 922: rmse=0.37, a=0.89, b=-2.34
Step 923: rmse=0.37, a=0.89, b=-2.34
Step 924: rmse=0.37, a=0.89, b=-2.34
Step 925: rmse=0.37, a=0.89, b=-2.35
Step 926: rmse=0.37, a=0.89, b=-2.35
Step 927: rmse=0.37, a=0.89, b=-2.35
Step 928: rmse=0.37, a=0.89, b=-2.35
Step 929: rmse=0.37, a=0.89, b=-2.35
Step 930: rmse=0.37, a=0.89, b=-2.35
Step 931: rmse=0.37, a=0.89, b=-2.35
Step 932: rmse=0.37, a=0.89, b=-2.35
Step 933: rmse=0.37, a=0.89, b=-2.35
Step 934: rmse=0.37, a=0.89, b=-2.35
Step 935: rmse=0.37, a=0.89, b=-2.36
Step 936: rmse=0.37, a=0.89, b=-2.36
Step 937: rmse=0.37, a=0.89, b=-2.36
Step 938: rmse=0.37, a=0.89, b=-2.36
Step 939: rmse=0.37, a=0.89, b=-2.36
Step 940: rmse=0.37, a=0.89, b=-2.36
Step 941: rmse=0.37, a=0.89, b=-2.36
Step 942: rmse=0.37, a=0.89, b=-2.36
Step 943: rmse=0.37, a=0.89, b=-2.36
Step 944: rmse=0.37, a=0.89, b=-2.36
Step 945: rmse=0.37, a=0.89, b=-2.36
Step 946: rmse=0.37, a=0.89, b=-2.37
Step 947: rmse=0.37, a=0.89, b=-2.37
Step 948: rmse=0.37, a=0.90, b=-2.37
Step 949: rmse=0.37, a=0.90, b=-2.37
Step 950: rmse=0.37, a=0.90, b=-2.37
Step 951: rmse=0.37, a=0.90, b=-2.37
Step 952: rmse=0.37, a=0.90, b=-2.37
Step 953: rmse=0.37, a=0.90, b=-2.37
Step 954: rmse=0.37, a=0.90, b=-2.37
Step 955: rmse=0.37, a=0.90, b=-2.37
Step 956: rmse=0.37, a=0.90, b=-2.37
Step 957: rmse=0.37, a=0.90, b=-2.38
Step 958: rmse=0.37, a=0.90, b=-2.38
Step 959: rmse=0.37, a=0.90, b=-2.38
Step 960: rmse=0.37, a=0.90, b=-2.38
Step 961: rmse=0.37, a=0.90, b=-2.38
Step 962: rmse=0.37, a=0.90, b=-2.38
Step 963: rmse=0.37, a=0.90, b=-2.38
Step 964: rmse=0.37, a=0.90, b=-2.38
Step 965: rmse=0.37, a=0.90, b=-2.38
Step 966: rmse=0.37, a=0.90, b=-2.38
Step 967: rmse=0.37, a=0.90, b=-2.38
Step 968: rmse=0.37, a=0.90, b=-2.39
Step 969: rmse=0.37, a=0.90, b=-2.39
Step 970: rmse=0.37, a=0.90, b=-2.39
Step 971: rmse=0.37, a=0.90, b=-2.39
Step 972: rmse=0.37, a=0.90, b=-2.39
Step 973: rmse=0.37, a=0.90, b=-2.39
Step 974: rmse=0.37, a=0.90, b=-2.39
Step 975: rmse=0.37, a=0.90, b=-2.39
Step 976: rmse=0.37, a=0.90, b=-2.39
Step 977: rmse=0.37, a=0.90, b=-2.39
Step 978: rmse=0.37, a=0.90, b=-2.39
Step 979: rmse=0.37, a=0.90, b=-2.39
Step 980: rmse=0.37, a=0.90, b=-2.40
Step 981: rmse=0.37, a=0.90, b=-2.40
Step 982: rmse=0.37, a=0.90, b=-2.40
Step 983: rmse=0.37, a=0.91, b=-2.40
Step 984: rmse=0.37, a=0.91, b=-2.40
Step 985: rmse=0.37, a=0.91, b=-2.40
Step 986: rmse=0.37, a=0.91, b=-2.40
Step 987: rmse=0.37, a=0.91, b=-2.40
Step 988: rmse=0.37, a=0.91, b=-2.40
Step 989: rmse=0.37, a=0.91, b=-2.40
Step 990: rmse=0.37, a=0.91, b=-2.40
Step 991: rmse=0.37, a=0.91, b=-2.41
Step 992: rmse=0.37, a=0.91, b=-2.41
Step 993: rmse=0.37, a=0.91, b=-2.41
Step 994: rmse=0.37, a=0.91, b=-2.41
Step 995: rmse=0.37, a=0.91, b=-2.41
Step 996: rmse=0.37, a=0.91, b=-2.41
Step 997: rmse=0.37, a=0.91, b=-2.41
Step 998: rmse=0.37, a=0.91, b=-2.41
Step 999: rmse=0.37, a=0.91, b=-2.41
>>> 
>>> P = [1/(1+math.exp(-(b + a*X[i]))) for i in range(0,n)]
>>> print('x\t y\t Prob\t Predict')
x	 y	 Prob	 Predict
>>> for i in range(0,n):
	print('%0.2f\t %d\t %0.2f\t %d'%(X[i], Y[i], P[i], round(P[i])))

	
0.50	 0	 0.12	 0
0.75	 0	 0.15	 0
1.00	 0	 0.18	 0
1.25	 0	 0.22	 0
1.50	 0	 0.26	 0
1.75	 0	 0.31	 0
1.75	 1	 0.31	 0
2.00	 0	 0.36	 0
2.25	 1	 0.41	 0
2.50	 0	 0.47	 0
2.75	 1	 0.52	 1
3.00	 0	 0.58	 1
3.25	 1	 0.63	 1
3.50	 0	 0.68	 1
4.00	 1	 0.77	 1
4.25	 1	 0.81	 1
4.50	 1	 0.84	 1
4.75	 1	 0.87	 1
5.00	 1	 0.89	 1
5.50	 1	 0.93	 1
>>> 