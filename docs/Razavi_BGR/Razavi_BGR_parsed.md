Here is the image describtion:
```
The image shows a person dressed in formal attire. The individual is wearing a dark suit jacket over a white dress shirt, paired with a red tie. The background of the image is a light blue color. The name "Behzad Razavi" is written at the bottom of the image in a bold, sans-serif font. The person's hair appears to be gray and slightly curly.
```

# **The Design of a Low-Voltage Bandgap Reference**

**THE ANALOG MIND**

*M*Most integrated circuits incorporate bandgap references (often simply called *bandgaps*) to define certain dc voltages or currents that serve various building blocks. In this article, we introduce a step-by-step procedure for the design of low-voltage bandgaps. As presented in Figure 1, a typical power-management environment employs a low-dropout (LDO) circuit that, from a global supply of 1.2 V, generates a moderately regulated voltage around 1 V. This voltage acts as a local supply for the bandgap circuit and some other building blocks. It is desirable for the bandgap to provide substantial supply rejection to minimize corruption in its output due to the electronic noise produced by the LDO and the transient perturbations caused by the switching activities within the other building blocks.

We target the following specifications:

- output voltage = 0.5 V
- output voltage variation 1 5 mV from 0 Cc to 100 Cc
- supply rejection 2 40 dB
- power consumption 1 1 mW
- supply voltage =1 5 V ! %.

We design the circuit in 28-nm CMOS technology. The reader is referred to [1]–[12] for background information.

# Basic Operation

We wish to generate a voltage that is nominally independent of the

*Digital Object Identifier 10.1109/MSSC.2021.3088963 Date of current version: 25 August 2021*

Here is the image describtion:
```
The image depicts a simple electronic circuit diagram. Here is a detailed description:

1. **Power Supply**: The circuit starts with a power supply of 1.2 volts, indicated by the text "1.2 V" at the top left of the image.

2. **LDO (Low Dropout Regulator)**: The 1.2 V input is fed into an LDO regulator. The LDO is represented by a rectangular block labeled "LDO". The LDO is a type of voltage regulator that can operate with a very small input-output differential voltage.

3. **Output Voltage**: The LDO regulates the input voltage down to 1 volt, as indicated by the text "1 V" at the output of the LDO.

4. **Bandgap Reference**: The 1 V output from the LDO is connected to a Bandgap Reference circuit. This is represented by another rectangular block labeled "Bandgap Reference". The Bandgap Reference circuit is connected to ground, as indicated by the line extending downwards from the block to the ground symbol.

5. **Continuation**: The output of the Bandgap Reference circuit is shown to continue further, as indicated by the three dots (ellipsis) at the right end of the image. This suggests that the output is used in subsequent parts of the circuit not shown in the image.

In summary, the image shows a 1.2 V power supply being regulated down to 1 V by an LDO, which then feeds into a Bandgap Reference circuit. The Bandgap Reference circuit is grounded and its output continues to other parts of the circuit.
```

**FIGURE 1: A typical power-management environment.**

temperature. This can be accomplished by summing two voltages that have opposite temperature coefficients (TCs), as practiced in [1], [3], and [11]. Alternatively, we can first sum two currents of opposite TCs and then allow the result to flow through a resistor [9]. We pursue the latter here.

The bandgap core is typically realized as illustrated in Figure 2(a), where the emitter areas of *Q*1 and *Q*2 differ by a factor of *n*, and amplifier *A*1 adjusts the gate voltage of *M*1 and *M*2 to equalize *VX* and *VY* . We thus obtain

$$\mathcal{V}\_{\rm BE1} = \mathcal{V}\_{\rm BE2} + |I\_{D2}| \mathcal{R}\_1 \,. \tag{1}$$

Hence,

$$V\_T \ln \frac{I\_{D1}}{I\_{S1}} = V\_T \ln \frac{I\_{D2}}{I\_{S2}} + |I\_{D2}| R\_1,\qquad(2)$$

where *IS*1 and *IS*2 denote the emitter saturation currents of *Q*1 and *Q*2, respectively. Viewing *Q*1 as a unit and *Q*2 as *n* units in parallel, we have *I n S S* 2 1 = *I* and

$$|I\_{D2}|R\_1 = V\_T \ln n,\tag{3}$$

where *M*1 and *M*2 are assumed to be identical. The voltage across *R*1 is therefore proportional to the absolute temperature (PTAT) and so are the drain currents of *M*1 and *M*2 if *R*1 has a zero TC.

It is possible to make *ID*1 and *ID*<sup>2</sup> independent of the temperature by attaching two resistors from *X* and *Y* to the ground [see Figure 2(b)] [9]. Let us formulate the circuit's behavior, assuming that *R R* 2 3 = . Since *V V X Y* . , (1) still holds, and the current through *R*1 is still equal to ( ) *V n <sup>T</sup>* ln /*R*1. Summing this current and that through *R*3, we have

$$|I\_{D1}| = |I\_{D2}| = \frac{V\_T \ln n}{R\_1} + \frac{|V\_{\text{RE1}}|}{R\_3} \tag{4}$$

$$\frac{1}{R\_3} = \frac{1}{R\_3} \left(\frac{R\_3}{R\_1} \, V\_T \ln n + |V\_{\text{BE1}}|\right). \qquad (5)$$

The two terms on the right-hand side of (5) represent currents with opposite TCs. For | | *ID*2 to have a TC of zero, we select ( ) *R R* 3 1 / *V n <sup>T</sup>* ln to be approximately 17*VT* [12]. Now, as depicted in Figure 2(c), this current is copied and applied to a resistor to yield a nominally constant output voltage [9],

$$V\_{\rm out} = \frac{R\_L}{R\_3} \left(\frac{R\_3}{R\_1} \, V\_T \ln \, \pi + |V\_{\rm BE1}|\right). \qquad (6)$$

The key to the circuit's low-voltage operation is that *V*out can be arbitrarily small even though | | *V V* BE +17 *<sup>T</sup>* .1 2. V at *T* =25c C.

### Design Issues

The topology of Figure 2(c) entails several issues. First, noting that the TC of

Here is the image describtion:
```
The image shows three different configurations of a differential amplifier circuit, each with slight variations. Let's describe each configuration in detail:

### (a) Basic Differential Amplifier
- **Transistors**: The circuit uses two NPN bipolar junction transistors (BJTs), labeled Q1 and Q2.
- **MOSFETs**: There are two PMOS transistors, labeled M1 and M2, connected at the top.
- **Current Source**: A current source labeled P is connected between the sources of M1 and M2 and the positive supply voltage V_DD.
- **Operational Amplifier**: An operational amplifier (A1) is used with its inverting input connected to node X and its non-inverting input connected to node Y.
- **Resistor**: A resistor R1 is connected between node Y and ground.
- **Inputs**: The base of Q1 is connected to an input signal labeled A_E, and the base of Q2 is connected to another input signal labeled nA_E.
- **Nodes**: The emitters of Q1 and Q2 are connected to ground.

### (b) Differential Amplifier with Additional Resistor
- **Transistors**: Similar to (a), it uses two NPN BJTs (Q1 and Q2) and two PMOS transistors (M1 and M2).
- **Current Source**: The current source P is still present.
- **Operational Amplifier**: The operational amplifier (A1) is used in the same configuration.
- **Resistors**: In addition to R1, there is another resistor R2 connected between node X and ground.
- **Inputs**: The base of Q1 is connected to A_E, and the base of Q2 is connected to nA_E.
- **Nodes**: The emitters of Q1 and Q2 are connected to ground.

### (c) Differential Amplifier with Output Stage
- **Transistors**: This configuration also uses two NPN BJTs (Q1 and Q2) and two PMOS transistors (M1 and M2). Additionally, there is an NMOS transistor labeled M3.
- **Current Source**: The current source P is present.
- **Operational Amplifier**: The operational amplifier (A1) is used in the same configuration.
- **Resistors**: There are three resistors: R1 connected between node Y and ground, R2 connected between node X and ground, and R3 connected between node Y and the drain of M3.
- **Output Stage**: The drain of M3 is connected to the output node V_out, and a load resistor R_L is connected between V_out and ground.
- **Inputs**: The base of Q1 is connected to A_E, and the base of Q2 is connected to nA_E.
- **Nodes**: The emitters of Q1 and Q2 are connected to ground.

### Summary
- **(a)**: Basic differential amplifier with a single resistor R1.
- **(b)**: Differential amplifier with an additional resistor R2.
- **(c)**: Differential amplifier with an output stage including an NMOS transistor M3 and a load resistor R_L.

Each configuration builds upon the previous one, adding more components to enhance the functionality and performance of the differential amplifier.
```

