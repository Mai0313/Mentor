# **Bandgap Reference Verification**

**Rapid Adoption Kit (RAK)**

Product Version: IC6.1.8 ISR21, Spectre20.1 ISR10 December 2021

#### Copyright Statement

© 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Cadence and the Cadence logo are registered trademarks of Cadence Design Systems, Inc. All others are the property of their respective holders.

# **Contents**

| Purpose4                     |
|------------------------------|
| Audience4                    |
| Tool Versions4               |
| Overview4                    |
| Setting Up the RAK Database5 |
| 6                            |
| 30                           |
| 41                           |
| Measurement of Bandgap51     |
| 59                           |
| Supports59                   |
| 59                           |
|                              |

### <span id="page-3-0"></span>**Purpose**

This RAK introduces Bandgap Reference Voltage supply variation across PVT corners, PSRR, Stability, and Transient Noise setup examples. The document helps understand the usage of dc/dc with temperature sweep, ac, stb, and transient noise analysis to measure the various Bandgap design specifications based on different testbench setups.

### <span id="page-3-1"></span>**Audience**

This RAK is intended for ADE Explorer and Spectre users who want to measure Bandgap variations, Stability, PSRR, and Transient Noise of a Bandgap.

## <span id="page-3-2"></span>**Tool Versions**

This RAK has been verified using IC 6.1.8 ISR21 and Spectre20.1 ISR10 with Spectre/SpectreX Mode.

### <span id="page-3-3"></span>**Overview**

### **1.1 Design Example**

Bandgap references (BGR) are fundamental circuits, which are used to provide reference supply that has little dependence on temperature (temperature independent).

You can generate a temperature-independent quantity (Voltage and Current) by summation of Negative-temperature coefficient quantity and Positive-temperature coefficient quantity.

It has been implemented using the Cadence generic PDK 45nm CMOS process.

The key analog components of the BGR are the Positive-temperature coefficient and Negative-temperature coefficient generation with BJT used as diode, OpAmp, and startup circuit.

### **1.2 Lab Overview**

BGRs are fundamental circuits that are used to provide reference supply (temperature independent) in integrated circuits.

The Bandgap circuit used in this RAK is based on the voltage summing topology.

• Temperature sweep analysis determines temperature variations on the output reference supply.

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 4

- Loop gain and phase determine whether a negative-feedback loop of a BGR is stable.
- PSRR is a measure of the influence of power supply ripple on the BGR output voltage.
- Generally, several devices contribute towards the noise in a BGR circuit. Transient noise calculates the effects of large signals on virtually any system. It also determines the impact of noise in the time domain.

This RAK consists of examples on the following topics:

- Measurement of temperature variation using dc sweep analysis
- PSRR of a BGR using ac analysis
- Loop gain and phase margin of a BGR using stability analysis
- Large signal noise of a BGR using transient noise analysis

### <span id="page-4-0"></span>**Setting Up the RAK Database**

Action 1: Unzip and untar the TB\_BGR.tar.gz database.

Unix> tar -zxvf TB\_BGR.tar.gz

Action 2: Navigate to the TB\_BGR directory.

Unix> cd TB\_BGR

### <span id="page-5-0"></span>**Lab 1: Output Variation Measurements Using DC Analysis**

- DC analysis (temperature sweep) is used to measure the BGR output variation and accuracy (V/°C).
- DC analysis finds the DC operating-point or DC transfer curves of the circuit. To generate transfer curves, specify a parameter and a sweep range.
- Circuit temperature is used as a swept parameter.

Action 1: Invoke **Virtuoso**.

Unix> virtuoso &

- Action 2: Open the Library Manager from the CIW window by navigating to **Tools > Library Manager**.
- Action 3: From the Library Manager, open the **TB\_BGR > tb\_bgr > schematic** view.

Here is the image describtion:
```
The image shows a schematic diagram of an electronic circuit, likely designed using a circuit design software. The diagram is displayed on a grid background, which is typical for such software to help with component placement and alignment.

### Components and Connections:
1. **Voltage Sources:**
   - There are two voltage sources labeled `V7` and `V3`.
   - `V7` is set to `vdc=avdd` with an AC magnitude of 1 (`ac=1`).
   - `V3` is set to `vdc=avss`.

2. **Current Sources:**
   - There are two current sources within the green box labeled `BGR Circuit`.
   - These current sources are connected to resistors.

3. **Resistors:**
   - There are several resistors in the circuit, both inside and outside the `BGR Circuit` box.
   - The resistors inside the `BGR Circuit` are connected in a specific configuration, likely forming a voltage divider or a biasing network.

4. **Nodes and Labels:**
   - The nodes are labeled with identifiers such as `PPA`, `PPA`, `V_BGR`, and `V_BGR`.
   - The node `PPA` is connected to the positive terminal of `V7` and the top of the `BGR Circuit`.
   - The node `V_BGR` is connected to the right side of the `BGR Circuit` and extends to a capacitor labeled `C8`.

5. **Capacitor:**
   - There is a capacitor labeled `C8` connected to the `V_BGR` node and ground.

6. **Ground Connections:**
   - The circuit has multiple ground connections, indicated by the ground symbols.
   - The ground connections are used to complete the circuit and provide a common reference point.

7. **BGR Circuit:**
   - The green box labeled `BGR Circuit` likely stands for Bandgap Reference Circuit, which is commonly used to provide a stable reference voltage that is independent of temperature and supply voltage variations.
   - The circuit inside the `BGR Circuit` box includes transistors and resistors arranged in a specific configuration to achieve the desired reference voltage.

### Summary:
The schematic diagram represents a circuit with voltage sources, current sources, resistors, and a capacitor. The central part of the circuit is the `BGR Circuit`, which is likely a Bandgap Reference Circuit designed to provide a stable reference voltage. The connections and components are arranged to achieve the desired electrical characteristics, with labeled nodes and ground connections to complete the circuit.
```

Here is the image describtion:
```
The image is a caption for a figure in a document or presentation. The caption reads "Figure 1: Bandgap testbench schematic." The text is in a bold font, indicating that it is a title or heading for the figure it describes. The figure itself is not visible in the image, so no details about the schematic can be provided. The caption suggests that the figure is a schematic diagram related to a bandgap testbench, which is likely a circuit or setup used to test or demonstrate the properties of a bandgap reference in electronics.
```

- Action 4: From the schematic, select **Launch > ADE Explorer**.
- Action 5: In the **Launch ADE Explorer** window, select **Create New View** and click **OK**.

| Launch ADE Explorer                   | 1 |
|---------------------------------------|---|
| ADE Explorer                          |   |
| Create New View! O Open Existing View |   |
| Help<br>OK<br>Cancel                  |   |

**Figure 2: Launching ADE Explorer from schematic window**

Action 6: In the **Create new ADE Explorer view** window, select **Library > TB\_BGR**, **Cell > tb\_bgr**. Type the view as maestro\_Dc and click **OK**.

| Library           | TB BGR                                              |
|-------------------|-----------------------------------------------------|
| Cell              | tb_bgr                                              |
| View              | maestro_Dc                                          |
| lype              | maestro                                             |
| Application       |                                                     |
| Open with         | ADE Explorer                                        |
|                   | _ Always use this application for this type of file |
| Library path file |                                                     |
|                   | I/BGR_Verification_Workshop/cds . lib               |
|                   | Open in new tab current tab O new window            |

**Figure 3: Opening maestro\_Dc view of tb\_bgr cell** 

The **ADE Explorer** window opens as shown in Figure 4.

| Ci                                                                                                                                                                                                                                                                                                       | Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr maestro_Dc                                                          | ×■×                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------|
|                                                                                                                                                                                                                                                                                                          | cadence<br>Launch Session Setup Analyses Variables Outputs Simulation Results Tools EAD Parastics/LDE Window Help |                                          |
| 奥德 德 27 %                                                                                                                                                                                                                                                                                                | Co Replace (None) (None) 7                                                                                        |                                          |
| 3 円×<br>Setup                                                                                                                                                                                                                                                                                            | # tb_bgr x   = maestro_Dc X                                                                                       |                                          |
| Name<br>Value<br>▶<br>▼ Filter<br>Filter<br>TB_BGR_tb_bgr_1<br>Simulator spectre<br>Analyses<br>Click to add analysis<br>Design Variables<br>Click to add variable<br>Parameters<br>ਦਿ<br>><br>Corners<br>><br>F<br>Reliability Analyses<br>+<br>Monte Carlo Sampling<br>ಿ<br>Checks/Asserts<br>4<br>120 | Name<br>Details<br>Type<br>пиц.                                                                                   | ရှိ AC  ဝိပ်လ   ဝိပ်လ<br>न<br>▼ × な<br>* |
| limouse L:<br>1(3)                                                                                                                                                                                                                                                                                       | M:                                                                                                                | R:                                       |
|                                                                                                                                                                                                                                                                                                          | TB_BGR tb_bgr schematic   Simulator: spectre aps                                                                  |                                          |

**Figure 4: ADE Explorer window showing maestro\_Dc view of tb\_bgr cell** 

Action 7: In the **ADE Explorer** window**,** select **Setup > Model Libraries** as shown in Figure 5.

Here is the image describtion:
```
The image shows a screenshot of the Cadence Virtuoso ADE Explorer software interface, specifically in the context of editing a project named "TB_BGR tb_bgr maestro_Dc." The interface is divided into several sections and menus.

1. **Top Menu Bar**: 
   - The topmost part of the interface contains a menu bar with options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.
   - The "Setup" menu is currently expanded, displaying a dropdown list of options.

2. **Setup Menu**:
   - The expanded "Setup" menu includes the following options:
     - Job Setup...
     - Design...
     - Simulator...
     - Save Options...
     - High-Performance Simulation...
     - Model Libraries... (highlighted in yellow)
     - Temperature...
     - Stimuli...
     - Simulation Files...
     - EM/IR Analysis...
     - MATLAB/Simulink
     - Environment...

3. **Main Toolbar**:
   - Below the menu bar, there is a toolbar with various icons and options.
   - There is a search bar with the placeholder text "Replace" and a dropdown menu labeled "(None)".
   - To the right of the search bar, there are icons for different functions, including a folder icon, a red arrow, and a yellow pencil.

4. **Left Sidebar**:
   - The left sidebar contains a section labeled "Setup" with a list of items such as Parameters, Corners, Reliability Analysis, Monte Carlo, and Checks/Asserts.
   - The item "TB_BGR_tb_bgr" is selected, and there are icons indicating different statuses or actions next to each item.

5. **Main Workspace**:
   - The main workspace area is mostly blank, with a tab labeled "maestro_Dc" open.
   - There is a "Details" column header, but no specific details are visible in the workspace.

6. **Right Sidebar**:
   - The right sidebar contains a few icons, including a pencil, a checkmark, a cross, a play button, and a waveform icon, which likely represent different actions or tools available for use.

Overall, the image captures the user interface of the Cadence Virtuoso ADE Explorer software, highlighting the "Setup" menu and its options, with a focus on the "Model Libraries..." option.
```

 **Figure 5: Opening Model Library Setup form from ADE Explorer window**

The **Model Library Setup** form opens as shown in Figure 6.

Action 8: Browse the **gpdk045.scs** model file in the **Model File** section.

Action 9: Set the **Section** to **tt** in the **Model Library Setup** form. Then, click **OK**.

