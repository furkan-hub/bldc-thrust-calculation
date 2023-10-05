import numpy as np
import matplotlib.pyplot as plt

# Motor and propeller parameters
motor_speed_rpm = 10000  # Motor speed (RPM)
propeller_diameter_m = 0.1  # Propeller diameter (meter)
air_speed_m_s = np.linspace(0.1, 100, 100)  # Airspeed range (0.1 to 100 m/s)
air_density_kg_m3 = 1.225  # Average air density (kg/m^3)

# Thrust calculation function
def calculate_thrust(speed_rpm, propeller_diameter_m, air_speed_m_s, air_density_kg_m3):
    speed_rad_s = speed_rpm * (2 * np.pi / 60)
    propeller_area_m2 = np.pi * (propeller_diameter_m / 2) ** 2
    
    # Prevent zero division error by checking airspeed
    thrust_coefficient = np.zeros_like(air_speed_m_s, dtype=float)
    valid_indices = air_speed_m_s > 0.0
    thrust_coefficient[valid_indices] = (2 * speed_rad_s ** 2 * propeller_area_m2) / (air_density_kg_m3 * air_speed_m_s[valid_indices] ** 2)
    
    thrust_N = thrust_coefficient * air_density_kg_m3 * propeller_area_m2 * air_speed_m_s ** 2
    return thrust_N

# Perform thrust calculations
thrust_values_N = calculate_thrust(motor_speed_rpm, propeller_diameter_m, air_speed_m_s, air_density_kg_m3)

# Display the results in a graph
plt.figure(figsize=(8, 6))
plt.plot(air_speed_m_s, thrust_values_N)
plt.xlabel('Air Speed (m/s)')
plt.ylabel('Thrust (N)')
plt.title('Propeller Thrust Calculation')
plt.grid(True)
plt.show()
