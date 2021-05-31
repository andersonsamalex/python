import cv2
import numpy as np
from skimage import io

def dominant_color(img):
    pixels = np.float32(img.reshape(-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    dom = palette[np.argmax(counts)]
    
    return dom

fname = input("Enter image to be flattened: ")
orientation = input("H or V: ")
img = io.imread(fname + '.png')
rows, cols, ch = img.shape
print(img.shape)
img2 = np.zeros((rows, cols, ch),np.uint8)
print("Processing...")

if (orientation == 'H'):
    for x in range(rows):
        row = img[x,:]
        color = dominant_color(img = row)
        for y in range(cols):
            img2[x,y,0] = int(color[0])
            img2[x,y,1] = int(color[1])
            img2[x,y,2] = int(color[2])
if (orientation == 'V'):
    for x in range(cols):
        col = img[:,x]
        color = dominant_color(img = col)
        for y in range(rows):
            img2[y,x,0] = int(color[0])
            img2[y,x,1] = int(color[1])
            img2[y,x,2] = int(color[2])

io.imsave(fname + '_flattened.png',img2)
print("Finished.")

