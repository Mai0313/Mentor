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
The image depicts a schematic diagram of an electronic circuit, likely designed using a circuit design software. The diagram is displayed on a black grid background, which is typical for such software to help with component placement and alignment.

The circuit is divided into two main sections:

1. **Left Section:**
   - This section contains two voltage sources labeled V7 and V3.
   - V7 is set to a voltage of "vdd" with an AC magnitude of 1.
   - V3 is set to a voltage of "vee".
   - Both voltage sources are connected to a common ground.
   - The nodes are labeled PPA and PPA (likely a typo, as they should be different) and are connected to the right section of the circuit.

2. **Right Section:**
   - This section is enclosed in a green rectangular box labeled "BGR Circuit," which stands for Bandgap Reference Circuit.
   - Inside the BGR Circuit, there are two current sources and several resistors arranged in a specific configuration.
   - The top of the BGR Circuit has a node labeled PPA, which connects to the left section.
   - The right side of the BGR Circuit has a node labeled V_BGR, which connects to a capacitor labeled C8 that is grounded.
   - The bottom of the BGR Circuit has a node labeled V3, which also connects to the left section.

The circuit appears to be a part of a larger design, possibly for generating a stable reference voltage using a bandgap reference circuit. The labels and connections suggest that the circuit is designed to provide a stable output voltage (V_BGR) that is less sensitive to temperature variations and supply voltage changes.
```

Here is the image describtion:
```
The image is a caption that reads "Figure 1: Bandgap testbench schematic." It is written in black text on a white background. The text is bold and appears to be a title or label for a figure in a document, likely indicating that the accompanying figure is a schematic diagram related to a bandgap testbench. There is no actual schematic or diagram visible in the image provided, only the caption.
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
The image is a screenshot of the Cadence Virtuoso ADE Explorer software interface. The title bar at the top indicates that the current project is "TB_BGR tb_bgr maestro_Dc." The interface is divided into several sections:

1. **Menu Bar**: At the top, there is a menu bar with various options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

2. **Setup Menu**: The "Setup" menu is expanded, showing a dropdown list of options including:
   - Job Setup
   - Design
   - Simulator
   - Save Options
   - High-Performance Simulation
   - Model Libraries (highlighted in yellow)
   - Temperature
   - Stimuli
   - Simulation Files
   - EM/IR Analysis
   - MATLAB/Simulink
   - Environment

3. **Toolbar**: Below the menu bar, there is a toolbar with icons for various functions such as Replace, and a dropdown menu currently set to "(None)." There are also icons for other actions, but their specific functions are not clear from the image.

4. **Left Panel**: On the left side, there is a panel with a list of items under "Setup," including:
   - TB_BGR_tb_bgr
   - Simulator
   - Analyses
   - Design Variables
   - Parameters
   - Corners
   - Reliability Analysis
   - Monte Carlo
   - Checks/Asserts

5. **Main Workspace**: The main workspace area is mostly blank, with a tab labeled "maestro_Dc" open. There is a "Details" column header, but no specific details are visible in the workspace.

6. **Right Panel**: On the right side, there are icons for various actions, including what appears to be options for AC, DC, and Transient analysis, as well as icons for running simulations and viewing results.

The overall interface is designed for setting up and running simulations, managing design variables, and analyzing results within the Cadence Virtuoso ADE Explorer environment.
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
The image shows a screenshot of a software interface, specifically a setup window for a simulation or analysis tool. The window is titled "Setup" and contains a hierarchical list of options and settings.

At the top of the list, there is an entry labeled "TB_BGR_tb_bgr_1" with an upward-pointing arrow icon next to it, indicating it might be a project or file name.

Below that, there is an entry labeled "Simulator spectre" with a green icon resembling a gear or a tool, suggesting it is the selected simulator.

Next, there is a section labeled "Analyses" with a green icon that looks like a graph or chart. Under this section, there is a highlighted yellow text that says "Click to add analysis," indicating that the user can add a new analysis here.

Following that, there is a section labeled "Design Variables" with a red icon that looks like a set of sliders or controls. Under this section, there is a text that says "Click to add variable," suggesting that the user can add new design variables.

Within the "Design Variables" section, there are two sub-sections: "Parameters" and "Corners." The "Parameters" sub-section has a red checkmark icon next to it, indicating it is selected or active. The "Corners" sub-section has a red checkmark icon and a small icon that looks like a document or a piece of paper.

Further down, there is a section labeled "Reliability Analyses" with a green icon that looks like a graph or chart. Under this section, there is a sub-section labeled "Monte Carlo Sampling" with a green icon that looks like a dice or a randomization symbol.

At the bottom of the list, there is a section labeled "Checks/Asserts" with a red checkmark icon, indicating it is selected or active.

The window also has columns labeled "Name" and "Value" with filter options at the top, suggesting that the user can filter the list based on these columns.
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
The image is a screenshot of the Virtuoso ADE Explorer software interface, specifically showing the editing environment for a project named "TB_BGR tb_bgr maestro_Dc." The interface is divided into several sections:

1. **Top Menu Bar**: This contains various menu options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help. The "Outputs" menu is currently expanded, showing options like Add, Delete, Import, Export, Send To Expression Editor, To Be Saved, To Be Plotted, and Save All (highlighted in yellow).

2. **Setup Panel (Left Side)**: This panel lists the setup components for the project. It includes:
   - A filter option at the top.
   - A hierarchical tree structure showing:
     - The test bench "TB_BGR_tb_bgr_1."
     - The simulator being used, which is "spectre."
     - The analyses being performed, specifically a DC analysis with a temperature range from -40 to 120 degrees Celsius and an automatic start-stop feature.
     - Design Variables, which include Parameters, Corners, Reliability Analyses, Monte Carlo Sampling, and Checks/Asserts.

3. **Main Workspace (Right Side)**: This is a large, mostly empty area labeled "Details," which is likely where detailed information or results would be displayed.

4. **Toolbar (Above the Main Workspace)**: This contains various icons for different functions, such as adding, deleting, and other operations. There is also a dropdown menu labeled "(None)" and a search bar.

5. **Right Sidebar**: This contains additional tool icons, including options for running simulations, stopping processes, and other actions.

The overall interface is designed for managing and analyzing electronic design automation (EDA) projects, with a focus on setting up simulations, defining variables, and handling outputs.
```

Here is the image describtion:
```
The image is a text label that reads "Figure 9: Options for saving outputs." The text is in a bold, black font, indicating that it is likely a caption or title for a figure in a document or presentation. The label suggests that the figure it refers to provides information or options related to saving outputs, possibly in a software or data processing context.
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
The image is a screenshot of the Virtuoso ADE Explorer Editing interface, specifically for a project named "TB_BGR tb_bgr maestro_Dc." The interface is part of the Cadence design environment, used for electronic design automation.

At the top of the interface, there is a menu bar with various options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help. The "Variables" menu is currently open, showing options like Edit, Delete, Find, Copy From Cellview, and Copy To Cellview. The "Copy From Cellview" option is highlighted.

Below the menu bar, there is a toolbar with icons for different functions, including a replace function, a drop-down menu for selecting different views, and a search bar. The toolbar also includes icons for running simulations and other tasks.

The main part of the interface is divided into two sections. The left section, labeled "Setup," contains a hierarchical tree structure with various elements related to the project. These elements include:
- TB_BGR_tb_bgr_1 (the testbench)
- Simulator (spectre)
- Analyses (with a sub-item "dc" and a range of -40 to 120 for Automatic Start-Stop)
- Design Variables (with variables "avdd" set to 2 and "avss" set to 0, both highlighted in yellow)
- Parameters
- Corners
- Reliability Analyses
- Monte Carlo Sampling
- Checks/Asserts

