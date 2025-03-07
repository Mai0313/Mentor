### If the Task Type is `Opamp` or `Amplifier`, please refer the code below to verify your circuit.

```
import numpy as np
analysis = simulator.dc(V[IN_NAME]=slice(0, 5, 0.01))
with open("[DC_PATH]", "w") as fopen:
    out_voltage = np.array(analysis.Vout)
    in_voltage = np.array(analysis.V[IN_NAME])
    print("out_voltage: ", out_voltage)
    print("in_voltage: ", in_voltage)
    for item in in_voltage:
        fopen.write(f"{item:.4f}")
    fopen.write("\\n")
    for item in out_voltage:
        fopen.write(f"{item:.4f}")
    fopen.write("\\n")
```

### If the Circuit Type is not `Oscillator`, `Integrator`, `Differentiator`, `Adder`, `Subtractor`, `Schmitt`, or `BGR`, please follow the guidelines below to verify your circuit and ensure it meets the design requirements while avoiding common mistakes.

1. **Node Verification**:
   - **Input/Output Node Confirmation**: Ensure that all specified input and output nodes exist in your netlist. For example, if input node `Vin` and output node `Vout` are specified, please check whether they are correctly defined in the netlist.
   - **Consistency of Node Naming**: Check that the node names in the netlist match the required names exactly, avoiding case sensitivity issues or spelling errors.

2. **Operating Point (OP) Verification**:
   - **Voltage Source Settings**: Confirm that the voltage sources in the circuit (such as `Vdd`, `Vinp`, `Vinn`) are correctly set and comply with the circuit design requirements.
   - **Differential Input Voltages**: If the circuit is a differential design (e.g., a differential amplifier), ensure that the voltages of `Vinp` and `Vinn` are equal unless the design specifically requires a differential voltage.

3. **Component and Connection Verification**:
   - **Existence of Resistors**: In tasks that require a load resistor, check whether the netlist includes correctly connected resistor components.
   - **Miller Compensation Capacitor** (applicable to Task 9): Confirm that the Miller capacitor is correctly connected between the first stage output and the output node.
   - **Diode-Connected Load** (applicable to Task 10): Check whether the circuit includes a diode-connected load, such as by connecting the gate and drain of a MOSFET.
   - **Common Source/Gate/Drain Configurations**: According to the amplifier type, verify that the input and output nodes are connected to the correct terminals (Gate, Drain, Source) of the MOSFET. For example:
     - **Common-Gate Amplifier**: The input should be connected to the source, with the gate serving as the common node.
     - **Common-Drain Amplifier (Source Follower)**: The output should be taken from the source terminal.

4. **MOSFET Operating Region Verification**:
   - **NMOS Transistors**:
     - **V\_GS Verification**: Ensure the gate-source voltage `V_GS` is greater than the threshold voltage `V_TH` (`V_GS > V_TH`) to properly turn on the NMOS transistor.
     - **V\_DS Verification**: Confirm that the drain-source voltage `V_DS` is positive, and the drain voltage is higher than the source voltage (`V_D > V_S`).
     - **Connection Reasonableness**: Avoid connecting the drain of an NMOS transistor directly to ground.
   - **PMOS Transistors**:
     - **V\_SG Verification**: Ensure the source-gate voltage `V_SG` is greater than the threshold voltage `V_TH` (`V_SG > V_TH`), meaning the gate voltage is lower than the source voltage.
     - **V\_SD Verification**: Confirm that the source-drain voltage `V_SD` is positive, and the source voltage is higher than the drain voltage (`V_S > V_D`).
     - **Connection Reasonableness**: Avoid connecting the drain of a PMOS transistor directly to `Vdd`.

5. **Special Components and Configuration Verification**:
   - **Capacitor Connections**: Check that capacitor components are correctly connected, especially when compensation or AC bypass is required.
   - **Inductors and Other Components**: If the circuit involves inductors or other special components, ensure they meet the design requirements.

6. **Circuit Topology and Functionality Verification**:
   - **Overall Structure**: Confirm that the entire circuit structure aligns with the design objectives, avoiding unnecessary or missing components.
   - **Signal Path Check**: Verify the signal path to ensure the input signal can correctly influence the output.

7. **Simulation Setup and Result Verification**:
   - **Simulation Commands**: Ensure that you have used the correct SPICE simulation directives (e.g., `.OP`, `.DC`, `.AC`, `.TRAN`).
   - **Reasonableness of Results**: Run the simulation and check whether the results meet expectations, such as DC operating point voltages, current directions, gain, etc.
   - **Troubleshooting**: If simulation results are abnormal, check for issues like unconnected components, short circuits, or incorrect grounding.

8. **Model and Parameter Confirmation**:
   - **Component Models**: Verify that the component models used (such as `NMOS`, `PMOS`) are correct and that the model parameters meet the design requirements.
   - **Key Parameters**: Ensure that critical parameters like threshold voltage (`V_TH`), electron mobility, and others are reasonably set.

9. **File Format and Syntax Verification**:
   - **Netlist Syntax**: Ensure that the netlist syntax is correct, with no spelling errors, missing parameters, or incorrect node definitions.
   - **Line Formatting**: Check each line's format to ensure it complies with SPICE netlist syntax conventions.

