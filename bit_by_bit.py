# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tenemos 4 tipos de operaciones bit a bit: (Operaciones logicas)
# cv2.bitwise_and(img1, img2 , mask)  |  cv2.bitwise_or()  |  cv2.bitwise_xor()  |  cv2.bitwise_not()

# IMAGENES
image_1 = cv2.imread('img1.png', 0)
image_2 = cv2.imread('img2.png', 0)

# OPERACION AND
image_and = cv2.bitwise_and(image_1, image_2, mask=None)

# OPERACION OR
image_or = cv2.bitwise_or(image_1, image_2, mask=None)

# OPERACION XOR
image_xor = cv2.bitwise_xor(image_1, image_2, mask=None)


# Mostramos Imagenes
fig = plt.figure()

# IMAGEN 1
ax1 = fig.add_subplot(2, 3, 1)
ax1.imshow(image_1, cmap="gray")
ax1.set_title("IMAGEN 1")

# IMAGEN 2
ax2 = fig.add_subplot(2, 3, 4)
ax2.imshow(image_2, cmap="gray")
ax2.set_title("IMAGEN 2")

# IMAGEN AND
ax3 = fig.add_subplot(2, 3, 2)
ax3.imshow(image_and, cmap="gray")
ax3.set_title("IMAGEN AND")

# IMAGEN OR
ax4 = fig.add_subplot(2, 3, 3)
ax4.imshow(image_or, cmap="gray")
ax4.set_title("IMAGEN OR")

# IMAGEN XOR
ax5 = fig.add_subplot(2, 3, 5)
ax5.imshow(image_xor, cmap="gray")
ax5.set_title("IMAGEN XOR")

# APLICACION CON IMG
image_logo = cv2.imread('logo.png')
image_background = cv2.imread('fondo.png')

# CORRECCION DE COLOR
img_logo = cv2.cvtColor(image_logo, cv2.COLOR_BGR2RGB)
img_back = cv2.cvtColor(image_background, cv2.COLOR_BGR2RGB)

# CREAMOS UNA MASCARA
gray_logo = cv2.cvtColor(img_logo, cv2.COLOR_RGB2GRAY)
_, img_mask = cv2.threshold(gray_logo, 127, 255, cv2.THRESH_BINARY)

# MASCARA INVERTIDA
img_mask_inv = cv2.bitwise_not(img_mask)

# REALIZAMOS OPERACIONES
img_app_1 = cv2.bitwise_and(img_logo, img_back, mask=img_mask)

img_app_2 = cv2.bitwise_and(img_logo, img_logo, mask=img_mask_inv)

img_app_3 = cv2.subtract(img_back, img_app_2)

# Mostramos Imagenes
fig1 = plt.figure()

# IMAGEN 1
ax11 = fig1.add_subplot(3, 3, 1)
ax11.imshow(img_logo)
ax11.set_title("IMAGEN 1")

# IMAGEN 2
ax22 = fig1.add_subplot(3, 3, 4)
ax22.imshow(img_back)
ax22.set_title("IMAGEN 2")

# IMAGEN MASK
ax33 = fig1.add_subplot(3, 3, 2)
ax33.imshow(img_mask, cmap="gray")
ax33.set_title("IMAGEN MASK")

# IMAGEN MASK INVERTIDA
ax44 = fig1.add_subplot(3, 3, 3)
ax44.imshow(img_mask_inv, cmap='gray')
ax44.set_title("IMAGEN MASK INV")

# IMAGEN AND
ax44 = fig1.add_subplot(3, 3, 5)
ax44.imshow(img_app_1)
ax44.set_title("IMAGEN AND")

# IMAGEN AND 2
ax44 = fig1.add_subplot(3, 3, 6)
ax44.imshow(img_app_2)
ax44.set_title("IMAGEN AND 2")

# IMAGEN ADD
ax44 = fig1.add_subplot(3, 3, 8)
ax44.imshow(img_app_3)
ax44.set_title("IMAGEN ADD")

plt.show()