The right section of the interface is currently empty, with a placeholder for "maestro_Dc" under the "Type" column, but no details are filled in.

Overall, the image shows a detailed view of the setup and configuration options available in the Virtuoso ADE Explorer for a specific electronic design project.
```

#### **Figure 11: Copying variables from cell view**

- Action 17: In the **ADE Explorer** window, click on the green arrow button to **netlist and run** the simulation.
- Action 18: In the **ADE Explorer** window, choose **Results > Direct Plot > Main Form** to open the **Direct Plot** form as shown in Figure 12.

Here is the image describtion:
```
The image shows a screenshot of a software interface, specifically a menu related to plotting results in a simulation environment. The title bar at the top indicates that the software is "Explorer Editing: TB_BGR tb_bgr maestro_Dc."

The menu bar below the title bar contains several options: "Simulation," "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is expanded, revealing a dropdown list of options. The highlighted option in this list is "Direct Plot," which is selected.

Upon selecting "Direct Plot," a secondary menu appears to the right, titled "Direct Plot." This menu contains a list of plotting options under the heading "Main Form ...". The options listed are:
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

The interface appears to be part of a simulation or design tool, likely used for electrical or electronic circuit analysis, given the context of the options available for plotting various signal and noise characteristics.
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
The image is a screenshot of a software interface from Cadence Virtuoso, specifically the Visualization & Analysis XL tool. The interface is displaying a graph of a DC response analysis for a test bench named "TB_BGR_tb_bgr_1".

Here are the detailed observations:

1. **Software Interface**:
   - The title bar at the top reads "Virtuoso (R) Visualization & Analysis XL: TB_BGR_tb_bgr maestro_Dc".
   - The Cadence logo is visible in the top right corner.
   - The menu bar includes options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
   - Below the menu bar, there is a toolbar with various icons for different functions, such as zoom, pan, and data point selection.

2. **Graph Details**:
   - The graph is labeled "DC Response" on the left side.
   - The x-axis represents temperature (temp) in degrees Celsius (C), ranging from -40.0 to 120.0.
   - The y-axis represents voltage (V) in volts (V), ranging from approximately 1.17875 to 1.1825.
   - The graph shows a single curve (green line) that forms a parabolic shape, peaking at around 40.0°C with a voltage of approximately 1.182303V.
   - There are markers on the graph indicating specific data points:
     - A red marker at the peak (40.0°C, 1.182303V).
     - A blue marker at the right end (120.0°C, 1.178871V).
     - A purple marker indicating a delta (dx: 80.0°C, dy: 3.43138662mV, slope: 42.8923327uV/C).

3. **Additional Interface Elements**:
   - On the left side, there is a panel titled "DC Response" with a list of names, currently showing "v" and "V_BGR; dc (V)".
   - The toolbar above the graph includes options for different graph types and settings, with the "Classic" view selected.
   - The status bar at the bottom shows mouse coordinates (L: 18(48), M:, R:).

Overall, the image depicts a detailed analysis of a DC response in a temperature sweep, showing how the voltage varies with temperature for a specific circuit or component.
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
The image shows a screenshot of a software interface, likely related to data analysis or signal processing. The interface includes several buttons and options at the top, such as "Off," "Family," "Wave," "Clip," "Append," and "Rectangular." There is also a gear icon highlighted with a red box, indicating it might be a settings or configuration button.

Below the toolbar, there is a text input area where a command is written in a programming or scripting language. The command shown is:
```
ymax(v("V_BGR"?result "dc"))
```
This suggests that the user is working with some form of data manipulation or analysis, possibly involving variables and functions.

On the left side of the interface, there is a small section labeled "Key P..." with buttons numbered 7, 8, 9, and a division symbol (/), which might be part of a virtual keypad or a quick access panel for numerical input.

The overall design and elements suggest that this software is used for technical or scientific purposes, involving data entry, manipulation, and possibly visualization.
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
The image is a screenshot of the Virtuoso ADE Explorer Editing interface from Cadence. The interface is divided into two main sections: the left panel titled "Setup" and the right panel showing tabs for "tb_bgr" and "maestro_Dc".

In the left panel under "Setup," there is a hierarchical list of settings and parameters for a simulation setup named "TB_BGR_tb_bgr_1." The list includes:
- "Simulator spectre" indicating the simulator being used.
- "Analyses" with a checked "dc" analysis, which has parameters t=-40, 120, 10 Linear Step Size Start.
- "Design Variables" with variables "avdd" set to 2 and "avss" set to 0.
- "Parameters" and "Corners" sections.
- "Reliability Analyses" with "Monte Carlo Sampling" checked.
- "Checks/Asserts" section.

The right panel shows the "maestro_Dc" tab, which lists expressions related to the simulation. There are two highlighted entries:
1. "BGR_output" with three expressions:
   - v("V_BGR" ?result "dc")
   - ymax(v("V_BGR" ?result "dc"))
   - ymin(v("V_BGR" ?result "dc"))
2. "BGR_variation" with one expression:
   - (ymax(v("V_BGR" ?result "dc")) - ymin(v("V_BGR" ?result "dc")))

The interface also includes a toolbar at the top with various icons for launching, session management, setup, analyses, variables, outputs, simulation, results, tools, EAD, Parasitics/LDE, window, and help options. The Cadence logo is visible in the top right corner.
```

**Figure 20: ADE maestro\_Dc view**

Action 32: Close the **ViVA** window.

Action 33: In the **ADE Explorer** window, click on the **Add outputs** icon and select **OP Parameters**.

Here is the image describtion:
```
The image shows a user interface menu from a software application, likely related to engineering or data analysis. The menu is displayed in a vertical layout with various options listed. Each option is accompanied by an icon to its left for visual identification. The options listed in the menu are:

1. Expression (icon: f0)
2. Signal (icon: a waveform)
3. OCEAN script (icon: a document with "SKILL" written on it)
4. MATLAB expression (icon: f0)
5. MATLAB script (icon: a document)
6. Area Specification (icon: a grid or area)
7. Op Region Spec (icon: a region or area)
8. Violation Filter (icon: an exclamation mark)
9. OP Parameters (icon: highlighted in yellow)

The menu is enclosed in a red border, and the "OP Parameters" option is specifically highlighted with a yellow background, indicating it is either selected or emphasized for attention. On the left side of the menu, there are additional icons for other functionalities, including a pencil, a cross, a play button, a stop button, and a waveform.
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
The image shows a screenshot of a software interface, specifically from a tool used for circuit simulation and analysis. The title bar at the top indicates that the software is in "Explorer Editing" mode for a project named "TB_BGR tb_bgr maestro_Dc."

Below the title bar, there is a menu bar with several options: "Simulation," "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is highlighted, indicating that it is currently selected.

A dropdown menu is open under the "Results" menu, displaying several options:
- Plot Outputs
- Direct Plot (highlighted in yellow)
- Print
- Annotate
- Vector
- Circuit Conditions...
- Electrothermal Report...
- EM/IR Data
- Save...
- Select...
- Delete...
- Printing/Plotting Options...

To the right of this dropdown menu, another panel titled "Direct Plot" is open. This panel lists various plotting options under the "Main Form..." heading:
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

The interface appears to be part of a software tool used for analyzing and plotting different aspects of circuit simulations, such as transient signals, AC characteristics, and noise figures.
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
The image depicts an electronic circuit schematic. The schematic is divided into two main sections:

1. **Left Section:**
   - This section contains a power supply arrangement.
   - There are two voltage sources labeled "vdc=vdd" and "vdc=avss".
   - The "vdc=vdd" source is connected to a node labeled "PPA" and is grounded.
   - The "vdc=avss" source is connected to a node labeled "SSA" and is also grounded.
   - The connections are highlighted with red dots at the nodes.