**FIGURE 2: (a) A basic bandgap core. (b) The addition of resistors to create constant currents. (c) The addition of an output branch.**

the base-emitter voltage, 2 2 *V T* BE / , is around -1 5. , m C V/c we expect | | *V*BE1 to be relatively large at low temperatures. With a worst-case *V*DD of 0.95 V, this leaves little voltage headroom for *M*1 and *M*2. We must therefore select relatively large bipolar transistors and low collector currents to ensure a moderate | | *V V* BE = *T C* ln( ) *I I* / *<sup>S</sup>* .

Second, as *T* goes from 0 Cc to +100 Cc , | | *V*BE1 in Figure 2(c) drops by roughly 150 mV, whereas *V*out remains relatively constant. The resulting difference between the drain-source voltages of *M*1 2, and *M*3 leads to a substantial error in *ID*3 and, hence, a large variation in *V*out. We will resolve this issue through the use of a regulated cascode structure.

Third, the offset of *A*1, *V*OS1, in Figure 2(c) introduces an error in *V*out . We have [13]

$$V\_{\rm out} = \frac{R\_L}{R\_3} \left[ |V\_{\rm BE1}| + \frac{R\_3}{R\_1} V\_T \ln n \right]$$

$$- \left( 1 + \frac{R\_3}{R\_1} \right) V\_{\rm GS1} \right]. \tag{7}$$

The contribution of *V*OS1 can be minimized by maximizing ln*n*—a remedy that costs chip area.

Fourth, the 40-dB supply-rejection requirement imposes a lower bound on the operation amplifier (op amp) gain in Figure 2(c). As explained next, *A*1 must reach several hundred.

Fifth, the bandgap core of Figure 2(b) and (c) can indefinitely remain off after powerup if *VX* and *VY* begin from zero and *A*1 loses the ability to control *VP*. The core must therefore incorporate a startup circuit.

# Core Design

The design of the core presented in Figure 2(a) begins with the choice of the bipolar transistors' dimensions and emitter area ratio, *n*. From the issues outlined in the previous section, we note that the limited voltage headroom makes it desirable to minimize | | *V*BE and, hence, maximize the emitter

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (a) and a graph (b).

### Part (a): Circuit Diagram
The circuit diagram shows a bandgap reference circuit, which is used to generate a stable reference voltage that is relatively independent of temperature variations. The components and their connections are as follows:

1. **Transistors M1 and M2**: These are PMOS transistors connected at the top of the circuit. Their sources are connected to the supply voltage \( V_{DD} \), and their drains are connected to nodes X and Y, respectively.
2. **Operational Amplifier (A1)**: The op-amp has its non-inverting input (+) connected to node X and its inverting input (-) connected to node Y. The output of the op-amp is connected to the gates of M1 and M2.
3. **Resistor (R1)**: A resistor with a value of 2 kΩ is connected between nodes X and Y.
4. **Transistors Q1 and Q2**: These are bipolar junction transistors (BJTs) with their emitters connected to the ground. Q1 has a size ratio of 4x, and Q2 has a size ratio of 64x. The bases of Q1 and Q2 are connected together and to node Y. The collectors of Q1 and Q2 are connected to nodes X and Y, respectively.
5. **Current Sources**: Two current sources, each providing 35 µA, are connected to nodes X and Y, respectively.

The circuit parameters are given as:
- \( \frac{W}{L} = \frac{50 \mu m}{120 nm} \)
- \( A_1 = 100 \)

### Part (b): Graph
The graph plots the voltages \( V_X \) and \( V_P \) against temperature, ranging from 0°C to 100°C. The y-axis represents the voltage in volts (V), and the x-axis represents the temperature in degrees Celsius (°C).

1. **\( V_X \) (Blue Line)**: This voltage decreases linearly with increasing temperature, starting from approximately 0.77 V at 0°C and dropping to about 0.55 V at 100°C.
2. **\( V_P \) (Red Line)**: This voltage increases linearly with increasing temperature, starting from approximately 0.55 V at 0°C and rising to about 0.65 V at 100°C.

The graph shows the temperature dependence of the voltages at nodes X and P, illustrating how the bandgap reference circuit compensates for temperature variations to maintain a stable reference voltage.
```

**FIGURE 3: (a) The preliminary core design and (b) its internal voltages versus** *T***.**

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (labeled as (a)) and a graph (labeled as (b)).

### Part (a): Circuit Diagram
The circuit diagram shows a configuration involving two MOSFET transistors (M1 and M2), an operational amplifier (A1), and two resistors (R1 and another resistor represented as 1/gm1). Here are the key components and their connections:

1. **Power Supply (VDD)**: The positive terminal of the power supply is connected to the drain of transistor M1.
2. **Transistor M1**: The source of M1 is connected to node P, and its gate is connected to node X.
3. **Transistor M2**: The drain of M2 is connected to node P, and its source is connected to ground. The gate of M2 is connected to node Y.
4. **Operational Amplifier (A1)**: The non-inverting input (+) of A1 is connected to node X, and the inverting input (-) is connected to node Y. The output of A1 is connected to node P.
5. **Resistor R1**: One end of R1 is connected to node Y, and the other end is connected to ground.
6. **Resistor 1/gm1**: One end of this resistor is connected to node X, and the other end is connected to ground.

### Part (b): Graph
The graph plots the Power Supply Rejection Ratio (PSRR) in decibels (dB) against frequency in Hertz (Hz). The x-axis represents the frequency on a logarithmic scale ranging from 10^5 Hz to 10^9 Hz. The y-axis represents the PSRR in dB, ranging from -23 dB to -19.5 dB.

Key observations from the graph:
1. At lower frequencies (around 10^5 Hz), the PSRR is approximately -23 dB.
2. As the frequency increases, the PSRR initially remains relatively constant.
3. Around 10^7 Hz, the PSRR starts to increase, reaching a peak of about -19.5 dB at a frequency slightly below 10^9 Hz.
4. After the peak, the PSRR decreases slightly as the frequency approaches 10^9 Hz.

### Summary
The image illustrates a specific electronic circuit and its performance in terms of PSRR across a range of frequencies. The circuit diagram shows a configuration involving MOSFETs, an operational amplifier, and resistors, while the graph provides insight into how the PSRR varies with frequency, showing a notable increase in PSRR at higher frequencies.
```

