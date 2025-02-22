import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# sin グラフ
x = np.arange(0, 6, 0.1)
y = np.sin(x)
# グラフの描画
plt.plot(x, y)
plt.show()

# cos グラフ
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

# Image
# 実行するパスからの相対パスで指定
img = imread('./assets/tennis.jpeg')
plt.imshow(img)
plt.show()