2. **Right Section:**
   - This section contains a circuit labeled "BGR Circuit" which stands for Bandgap Reference Circuit.
   - The BGR Circuit is enclosed in a green rectangular box.
   - At the top of the BGR Circuit, there is a current source labeled "I18" connected to a node labeled "vdd".
   - Inside the BGR Circuit, there are two current sources and several resistors arranged in a specific configuration.
   - The output of the BGR Circuit is labeled "V_BGR" and is connected to a capacitor labeled "c=1p" and a node labeled "gnd" (ground).
   - The "V_BGR" node is also connected to the right side of the schematic.

Overall, the schematic shows a power supply section on the left and a Bandgap Reference Circuit on the right, with connections and components clearly labeled.
```

**Figure 29: Plotting supply current**

The waveform is plotted as shown in Figure 30. The "i("/V7/PLUS" ?result "dc")" supply current expression is added to the **Outputs Setup** table in ADE Explorer.

Here is the image describtion:
```
The image is a screenshot of a graph from the Virtuoso Visualization & Analysis XL software, which is used for electronic design automation. The graph displays the results of a DC analysis over a temperature range from -40°C to 120°C.

Key elements of the image include:

1. **Graph Title and Software Information**:
   - The title bar at the top reads "Virtuoso (R) Visualization & Analysis XL: TB BGR tb_bgr maestro_Dc".
   - The software is identified as Cadence, a well-known EDA tool.

2. **Graph Details**:
   - The x-axis represents temperature (temp) in degrees Celsius (°C), ranging from -40°C to 120°C.
   - The y-axis represents current (I) in microamperes (µA), ranging from approximately -81.5 µA to -75.5 µA.
   - The graph shows a single trace labeled "i/V7/PLUS" with a purple line.

3. **Data Points and Annotations**:
   - There are two marked data points on the graph:
     - At -40.0°C, the current is -75.92529 µA.
     - At 120.0°C, the current is -81.23888 µA.
   - An annotation indicates the change in current (dy) over the temperature range (dx) with values: dx = 160.0°C, dy = 5.313584 µA, and a slope (s) of 33.2099 nA/°C.

4. **Graphical User Interface (GUI)**:
   - The GUI includes various toolbars and menus for file operations, editing, viewing, graphing, axis adjustments, tracing, markers, measurements, tools, window management, and browsing.
   - There are icons for different functions such as zooming, panning, and data point selection.
   - The left panel shows the trace name "i/V7/PLUS" with a filter icon.

5. **Additional Information**:
   - The bottom of the image shows a status bar with details about the trace, history, test, design point, and corner.

Overall, the image provides a detailed view of the current versus temperature analysis for a specific electronic component or circuit, with clear annotations and a user-friendly interface for further analysis and exploration.
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
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL tool, which is used for analyzing electronic circuits. The interface is divided into two main sections, each displaying different graphs and data points.

1. **Left Section:**
   - This section shows a scatter plot with the title "BGR_variation:ymin(v("/V_BGR")...ymax(v("/V_BGR")?result "dc")".
   - The x-axis is labeled "avss" and ranges from -1.0 to 1.0.
   - The y-axis ranges from -0.1 to 1.3.
   - There are three data points labeled M2, M3, and M4:
     - M2: Located at (0.0, 1.1789)
     - M3: Located at (0.0, 1.1823)
     - M4: Located at (0.0, 3.4314m)
   - The data points are color-coded: M2 and M3 are green, while M4 is red with a cross symbol.

2. **Right Section:**
   - This section shows a line graph with the title "BGR_output:Supply_Current".
   - The x-axis is labeled "temp (C)" and ranges from 40.0 to 120.0.
   - The left y-axis is labeled "V (V)" and ranges from 1.17875 to 1.1825.
   - The right y-axis is labeled "I (n)" and ranges from -81.5 to -75.5.
   - There are two lines plotted:
     - A red line representing "BGR_output" which forms a parabolic shape.
     - A yellow line representing "Supply_Current" which is linear.
   - There are two data points labeled:
     - A red point at 40.0C with a value of 1.182303V.
     - A blue point at 120.0C with a value of 1.17875V.
   - An annotation indicates a delta (dx) of 80.0C and a delta (dy) of 3.43138662mV with a slope of 42.8923.

The interface includes various toolbars and menus at the top for different functions like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, and Browser. The bottom of the interface shows a status bar with information about the current trace, history, test, design point, and corner.
```

#### **Figure 32: Plots in ViVA**

Action 46: In the **ADE Explorer** window, click on the up arrow to open the **ADE Assembler** window as shown in Figure 33.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a setup window for a simulation tool. The window is titled "Setup" and contains a hierarchical list of settings and parameters for a simulation.

At the top of the window, there are two columns labeled "Name" and "Value." Below these columns, there is a list of items organized in a tree structure. The items are as follows:

1. **TB_BGR_tb_bgr_1**: This appears to be the name of the test bench or the top-level simulation setup.
   - **Simulator spectre**: Indicates that the simulator being used is Spectre.
   - **Analyses**: This section contains the types of analyses to be performed.
     - **dc**: A DC analysis is specified with parameters "t -40 120 Automatic Start-Stop."
   - **Design Variables**: This section lists the design variables used in the simulation.
     - **avdd**: A design variable with a value of 2.
     - **avss**: A design variable with a value of 0.
   - **Parameters**: This section is currently empty, with a prompt to "Click to add variable."
   - **Corners**: This section is also empty, with a prompt to "Click to add variable."
   - **Reliability Analyses**: This section includes a sub-item.
     - **Monte Carlo Sampling**: Indicates that Monte Carlo sampling is part of the reliability analyses.
   - **Checks/Asserts**: This section is currently empty, with a prompt to "Click to add variable."

There are various icons next to each item, such as a green checkmark, a red cross, and a blue arrow pointing upwards, which likely represent different statuses or actions that can be taken for each item. The blue arrow icon is highlighted with a red border, indicating it might be the currently selected or active item.

Overall, the image depicts a detailed setup for running a simulation with specific analyses, design variables, and reliability checks.
```

#### **Figure 33: Up Arrow to open ADE Assembler**

Here is the image describtion:
```
The image is a screenshot of the Virtuoso ADE Assembler software interface, specifically showing the editing of a test bench named "TB_BGR tb_bgr maestro_Dc." The interface is divided into several sections:

1. **Top Menu Bar**: This contains various menu options such as Launch, File, Create, Tools, Options, Run, EAD, Parasitics/LDE, Window, and Help. There are also several icons for quick access to common functions like saving, opening files, and running simulations.

2. **Data View Panel (Left Side)**: This panel shows a hierarchical tree structure with categories such as Tests, Global Variables, Parameters, Corners, Documents, Setup States, Reliability Analyses, and Checks/Asserts. The "Nominal" corner is selected under the Corners category.

3. **Run Summary Panel (Bottom Left)**: This panel provides a summary of the current run, indicating that there is 1 Test, 1 Point Sweep, and 0 Corners selected.

4. **Main Panel (Center)**: This is the primary workspace where the test setup and results are displayed. It is divided into two tabs: "Data" and "History." The "Data" tab is currently active.

5. **Outputs Setup Section**: This section lists the outputs for the test bench "TB_BGR_tb_bgr_1." There are seven rows, each representing a different output or expression to be evaluated. The columns include:
   - **Test**: The name of the test bench.
   - **Name**: The name of the output or expression.
   - **Type**: The type of the output (e.g., expr, oppoint).
   - **Details**: Specific details or expressions for the output.
   - **EvalType**: The evaluation type, which is set to "point" for all rows.
   - **Plot**: A checkbox to indicate whether the output should be plotted.
   - **Save**: A checkbox to indicate whether the output should be saved.
   - **Spec**: Specification details (currently empty).
   - **Weight**: Weight details (currently empty).
   - **Units**: Units of measurement (currently empty).
   - **Digits**: Number of digits for precision (currently empty).

6. **Status Bar (Bottom)**: This bar shows the status of the current operation, including trace information and design point details.

Overall, the image depicts a detailed setup for running and analyzing a test bench in the Virtuoso ADE Assembler environment, with various outputs and expressions configured for evaluation.
```

