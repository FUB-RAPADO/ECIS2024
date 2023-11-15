# ==========================================
# Imports
# ==========================================
import pandas as pd
import itertools


# ==========================================
# Calculate global clustering coefficient
# ==========================================
def calculate_share(share_list):

    share_list_sum = sum(share_list)

    for i in range(0, len(share_list)):
        share_list[i] = (share_list[i] / share_list_sum) * 100

    return share_list


# ==========================================
# Data import and preprocessing
# ==========================================

df_owner_control = pd.read_csv('data/5_Owner_control/owner_control.csv', header=0, sep=';')

# ------------------------------------------
# BITCOIN DATA
# ------------------------------------------

# Decision-making
df_btc_dm = pd.read_csv('data/1_Decision_making/Bitcoin_decision_making.csv', header=0, sep=';', encoding='latin1')
list_btc_dm = df_btc_dm['Hash_Raten_Anteil'].values.tolist()

# Hosting Concentration
df_btc_ho = pd.read_csv('data/2_Hosting_concentration/Bitcoin_hosting.csv', header=0, sep=';')
list_btc_ho = df_btc_ho['Network_Share'].values.tolist()

# Geographical diversity
df_btc_geo = pd.read_csv('data/3_Geographical_diversity/Bitcoin_Geo.csv', header=0, sep=';')
list_btc_geo = df_btc_geo['Nodes'].values.tolist()

# Reference client contributions
df_btc_rcc = pd.read_csv('data/4_Reference_client_contributions/Bitcoin_contributions.csv', header=0, sep=';')
list_btc_rcc = df_btc_rcc['Commits'].values.tolist()
calculate_share(list_btc_rcc)

