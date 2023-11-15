# ==========================================
# Imports
# ==========================================
import copy

from data_import import *
from global_clustering_coefficient import *
from gini_coefficient import *
from shannon_index import *
from geographical_diversity_index import *
from fractional_owner_index import *
import networkx as nx


# ==========================================
# Style for console output
# ==========================================
def esc(code):
    return f'\033[{code}m'
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences


def calculate_rapado_scenarios(scenario, decision_making, geo_diversity, owner_control, network_top, hosting):

    res_decision_making = calculate_gini(copy.deepcopy(decision_making))
    res_geo_diversity = normalize_geographical_diversity_index(copy.deepcopy(geo_diversity))
    res_owner_control = owner_control
    res_network_top = calculate_gcc(network_top)
    res_hosting = calculate_shannon_index(copy.deepcopy(hosting))

    # ------------------------------------------
    # Calculate overall DECENTRALIZATION DEGREE
    rapado_decentralization = (10 * res_decision_making +
                               5 * res_hosting +
                               7 * res_geo_diversity +
                               6 * res_owner_control +
                               8 * res_network_top) / 36

    # ------------------------------------------
    # Console output
    print("")
    print("RAPADO scenario ", scenario, " results:")
    print(esc('32'), "Decision making:                  ", esc('34'), round(res_decision_making, 4))
    print(esc('32'), "Network topology:                 ", esc('34'), round(res_network_top, 4))
    print(esc('32'), "Hosting concentration:            ", esc('34'), round(res_hosting, 4))
    print(esc('32'), "Geographical diversity:           ", esc('34'), round(res_geo_diversity, 4))
    print(esc('32'), "Owner control:                    ", esc('34'), round(res_owner_control, 4))
    print(esc('0;1'), "------------------------------------------")
    print(esc('32;1'), "Overall decentralization degree:  ", esc('34'), round(rapado_decentralization, 4), esc('0'))


# ==========================================
# Calculate RAPADO score
# ==========================================
def rapado_implications():

    # ------------------------------------------
    # Graph generation

    # Graph of Scenario A
    a_edge_list = [(1, 2), (1, 3), (1, 6), (2, 3), (2, 4), (3, 8), (4, 7), (4, 9), (5, 7), (5, 10), (5, 6), (6, 10), (7, 8), (8, 9), (9, 10)]
    a_network_top = nx.Graph()
    a_network_top.add_edges_from(a_edge_list)

    # Graph of Scenario B
    b_edge_list = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 7), (3, 6), (4, 5), (4, 8), (5, 6), (6, 8), (7, 8), (7, 9), (8, 10), (9, 10)]
    b_network_top = nx.Graph()
    b_network_top.add_edges_from(b_edge_list)

    # Graph of Scenario C
    c_edge_list = [(1, 3), (1, 10), (2, 4), (2, 6), (2, 10), (3, 5), (4, 8), (5, 6), (5, 7), (6, 9), (7, 8), (8, 9), (9, 10)]
    c_network_top = nx.Graph()
    c_network_top.add_edges_from(c_edge_list)

    # ------------------------------------------
    # Data definition Scenario A
    a_decision_making = [5, 5, 5, 5, 10, 10, 10, 15, 15, 20]
    a_geo_diversity = [1, 2, 2, 2, 3]
    a_owner_control = 0.97
    a_hosting = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # ------------------------------------------
    # Data definition Scenario B
    b_decision_making = [5, 5, 5, 5, 5, 5, 5, 5, 5, 55]
    b_geo_diversity = [10]
    b_owner_control = 0.95
    b_hosting = [3, 3, 4]

    # ------------------------------------------
    # Data definition Scenario C
    c_decision_making = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    c_geo_diversity = [2, 4, 4]
    c_owner_control = 1
    c_hosting = [1, 1, 1, 1, 1, 1, 4]

    # ------------------------------------------
    # Calculation of decentralization degree for scenarios
    calculate_rapado_scenarios("A", a_decision_making, a_geo_diversity, a_owner_control, a_network_top, a_hosting)
    calculate_rapado_scenarios("B", b_decision_making, b_geo_diversity, b_owner_control, b_network_top, b_hosting)
    calculate_rapado_scenarios("C", c_decision_making, c_geo_diversity, c_owner_control, c_network_top, c_hosting)


