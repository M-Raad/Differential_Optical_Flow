import cv2


def gaussian_presmoothing (img, kernel_size, sigma):
    blurred_image = cv2.GaussianBlur(img, kernel_size, sigma)
    return blurred_image
    