# ==========================================
# Imports
# ==========================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# ==========================================
# Cumulating values of list
# ==========================================
def cumulate_list(cumulative_list):
    
    # Iterate through all elements of given list
    for i in range(1, len(cumulative_list)):
        
        # Sum element and previous element
        cumulative_list[i] = cumulative_list[i] + cumulative_list[i-1]

    return cumulative_list


# ==========================================
# Plotting of lorenz curve and nakamoto coefficient
# ==========================================
def plot_gini(plot_list, blockchain, parameter, x_name, y_name):

    # Sort items in ascending order
    plot_list.sort()

    # Cumulate list values for plotting
    cumulated_list = cumulate_list(plot_list)

    # Values for y-axis:
    y_pos = np.arange(len(cumulated_list))+1

    # Change color of bars if share is over 50%
    colors = ["lightsteelblue" if i < 49 else "orange" for i in cumulated_list]

    # Create bar chart and line of equality
    plt.bar(y_pos, cumulated_list, color=colors, width=2)
    # plt.bar(y_pos, cumulated_list, color=colors, width=300)
    plt.plot([0, len(cumulated_list)], [0, 100], 'r', linewidth=1)
    # plt.rcParams['figure.figsize'] = [70, 10]

    # Adding grid lines for y-axis
    plt.gca().yaxis.grid(True)

    # Definition of label ranges
    y_step = 10000

    if len(cumulated_list) < 50:
        y_step = 1
    elif len(cumulated_list) < 70:
        y_step = 5
    elif len(cumulated_list) < 120:
        y_step = 10
    elif len(cumulated_list) < 300:
        y_step = 20
    elif len(cumulated_list) < 500:
        y_step = 50
    elif len(cumulated_list) < 1000:
        y_step = 100
    elif len(cumulated_list) < 1300:
        y_step = 200
    elif len(cumulated_list) < 4000:
        y_step = 250

    # Formate axes
    plt.xticks(np.arange(len(cumulated_list)+1, step=y_step))
    plt.yticks(np.arange(101, step=10))
    plt.ylim(bottom=0)
    plt.xlim(left=0)

    # Axes labels
    plt.ylabel(y_name + ' (%)')
    plt.xlabel(x_name)

    # Export and show graphic
    plt.savefig(('figures/gini_plot_' + blockchain + '_' + parameter + '_' + x_name.replace(" ", "").lower() + '_' + y_name.replace(" ", "").lower() + '.png'))
    plt.show()

    # Clear current plot
    plt.clf()
    plt.close()


# ==========================================
# Calculation of normalized Gini coefficient
# ==========================================
def calculate_gini(gini_list):

    gini_list.sort()

    # Initialize variables for calculation
    counter = 0
    denominator = 0

    # Iterate through all elements of given list
    for i in range(0, len(gini_list)):

        # Sum values according to Gini coefficient formula
        counter = counter + (i + 1) * gini_list[i]

    # Calculate final value of counter
    counter = counter * 2

    # Iterate through all elements of given list
    for i in range(0, len(gini_list)):

        # Sum values of given list
        denominator = denominator + gini_list[i]

    # Calculate finale value of denominator
    denominator = denominator * len(gini_list)

    # Calculate gini coefficient
    gini = (counter / denominator) - ((len(gini_list) + 1) / len(gini_list))

    # Normalize gini coefficient
    gini_normalized = gini * (len(gini_list) / (len(gini_list) - 1))

    # Reciprocal of gini coefficient
    gini_normalized = 1 - gini_normalized

    return gini_normalized
