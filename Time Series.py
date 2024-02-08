#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:30:50 2024

@author: shivansh420
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the given URL
data_url = "https://raw.githubusercontent.com/SAURABH-RAI1729/KRITIGW/main/GW150914_strain_data_final.txt"
data = pd.read_csv(data_url, sep="\s+", header=None, names=['Time', 'Strain'])

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Strain'], label='Gravitational Strain', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.title('Time-Series Plot of Gravitational Strain')
plt.legend()
plt.grid(True)
plt.show()