**FIGURE 4: (a) A test setup for studying PSRR and (b) the PSRR of the basic core.**

Authorized licensed use limited to: UCLA Library. Downloaded on November 30,2021 at 21:02:47 UTC from IEEE Xplore. Restrictions apply.

areas. But the op amp-offset issue demands that *n* also be large, leading to an area-hungry solution. As a reasonable compromise, we select four unit transistors for *Q*<sup>1</sup> , each having

Here is the image describtion:
```
The image depicts a complex transistor circuit, likely part of an analog or mixed-signal integrated circuit. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are PMOS transistors connected at the top of the circuit. Their sources are connected to the supply voltage \( V_{DD} \), and their drains are connected to nodes P and Y, respectively.
   - **Ma and Mb:** These are PMOS transistors forming a current mirror. Their sources are connected to \( V_{DD} \), and their gates are connected together and to the drain of Ma.
   - **MX and MY:** These are NMOS transistors forming a differential pair. Their sources are connected together and to a current source labeled \( I_{SS} \) (50 µA). Their gates are connected to nodes X and Y, respectively.
   - **Q1 and Q2:** These are NMOS transistors with different sizes. Q1 has a size ratio of 4x, and Q2 has a size ratio of 64x. Their sources are connected to the ground, and their gates are connected to nodes X and Y, respectively.

2. **Resistor:**
   - **R1:** This is a resistor with a value of 2 kΩ connected between node Y and the ground.

3. **Current Source:**
   - **I_{SS}:** This is a current source providing a constant current of 50 µA to the sources of transistors MX and MY.

4. **Nodes:**
   - **X and Y:** These are the input nodes for the differential pair transistors MX and MY.
   - **P:** This node is connected to the drain of M1 and the source of Ma.

5. **Dimensions:**
   - The transistors have a width-to-length ratio (W/L) of 50 µm / 120 nm.

The circuit appears to be a differential amplifier with a current mirror load. The differential pair (MX and MY) amplifies the difference between the voltages at nodes X and Y. The current mirror (Ma and Mb) ensures that the current through MX and MY is mirrored accurately. The resistor R1 converts the current difference into a voltage at node Y. The transistors Q1 and Q2, with different sizes, might be used for further amplification or as part of a biasing network.
```

**FIGURE 5: The bandgap core with a simple OTA.**

an emitter area of 5 m*n n* #5 m, and 64 units for *Q*2. Thus, | | *V*BE .750 mV and *V n <sup>T</sup>* ln .72mV at room temperature. The weak dependence of *V n <sup>T</sup>* ln upon *n* suggests that the effect of offset in (7) cannot be reduced easily through this variable.

Another approach to lowering the effect of the op amp offset in Figure 2(a) involves scaling *ID*1 up with respect to *ID*2. Denoting this ratio by *m*, we recognize from (2) that

$$|I\_{D2}|R\_1 = V\_T \ln(n \cdot m). \tag{8}$$

This result carries over to (7). Nevertheless, an *m* value substantially greater than unity also raises | | *V*BE1 , exacerbating the metal-oxide-semiconductor (MOS) transistor voltage headroom iss-ue at low temperatures. For exam-

Here is the image describtion:
```
The image is a graph that plots voltage (V) against temperature (°C). The x-axis represents temperature, ranging from 0°C to 100°C, while the y-axis represents voltage, ranging from 0.5V to 0.8V. 

There are three lines on the graph, each representing a different voltage:

1. **V_X (blue line)**: This line starts at approximately 0.78V at 0°C and decreases linearly to about 0.55V at 100°C. It has a negative slope, indicating that the voltage decreases as the temperature increases.

2. **V_A (red line)**: This line starts at approximately 0.55V at 0°C and increases linearly to about 0.65V at 100°C. It has a positive slope, indicating that the voltage increases as the temperature increases.

3. **V_P (yellow line)**: This line also starts at approximately 0.55V at 0°C and increases linearly to about 0.63V at 100°C. It has a positive slope similar to V_A but is slightly lower in value.

The three lines intersect at different points. Notably, V_X intersects with both V_A and V_P around 70°C. The graph includes a legend in the top right corner that labels each line with its corresponding voltage symbol (V_X, V_A, V_P) and color. The background of the graph is light pink, and the grid lines are gray, aiding in the readability of the data points.
```

**FIGURE 6: The internal voltages of the bandgap core versus** *T***.**

Here is the image describtion:
```
The image is a graph that plots Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from 10^5 Hz (100 kHz) to 10^9 Hz (1 GHz) on a logarithmic scale. The y-axis represents the PSRR, ranging from -60 dB to 20 dB.

There are three curves on the graph, each representing PSRR at different temperatures:
1. The blue curve represents PSRR at 0°C.
2. The red curve represents PSRR at 50°C.
3. The yellow curve represents PSRR at 100°C.

Observations:
- At lower frequencies (around 10^5 Hz), the PSRR is relatively stable for all three temperatures, with the blue curve (0°C) showing the highest PSRR, followed by the red curve (50°C), and the yellow curve (100°C) showing the lowest PSRR.
- As the frequency increases, the PSRR for all three temperatures starts to decrease.
- Around 10^7 Hz, the PSRR begins to drop more sharply for all three temperatures.
- At higher frequencies (approaching 10^9 Hz), the PSRR for all three temperatures converges and increases, with the curves becoming almost indistinguishable from each other.

The graph indicates that PSRR is better (more negative) at lower frequencies and degrades as the frequency increases, with temperature having a noticeable impact on PSRR at lower frequencies but less so at higher frequencies.
```

**FIGURE 7: The PSRR responses of the core for different temperatures.**

The next task is to select the bias current in each branch, the value of *R*1, and the dimensions of *M*1 and *M*2. Anticipating about half a dozen bias currents in the main branches and the op amp(s) in the final design and bearing in mind the 1-mW power budget, we choose | | *I I D D* 1 2 =| |.35 *n* A and hence *R*<sup>1</sup> =2kX. For the PMOS transistors, the channel area must be large enough to minimize mismatch and flicker noise, and the length must be long enough to ensure that channel-length modulation does not limit the supply rejection. Based on these considerations, we select ( / *W L*)1 2, =50 *n*m n /120 m.

Figure 3(a) depicts the preliminary core design. We simulate the circuit while assuming an ideal op amp having a gain of 100. Our objective is twofold: to measure the extreme values of *VX*, *VY*, and *VP* and to quantify the power-supply-rejection ratio (PSRR). In Figure 3(b), *VX* and *VP* are plotted as a function of the temperature. (The high op amp gain guarantees that *V V Y X* . .) These results reveal several points. First, | | *V V P X* - =| | *V V* GS1 1 - DS has a maximum value of about 230 mV, placing *M*1 and *M*2 in saturation. That is, ( ) *W L*/ 1 2, is adequately large. Second, the op amp input stage must operate properly across the common-mode (CM) range of *VX* and *VY* —from around 780 mV to 620 mV. Third, the op amp output must accommodate the variation of *VP* from 550 mV to 640 mV.

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, which appears to be a differential amplifier or a similar analog circuit. The circuit consists of both PMOS and NMOS transistors arranged in a specific configuration.

1. **Transistors:**
   - There are four transistors in total, labeled as \( M_a \), \( M_b \), \( M_1 \), and \( M_2 \).
   - \( M_a \) and \( M_b \) are PMOS transistors, indicated by the arrow pointing outwards from the source.
   - \( M_1 \) and \( M_2 \) are NMOS transistors, indicated by the arrow pointing inwards towards the source.

