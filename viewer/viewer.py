import matplotlib.pyplot as plt
from matplotlib import colors  # For handling color maps and normalizations in plots
import numpy as np

colour_map = colors.ListedColormap(['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#B10DC9'])
norm = colors.Normalize(vmin=0, vmax=9)

colour_bar = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
# Sample Kaggle input data
data = {
    "00576224": {
        "test": [{"input": [[3, 2], [7, 8]]}],
        "train": [
            {
                "input": [[8, 6], [6, 4]],
                "output": [
                    [8, 6, 8, 6, 8, 6], 
                    [6, 4, 6, 4, 6, 4], 
                    [6, 8, 6, 8, 6, 8], 
                    [4, 6, 4, 6, 4, 6], 
                    [8, 6, 8, 6, 8, 6], 
                    [6, 4, 6, 4, 6, 4]
                ]
            },
            {
                "input": [[7, 9], [4, 3]],
                "output": [
                    [7, 9, 7, 9, 7, 9], 
                    [4, 3, 4, 3, 4, 3], 
                    [9, 7, 9, 7, 9, 7], 
                    [3, 4, 3, 4, 3, 4], 
                    [7, 9, 7, 9, 7, 9], 
                    [4, 3, 4, 3, 4, 3]
                ]
            }
        ]
    }
}

# Function to display grids in subplots and add color code key
def display_all_grids_with_key(data):
    # Count total number of grids (train input/output + test input)
    num_train_cases = len(data["train"])
    num_test_cases = len(data["test"])
    
    # Total number of subplots = train inputs + train outputs + test inputs + colur bar
    total_plots =1 +  (num_train_cases * 2 + num_test_cases)
    
    # Create the subplots figure
    fig, axs = plt.subplots(1, total_plots, figsize=(15, 5))
    fig.suptitle("Kaggle Data Visualization with Color Code", fontsize=16)

    # Track subplot index
    subplot_idx = 0
    
    # Loop over train cases
    for idx, train_case in enumerate(data["train"]):
        # Train input
        input_data = np.array(train_case['input'])
        im = axs[subplot_idx].imshow(input_data, cmap=colour_map, norm=norm)
        axs[subplot_idx].set_title(f"Train Input {idx+1}")
        axs[subplot_idx].set_xticks([])  # Remove x-axis ticks
        axs[subplot_idx].set_yticks([])  # Remove y-axis ticks
        subplot_idx += 1
        
        # Train output
        output_data = np.array(train_case['output'])
        im = axs[subplot_idx].imshow(output_data, cmap=colour_map, norm=norm)
        axs[subplot_idx].set_title(f"Train Output {idx+1}")
        axs[subplot_idx].set_xticks([])  # Remove x-axis ticks
        axs[subplot_idx].set_yticks([])  # Remove y-axis ticks
        subplot_idx += 1
    
    # Loop over test cases
    for idx, test_case in enumerate(data["test"]):
        # Test input
        input_data = np.array(test_case['input'])
        im = axs[subplot_idx].imshow(input_data, cmap=colour_map, norm=norm)
        axs[subplot_idx].set_title(f"Test Input {idx+1}")
        axs[subplot_idx].set_xticks([])  # Remove x-axis ticks
        axs[subplot_idx].set_yticks([])  # Remove y-axis ticks
        subplot_idx += 1

    # Add a color bar to display the color code for the grids

    output_data = np.array(colour_bar)
    im = axs[subplot_idx].imshow(output_data, cmap=colour_map, norm=norm)
    axs[subplot_idx].set_title("Key")
    axs[subplot_idx].set_xticks([])  # Remove x-axis ticks
    axs[subplot_idx].set_yticks([0,1,2,3,4,5,6,7,8,9])  
    subplot_idx += 1
    
    # cbar = fig.colorbar(im, ax=axs, orientation='vertical', fraction=0.02, pad=0.04)
    # cbar.set_label("Grid Value Color Code", fontsize=12)

    # Adjust layout to prevent overlap of titles and grids
    #plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    # Show the final plot
    plt.show()

# Call the function to display the grids
for task_id, task_data in data.items():
    display_all_grids_with_key(task_data)