#### **Figure 34: Assembler view of maestro\_Dc**

Action 47: In the ADE Assembler **Data View** window, expand **Corners** using the **+** sign and then, **Click to add corners** as shown in Figure 35.

Here is the image describtion:
```
The image shows a software interface titled "Data View." It appears to be a hierarchical tree structure used for organizing and managing different elements within a project or dataset. The interface is divided into two main columns: "Name" and "Value," each with a filter option at the top.

The tree structure includes the following elements, each with a checkbox to the left indicating whether they are selected or not:

1. **Tests** - This item is selected, as indicated by the checked box.
2. **Global Variables** - This item is also selected.
3. **Parameters** - This item is selected as well.
4. **Corners** - This item is partially selected, indicated by a yellow box with a check mark. It has a sub-item:
   - **Nominal** - This sub-item is selected.
   - **Click to add corner** - This is highlighted in yellow, suggesting it is an interactive element where the user can add a new corner.
5. **Documents** - This item is not selected.
6. **Setup States** - This item is not selected.
7. **Reliability Analyses** - This item is not selected.
8. **Checks/Asserts** - This item is not selected.

Each item in the tree has an icon next to it, representing its type or category. The interface is designed to allow users to manage and organize various components of their project efficiently.
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
The image is a screenshot of a software interface, specifically from Cadence Virtuoso Visualization & Analysis XL. The interface is used for analyzing electronic circuits, and the current display shows a graph of the output voltage (V) versus temperature (temp in °C) for a bandgap reference (BGR) circuit.

Key elements of the image include:

1. **Software Interface**: The top bar shows the software name "Virtuoso (R) Visualization & Analysis XL" and the specific testbench file "TB_BGR_tb_bgr_ref_maestro_Dc".

2. **Graph**: The main part of the image is a graph plotting the output voltage (V) on the Y-axis against temperature (°C) on the X-axis. The temperature range is from -40°C to 120°C, and the voltage range is from approximately 1.172V to 1.194V.

3. **Curves**: There are multiple colored curves on the graph, each representing the BGR output voltage at different process corners or conditions. The colors include red, orange, yellow, green, cyan, blue, and magenta.

4. **Markers and Annotations**: 
   - A vertical line at 60°C intersects the curves, with a marker showing the voltage at this temperature for each curve.
   - Two specific points are highlighted: one at 60.0°C with a voltage of 1.192176V (top curve) and another at 120.0°C with a voltage of 1.171816V (bottom curve).
   - An annotation at the bottom right corner indicates a change in voltage (dy) of -20.359974mV over a temperature change (dx) of 60.0°C, resulting in a temperature coefficient of 339.3329uV/°C.

5. **Tabs and Controls**: 
   - On the left side, there is a tab labeled "BGR_output" with a tree structure showing "BGR_output" as the selected item.
   - The top toolbar contains various icons and dropdown menus for file operations, graph settings, measurements, and other tools.

6. **Date and Time**: The top right corner of the graph area shows the date and time "Thu Oct 14 08:11:32 2021".

Overall, the image depicts a detailed analysis of the BGR circuit's output voltage behavior over a range of temperatures, with specific focus on the voltage stability and temperature coefficient.
```

**Figure 44: BGR\_output plots Across PVT Corners**

Action 57: Close all windows but leave the **Virtuoso** session open for the next lab.

### <span id="page-29-0"></span>**Lab 2: Power Supply Rejection Ratio of Bandgap Using Ac Analysis**

This lab is set up to determine PSRR of the Bandgap circuit. PSRR is a measure of the influence of the power supply ripple on the Bandgap output voltage.

PSRR analysis is used to measure the effect of supply ripples on the output reference supply.

Action 58: From the Library Manager, open **TB\_BGR > tb\_bgr > schematic**. The schematic window opens as shown in Figure 45.

Here is the image describtion:
```
The image depicts an electronic circuit schematic. The schematic is divided into two main sections:

1. **Left Section:**
   - This section contains two voltage sources labeled V7 and V8.
   - V7 is connected to a node labeled "PPA" and has parameters vdc=vdd and ac=1.
   - V8 is connected to a node labeled "BGR" and has parameters vdc=vss.
   - Both voltage sources are connected to a common ground.

2. **Right Section:**
   - This section contains a more complex circuit enclosed in a green rectangle labeled "BGR Circuit."
   - The circuit includes two current sources at the top, connected to resistors in series.
   - The resistors are connected to a node labeled "V_BGR."
   - The node "V_BGR" is connected to a capacitor labeled "C0" which is grounded.
   - The bottom part of the circuit includes additional components and connections, forming a more intricate design.

The entire schematic is drawn on a black background with a grid pattern, which is typical for electronic design automation (EDA) tools. The connections and components are color-coded for clarity, with red, green, and blue lines representing different parts of the circuit.
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
The image is a screenshot of the Virtuoso ADE Explorer software interface, which is used for analog and mixed-signal design and simulation. The title bar at the top indicates that the current project being edited is "TB_BGR tb_bgr maestro_Ac."

The interface is divided into several sections:

1. **Menu Bar**: At the very top, there is a menu bar with options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

2. **Toolbar**: Below the menu bar, there is a toolbar with various icons for common actions like opening, saving, and running simulations. There is also a search bar with options to replace text and a dropdown menu currently set to "(None)."

3. **Setup Panel**: On the left side, there is a panel titled "Setup" which contains a hierarchical tree structure. The tree includes:
   - TB_BGR_tb_bgr_1
   - Simulator spectre
   - Analyses (with an option to add analysis)
   - Design Variables (with an option to add variable)
   - Parameters
   - Corners (checked)
   - Reliability Analyses
   - Monte Carlo Sampling
   - Checks/Asserts

4. **Main Workspace**: The central part of the interface is a large blank area, which is likely where detailed information or results would be displayed once a simulation is run or a specific item is selected from the setup panel.

5. **Right Toolbar**: On the right side, there is a vertical toolbar with icons for various actions such as running simulations, stopping simulations, and other controls.

6. **Status Bar**: At the bottom, there is a status bar that shows the current mouse position and other status messages. It indicates that the current schematic is "TB_BGR tb_bgr schematic" and the simulator being used is "spectre aps."

Overall, the interface is designed to manage and run simulations for analog and mixed-signal designs, providing various tools and options for setting up and analyzing the design parameters and results.
```

#### **Figure 49: ADE Explorer window showing maestro\_Ac view**

Action 64: In the **ADE Explorer** window, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a setup window for a simulation or analysis tool. The window is divided into two main columns: "Name" and "Value," each with a filter option at the top.

The left column lists various components and settings for the simulation:

1. **TB_BGR_tb_bgr_1**: This appears to be the name of the current project or test bench.
2. **Simulator spectre**: Indicates the simulator being used, which is "spectre."
3. **Analyses**: A section for adding and managing different types of analyses. There is a highlighted prompt "Click to add analysis" suggesting that the user can add a new analysis here.
4. **Design Variables**: A section for managing design variables, with a prompt "Click to add variable."
5. **Parameters**: This section is checked, indicating it is active or selected.
6. **Corners**: This section is also checked, indicating it is active or selected.
7. **Reliability Analyses**: This section is not expanded, suggesting it contains additional settings or options.
8. **Monte Carlo Sampling**: This section is not expanded, suggesting it contains additional settings or options.
9. **Checks/Asserts**: This section is not expanded, suggesting it contains additional settings or options.

