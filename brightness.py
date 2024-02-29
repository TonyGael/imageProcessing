# importamos las librerías:
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos la imagen:
img = cv2.imread('robotech.jpg')
img_mat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convertimos a ESCALA DE GRISES
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# creamos una matriz del tamaño de la imagen:
matriz_rgb = np.ones(img.shape, dtype='uint8') * 50
matriz_gray = np.ones(gray.shape, dtype='uint8') * 50

# AumentaMos en brillo en La iMagen RGB
brillo_rgb = cv2.add(img, matriz_rgb)
brillo_rgbm = cv2.cvtColor(brillo_rgb, cv2.COLOR_BGR2RGB)

# Disminuimos el brillo en RGB
oscuro_rgb = cv2.subtract(img, matriz_rgb)
oscuro_rgbm = cv2.cvtColor(oscuro_rgb, cv2.COLOR_BGR2RGB)

# AUMENTAMOS EL BRILLO EN LA IMAGEN GRIS
brillo_gray = cv2.add(gray, matriz_gray)

# disminuimos el brillo en la imagen gris
oscuro_gray = cv2.subtract(gray, matriz_gray)

# PLoteamos las imagenes
fig = plt.figure()

# Imagen original:
ax1 = fig.add_subplot(2, 3, 1)
ax1.imshow(img_mat)
ax1.set_title('IMAGEN ORIGINAL EN ax1 EN POSICION (2, 3, 1)')

# BRILLANTE EN  RGB
ax3 = fig.add_subplot(2, 3, 2)
ax3.imshow(brillo_rgbm)
ax3.set_title('BRILLANTE RGB EN ax3 EN POSICION (2, 3, 2)')

# OSCURO EN RGB
ax4 = fig.add_subplot(2, 3, 3)
ax4.imshow(oscuro_rgbm)
ax4.set_title('OSCURO EN RGB EN POSICION (2, 3, 3)')

# IMAGEN EN ESCALA DE GRISES
ax2 = fig.add_subplot(2, 3, 4)
ax2.imshow(gray, cmap='gray')
ax2.set_title('EDG EN ax2 EN POSICION (2, 3, 4)')

# BRILLANTE EN ESCALA DE GRISES
ax3 = fig.add_subplot(2, 3, 5)
ax3.imshow(brillo_gray, cmap='gray')
ax3.set_title('BRILLANTE EN EDG EN ax3 EN POSICION (2, 3, 5)')

# OSCURO EN ESCALA DE GRISES
ax4 = fig.add_subplot(2, 3, 6)
ax4.imshow(oscuro_gray, cmap='gray')
ax4.set_title('OSCURO EN EDG EN ax4 EN POSICION (2, 3, 6)')

plt.show()

# PLOTEAMOS LA IMAGEN:
cv2.imshow('IMAGEN BRILLANTE EN EDG', brillo_gray)
cv2.imshow('IMAGEN OSCURA EN EDG', oscuro_gray)
cv2.imshow('IMAGEN BRILLANTE RGB', brillo_rgb)
cv2.imshow('IMAGEN OSCURA RGB', oscuro_rgb)

cv2. waitKey(0)