| spectre0: Model Library Setup             |                           |  |
|-------------------------------------------|---------------------------|--|
| Model File                                | Section                   |  |
| E-Global Model Files                      |                           |  |
| /gpdk045_v_3_5/models/spectre/gpdk045.scs | itt                       |  |
| { < Click here to add model file>         |                           |  |
|                                           |                           |  |
|                                           |                           |  |
|                                           |                           |  |
|                                           |                           |  |
|                                           | Cancel Apply   Help<br>OK |  |

**Figure 6: Set model file in Model Library Setup form**

Action 10: In the ADE Explorer **Setup** assistant, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a setup window for a simulation tool. The window is titled "Setup" and contains a hierarchical tree structure with various options and settings for configuring a simulation.

Here is a detailed description of the elements in the image:

1. **Title Bar**: The top of the window has a title bar with the label "Setup" and a help icon (a question mark inside a circle) on the right side.

2. **Tree Structure**: The main part of the window displays a tree structure with expandable and collapsible nodes. Each node has an icon and a label. The nodes are as follows:
   - **TB_BGR_tb_bgr_1**: This is the root node, indicated by an upward arrow icon.
   - **Simulator spectre**: This node has a green icon with a gear and a waveform, indicating the simulator being used is "spectre."
   - **Analyses**: This node has a green icon with a gear and a magnifying glass. It is expandable, and currently, it shows a sub-item labeled "Click to add analysis" highlighted in yellow.
   - **Design Variables**: This node has a red icon with a gear and a pencil. It is expandable, and currently, it shows a sub-item labeled "Click to add variable."
   - **Parameters**: This node has a red icon with a gear and a checkmark, indicating that parameters are selected.
   - **Corners**: This node has a red icon with a gear and a document, indicating that corner analysis is selected.
   - **Reliability Analyses**: This node has a green icon with a gear and a clock. It is not expanded.
   - **Monte Carlo Sampling**: This node has a green icon with a gear and a dice, indicating Monte Carlo sampling options.
   - **Checks/Asserts**: This node has a red icon with a gear and a checkmark. It is not expanded.

3. **Columns**: The tree structure is divided into two columns:
   - **Name**: This column lists the names of the nodes and sub-items.
   - **Value**: This column is currently empty, but it is intended to display the values or settings associated with each node.

4. **Filter Options**: At the top of each column, there are filter options indicated by red downward arrows, allowing the user to filter the items in the tree structure.

Overall, the image shows a setup interface for configuring a simulation, with various options for analyses, design variables, parameters, corners, reliability analyses, Monte Carlo sampling, and checks/asserts.
```

**Figure 7: Opening 'Analyses' form from 'Click to add analysis'**

Action 11: In the **Choosing Analyses** form, select the **dc** analysis with the following setup. Then, click **OK**:

- Enable **Save DC Operating Point**.
- Select **Sweep Variable** as **Temperature**.
- For **Sweep Range**, set **Start** to **-40** and **Stop** to **120**.
- Choose **Linear** for **Sweep Type** with step size of **10**.

|                     |                         |             | Choosing Analyses -- ADE Explorer | ×          |
|---------------------|-------------------------|-------------|-----------------------------------|------------|
| Analysis            | C tran                  | O dc        | ac                                | noise<br>D |
|                     | xf                      | sens        | dcmatch O                         | acmatch    |
|                     | stb                     | pz          | If                                | Sp         |
|                     | envip                   | bss         | pac                               | pstb       |
|                     | pnoise                  | D<br>pxf    | psp                               | dbss       |
|                     | qpac                    | qpnoise     | qpxf<br>D                         | dbsp       |
|                     | hb                      | hbac        | hbstb                             | hbnoise    |
|                     | hbsp                    | hbxf        |                                   |            |
|                     |                         | DC Analysis |                                   |            |
|                     | Save DC Operating Point | >           |                                   |            |
| Hysteresis Sweep    |                         |             |                                   |            |
|                     |                         |             |                                   |            |
| Sweep Variable      |                         |             |                                   |            |
|                     | Temperature             |             |                                   |            |
|                     | Design Variable         |             |                                   |            |
|                     | Component Parameter     |             |                                   |            |
|                     |                         |             |                                   |            |
|                     | Model Parameter         |             |                                   |            |
|                     |                         |             |                                   |            |
| Sweep Range         |                         |             |                                   |            |
| Start-Stop          |                         |             |                                   |            |
| Center-Span         |                         | Start -40   | Stop                              | 120        |
|                     |                         |             |                                   |            |
| Sweep Type          |                         |             |                                   | 10         |
|                     |                         | Step Size   |                                   |            |
| Linear              |                         |             | Number of Steps                   |            |
| Add Specific Points |                         |             |                                   |            |
| Add Points By File  |                         |             |                                   |            |
| Enabled<br>>        |                         |             |                                   | Options    |

 **Figure 8: Setup of DC-Sweep Analysis**

Action 12: In the **ADE Explorer** window, select **Outputs > Save All** as shown in Figure 9.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically for a test bench named "TB_BGR tb_bgr maestro_Dc" in the Cadence design environment. The interface is divided into several sections:

1. **Top Menu Bar**: 
   - The top menu bar includes options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.
   - The "Outputs" menu is currently expanded, showing options like Add, Delete, Import, Export, Send To Expression Editor, To Be Saved, To Be Plotted, and Save All. The "Save All" option is highlighted in yellow.

2. **Setup Panel (Left Side)**:
   - This panel lists the setup details for the test bench.
   - It includes the name of the test bench "TB_BGR_tb_bgr_1".
   - The simulator being used is "spectre".
   - Under "Analyses", there is a DC analysis named "dc" with a temperature range from -40 to 120 and an automatic start-stop feature.
   - There are sections for Design Variables, Parameters, Corners, Reliability Analyses, Monte Carlo Sampling, and Checks/Asserts, though these sections are not expanded.

3. **Main Workspace (Right Side)**:
   - The main workspace is currently empty, with no specific details or results displayed.
   - There are a few icons on the right side of the workspace, including options for details, a green play button (likely for running simulations), a brown stop button, and a waveform icon.

4. **Toolbar**:
   - The toolbar at the top of the workspace includes icons for various functions such as saving, opening, and other common actions.

Overall, the image shows a user interface for setting up and managing simulations in the Cadence Virtuoso ADE Explorer, with a focus on the outputs configuration.
```

Here is the image describtion:
```
The image is a screenshot of a figure caption. The caption reads "Figure 9: Options for saving outputs" in bold text. The font appears to be a standard sans-serif typeface, and the text is black on a white background. The caption suggests that it is part of a larger document, likely a report or a presentation, and it indicates that the figure associated with this caption provides information about different options available for saving outputs.
```

Action 13: Enable **all** for **Select device currents**. For **Select signals to output**, **allpub** will be enabled by default. Then, click **OK**.

|                                   | Save Options<br>X                           |                                                  |  |  |  |  |
|-----------------------------------|---------------------------------------------|--------------------------------------------------|--|--|--|--|
| Basic                             | Save By Subckt                              |                                                  |  |  |  |  |
|                                   | Save Options                                |                                                  |  |  |  |  |
|                                   | Select signals to output (save)             | _ none _ selected _ Ivipub         allpub  _ all |  |  |  |  |
|                                   | Select power signals to output (pwr)        | _ none _ total _ devices _ subckts _ all         |  |  |  |  |
|                                   | Set level of subcircuit to output (nestlyl) |                                                  |  |  |  |  |
| Select device currents (currents) |                                             | _ selected _ nonlinear y all   _ none            |  |  |  |  |
|                                   | Select AC terminal currents (useprobes)     | _ yes _ no                                       |  |  |  |  |
|                                   | Subcircuit Probe Level (subcktprobelvl)     |                                                  |  |  |  |  |
|                                   | Select AHDL variables (saveahdlvars)        | selected all                                     |  |  |  |  |
|                                   | Transient Time Window Options               |                                                  |  |  |  |  |
|                                   | Transient time window save options          | Time Setup                                       |  |  |  |  |
|                                   |                                             |                                                  |  |  |  |  |

#### **Figure 10: Setting save options**

Action 14: In the **ADE Explorer** window, click on **Variables** and select **Copy From Cellview** as shown in Figure 11.

Action 15: Set **avdd** to **2**.

Action 16: Set **avss** to **0**.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically for a test bench named "TB_BGR tb_bgr maestro_Dc" in the Cadence design environment. The interface is divided into several sections and menus.

1. **Top Menu Bar**: 
   - The top menu bar includes options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.
   - The "Variables" menu is currently open, showing options like Edit, Delete, Find, Copy From Cellview, and Copy To Cellview. The "Copy From Cellview" option is highlighted.

2. **Setup Section**:
   - On the left side, there is a "Setup" section with a hierarchical tree structure.
   - The tree includes:
     - **TB_BGR_tb_bgr_1**: The name of the test bench.
     - **Simulator**: The simulator being used is "spectre".
     - **Analyses**: Under this, there is a "dc" analysis with parameters t=-40 120 Automatic Start-Stop.
     - **Design Variables**: This section lists variables used in the design. Two variables are shown:
       - `avdd` with a value of 2 (highlighted in yellow).
       - `avss` with a value of 0 (highlighted in yellow).
     - **Parameters, Corners, Reliability Analyses, Monte Carlo Sampling, Checks/Asserts**: These sections are present but not expanded.

3. **Main Workspace**:
   - The main workspace on the right side is mostly empty, with a tab labeled "maestro_Dc".
   - There are options to "Replace" and a dropdown menu with "(None)" selected.
   - There are icons for various actions, such as saving, running simulations, and viewing results.

4. **Right Toolbar**:
   - The right side of the interface has a vertical toolbar with icons for different functions, including:
     - A green checkmark (possibly for validation or running checks).
     - A red cross (likely for stopping or canceling an action).
     - A green play button (for starting a simulation).
     - A brown square (possibly for stopping a simulation).
     - A waveform icon (likely for viewing simulation results).

Overall, the image shows a user interface for setting up and running simulations in the Cadence Virtuoso ADE Explorer, with a focus on managing design variables and analyses.
```

#### **Figure 11: Copying variables from cell view**

- Action 17: In the **ADE Explorer** window, click on the green arrow button to **netlist and run** the simulation.
- Action 18: In the **ADE Explorer** window, choose **Results > Direct Plot > Main Form** to open the **Direct Plot** form as shown in Figure 12.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from a tool used for electronic design automation (EDA). The title bar at the top indicates that the current project is "TB_BGR tb_bgr maestro_Dc."

The interface has a menu bar with several options: "Simulation," "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is expanded, showing a dropdown list of options. The highlighted option in this list is "Direct Plot," which is selected.

Upon selecting "Direct Plot," a side panel titled "Direct Plot" appears on the right side of the interface. This panel contains a list of various plotting options, which include:

1. Main Form ...
2. Transient Signal
3. Transient Minus DC
4. Transient Sum
5. Transient Difference
6. AC Magnitude
7. AC dB10
8. AC dB20
9. AC Phase
10. AC Magnitude & Phase
11. AC Gain & Phase
12. Equivalent Output Noise
13. Equivalent Input Noise
14. Squared Output Noise
15. Squared Input Noise
16. Noise Figure
17. DC

The options in the "Direct Plot" panel are likely used for different types of data visualization and analysis related to electronic circuit simulations. The interface appears to be part of a sophisticated tool used by engineers to analyze and visualize the performance of electronic circuits.
```

**Figure 12: Opening Direct Plot Form from ADE Explorer**

- Action 19: To plot BGR\_output, select **Voltage** as **Function**, **Net** as **Select** from the drop-down list.
- Action 20: Enable the **Add To Outputs** checkbox. Select the **V\_BGR** net from the schematic window.

|                                   | Direct Plot Form                 | 2 |
|-----------------------------------|----------------------------------|---|
| Plotting Mode<br>Analysis<br>O dc | Append                           |   |
| Function                          |                                  |   |
| 0<br>Voltage                      | Voltage Ratio                    |   |
| Current                           | Current Ratio                    |   |
| Power                             | Power Ratio                      |   |
|                                   | Transresistance Transconductance |   |
| Net<br>Select                     |                                  |   |
| ટી<br>Add To Outputs              |                                  |   |
| > Select Net on schematic         |                                  |   |
|                                   | Help<br>Close                    |   |

 **Figure 13: Direct Plot Form** 

The plot appears as shown in Figure 14. If the waveform is plotted in the docked VIVA

assistant within Explorer/Assembler, you can undock it by clicking on .

Action 21: Add a delta marker by hovering over the peak of the plot and pressing the **A** bindkey.

Action 22: Hover over the lowest part of the curve and press the **B** bindkey.

A delta marker will be added like the one shown below.

The v("/V\_BGR" ?result "dc") expression is also added to the **Outputs Setup** table in the **maestro\_Dc** view.

Here is the image describtion:
```
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL software, which is used for analyzing electronic circuits. The specific analysis shown is a DC response of a circuit, likely a bandgap reference (BGR) circuit, as indicated by the file name "TB_BGR_tb_bgr_1".

The main part of the image is a graph plotting voltage (V) on the y-axis against temperature (temp in °C) on the x-axis. The graph shows a parabolic curve, which is typical for a bandgap reference voltage versus temperature plot. The curve starts at around 1.17875V at -40°C, peaks at approximately 1.182303V at 40°C, and then decreases to about 1.178871V at 120°C.

Several markers and annotations are present on the graph:
1. A red marker labeled "A" at the peak of the curve, indicating the maximum voltage of 1.182303V at 40.0°C.
2. A blue marker labeled "B" at the right end of the curve, indicating a voltage of 1.178871V at 120.0°C.
3. A purple annotation showing the difference in voltage (dy) and temperature (dx) between the peak and the right end of the curve. It indicates a change of 80.0°C in temperature and a voltage change of 3.43138662mV, with a slope (s) of 42.8923327uV/°C.

The software interface includes various toolbars and menus:
- The top menu bar includes options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
- Below the menu bar, there are icons for different tools and settings, including options for subwindows, data points, and different graph styles.
- The left sidebar shows the "DC Response" section with a list of plotted variables, in this case, "v" representing the voltage of the bandgap reference.

The software window is titled "Virtuoso (R) Visualization & Analysis XL: TB_BGR tb_bgr maestro_Dc," indicating the specific tool and analysis being used. The Cadence logo is visible in the top right corner of the window.
```

**Figure 14: BGR output plot with temperature sweep DC analysis**

Action 23: Select the **/V\_BGR** plot on ViVA and click the calculator icon as shown in Figure 14.

The **ViVA calculator** window will open with the v("/V\_BGR" ?result "dc") expression as shown in Figure 15.

| Virtuoso (R) Visualization & Analysis XL calculator                                                                                                                                                      |  |  |  |  |  |  |  |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|
| File Tools View Options Constants Help                                                                                                                                                                   |  |  |  |  |  |  |  |  |  |
| In Context Results DB:<br>/TB_BGR/tb_bgr/maestro_Dc/results/maestro/ExplorerRun.0/1/TB_BGR_tb_bgr_1/psf                                                                                                  |  |  |  |  |  |  |  |  |  |
| app plot erplot   average cross dB20 sqrt ymax                                                                                                                                                           |  |  |  |  |  |  |  |  |  |
| Ovs O os O op O ot O mp<br>0<br>vf<br>Ovdc<br>Ovn<br>D<br>U zm<br>D<br>vt<br>sp<br>O vswr U hp<br>TB_BGR_tb_bgr_1<br>O it<br>O if   O idc<br>O var<br>0 vn2<br>O is<br>O opt<br>Uzp Uyp<br>Ogd<br>O data |  |  |  |  |  |  |  |  |  |
| ● Off ○ Family ○ Wave   Clip   - Append<br>7 366 日<br>▼ Rectangular                                                                                                                                      |  |  |  |  |  |  |  |  |  |
| ದಿಸ<br>Key P<br>v "/V_BGR" ?result "dc")<br>7<br>8<br>9                                                                                                                                                  |  |  |  |  |  |  |  |  |  |

**Figure 15: ViVA-XL calculator window**

Action 24: Select the **ymax** function from the **Functional Panel** window.

| Function Panel                                                                                         |                                                                              |                                                                                                                |                                                                                                    |                                                                                                 |                                                                       |                                                                                                                        |                                                     |  |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--|
| Special Functions<br>T fx                                                                              |                                                                              |                                                                                                                |                                                                                                    |                                                                                                 |                                                                       |                                                                                                                        |                                                     |  |
| PN<br>aaSP<br>abs_jitter<br>analog2Digital<br>average<br>bandwidth<br>busTransition<br>calcVal<br>clip | cross<br>d2a<br>dBm<br>delay<br>delayMeasure<br>deriv<br>dff<br>dftbb<br>dnl | eyeDiagram<br>eyeHeightAtXY<br>eyeWidthAtXY<br>fallTime<br>firstVal<br>flip<br>fourEval<br>freq<br>freq_jitter | getData<br>groupDelay<br>harmonic<br>harmonicFreq normalQQ<br>histogram2D<br>iinteg<br>in<br>integ | astval<br>loadpull<br>lshift<br>normalQQPValue pstddev<br>num Conv<br>overshoot<br>pavg<br>peak | pow<br>prms<br>psd<br>psdbb<br>pzbode<br>pzfilter<br>rise lime<br>rms | sample<br>settlingTime<br>skewness<br>slewRate<br>spectralPower<br>spectrumMeas ymax<br>stodev<br>swapSweep<br>tangent | value<br>waveVsWave<br>xmax<br>xmin<br>xval<br>ymin |  |
| compare<br>compression<br>compressionVRI<br>convolve                                                   | dutyCycle<br>evmQAM<br>evmQpsk<br>eyeAperture                                | frequency<br>gainBwProd<br>gainMargin<br>getAsciiWave                                                          | intersect<br>ipn<br>ipnVRI<br>kurtosis                                                             | peakToPeak<br>period_jitter<br>phaseMargin<br>phaseNoise                                        | rmsNoise<br>root<br>rshift                                            | thd<br>rms_jitter triggeredDelay<br>unityGainFreq<br>V                                                                 |                                                     |  |

#### **Figure 16: Functional Panel of ViVA-XL calculator**

The expression will become ymax(v("/V\_BGR" ?result "dc")) as shown in Figure 17.

Action 25: In the **ViVA calculator** window, click on the **Send buffer expression to ADE output** icon .

The expression is added to the **ADE Output Setup** table.

Here is the image describtion:
```
The image shows a screenshot of a software interface, likely related to data analysis or signal processing. Here are the details:

1. **Top Toolbar**:
   - There are several buttons and options in the top toolbar.
   - From left to right, the first button is a red circle labeled "Off".
   - Next, there are three radio buttons labeled "Family", "Wave", and "Clip", with "Clip" being checked.
   - Following these, there is a button with a grid icon.
   - Then, there is a button with a green arrow pointing to the right, labeled "Append".
   - Next to it, there is a dropdown menu set to "Rectangular".
   - Finally, there is a gear icon button highlighted with a red box around it, indicating it is likely the settings or configuration button.

2. **Text Box**:
   - Below the toolbar, there is a text box with some code written in it.
   - The code reads: `ymax(v("V_BGR"?result "dc"))`
   - The text is color-coded, with "ymax" in blue, `v("V_BGR"?result "dc")` in green, and the rest in black.

3. **Key Pad**:
   - On the left side of the interface, there is a small keypad with buttons labeled 7, 8, 9, and a division symbol (/).
   - The keypad is labeled "Key P..." at the top, which is likely short for "Key Pad".

The overall interface appears to be part of a specialized software tool, possibly for scientific or engineering purposes, where users can input and manipulate data or signals.
```

**Figure 17: ViVA-XL calculator buffer**

Action 26: Repeat this to add the following expression to the **ADE Output Setup** table:

ymin(v("/V\_BGR" ?result "dc"))

|                | · Off O Family O Wave   Clip   Append | Rectangular<br>> | 费目 |
|----------------|---------------------------------------|------------------|----|
| Key P          | BX   ymin v("/V_BGR" ?result "dc")    |                  |    |
| 79<br>8<br>9 / |                                       |                  |    |

**Figure 18: ViVA-XL calculator buffer**

Action 27: In the **ViVA calculator** window, write the following expression:

```
ymax(v("/V_BGR" ?result "dc")) - ymin(v("/V_BGR" ?result 
"dc"))
```
Action 28: Add this expression in the **ADE maestro** view using the **Send buffer expression to ADE output** icon.

Action 29: Evaluate the expression value using the **Evaluate the buffer** icon.

|   |               |   | · Off O Family C Wave & Clip   Append |                                                                     | ▼ Rectangular | 1 |
|---|---------------|---|---------------------------------------|---------------------------------------------------------------------|---------------|---|
| 7 | Key P  .<br>8 | 9 |                                       | (0)X] ymax(v("/V_BGR" ?result "dc"))-ymin(v("/V_BGR" ?result "dc")) |               |   |

#### **Figure 19: ViVA-XL calculator buffer**

Action 30: In the **ADE Explorer** window, double-click on the **Name** column for the v("/V\_BGR" ?result "dc") expression and type in the name BGR\_output as shown in Figure 20.

Action 31: Similarly, add the name BGR\_variation for the last expression.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer, a tool used for analog and mixed-signal design and simulation, specifically showing a setup for a testbench named "TB_BGR_tb_bgr_1". The interface is divided into two main sections: the left panel and the right panel.

### Left Panel:
- **Header**: The header of the left panel shows the hierarchy of the setup, starting with "TB_BGR_tb_bgr_1".
- **Simulator**: The simulator being used is "spectre".
- **Analyses**: The analysis type selected is "dc" with a temperature sweep from -40 to 120 degrees Celsius in 10-degree steps.
- **Design Variables**: Two design variables are listed:
  - `avdd` with a value of 2.
  - `avss` with a value of 0.
- **Parameters**: This section is checked but not expanded, so no details are visible.
- **Corners**: This section is checked but not expanded, so no details are visible.
- **Reliability Analyses**: This section is checked and includes "Monte Carlo Sampling".
- **Checks/Asserts**: This section is checked but not expanded, so no details are visible.

### Right Panel:
- **Header**: The header of the right panel shows two tabs: "tb_bgr" and "maestro_Dc". The "maestro_Dc" tab is currently active.
- **Table**: The table in the right panel lists expressions and their details:
  - **BGR_output**:
    - **Name**: `BGR_output`
    - **Type**: `expr`
    - **Details**: `v("/V_BGR" ?result "dc")`
  - **BGR_variation**:
    - **Name**: `BGR_variation`
    - **Type**: `expr`
    - **Details**: `(ymax(v("/V_BGR" ?result "dc")) - ymin(v("/V_BGR" ?result "dc")))`

### Toolbar:
- The toolbar at the top includes various icons for launching, session management, setup, analyses, variables, outputs, simulation, results, tools, EAD, parasitics/LDE, window, and help.
- There is a search bar with the option to replace text and a dropdown menu for selecting different options.
- Additional icons for saving, opening, and other file operations are present.

### Additional Elements:
- On the right side of the interface, there are icons for AC, DC, and Transient analyses, as well as a green checkmark and a brown box, possibly indicating the status of the setup or simulation.

Overall, the image shows a detailed setup for a DC analysis of a bandgap reference (BGR) circuit, with specific expressions defined for output voltage and its variation across the temperature sweep.
```

**Figure 20: ADE maestro\_Dc view**

Action 32: Close the **ViVA** window.

Action 33: In the **ADE Explorer** window, click on the **Add outputs** icon and select **OP Parameters**.

Here is the image describtion:
```
The image shows a section of a graphical user interface (GUI) with a vertical toolbar on the left side and a dropdown menu on the right side. The toolbar contains several icons arranged vertically, each representing different functions or tools. Here is a detailed description of the elements:

1. **Toolbar Icons (from top to bottom):**
   - **First Icon:** A small image of a document with a pencil, likely representing a general editing or documentation tool.
   - **Second Icon:** A green icon with a wrench and screwdriver crossed, indicating settings or configuration options. This icon is highlighted, suggesting it is currently selected.
   - **Third Icon:** A brown "X" symbol, typically used for closing or deleting an item.
   - **Fourth Icon:** A green play button, commonly used to start or execute a process.
   - **Fifth Icon:** A brown square, which might represent a stop button or a different function.
   - **Sixth Icon:** A waveform or signal icon, possibly related to signal processing or analysis.

2. **Dropdown Menu (highlighted in red):**
   - The dropdown menu is displayed because the second icon (settings/configuration) is selected.
   - The menu contains the following options:
     - **Expression:** Represented by an "f0" symbol, likely used for mathematical or logical expressions.
     - **Signal:** Indicated by a waveform icon, related to signal processing.
     - **OCEAN script:** Represented by a document icon with "SKILL" written on it, referring to a scripting language used in certain software environments.
     - **MATLAB expression:** Another "f0" symbol, indicating the use of MATLAB for expressions.
     - **MATLAB script:** A document icon, indicating the use of MATLAB scripts.
     - **Area Specification:** No specific icon, likely used for defining areas within a design or layout.
     - **Op Region Spec:** No specific icon, possibly used for specifying operational regions.
     - **Violation Filter:** An exclamation mark icon, likely used for filtering violations or errors.
     - **OP Parameters:** Highlighted in yellow, indicating it is the currently selected option. This likely refers to operational parameters.