# Improvement protocol
df_btc_ip = pd.read_csv('data/6_Improvement_protocol/Bitcoin_improvement_proposals.csv', header=0, sep=';', encoding='latin1')
df_btc_ip_count = df_btc_ip['Author'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_btc_ip = df_btc_ip_count['counts'].values.tolist()
calculate_share(list_btc_ip)

# Owner control
list_btc_oc = [df_owner_control.iloc[0]['Supply'], df_owner_control.iloc[0]['Total_supply']]

#  Exchange concentration
df_btc_ex = pd.read_csv('data/7_Exchange_concentration/Bitcoin_exchanges.csv', header=0, sep=';')
list_btc_ex = df_btc_ex['Volume'].values.tolist()
calculate_share(list_btc_ex)

# ------------------------------------------
# CARDANO DATA
# ------------------------------------------

# Decision-making
df_car_dm = pd.read_csv('data/1_Decision_making/Cardano_decision_making.csv', header=0, sep=';')
list_car_dm = df_car_dm['Stake'].values.tolist()
calculate_share(list_car_dm)

# Hosting Concentration
df_car_ho = pd.read_csv('data/2_Hosting_concentration/Cardano_hosting.csv', header=0, sep=';', encoding='latin1')
list_car_ho = df_car_ho['Uniq'].values.tolist()

# Geographical diversity
df_car_geo = pd.read_csv('data/3_Geographical_diversity/Cardano_Geo.csv', header=0, sep=';')
list_car_geo = df_car_geo['Uniq'].values.tolist()

# Reference client contributions
df_car_rcc = pd.read_csv('data/4_Reference_client_contributions/Cardano_contributions.csv', header=0, sep=';')
list_car_rcc = df_car_rcc['Commits'].values.tolist()
calculate_share(list_car_rcc)

# Improvement protocol
df_car_ip = pd.read_csv('data/6_Improvement_protocol/Cardano_improvement_proposals.csv', header=0, sep=';', encoding='latin1')
df_car_ip_count = df_car_ip['Author'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_car_ip = df_car_ip_count['counts'].values.tolist()
calculate_share(list_car_ip)

# Owner control
list_car_oc = [df_owner_control.iloc[1]['Supply'], df_owner_control.iloc[1]['Total_supply']]

#  Exchange concentration
df_car_ex = pd.read_csv('data/7_Exchange_concentration/Cardano_exchanges.csv', header=0, sep=';', encoding='latin1')
list_car_ex = df_car_ex['Volume'].values.tolist()
calculate_share(list_car_ex)

# ------------------------------------------
# SOLANA DATA
# ------------------------------------------

# Decision-making
df_sol_dm = pd.read_csv('data/1_Decision_making/Solana_decision_making.csv', header=0, sep=';', encoding='latin1')
list_sol_dm = df_sol_dm['Active_stake'].values.tolist()
calculate_share(list_sol_dm)

# Hosting Concentration
df_sol_ho = pd.read_csv('data/2_Hosting_concentration/Solana_hosting.csv', header=0, sep=';')
list_sol_ho = df_sol_ho['No_Validators'].values.tolist()

# Geographical diversity
df_sol_geo = pd.read_csv('data/3_Geographical_diversity/Solana_Geo.csv', header=0, sep=';')
list_sol_geo = df_sol_geo['No_Validators'].values.tolist()

# Reference client contributions
df_sol_rcc = pd.read_csv('data/4_Reference_client_contributions/Solana_contributions.csv', header=0, sep=';')
list_sol_rcc = df_sol_rcc['Commits'].values.tolist()
calculate_share(list_sol_rcc)

# Improvement protocol
df_sol_ip = pd.read_csv('data/6_Improvement_protocol/Solana_improvement_proposals.csv', header=0, sep=';')
df_sol_ip_count = df_sol_ip['Author'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_sol_ip = df_sol_ip_count['counts'].values.tolist()
calculate_share(list_sol_ip)

# Owner control
list_sol_oc = [df_owner_control.iloc[2]['Supply'], df_owner_control.iloc[2]['Total_supply']]

# Exchange concentration
df_sol_ex = pd.read_csv('data/7_Exchange_concentration/Solana_exchanges.csv', header=0, sep=';', encoding='latin1')
list_sol_ex = df_sol_ex['Volume'].values.tolist()
calculate_share(list_sol_ex)

# ------------------------------------------
# ETHEREUM DATA
# ------------------------------------------

# Decision-making
df_eth_dm = pd.read_csv('data/1_Decision_making/Ethereum_decision_making.csv', header=0, sep=';', encoding='latin1')
list_eth_dm = df_eth_dm['Stake'].values.tolist()
calculate_share(list_eth_dm)
list_eth_dm.pop()
list_eth_dm = list_eth_dm + list(itertools.repeat(0.000154725, 175961))

# Hosting Concentration
df_eth_ho = pd.read_csv('data/2_Hosting_concentration/Ethereum_Hosting.csv', header=0, sep=';')
df_eth_ho_count = df_eth_ho['ISP'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_eth_ho = df_eth_ho_count['counts'].values.tolist()

# Geographical diversity
df_eth_geo = pd.read_csv('data/3_Geographical_diversity/Ethereum_Geo.csv', header=0, sep=';')
df_eth_geo_count = df_eth_geo['Country'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_eth_geo = df_eth_geo_count['counts'].values.tolist()

# Reference client contributions
df_eth_rcc = pd.read_csv('data/4_Reference_client_contributions/Ethereum_contributions.csv', header=0, sep=';')
list_eth_rcc = df_eth_rcc['Commits'].values.tolist()
calculate_share(list_eth_rcc)

# Improvement protocol
df_eth_ip = pd.read_csv('data/6_Improvement_protocol/Ethereum_improvement_proposals.csv', header=0, sep=';')
df_eth_ip_count = df_eth_ip['Author'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_eth_ip = df_eth_ip_count['counts'].values.tolist()
calculate_share(list_eth_ip)

# Owner control
list_eth_oc = [df_owner_control.iloc[3]['Supply'], df_owner_control.iloc[3]['Total_supply']]

# Exchange concentration
df_eth_ex = pd.read_csv('data/7_Exchange_concentration/Ethereum_exchanges.csv', header=0, sep=';', encoding='latin1')
list_eth_ex = df_eth_ex['Summe'].values.tolist()
calculate_share(list_eth_ex)

# ------------------------------------------
# AVALANCHE DATA
# ------------------------------------------

# Decision-making
df_ava_dm = pd.read_csv('data/1_Decision_making/Avalanche_decision_making.csv', header=0, sep=';', encoding='latin1')
list_ava_dm = df_ava_dm['Stake'].values.tolist()
calculate_share(list_ava_dm)

# Hosting Concentration
df_ava_ho = pd.read_csv('data/2_Hosting_concentration/Avalanche_hosting.csv', header=0, sep=';')
df_ava_ho_count = df_ava_ho['ISP'].value_counts().rename_axis('unique_values').reset_index(name='counts')
list_ava_ho = df_ava_ho_count['counts'].values.tolist()

# Geographical diversity
df_ava_geo = pd.read_csv('data/3_Geographical_diversity/Avalanche_Geo.csv', header=0, sep=';')
list_ava_geo = df_ava_geo['Nodes'].values.tolist()

# Reference client contributions
df_ava_rcc = pd.read_csv('data/4_Reference_client_contributions/Avalanche_contributions.csv', header=0, sep=';')
list_ava_rcc = df_ava_rcc['Commits'].values.tolist()
calculate_share(list_ava_rcc)

# Improvement protocol
df_ava_ip = pd.read_csv('data/6_Improvement_protocol/Avalanche_improvement_proposals.csv', header=0, sep=';')
list_ava_ip = df_ava_ip['Pull_requests'].values.tolist()
calculate_share(list_ava_ip)

# Owner control
list_ava_oc = [df_owner_control.iloc[4]['Supply'], df_owner_control.iloc[4]['Total_supply']]

# Exchange concentration
df_ava_ex = pd.read_csv('data/7_Exchange_concentration/Avalanche_exchanges.csv', header=0, sep=';', encoding='latin1')
list_ava_ex = df_ava_ex['Summe'].values.tolist()
calculate_share(list_ava_ex)
