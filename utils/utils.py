import numpy as np 
import config





def finite_diff_coeffs(stencil_len, order):
    # Create the matrix A
    A = np.zeros((stencil_len, stencil_len))
    for i in range(stencil_len):
        for j in range(stencil_len):
            A[i, j] = ((j - stencil_len // 2) ** i) / np.math.factorial(i)

    # Create the vector b
    b = np.zeros(stencil_len)
    b[order] = 1

    # Solve the system of linear equations
    coeffs = np.linalg.solve(A, b)
    return coeffs




def gaussian_presmoothing (img, kernel_size, sigma):
    blurred_image = cv2.GaussianBlur(img, kernel_size, sigma)
    return blurred_image