The interface uses icons to represent different sections and their statuses, such as checkboxes for active items and folder icons for expandable sections. The overall design is typical of engineering or simulation software, with a focus on organizing and managing various parameters and analyses.
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
The image is a screenshot of the Virtuoso ADE Explorer Edition software interface. The interface is divided into several sections and menus, with a focus on the "Setup" tab.

1. **Top Menu Bar**:
   - The top menu bar includes options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, and Results.
   - The "Variables" menu is highlighted in yellow, indicating it is currently selected or active.
   - A dropdown menu under "Variables" is open, showing options like Edit, Delete, Find, Copy From Cellview (highlighted in yellow), and Copy To Cellview.

2. **Setup Section**:
   - The left panel is labeled "Setup" and contains a hierarchical tree structure.
   - The tree structure includes:
     - **TB_BGR_tb_bgr_1**: The top-level item, likely representing a test bench or project.
     - **Simulator_spectre**: The simulator being used.
     - **Analyses**: A section for different types of analyses, with "ac" analysis (1.1G Automatic Start-Stop) checked.
     - **Design Variables**: A section listing design variables, with two variables highlighted in yellow:
       - **avdd**: Set to a value of 2.
       - **avss**: Set to a value of 0.
     - Other sections include Parameters, Corners, Reliability Analyses, Monte Carlo Sampling, and Checks/Asserts, but these are not expanded or detailed in the image.

3. **Icons and Buttons**:
   - Various icons and buttons are present at the top of the Setup panel, including options to save, open, and manage files or settings.
   - A temperature setting of 27°C is displayed, possibly indicating the operating condition for the simulation.

Overall, the image provides a detailed view of the Virtuoso ADE Explorer Edition interface, focusing on the setup and configuration of a simulation environment, with specific attention to design variables and analysis settings.
```

 **Figure 52: Copying variables from cell view**

- Action 68: In the **ADE Explorer** window, click on the green arrow button to **netlist and run** the simulation.
- Action 69: When the simulation is complete, click on **Simulation > Output Log** in the **ADE Explorer** window as shown in Figure 53.
- Action 70: Verify that simulation has completed with 0 errors.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from the Virtuoso ADE Explorer Editing environment. The interface appears to be related to simulation tasks within the software. 

At the top of the image, there is a menu bar with several tabs, including "Outputs," "Results," "Tools," "EAD," and "Parasitic." The tab "Simulation" is highlighted in yellow, indicating that it is currently selected.

Below the "Simulation" tab, a dropdown menu is open, displaying several options. The options listed in the dropdown menu are:
- Netlist and Run
- Run
- Stop
- Suspend (grayed out, indicating it is not currently available)
- Resume (grayed out, indicating it is not currently available)
- Run Preview
- MDL Control
- Options (with a submenu indicated by a right arrow)
- Netlist (with a submenu indicated by a right arrow)
- Output Log (highlighted in yellow)
- Linter Log
- Convergence Aids
- Diagnostics

To the right of the dropdown menu, there is a section with a dropdown box labeled "(None)" and a red arrow indicating it can be expanded or collapsed. 

The interface is designed for managing and executing simulation tasks, with various options for running, stopping, and previewing simulations, as well as accessing logs and diagnostic tools.
```

**Figure 53: Opening simulation log file from ADE Explorer window**

Action 71: In the **ADE Explorer** window, choose **Results > Direct Plot > Main Form** to open **Direct Plot Form** as shown in Figure 54.

Learn more at Cadence Learning and Support Portal - https://support.cadence.com © 2021 Cadence Design Systems, Inc. All rights reserved worldwide. Page 35

Here is the image describtion:
```
The image shows a screenshot of a software interface, specifically from a tool used for circuit design or simulation, likely Cadence Virtuoso. The title bar at the top indicates that the user is in the "TB_BGR tb_bgr maestro_Ac" environment.

The interface has a menu bar with several options: "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is expanded, revealing a dropdown list of options. The highlighted option in this list is "Direct Plot," which is further expanded to show another submenu.

The "Direct Plot" submenu contains several options, including:
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

The highlighted options in the image are "Direct Plot" and "Main Form ...", indicating that these are the currently selected or focused items. The interface appears to be designed for plotting and analyzing various types of simulation data, such as transient signals, AC characteristics, and noise figures.
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
The image is a screenshot of the Cadence Virtuoso Visualization & Analysis XL tool, displaying an AC response graph. The graph plots the voltage gain (V in dB) against frequency (freq in Hz) on a logarithmic scale. 

Key features of the image include:

1. **Graph Title and Labels**:
   - The graph is titled "AC Response".
   - The y-axis is labeled "V (dB)" and ranges from -48.0 dB to -15.0 dB.
   - The x-axis is labeled "freq (Hz)" and ranges from 10^0 to 10^9 Hz.

2. **Data Points and Markers**:
   - There are three markers on the graph:
     - M1 at 7.94328 Hz with a value of -41.2436 dB.
     - M2 at 1.99526 MHz with a value of -17.2929 dB, which appears to be the peak of the response curve.
     - M3 at 436.516 MHz with a value of -47.8076 dB.

3. **Graph Curve**:
   - The curve starts at a low frequency with a relatively flat response around -41 dB.
   - It then rises sharply to a peak at approximately 1.99526 MHz.
   - After the peak, the curve drops steeply and continues to decline, reaching around -47.8076 dB at 436.516 MHz.

4. **Interface Elements**:
   - The top menu bar includes options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
   - There are various toolbar icons for different functions, such as zoom, pan, and data point selection.
   - The left panel shows the AC response name and a trace labeled "v / V_BGR; ac dB20(V)".
   - The bottom status bar provides information about the trace and the test being run.

5. **Highlighted Toolbar Icon**:
   - A specific toolbar icon is highlighted with a red box, indicating it might be the currently selected or active tool.

Overall, the image provides a detailed view of the AC response of a circuit, showing how the voltage gain varies with frequency, with specific markers highlighting key points on the response curve.
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
The image is a text label that reads "Figure 57: ViVA-XL calculator." It appears to be a caption or title for a figure in a document, likely referring to an image or illustration of a ViVA-XL calculator that is not shown in the provided image. The text is in a bold font, indicating it is a heading or important label within the document.
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
The image shows a screenshot of a software interface, likely related to electrical engineering or signal processing. The interface includes a keypad on the left side with numbers 0-9 and basic arithmetic operators (/, *, -, +). 

To the right of the keypad, there is a text input area where a command is being entered. The command shown is:
```
value(db(vfreq("ac" "/V_BGR")) 1)
```
This command appears to be related to calculating the decibel value of a frequency response, possibly for an AC signal, with a specific reference to "V_BGR".

Above the text input area, there is a toolbar with several options:
- "Off" with a red dot next to it.
- "Family" and "Wave" options.
- A "Clip" option with a checkmark next to it.
- Icons representing different functions, including a waveform icon, an append icon, and a settings gear icon highlighted with a red box.
- A dropdown menu labeled "Rectangular".

The overall design suggests that this is a specialized tool for analyzing or simulating electrical signals, with a focus on frequency response and decibel calculations.
```

Here is the image describtion:
```
The image is a screenshot of a text label that reads "Figure 60: ViVA-XL calculator buffer." The text is in black font on a white background. The label appears to be a caption or title for a figure in a document, likely referring to an image or diagram related to the ViVA-XL calculator buffer.
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
The image appears to be a screenshot or a snippet from a document or presentation. It includes a figure label at the top that reads "Figure 61: ADE maestro_Ac view." The text is in black and uses a bold font, indicating that it is a title or caption for an image or diagram that is supposed to be displayed below it. However, the actual image or diagram referred to by the caption is not visible in the provided snippet. The context suggests that the image would be related to a view or interface of a software or system named "ADE maestro_Ac."
```

