import os
import argparse
from config import *

from methods.lucas_kanade import lucas_kanade_flow
from methods.horn_schunck import horn_schunck_flow


from utils.image_utils import gaussian_presmoothing
from utils.math_utils import 










     
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Differential Optical Flow Estimation")
    parser = argparse.add_argument("--method", type=str, choices = ["lucas_kanade",
                                                                    "horn_schunck",
                                                                    "spatial_clg",
                                                                    "spatiotemporal_clg"
                                                                    "nonquadratic_clg",
                                                                    "multiresolution_variant"],
                                                                    requird = True, help = "Choose the disired  optic flow method from the list.")
    
    parser.add_argument("--local_window_size", type=int, default=LOCAL_WINDOW_SIZE, help="Neighbors with the same flow assumption")
    parser.add_argument("--pre_smoothing", type=bool, default=PRE_SMOOTHING, help="Pre-smoothing is required or not?")
    parser.add_argument("--intensity_diff_order", type=int, help="The order of finite_difference_approximation")
    
    args = parser.parse_args()
    