The overall interface appears to be part of a software application used for design, analysis, or simulation, with various tools and options for configuring and executing different tasks.
```

#### **Figure 21: Adding operating point parameters in output**

This adds an operating parameter expression row.

- Action 34: Click on the **select operating point instances icon** to open the schematic.
- Action 35: Descend into the BGR\_circuit schematic and select the **M12** pmos instance.

| 25, 815, 815, 35, 815, 8 |  |
|--------------------------|--|

This adds the **/I18/M12** instance.

Action 36: Now, click on the **Select operating point parameters** icon to open the **Select OP Parameters** form.

| oppoint //118/M12 |  |                                   |
|-------------------|--|-----------------------------------|
|                   |  | Select operating point parameters |

**Figure 22: Operating point in output**

| Select OP Parameters -- A x |
|-----------------------------|
| Operating Point Parameters  |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
| Get from Simulation         |
| OK Cancel   Help            |
|                             |

**Figure 23: Select operating point parameter for /I18/M12 instance**

Action 37: Click on **Get from Simulation**.

All operating points associated with the **/I18/M12** instance will appear in the **Select OP Parameter** form.

Action 38: Select **region** and click **OK**.

| Select OP Parameters -- A x |      |
|-----------------------------|------|
| Operating Point Parameters  |      |
| vth drive<br>vdss           |      |
| vsat_marg                   |      |
| vdsat marg                  |      |
| self_gain<br>rout           |      |
| beff                        |      |
| fug                         |      |
| ft<br>rgate                 |      |
| vearly                      |      |
| region                      |      |
| reversed                    |      |
|                             |      |
| Get from Simulation         |      |
| OK   Cancel                 | Help |

#### **Figure 24: Selecting region operating point for /I18/M12 instance**

The **oppoint** parameters expression should appear as shown in the following table.

| /118/M12 oppoint |  |  | ਤੇ ਕਿ |  |
|------------------|--|--|-------|--|
|------------------|--|--|-------|--|

#### **Figure 25: Final oppoint region expression for /I18/M12 instance**

- Action 39: Repeat this and add another operating point region expression for the **/I18/M5** instance.
- Action 40: In the **ADE Explorer** window, choose **Results > Direct Plot > Main Form** to open **Direct Plot Form** as shown in Figure 26.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from a tool used for electronic circuit simulation and analysis. The interface appears to be from a program like Cadence Virtuoso, which is commonly used for designing and simulating integrated circuits.

At the top of the interface, there is a menu bar with several options: "Simulation," "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is currently selected and expanded.

Within the "Results" menu, several options are listed:
- Plot Outputs
- Direct Plot (highlighted in yellow)
- Print
- Annotate
- Vector
- Circuit Conditions
- Electrothermal Report
- EM/IR Data
- Save
- Select
- Delete
- Printing/Plotting Options

The "Direct Plot" option is further expanded, revealing a submenu titled "Direct Plot." This submenu contains a list of different types of plots and analyses that can be performed. The options listed in the "Direct Plot" submenu are:
- Main Form
- Transient Signal
- Transient Minus DC
- Transient Sum
- Transient Difference
- AC Magnitude
- AC dB10
- AC dB20
- AC Phase
- AC Magnitude & Phase
- AC Gain & Phase
- Equivalent Output Noise
- Equivalent Input Noise
- Squared Output Noise
- Squared Input Noise
- Noise Figure
- DC

The interface is designed to allow users to select various types of plots and analyses to visualize and interpret the results of their circuit simulations. The highlighted "Direct Plot" option indicates that the user is currently focused on this feature, and the expanded submenu shows the specific types of plots available for selection.
```

#### **Figure 26: Opening Direct Plot Main Form from the ADE Explorer**

Action 41: In the **Direct Plot Form** window, select **Current** as **Function** and enable the **Add To Outputs** checkbox.

|                           | Direct Plot Form<br>20                                |
|---------------------------|-------------------------------------------------------|
| Plotting Mode<br>Analysis | Append                                                |
| O dc<br>Function          |                                                       |
| D<br>Voltage              | Voltage Ratio<br>D                                    |
| Current                   | Current Ratio                                         |
| Power                     | Power Ratio                                           |
|                           | Transresistance J Transconductance                    |
| Terminal<br>Select        |                                                       |
| Add To Outputs Y          | > Select Instance Terminal on schematic<br>Close Help |

 **Figure 27: Direct Plot Form**

Action 42: Go to the schematic tab and return to the level above by clicking the up arrow on the schematic Go toolbar.

|                          |         | Virtuoso® ADE Explorer Editing: BGR Circ                                     |
|--------------------------|---------|------------------------------------------------------------------------------|
|                          |         | Launch File Edit View Create Check Options Window Parasitics/LDE ADE Explore |
|                          |         | ロ × の 17 9<br>@ 12                                                           |
|                          | Basic   |                                                                              |
|                          |         | Replace                                                                      |
| Navigator                | ? ~ x   | 118 (BGR_circuit)<br>×<br>maestro Dc                                         |
| Schematic<br>BGR_circuit |         |                                                                              |
| - OBJECTS                |         |                                                                              |
| All                      |         |                                                                              |
| Instances                | 15      | proga2v<br>2 pm092v                                                          |
| Nets                     | 11<br>> | ARTANT PATI<br>w=20                                                          |
| Pins                     | 3<br>D  |                                                                              |
| Nets and Pins            |         | 1.20737   . 3.9811m<br>11 -1                                                 |

#### **Figure 28: Clicking the up arrow on the schematic**

Action 43: Select the **PLUS** node of the **V7** supply voltage source as shown in Figure 29.

Here is the image describtion:
```
The image shows a schematic diagram of an electronic circuit. The diagram is divided into two main sections: the left section and the right section.

### Left Section:
- The left section contains a simple circuit with two voltage sources and a ground connection.
- There are two voltage sources labeled "vdc=vdd" and "vdc=avss".
- The "vdc=vdd" source is connected to a node labeled "PPA" and is also connected to a ground symbol through a component labeled "gnd".
- The "vdc=avss" source is connected to a node labeled "SSA" and is also connected to the ground symbol.
- The ground symbol is connected to the bottom of the "vdc=avss" source.
- The connections are highlighted with red lines, and the "vdc=vdd" source is enclosed in a red square.

### Right Section:
- The right section contains a more complex circuit labeled "BGR_Circuit".
- The circuit is enclosed in a green rectangular box.
- At the top of the box, there is a current source labeled "I18" connected to a node labeled "vdd".
- Below the current source, there are two current sources connected in parallel, each with a resistor connected in series.
- The node between the two resistors is labeled "V_BGR".
- The "V_BGR" node is connected to an external capacitor labeled "c=1p" and a ground symbol labeled "gpd".
- The bottom of the "BGR_Circuit" is connected to a node labeled "vss".

### Connections:
- The "PPA" node from the left section is connected to the "vdd" node in the right section.
- The "SSA" node from the left section is connected to the "vss" node in the right section.

### Labels and Colors:
- The labels "PPA" and "SSA" are in blue.
- The labels "vdc=vdd" and "vdc=avss" are in orange.
- The labels "vdd", "vss", and "V_BGR" are in red.
- The ground symbols are in green.
- The connections are highlighted with red lines.

Overall, the image depicts a schematic of a voltage reference circuit, likely a bandgap reference (BGR) circuit, with connections to power supply nodes and ground.
```

**Figure 29: Plotting supply current**

The waveform is plotted as shown in Figure 30. The "i("/V7/PLUS" ?result "dc")" supply current expression is added to the **Outputs Setup** table in ADE Explorer.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from Cadence Virtuoso, which is used for electronic design automation (EDA). The interface is displaying a graph from a DC analysis of a circuit, likely a bandgap reference (BGR) circuit, as indicated by the file name "TB_BGR_tb_bgr_1".

Here are the detailed observations:

1. **Software Interface**:
   - The title bar at the top reads "Virtuoso (R) Visualization & Analysis XL: TB BGR tb_bgr maestro_Dc".
   - The interface has multiple toolbars with various icons for different functions such as file operations, graph manipulation, measurements, and window management.

2. **Graph Details**:
   - The graph is labeled "DC Analysis `dc`: temp = (-40 C -> 120 C)" indicating that the analysis is performed over a temperature range from -40°C to 120°C.
   - The x-axis represents the temperature in degrees Celsius (°C), ranging from -40°C to 120°C.
   - The y-axis represents the current (I) in microamperes (µA), ranging from approximately -81.5 µA to -75.5 µA.

3. **Data Points and Line**:
   - A magenta line represents the current variation with temperature.
   - There are two marked data points on the graph:
     - At -40.0°C, the current is -75.92529 µA.
     - At 120.0°C, the current is -81.23888 µA.
   - The slope of the line (dy/dx) is calculated as 33.2099 nA/°C, indicating the rate of change of current with temperature.

4. **Annotations**:
   - The graph has annotations showing the exact values at the marked data points.
   - There is a label indicating the change in current (dy) over the change in temperature (dx), which is 5.313584 µA over 160.0°C.

5. **Additional Interface Elements**:
   - On the left side, there is a panel showing the trace being analyzed, labeled "i/V7/PLUS...".
   - The bottom of the interface shows a status bar with information about the trace and the design point.

Overall, the image provides a detailed view of the current variation with temperature for a specific circuit, analyzed using the Cadence Virtuoso software.
```

#### **Figure 30: BGR supply current plot with temperature sweep DC analysis**

Action 44: Name this expression as Supply\_Current in the ADE **Outputs Setup** table.

|                     |     |                |                   | Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr maestro_Dc                                               |        |     |           | - DX    |
|---------------------|-----|----------------|-------------------|--------------------------------------------------------------------------------------------------------|--------|-----|-----------|---------|
|                     |     |                |                   | Launch Session Setup Analyses Variables Outputs Simulation Results Tools EAD Parasitics DE Window Help |        |     |           | cadence |
|                     |     |                |                   | 日日日本日本の『アッセスタート-テ-ミ-19日の数字11日本<br>12                                                                   |        |     |           |         |
| 0 - 0 - 0 - 0 Basic |     |                | - East<br>1 43    | The Us to In Q. Search                                                                                 |        |     |           |         |
| 를<br>能              | 2   | 12<br>Lo       | (None)<br>Replace | 2 2 2 0<br>Lo = = = de<br>- Sim Time 0                                                                 |        |     |           |         |
| Navigator           | 36× | Name           | Type              | Details                                                                                                | Value  |     | Plot Save |         |
| Schematic           |     | BGR_output     | expr              | v("/V_BGR" ?result "dc")                                                                               | 2      | >   |           | ుండి    |
| to ber              |     | /118/M12       | oppoint           | /118/M12 region                                                                                        | মি     | 1   | <         | P       |
| - OBJECTS           |     | /118/M5        | oppoint           | /118/M5 region                                                                                         | 1      |     | >         |         |
| All<br>Instances    | 6 > | Supply_Current | expr              | i("/V7/PLUS" ?result "dc")                                                                             | R      | <   |           | 10      |
| Nets                | 4   | BGR variation  | expr              | (ymax(v("/V_BGR" ?result "dc")) - ymin(v("/V_BGR" ?result "dc")))                                      | 3.431m | A   |           | ×       |
| Pins                |     |                | expr              | ymin(v("/V_BGR" ?result "dc"))                                                                         | 1.179  | ત્વ |           | 0       |
| Nets and Pins       |     |                | expr              | ymax(v("/V_BGR" ?result "dc"))                                                                         | 1.182  | >   |           |         |
| - GROUPS            |     |                |                   |                                                                                                        |        |     |           |         |
| Cells               |     |                |                   |                                                                                                        |        |     |           |         |
| Types               |     |                |                   |                                                                                                        |        |     |           |         |
|                     |     |                |                   |                                                                                                        |        |     |           |         |
|                     |     |                |                   |                                                                                                        |        |     |           |         |

**Figure 31: ADE maestro\_Dc view**

Action 45: In the **ADE Explorer** window, click on the **Plot Outputs** icon to see all plots together as shown in Figure 32.

Here is the image describtion:
```
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL software, which is used for analyzing electronic circuits. The interface is divided into several sections, each displaying different types of data and analysis results.

1. **Top Menu Bar**: The top of the window contains a menu bar with options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, and Browser. These menus provide various functionalities for managing and analyzing the data.

2. **Toolbar**: Below the menu bar, there is a toolbar with icons for quick access to common functions such as opening files, saving, zooming, and other analysis tools.

3. **Subwindow Tabs**: There are tabs labeled "Subwindow" and "Data Point" which allow users to switch between different views or data points within the analysis.

4. **Main Analysis Area**: The main area of the interface is divided into two sections:
   - **Left Section**: This section shows a scatter plot with the title "BGR_variation:ymin(v("/V_BGR")...ymax(v("/V_BGR")?result "dc")". The plot has a vertical axis labeled from -0.1 to 1.3 and a horizontal axis labeled from -1.0 to 1.0. There are three markers labeled M2, M3, and M4, with their respective coordinates displayed. M2 and M3 are green markers, while M4 is a red marker.
   - **Right Section**: This section shows a graph with the title "BGR_output:Supply_Current". The graph has two vertical axes: the left axis labeled "V (V)" ranging from 1.17875 to 1.1825, and the right axis labeled "I (n)" ranging from -81.5 to -75.5. The horizontal axis is labeled "temp (C)" and ranges from 40.0 to 120.0. The graph displays two curves: a red curve labeled "BGR_output" and a yellow curve labeled "Supply_Current". There are markers on the curves indicating specific data points, with one marker at 40.0C and 1.182303V, and another at 120.0C. The difference between these points is also indicated (dx: 80.0C, dy: 3.43138662mV).

5. **Status Bar**: At the bottom of the window, there is a status bar displaying information about the current trace, history, test, design point, and corner. The specific details shown are:
   - Trace: BGR_output
   - History: ExplorerRun.0
   - Test: TB_BGR_tb_bgr_1
   - Design Point: 1
   - Corner: nom

Overall, the image shows a detailed analysis of a bandgap reference (BGR) circuit, with specific focus on the output voltage variation and supply current over a range of temperatures.
```

#### **Figure 32: Plots in ViVA**

Action 46: In the **ADE Explorer** window, click on the up arrow to open the **ADE Assembler** window as shown in Figure 33.

Here is the image describtion:
```
The image is a screenshot of a software interface, likely from an electronic design automation (EDA) tool used for circuit simulation. The interface is titled "Setup" and contains a hierarchical tree structure with various settings and parameters for a simulation.

Here is a detailed description of the elements in the image:

1. **Top Bar**:
   - The top bar contains the title "Setup" and has two columns labeled "Name" and "Value".
   - There is a filter icon (funnel shape) next to the "Filter" text box, which is currently empty.

2. **Tree Structure**:
   - The tree structure is organized into several expandable and collapsible sections, indicated by small icons next to each item.
   - The first item in the tree is "TB_BGR_tb_bgr_1", which appears to be the name of the testbench or simulation setup.
   - Below this, there are several categories, each with specific settings and parameters.

3. **Categories and Settings**:
   - **Simulator**: The simulator being used is "spectre".
   - **Analyses**: This section includes a "dc" analysis with parameters "t -40 120 Automatic Start-Stop".
   - **Design Variables**: This section lists two variables:
     - "avdd" with a value of 2.
     - "avss" with a value of 0.
   - **Parameters**: This section is present but does not have any specific parameters listed.
   - **Corners**: This section is present but does not have any specific corners listed.
   - **Reliability Analyses**: This section includes "Monte Carlo Sampling".
   - **Checks/Asserts**: This section is present but does not have any specific checks or asserts listed.

4. **Icons**:
   - Each category and item has an associated icon. For example, the "Analyses" section has a green icon with a waveform symbol, and the "Design Variables" section has a red icon with a variable symbol.
   - The first item, "TB_BGR_tb_bgr_1", has a blue arrow icon pointing upwards, which is highlighted with a red square around it. This likely indicates that this item is currently selected or has some special status.

Overall, the image shows a detailed setup for a circuit simulation, including the simulator type, analysis type, design variables, and other parameters. The interface allows users to configure and manage various aspects of the simulation.
```

#### **Figure 33: Up Arrow to open ADE Assembler**

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Assembler software interface, specifically showing the editing of a test bench named "TB_BGR tb_bgr maestro_Dc." The interface is divided into several sections and panels, each serving a different purpose.

1. **Top Menu Bar**: 
   - The topmost part of the interface contains a menu bar with options such as Launch, File, Create, Tools, Options, Run, EAD, Parasitics/LDE, Window, and Help.
   - Below the menu bar, there are various icons for quick access to common functions like saving, opening files, running simulations, and more.

2. **Data View Panel (Left Side)**:
   - This panel is on the left side of the interface and is labeled "Data View."
   - It contains a hierarchical tree structure with categories such as Tests, Global Variables, Parameters, Corners, Documents, Setup States, Reliability Analyses, and Checks/Asserts.
   - The "Tests" category is expanded, showing "TB_BGR_tb_bgr_1" as the selected test.
   - The "Corners" category is also expanded, showing "Nominal" as the selected corner.

3. **Run Summary Panel (Bottom Left)**:
   - Below the Data View panel, there is a "Run Summary" panel.
   - It shows that there is 1 Test, 1 Point Sweep, and 0 Corners selected for the current run.

4. **Outputs Setup Panel (Center)**:
   - The central part of the interface is the "Outputs Setup" panel.
   - It displays a table with columns labeled Test, Name, Type, Details, EvalType, Plot, Save, Spec, Weight, Units, and Digits.
   - The table lists seven rows, each representing a different output or expression to be evaluated:
     - Row 1: supply current (expr) - `I("/V7/PLUS" ?result "dc")`
     - Row 2: BGR_output (expr) - `v("/V_BGR" ?result "dc")`
     - Row 3: BGR_expression (expr) - `v(max("/V_BGR" ?result "dc"))`
     - Row 4: /I18/M12 (oppoint) - `/I18/M12 region`
     - Row 5: /I18/M5 (oppoint) - `/I18/M5 region`
     - Row 6: (expr) - `ymax("/V_BGR" ?result "dc")`
     - Row 7: (expr) - `ymin("/V_BGR" ?result "dc")`
   - The "EvalType" for all rows is set to "point."
   - The "Plot" and "Save" checkboxes are checked for some rows, indicating which outputs will be plotted and saved.

5. **Status Bar (Bottom)**:
   - At the bottom of the interface, there is a status bar showing the current trace, history, test, design point, and corner information.
   - It indicates that the trace is "BGR_output," the history is "ExplorerRun.0," the test is "TB_BGR_tb_bgr_1," the design point is "1," and the corner is "nom."

Overall, the image shows a detailed setup for running a simulation in the Virtuoso ADE Assembler, with specific outputs and expressions configured for evaluation.
```

#### **Figure 34: Assembler view of maestro\_Dc**

Action 47: In the ADE Assembler **Data View** window, expand **Corners** using the **+** sign and then, **Click to add corners** as shown in Figure 35.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a "Data View" panel. The panel is divided into two main columns: "Name" and "Value," each with a filter option at the top.

The "Name" column lists various categories, each with an associated checkbox that can be checked or unchecked to include or exclude the category from the view. The categories listed are:

1. Tests (checked)
2. Global Variables (checked)
3. Parameters (checked)
4. Corners (partially checked, indicated by a yellow square in the checkbox)
   - Nominal (checked)
   - Click to add corner (highlighted in yellow)
5. Documents (unchecked)
6. Setup States (unchecked)
7. Reliability Analyses (unchecked)
8. Checks/Asserts (unchecked)

Each category has an icon next to it, representing its type. For example, "Tests" has a gear icon, "Global Variables" and "Parameters" have a group of people icon, "Corners" has a thermometer icon, and "Documents" has a document icon.

The "Corners" category is expanded to show its subcategories, "Nominal" (which is checked) and "Click to add corner" (highlighted in yellow, indicating it is an interactive element where the user can add a new corner).

