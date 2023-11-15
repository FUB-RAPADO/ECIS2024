# ==========================================
# Imports
# ==========================================
import math


# ==========================================
# Calculate shannon index
# ==========================================
def calculate_shannon_index(sw_list):

    shannon_coefficient = 0

    for i in range(1, len(sw_list)):
        shannon_coefficient += (sw_list[i]/sum(sw_list)) * math.log2((sw_list[i]/sum(sw_list)))

    shannon_coefficient *= -1
    shannon_coefficient /= math.log2(sum(sw_list))

    return shannon_coefficient