# ==========================================
# Calculate overall decentralization degree
# ==========================================
def calculate_decentralization_degree(blockchain_name, hashPower_list, hosting_list, geo_list, exchange_list, contributions_list, owner_list, improvement_protocol_list):

    # ------------------------------------------
    # Plot and calculate parameter DECISION MAKING
    plot_gini(copy.deepcopy(hashPower_list), blockchain_name, 'Decision_making', 'Miner_Pools', 'Power')
    gini_hash_power = calculate_gini(copy.deepcopy(hashPower_list))

    # ------------------------------------------
    # Calculate parameter NETWORK TOPOLOGY
    # gcc_network_topology = calculate_gcc(gr)

    # ------------------------------------------
    # Calculate parameter HOSTING CONCENTRATION
    shannon_hosting = calculate_shannon_index(copy.deepcopy(hosting_list))

    # ------------------------------------------
    # Plot and calculate parameter GEOGRAPHICAL DIVERSITY
    index_geo_diversity = normalize_geographical_diversity_index(copy.deepcopy(geo_list))
    # plot_geographical_diversity(geo_list)

    # ------------------------------------------
    # Calculate parameter EXCHANGE CONCENTRATION
    gini_exchange_concentration = calculate_gini(copy.deepcopy(exchange_list))
    plot_gini(copy.deepcopy(exchange_list), blockchain_name, 'Exchange_concentration', 'Exchanges', 'Volume')

    # ------------------------------------------
    # Plot and calculate parameter REFERENCE CLIENT CONCENTRATION
    gini_reference_client = calculate_gini(copy.deepcopy(contributions_list))
    plot_gini(copy.deepcopy(contributions_list), blockchain_name, 'Reference_client_contributions', 'Contributors', 'Commits')

    # ------------------------------------------
    # Calculate parameter OWNER CONTROL
    fractional_index_owner_control = calculate_fractional_owner_index(owner_list)

    # ------------------------------------------
    # Calculate parameter IMPROVEMENT PROTOCOL
    gini_improvement_protocol = calculate_gini(copy.deepcopy(improvement_protocol_list))
    plot_gini(copy.deepcopy(improvement_protocol_list), blockchain_name, 'Improvement_protocol', 'Contributors', 'Proposals')

    # ------------------------------------------
    # Calculate overall DECENTRALIZATION DEGREE
    decentralization_degree = (10 * gini_hash_power +
                               5 * shannon_hosting +
                               7 * index_geo_diversity +
                               6 * gini_exchange_concentration +
                               5 * gini_reference_client +
                               6 * fractional_index_owner_control +
                               # 8 * gcc_network_topology +
                               6 * gini_improvement_protocol) / 45

    # ------------------------------------------
    # Console output
    print("")
    print(esc('32'), "Decision making:                  ", esc('34'), round(gini_hash_power, 4))
    # print(esc('32'), "Network topology:                 ", esc('34'), round(gcc_network_topology, 4))
    print(esc('32'), "Hosting concentration:            ", esc('34'), round(shannon_hosting, 4))
    print(esc('32'), "Geographical diversity:           ", esc('34'), round(index_geo_diversity, 4))
    print(esc('32'), "Exchange concentration:           ", esc('34'), round(gini_exchange_concentration, 4))
    print(esc('32'), "Reference client contribution:    ", esc('34'), round(gini_reference_client, 4))
    print(esc('32'), "Owner control:                    ", esc('34'), round(fractional_index_owner_control, 4))
    print(esc('32'), "Improvement protocol:             ", esc('34'), round(gini_improvement_protocol, 4))
    print(esc('0;1'), "------------------------------------------")
    print(esc('32;1'), "Overall decentralization degree:  ", esc('34'), round(decentralization_degree, 4), esc('0'))


# ==========================================
# Main
# ==========================================

# rapado_implications() # wieder rein machen

print('')
print('BITCOIN:')
# # Calculate BITCOIN decentralization degree:
calculate_decentralization_degree('Bitcoin',
                                  copy.deepcopy(list_btc_dm),
                                  copy.deepcopy(list_btc_ho),
                                  copy.deepcopy(list_btc_geo),
                                  copy.deepcopy(list_btc_ex),
                                  copy.deepcopy(list_btc_rcc),
                                  copy.deepcopy(list_btc_oc),
                                  copy.deepcopy(list_btc_ip))

print('')
print('CARDANO:')
# Calculate CARDANO decentralization degree:
calculate_decentralization_degree('Cardano',
                                  copy.deepcopy(list_car_dm),
                                  copy.deepcopy(list_car_ho),
                                  copy.deepcopy(list_car_geo),
                                  copy.deepcopy(list_car_ex),
                                  copy.deepcopy(list_car_rcc),
                                  copy.deepcopy(list_car_oc),
                                  copy.deepcopy(list_car_ip))

print('')
print('SOLANA:')
# Calculate SOLANA decentralization degree:
calculate_decentralization_degree('Solana',
                                  copy.deepcopy(list_sol_dm),
                                  copy.deepcopy(list_sol_ho),
                                  copy.deepcopy(list_sol_geo),
                                  copy.deepcopy(list_sol_ex),
                                  copy.deepcopy(list_sol_rcc),
                                  copy.deepcopy(list_sol_oc),
                                  copy.deepcopy(list_sol_ip))

print('')
print('ETHEREUM:')
# Calculate ETHEREUM decentralization degree:
calculate_decentralization_degree('Ethereum',
                                  copy.deepcopy(list_eth_dm),
                                  copy.deepcopy(list_eth_ho),
                                  copy.deepcopy(list_eth_geo),
                                  copy.deepcopy(list_eth_ex),
                                  copy.deepcopy(list_eth_rcc),
                                  copy.deepcopy(list_eth_oc),
                                  copy.deepcopy(list_eth_ip))

print('')
print('AVALANCHE:')
# Calculate ETHEREUM decentralization degree:
calculate_decentralization_degree('Avalanche',
                                  copy.deepcopy(list_ava_dm),
                                  copy.deepcopy(list_ava_ho),
                                  copy.deepcopy(list_ava_geo),
                                  copy.deepcopy(list_ava_ex),
                                  copy.deepcopy(list_ava_rcc),
                                  copy.deepcopy(list_ava_oc),
                                  copy.deepcopy(list_ava_ip))
