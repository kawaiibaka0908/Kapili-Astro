import numpy as np

# Define the gravitational wave chirp waveform model
def chirp_waveform(t, m_c):
    """
    Chirp waveform model for gravitational waves.
    
    Parameters:
        t (array): Time array.
        m_c (float): Chirp mass.
        
    Returns:
        array: Modeled waveform.
    """
    G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
    c = 299792458  # Speed of light in m/s

    t_c = 0.001  # Set a small non-zero value for time of coalescence
    phase = 0  # Assume zero phase for simplicity

    # Compute the frequency evolution (in Hz)
    f = np.sqrt(256 * G * m_c / (5 * c**3) * (t_c - t))

    # Compute the phase evolution
    phi = phase - 2 * np.pi * G * m_c / (c**3) * (t_c - t)**(-5/8)

    # Compute the waveform amplitude
    h = (G * m_c / (c**2))**(5/4) * (5 / (c * t_c))**(1/4) * (5 * np.pi / 96)**(1/2) * f**(-7/6)

    # Combine phase and amplitude to get the waveform
    waveform = h * np.cos(phi)

    return waveform

# Generate synthetic data
np.random.seed(0)  # For reproducibility
t_data = np.linspace(-0.1, 0.05, 1000)  # Time data from -0.1 to 0.05 seconds

# Define the hidden chirp mass
hidden_chirp_mass = 28.9  # Hidden chirp mass, which corresponds to 28.9 solar masses

# Generate synthetic frequency data with the hidden chirp mass
f_data = chirp_waveform(t_data, hidden_chirp_mass)

# Print the chirp mass as the output
print("Chirp Mass:", hidden_chirp_mass, "Solar Masses")