2. **Connections:**
   - The sources of \( M_a \) and \( M_b \) are connected to a voltage source labeled \( \Delta V_{DD} \).
   - The gates of \( M_a \) and \( M_b \) are connected together and to a node labeled \( A \).
   - The drains of \( M_a \) and \( M_b \) are connected to the drains of \( M_1 \) and \( M_2 \), respectively.
   - The sources of \( M_1 \) and \( M_2 \) are connected to a common node labeled \( P \).
   - The node \( P \) is connected to another voltage source labeled \( \Delta V_{DD} \).

3. **Voltage Sources:**
   - There are three voltage sources in the circuit, all labeled \( \Delta V_{DD} \), which suggests that they are providing a differential voltage supply.
   - The main supply voltage \( V_{DD} \) is connected to the drains of \( M_1 \) and \( M_2 \).

4. **Circuit Function:**
   - The circuit is likely a differential amplifier, where \( M_a \) and \( M_b \) form the differential pair, and \( M_1 \) and \( M_2 \) act as the load transistors.
   - The node \( A \) is the input node for the differential signal.
   - The node \( P \) is the common source node for the differential pair.

5. **Operation:**
   - When a differential input signal is applied to the gates of \( M_a \) and \( M_b \), the current through \( M_a \) and \( M_b \) will vary depending on the input voltage difference.
   - This variation in current will be mirrored by \( M_1 \) and \( M_2 \), producing a differential output voltage at the drains of \( M_1 \) and \( M_2 \).

In summary, the image shows a differential amplifier circuit with PMOS transistors forming the differential pair and NMOS transistors acting as the load, with differential voltage sources applied to the circuit.
```

**FIGURE 8: The bootstrapping of node** *P* **by the OTA active load.**

#### 8 SUMMER 2021 *IEEE SOLID-STATE CIRCUITS MAGAZINE*

Next, we investigate the core's supply rejection by constructing the setup displayed in Figure 4. The supply voltage varies by a small amount, T*V*DD, and *Q*1 and *Q*2 are replaced with their small-signal resistances. Note that 1 1 / / *g g m m* 1 2 = because *Q*<sup>1</sup> and *Q*2 carry equal currents. If *ID*1 and *ID*2 change by T*ID*, we have

$$
\Delta V\_Y - \Delta V\_X = \Delta I\_D \left( R\_1 + \frac{1}{\mathcal{G}\_{m2}} \right) - \Delta I\_D \frac{1}{\mathcal{G}\_{m1}} \tag{9}
$$

$$
= \Delta I\_D R\_1,\tag{10}
$$

and, hence, T T *V A P D* = 1 1 *I R* . In a well-designed circuit, we expect T*ID* to be small and *V*GS1,2 to be relatively constant, which predicts that T T *V V <sup>P</sup>* . DD . It follows that

$$
\Delta I\_D \approx \frac{\Delta V\_{\rm DD}}{\overline{A\_1}\,\overline{R\_1}}.\tag{11}
$$

We now ask, which quantity is the "output" of interest here? Since the drain current of *M*1 and *M*2 is eventually copied and applied to a resistor [e.g., *RL* in Figure 2(c)] to generate the reference voltage, we define the PSRR as

$$\text{PSRR} = \frac{\Delta V\_{\text{DD}}}{\Delta I\_{\text{D}} R\_L} \tag{12}$$

$$\approx \frac{A\_1 R\_1}{R\_L}. \tag{13}$$

Moreover, if *R*1 sustains a voltage of *V n <sup>T</sup>* ln .72mV mV and *RL* an output voltage of 500 mV, we have *R R* <sup>1</sup>/ *<sup>L</sup>* = 0 1. . 4 It follows that

$$\text{PSRR} = 0.14 \, A\_1 \,. \tag{14}$$

For 40 dB of rejection, *A*1 must exceed 700. In practice, the PSRR is plotted as the inverse of the previous quantities, i.e., as the magnitude of the transfer function from *V*DD to the output of interest.

For initial PSRR simulations, we simply multiply the voltage variation across *R*1 by 1 0/ . , 14 arriving at the plot presented in Figure 4(b). For supply-perturbation frequencies up to tens of megahertz, the PSRR is around –23 dB, which agrees with (14). At higher frequencies, *C C* GS1 2 + GS in Figure 4(a) couples the *V*DD changes to *C*GD1 and *C*GD2, causing *VX* and *VY* to bounce. The PSRR

Here is the image describtion:
```
The image depicts a differential amplifier circuit with active loads. Here is a detailed description of the circuit components and their connections:

1. **Transistors:**
   - There are six MOSFET transistors labeled as \(M_a\), \(M_b\), \(M_c\), \(M_d\), \(M_X\), and \(M_Y\).
   - \(M_a\) and \(M_b\) are the main differential pair transistors.
   - \(M_c\) and \(M_d\) are the active load transistors.
   - \(M_X\) and \(M_Y\) are the tail current source transistors.

2. **Resistors:**
   - Two resistors, \(R_a\) and \(R_b\), are connected in series between the drains of \(M_a\) and \(M_b\).
   - The values of \(R_a\) and \(R_b\) are both 40 kΩ.

3. **Current Source:**
   - There is a current source labeled \(I_{SS}\) providing a current of 50 µA, connected to the sources of \(M_X\) and \(M_Y\).

4. **Power Supply:**
   - The circuit is powered by a voltage source \(V_{DD}\) connected to the drains of \(M_c\) and \(M_d\).

5. **Inputs and Outputs:**
   - The input signals are applied at nodes \(X\) and \(Y\), which are connected to the gates of \(M_X\) and \(M_Y\), respectively.
   - The output is taken from the node labeled "To Node P," which is connected to the drain of \(M_d\).

6. **Transistor Dimensions:**
   - The width-to-length ratio (\(W/L\)) of the transistors is given as 50 µm / 120 nm.

In summary, this is a differential amplifier circuit with active loads, where the differential pair transistors \(M_a\) and \(M_b\) are loaded by the active load transistors \(M_c\) and \(M_d\). The resistors \(R_a\) and \(R_b\) provide additional resistance in the circuit, and the current source \(I_{SS}\) sets the tail current for the differential pair. The output is taken from the drain of \(M_d\).
```

**FIGURE 9: A two-stage op amp for use in the bandgap reference.**

is far short of the desired value, necessitating further design efforts.

#### Op Amp Design

Since the op amp in Figure 3(a) must operate with input CM levels as high as 780 mV, we select an NMOS input stage for it. The simplest implementation is a five-transistor operational transconductance amplifier (OTA), as presented in Figure 5. We assume *W L*/ / =50 *n*m n 120 m for all of the transistors. With a tail current of 50 *μ*A, the op amp provides a gain of about 20, and *MX* and *MY* exhibit a minimum source voltage of 350 mV at *T* =100 Cc , which is sufficient for *I*SS . However, at *T* = 0 Cc , both | | *V*BE and | | *V*TH1,2 take on large values, possibly pushing *MX* into the triode region and lowering the op amp gain. Figure 6 plots *VX*, *VA*, and *VP* versus *T*, demonstrating that *V V X A* keeps *MX* in saturation. Figure 7

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, specifically a differential amplifier with active loads. Here is a detailed description of the circuit:

1. **Transistors**:
   - There are four MOSFET transistors labeled \( M_c \), \( M_a \), \( M_b \), and \( M_d \).
   - \( M_a \) and \( M_b \) are the input transistors of the differential pair.
   - \( M_c \) and \( M_d \) are the active load transistors.

2. **Connections**:
   - The sources of \( M_a \) and \( M_b \) are connected together and to a current source (not shown in the image) which typically would be connected to the ground.
   - The drains of \( M_a \) and \( M_b \) are connected to the drains of \( M_c \) and \( M_d \) respectively.
   - The gates of \( M_c \) and \( M_d \) are connected to a common voltage \( V_{DD} \), which is the supply voltage.

3. **Inputs**:
   - The gates of \( M_a \) and \( M_b \) are the differential inputs, labeled as \( \Delta V_{DD} \).

4. **Outputs**:
   - The drains of \( M_c \) and \( M_d \) are the differential outputs, also labeled as \( \Delta V_{DD} \).

5. **Power Supply**:
   - The circuit is powered by a voltage source \( V_{DD} \), which is connected to the sources of \( M_c \) and \( M_d \).

6. **Resistors**:
   - There are resistors connected between the gates of \( M_a \) and \( M_b \) and the common node between the sources of \( M_a \) and \( M_b \).

This configuration is typical for a differential amplifier, where \( M_a \) and \( M_b \) form the differential pair, and \( M_c \) and \( M_d \) act as active loads to provide high gain. The differential inputs \( \Delta V_{DD} \) are applied to the gates of \( M_a \) and \( M_b \), and the differential output is taken from the drains of \( M_c \) and \( M_d \).
```