Action 81: Click **Plot Outputs** . The expressions are plotted as shown in Figure 62.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from Cadence Virtuoso Visualization & Analysis XL. The interface is used for analyzing and visualizing data, likely related to electronic circuit design and simulation.

The interface is divided into three main sections:

1. **Left Section (PSRR_plot):**
   - This section contains a plot labeled "PSRR_plot."
   - The plot is a graph with the y-axis labeled "V (dB)" ranging from -15.0 to -48.0 dB.
   - The x-axis is labeled "freq (Hz)" and spans from 10^0 to 10^9 Hz.
   - A red line represents the data, showing a peak at around 1.9953 MHz with a value of -17.293 dB (marked as M6).
   - Another marker (M5) indicates a point at 7.9433 Hz with a value of -41.244 dB.

2. **Middle Section:**
   - This section contains a plot labeled "DC_PSRR."
   - The y-axis is labeled "V (dB)" ranging from -37.0 to -46.0 dB.
   - The x-axis is labeled "avss" and ranges from -1.0 to 1.0.
   - A single red data point is marked at (0, -41.244 dB) with a label M7.

3. **Top Menu and Toolbar:**
   - The top of the interface includes a menu bar with options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
   - Below the menu bar, there is a toolbar with various icons for different functions, such as saving, zooming, and data manipulation.

The interface also includes a timestamp indicating the date and time of the analysis: "Tue Oct 12 13:05:48 2021." The software appears to be used for analyzing Power Supply Rejection Ratio (PSRR) in electronic circuits, with detailed plots and markers highlighting specific data points.
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
The image depicts a detailed electronic circuit schematic, likely designed using a CAD (Computer-Aided Design) tool for integrated circuits. The schematic includes various components and connections, which are described as follows:

1. **Transistors**: 
   - There are multiple PMOS and NMOS transistors labeled with their respective types and dimensions. For example, PMOS transistors are labeled as "pmos2v" and NMOS transistors as "nmos2v". The dimensions (width and length) are specified, such as "w=2u" and "l=2u".
   - Specific transistors are labeled with identifiers like M15, M14, M5, M12, M0, M1, and Q4.

2. **Resistors**:
   - Several resistors are present, labeled with their resistance values and types. For instance, R1, R2, R3, and R4 have values like 44.8K, 5.33333K, and 130K ohms.
   - The resistors are also labeled with their segment counts, such as "segmenta=42" and "segmenta=5".

3. **Capacitors**:
   - A capacitor labeled C1 with a value of 5pF is included in the circuit.

4. **Operational Amplifier**:
   - An operational amplifier (op-amp) is depicted in the center of the schematic, labeled as "AVDD_BGR". It has input and output connections labeled "inp", "inn", "out", "vdd", and "vss".

5. **Voltage Sources and Nodes**:
   - The circuit includes various voltage sources and nodes labeled "vdd", "vss", "V_BGR", and "VF1".
   - The nodes are connected through blue lines representing the connections between different components.

6. **Highlighted Section**:
   - A section of the circuit is highlighted with a red rectangle, indicating a specific area of interest or importance. This section includes a transistor labeled "PR1".

7. **Connections**:
   - The components are interconnected with lines representing electrical connections. The connections are color-coded, with blue lines for general connections and red lines for power supply connections.

Overall, the schematic represents a complex electronic circuit, possibly a voltage reference or regulator circuit, given the presence of the operational amplifier and the labeled voltage nodes. The detailed labeling of components and their values suggests a precise design intended for simulation or fabrication in an integrated circuit.
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
The image shows a screenshot of the Virtuoso ADE Explorer Editing interface from Cadence Design Systems. The title bar at the top indicates that the current project is "TB_BGR tb_bgr maestro_Stb."

The interface is divided into several sections:

1. **Menu Bar**: Located at the top, it includes various dropdown menus such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

2. **Toolbar**: Below the menu bar, there is a toolbar with icons for common actions like saving, opening files, and other utilities. There is a search bar with the label "Replace" and a dropdown menu set to "(None)." There are also icons for additional functionalities.

3. **Setup Panel**: On the left side, there is a panel titled "Setup" which lists various components and settings for the project. It includes:
   - TB_BGR_tb_bgr_1
   - Simulator spectre
   - Analyses
   - Design Variables
   - Parameters
   - Corners
   - Reliability Analyses
   - Monte Carlo Sampling
   - Checks/Asserts

   Each of these items can be expanded or collapsed, and some have checkboxes next to them indicating their selection status.

4. **Main Workspace**: The central part of the interface is divided into tabs. The active tab is "tb_bgr" and there is another tab labeled "maestro_Stb." The workspace under the "tb_bgr" tab is currently empty, with columns for "Name," "Type," and "Details."

5. **Right Sidebar**: On the right side, there is a vertical toolbar with icons for various actions, such as adding, editing, and running simulations.

The overall layout is designed to facilitate the setup and execution of electronic design automation (EDA) tasks, specifically for analog and mixed-signal design verification.
```

**Figure 66: ADE Explorer window showing maestro\_Stb view** 

Action 88: In **ADE Explorer**, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically a "Setup" window. The window is divided into two main columns: "Name" and "Value," each with a filter option indicated by a red downward arrow.

The "Name" column contains a hierarchical list of items, each with an associated icon:
1. "TB_BGR_tb_bgr_1" with an upward arrow icon.
2. "Simulator spectre" with a green gear icon.
3. "Analyses" with a green gear icon, and a sub-item "Click to add analysis" highlighted in yellow.
4. "Design Variables" with a red cube icon, and a sub-item "Click to add variable" in grey text.
5. "Parameters" with a red cube icon and a checkmark.
6. "Corners" with a thermometer icon and a checkmark.
7. "Reliability Analyses" with a green gear icon, and a sub-item "Monte Carlo Sampling" with a green cube icon.
8. "Checks/Asserts" with a red cube icon.

The "Value" column is empty, indicating that no specific values are currently assigned to the items listed in the "Name" column. The interface appears to be part of a software tool used for simulation or analysis, likely in an engineering or scientific context.
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
The image is a screenshot of the Virtuoso ADE Explorer interface, which is a tool used for analog design and simulation. The interface has several menu options at the top, including "Launch," "Session," "Setup," "Analyses," "Variables," "Outputs," "Simulation," "Results," and "Tools." The "Variables" menu is highlighted, and a dropdown menu is visible with options such as "Edit...," "Delete," "Find," "Copy From Cellview," and "Copy To Cellview." The "Copy From Cellview" option is highlighted in yellow.

Below the menu bar, there is a section labeled "Setup" with a hierarchical list of items. The list includes:
- "TB_BGR_tb_bgr_1" with a green icon indicating it is a test bench.
- "Simulator spectre" indicating the simulator being used.
- "Analyses" with a sub-item "dc" that has a checkbox checked, indicating that a DC analysis is selected. The analysis has parameters "t -40 120 Automatic Start-Stop."
- "Design Variables" with two variables listed:
  - "avdd" with a value of 2, highlighted in yellow.
  - "avss" with a value of 0, also highlighted in yellow.

The interface also includes various icons and buttons for different functions, such as saving, running simulations, and adjusting settings. The overall layout is typical of a design and simulation tool, with a focus on managing and configuring different aspects of the simulation environment.
```

**Figure 69: Copying variables from cell view**

- Action 93: In the **ADE Explorer** window, click on the green button to **netlist and run** the simulation.
- Action 94: Select **Results > Direct Plot > Main Form** in the **ADE Explorer** window as shown in Figure 70 to open **Direct Plot Form**.

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from the Virtuoso ADE Explorer, which is used for analog design environments. The title bar indicates that the current project is "TB_BGR tb_bgr maestro_Stb."

