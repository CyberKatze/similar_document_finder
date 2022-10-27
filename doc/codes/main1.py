#! /usr/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt
from lcs import LCS, sim_rate, contain_rate, dist_finder


def plot_at_y(ax, arr, val, **kwargs):
    '''Plot 1-d scatter'''
    ax.plot(arr, np.zeros_like(arr) + val, 'x',color='green', **kwargs)
    ax.set_yticklabels([])


if __name__ == "__main__":
    # getting file names from Terminal args
    if len(sys.argv) >= 3:
        f_name1 = sys.argv[1]
        f_name2 = sys.argv[2]
    else:
        # default values of filenames
        f_name1 = 'text1.txt'
        f_name2 = 'text2.txt'
    
    #opening files
    with open(f_name1, 'r') as f1:
        with open(f_name2, 'r') as f2:
            # Read and split text to words
            t1 = f1.read().split()
            t2 = f2.read().split()

            lcs = LCS(t1, t2)
            sim = sim_rate(t1,t2,lcs)
            contain = contain_rate(t1, t2, lcs)

            print("Similarity Score: {:.2%}  \n"
                    "Inclusion Score: {:.2%}  \n"
                    "\nLCS Words: \n{}".format(sim, contain, ' '.join(lcs)))

            # Plotting distribution of LCS occurances in t1 and t2
            fig, (ax1, ax2) = plt.subplots(2)
            ax1.set_title("Text1 LCS occurance")
            ax2.set_title("Text2 LCS occurance")
            plot_at_y(ax1, dist_finder(t1, lcs), 0) 
            plot_at_y(ax2, dist_finder(t2, lcs), 0)
            plt.show()