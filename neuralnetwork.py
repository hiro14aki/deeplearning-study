import numpy as np

# シグモイド関数(活性化関数)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 恒等関数(シグマ)
def identity_function(x):
        return x

# 1階層目の重み付け
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape) # (2, 3)
print(X.shape)  # (2,)
print(B1.shape) # (3,)

# 1階層目の重み付き和
A1 = np.dot(X, W1) + B1
print(A1)

# 1階層目の活性化関数
Z1 = sigmoid(A1)
print(Z1)

# 2層目の重み付け
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape) # (3,)
print(W2.shape) # (3, 2)
print(B2.shape) # (2,)

# 2階層目の重み付け和
A2 = np.dot(Z1, W2) + B2

# 2階層目の活性化関数
Z2 = sigmoid(A2)
print(Z2)

# 3階層目の重み付け
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

# 2階層目の重み付け和
A3 = np.dot(Z2, W3) + B3

# 3階層目の恒等関数
Y = identity_function(A3)
print(Y)
