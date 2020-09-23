# Group 3 Team Library
# group3lib.py
# DSC630 Fall 2020 - Term Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the random seed
np.random.seed(3) 

def read_file():
    
    marketingDf = pd.read_csv("data/datasets_129450_309761_DirectMarketing.csv")
    return marketingDf

def create_scatterplots(data):
    
    plt.scatter(data.Salary,data.AmountSpent)
    plt.xlabel('Salary')
    plt.ylabel('Amount Spent');
    plt.title('Amount Spent vs. Salary')
    plt.show();
    
    plt.scatter(data.Catalogs,data.AmountSpent)
    plt.xlabel('Catalogs')
    plt.ylabel('Amount Spent');
    plt.title('Amount Spent vs. Catalogs')
    plt.show();
    
    plt.scatter(data.Catalogs,data.Salary)
    plt.xlabel('Catalogs')
    plt.ylabel('Salary');
    plt.title('Salary vs. Catalogs')
    plt.show();

