# importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos la imagen
image = cv2.imread('robotech.jpg')

# Pasamos img a EDG
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Creamos la matriz del tamañp de la imagen seleccionada
matrix = np.ones(gray_image.shape, dtype='uint8') * 50

# Cómo umbralizamos la imagen brillante?
# Comando: retval, dst = cv2.threshold(img, tresh(Umbral: debajo = 0, encima = 255), maxval, tipo de umbral)
#                  maxval = TRESH_BINARY o THRESH_BINARY_INV
# Comando:         dst = cv2.adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blocksize)
#                  adaptiveMethod = BORDER_REPLICATE o BORDER_ISOLATE
#                  thresholdType = TRESH_BINARY o THRESH_BINARY_INV

# Vamos a aumentar el brillo de la imagen en EDG
bright_gray = cv2.add(gray_image, matrix)

# El THRESHOLD, EL UMBRALIZADO
_, image_thres_1 = cv2.threshold(bright_gray, 160, 255, cv2.THRESH_BINARY)

_, image_thres_2 = cv2.threshold(bright_gray, 180, 255, cv2.THRESH_BINARY_INV)

# THRESHOLD ADAPTIVE
image_adaptive_1 = cv2.adaptiveThreshold(bright_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Disminuimos el brillo en gray_image
dark_gray = cv2.subtract(gray_image, matrix)

_, image_thres_3 = cv2.threshold(dark_gray, 50, 255, cv2.THRESH_BINARY)

_, image_thres_4 = cv2.threshold(dark_gray, 50, 255, cv2.THRESH_BINARY_INV)

# THRESHOLD ADAPTIVE
image_adaptive_2 = cv2.adaptiveThreshold(dark_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 7)

# Ploteamos las imágenes
fig = plt.figure()
# IMAGEN BRILLANTE
ax1 = fig.add_subplot(2, 4, 1)
ax1.imshow(bright_gray, cmap="gray")
ax1.set_title("BRILLANTE")

# BRILLANTE THRESH 1
ax3 = fig.add_subplot(2, 4, 2)
ax3.imshow(image_thres_1, cmap="gray")
ax3.set_title("BRILLANTE THRESH 1")

# BRILLANTE THRESH 2
ax4 = fig.add_subplot(2, 4, 3)
ax4.imshow(image_thres_2, cmap="gray")
ax4.set_title("BRILLANTE THRESH 2")

# BRILLANTE ADAPTIVE
ax4 = fig.add_subplot(2, 4, 4)
ax4.imshow(image_adaptive_1, cmap="gray")
ax4.set_title("BRILLANTE ADAPTIVE 1")

# OSCURA
ax2 = fig.add_subplot(2, 4, 5)
ax2.imshow(dark_gray, cmap="gray")
ax2.set_title("OSCURO")

# OSCURA THRESH 1
ax3 = fig.add_subplot(2, 4, 6)
ax3.imshow(image_thres_3, cmap="gray")
ax3.set_title("OSCURO THRESH 1")

# OSCURA THRESH 2
ax4 = fig.add_subplot(2, 4, 7)
ax4.imshow(image_thres_4, cmap="gray")
ax4.set_title("OSCURO THRESH 2")

# OSCURA ADAPTIVE
ax4 = fig.add_subplot(2, 4, 8)
ax4.imshow(image_adaptive_2, cmap="gray")
ax4.set_title("OSCURO ADAPTIVE 1")

plt.show()
