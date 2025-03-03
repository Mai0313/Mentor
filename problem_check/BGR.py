# ----- New Testbench: Temperature Sweep (Vdd fixed at 5V) -----
import numpy as np
# Define the temperature sweep (e.g., from 0°C to 100°C in steps of 10°C)
temperatures = np.linspace(0, 100, 11)
vout_values = []

# Perform operating point analysis for each temperature
for temp in temperatures:
    # Create a simulator instance with the current temperature
    simulator = circuit.simulator(temperature=temp, nominal_temperature=temp)
    analysis = simulator.operating_point()
    
    # Extract the Vout value at this temperature and store it
    vout = float(analysis['Vout'])
    vout_values.append(vout)

# Problem check criteria: Verify if the Bandgap reference output meets the expected criteria.
def check_bandgap_reference(vout_values):
    # Check if Vout is within an acceptable range (e.g., 1.2V ± 5%)
    target_voltage = 5
    tolerance = 0.05  # ±5%
    
    for vout in vout_values:
        if abs(vout - target_voltage) / target_voltage > tolerance:
            return False
    
    # Check if Vout is stable across temperature variations (allow ≤ 100mV variation)
    max_variation = max(vout_values) - min(vout_values)
    if max_variation > 0.1:  # 100mV
        return False
    
    return True

# Evaluate the circuit performance across the temperature sweep
if check_bandgap_reference(vout_values):
    print("Bandgap reference circuit passes the temperature sweep check.")
else:
    print("Bandgap reference circuit fails the temperature sweep check.")

# Print Vout values vs. Temperature for inspection
print("\nTemperature vs Vout values:")
for temp, vout in zip(temperatures, vout_values):
    print(f"Temperature = {temp:.1f}°C, Vout = {vout:.4f} V")