**FIGURE 10: Paths from** *V***DD to the internal nodes of the two-stage op amp.**

presents how the PSRR responses at *T* = 0 Cc , 50c C, and 100c C illustrate a degradation at low temperatures.

An interesting observation in Figure 7 is that the low-frequency PSRR is around –35 dB at *T* = 0 Cc , whereas (14) would yield 1 0 /( .14*A*1) / -9dB for *A*<sup>1</sup> =20. Why is the performance better than expected? In the analysis leading to (14), we assumed that the op amp must multiply *V V Y X* - by *A*<sup>1</sup> to adjust *VP* and allow it to track *V*DD. However, in the circuit of Figure 5, the OTA provides an additional

Here is the image describtion:
```
The image is a graph that plots Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from \(10^5\) Hz (100 kHz) to \(10^9\) Hz (1 GHz). The y-axis represents the PSRR, ranging from -60 dB to 20 dB.

There are three curves on the graph, each representing PSRR at different temperatures: 0°C, 50°C, and 100°C. The blue curve represents 0°C, the red curve represents 50°C, and the yellow curve represents 100°C.

Key observations from the graph:
- At lower frequencies (around \(10^5\) Hz), the PSRR is approximately -40 dB for all three temperatures.
- As the frequency increases, the PSRR for the 0°C curve (blue) decreases more significantly compared to the other two curves, reaching around -55 dB at \(10^6\) Hz.
- Beyond \(10^6\) Hz, the PSRR for all three temperatures starts to increase.
- At higher frequencies (approaching \(10^9\) Hz), the PSRR for all three temperatures converges and increases to around 10 dB.

The graph shows that the PSRR is temperature-dependent, with the PSRR at 0°C being lower at certain frequencies compared to 50°C and 100°C. However, at very high frequencies, the PSRR values for all temperatures converge.
```

**FIGURE 11: The PSRR of the core with a two-stage op amp.**

Authorized licensed use limited to: UCLA Library. Downloaded on November 30,2021 at 21:02:47 UTC from IEEE Xplore. Restrictions apply.

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (part a) and a graph (part b).

### Part (a): Circuit Diagram
The circuit diagram shows a bandgap reference circuit, which is commonly used to generate a stable reference voltage that is independent of temperature variations. Here are the key components and their connections:

1. **Transistors and Current Sources:**
   - **M1 and M2:** These are PMOS transistors connected to the positive supply voltage \( V_{DD} \).
   - **M3:** Another PMOS transistor connected to \( V_{DD} \) and the output voltage \( V_{out} \).
   - **Q1 and Q2:** These are bipolar junction transistors (BJTs) with different emitter areas (Q1 has 4 times the emitter area of Q2).

2. **Operational Amplifier (A1):**
   - The operational amplifier (A1) has its non-inverting input connected to node X and its inverting input connected to node Y.
   - The output of the operational amplifier is connected to the gate of M1 and M2 at node P.

3. **Resistors:**
   - **R1:** A 2 kΩ resistor connected between the emitter of Q2 and ground.
   - **R2:** A 13 kΩ resistor connected between the emitter of Q1 and ground.
   - **R3:** A 13 kΩ resistor connected between the source of M3 and ground.
   - **R_L:** A 5.5 kΩ load resistor connected between the source of M3 and ground.

4. **Current Sources:**
   - Two current sources, each providing 35 µA, are connected to the collectors of Q1 and Q2.

5. **Transistor Dimensions:**
   - The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.

### Part (b): Graph
The graph plots the current \( |I_{D2}| \) (in µA) against temperature (in °C). The key features of the graph are:

- The x-axis represents the temperature, ranging from 0°C to 100°C.
- The y-axis represents the current \( |I_{D2}| \) in microamperes (µA), ranging from 93.25 µA to 93.65 µA.
- The graph shows a positive slope, indicating that the current \( |I_{D2}| \) increases with temperature.

### Summary
The circuit in part (a) is designed to provide a stable reference voltage, and the graph in part (b) shows how the current \( |I_{D2}| \) varies with temperature, demonstrating the temperature dependence of the circuit's performance.
```

**FIGURE 12: (a) The bandgap reference with** *R***2 and** *R***3 added and (b) the drain current of** *M***2 versus** *T***.**

Here is the image describtion:
```
The image is a graph that plots voltage (V) against temperature (°C). The x-axis represents temperature, ranging from 0°C to 100°C, while the y-axis represents voltage, ranging from 0.5V to 0.8V. 

There are two lines plotted on the graph:
1. A blue line labeled \( V_Y \) which starts at approximately 0.77V at 0°C and decreases linearly to about 0.58V at 100°C.
2. A red line labeled \( V_{out} \) which starts at approximately 0.58V at 0°C and decreases more gradually to about 0.53V at 100°C.

The background of the graph is light pink, and there is a legend in the upper right corner that identifies the blue line as \( V_Y \) and the red line as \( V_{out} \). The graph has grid lines to help with reading the values more accurately.
```

**FIGURE 13: The voltages at node** *Y* **and at the output of the bandgap circuit versus** *T***.**

Here is the image describtion:
```
The image depicts a complex analog circuit, likely a part of an integrated circuit design, featuring multiple transistors, resistors, and operational amplifiers. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors connected in a current mirror configuration. The gate of M1 is connected to the gate of M2, and both gates are connected to node P. The source of M1 is connected to the output of operational amplifier A1, while the source of M2 is connected to node Y.
   - **M3 and M4:** These are also NMOS transistors. The gate of M3 is connected to node N, and the gate of M4 is connected to the output of operational amplifier A2. The source of M3 is connected to node N, and the source of M4 is connected to the output node Vout.

2. **Operational Amplifiers:**
   - **A1:** This op-amp has its non-inverting input connected to node X and its inverting input connected to node Y. The output of A1 is connected to the gate of M1.
   - **A2:** This op-amp has its non-inverting input connected to node N and its inverting input connected to the junction of R3 and RL. The output of A2 is connected to the gate of M4.

3. **Resistors:**
   - **R1:** A 2 kΩ resistor connected between node Y and the emitter of transistor Q2.
   - **R2:** A 13 kΩ resistor connected between the base of transistor Q1 and ground.
   - **R3:** A 13 kΩ resistor connected between node N and the inverting input of A2.
   - **RL:** A 5.5 kΩ load resistor connected between the output node Vout and ground.