The interface appears to be part of a software tool used for managing and organizing various elements related to testing, variables, parameters, and other aspects of a project or system.
```

 **Figure 35: Opening Corner Setup**

The **Corners Setup** window will open.

|                                                       |   |         |  | Corners Setup |  |  |                            |  | × |
|-------------------------------------------------------|---|---------|--|---------------|--|--|----------------------------|--|---|
| - 四十分 日 日 日   8   0   8   0   7   Fiter name   7   18 |   |         |  |               |  |  |                            |  |   |
| Resource Corner Nominal                               |   |         |  |               |  |  |                            |  |   |
|                                                       |   |         |  |               |  |  |                            |  |   |
|                                                       |   |         |  |               |  |  |                            |  |   |
| Corners                                               | > | Nominal |  |               |  |  |                            |  |   |
|                                                       |   |         |  |               |  |  |                            |  |   |
| Temperature                                           |   |         |  |               |  |  |                            |  |   |
| Design Variables                                      |   |         |  |               |  |  |                            |  |   |
| Click to add                                          |   |         |  |               |  |  |                            |  |   |
| Parameters                                            |   |         |  |               |  |  |                            |  |   |
| Click to add                                          |   |         |  |               |  |  |                            |  |   |
| Model Files                                           |   |         |  |               |  |  |                            |  |   |
| Click to add                                          |   |         |  |               |  |  |                            |  |   |
| Model Group(s)                                        |   |         |  |               |  |  |                            |  |   |
| Click to add                                          |   |         |  |               |  |  |                            |  |   |
| Tests                                                 |   |         |  |               |  |  |                            |  |   |
| V  BGR_tb_bgr_1                                       | > |         |  |               |  |  |                            |  |   |
| mber of Corners                                       | 1 |         |  |               |  |  |                            |  |   |
|                                                       |   |         |  | 1000          |  |  |                            |  |   |
|                                                       |   |         |  |               |  |  |                            |  |   |
|                                                       |   |         |  |               |  |  | OK   Cancel   Apply   Help |  |   |

#### **Figure 36: Initial Corner Setup**

Action 48: Click on the **add new corner** icon . This will add a corner, **C0**.

Action 49: Click on **Click to add** under **Design Variables** as shown in Figure 37. Select **avdd** and then enter the values 1.8 2.2.

| Corners           | > | Nominal | CO<br>S                   |
|-------------------|---|---------|---------------------------|
| Temperature       |   |         |                           |
| Design Variables  |   |         |                           |
| Click to add      |   |         |                           |
| Parameters        |   |         |                           |
| Click to add      |   |         |                           |
| Model Files       |   |         |                           |
| Click to add      |   |         |                           |
| Model Group(s)    |   |         | <modelgroup></modelgroup> |
| Click to add      |   |         |                           |
| Tests             |   |         |                           |
| J  BGR_tb_bgr_1 V |   |         | >                         |
| Tags              |   |         |                           |

**Figure 37: Adding new corner, design variables, and model files in corner setup**

Action 50: Click on **Click to add** under **Model Files** as shown in Figure 38.

| Add/Edit Model Files<br>X                |
|------------------------------------------|
| Model Files -                            |
| Model<br>Click to add                    |
| Up<br>Down<br>Edit<br>Delete             |
| Import from Tests   OK   Cancel     Help |

#### **Figure 38: Add/Edit Model Files form**

Action 51: Click on **Import from Tests** and then, click **OK**.

Action 52: Select the **tt**, **ss**, **sf**, **fs**, **ff** sections and ensure the box is checked. Then, click **OK**.

The **Corners Setup** form will look like Figure 39.

|                            |                |         |                                                                                                       |                 |  | Corners Setup |  |  |  |  |                   | × |
|----------------------------|----------------|---------|-------------------------------------------------------------------------------------------------------|-----------------|--|---------------|--|--|--|--|-------------------|---|
| · 曰 + 8 日 日   "            |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| Resource Corner Nominal    |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| C0/gpdk045.scs             | tt ss sf fs ff |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| Corners                    | >              | Nominal | >                                                                                                     | CO              |  |               |  |  |  |  |                   |   |
| Temperature                |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| Design Variables           |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| avdd                       |                |         |                                                                                                       | 1.8 2.2         |  |               |  |  |  |  |                   |   |
| Click to add               |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| Parameters<br>Click to add |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| Model Files                |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
| gpdk045.scs                |                |         |                                                                                                       | Ttt ss sf fs ff |  |               |  |  |  |  |                   |   |
| Click to add               |                |         | ff                                                                                                    |                 |  |               |  |  |  |  |                   |   |
| Model Group(s)             |                |         | <m fs<="" td=""><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></m> |                 |  |               |  |  |  |  |                   |   |
| Click to add               |                |         | mc                                                                                                    |                 |  |               |  |  |  |  |                   |   |
| Tests                      |                |         | ਕੇ                                                                                                    |                 |  |               |  |  |  |  |                   |   |
| J  BGR_tb_bgr_1            | >              |         | ટટ<br>C<br>tt                                                                                         |                 |  |               |  |  |  |  |                   |   |
| mber of Corners            |                | 1       |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
|                            |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
|                            |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |
|                            |                |         |                                                                                                       |                 |  | 111111        |  |  |  |  |                   |   |
|                            |                |         |                                                                                                       |                 |  |               |  |  |  |  | Cancel Apply Help |   |
|                            |                |         |                                                                                                       |                 |  |               |  |  |  |  |                   |   |

**Figure 39: Final Corner Setup**

Action 53: To add specifications to the **Outputs Setup** of the **ADE Assembler** view, double-click on the **Spec** field on the row for the **ymax** expression.

Select **<** from the drop-down menu. Add the 1.195 value as shown in Figure 40.

| Test            | Name           | Type     | Details                                      | Eval Type | Plot | Save | Spec                              | Weight   |
|-----------------|----------------|----------|----------------------------------------------|-----------|------|------|-----------------------------------|----------|
| Filter          | ▼ Filter       | ▼ Filter | ><br>Filter                                  | ▼ Filter  | ♪    |      | Filter                            | ▼ Filter |
| TB_BGR_tb_bgr_1 | BGR output     | expr     | v("/V_BGR" ?result "dc")                     | point     | >    | 1    |                                   |          |
| TB_BGR_tb_bgr_1 | BGR_variation  | expr     | (ymax(v("/V_BGR" ?result "dc")) - ymin(v("/V | point     | <    | 11   |                                   |          |
| TB_BGR_tb_bgr_1 |                | expr     | ymin(v("/V_BGR" ?result "dc"))               | point     | 4    | 1    |                                   |          |
| TB_BGR_tb_bgr_1 |                | expr     | ymax(v("/V_BGR" ?result "dc"))               | point     | >    |      |                                   |          |
| TB_BGR_tb_bgr_1 | /118/M12       | oppoint  | /118/M12  region                             | point     | 187  | V    | none                              |          |
| TB_BGR_tb_bgr_1 | /118/M5        | oppoint  | /118/M5 region                               | point     | 15   | >    | minimize                          |          |
| TB_BGR_tb_bgr_1 | Supply_Current | expr     | i("/\7/PLUS" ?result "dc")                   | point     | 4    |      | maximize<br>V                     |          |
|                 |                |          |                                              |           |      |      | A<br>range<br>tol<br>info<br>wave |          |

#### **Figure 40: Adding specs in Outputs Setup of ADE Assembler**

Action 54: Repeat this using the following table to add specifications to the other expressions.

| 0                                                                   |                         |                                  |                                       | Virtuoso® ADE Assembler Editing: TB_BGR tb_bgr maestro_Dc |                           |   |             |           | X = = x |
|---------------------------------------------------------------------|-------------------------|----------------------------------|---------------------------------------|-----------------------------------------------------------|---------------------------|---|-------------|-----------|---------|
| Launch File Create Tools Options Run EAD Parasitics/LDE Window Help |                         |                                  |                                       |                                                           |                           |   |             |           | cadence |
| । ਨਾ                                                                | 网                       | 图 合图<br>a                        |                                       | 기록<br>Basic                                               |                           |   |             |           |         |
| 0<br>No Parasitics/LDE                                              | E3<br>No Sweeps         | > Single Run, Sweeps and Corners |                                       | ್ರಿ<br>><br>Reference:                                    |                           |   |             | ర్లో<br>g |         |
| ? 日 X<br>Data View                                                  | tb_bgr X                | maestro_Dc<br>×                  |                                       |                                                           |                           |   |             |           |         |
| Name<br>Value                                                       | Outputs Setup           | Results                          |                                       |                                                           |                           |   |             |           |         |
| ▼ Filter<br>Filter<br>0 7 8 8 Tests                                 | 1 Pay<br>x<br>2017<br>C | Filter  ▼                        | 2 0 日 日 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | (ex) - 0 - 0 0 0 0 0                                      |                           |   |             |           |         |
| 田 Global Variables                                                  | / rows<br>Test          | Name                             |                                       | Details                                                   |                           |   | Plot   Save | Spec      |         |
| 中文 Parameters<br>Corners                                            | ilter                   | ▼ Filter                         | Type<br>▼ Filter                      | Filter                                                    | EvalType<br>▼ Filter<br>マ |   |             | Filter    |         |
| 国国 Documents                                                        | TB_BGR_tb_bgr_1         | BGR_output                       | expr                                  | v("/V_BGR" ?result "dc")                                  | point                     | < |             |           |         |
| মি<br>Setup States                                                  | TB_BGR_tb_bgr_1         |                                  | expr                                  | ymax(v("/V_BGR" ?result "dc"))                            | point                     | < |             | < 1.195   |         |
| [ Reliability Analyses                                              | TB_BGR_tb_bgr_1         |                                  | expr                                  | ymin(v("/V_BGR" ?result "dc"))                            | point                     | V |             | > 1.165   |         |
| Data   History                                                      | TB_BGR_tb_bgr_1         | BGR_variation                    | expr                                  | (ymax(v("/V_BGR" ?result "dc")) - ymin(v("/V              | point                     | < |             | < 8m      |         |
| ? 日 ×<br>Run Summary                                                | TB_BGR_tb_bgr_1         | /118/M12                         | oppoint                               | /118/M12 region                                           | point                     |   | <           |           |         |
| 1 Test<br>Nominal Corner                                            | TB_BGR_tb_bgr_1         | /118/M5                          | oppoint                               | /118/M5 region                                            | point                     |   | V           |           |         |
| 1 Point Sweep<br>> 10 Corners                                       | TB_BGR_tb_bgr_1         | Supply_Current                   | expr                                  | i("/\7/PLUS" ?result "dc")                                | point                     | < |             |           |         |
| History Item<br>Status                                              |                         |                                  |                                       |                                                           |                           |   |             |           |         |
|                                                                     |                         |                                  |                                       | 1100                                                      |                           |   |             |           |         |
| mouse L:                                                            |                         |                                  |                                       | M:                                                        |                           |   |             |           | R:      |
| 32(80)                                                              |                         |                                  |                                       |                                                           |                           |   |             |           |         |

**Figure 41: ADE Assembler setup of maestro\_Dc**

Action 55: Run the simulation by clicking on the green run icon to **netlist and run simulation** across corners.

All output design parameters, BGR\_variation, supply current, ymax, and ymin of BGR\_output are passing the specifications.

|                                                                     |                                 |                                                   |         |         | Virtuoso® ADE Assembler Editing: TB_BGR tb_bgr maestro_Dc |                                                                                                                                                                                             |                                                                                                                                                                                |        |        | = ロ×    |
|---------------------------------------------------------------------|---------------------------------|---------------------------------------------------|---------|---------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|---------|
| Launch File Create Tools Options Run EAD Parasitics/LDE Window Help |                                 |                                                   |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        | cadence |
| 4 0<br>7 1                                                          | 0%                              |                                                   | -Q B    |         |                                                           | · 電電                                                                                                                                                                                        |                                                                                                                                                                                |        |        |         |
| 6<br>No Parasitics/LDE                                              | No Sweeps                       | Single Run, Sweeps and Corners                    |         |         | 17 8                                                      | Reference                                                                                                                                                                                   |                                                                                                                                                                                | ਜ਼ੀ    | శ్రీని |         |
| ? 日 ×<br>Data View                                                  | tb_bgr X                        | maestro_Dc X                                      |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |
| Name<br>Value                                                       | Outputs Setup                   | Results                                           |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |
| ▼ Filter<br>Filter<br>E L & Tests                                   | Detail                          | ్రెస్                                             |         |         |                                                           |                                                                                                                                                                                             | ============================================================================================================================================================================== |        |        |         |
| Global Variables<br>E                                               |                                 | Parameter                                         | Nominal |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | CO O   |         |
| Parameters                                                          |                                 | avdd                                              | 2       |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | 1.8    |         |
| Corners                                                             |                                 | gpdk045.scs                                       | tt      |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | tt     |         |
| Documents<br>Setup States                                           | Trows                           |                                                   |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |
| _ Reliability Analyses<br>मि                                        | Test                            | Output                                            | Nominal | Spec    | Weight                                                    | Pass/Fail<br>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | Min                                                                                                                                                                            | Max    | CO O   |         |
| Data   History                                                      | Ilter                           | ><br>Filter                                       | ilter   | Filter  | ▼ Filter                                                  | ▼ Filter                                                                                                                                                                                    | * Filter                                                                                                                                                                       | Filter | Filter |         |
| ?日X                                                                 |                                 |                                                   |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |
| Run Summary                                                         | TB_BGR_tb_bgr    BGR_output     |                                                   | 2       |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | 2      | E       |
| 1 Test<br>V Nominal Corner                                          | TB_BGR_tb_bgr  ymax(v("/V_BG    |                                                   | 1.182   | < 1.195 |                                                           | pass                                                                                                                                                                                        | 1.176                                                                                                                                                                          | 1.192  | 1.18   |         |
| 1 Point Sweep<br>V 10 Corners                                       | TB_BGR_tb_bgr    ymin(v("/V_BGR |                                                   | 1979    | > 1.165 |                                                           | pass                                                                                                                                                                                        | 1.172                                                                                                                                                                          | 1.188  | 1.176  |         |
|                                                                     | TB_BGR_tb_bgr    BGR_variation  |                                                   | 3.431m  | < 8m    |                                                           | pass                                                                                                                                                                                        | 3.165m                                                                                                                                                                         | 4.638m | 3.859m |         |
|                                                                     | TB_BGR_tb_bgr  /118/M12         |                                                   | J       |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | R      |         |
|                                                                     | TB_BGR_tb_bgr  /118/M5          |                                                   | ನ       |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | િ      | TRI     |
| History Item<br>Status                                              | TB_BGR_tb_bgr    Supply_Current |                                                   | న       |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        | 2      |         |
|                                                                     |                                 |                                                   | THE     |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |
|                                                                     |                                 | ExplorerRun.0 () ExplorerRORun.0.RO Interactive.0 |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        | ×       |
| mouse L:                                                            |                                 |                                                   |         | M:      |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        | R       |
| 32(80)                                                              |                                 |                                                   |         |         |                                                           |                                                                                                                                                                                             |                                                                                                                                                                                |        |        |         |

**Figure 42: Results tab view of Assembler maestro\_Dc**

Action 56: Right-click on the **Nominal** column for BGR\_output and select **Plot Across Corners** as shown in Figure 43.

|                                                                                                                     | Parameter                                                                                               |                     | Nominal                                                                                                    |                                                                                                                                                                                                                                                               |  |       |  |  |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-------|--|--|
|                                                                                                                     | avdd<br>gpdk045.scs                                                                                     |                     | View Log Messages<br>View Netlist<br>View Netlisted Checks/Asserts<br>View Dynamic/Static Violation Report |                                                                                                                                                                                                                                                               |  |       |  |  |
| rows                                                                                                                |                                                                                                         |                     |                                                                                                            | Open Terminal                                                                                                                                                                                                                                                 |  |       |  |  |
| Test                                                                                                                | Output                                                                                                  | No                  | Job Log                                                                                                    |                                                                                                                                                                                                                                                               |  |       |  |  |
| Filter                                                                                                              | ▼ Filter                                                                                                | ▼ Filter            |                                                                                                            | Cancel Selected Simulation(s)                                                                                                                                                                                                                                 |  | Firer |  |  |
| TB_BGR_tb_bgr<br>TB_BGR_tb_bgr<br>TB_BGR_tb_bgr<br>TB_BGR_tb_bgr<br>TB_BGR_tb_bgr<br>TB_BGR_tb_bgr<br>TB_BGR_tb_bgr | BGR output<br>BGR variation<br>ymin(v("/V_BGR<br>ymax(v("/V_BG<br>/118/M12<br>/118/M5<br>Supply_Current | 3<br>W<br>ﺍﺳ<br>ﺍﻟﻤ | Plot All<br>Plot                                                                                           | Plot Associated Signals<br>Quick Plot All<br>Plot Across Corners<br>Plot Across Design Points<br>Create Copy Of Selected Corner<br>Troubleshoot Point<br>Open Debug Environment<br>Spectre Interactive Environment<br>Open Results Browser<br>Open Calculator |  |       |  |  |

**Figure 43: Plotting across corners** 

Here is the image describtion:
```
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL tool, which is used for analyzing electronic circuit simulations. The specific simulation being analyzed is labeled "TB_BGR_tb_bgr_1" and the data being displayed is for "BGR_output."

The main part of the image is a graph plotting the output voltage (V) of a bandgap reference circuit against temperature (°C). The x-axis represents the temperature range from -40°C to 120°C, while the y-axis represents the output voltage ranging from approximately 1.172V to 1.194V.

There are multiple colored curves on the graph, each representing the output voltage of the bandgap reference circuit under different conditions or process corners. The curves show how the output voltage changes with temperature. The curves generally exhibit a parabolic shape, indicating that the output voltage increases with temperature up to a certain point and then decreases.

Two specific data points are highlighted on the graph:
1. A point at 60.0°C with an output voltage of 1.192176V, marked with a red triangle and a label.
2. A point at 120.0°C with an output voltage of 1.171816V, marked with a red circle and a label.

The difference in voltage between these two points is also indicated, with a delta (dy) of -20.359974mV and a temperature coefficient (s) of -339.3329uV/°C.

The toolbar at the top of the window contains various icons and options for manipulating the graph, such as zooming, panning, and changing the display settings. The left sidebar lists the available data traces, with "BGR_output" being the selected trace.

The bottom of the window shows a status bar with information about the selected trace, including the model files, test name, design point, and corner.

Overall, the image provides a detailed view of the temperature dependence of the bandgap reference circuit's output voltage, with specific data points and differences highlighted for analysis.
```

**Figure 44: BGR\_output plots Across PVT Corners**

Action 57: Close all windows but leave the **Virtuoso** session open for the next lab.

### <span id="page-29-0"></span>**Lab 2: Power Supply Rejection Ratio of Bandgap Using Ac Analysis**

This lab is set up to determine PSRR of the Bandgap circuit. PSRR is a measure of the influence of the power supply ripple on the Bandgap output voltage.

PSRR analysis is used to measure the effect of supply ripples on the output reference supply.

Action 58: From the Library Manager, open **TB\_BGR > tb\_bgr > schematic**. The schematic window opens as shown in Figure 45.

Here is the image describtion:
```
The image shows a schematic diagram of an electronic circuit, likely created using a circuit design software. The diagram is displayed on a grid background, which is typical for such software to help with component placement and alignment.

### Components and Connections:
1. **Power Supplies:**
   - There are two voltage sources labeled `V7` and `V8`.
   - `V7` is connected to a node labeled `PPA` and has parameters `vdc=vdd` and `ac=1`.
   - `V8` is connected to a node labeled `VSS` and has a parameter `vdc=vss`.

2. **Ground Connection:**
   - The ground symbol is connected to the bottom node of `V7`.

3. **BGR Circuit:**
   - The main part of the diagram is enclosed in a green rectangle labeled `BGR Circuit`, which stands for Bandgap Reference Circuit.
   - Inside the BGR Circuit, there are two current sources connected in parallel, each with a resistor in series.
   - The top node of the left current source is connected to the `PPA` node.
   - The top node of the right current source is connected to a node labeled `V_BGR`.
   - The bottom nodes of both current sources are connected to a common node at the bottom of the BGR Circuit.