The screenshot shows a dropdown menu under the "Results" tab, which is highlighted in yellow. The "Results" menu has several options, including "Plot Outputs," "Direct Plot," "Print," "Annotate," "Vector," "Circuit Conditions," "Electrothermal Report," "EM/IR Data," "Save," "Select," "Delete," and "Printing/Plotting Options."

The "Direct Plot" option is selected, and it opens a sub-menu on the right side. This sub-menu is titled "Direct Plot" and contains various plotting options. The first option, "Main Form ...," is highlighted in yellow. Other options in the sub-menu include "Transient Signal," "Transient Minus DC," "Transient Sum," "Transient Difference," "AC Magnitude," "AC dB10," "AC dB20," "AC Phase," "AC Magnitude & Phase," "AC Gain & Phase," and "Equivalent Output Noise."

The interface is designed for users to select different plotting and analysis options for their circuit simulations. The highlighted options indicate the current selections or areas of focus within the software.
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
The image is a screenshot of the Virtuoso (R) Visualization & Analysis XL software by Cadence, which is used for analyzing electronic circuits. The specific analysis shown is for a test bench named "TB_BGR_tb_bgr_1" and it displays the loop gain and phase characteristics of a circuit.

The main window is divided into two sections:
1. The left section lists the different measurements or traces being analyzed. In this case, it shows "Loop Gain Phase" and "Loop Gain dB20" with their respective values.
2. The right section is a graph plotting the loop gain and phase against frequency (Hz). The x-axis represents the frequency on a logarithmic scale ranging from 10^1 to 10^9 Hz. The y-axis on the left side represents the loop gain in degrees (deg) and the y-axis on the right side represents the loop gain in decibels (dB).

Two traces are plotted:
- The red trace represents the loop gain phase, with a marker at M2 indicating a value of 3.46737 Hz and 179.998 degrees.
- The yellow trace represents the loop gain in dB, with a marker at M1 indicating a value of 2.29087 Hz and 27.5172 dB.

Additional markers on the graph show specific data points:
- A red marker at 35.55463 degrees.
- A yellow marker at 50.96456 m dB.

The top toolbar contains various icons and options for editing, viewing, graphing, and analyzing the data. The software's title bar indicates the current test and the date and time of the analysis (Tue Oct 12 13:42:52 2021).

Overall, the image provides a detailed view of the loop gain and phase characteristics of the circuit being analyzed, with specific data points highlighted for further examination.
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
The image is a screenshot or snippet of text that reads "Figure 76: ADE maestro_Stb view." The text is in black font on a white background. The font appears to be a standard sans-serif typeface, and the text is likely part of a larger document, such as a technical manual, report, or presentation. The figure number "76" suggests that this is one of many figures in the document, and "ADE maestro_Stb view" likely refers to a specific view or screen within a software application or system named ADE Maestro.
```

Here is the image describtion:
```
The image contains a text instruction that reads: "Action 105: Click Plot Outputs." The text is formatted with "Action 105:" in red, while "Click Plot Outputs" is in black, with "Plot Outputs" in bold. To the right of the text, there is a small icon that appears to be a graphical representation of a plot or chart, indicating where to click. The icon is a small square with a line graph inside it.
```

Here is the image describtion:
```
The image is a screenshot of a software interface, specifically from Cadence Virtuoso Visualization & Analysis XL, used for analyzing electronic circuits. The interface is displaying various plots and data points related to loop gain and phase margin analysis.

1. **Top Bar**: The top bar contains the software name "Virtuoso (R) Visualization & Analysis XL" and the specific test being analyzed "TB_BGR_tb_bgr maestro_Stb". There are multiple icons and options for file management, editing, viewing, graphing, axis adjustments, tracking, measurements, tools, window management, browsing, and help.

2. **Left Panel**: The left panel lists the data being analyzed, labeled "Loop Gain Phase: Loop Gain dB20". It shows a hierarchical structure with a name "Vis V1" and two sub-items: "Loop Gain Phase" and "Loop Gain dB20".

3. **Main Plot Area**: The main plot area is divided into two sections:
   - **Left Section**: This section contains two plots overlaid on the same graph. The x-axis represents frequency (Hz) on a logarithmic scale, ranging from 10^1 to 10^9 Hz. The y-axis on the left represents loop gain in decibels (dB), and the y-axis on the right represents loop gain phase in degrees (deg).
     - The red curve represents the loop gain phase, with a highlighted data point at 12.0202 Hz showing a phase of 179.992 degrees.
     - The yellow curve represents the loop gain in dB, with a highlighted data point at 7.94328 Hz showing a gain of 27.5172 dB.
     - Another data point on the yellow curve at 1.84652 MHz shows a gain of 3.102068 mB.
   - **Right Section**: This section contains a plot with the x-axis labeled "avss" and the y-axis labeled with a range from 6.0 to 36.0. There are two highlighted data points:
     - A red data point labeled "M4: 0.0 35.531".
     - A yellow data point labeled "M5: 0.0 6.8735".

4. **Bottom Bar**: The bottom bar shows the trace information "Trace: Loop Gain Phase; History: ExplorerRun.0; Test: TB_BGR_tb_bgr_1".

Overall, the image depicts a detailed analysis of loop gain and phase margin, with specific data points highlighted for further examination.
```

### **Figure 77: Output plots**

Action 106: Close all windows but leave the **Virtuoso** session open for the next lab.

### <span id="page-50-0"></span>**Lab 4: Transient Noise Measurement of Bandgap**

- Transient noise calculates the effects of large-signal noise on virtually any system. It determines the impact of noise in the time domain. This is an extension to the current **transient analysis** in **Spectre**.
- This section provides an overview of the transient noise analysis setup form in **ADE**. Later, it provides an overview of **Direct Plot Form** (for plotting transient noise results after the transient simulation).

Action 107: From the **Library Manager**, open the **TB\_BGR > tb\_bgr > schematic**  view. The schematic window opens as shown in Figure 78.

Here is the image describtion:
```
The image depicts an electronic circuit schematic. Here is a detailed description of the components and connections:

1. **Power Supply Section (Left Side):**
   - There are two voltage sources labeled V7 and V8.
   - V7 is connected to a node labeled "PPA" and has a voltage value of "vdd" with an AC magnitude of 1.
   - V8 is connected to a node labeled "BGR" and has a voltage value of "vss".
   - Both voltage sources are connected to a common ground.

2. **Bandgap Reference Circuit (Right Side):**
   - The main circuit is enclosed in a green rectangular box labeled "BGR Circuit".
   - Inside the BGR Circuit, there are two current sources at the top, each connected to a resistor.
   - The resistors are connected in series and form a voltage divider.
   - The top of the left current source is connected to a node labeled "PPA".
   - The top of the right current source is connected to a node labeled "V_BGR".
   - The bottom of the voltage divider is connected to a node labeled "VSS".
   - The node "V_BGR" is connected to an external capacitor labeled "C8", which is grounded.

3. **Connections:**
   - The node "PPA" from the power supply section is connected to the top of the left current source in the BGR Circuit.
   - The node "V_BGR" from the BGR Circuit is connected to the capacitor "C8".
   - The node "VSS" from the power supply section is connected to the bottom of the voltage divider in the BGR Circuit.

Overall, the schematic represents a bandgap reference circuit with power supply connections and an external capacitor for stabilization.
```

**Figure 78: Schematic of tb\_bgr cell testbench**

Action 108: From the schematic, select **Launch > ADE Explorer**.

Action 109: In the **Launch ADE Explorer** window, select **Create New View** and click **OK**.

Here is the image describtion:
```
The image is a screenshot of a dialog box titled "Launch ADE Explorer." The dialog box provides options for the user to either create a new view or open an existing view within the ADE Explorer application. 