10. **Suggestions and Corrections**:
    - **Addressing Issues**: If you find problems during the verification process, make adjustments based on the suggestions. For example, modify component parameters, reconnect nodes, or add necessary components.
    - **Re-simulation**: After making corrections, re-run the simulation to confirm that the issues have been resolved.

### If the Circuit Type is `CurrentMirror`, `Amplifier`, `Opamp` or `Inverter`, please follow the guidelines below to verify your circuit and ensure it meets the design requirements while avoiding common mistakes.

1. **Code Structure and Syntax:**

- **Correct File Formatting:**
  - Ensure that your code is properly formatted and saved with the correct file extension (e.g., `.py` for Python scripts).
  - Avoid syntax errors by checking for missing parentheses, colons, or indentation errors.

- **Executable Code:**
  - Your code should be executable as a standalone script.
  - Import all necessary modules and packages required for your code to run.

2. **Input Voltage Source Specification (For Amplifier and Opamp Tasks):**

- **Combined DC and AC Components:**
  - Define your input voltage source `Vin` with both DC and small-signal AC components to enable proper DC biasing and AC analysis.
  - **Example Syntax:**
    ```python
    circuit.V('Vin', 'vin', circuit.gnd, 'dc 1.0 ac 1u')
    ```
    - This specifies a DC voltage of `1.0V` and an AC small-signal amplitude of `1µV`.

- **Voltage Specification Consistency:**
  - Ensure that the voltage value is correctly specified and consistent throughout your code.
  - When modifying or specifying voltages, use precise and consistent units.

3. **Compatibility with Testing Scripts:**

- **Awareness of Test Integration:**
  - Your code will be combined with pre-written testing scripts specific to each task (e.g., `CurrentMirror.py`, `Amplifier.py`, `Opamp.py`, `Inverter.py`).
  - Avoid naming conflicts or redefining variables and functions that may interfere with the test scripts.

- **Modularity and Independence:**
  - Write your code in a way that it can be seamlessly integrated with other scripts.
  - Do not hard-code values or paths that might cause errors when your code is combined with the test scripts.

4. **Task-Specific Guidelines:**

- **Current Mirror Task:**
  - Ensure that your current mirror circuit is correctly implemented with proper connections and element values.
  - Verify that the mirroring action functions as intended, maintaining consistent current levels.

- **Amplifier and Opamp Tasks:**
  - Pay special attention to the input voltage source definition as mentioned above.
  - Ensure that your amplifier provides the correct gain and operates within the desired frequency range.
  - Check that biasing conditions are correctly set for all transistors.

- **Inverter Task:**
  - Confirm that your inverter circuit operates correctly, inverting the input signal as expected.
  - Verify the transfer characteristics and switching thresholds.

5. **Simulation and Verification:**

- **Running Simulations:**
  - After writing your code, run simulations to verify that your circuit behaves as expected.
  - Use appropriate simulation commands (e.g., `.dc`, `.ac`, `.tran`) to test different aspects of your circuit.

- **Analyzing Results:**
  - Examine simulation outputs such as voltage waveforms, current levels, and frequency responses.
  - Ensure that the outputs match theoretical predictions and design specifications.

6. **Error Checking and Debugging:**

- **Handling Execution Errors:**
  - If errors occur when running your code (e.g., syntax errors, exceptions), read the error messages carefully to identify the issue.
  - Common errors include undefined variables, incorrect function calls, or improper file paths.

- **Debugging Tips:**
  - Use print statements or debugging tools to monitor variable values and program flow.
  - Validate each part of your code incrementally to isolate and fix errors.

7. **Consistency and Naming Conventions:**

- **Node and Component Naming:**
  - Use consistent and clear names for nodes and components to enhance readability and maintainability.
  - Follow standard naming conventions (e.g., `Vdd` for supply voltage, `Vin` for input voltage).

- **Avoiding Case Sensitivity Issues:**
  - Remember that node names and component labels may be case-sensitive.
  - Ensure that you use the correct case consistently throughout your code.

8. **Code Comments and Documentation:**

- **Inline Comments:**
  - Include comments in your code to explain complex sections or important configurations.
  - This helps others (and yourself) understand the purpose and function of your code.

- **Documentation Strings:**
  - Use docstrings to provide descriptions for functions and classes.
  - This is especially helpful if your code will be used by others or integrated with additional scripts.

9. **Submission Guidelines:**

- **Complete Code Submission:**
  - Submit your entire code, including all necessary functions, classes, and definitions.
  - Ensure that no dependencies or external files are missing from your submission.

- **File Naming Conventions:**
  - Name your files appropriately, possibly including your name or student ID for identification.
  - Follow any specific file naming guidelines provided by your instructor.

10. **Final Checks Before Submission:**

- **Re-Run Your Code:**
  - After making any changes, run your code again to confirm that it executes successfully without errors.
  - Verify that all simulations complete and outputs are generated as expected.

- **Clean Up Code:**
  - Remove any unnecessary print statements or debugging code.
  - Ensure that your code is tidy and well-organized.

- **Ask for Help if Needed:**
  - If you encounter persistent issues that you cannot resolve, don't hesitate to reach out to your instructor or teaching assistant for assistance.
