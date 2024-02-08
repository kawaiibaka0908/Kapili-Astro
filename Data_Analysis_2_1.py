import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform

mass1_GW150914 = 36.0  
mass2_GW150914 = 29.0  
spin1z_GW150914 = 0.0  
delta_t_GW150914 = 1.0/4096  
f_lower_GW150914 = 20.0  

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
plt.legend()
plt.show()