4. **Current Sources:**
   - Two current sources, each providing 35 µA, are connected to the drains of M1 and M2, respectively.

5. **Transistors Q1 and Q2:**
   - **Q1:** A bipolar junction transistor (BJT) with its base connected to R2, its emitter connected to ground, and its collector connected to node X.
   - **Q2:** Another BJT with its base connected to node X, its emitter connected to ground through a scaling factor of 4x, and its collector connected to node Y through a scaling factor of 64x.

6. **Dimensions:**
   - The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.

7. **Power Supply:**
   - The circuit is powered by a supply voltage VDD connected to the drains of M1, M2, and M3.

The circuit appears to be a part of a precision analog design, possibly a current mirror or a differential amplifier with additional stages for amplification and feedback control. The use of operational amplifiers and precise resistor values suggests a focus on maintaining accuracy and stability in the circuit's operation.
```

**FIGURE 14: The bandgap circuit with a regulated cascode.**

tracking mechanism: If *V*DD varies by T*V*DD, so do *VA and VP* (Figure 8). In essence, the OTA's PMOS active load bootstraps *P* to *V*DD.

That T T *V V P A* . can be seen by noting that, in the absence of asymmetries within the op amp, *V V P A* = if *V V X Y* = . This property is generally considered a drawback of the fivetransistor OTA, but it proves useful here. Since the *V*DD perturbation is directly applied to node *P* by *Ma* and *Mb*, the op amp provides only additional correction.

The PSRR degradation at low temperatures calls for a higher op amp gain and, hence, a two-stage topology. Figure 9 illustrates a simple design wherein the output CM level of the first stage is set by *Ra* and *Rb* to be equal to one PMOS source-gate voltage below *V*DD. This method also defines the bias currents of the second stage by forming current mirrors. Thus, the total supply current is about 100 *μ*A. This op amp offers a gain of 380 at *T* = 0 Cc and 320 at *T* =100 Cc , improving the PSRR according to (14).

Does the effect illustrated in Figure 8 exist in the two-stage op amp as well? If *V V X Y* . and *V*DD changes by T*V*DD, then so do the drain voltages of *Ma* and *Mb* (Figure 10). We observe that the gate-source voltages of *Mc* and *Md* remain relatively constant, introducing little change at their drains and, hence, in *VP* . In other words, this op amp does not provide the direct cancelation mechanism of the five-transistor OTA. Figure 11 plots the bandgap core PSRR in the presence of the two-stage op amp.

# Complete Bandgap Reference

As prescribed by Figure 2(b), we must attach equal resistors from nodes *X* and *Y* to the ground to change the nature of *ID*1 and *ID*2 from PTAT to temperature-independent quantities. This requires that ( ) *R R* 3 1 / *V n <sup>T</sup>* ln be around 17*VT* and *R R* 2 3 = . 6*R*1 if *n* =16. Figure 12 displays the modified circuit as well as | | *ID*2 versus *T*. Resistors *R*2 and *R*3 are rounded up to 13kX, and the op amp is implemented as the two-stage topology of Figure 9. We note that | | *ID*2 changes by less than 0.4% across our temperature range of interest.

In the next step, we copy *ID*2 and apply the result to *RL*, forming the reference voltage, *V*out . According to (6), an output voltage of 0.5 V requires *R R <sup>L</sup>* / <sup>2</sup> . 0 4. 2 because the quantity within the parenthesis is around 1.2 V. It follows that *RL* =5 5. . kX Plotted in Figure 13 is *V*out versus *T*, exhibiting a variation of 40 mV.

Why does *V*out drift so much even though *ID*2 is fairly constant? This error arises from the temperaturedependent difference between *V*DS2 and *V*DS3 and the channel-length modulation of *M*2 and *M*3. From Figure 13, we note that *V V <sup>Y</sup>* - out is equal to 200 mV at *T* = 0 Cc and 85 mV at *T* =100 Cc . The relatively long transistor channels still prove inadequate in obtaining an acceptably small current mismatch between *M*2 and *M*3.

The error due to channel-length modulation is suppressed if we guarantee that the drain voltage of *M*3 tracks that of *M*2. This can be accomplished by a regulated cascode structure. Figure 14 illustrates the idea of comparing these voltages by means of op amp *A*2 and adjusting the gate voltage of *M*4 accordingly. As *VY* falls with *T*, so does *VN*, leaving less voltage headroom for *M*<sup>4</sup> and requiring that its overdrive voltage increase. Even if *M*4 operates in the triode region (e.g., at high temperatures), the loop gain provided by *A*2 still ensures that *V V N Y* . . Op amp *A*2 is realized as in Figure 9 but with *W L*/ / =25 *n* m 12 n0 m for all of the transistors. Figure 15 plots *V*out versus *T*, revealing a variation of about 2.5 mV. The total supply current is around 0.5 mA. We have therefore met all of the specifications except for the supply rejection.

Figure 16 depicts the PSRR. Owing to the high op amp gain, the lowfrequency value satisfies our target. Beyond 10 MHz, however, the PSRR degrades because the gain of *A*<sup>1</sup> in Figure 14 begins to fall. This is expected as the op amp's low-bias currents yield a high output resistance, about 45 kΩ, which, along with *CCC* GS1 2 ++= GS GS3 0 3. 5pF, creates an open-loop pole in the vicinity of 10 MHz. To improve the PSRR, we add a simple low-pass filter to the output node. Figure 17 depicts the filter and the resulting PSRR.

## Output Noise and Offset

In most applications, the noise of bandgap references proves critical. A circuit using *ID*2 or *V*out in Figure 14 as a reference can experience performance degradation due to their noise. Figure 18 plots the noise voltage in *V*out . At frequencies up to several hundred megahertz, it is dominated by the flicker noise of *M*2 and *M*3. At 1 GHz, these devices and the first stage of the op amp contribute significant thermal noise.

Here is the image describtion:
```
The image is a graph that plots the output voltage (V_out) against temperature (°C). The x-axis represents the temperature in degrees Celsius, ranging from 0°C to 100°C. The y-axis represents the output voltage in volts, ranging from 0.513 V to 0.5155 V.

The graph shows a single curve that starts at approximately 0.5132 V when the temperature is 0°C and gradually increases as the temperature rises. The curve is smooth and slightly concave upwards, indicating a positive correlation between temperature and output voltage. At 100°C, the output voltage reaches approximately 0.5152 V.

The background of the graph is light pink, and the grid lines are gray, providing a clear contrast with the blue curve representing the data. The labels on the axes are in black, with the y-axis labeled "V_out (V)" and the x-axis labeled "Temperature (°C)." The graph provides a visual representation of how the output voltage changes with temperature.
```

**FIGURE 15: The output voltage of the final design versus** *T***.**

Here is the image describtion:
```
The image is a graph that plots Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from \(10^5\) Hz (100 kHz) to \(10^9\) Hz (1 GHz) on a logarithmic scale. The y-axis represents the PSRR, ranging from -50 dB to 20 dB.

The graph shows a curve that starts at around -40 dB at \(10^5\) Hz and remains relatively flat until approximately \(10^7\) Hz (10 MHz). After this point, the curve begins to rise, indicating a decrease in PSRR, and continues to increase steeply as the frequency approaches \(10^9\) Hz (1 GHz). The PSRR reaches 0 dB at around \(10^8\) Hz (100 MHz) and continues to rise above 0 dB as the frequency increases further.