- The title "Launch ADE Explorer" is displayed at the top of the dialog box in a black bar with white text.
- Below the title, there is a section labeled "ADE Explorer" in red text.
- Within this section, there are two radio button options:
  1. "Create New View" - This option is selected, as indicated by the filled red circle next to it.
  2. "Open Existing View" - This option is not selected, as indicated by the empty circle next to it.
- The "Create New View" option is highlighted with a red border, emphasizing that it is the current selection.
- At the bottom of the dialog box, there are three buttons:
  1. "OK" - This button is red with white text.
  2. "Cancel" - This button is gray with black text.
  3. "Help" - This button is also gray with black text.

The overall design of the dialog box is simple and user-friendly, with clear options and buttons for navigation.
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
The image is a screenshot of the Virtuoso ADE Explorer, a software tool used for analog and mixed-signal design and simulation. The title bar at the top indicates that the current project is "TB_BGR tb_bgr maestro_Tran_Noise."

The interface is divided into several sections:

1. **Menu Bar**: At the very top, there is a menu bar with options such as Launch, Session, Setup, Analyses, Variables, Outputs, Simulation, Results, Tools, EAD, Parasitics/LDE, Window, and Help.

2. **Toolbar**: Below the menu bar, there is a toolbar with various icons for common actions like opening, saving, and running simulations. There is also a search and replace bar.

3. **Setup Panel (Left Side)**: On the left side, there is a panel labeled "Setup" with a hierarchical tree structure. It includes:
   - TB_BGR_tb_bgr_1
   - Simulator spectre
   - Analyses (with a prompt to click to add analysis)
   - Design Variables (with a prompt to click to add variable)
   - Parameters (with sub-items like Corners and Reliability Analyses)
   - Monte Carlo Sampling
   - Checks/Asserts

4. **Main Panel (Center)**: The central part of the interface is mostly blank, indicating that no specific analysis or data is currently displayed. It has columns for Name, Type, Details, Plot, Save, and Spec.

5. **Right Toolbar**: On the right side, there is a vertical toolbar with icons for various actions, such as running simulations, stopping simulations, and plotting results.

6. **Status Bar**: At the bottom, there is a status bar showing the mouse coordinates and some additional information about the current project and simulator.

Overall, the image shows the initial setup stage of a simulation project in the Virtuoso ADE Explorer, with no specific analyses or results displayed yet.
```

#### **Figure 81: ADE Explorer window showing maestro\_Tran\_Noise view**

In **ADE Explorer**, select **Click to add analysis** in the **Analyses** section of the **Setup** assistant as shown in Figure 82.

Here is the image describtion:
```
The image is a screenshot of a software interface titled "Setup." The interface is divided into two main columns: "Name" and "Value." At the top of each column, there is a filter option indicated by a red downward arrow.

The left column lists various components and settings in a hierarchical tree structure. The components are as follows:

1. **TB_BGR_tb_bgr_1**: Represented by a blue house icon.
2. **Simulator spectre**: Represented by a green gear icon.
3. **Analyses**: Represented by a green folder icon. Under this, there is a highlighted option in yellow that says "Click to add analysis."
4. **Design Variables**: Represented by a red cube icon. Under this, there is a greyed-out option that says "Click to add variable."
5. **Parameters**: Represented by a red checkmark icon, indicating it is selected.
6. **Corners**: Represented by a red thermometer icon, also selected.
7. **Reliability Analyses**: Represented by a green checkmark icon, not selected. Under this, there is an option for "Monte Carlo Sampling," represented by a green cube icon, which is also not selected.
8. **Checks/Asserts**: Represented by a grey checkmark icon, not selected.

The right column, labeled "Value," is currently empty and does not display any values corresponding to the names listed in the left column. The interface appears to be part of a software tool used for setting up simulations or analyses, likely in an engineering or scientific context.
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
The image is a screenshot of a software interface, specifically from the Virtuoso ADE Explorer Editing environment. The interface appears to be part of a simulation tool used for electronic design automation (EDA).

Key elements in the image include:

1. **Menu Bar**: At the top, there is a menu bar with several options, including "Outputs," "Results," "Tools," "EAD," and "Parasitics."

2. **Highlighted Menu**: The "Simulation" menu is highlighted in yellow, indicating that it is currently selected or active.

3. **Dropdown Menu**: Below the "Simulation" menu, a dropdown menu is open, displaying several options:
   - "Netlist and Run"
   - "Run"
   - "Stop"
   - "Suspend" (grayed out, indicating it is not currently available)
   - "Resume" (grayed out, indicating it is not currently available)
   - "Run Preview"
   - "MDL Control"
   - "Options" (with a submenu indicated by a right arrow)
   - "Netlist"
   - "Output Log..." (highlighted in yellow)
   - "Linter Log..."
   - "Convergence Aids"
   - "Diagnostics"

4. **Toolbar**: There is a toolbar with various icons and a dropdown menu labeled "(None)" on the right side of the image.

The interface is designed for managing and running simulations, with options to control the simulation process, view logs, and access various tools and diagnostics. The highlighted "Output Log..." option suggests that the user is likely interested in viewing the output log of a simulation.
```

**Figure 85: Opening simulation log file from ADE Explorer window**

Action 115: Click **Results > Direct Plot > Main Form** in the **ADE Explorer** window as shown in Figure 86 to open the **Direct Plot** form.

Here is the image describtion:
```
The image shows a screenshot of a software interface, specifically a menu related to plotting results in a simulation or analysis tool. The top part of the interface displays the title "TB_BGR tb_bgr maestro_Tran_Noise," indicating the current project or file being worked on.

The menu bar at the top includes several options: "Results," "Tools," "EAD," "Parasitics/LDE," "Window," and "Help." The "Results" menu is expanded, revealing a dropdown list of options. The "Direct Plot" option is highlighted in yellow, indicating it is selected.

When "Direct Plot" is selected, a secondary menu appears to the right, titled "Direct Plot." This menu contains several options, with "Main Form ..." highlighted in yellow. Other options in this menu include:

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

The interface appears to be part of a software tool used for electrical or electronic circuit simulation and analysis, providing various plotting and data visualization options for different types of signals and noise measurements.
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
The image is a screenshot of a software interface, specifically the Virtuoso Visualization & Analysis XL tool from Cadence. The interface is displaying a graph of a transient response analysis.

Here are the details of the image:

1. **Software Interface**:
   - The top bar shows the title "Virtuoso (R) Visualization & Analysis XL: TB_BGR tb_bgr maestro_Tran_Noise".
   - The menu bar includes options like File, Edit, View, Graph, Axis, Trace, Marker, Measurements, Tools, Window, Browser, and Help.
   - Below the menu bar, there are various tool icons for different functions.

2. **Graph Area**:
   - The graph is titled "Transient Response".
   - The y-axis is labeled in decibels (dB) ranging from -190 dB to -30 dB.
   - The x-axis is labeled in frequency (MHz) ranging from 0 to 100 MHz.
   - The graph shows a green plot line representing the power spectral density (psd) of a signal over frequency.
   - Two markers are present on the graph:
     - M1 at 15.62 MHz with a value of -161.876 dB.
     - M2 at 91.95 MHz with a value of -180.564 dB.

3. **Additional Information**:
   - The left side of the graph area has a section labeled "Name" with a blacked-out entry and a green bar labeled "db10(psd(...hGain".
   - The bottom of the image shows a status bar with detailed trace information: "Trace: db10(psd(VT("/V_BGR") 100u 1.7m 320000 ?windowName "Rectangular" ?smooth 1 ?windowSize 20000 ?detrending "None" ?cohGain 1)); History: ExplorerRun.0; Test: T".

Overall, the image depicts a detailed analysis of a signal's power spectral density over a range of frequencies using the Cadence Virtuoso tool.
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