4. **Resistors:**
   - There are two resistors inside the BGR Circuit, each connected in series with the current sources.
   - The resistors are connected to the `PPA` and `V_BGR` nodes.

5. **Output Node:**
   - The node labeled `V_BGR` is connected to an output node labeled `V_BGR` outside the BGR Circuit.
   - This output node is connected to a capacitor labeled `C0`, which is grounded.

6. **Labels and Annotations:**
   - The nodes and components are labeled with various annotations such as `PPA`, `V_BGR`, `VSS`, and `BGR Circuit`.
   - The current sources and resistors inside the BGR Circuit are not explicitly labeled with values.

### Summary:
The schematic represents a Bandgap Reference Circuit, which is a common circuit used to generate a stable reference voltage that is independent of temperature and supply voltage variations. The circuit includes voltage sources, current sources, resistors, and a capacitor, all interconnected to achieve the desired reference voltage output.
```

**Figure 45: Schematic of tb\_bgr cell testbench**

Action 59: In the **schematic** view, select the **V7** dc supply voltage source and press the **Q** bindkey key to open the **Edit Object Properties** form. Confirm that **AC magnitude** is defined as **1V**.

| Apply To                   | only current instance >>      |                        |
|----------------------------|-------------------------------|------------------------|
| Show                       | _ system & user & CDF         |                        |
| Browse                     | Reset Instance Labels Display |                        |
| Property                   | Value                         | Display                |
| Library Name               | analogLib                     | off                    |
| Cell Name                  | vdc                           | off                    |
| View Name                  | symbol                        | off                    |
| Instance Name              | V7                            | off                    |
|                            | Add<br>Delete                 | Modify                 |
| User Property              | Master Value                  | Local Value<br>Display |
| Ivsignore                  | TRUE                          | off                    |
| CDF Parameter              | Value                         | Display                |
| Noise file name            |                               | off                    |
| Number of noise/freq pairs | 0                             | off                    |
| DC voltage                 | avdd V                        | off                    |
| AC magnitude               | 1 V                           | off                    |
| AC phase                   |                               | off                    |
| XF magnitude               |                               | off                    |
| PAC magnitude              |                               | off                    |
| PAC phase                  |                               | off                    |
| Temperature coefficient 1  |                               | off                    |
| Temperature coefficient 2  |                               | off                    |
| Nominal temperature        |                               | off                    |

**Figure 46: Object property of supply voltage source**

- Action 60: Cancel the form.
- Action 61: From the schematic, select **Launch > ADE Explorer**.
- Action 62: In the **Launch ADE Explorer** window that opens, select **Create New View** and click **OK**.

| Launch ADE Explorer                                |  |
|----------------------------------------------------|--|
| ADE Explorer<br>Create New View Open Existing View |  |
| Cancel<br>Help<br>OK                               |  |

**Figure 47: Launching ADE Explorer from the schematic window**

Action 63: In the **Create new ADE Explorer view** window, change the view name to maestro\_Ac.

| Library           | TB BGR                                            |  |  |
|-------------------|---------------------------------------------------|--|--|
| Cell              | tb bgr                                            |  |  |
| View              | maestro Ac                                        |  |  |
| lype              | maestro                                           |  |  |
| Application       |                                                   |  |  |
| Open with         | ADE Explorer                                      |  |  |
|                   | Always use this application for this type of file |  |  |
| Library path file |                                                   |  |  |
|                   | /BGR_Verification_Workshop/cds lib                |  |  |
|                   | Open in @ new tab O current tab O new window      |  |  |

#### **Figure 48: Opening maestro\_Ac view of tb\_bgr cell**

The **ADE Explorer** window opens as shown in Figure 49.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer, a tool used for analog and mixed-signal design and simulation, developed by Cadence Design Systems. The interface is divided into several sections:

1. **Title Bar**: At the top, it displays "Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr maestro_Ac" indicating the current project or file being worked on.

2. **Menu Bar**: Below the title bar, there is a menu bar with options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

3. **Toolbar**: Directly under the menu bar, there is a toolbar with various icons for quick actions like saving, opening files, and other common tasks. There is also a search bar with "Replace" and a dropdown menu set to "(None)".

4. **Setup Panel**: On the left side, there is a panel titled "Setup" which contains a hierarchical tree structure. The tree includes:
   - TB_BGR_tb_bgr_1
   - Simulator spectre
   - Analyses (with a prompt to "Click to add analysis")
   - Design Variables (with a prompt to "Click to add variable")
   - Parameters
   - Corners (with a checkbox ticked)
   - Reliability Analyses
   - Monte Carlo Sampling
   - Checks/Asserts

5. **Main Workspace**: The central part of the interface is a large blank area, likely where the main content or results would be displayed. It currently shows a tab labeled "maestro_Ac".

6. **Right Toolbar**: On the right side, there is a vertical toolbar with icons for various actions such as running simulations, stopping simulations, and other controls.

7. **Status Bar**: At the bottom, there is a status bar with some text indicating "TB_BGR tb_bgr schematic" and "Simulator: spectre aps".

The interface is designed to facilitate the setup, execution, and analysis of simulations for electronic circuit designs.
```

#### **Figure 49: ADE Explorer window showing maestro\_Ac view**

Action 64: In the **ADE Explorer** window, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a setup window for a simulation or analysis tool. The window is titled "Setup" and is divided into two main columns: "Name" and "Value," each with a filter option at the top.

The left column, under "Name," contains a hierarchical list of items, each with an associated icon:

1. **TB_BGR_tb_bgr_1**: This appears to be the name of the test bench or project.
   - Icon: A blue upward arrow.

2. **Simulator spectre**: This indicates the simulator being used, which is "spectre."
   - Icon: A green gear.

3. **Analyses**: This section is for adding different types of analyses.
   - Icon: A green gear.
   - Sub-item: "Click to add analysis" (highlighted in yellow), suggesting that the user can click here to add a new analysis.

4. **Design Variables**: This section is for managing design variables.
   - Icon: A red cube.
   - Sub-item: "Click to add variable," indicating that the user can add new variables here.

5. **Parameters**: This section is for setting parameters.
   - Icon: A red cube.
   - Checkbox: Checked, indicating that this section is active or selected.

6. **Corners**: This section is likely for corner case analyses.
   - Icon: A thermometer.
   - Checkbox: Checked, indicating that this section is active or selected.

7. **Reliability Analyses**: This section is for reliability analyses.
   - Icon: Not visible, but the section is collapsed.

8. **Monte Carlo Sampling**: This section is for Monte Carlo sampling analyses.
   - Icon: A green circular arrow.
   - Checkbox: Unchecked, indicating that this section is not active or selected.

9. **Checks/Asserts**: This section is for checks and assertions.
   - Icon: Not visible, but the section is collapsed.

The right column under "Value" is empty, suggesting that no specific values or settings are currently displayed or selected for the items in the "Name" column. The interface also includes small question mark icons in the top right corner, likely for help or additional information.
```

**Figure 50: Opening 'Analyses' form from 'Click to add analysis'**

Action 65: In the **Choosing Analyses** form, select the **ac** analysis and set the following options. Then, click **OK**:

- Select **Frequency** as **Sweep Variable**.
- Set the **Start** frequency to **1**Hz and **Stop** frequency for **1G**Hz.
- Choose **Automatic** for **Sweep Type**.

|                                                                                                                       |                     |             | Choosing Analyses -- ADE Explorer | ×               |
|-----------------------------------------------------------------------------------------------------------------------|---------------------|-------------|-----------------------------------|-----------------|
| Analysis                                                                                                              | 0<br>tran           | D<br>dc     | C ac                              | D<br>noise      |
|                                                                                                                       | xf                  | sens        | dcmatch                           | acmatch         |
|                                                                                                                       | stb                 | pz          | 11                                | sp              |
|                                                                                                                       | envlp               | bss         | pac                               | pstb            |
|                                                                                                                       | pnoise              | pxf         | psp                               | dbss            |
|                                                                                                                       | qpac                | qpnoise     | qpxf                              | dbsp            |
|                                                                                                                       | hb                  | hbac        | hbstb                             | hbnoise         |
|                                                                                                                       | hbsp                | hbxf        |                                   |                 |
|                                                                                                                       |                     | AC Analysis |                                   |                 |
| Sweep Variable                                                                                                        |                     |             |                                   |                 |
| Frequency<br>0                                                                                                        |                     |             |                                   |                 |
| Design Variable                                                                                                       |                     |             |                                   |                 |
| Temperature                                                                                                           |                     |             |                                   |                 |
|                                                                                                                       | Component Parameter |             |                                   |                 |
|                                                                                                                       | Model Parameter     |             |                                   |                 |
| None                                                                                                                  |                     |             |                                   |                 |
| Sweep Range<br>Start-Stop<br>O<br>Center-Span<br>Sweep Type<br>Automatic<br>Add Specific Points<br>Add Points By File |                     | Start       | Stop                              | 1 G             |
|                                                                                                                       |                     |             |                                   |                 |
| Specialized Analyses                                                                                                  |                     |             |                                   |                 |
| None                                                                                                                  |                     |             |                                   |                 |
| Enabled<br>V                                                                                                          |                     |             | OK Cancel   Defaults   Apply      | Options<br>Help |

#### **Figure 51: Setup of DC-Sweep Analysis**

- Action 66: In the **ADE Explorer** window, click on **Variables** and select **Copy From Cellview** as shown in Figure 52.
- Action 67: In the **Setup** assistant, set the **Design Variables** values for **avdd=2** and **avss=0**.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Edition software interface, which is used for analog and mixed-signal design and simulation. The interface is divided into several sections and menus.

1. **Top Menu Bar**:
   - The top menu bar includes options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, and more.
   - The "Variables" menu is highlighted in yellow, indicating it is currently selected or active.

2. **Dropdown Menu**:
   - Under the "Variables" menu, a dropdown menu is visible with options: Edit, Delete, Find, Copy From Cellview, and Copy To Cellview.
   - The "Copy From Cellview" option is highlighted in yellow, indicating it is the selected option.

3. **Setup Panel**:
   - The left side of the interface shows the "Setup" panel.
   - The panel includes a hierarchical tree structure with various components:
     - **TB_BGR_tb_bgr_1**: This appears to be the name of the testbench or the top-level design.
     - **Simulator_spectre**: Indicates that the Spectre simulator is being used.
     - **Analyses**: Lists the types of analyses being performed. In this case, an "ac" analysis with a range from 1 to 1G (1 GHz) is selected.
     - **Design Variables**: This section lists the design variables used in the simulation.
       - Two design variables are shown:
         - `avdd` with a value of 2.
         - `avss` with a value of 0.
     - Other sections include Parameters, Corners, Reliability Analyses, Monte Carlo Sampling, and Checks/Asserts, but they are not expanded or detailed in this screenshot.

4. **Highlighted Elements**:
   - The "Variables" menu and the "Copy From Cellview" option are highlighted in yellow.
   - The design variables `avdd` and `avss` are also highlighted in yellow, indicating they are of particular interest or importance in this context.

Overall, the image provides a detailed view of the setup and configuration of a simulation environment within the Virtuoso ADE Explorer Edition software, focusing on the design variables and the action of copying variables from a cell view.
```

 **Figure 52: Copying variables from cell view**

- Action 68: In the **ADE Explorer** window, click on the green arrow button to **netlist and run** the simulation.
- Action 69: When the simulation is complete, click on **Simulation > Output Log** in the **ADE Explorer** window as shown in Figure 53.
- Action 70: Verify that simulation has completed with 0 errors.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically the Virtuoso ADE Explorer Editing environment. The interface appears to be part of a simulation tool used for electronic design automation (EDA). 

At the top of the interface, there is a menu bar with several options, including "Outputs," "Results," "Tools," "EAD," and "Parasitics." The "Simulation" menu is highlighted in yellow, indicating that it is currently selected or active.

Below the menu bar, there is a dropdown menu that has been expanded. This dropdown menu contains several options related to simulation tasks. The options listed in the dropdown menu are:

1. Netlist and Run
2. Run
3. Stop
4. Suspend (grayed out, indicating it is not currently available)
5. Resume (grayed out, indicating it is not currently available)
6. Run Preview
7. MDL Control
8. Options (with a submenu indicated by a right arrow)
9. Netlist (with a submenu indicated by a right arrow)
10. Output Log (highlighted in yellow)
11. Linter Log
12. Convergence Aids
13. Diagnostics

The "Output Log" option is also highlighted in yellow, suggesting that it is either selected or being pointed out for emphasis.

To the right of the dropdown menu, there is a field with the label "(None)" and a red arrow, which might be a dropdown selector for additional options or settings.

Overall, the image shows a detailed view of the simulation menu within the Virtuoso ADE Explorer Editing environment, highlighting the "Simulation" menu and the "Output Log" option.
```

**Figure 53: Opening simulation log file from ADE Explorer window**

Action 71: In the **ADE Explorer** window, choose **Results > Direct Plot > Main Form** to open **Direct Plot Form** as shown in Figure 54.

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 35

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from a tool used for circuit simulation and analysis. The title bar at the top indicates that the software is "Explorer Editing: TB_BGR tb_bgr maestro_Ac." The interface appears to be from a software suite used for electronic design automation (EDA), likely Cadence Virtuoso, which is commonly used for integrated circuit design.

The screenshot shows a dropdown menu under the "Results" tab, which is highlighted in yellow. The "Results" menu has several options, and the "Direct Plot" option is selected, also highlighted in yellow. When "Direct Plot" is selected, a sub-menu appears to the right, titled "Direct Plot," which lists various plotting options.

The "Direct Plot" sub-menu includes the following options:
- Main Form ...
- Transient Signal
- Transient Minus DC
- Transient Sum
- Transient Difference
- AC Magnitude
- AC dB10
- AC dB20
- AC Phase
- AC Magnitude & Phase
- AC Gain & Phase
- Equivalent Output Noise
- Equivalent Input Noise
- Squared Output Noise
- Squared Input Noise
- Noise Figure
- DC

Each of these options represents different types of plots or analyses that can be performed on the simulation results. The interface is designed to allow users to visualize and analyze various aspects of their circuit's performance, such as transient response, AC response, noise characteristics, and DC operating points.
```

**Figure 54: Opening Direct Plot Form from ADE Explorer window**

- Action 72: To plot the gain, select **Voltage** as the **Function**, **Net** from the drop-down menu, and **dB20** as **Modifier**.
- Action 73: Enable the **Add To Outputs** checkbox and select the **V\_BGR** net from the schematic.

|                                | Direct Plot Form         | 20         |
|--------------------------------|--------------------------|------------|
| Plotting Mode<br>Analysis      | Append                   |            |
| ac<br>0                        |                          |            |
| Function                       |                          |            |
| · Voltage C Current<br>GD<br>3 |                          |            |
| Select Net                     |                          |            |
| Modifier                       |                          |            |
| dB20                           | Magnitude O Phase O dB10 |            |
| Add To Outputs                 | 》                        |            |
| > Select Net on schematic      |                          |            |
|                                |                          | Close Help |

**Figure 55: Direct Plot Form** 

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 36