The background of the graph is light pink, and the grid lines are in a light gray color, providing a clear contrast to the blue curve representing the PSRR data.
```

**FIGURE 16: The PSRR of the final design.**

If the output noise is unacceptably high for a given application, we can pursue three methods to reduce it. First, to lower the flicker noise, the channel areas of *M*1–*M*3 can be increased while maintaining their *W L*/ ratio. Second, the widths and bias currents of *M*1–*M*3 and the areas of *Q*1 and *Q*2 can be scaled up, and the values of all of the resistors can be scaled down by the same factor to reduce the output thermal noise. This remedy trades noise for area and power. Third, the output lowpass filter can incorporate larger capacitors, but at the cost of area.

The op amp offset, *V*OS, arises primarily from the first stage in Figure 9. Writing the threshold mismatch as T*V A* TH = VTH / *WL* and assuming

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (a) and a graph (b).

(a) Circuit Diagram:
- The circuit features a MOSFET transistor labeled M4.
- The source of M4 is connected to ground.
- The gate of M4 is connected to a node that is also connected to a 5.5 kΩ resistor (RL) and a 1 pF capacitor, both of which are connected to ground.
- The drain of M4 is connected to another 5.5 kΩ resistor.
- The other end of this 5.5 kΩ resistor is connected to the output node (Vout).
- The output node (Vout) is also connected to a 1 pF capacitor, which is connected to ground.

(b) Graph:
- The graph plots Power Supply Rejection Ratio (PSRR) in decibels (dB) on the vertical axis against Frequency in Hertz (Hz) on the horizontal axis.
- The frequency range spans from 10^5 Hz (100 kHz) to 10^9 Hz (1 GHz).
- The PSRR values range from -44 dB to -54 dB.
- The PSRR curve starts at around -44 dB at 10^5 Hz, dips to approximately -52 dB around 10^8 Hz, and then rises slightly before dipping again near 10^9 Hz.

Overall, the image illustrates the PSRR performance of the given circuit over a wide frequency range.
```

**FIGURE 17: (a) The addition of a low-pass filter and (b) the resulting PSRR.**

Here is the image describtion:
```
The image is a graph that plots Output Noise (in nV/√Hz) against Frequency (in Hz). The x-axis represents the frequency on a logarithmic scale, ranging from 10^4 Hz (10,000 Hz) to 10^9 Hz (1,000,000,000 Hz). The y-axis represents the output noise, also on a logarithmic scale, ranging from 0 to 700 nV/√Hz.

The graph shows a curve that starts at a high noise level of around 600 nV/√Hz at 10^4 Hz. As the frequency increases, the noise level decreases sharply, reaching around 100 nV/√Hz at approximately 10^5 Hz. The noise level continues to decrease more gradually, reaching a minimum of around 50 nV/√Hz between 10^6 Hz and 10^7 Hz. After this point, the noise level remains relatively constant until it starts to increase slightly again as the frequency approaches 10^9 Hz.

The overall trend of the graph indicates that the output noise decreases with increasing frequency up to a certain point, after which it stabilizes and then slightly increases at very high frequencies.
```

**FIGURE 18: The output noise voltage of the bandgap reference.**

Here is the image describtion:
```
The image shows two different circuit diagrams labeled (a) and (b). Both circuits appear to be related to MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) configurations, likely for amplification or switching purposes.

### Circuit (a):
1. **Power Supply**: The circuit is powered by a voltage source labeled as 1V, which is connected to the top rail of the circuit.
2. **Capacitor (C_S)**: There is a capacitor labeled \( C_S \) connected between the voltage source and the gate of the MOSFET \( M_S \).
3. **Resistor (R_S)**: A resistor labeled \( R_S \) is connected between the gate of \( M_S \) and ground.
4. **MOSFET (M_S)**: The MOSFET \( M_S \) has its gate connected to the junction of \( C_S \) and \( R_S \), its source connected to ground, and its drain connected to the node \( P \).
5. **Current Mirror**: The node \( P \) is connected to the drains of two MOSFETs \( M_1 \) and \( M_2 \), which form a current mirror configuration. The sources of \( M_1 \) and \( M_2 \) are connected to the power supply \( V_{DD} \).

### Circuit (b):
1. **Power Supply**: Similar to circuit (a), this circuit is also powered by a voltage source \( V_{DD} \) connected to the top rail.
2. **Operational Amplifier (A_3)**: There is an operational amplifier \( A_3 \) with its non-inverting input (+) connected to a reference voltage \( V_r \) and its inverting input (-) connected to the output voltage \( V_{out} \).
3. **Inverter**: The output of the operational amplifier \( A_3 \) is connected to an inverter.
4. **MOSFET (M_S)**: The output of the inverter is connected to the gate of the MOSFET \( M_S \). The source of \( M_S \) is connected to ground, and the drain is connected to the node \( P \).
5. **Current Mirror**: Similar to circuit (a), the node \( P \) is connected to the drains of two MOSFETs \( M_1 \) and \( M_2 \), forming a current mirror. The sources of \( M_1 \) and \( M_2 \) are connected to the power supply \( V_{DD} \).

### Common Elements:
- Both circuits use a current mirror configuration with MOSFETs \( M_1 \) and \( M_2 \).
- Both circuits have a node \( P \) that connects the drain of \( M_S \) to the current mirror.
- Both circuits are powered by a voltage source \( V_{DD} \).

### Differences:
- Circuit (a) uses a capacitor \( C_S \) and a resistor \( R_S \) to control the gate of \( M_S \).
- Circuit (b) uses an operational amplifier \( A_3 \) and an inverter to control the gate of \( M_S \).

These circuits are likely used in applications where precise control of the current through \( M_S \) is required, such as in analog signal processing or sensor interfacing.
```

**FIGURE 19: The start-up circuits using (a) a timing mechanism and (b) a high-gain comparison method.** *(continued on p. 16)*

*A*VTH .3mV, we obtain *V*OS .1 7. mV. From (7), this translates to an error of about 5 mV in *V*out, which is a reasonable amount.

#### Start-Up and Transient Response

To ensure that the reference generator of Figure 14 reaches the desired state when the circuit is turned on, we must examine the initial behavior of the core and the two-stage op amp. Suppose *VX* and *VY* are zero at powerup. Then, *MX*, *MY*, *Ma*, and *Mb* in Figure 9 remain off, and so do *Mc* and *Md*. We recognize that node *P* floats, possibly keeping *M*1 and *M*2 off as well. This degenerate state can be avoided if we add a means to prohibit *VP* from staying high when the circuit turns on.

Whether a bandgap remains off or not depends on a number of factors. Capacitive coupling paths from *V*DD to the internal nodes, e.g., to *X* and *Y* in Figure 14, can turn on the circuit. Also, the slope of the *V*DD ramp and the temperature may encourage or impede the start-up process.

To ensure start-up, we can employ a timing circuit to initially keep node *P* in Figure 14 low. Figure 19(a) illustrates the idea of drawing a current from *P* by *MS* as node *G* tracks the *V*DD ramp and exceeds the transistor threshold. After *V*DD stabilizes, *VG* returns to zero. The drawback of this approach is that if *V*DD takes, for example, 1 ms to ramp up, then *R*1 and *C*1 must be extremely large to permit *G* to go high.

