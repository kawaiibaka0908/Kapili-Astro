#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:10:27 2024

@author: shivansh420
"""

import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform

# Define the parameters for GW150914
mass1_GW150914 = 36.0  # Mass of the first black hole in solar masses
mass2_GW150914 = 29.0  # Mass of the second black hole in solar masses
spin1z_GW150914 = 0.0  # Spin of the first black hole (assuming no spin for simplicity)
delta_t_GW150914 = 1.0/4096  # Time interval between data points (1 sample per 4096 Hz)
f_lower_GW150914 = 20.0  # Lower frequency cutoff for the waveform (in Hz)

# Generate the time-domain waveform for GW150914 using the IMRPhenomD approximant
hp_GW150914, _ = get_td_waveform(approximant='IMRPhenomD',
                                  mass1=mass1_GW150914,
                                  mass2=mass2_GW150914,
                                  spin1z=spin1z_GW150914,
                                  delta_t=delta_t_GW150914,
                                  f_lower=f_lower_GW150914)

# Plot the waveform
plt.plot(hp_GW150914.sample_times, hp_GW150914, label='GW150914 (IMRPhenomD)')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.xlim(-0.2, 0.05)  # Adjust x-axis limits to focus on a smaller time window around the merger time
plt.legend()
plt.show()
