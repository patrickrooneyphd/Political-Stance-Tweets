# Some small, useful functions across notebooks

import os
import matplotlib.pyplot as plt

def set_project_root():
    current = os.getcwd()
    if "/notebooks" in current:
        os.chdir('..')
        root = os.getcwd()
        return root
    else: 
        return current

    
def change_dir(root, path_ext):
    """
    :param path_ext: the desired path within project root folder (e.g., src, data)
    """
    os.chdir(root)
    if not os.path.isdir(os.getcwd() + path_ext):
        os.makedirs(os.getcwd() + path_ext)
    new_dir = os.path.join(os.getcwd() + path_ext)
    os.chdir(new_dir)
    print('      ')
    print('New Working Directory: ~' + path_ext)

# Saving images
def save_image(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    ch_dir('/analysis/figures')
    if tight_layout:
        plt.tight_layout()
    plt.savefig(fig_id, format=fig_extension, dpi=resolution)
    os.chdir('..')
    ch_dir('/notebooks')

    
#Plotting Word clouds
def plot_cloud(wordcloud, title):
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.title(title, fontsize=24)
    plt.show() 
    print("  ")
    print("  ")

    