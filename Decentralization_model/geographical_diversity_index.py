# ==========================================
# Imports and final variables
# ==========================================
import math
import itertools

# Total countries in world
total_countries = 193


# ==========================================
# Calculate geographical diversity index
# ==========================================
def calculate_geo_index(case_list):

    countries_with_nodes = total_countries - case_list.count(0)

    counter = math.log(total_countries, (countries_with_nodes+1)) - math.log(total_countries, (total_countries+1))
    denominator = math.log2(total_countries) - math.log(total_countries, (total_countries+1))

    summed = 0

    for i in range(0, total_countries):
        summed += pow((case_list[i]-(sum(case_list)/total_countries)), 2)

    index = (2 - (counter/denominator)) * math.sqrt((summed/total_countries))

    return index


# ==========================================
# Normalize geographical diversity index
# ==========================================
def normalize_geographical_diversity_index(geo_list):

    even = sum(geo_list)//total_countries

    # Generate best and worst case for available nodes
    best_case_list = [even+1 if i < sum(geo_list) % total_countries else even for i in range(0, total_countries)]
    worst_case_list = list(itertools.repeat(0, 193))
    worst_case_list[0] = sum(geo_list)
    geo_list = geo_list + list(itertools.repeat(0, total_countries - len(geo_list)))

    # Calculate best, worst, and actual geo index
    geo_index_min = calculate_geo_index(worst_case_list)
    geo_index_max = calculate_geo_index(best_case_list)
    geo_index = calculate_geo_index(geo_list)

    # Normalize index
    normalized_index = ((geo_index_min - geo_index - geo_index_max)/(geo_index_min - geo_index_max))
    if normalized_index < 0:
        normalized_index = 0.0

    return normalized_index