We instead explore a different line of thought: if the circuit remains inactive after *V*DD rises, then *V*out in Figure 14 is zero and can be compared to a reference roughly representing its desired value. The result can then enable a mechanism to draw current from *P*. As depicted in Figure 19(b), amplifier *A*3 compares *V*out to *Vr* and turns on *MS* if the former is well below the latter. The amplifier is implemented as the OTA displayed in Figure 5, except *W L*/ is chosen to be equal to 5 3 *n*m n / 0 m for all of the transistors. To accommodate the offset of *A*3, we select

#### 12 SUMMER 2021 *IEEE SOLID-STATE CIRCUITS MAGAZINE*

of ac coupling attenuates the low-frequency component of the signal, causing baseline wander, which may result in the loss of data in wireline communication. To restore this low-frequency component for a random binary sequence or, equivalently, to remove the base line wander, we employ a comparator with quantized feedback in conjunction with superposition.

# Acknowledgment

I would like to thank Hossein Shakiba (the author of [2]) for his insights and discussions that inspired this article.

#### References

- [1] B. E . Boser, "Offset control," in *EECS 247: Lecture Notes 27*, Berkeley, CA: Univ. of California, 2002, pp. 1–15. [Online]. Available: https://inst.eecs .berkeley.edu//~n247/fa07/lectures/L27 .pdf
- [2] M. H. Shakiba, "A 2.5Gb/s adaptive cable equalizer," in *Proc*. *Dig. Tech. IEEE Int. Solid-State Circuits Conf. (ISSCC)*, Feb. 1999, pp. 396–397. doi: 10.1109/ISSCC .1999.759317.
- [3] F. Waldhauer "Quantized feedback in an experimental 280-Mb/s digital repeater for coaxial transmission," *IEEE Trans. Commun.*, vol. 22, no. 1, pp. 1–5, Jan. 1974. doi: 10.1109/TCOM.1974.1092055.
- [4] A. Sheikholeslami, "Circuit intuitions: Equalizer circuit," *IEEE Solid State Circuits Mag.*, vol. 12, no. 1, pp. 6–7, Winter 2020. doi: 10.1109/MSSC.2019.2952233.

# **THE ANALOG MIND**

*(continued from p. 12)*

Here is the image describtion:
```
The image consists of two graphs, labeled (a) and (b), each depicting voltage versus time. Both graphs have a pink background and share the same axes: the x-axis represents time in nanoseconds (ns), ranging from 0 to 1,000 ns, and the y-axis represents voltage in volts (V), ranging from 0 to 1 V.

In both graphs, three voltage curves are plotted:
1. \( V_{DD} \) (blue line)
2. \( V_P \) (red line)
3. \( V_{out} \) (yellow line)

### Graph (a):
- The blue line (\( V_{DD} \)) shows a linear increase from 0 V at 0 ns to 1 V at 1,000 ns.
- The red line (\( V_P \)) starts at 0 V and increases gradually, reaching approximately 0.6 V at around 800 ns, then it fluctuates and peaks just below 1 V before stabilizing.
- The yellow line (\( V_{out} \)) remains at 0 V until around 800 ns, then it spikes sharply to about 0.8 V, fluctuates, and eventually stabilizes around 0.2 V.

### Graph (b):
- The blue line (\( V_{DD} \)) is identical to that in graph (a), showing a linear increase from 0 V at 0 ns to 1 V at 1,000 ns.
- The red line (\( V_P \)) starts at 0 V and increases gradually, with several fluctuations, reaching approximately 0.6 V at around 800 ns, and then it stabilizes around 0.5 V.
- The yellow line (\( V_{out} \)) starts at 0 V and increases gradually with several fluctuations, following a similar pattern to the red line but with slightly lower values, and stabilizes around 0.4 V.

Both graphs include a legend at the bottom center, indicating the color coding for the three voltage curves: \( V_{DD} \) (blue), \( V_P \) (red), and \( V_{out} \) (yellow).
```

**FIGURE 20: The bandgap internal waveforms (a) without and (b) with the start-up circuit.**

*Vr* . 0 4. V and generate it from *V*DD by a resistive divider. Figure 20(a) and (b) plots *V*DD, *VP*, and *V*out for a 900-ns *V*DD ramp before and after the start-up circuit is added, respectively. We note that the former fails (in fact, it oscillates with a period of several microseconds) whereas the latter settles properly. For a 1-ms *V*DD ramp, the bandgap turns on with or without the start-up mechanism.

#### References

- [1] R. J. Widlar, "Some circuit design techniques for linear integrated circuits," *IEEE Trans. Circuit Theory*, vol. 12, no. 4, pp. 586–590, Dec. 1965. doi: 10.1109/TCT .1965.1082512.
- [2] R. J. Widlar, "New developments in IC voltage regulators," *IEEE J. Solid-State Circuits*, vol. 6, no. 1, pp. 2–7, Feb. 1971. doi: 10.1109/JSSC.1971.1050151.
- [3] A. P. Brokaw, "A simple three-terminal IC bandgap reference," *IEEE J. Solid-State Circuits*, vol. 9, no. 6, pp. 388–393, Dec. 1974. doi: 10.1109/JSSC.1974.1050532.
- [4] R. A. Blauschild, P. A. Tucci, R. S. Muller, and R. G. Meyer, "A new NMOS temperature-

stable voltage reference," *IEEE J. Solid-State Circuits*, vol. 13, no. 6, pp. 767–774, Dec. 1978. doi: 10.1109/JSSC.1978.1052048.

- [5] Y. P. Tsividis and R. W. Ulmer, "A CMOS voltage reference," *IEEE J. Solid-State Circuits*, vol. 13, no. 6, pp. 774–778, Dec. 1978. doi: 10.1109/JSSC.1978.1052049.
- [6] E. A. Vittoz and O. Neyroud, "A low-voltage CMOS bandgap reference," *IEEE J. Solid-State Circuits*, vol. 14, no. 3, pp. 573–577, June 1979. doi: 10.1109/JSSC.1979.1051218.
- [7] R. Gregorian, G. Wegner, and W. E. Nicholson, "An integrated single-chip PCM voice codec with filters," *IEEE J. Solid-State Circuits*, vol. 16, no. 4, pp. 322–333, Aug. 1981. doi: 10.1109/JSSC.1981. 1051596.
- [8] K. E. Kujik, "A precision reference voltage source," *IEEE J. Solid-State Circuits*, vol. 8, pp. 222–226, June 1973. doi: 10.1109/JSSC .1973.1050378.
- [9] H. Banba et al., "A CMOS bandgap reference circuit with Sub-1-V operation," *IEEE J. Solid-State Circuits*, vol. 34, no. 5, pp. 670–674, May 1999. doi: 10.1109/4.760378.
- [10] C. J. B. Fayomi et al., "Sub-1-V CMOS bandgap reference design techniques: A survey," *Analog Integr. Circuits Signal Process.*, vol. 62, no. 2, pp. 141–157, Feb. 2010. doi: 10.1007/s10470-009-9352-4.
- [11] H. Neuteboom, B. M. J. Kup, and M. Janssens, "A DSP-based hearing instrument IC," *IEEE J. Solid-State Circuits*, vol. 32, no. 11, pp. 1790–1806, Nov. 1997. doi: 10.1109/ 4.641702.
- [12] B. Razavi, "The bandgap reference," *IEEE Solid State Circuits Mag.*, vol. 8, no. 3, pp. 9–12, Summer 2016. doi: 10.1109/MSSC.2016 .2577978.
- [13] B. Razavi, *Design of Analog CMOS Integrated Circuits*, 2nd ed., New York, NY, USA: McGraw-Hill, 2017.