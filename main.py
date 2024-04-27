import os
import argparse
from config import *

from methods.lucas_kanade import Lucas_Kanade_flow
from methods.horn_schunck import horn_schunck_flow


from utils.image_utils import gaussian_presmoothing
from utils.math_utils import 









def main():
    parser = argparse.ArgumentParser(description="Differential Optical Flow Estimation")
    parser.add_argument("--local_window_size", type=int, default=LOCAL_WINDOW_SIZE, help="Neighbors with the same flow assumption")
    parser.add_argument("--pre_smoothing", type=bool, default=PRE_SMOOTHING, help="Pre-smoothing is required or not?")
    args = parser.parse_args()
    
    
    #if pre_smoothing:
    img_1 = gaussian_presmoothing(img_1)
    img_2 = gaussian_presmoothing(img_2)

     
if __name__ == "__main__":
    main()
    main()
    