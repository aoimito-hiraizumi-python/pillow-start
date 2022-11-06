import numpy as np
from PIL import Image

# 0が黒 255が白
# l = np.array([
#     [0, 128, 255],
#     [0, 128, 255],
#     [0, 128, 255],
# ])

row_data = np.arange(256)
# 0から256の一個まえの数字を生成
im_data = np.tile(row_data, (255, 1))
# 縦方向にも生成


im = Image.fromarray(np.uint8(im_data), "L")
im.show()