The PSRR waveform is plotted as shown in Figure 56. The db(vfreq('ac "/V\_BGR")) expression is added to the maestro view.

Here is the image describtion:
```
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL software, which is used for analyzing electronic circuits. The main window displays an AC response graph, showing the voltage gain (V) in decibels (dB) on the y-axis versus frequency (freq) in Hertz (Hz) on the x-axis. The graph is plotted on a logarithmic scale for both axes.

Key elements of the image include:

1. **Graph Plot**: The graph shows a single trace labeled "v / V_BGR; ac dB20(V)" with a green line. The trace has three markers:
   - **M1**: Located at 7.94328 Hz with a gain of -41.2436 dB.
   - **M2**: Located at 1.99526 MHz with a gain of -17.2929 dB, indicating a peak in the response.
   - **M3**: Located at 436.516 MHz with a gain of -47.8076 dB.

2. **Toolbar**: The toolbar at the top of the window contains various icons for different functions, such as opening files, saving, zooming, panning, and other analysis tools. The "Data Point" tool is highlighted, and the "family" and "Classic" options are selected.

3. **Subwindow**: The subwindow is labeled "1" and contains the AC response graph. There is a scrollbar above the graph for navigating through the data.

4. **Left Panel**: The left panel lists the AC response under the "Name" section, with a green checkmark indicating the selected trace.

5. **Status Bar**: The status bar at the bottom of the window shows the trace details, including the history, test name, and the specific trace being analyzed.

6. **Menu Bar**: The menu bar at the top of the window includes options such as File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.

Overall, the image provides a detailed view of the AC response analysis of a circuit, highlighting key frequencies and their corresponding voltage gains.
```

Action 74: Add single-point markers using the **M** bindkey on the plot.

**Figure 56: Plot of PSRR in ViVA-XL waveform window**

Action 75: Select the PSRR plot and click the **calculator** icon as shown in Figure 56.

The expression for the PSRR plot is added to the calculator as shown in Figure 57.

|                                        |                                          |                               |                    | Virtuoso (R) Visualization & Analysis XL calculator                           |               |                            |            |               |
|----------------------------------------|------------------------------------------|-------------------------------|--------------------|-------------------------------------------------------------------------------|---------------|----------------------------|------------|---------------|
| File Tools View Options Constants Help |                                          |                               |                    |                                                                               |               |                            |            |               |
| In Context Results DB:                 |                                          |                               |                    | /TB_BGR/tb_bgr/maestro_Ac/results/maestro/ExplorerRun.0/1/TB_BGR_tb_bgr_1/psf |               |                            |            |               |
| app plot erplot                        | average cross dB20 sqrt ymax             |                               |                    |                                                                               |               |                            |            |               |
| TB_BGR_tb_bgr_1                        | D<br>vf<br>D<br>vt<br>0<br>it<br>D<br>if | U vdc<br>U VS<br>Uidc<br>U is | 0 05<br>Oop<br>opt | O ot<br>Ump<br>V var                                                          | U vn<br>0 vn2 | D<br>sp<br>VSWL<br>Uzp Uyp | hp<br>O gd | ZIm<br>J data |
|                                        | · Off · Family O Wave · Clip   Append    |                               | Rectangular        | 17 3 8 日                                                                      |               |                            |            |               |
| (B)<br>Key P<br>X                      | db vfreq('ac "/V_BGR"))                  |                               |                    |                                                                               |               |                            |            |               |
| 7<br>8<br>9                            |                                          |                               |                    |                                                                               |               |                            |            |               |
| 4<br>5<br>6<br>*                       |                                          |                               |                    |                                                                               |               |                            |            |               |

Here is the image describtion:
```
The image is a caption that reads "Figure 57: ViVA-XL calculator." The text is in bold, indicating that it is likely part of a larger document or presentation, specifically referring to a figure labeled as number 57. The subject of the figure is the "ViVA-XL calculator," which suggests that the figure is an illustration or image of a calculator named ViVA-XL. However, the actual image of the calculator is not provided in the text snippet.
```

Action 76: In the calculator, select the **value** function from the **Functional Panel** window.

| Function Panel                    |              |                |                       |                |           |                           |            |
|-----------------------------------|--------------|----------------|-----------------------|----------------|-----------|---------------------------|------------|
| Special Functions<br>ರ<br>fx<br>r |              |                |                       |                |           |                           |            |
| PN                                | cross        | eyeDiagram     | getData               | lastVal        | pow       | sample                    | value      |
| aasp                              | d2a          | eyeHeightAtXY  | groupDelay            | loadpull       | pris      | settling lime             | waveVsWave |
| abs_jitter                        | dBm          | eye Width AtXY | harmonic              | Ishift         | psd       | skewness                  | xmax       |
| analog2Digital                    | delay        | fallTime       | harmonicFreq normalQQ |                | psdbb     | slewRate                  | xmin       |
| average                           | delayMeasure | firstVal       | histogram2D           | normalQQPValue | pstddev   | spectralPower             | xval       |
| bandwidth                         | deriv        | flip           |                       | num Conv       | pzbode    | spectrumMeas ymax         |            |
| bus Transition                    | dff          | fourEval       | iinteg                | overshoot      | pzfilter  | stodev                    | ymın       |
| calcVal                           | dftbb        | freq           | וחו                   | pavg           | rise Time | swapSweep                 |            |
| clip                              | dnl          | freq_jitter    | integ                 | peak           | rms       | tangent                   |            |
| compare                           | dutyCycle    | frequency      | intersect             | peakToPeak     | rmsNoise  | thd                       |            |
| compression                       | evmQAM       | gainBwProd     | ipn                   | period_jitter  |           | rms_jitter triggeredDelay |            |
| compressionVRI                    | evmQpsk      | gainMargin     | IpnVRI                | phaseMargin    | root      | unityGainFreq             |            |
| convolve                          | eyeAperture  | getAsciiWave   | kurtosis              | phaseNoise     | rshift    | V                         |            |

**Figure 58: Functional Panel of ViVA-XL calculator**

Action 77: The **Functional Panel** window will contain the signal name as shown in Figure 59. Set the value of **Interpolate at** as **1**. Click **OK**.

| value                          |                                 |                           |
|--------------------------------|---------------------------------|---------------------------|
|                                | Signal  db(vfreq('ac "/V_BGR")) |                           |
| Interpolate at                 | 11                              |                           |
| Interpolation method linear    |                                 |                           |
| Number of occurrences single   |                                 |                           |
| Period (required for multiple) |                                 |                           |
| Plot/print vs.                 | time                            |                           |
| Extrapolate                    | on                              |                           |
|                                |                                 | Apply Defaults Help Close |

**Figure 59: Using value calculator function of ViVA-XL calculator**

The expression will become value(db(vfreq('ac "/V\_BGR")) 1 ) as shown in Figure 60.

Action 78: Click the **Send buffer expression to ADE output** icon to add the expression to the maestro view.

Here is the image describtion:
```
The image shows a screenshot of a software interface, likely related to electronic circuit simulation or analysis. Here are the details:

1. **Top Toolbar**:
   - There are several buttons and options in the top toolbar:
     - "Off" button (possibly to turn off a feature or function).
     - "Family" button.
     - "Wave" button.
     - "Clip" button (checked).
     - A button with a waveform icon and a green arrow (likely related to running or simulating a waveform).
     - "Append" button with a dropdown arrow.
     - "Rectangular" button with a dropdown arrow.
     - A gear icon button (highlighted with a red box, indicating it might be important or currently selected).
     - A button with a grid or table icon.

2. **Main Text Area**:
   - The main text area contains a command or script:
     - `value(db(vfreq("ac "/V_BGR")) 1)`
     - This command seems to be related to calculating or displaying a value in decibels (db) for a frequency response (vfreq) of an AC signal at a node or variable named "V_BGR".

3. **Keypad**:
   - On the left side, there is a virtual keypad with numbers and basic arithmetic operators:
     - Numbers: 7, 8, 9, 4, 5, 6.
     - Operators: division (/), multiplication (*).

4. **Additional Buttons**:
   - There is a button labeled "Key P..." which might be for additional keypad options or functions.
   - A button with a folder icon, possibly for opening or saving files.

The interface appears to be designed for users who are performing calculations or simulations, likely in the context of electrical engineering or circuit design. The highlighted gear icon suggests that the user might be in a settings or configuration mode.
```

Here is the image describtion:
```
The image is a screenshot of a figure caption from a document or presentation. The caption reads "Figure 60: ViVA-XL calculator buffer" in bold text. The font is black and appears to be a standard sans-serif typeface. The text is centered and clearly legible against a white background. The figure number "60" suggests that this is part of a larger series of figures, and the mention of "ViVA-XL calculator buffer" indicates that the figure likely pertains to a specific feature or component of the ViVA-XL calculator.
```

Action 79: In the **ADE Explorer** window, select the **Name** field and add the expression name BGR\_output as shown in Figure 61.

Action 80: Name the first expression as PSRR\_plot.

The maestro view should now look like this:

| C                                          |          |           |         | Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr maestro_Ac                                              |       |      |      |      | - OX      |
|--------------------------------------------|----------|-----------|---------|-------------------------------------------------------------------------------------------------------|-------|------|------|------|-----------|
|                                            |          |           |         | Launch Session Setup Analyses Variables Outputs Simulation Results Tools EAD Parastics/DE Window Help |       |      |      |      | cadence   |
| ో వి<br>日 :"<br>27                         | してい<br>0 | 0         | Replace | - 17 2<br>(None)                                                                                      |       |      |      |      |           |
| Setup                                      | ? BX     | tb_bgr X  |         | maestro_Ac X                                                                                          |       |      |      |      | 84        |
| Name<br>Value                              |          | Name      | Type    | Details                                                                                               | Value | Plot | Save | Spec | ్రైల్ రెం |
| Filter<br>Filter                           | >        | PSRR_plot | expr    | db(vfreq(ac "/V_BGR"))                                                                                |       | 4    |      |      |           |
| 11<br>TB_BGR_tb_bgr_1                      |          | DC PSRR   | expr    | value(db(vfreq('ac "/V_BGR")) 1)                                                                      |       | <    | 1    |      |           |
| ! Q<br>Simulator spectre                   |          |           |         |                                                                                                       |       |      |      |      | 0         |
| Analyses                                   |          |           |         |                                                                                                       |       |      |      |      | X         |
| 1 1G Automatic Start-Stop<br>vac           |          |           |         |                                                                                                       |       |      |      |      |           |
| Click to add analysis<br>Design Variables  |          |           |         |                                                                                                       |       |      |      |      |           |
| ్రాంగ్ర<br>avdd                            |          |           |         |                                                                                                       |       |      |      |      |           |
| ្រ<br>avss<br>0                            |          |           |         |                                                                                                       |       |      |      |      |           |
| - Click to add variable<br>Parameters<br>ு |          |           |         |                                                                                                       |       |      |      |      |           |

Here is the image describtion:
```
The image is a caption that reads "Figure 61: ADE maestro_Ac view." The text is in bold and appears to be a label or title for a figure in a document, likely referring to a specific view or screenshot from a software or application named "ADE maestro_Ac." The caption is straightforward and does not include any graphical elements or additional context.
```

Action 81: Click **Plot Outputs** . The expressions are plotted as shown in Figure 62.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically the Cadence Virtuoso Visualization & Analysis XL tool, which is used for analyzing electronic circuits. The interface is divided into several sections and contains various graphical elements and data points.

1. **Top Bar**: 
   - The top bar contains the title "Virtuoso (R) Visualization & Analysis XL: TB_BGR tb_bgr maestro_Ac" indicating the tool and the specific test bench being analyzed.
   - There are multiple menu options such as File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
   - Below the menu, there are several icons for quick access to various functions like opening files, saving, zooming, and other analysis tools.

2. **Left Panel**:
   - The left panel is labeled "PSRR_plot" and contains a list of plots. In this case, there is one plot named "PSRR_plot" with a red line indicating it is visible.

3. **Main Graph Area**:
   - The main graph area is divided into two sub-windows.
   - The left sub-window displays a plot with the title "Tue Oct 12 13:05:48 2021". The x-axis is labeled "freq (Hz)" and spans from 10^0 to 10^9 Hz, while the y-axis is labeled "V (dB)" and ranges from -48.0 to -15.0 dB.
   - The plot shows a red line graph representing the Power Supply Rejection Ratio (PSRR) over frequency. There are two markers on the graph:
     - Marker M6 at 1.9953 MHz with a value of -17.293 dB.
     - Marker M5 at 7.9433 Hz with a value of -41.244 dB.
   - The right sub-window is labeled "DC_PSRR" and shows a single data point at (0, -41.244) with a marker M7.

4. **Bottom Bar**:
   - The bottom bar shows the trace information: "Trace: PSRR_plot; History: ExplorerRun0; Test: TB_BGR_tb_bgr_1".
   - There are coordinates for the mouse position (L:) and another set of coordinates (R:).

Overall, the image depicts the analysis of the PSRR of a bandgap reference circuit over a wide frequency range using the Cadence Virtuoso tool. The markers highlight specific points of interest on the graph.
```

#### **Figure 62: Output plots**

Action 82: Close all windows but leave the **Virtuoso** session open for the next lab.

### <span id="page-40-0"></span>**Lab 3: Loop Gain and Phase Measurement of Bandgap Using Stability Analysis**

- Stability analysis is a linear small-signal variant of AC analysis.
- Spectre stability analysis performs a Middlebrook stability analysis.
	- o In this method, if you connect an ideal **0V** voltage source in series with the feedback path and drive it with a **1V** signal at all frequencies, the loop gain transfer function appears across the voltage source terminals.
- Stability analysis measures the open loop gain and phase in the circuit with the loop closed.
	- o The loading in the feedback path is maintained.
	- o A single-ended **iprobe** can be instantiated in the schematic to act as the signal source for the stability analysis.

Action 83: From the Library Manager, open the **TB\_BGR > tb\_bgr > schematic** view.

Action 84: Descend into BGR\_circuit.

BGR\_circuit contains an iprobe, IPRB0, as shown in Figure 63.

Here is the image describtion:
```
The image is a schematic diagram of an electronic circuit, likely designed using a CAD tool for integrated circuit design. Here is a detailed description of the components and connections in the circuit:

1. **Transistors:**
   - There are several MOSFET transistors labeled with their types and dimensions. For example:
     - M15, M14, M5, M12 are PMOS transistors with dimensions (w=2u, l=2u) for M15 and M14, (w=8u, l=2u) for M5, and (w=8u, l=2u) for M12.
     - M0, M1 are NMOS transistors with dimensions (w=4u, l=2u).
     - Q5 and Q4 are bipolar junction transistors (BJTs) with labels vpn2 and vpn2 respectively.

2. **Resistors:**
   - Several resistors are present, labeled with their resistance values and types. For example:
     - R3 with a resistance of 130K.
     - R4 and R1 with a resistance of 44.8K.
     - R2 with a resistance of 5.33333K.

3. **Capacitors:**
   - There is a capacitor labeled C1 with a capacitance of 5pF.

4. **Operational Amplifier:**
   - An operational amplifier (op-amp) is present in the center of the schematic, labeled as "AVDD_BGR" with input pins (inp, inn) and output pin (op).

5. **Power Supply:**
   - The circuit is powered by a supply voltage labeled "vdd" and a ground connection labeled "vss".

6. **Connections:**
   - The circuit has various connections between the components, with nodes labeled for clarity. For example:
     - The output of the op-amp is connected to the gate of the PMOS transistor M12.
     - The source of M12 is connected to the power supply (vdd), and its drain is connected to the output labeled "V_BGR".
     - The resistors R1 and R2 are connected in series between the output "V_BGR" and ground (vss), with a connection to the base of the BJT Q4.

7. **Highlighted Section:**
   - A section of the circuit is highlighted with a red rectangle, indicating a specific area of interest. This section includes a PMOS transistor labeled PRS.

8. **Labels and Annotations:**
   - Various labels and annotations are present to indicate the dimensions of the transistors, the resistance values of the resistors, and the connections between components.

Overall, the schematic appears to be a detailed representation of an analog circuit, possibly a bandgap reference circuit, given the presence of BJTs, resistors, and an op-amp. The circuit is designed to provide a stable reference voltage (V_BGR) that is independent of temperature and supply voltage variations.
```

**Figure 63: Bandgap circuit Schematic for stability analysis (stb)**

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 41

Action 85: From the schematic, select **Launch > ADE Explorer**.

Action 86: In the **Launch ADE Explorer** window that opens, select **Create New View** and click **OK**.

| Launch ADE Explorer |                    |  |
|---------------------|--------------------|--|
| ADE Explorer        |                    |  |
| Create New View     | Open Existing View |  |
| OK                  | Cancel<br>Help     |  |

 **Figure 64: Launching ADE Explorer from schematic window**

Action 87: In the **Create new ADE Explorer view** window, change the view name to maestro\_Stb.

| Library           | TB BGR                                            |
|-------------------|---------------------------------------------------|
| Cell              | tb_bgr                                            |
| View              | maestro Stb                                       |
| lype              | maestro                                           |
| Application       |                                                   |
| Open with         | ADE Explorer                                      |
|                   | Always use this application for this type of file |
| Library path file |                                                   |
|                   | /BGR_Verification_Workshop/cds . lib              |
|                   | Open in new tab current tab _ new window          |

**Figure 65: Opening maestro\_Stb view of tb\_bgr cell** 

The **ADE Explorer** window appears as shown in Figure 66.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically for a project named "TB_BGR tb_bgr maestro_Stb." This software is part of the Cadence Design Systems suite, used for electronic design automation (EDA).

Here are the detailed elements of the interface:

1. **Title Bar**: 
   - The title bar at the top reads "Virtuoso ADE Explorer Editing: TB_BGR tb_bgr maestro_Stb," indicating the current project and file being edited.

2. **Menu Bar**:
   - Below the title bar, there is a menu bar with the following options: Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

3. **Toolbar**:
   - Below the menu bar, there is a toolbar with various icons and options. Some of the visible icons include:
     - A save icon (floppy disk).
     - A red stop sign (possibly for stopping a process).
     - A green play button (likely for running a simulation).
     - A yellow folder (for opening files).
     - A magnifying glass (for search).
     - A replace option with a dropdown menu.
     - A dropdown menu with the label "(None)".
     - An icon for settings or preferences.

4. **Setup Pane**:
   - On the left side of the interface, there is a pane titled "Setup" with a filter option at the top.
   - The setup pane contains a hierarchical tree structure with the following items:
     - TB_BGR_tb_bgr_1
     - Simulator spectre
     - Analyses
     - Design Variables
     - Parameters
     - Corners (checked)
     - Reliability Analyses
     - Monte Carlo Sampling
     - Checks/Asserts

5. **Main Editing Area**:
   - The main editing area is divided into two tabs: "tb_bgr" and "maestro_Stb."
   - The "maestro_Stb" tab is currently active, but the area is empty, indicating no content is displayed or loaded yet.

6. **Details Pane**:
   - On the right side of the interface, there is a vertical toolbar with several icons, including:
     - A pencil (edit).
     - A green checkmark (possibly for validation).
     - A red cross (delete or cancel).
     - A green play button (run).
     - A brown square (stop).
     - A waveform icon (likely for viewing results or waveforms).

Overall, the interface is designed for setting up and running simulations, managing design variables, and analyzing results within the Virtuoso ADE Explorer environment.
```

**Figure 66: ADE Explorer window showing maestro\_Stb view** 

Action 88: In **ADE Explorer**, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a setup window for a simulation or analysis tool. The window is titled "Setup" and contains a hierarchical tree structure with various options and settings.

At the top of the tree, there is an entry labeled "TB_BGR_tb_bgr_1" with an upward-pointing arrow icon next to it. Below this, there is an entry labeled "Simulator spectre" with a green icon that looks like a gear or a cog, indicating that the Spectre simulator is being used.

The next entry is "Analyses," which has a folder icon next to it. Under this entry, there is a highlighted line in yellow that says "Click to add analysis," suggesting that the user can add a new analysis at this point.

Following this, there is an entry labeled "Design Variables" with a folder icon. Under this, there is a line that says "Click to add variable," indicating that the user can add design variables here.

Next, there is an entry labeled "Parameters" with a checked box and a red icon that looks like a stack of papers or documents. This indicates that the parameters section is active or selected.

Below "Parameters," there is an entry labeled "Corners" with a checked box and an icon that looks like a small document with a corner folded over. This suggests that corner analysis is also active or selected.

Further down, there is an entry labeled "Reliability Analyses" with a folder icon, which is currently not expanded or selected.

Under "Reliability Analyses," there is an entry labeled "Monte Carlo Sampling" with a green icon that looks like a scatter plot or a set of data points, indicating that Monte Carlo sampling is an available option but not currently selected.

Finally, there is an entry labeled "Checks/Asserts" with a folder icon, which is also not expanded or selected.

Overall, the image shows a setup interface where the user can configure various aspects of a simulation, including adding analyses, design variables, parameters, corner analyses, reliability analyses, and Monte Carlo sampling.
```

**Figure 67: Opening 'Analyses' form from 'Click to add analysis'**

Action 89: In the **Choosing Analyses** form, select the **stb** analysis and set up the options as follows:

- Set **Sweep Variable** as **Frequency**.
- Select the **Start** frequency **1**Hz and **Stop** frequency for **1G**Hz.
- Choose **Automatic** for **Sweep Type**.
- For **Probe instance/Terminal**, click on **Select** and descend into **schematic** and select **/I18/IPRB0**.
- For selecting **Local Ground Name**, click on **Select** for the **/vss** net.

Action 90: Click **OK**.

| dc<br>ac<br>noise<br>C tran<br>D<br>D<br>Analysis<br>xf<br>sens<br>dcmatch<br>acmatch<br>0<br>stb<br>If<br>pz<br>sp<br>envlp<br>pstb<br>bss<br>pac<br>pnoise<br>pxf<br>dbss<br>psp<br>qpnoise<br>qpac<br>qpxf<br>dbsp<br>hb<br>hbac<br>hbstb<br>hbnoise<br>hbxf<br>hbsp<br>Stability Analysis<br>Sweep Variable<br>Frequency<br>Design Variable<br>Temperature<br>Component Parameter<br>Model Parameter<br>None<br>Sweep Range<br>Start-Stop<br>Stop<br>Start<br>-<br>1 G<br>Center-Span<br>Sweep Type<br>Automatic<br>Add Specific Points<br>Add Points By File<br>Probe Instance/Terminal<br>/I18/IPRB0<br>Select<br>Local Ground Name<br>/vss<br>Select<br>Options<br>Enabled<br>> |  | Choosing Analyses -- ADE Explorer | × |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-----------------------------------|---|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                   |   |
| OK Cancel   Defaults<br>Apply   Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |                                   |   |

#### **Figure 68: Setup of DC-Sweep Analysis**

Action 91: In the **ADE Explorer** window, click on **Variables** and select **Copy From Cellview** as shown in Figure 69.

Action 92: In the **Setup** view assistant, set the **Design Variables** values for **avdd=2** and **avss=0**.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer interface, which is a tool used for analog design and simulation. The interface is divided into several sections and menus, with specific elements highlighted.

1. **Top Menu Bar**: 
   - The top menu bar contains several options: Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, and Tools.
   - The "Variables" menu is currently selected and expanded.

2. **Variables Menu**:
   - The "Variables" menu is highlighted in yellow, indicating it is active.
   - The expanded menu shows several options: Edit, Delete, Find, Copy From Cellview, and Copy To Cellview.
   - The "Copy From Cellview" option is highlighted in yellow, indicating it is the selected action.

3. **Setup Section**:
   - The left side of the interface shows the "Setup" section.
   - It lists the current testbench (TB_BGR_tb_bgr_1) and the simulator being used (spectre).
   - Under "Analyses," a DC analysis is selected with a temperature range from -40 to 120 degrees Celsius and an automatic start-stop feature.
   - The "Design Variables" section lists two variables: "avdd" with a value of 2 and "avss" with a value of 0. These variables are highlighted in yellow.

4. **Toolbar**:
   - Above the "Setup" section, there is a toolbar with various icons and options.
   - A thermometer icon with a value of 27 is visible, likely indicating the current temperature setting.
   - There are icons for saving, running simulations, and other functions.

5. **Right Side**:
   - On the right side, there is a dropdown menu labeled "Replace" and a text field with "maestro_Dc" entered.
   - This section likely pertains to managing different simulation setups or configurations.

Overall, the image shows the user interface of Virtuoso ADE Explorer with a focus on managing design variables and copying them from a cellview.
```

**Figure 69: Copying variables from cell view**

- Action 93: In the **ADE Explorer** window, click on the green button to **netlist and run** the simulation.
- Action 94: Select **Results > Direct Plot > Main Form** in the **ADE Explorer** window as shown in Figure 70 to open **Direct Plot Form**.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically showing the "Results" menu and the "Direct Plot" submenu. The interface appears to be part of a software tool used for electronic design automation (EDA).

1. **Top Menu Bar**: 
   - The top menu bar includes several options: "Simulation," "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help."
   - The "Results" menu is currently selected and expanded.

2. **Results Menu**:
   - The "Results" menu has several options listed vertically:
     - Plot Outputs
     - Direct Plot (highlighted in yellow)
     - Print
     - Annotate
     - Vector
     - Circuit Conditions (grayed out)
     - Electrothermal Report (grayed out)
     - EM/IR Data
     - Save
     - Select
     - Delete
     - Printing/Plotting Options

3. **Direct Plot Submenu**:
   - The "Direct Plot" submenu is expanded to the right, showing various plotting options:
     - Main Form (highlighted in yellow)
     - Transient Signal
     - Transient Minus DC
     - Transient Sum
     - Transient Difference
     - AC Magnitude
     - AC dB10
     - AC dB20
     - AC Phase
     - AC Magnitude & Phase
     - AC Gain & Phase
     - Equivalent Output Noise

4. **Interface Details**:
   - The interface title at the top indicates the current project or file being edited: "Virtuoso ADE Explorer Editing: TB_BGR tb_bgr maestro_Stb."
   - The background of the interface is predominantly gray and white, with some elements highlighted in yellow for emphasis.
   - The "Direct Plot" submenu is bordered in red, indicating it is the active selection.

Overall, the image shows a detailed view of the options available under the "Results" menu in the Virtuoso ADE Explorer, specifically focusing on the "Direct Plot" functionality and its various plotting options.
```

**Figure 70: Opening Direct Plot Form from ADE Explorer**

- Action 95: In the **Direct Plot Form** window, select the following to generate the Bode Plot:
	- **Loop Gain** from **Function**
	- **Magnitude and Phase** as **Modifier**
	- **dB20** as **Magnitude Modifier**
	- Enable **Add To Outputs**.
	- Click on the **Plot** button.

| Plotting Mode<br>Analysis | Append                                  |
|---------------------------|-----------------------------------------|
| C stb                     |                                         |
|                           |                                         |
| Function                  |                                         |
| S                         | Loop Gain Stability Summary             |
|                           | Phase Margin J Gain Margin              |
|                           | J PM Frequency GM Frequency             |
| Modifier                  |                                         |
|                           | Magnitude J Phase @ Magnitude and Phase |
| Magnitude Modifier        |                                         |
| None J dB10 @ dB20        |                                         |
| Add To Outputs            | Plot                                    |

### **Figure 71: Plotting loop gain from Direct Plot Form**

The loop gain waveforms will be plotted as shown in Figure 72.

Action 96: In the **ViVA** window, click **Split Current Strip** to separate the plots.

Action 97: Add single-point markers using the **M** bindkey on the plot.

Action 98: Place a vertical marker using the **V** bindkey on the plot.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso (R) Visualization & Analysis XL software, which is part of the Cadence suite used for electronic design automation. The software is displaying a graphical analysis of a test bench named "TB_BGR_tb_bgr_1" for a bandgap reference circuit.

The main window is divided into several sections:

1. **Top Menu Bar**: This contains various menu options such as File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help. These menus provide access to different functionalities and tools within the software.

2. **Toolbar**: Below the menu bar, there is a toolbar with icons for quick access to common functions. Some of the icons include options for opening files, saving, zooming in and out, and other analysis tools.

3. **Subwindow and Data Point**: There is a small section with a dropdown labeled "Subwindow" and a field labeled "Data Point" with a value of 1.838937MHz. This section allows the user to manage different subwindows and data points within the analysis.

4. **Graphical Display Area**: The main part of the window is dedicated to displaying the graphical results of the analysis. It is divided into two main plots:
   - **Top Plot (Loop Gain Phase)**: This plot shows the phase of the loop gain in degrees (LOOPGAIN (deg)) versus frequency (freq (Hz)). The phase is represented by a red curve. A data point is marked on the curve at approximately 3.46737Hz with a phase of 179.998 degrees, labeled as "M2: 3.46737Hz 179.998deg". Another data point is marked at a higher frequency with a phase of 35.55463 degrees.
   - **Bottom Plot (Loop Gain dB20)**: This plot shows the magnitude of the loop gain in decibels (LOOPGAIN (dB)) versus frequency (freq (Hz)). The magnitude is represented by a yellow curve. A data point is marked on the curve at approximately 2.29087Hz with a magnitude of 27.5172dB, labeled as "M1: 2.29087Hz 27.5172dB". Another data point is marked at a higher frequency with a magnitude of 50.96456m dB.

5. **Left Panel**: This panel lists the different traces being displayed in the graphical area. It includes "Loop Gain Phase" and "Loop Gain dB20" with their respective values and markers.

6. **Bottom Status Bar**: The status bar at the bottom of the window shows information about the current trace being analyzed, the history of the analysis, and the specific test being run ("TB_BGR_tb_bgr_1").

7. **Date and Time**: The top right corner of the graphical display area shows the date and time of the analysis, which is "Tue Oct 12 13:42:52 2021".

Overall, the image provides a detailed view of the loop gain phase and magnitude analysis for a bandgap reference circuit, with specific data points highlighted for further examination.
```

**Figure 72: Loop gain and phase plots in ViVA XL window**

- Action 99: In the **Direct Plot Form** window, select **Phase Margin** as **Function** to show the phase margin value in degrees as shown in Figure 73.
- Action 100: Click on **Add To Outputs** to add the phase margin expression to the maestro view.

|                           | Direct Plot Form              |
|---------------------------|-------------------------------|
| Plotting Mode<br>Analysis | Append                        |
| O stb                     |                               |
| Function                  |                               |
| Loop Gain                 | Stability Summary             |
|                           | Phase Margin   Gain Margin    |
|                           | J PM Frequency J GM Frequency |
|                           | Phase Margin = 35.5313 (Deg)  |
| Add To Outputs            |                               |
|                           | ose Help                      |

**Figure 73: Displayed phase margin in Direct Plot Form**

- Action 101: In the **Direct Plot Form** window, select **Gain Margin** as **Function** to show the gain margin value in **dB** as shown in Figure 74.
- Action 102: Click on **Add To Outputs** to add the gain margin expression to the maestro view.

| Direct Plot Form                                 |                 |
|--------------------------------------------------|-----------------|
| Append<br>Plotting Mode<br>Analysis              |                 |
| O stb                                            |                 |
| Function                                         |                 |
| Loop Gain<br>Stability Summary                   |                 |
| 0<br>Phase Margin J Gain Margin                  |                 |
| PM Frequency GM Frequency                        |                 |
| Gain Margin = 6.87348 (dB)<br>Add To Outputs   Y | Close<br>( Help |

**Figure 74: Displayed gain margin in Direct Plot Form**

Action 103: In the **Direct Plot Form** window, select **Stability Summary** to show both gain and phase margin values along with frequencies as shown in Figure 75.

|                                    | Direct Plot Form<br>X                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------|
| Plotting Mode<br>Analysis<br>O stb | Append                                                                                                  |
| Function                           |                                                                                                         |
| Loop Gain                          | Stability Summary                                                                                       |
|                                    | Phase Margin J Gain Margin                                                                              |
|                                    | PM Frequency O GM Frequency                                                                             |
|                                    | Phase Margin = 35.5313 (Deg) @ freq = 1.8278M (Hz)<br>Gain Margin = 6.87348 (dB) @ freq = 3.37497M (Hz) |
|                                    |                                                                                                         |
|                                    |                                                                                                         |
|                                    | Close (<br>Help                                                                                         |

**Figure 75: Displayed stability summary in Direct Plot Form**

**Note:** In the **Direct Plot Form** window, you can select **PM Frequency** to get just the phase-margin frequency and select **GM Frequency** to get the gain-margin frequency.

Action 104: The **ADE maestro** view will appear as shown in Figure 76.

|                                                                                                        |                         | Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr_ref maestro_Stb |       |                                                                                                                                                                               |         |
|--------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Launch Session Setup Analyses Variables Outputs Simulation Results Tools EAD Parasitics DE Window Help |                         |                                                               |       |                                                                                                                                                                               | cadence |
| 二四是<br>12 27 27 27                                                                                     | Replace                 | · EX - 2<br>▼ (None)                                          |       |                                                                                                                                                                               |         |
| ? BX<br>Setup                                                                                          | Name<br>Type            | Details                                                       | Value | Plot   Save                                                                                                                                                                   | Spec    |
| Name<br>Value                                                                                          | Loop Gain Phase<br>expr | phaseDegUnwrapped(getData("loopGain" ?result "stb"))          | 1 2   | <                                                                                                                                                                             | ੀਕ      |
| * Filter<br>Filter                                                                                     | 1111 oon Gain dB20      | db(maσ(σetData("loonGain" ?result "sto")))                    |       | ಡಿ                                                                                                                                                                            | 1       |
| 1<br>TB_BGR_tb_bgr_1                                                                                   | Phase Margin<br>expr    | getData("phaseMargin" ?result "stb_margin")                   | 35.53 | 4<br>I                                                                                                                                                                        | 20      |
| 6<br>Simulator spectre                                                                                 | Gain Margin<br>expr     | getData("gainMargin" ?result "stb_margin")                    | 6.873 | ﺍﻟﻤﺮﺍﺟﻊ   ﺍﻟﻤﺴﺎﺣﺔ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤﺘﺤﺪﺓ ﺍﻟﻤ |         |
| 白 & Analyses                                                                                           |                         |                                                               |       |                                                                                                                                                                               | ×       |
| v stb<br>1 1G //1 8/IPRB0 Automatic Star                                                               |                         |                                                               |       |                                                                                                                                                                               |         |
| 4 Click to add analysis                                                                                |                         |                                                               |       |                                                                                                                                                                               |         |
| ට විසි Design Variables                                                                                |                         |                                                               |       |                                                                                                                                                                               |         |
| രി<br>avdd                                                                                             |                         |                                                               |       |                                                                                                                                                                               |         |
| 网<br>0<br>વ્યવસ્ત                                                                                      |                         |                                                               |       |                                                                                                                                                                               |         |
| Click to add variable                                                                                  |                         |                                                               |       |                                                                                                                                                                               |         |
| 国网 Parameters                                                                                          |                         |                                                               |       |                                                                                                                                                                               |         |

Here is the image describtion:
```
The image is a caption that reads "Figure 76: ADE maestro_Stb view." The text is in a bold font, indicating that it is likely a title or label for a figure in a document or presentation. The caption suggests that the figure is related to a view or interface within a software or system named "ADE maestro_Stb." There are no other visual elements or details in the image itself.
```

Here is the image describtion:
```
The image appears to be a screenshot of a step or action from a set of instructions or a tutorial. The text is formatted as follows:

- "Action 105:" is written in red, indicating it is a specific step in a sequence of actions.
- "Click Plot Outputs" is written in black, with "Plot Outputs" in bold, suggesting it is an important term or button to be clicked.
- There is a small icon to the right of the text, which appears to be a graphical representation of a plot or chart, possibly indicating the button or link to be clicked.

The overall layout suggests that this is part of a guide or manual, likely related to software or data analysis, where the user is being instructed to click on a specific button labeled "Plot Outputs" to proceed with the task.
```

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically the Virtuoso Visualization & Analysis XL tool from Cadence, used for analyzing electronic circuits. The interface is divided into several sections, each displaying different types of data and controls.

1. **Top Menu Bar**: The top of the interface contains a menu bar with options such as File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help. These menus provide various functionalities for managing and analyzing data.

2. **Toolbar**: Below the menu bar, there is a toolbar with icons for quick access to common functions like opening files, saving, zooming, panning, and other analysis tools. The toolbar also includes a data point selector and a frequency display (1.846525MHz).

3. **Left Panel**: The left panel lists the different data traces available for analysis. In this case, it shows "Loop Gain Phase" and "Loop Gain dB20" with their respective values (35.33123deg and 3.102068m respectively).

4. **Main Graph Area**: The central part of the interface is divided into two main graph areas:
   - **Left Graph**: This graph displays the Loop Gain Phase (in red) and Loop Gain dB20 (in yellow) against frequency (Hz). The x-axis is logarithmic, ranging from 10^1 to 10^9 Hz. The y-axis on the left side shows the Loop Gain Phase in degrees, while the y-axis on the right side shows the Loop Gain in dB. Key points are marked with labels:
     - M3: 12.0202Hz, 179.992deg
     - M6: 7.94328Hz, 27.5172dB
     - V1: 1.846525MHz, 35.33123deg
     - V1: 1.846525MHz, 3.102068m dB
   - **Right Graph**: This graph shows the Phase Margin and Gain Margin. The x-axis is labeled "avss" and the y-axis shows the margin values. Key points are marked with labels:
     - M4: 0.0, 35.531
     - M5: 0.0, 6.8735

5. **Status Bar**: At the bottom of the interface, there is a status bar displaying information about the current trace, history, and test being analyzed. It shows "Trace: Loop Gain Phase; History: ExplorerRun.0; Test: TB_BGR_tb_bgr_1".

6. **Graph Controls**: Above each graph, there are controls for adjusting the view, such as sliders for zooming in and out, and buttons for panning.

Overall, the image shows a detailed analysis of loop gain phase and gain margin for an electronic circuit, with specific data points highlighted for further examination.
```

### **Figure 77: Output plots**

Action 106: Close all windows but leave the **Virtuoso** session open for the next lab.

### <span id="page-50-0"></span>**Lab 4: Transient Noise Measurement of Bandgap**

- Transient noise calculates the effects of large-signal noise on virtually any system. It determines the impact of noise in the time domain. This is an extension to the current **transient analysis** in **Spectre**.
- This section provides an overview of the transient noise analysis setup form in **ADE**. Later, it provides an overview of **Direct Plot Form** (for plotting transient noise results after the transient simulation).

Action 107: From the **Library Manager**, open the **TB\_BGR > tb\_bgr > schematic**  view. The schematic window opens as shown in Figure 78.

Here is the image describtion:
```
The image shows an electronic circuit schematic. Here is a detailed description of the components and connections:

1. **Power Supply Section (Left Side):**
   - There are two voltage sources labeled `V7` and `V8`.
   - `V7` is connected to a node labeled `PPA` and has a voltage value of `vdc=vdd` with an AC magnitude of `acm=1`.
   - `V8` is connected to a node labeled `PBX` and has a voltage value of `vdc=vss`.
   - Both voltage sources are connected to a common ground node.

2. **Bandgap Reference Circuit (Right Side):**
   - The main circuit is enclosed in a green rectangular box labeled `BGR Circuit`.
   - Inside the box, there are two current sources at the top, each represented by a circle with an arrow inside.
   - The left current source is connected to a resistor labeled `I10`.
   - The right current source is connected to a node labeled `V_BGR`.
   - Below the current sources, there are two resistors connected in series.
   - The bottom of the resistors is connected to the `BGR Circuit` block, which likely contains additional components not shown in detail.
   - The node `V_BGR` is connected to a capacitor labeled `C8`, which is connected to ground.

3. **Connections:**
   - The `PPA` node from the power supply section is connected to the top of the `BGR Circuit`.
   - The `PBX` node from the power supply section is connected to the bottom of the `BGR Circuit`.
   - The `V_BGR` node is an output node that provides the bandgap reference voltage.

Overall, the schematic represents a bandgap reference circuit, which is a common circuit used to generate a stable reference voltage that is independent of temperature and supply voltage variations.
```

**Figure 78: Schematic of tb\_bgr cell testbench**

Action 108: From the schematic, select **Launch > ADE Explorer**.

Action 109: In the **Launch ADE Explorer** window, select **Create New View** and click **OK**.

Here is the image describtion:
```
The image is a screenshot of a dialog box titled "Launch ADE Explorer." The dialog box presents two options under the heading "ADE Explorer." The first option is "Create New View," which is selected, as indicated by the filled radio button next to it. The second option is "Open Existing View," which is not selected. Below these options, there are three buttons: "OK" in red, "Cancel" in gray, and "Help" in gray. The "OK" button is highlighted, suggesting it is the default action if the user presses Enter. The overall design of the dialog box is simple and functional, with a focus on providing clear choices for the user.
```

**Figure 79: Launching ADE Explorer from the schematic window**

Action 110: In the **Create new ADE Explorer view** window, change the view name to maestro\_Tran\_Noise and click **OK**.

|                          | Create new ADE Explorer view<br>X                   |
|--------------------------|-----------------------------------------------------|
| File                     |                                                     |
| Library                  | TB BGR                                              |
| Cell                     | tb_bgr                                              |
| View                     | maestro_Tran_Noise                                  |
| Type                     | maestro                                             |
| Application<br>Open with | ADE Explorer                                        |
|                          | _ Always use this application for this type of file |
| Library path file        |                                                     |
|                          | /BGR_Verification_Workshop/cds.lib                  |
|                          | Open in ● new tab ○ current tab ○ new window        |
|                          | Cancel<br>Help                                      |

**Figure 80: Opening maestro\_Tran\_Noise view of the tb\_bgr cell** 

The **ADE Explorer** window opens as shown in Figure 81.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer, a software tool used for analog and mixed-signal design and simulation, specifically for a project named "TB_BGR tb_bgr maestro_Tran_Noise." The interface is divided into several sections:

1. **Top Menu Bar**: This contains various dropdown menus such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help. These menus provide access to different functionalities and settings within the software.

2. **Toolbar**: Below the menu bar, there is a toolbar with icons for common actions like opening, saving, running simulations, and other frequently used commands. The toolbar includes buttons for replacing components, setting up simulations, and other tasks.

3. **Setup Panel (Left Side)**: This panel is labeled "Setup" and contains a hierarchical tree structure. It shows the current testbench (TB_BGR_tb_bgr_1) and its associated settings:
   - **Simulator**: spectre
   - **Analyses**: This section is currently empty, indicating no analyses have been added yet.
   - **Design Variables**: This section is also empty.
   - **Parameters**: This section includes "Corners" and "Reliability Analyses" with "Monte Carlo Sampling" enabled.
   - **Checks/Asserts**: This section is empty.

4. **Main Workspace (Center)**: The central part of the interface is mostly blank, indicating that no specific analyses or results are currently displayed. It has columns for Name, Type, Details, Plot, Save, and Spec, which would typically show details of the simulations or analyses being performed.

5. **Right Sidebar**: This contains vertical icons for various actions such as running simulations, stopping simulations, and plotting results. The icons include:
   - A green play button (Run)
   - A red stop button (Stop)
   - A brown square (possibly for stopping or resetting)
   - A waveform icon (Plot)

6. **Status Bar (Bottom)**: The bottom of the interface has a status bar that shows the current mouse position (L: 17(45)), a message area (M:), and the current project details (R: TB_BGR tb_bgr schematic Simulator: spectre aps).

Overall, the image shows the initial setup stage of a simulation project in the Virtuoso ADE Explorer, with the user preparing to configure and run simulations for a bandgap reference (BGR) circuit.
```

#### **Figure 81: ADE Explorer window showing maestro\_Tran\_Noise view**

In **ADE Explorer**, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant as shown in Figure 82.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a "Setup" window. This window appears to be part of a simulation or analysis tool, likely used in electronic design automation (EDA) or circuit simulation.

Here are the detailed elements of the image:

1. **Title Bar**: The top of the window has a title bar with the label "Setup" and a help icon (a question mark inside a circle) on the right side.

2. **Columns**: Below the title bar, there are two columns labeled "Name" and "Value". Each column has a filter icon (a red downward-pointing triangle) that suggests the ability to filter the contents of the columns.

3. **Tree Structure**: The main part of the window displays a hierarchical tree structure with various nodes and sub-nodes. The nodes are expandable and collapsible, indicated by the small boxes with plus or minus signs next to them.

4. **Nodes and Sub-nodes**:
   - **TB_BGR_tb_bgr_1**: This is the top-level node, likely representing a test bench or a specific simulation setup.
   - **Simulator spectre**: This node indicates the simulator being used, which is "spectre".
   - **Analyses**: This node is expandable and currently has a sub-node labeled "Click to add analysis" highlighted in yellow, suggesting that the user can add a new analysis here.
   - **Design Variables**: This node is expandable and has a sub-node labeled "Click to add variable", indicating that the user can add design variables.
   - **Parameters**: This node is checked, indicating that it is selected or active. It has a sub-node with a thermometer icon, likely representing temperature or another parameter.
   - **Corners**: This node is checked and has a sub-node with a thermometer icon, indicating different operating conditions or process corners.
   - **Reliability Analyses**: This node is expandable but currently collapsed.
   - **Monte Carlo Sampling**: This node is expandable but currently collapsed, indicating that Monte Carlo sampling is part of the reliability analyses.
   - **Checks/Asserts**: This node is expandable but currently collapsed, likely used for verification purposes.

5. **Icons**: Each node has an associated icon that visually represents its function:
   - A house icon for the top-level node.
   - A green gear icon for the simulator.
   - A red analysis icon for analyses.
   - A red design variable icon for design variables.
   - A red checkmark icon for parameters.
   - A red thermometer icon for corners.
   - A green icon for reliability analyses.
   - A green icon for Monte Carlo sampling.
   - A green icon for checks/asserts.

Overall, the image shows a setup interface for configuring simulations, analyses, and design variables in an EDA tool.
```

#### **Figure 82: Opening 'Analyses' form from 'Click to add analysis'**

Action 111: In the **Choosing Analyses** form, select the **tran** analysis in **Choosing Analyses** form & set the following options as below:

- Enable the **Transient Noise** checkbox.
- Set **Noise Fmax** to **163.84M**.
- Enable the **Fourier Analysis Settings** checkbox.
- Set **Circuit Fundamental Frequency** to **10K**, **PSD Max Frequency** to **100M**, and **PSD Min Frequency** to **10K**.
- Click **OK**.

For more information about setting up transient noise, refer to the article, [Setting up](https://support.cadence.com/apex/ArticleAttachmentPortal?id=a1Od0000002JfiMEAS&pageName=ArticleContent)  [transient noise on a bandgap circuit,](https://support.cadence.com/apex/ArticleAttachmentPortal?id=a1Od0000002JfiMEAS&pageName=ArticleContent) to get an understanding of parameters values related to transient noise analyses, that is, Noise Fmax, PSD Max Frequency, and so on.

| Analysis           | ● tran                              | O dc                 | ac                                                            |    | noise   |
|--------------------|-------------------------------------|----------------------|---------------------------------------------------------------|----|---------|
|                    | xf                                  | sens                 | dcmatch                                                       |    | acmatch |
|                    | stb                                 | pz                   | If                                                            | sp |         |
|                    | envip                               | 555                  | pac                                                           |    | pstb    |
|                    | pnoise                              | pxf                  | psp                                                           |    | dbss    |
|                    | qpac                                | qpnoise O            | qpxf                                                          |    | dbsp    |
|                    | hb                                  | ) hbac               | Chbstb                                                        |    | hbnoise |
|                    | hbsp                                | / hbxf               |                                                               |    |         |
|                    |                                     | Transient Analysis   |                                                               |    |         |
| Stop Time          | 1.8m                                |                      |                                                               |    |         |
|                    |                                     |                      |                                                               |    |         |
|                    | Accuracy Defaults (errpreset)       |                      |                                                               |    |         |
|                    | _ conservative _ moderate _ liberal |                      |                                                               |    |         |
|                    |                                     |                      |                                                               |    |         |
| Transient Noise    |                                     |                      |                                                               |    |         |
| Noise Fmax         | 163.84M                             |                      | Tran noise Options                                            |    |         |
|                    | Fourier Analysis Settings           |                      |                                                               |    |         |
|                    |                                     |                      |                                                               |    |         |
|                    | Circuit Fundamental Frequency       |                      | 10K                                                           |    |         |
| _ PSD Start Time   |                                     |                      | 100u                                                          |    |         |
|                    |                                     | Sampling Settings    |                                                               |    |         |
| PSD Max Frequency  |                                     |                      | 100M                                                          |    |         |
|                    |                                     |                      |                                                               |    |         |
|                    | PSD Min Frequency                   |                      | 10K                                                           |    |         |
|                    |                                     |                      | Tran Stop Time will be calculated automatically when enabled. |    |         |
|                    |                                     |                      |                                                               |    |         |
| Strobe             |                                     |                      |                                                               |    |         |
|                    |                                     |                      |                                                               |    |         |
|                    |                                     | PSD Period Averaging |                                                               |    |         |
|                    | Number of PSD Windows               |                      | 16                                                            |    |         |
|                    |                                     | PSD Summary          |                                                               |    |         |
| PSD Start Time     |                                     | 100u                 | PSD Stop Time                                                 |    | 1.7m    |
|                    |                                     |                      |                                                               |    |         |
| PSD Min Freq       |                                     | 10K                  | PSD Max Freq                                                  |    | 100M    |
|                    | Number of Samples                   | 320000               | Window Size                                                   |    | 20000   |
|                    |                                     |                      |                                                               |    |         |
| _ Multiple Runs    |                                     |                      |                                                               |    |         |
|                    | Number of Runs                      | 100                  |                                                               |    |         |
| Noise Contribution |                                     | _ on _ off           |                                                               |    |         |

**Figure 83: Setup of transient noise analysis**

Action 112: In the **ADE Explorer** window, click on **Variables** and select **Copy From Cellview** as shown in Figure 84.

In the **Setup** view assistant, set the **Design Variables** values for **avdd=2** and **avss=0**.

**Figure 84: Copying variables from cell view**

- Action 113: In the **ADE Explorer** window, click on the green button to **netlist and run** the simulation.
- Action 114: Once the simulation finishes, click on **Simulation > Output Log** in the **ADE Explorer** window as shown in Figure 85. Verify that simulation has completed with 0 errors.

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically focusing on the "Simulation" menu. Here is a detailed description:

1. **Interface Title**: At the top, the title bar reads "Virtuoso® ADE Explorer Editing:" indicating the software and the specific module being used.

2. **Menu Bar**: Below the title bar, there is a menu bar with several options. The highlighted option is "Simulation," which is selected and expanded.

3. **Simulation Menu**: The "Simulation" menu is expanded, showing a list of options related to simulation tasks. The options listed in the menu are:
   - **Netlist and Run**: Likely used to generate a netlist and start the simulation.
   - **Run**: To start the simulation.
   - **Stop**: To stop the simulation.
   - **Suspend**: (grayed out, indicating it is not currently available).
   - **Resume**: (grayed out, indicating it is not currently available).
   - **Run Preview**: To preview the run settings or parameters.
   - **MDL Control**: (with a submenu indicated by a right arrow).
   - **Options**: (with a submenu indicated by a right arrow).
   - **Netlist**: (with a submenu indicated by a right arrow).
   - **Output Log**: Highlighted in yellow, suggesting it is the current selection or focus.
   - **Linter Log**: (with a submenu indicated by a right arrow).
   - **Convergence Aids**: (with a submenu indicated by a right arrow).
   - **Diagnostics**: (with a submenu indicated by a right arrow).

4. **Highlighted Items**: The "Simulation" menu item and the "Output Log" option within the menu are both highlighted in yellow, drawing attention to them.

5. **Additional Interface Elements**: To the right of the menu, there are additional interface elements, including a dropdown menu labeled "(None)" and a "Details" section, though these are not the primary focus of the image.

Overall, the image provides a clear view of the "Simulation" menu within the Virtuoso ADE Explorer Editing interface, with a specific focus on the "Output Log" option.
```

**Figure 85: Opening simulation log file from ADE Explorer window**

Action 115: Click **Results > Direct Plot > Main Form** in the **ADE Explorer** window as shown in Figure 86 to open the **Direct Plot** form.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from a tool used for electronic circuit simulation and analysis. The interface appears to be from a program related to Cadence Design Systems, which is commonly used for electronic design automation (EDA).

Here is a detailed description of the image:

1. **Menu Bar**: At the top of the interface, there is a menu bar with several options:
   - Results
   - Tools
   - EAD
   - Parasitics/LDE
   - Window
   - Help

2. **Highlighted Menu**: The "Results" menu is selected, and it has a dropdown menu open. Within this dropdown, the "Direct Plot" option is highlighted, indicating that it is selected.

3. **Submenu**: The "Direct Plot" option has a submenu that is also open. This submenu contains several options:
   - Main Form ...
   - Transient Signal
   - Transient Minus DC
   - Transient Sum
   - Transient Difference
   - AC Magnitude
   - AC dB10
   - AC dB20
   - AC Phase
   - AC Magnitude & Phase
   - AC Gain & Phase
   - Equivalent Output Noise
   - Equivalent Input Noise
   - Squared Output Noise
   - Squared Input Noise
   - Noise Figure
   - DC

4. **Highlighted Options**: Within the submenu, the "Main Form ..." option is highlighted, indicating that it is selected or about to be selected.

5. **Window Title**: The title of the window in the background is "TB_BGR tb_bgr maestro_Tran_Noise," which suggests that the user is working on a test bench (TB) for a bandgap reference (BGR) circuit, and they are analyzing transient noise.

6. **Interface Design**: The interface uses a combination of white, grey, and red colors. The highlighted options are marked with a yellow background, making them stand out from the rest of the menu items.

Overall, the image shows a user navigating through the "Results" menu to access the "Direct Plot" options in an electronic circuit simulation tool, likely to plot or analyze specific aspects of the circuit's performance.
```

**Figure 86: Opening Direct Plot Form from ADE Explorer window**

Action 116: In the **Direct Plot Form** window, select **Transient Noise** as **Function**.

Action 117: Select **Net** from the drop-down.

**Direct Plot Form** will look as shown in Figure 87 with the default PSD settings. Do not change these settings.

Action 118: Click on **Add To Outputs** to add the transient noise expression to the maestro view.

| Direct Plot Form<br>×     |                    |  |
|---------------------------|--------------------|--|
| Plotting Mode<br>Analysis | Append             |  |
| tran<br>O                 |                    |  |
| Function                  |                    |  |
| Voltage                   | Current            |  |
| Power                     | Noise Measurement  |  |
| O Transient Noise         |                    |  |
| · PSD C PN                |                    |  |
| Net<br>Select             |                    |  |
| PSD Default Settings      |                    |  |
| Fundamental Freq          | 10K                |  |
| Bin Number                | 16                 |  |
| Sample per Period         | 20K                |  |
| Detailed Settings         |                    |  |
| From                      | 100u               |  |
| To                        | 1 . 7 m            |  |
| Number of Samples         | 320000             |  |
| Window Type               | Rectangular        |  |
| Smoothing Factor          | 1                  |  |
| Window Size               | 20000              |  |
| Detrending Mode           | None               |  |
| Coherent Gain             | (none)             |  |
| Coherent Gain Factor 0    |                    |  |
| Add To Outputs &          | Default<br>(Replot |  |
| > Select Net on schematic |                    |  |
|                           | Close<br>Help      |  |

#### **Figure 87: Plotting output noise from Direct Plot Form**

Action 119: Select the **/V\_BGR** net from the **schematic** window.

Action 120: The Output Noise plot (in dB) will appear as shown in Figure 88.

Action 121: Place single-point markers on the plot using the **M** bindkey.

Here is the image describtion:
```
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL tool, which is used for analyzing electronic circuits. The specific analysis being displayed is a transient noise response of a circuit, likely a bandgap reference (BGR) circuit, as indicated by the file name "TB_BGR_tb_bgr_1" and the title bar.

The main part of the image is a graph plotting the power spectral density (PSD) in decibels (dB) against frequency in megahertz (MHz). The y-axis represents the PSD in dB, ranging from -190 dB to -30 dB. The x-axis represents the frequency, ranging from 0 to 100 MHz.

The graph shows a green trace that starts at a high value on the left (low frequency) and gradually decreases as the frequency increases. There are two markers on the graph:
- M1 at 15.62 MHz with a value of -161.876 dB.
- M2 at 91.95 MHz with a value of -180.564 dB.

The toolbar at the top of the window contains various icons and options for manipulating the graph, such as zooming, panning, and adding markers. The left sidebar lists the "Transient Response" with a single entry for the noise analysis.

At the bottom of the window, there is a status bar displaying details about the trace being analyzed, including the specific parameters and settings used for the analysis.

Overall, the image shows a detailed analysis of the noise performance of a circuit over a range of frequencies, with specific points of interest marked for further examination.
```

**Figure 88: Output transient noise plot in ViVA XL**

Action 122: Rename this expression in the maestro view to Tran\_Noise\_Plot as shown in Figure 89.

| Virtuoso® ADE Explorer Editing: TB_BGR tb_bgr_ref maestro_Tran_Noise                                                                                                                                                                 |                                                                                                                                        |                               |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--|
| Launch Session Setyp Analyses Variables Qutputs Simulation Results Tools EAD Parastics/LDE Window Help                                                                                                                               |                                                                                                                                        | cadence                       |  |
| 1/2 2 日 - 8 27 2 2 2 2 2 2 2 1 - 8 P P 1 - 8 P Replace<br>(None) (None) (2                                                                                                                                                           |                                                                                                                                        |                               |  |
| x BX<br>Setup<br>Name<br>Type<br>Tran_Noise_Plot<br>expr<br>Name<br>Value<br>><br>ilter<br>i ter<br>↑ TB BGR tb bgr_1<br>Simulator spectre<br>白 Analyses<br>tran<br>0 1.8m<br>L Click to add analysis<br>白晶 Design Variables<br>avdd | Value<br>Details<br>Plot   Save<br> db10(psd(VT("/V_BGR")0.0001 0.0017 320000 ?windowName "Rectangular" ?smooth 1 ?windowSiz<br>y<br>1 | Spec<br>2 Days<br>C<br>G<br>× |  |

#### **Figure 89: ADE maestro\_Tran\_Noise view**

Action 123: In the **ADE Explorer** window, click **Plot Outputs** .

Action 124: **Close** all windows and the **Virtuoso** session.

This concludes the RAK.

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 58

### <span id="page-58-0"></span>**References**

- 1. [Spectre Classic Simulator, Spectre Accelerated Parallel Simulator \(APS\), and](https://support.cadence.com/apex/techpubDocViewerPage?xmlName=spectreuser.xml&title=Spectre%20Classic%20Simulator,%20Spectre%20APS,%20Spectre%20X,%20and%20Spectre%20XPS%20User%20Guide%20--%20The%20Spectre%20X%20Circuit%20Simulator%20-%20Migrating%20from%20Spectre%20APS&hash=pgfId-1087925&c_version=20.1&path=spectreuser/spectreuser20.1/spectrex.html#pgfId-1087925)  [Spectre Extensive Partitioning Simulator \(XPS\) User Guide](https://support.cadence.com/apex/techpubDocViewerPage?xmlName=spectreuser.xml&title=Spectre%20Classic%20Simulator,%20Spectre%20APS,%20Spectre%20X,%20and%20Spectre%20XPS%20User%20Guide%20--%20The%20Spectre%20X%20Circuit%20Simulator%20-%20Migrating%20from%20Spectre%20APS&hash=pgfId-1087925&c_version=20.1&path=spectreuser/spectreuser20.1/spectrex.html#pgfId-1087925)
- 2. [Virtuoso ADE Explorer User Guide](https://support.cadence.com/apex/techpubDocViewerPage?xmlName=explorer.xml&title=Virtuoso%20ADE%20Explorer%20User%20Guide%20--%20Setting%20Up%20Explorer%20Environment%20-%20Setting%20Up%20Explorer%20Environment&hash=pgfId-1041651&c_version=ICADVM20.1&path=Explorer/ExplorerICADVM20.1/chap2.html#pgfId-1041651)
- 3. [Virtuoso Visualization and Analysis XL User Guide](https://support.cadence.com/apex/techpubDocViewerPage?xmlName=vivaxlug.xml&title=Virtuoso%20Visualization%20and%20Analysis%20XL%20User%20Guide%20--%20Calculator%20Functions%20-%20Calculator%20Functions&hash=pgfId-1234892&c_version=IC6.1.8&path=vivaxlug/vivaxlugIC6.1.8/appD.html#pgfId-1234892)
- 4. [Setting up transient noise on a bandgap circuit](https://support.cadence.com/apex/ArticleAttachmentPortal?id=a1Od0000002JfiMEAS&pageName=ArticleContent)

### <span id="page-58-1"></span>**Supports**

Cadence Learning and Support Portal provides access to support resources, including an extensive knowledge base, access to software updates for Cadence products, and the ability to interact with Cadence Customer Support. Visit [https://support.cadence.com](https://support.cadence.com/).

### <span id="page-58-2"></span>**Feedback**

Email comments, questions, and suggestions to [content\\_feedback@cadence.com.](mailto:content_feedback@cadence.com)