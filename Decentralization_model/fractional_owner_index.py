# ==========================================
# Calculate global clustering coefficient
# ==========================================
def calculate_fractional_owner_index(list_supply):
    owner_index = 1 - (list_supply[0] / list_supply[1])
    return owner_index
