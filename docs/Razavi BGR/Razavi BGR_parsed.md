Here is the image describtion:
```
The image shows a person wearing a dark suit jacket, a white dress shirt, and a red tie with a subtle pattern. The background is a solid light blue color. Below the image, the name "Behzad Razavi" is written in a bold, black font.
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
The image depicts a simple electronic circuit diagram. The diagram includes the following components and connections:

1. **Power Supply Input**: The circuit starts with a power supply input labeled "1.2 V" on the left side.
2. **LDO (Low Dropout Regulator)**: The 1.2 V input is connected to an LDO regulator. The LDO is represented by a rectangular block labeled "LDO".
3. **Output Voltage**: The output of the LDO is labeled "1 V", indicating that the LDO regulates the input voltage down to 1 V.
4. **Bandgap Reference**: The 1 V output from the LDO is connected to another block labeled "Bandgap Reference". This block is connected to ground (indicated by the ground symbol).
5. **Continuation**: The 1 V output line continues to the right, suggesting that it may be connected to other parts of the circuit not shown in the image.

The overall function of this circuit is to take a 1.2 V input and regulate it down to a stable 1 V output using an LDO, which is then used to power a bandgap reference circuit. The bandgap reference provides a stable reference voltage that is typically used in various analog and digital circuits.
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
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each circuit features a combination of transistors, resistors, and an operational amplifier. Here is a detailed description of each circuit:

### Circuit (a):
- **Transistors**: 
  - Two PMOS transistors labeled M1 and M2 are connected at the top, with their sources connected to V_DD.
  - Two NPN bipolar junction transistors (BJTs) labeled Q1 and Q2 are connected at the bottom.
- **Operational Amplifier**: 
  - An operational amplifier labeled A1 is placed in the middle, with its inverting input (-) connected to node X and its non-inverting input (+) connected to node Y.
- **Resistor**: 
  - A resistor labeled R1 is connected between node Y and ground.
- **Nodes**: 
  - Node X is connected to the drain of M1 and the collector of Q1.
  - Node Y is connected to the drain of M2 and the collector of Q2.
- **Inputs**: 
  - The base of Q1 is connected to a signal labeled A_E.
  - The base of Q2 is connected to a signal labeled nA_E.

### Circuit (b):
- **Transistors**: 
  - Similar to circuit (a), it has two PMOS transistors (M1 and M2) and two NPN BJTs (Q1 and Q2).
- **Operational Amplifier**: 
  - The operational amplifier A1 is configured the same way as in circuit (a).
- **Resistors**: 
  - A resistor labeled R1 is connected between node Y and ground.
  - An additional resistor labeled R2 is connected between node X and ground.
- **Nodes**: 
  - Node X is connected to the drain of M1 and the collector of Q1.
  - Node Y is connected to the drain of M2 and the collector of Q2.
- **Inputs**: 
  - The base of Q1 is connected to a signal labeled A_E.
  - The base of Q2 is connected to a signal labeled nA_E.

### Circuit (c):
- **Transistors**: 
  - In addition to the components in circuits (a) and (b), this circuit includes a third PMOS transistor labeled M3.
- **Operational Amplifier**: 
  - The operational amplifier A1 is configured the same way as in the previous circuits.
- **Resistors**: 
  - Resistor R1 is connected between node Y and ground.
  - Resistor R2 is connected between node X and ground.
  - An additional resistor labeled R3 is connected between node Y and the source of M3.
  - A load resistor labeled R_L is connected between the drain of M3 and ground.
- **Nodes**: 
  - Node X is connected to the drain of M1 and the collector of Q1.
  - Node Y is connected to the drain of M2 and the collector of Q2.
  - The source of M3 is connected to node Y, and its drain is connected to V_out.
- **Inputs**: 
  - The base of Q1 is connected to a signal labeled A_E.
  - The base of Q2 is connected to a signal labeled nA_E.

In summary, the three circuits show progressively more complex configurations of transistors, resistors, and an operational amplifier, with circuit (c) being the most complex, including an additional PMOS transistor and a load resistor.
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
The image consists of two parts: a circuit diagram (a) on the left and a graph (b) on the right.

(a) The circuit diagram shows a current mirror circuit with an operational amplifier (A1) and two transistors (M1 and M2). The circuit includes the following components:
- Two NMOS transistors, M1 and M2, connected in a current mirror configuration.
- An operational amplifier (A1) with its inverting input connected to node X and its non-inverting input connected to node Y.
- Two bipolar junction transistors (BJTs), Q1 and Q2, with their emitters connected to ground. Q1 has a current gain of 4x, and Q2 has a current gain of 64x.
- A resistor (R1) with a resistance of 2 kΩ connected between node Y and the collector of Q2.
- A current source providing 35 µA to the drain of M1 and another current source providing 35 µA to the drain of M2.
- The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.
- The amplifier A1 has a gain of 100.

(b) The graph on the right plots voltage against temperature. It shows two curves:
- The blue curve (V_X) represents the voltage at node X, which decreases linearly with increasing temperature.
- The red curve (V_P) represents the voltage at node P, which increases linearly with increasing temperature.
- The x-axis represents temperature in degrees Celsius (°C), ranging from 0 to 100.
- The y-axis represents voltage in volts (V), ranging from 0.5 to 0.8.

The graph indicates that as the temperature increases, V_X decreases while V_P increases.
```

**FIGURE 3: (a) The preliminary core design and (b) its internal voltages versus** *T***.**

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b).

(a) The left part of the image is a schematic diagram of an electronic circuit. The circuit includes the following components:
- A voltage source labeled \( V_{DD} \) connected to the drain of a PMOS transistor \( M_1 \).
- The source of \( M_1 \) is connected to a node labeled \( P \).
- Another PMOS transistor \( M_2 \) has its source connected to the same node \( P \) and its drain connected to a node labeled \( Y \).
- The gate of \( M_1 \) is connected to a node labeled \( X \).
- The gate of \( M_2 \) is connected to the output of an operational amplifier \( A_1 \).
- The operational amplifier \( A_1 \) has its inverting input connected to node \( X \) and its non-inverting input connected to node \( Y \).
- Node \( X \) is connected to ground through a resistor with a value of \( \frac{1}{g_{m1}} \).
- Node \( Y \) is connected to ground through a resistor labeled \( R_1 \) with a value of \( \frac{1}{g_{m2}} \).

(b) The right part of the image is a graph plotting Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency on a logarithmic scale ranging from \( 10^5 \) Hz to \( 10^9 \) Hz. The y-axis represents the PSRR in dB, ranging from -23 dB to -19.5 dB. The graph shows a curve that starts at around -22.5 dB at \( 10^5 \) Hz, remains relatively flat until around \( 10^7 \) Hz, then rises to a peak of approximately -20 dB at around \( 10^8 \) Hz, and finally dips slightly before rising again towards \( 10^9 \) Hz.
```

**FIGURE 4: (a) A test setup for studying PSRR and (b) the PSRR of the basic core.**

Authorized licensed use limited to: UCLA Library. Downloaded on November 30,2021 at 21:02:47 UTC from IEEE Xplore. Restrictions apply.

areas. But the op amp-offset issue demands that *n* also be large, leading to an area-hungry solution. As a reasonable compromise, we select four unit transistors for *Q*<sup>1</sup> , each having

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. The circuit includes several transistors, resistors, and current sources, and is designed to amplify the difference between two input signals.

Key components and their connections are as follows:

1. **Transistors:**
   - **M1 and M2:** These are the main transistors connected to the power supply voltage \( V_{DD} \) at the top. They are part of the differential pair.
   - **Ma and Mb:** These transistors are part of a current mirror configuration, which is used to ensure that the current through M1 and M2 is mirrored accurately.
   - **MX and MY:** These transistors are also part of the current mirror and are connected to nodes A and Y respectively.
   - **Q1 and Q2:** These are additional transistors connected to the ground. Q1 has a size ratio of 4x, and Q2 has a size ratio of 64x.

2. **Resistors:**
   - **R1:** This resistor has a value of 2 kΩ and is connected between node Y and the ground.

3. **Current Source:**
   - **ISS:** This is a current source providing a constant current of 50 µA.

4. **Nodes and Connections:**
   - **X and Y:** These are the input nodes where the differential input signals are applied.
   - **P:** This is a node connected to the drain of M2 and the source of Mb.
   - **A:** This is a node connected to the source of Ma and the drain of MX.

5. **Dimensions:**
   - The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.

The circuit operates by amplifying the difference between the voltages at nodes X and Y. The current mirror formed by Ma, Mb, MX, and MY ensures that the current through the differential pair (M1 and M2) is balanced, which is crucial for the proper functioning of the differential amplifier. The resistor R1 helps in converting the differential current into a voltage at node Y.
```

**FIGURE 5: The bandgap core with a simple OTA.**

an emitter area of 5 m*n n* #5 m, and 64 units for *Q*2. Thus, | | *V*BE .750 mV and *V n <sup>T</sup>* ln .72mV at room temperature. The weak dependence of *V n <sup>T</sup>* ln upon *n* suggests that the effect of offset in (7) cannot be reduced easily through this variable.

Another approach to lowering the effect of the op amp offset in Figure 2(a) involves scaling *ID*1 up with respect to *ID*2. Denoting this ratio by *m*, we recognize from (2) that

$$|I\_{D2}|R\_1 = V\_T \ln(n \cdot m). \tag{8}$$

This result carries over to (7). Nevertheless, an *m* value substantially greater than unity also raises | | *V*BE1 , exacerbating the metal-oxide-semiconductor (MOS) transistor voltage headroom iss-ue at low temperatures. For exam-

Here is the image describtion:
```
The image is a graph that plots voltage (V) against temperature (°C). The x-axis represents temperature, ranging from 0°C to 100°C, while the y-axis represents voltage, ranging from 0.5V to 0.8V. 

There are three different lines on the graph, each representing a different variable:
1. \( V_X \) (depicted in blue) starts at approximately 0.78V at 0°C and decreases linearly to about 0.55V at 100°C.
2. \( V_A \) (depicted in red) starts at approximately 0.55V at 0°C and increases linearly to about 0.65V at 100°C.
3. \( V_P \) (depicted in yellow) also starts at approximately 0.55V at 0°C and increases linearly to about 0.6V at 100°C.

The three lines intersect at around 70°C, where the voltages of \( V_X \), \( V_A \), and \( V_P \) are approximately equal. The graph has a legend in the top right corner that identifies the colors and corresponding variables. The background of the graph is light pink.
```

**FIGURE 6: The internal voltages of the bandgap core versus** *T***.**

Here is the image describtion:
```
The image is a graph that shows the Power Supply Rejection Ratio (PSRR) in decibels (dB) plotted against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from 10^5 Hz (100,000 Hz) to 10^9 Hz (1,000,000,000 Hz), and the y-axis represents the PSRR, ranging from -60 dB to 20 dB.

There are three curves on the graph, each representing PSRR at different temperatures:
1. The blue curve represents the PSRR at 0°C.
2. The red curve represents the PSRR at 50°C.
3. The yellow curve represents the PSRR at 100°C.

The graph shows that as the frequency increases, the PSRR decreases (becomes less negative) for all three temperatures. At lower frequencies, the PSRR is relatively stable, with the blue curve (0°C) having the highest PSRR, followed by the red curve (50°C), and the yellow curve (100°C) having the lowest PSRR. As the frequency approaches 10^9 Hz, the PSRR for all three temperatures converges and increases sharply.

The grid lines on the graph help to identify specific values of frequency and PSRR more easily. The legend in the graph indicates the color coding for the different temperatures.
```

**FIGURE 7: The PSRR responses of the core for different temperatures.**

The next task is to select the bias current in each branch, the value of *R*1, and the dimensions of *M*1 and *M*2. Anticipating about half a dozen bias currents in the main branches and the op amp(s) in the final design and bearing in mind the 1-mW power budget, we choose | | *I I D D* 1 2 =| |.35 *n* A and hence *R*<sup>1</sup> =2kX. For the PMOS transistors, the channel area must be large enough to minimize mismatch and flicker noise, and the length must be long enough to ensure that channel-length modulation does not limit the supply rejection. Based on these considerations, we select ( / *W L*)1 2, =50 *n*m n /120 m.

Figure 3(a) depicts the preliminary core design. We simulate the circuit while assuming an ideal op amp having a gain of 100. Our objective is twofold: to measure the extreme values of *VX*, *VY*, and *VP* and to quantify the power-supply-rejection ratio (PSRR). In Figure 3(b), *VX* and *VP* are plotted as a function of the temperature. (The high op amp gain guarantees that *V V Y X* . .) These results reveal several points. First, | | *V V P X* - =| | *V V* GS1 1 - DS has a maximum value of about 230 mV, placing *M*1 and *M*2 in saturation. That is, ( ) *W L*/ 1 2, is adequately large. Second, the op amp input stage must operate properly across the common-mode (CM) range of *VX* and *VY* —from around 780 mV to 620 mV. Third, the op amp output must accommodate the variation of *VP* from 550 mV to 640 mV.

Here is the image describtion:
```
The image depicts a schematic diagram of a CMOS (Complementary Metal-Oxide-Semiconductor) circuit. The circuit consists of two main parts: the left side in red and the right side in black.

1. **Left Side (Red) Components:**
   - **Transistors Ma and Mb:** These are PMOS transistors, indicated by the arrow pointing outwards from the source. They are connected in a configuration where their sources are tied to a voltage labeled as ΔV_DD.
   - **Node A:** The gates of Ma and Mb are connected together at a node labeled A.
   - **Connections:** The drain of Ma is connected to the source of Mb, and the drain of Mb is connected to the source of Ma, forming a cross-coupled pair.

2. **Right Side (Black) Components:**
   - **Transistors M1 and M2:** These are NMOS transistors, indicated by the arrow pointing inwards towards the source. They are connected in a configuration where their sources are tied to ground.
   - **Node P:** The gates of M1 and M2 are connected together at a node labeled P.
   - **Connections:** The drain of M1 is connected to the source of M2, and the drain of M2 is connected to the source of M1, forming another cross-coupled pair.

3. **Power Supply:**
   - The circuit is powered by a voltage source labeled V_DD, which is connected to the drains of Ma and Mb on the left side and the sources of M1 and M2 on the right side.

4. **Additional Connections:**
   - There are additional connections labeled ΔV_DD at various points in the circuit, indicating differential voltage inputs or outputs.

Overall, the image shows a differential CMOS circuit with cross-coupled PMOS and NMOS transistors, which is commonly used in applications such as differential amplifiers or sense amplifiers in memory circuits.
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
The image depicts a schematic diagram of a differential amplifier circuit. The circuit consists of several MOSFET transistors, resistors, and a current source. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - There are six MOSFET transistors labeled as Ma, Mb, Mc, Md, Mx, and My.
   - Ma and Mb are connected in a differential pair configuration.
   - Mc and Md are connected to the power supply (V_DD) and act as active loads for the differential pair.
   - Mx and My are connected to the sources of Ma and Mb, respectively, and are part of the current mirror configuration.

2. **Resistors:**
   - Two resistors, Ra and Rb, are connected in series between the drains of Ma and Mb.
   - The values of Ra and Rb are given as 40 kΩ each.

3. **Current Source:**
   - A current source labeled Iss is connected to the common source node of Mx and My, providing a constant current of 50 µA.

4. **Connections:**
   - The gates of Ma and Mb are the input terminals labeled X and Y, respectively.
   - The output of the differential amplifier is taken from the drain of Mb, labeled as "To Node P."
   - The circuit is powered by a supply voltage V_DD.

5. **Dimensions:**
   - The width-to-length ratio (W/L) of the transistors is specified as 50 µm / 120 nm.

Overall, this circuit is a typical differential amplifier with a current mirror load, used for amplifying the difference between two input signals (X and Y) while rejecting common-mode signals.
```

**FIGURE 9: A two-stage op amp for use in the bandgap reference.**

is far short of the desired value, necessitating further design efforts.

#### Op Amp Design

Since the op amp in Figure 3(a) must operate with input CM levels as high as 780 mV, we select an NMOS input stage for it. The simplest implementation is a five-transistor operational transconductance amplifier (OTA), as presented in Figure 5. We assume *W L*/ / =50 *n*m n 120 m for all of the transistors. With a tail current of 50 *μ*A, the op amp provides a gain of about 20, and *MX* and *MY* exhibit a minimum source voltage of 350 mV at *T* =100 Cc , which is sufficient for *I*SS . However, at *T* = 0 Cc , both | | *V*BE and | | *V*TH1,2 take on large values, possibly pushing *MX* into the triode region and lowering the op amp gain. Figure 6 plots *VX*, *VA*, and *VP* versus *T*, demonstrating that *V V X A* keeps *MX* in saturation. Figure 7

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with active loads. The circuit consists of four MOSFET transistors labeled Mc, Ma, Mb, and Md. 

- The transistors Ma and Mb are arranged in a differential pair configuration, with their sources connected together and their gates receiving differential input signals (ΔV_DD).
- The transistors Mc and Md are connected as active loads for the differential pair. Their gates are connected to the same voltage source V_DD.
- The drains of Ma and Mb are connected to the drains of Mc and Md, respectively.
- The sources of Mc and Md are connected to the positive supply voltage V_DD.
- The circuit also includes resistors connected between the sources of Ma and Mb and the common source node of the differential pair.

This configuration is typically used in analog circuits to amplify the difference between two input signals while rejecting any common-mode signals.
```

**FIGURE 10: Paths from** *V***DD to the internal nodes of the two-stage op amp.**

presents how the PSRR responses at *T* = 0 Cc , 50c C, and 100c C illustrate a degradation at low temperatures.

An interesting observation in Figure 7 is that the low-frequency PSRR is around –35 dB at *T* = 0 Cc , whereas (14) would yield 1 0 /( .14*A*1) / -9dB for *A*<sup>1</sup> =20. Why is the performance better than expected? In the analysis leading to (14), we assumed that the op amp must multiply *V V Y X* - by *A*<sup>1</sup> to adjust *VP* and allow it to track *V*DD. However, in the circuit of Figure 5, the OTA provides an additional

Here is the image describtion:
```
The image is a graph that plots Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from 10^5 Hz (100,000 Hz) to 10^9 Hz (1,000,000,000 Hz). The y-axis represents the PSRR, ranging from -60 dB to 20 dB.

There are three different colored lines on the graph, each representing PSRR at different temperatures:
- The blue line represents PSRR at 0°C.
- The red line represents PSRR at 50°C.
- The yellow line represents PSRR at 100°C.

At lower frequencies (around 10^5 Hz), all three lines start at approximately -40 dB. As the frequency increases, the PSRR for all three temperatures remains relatively flat until around 10^7 Hz. Beyond this point, the PSRR begins to increase for all three temperatures, with the blue line (0°C) showing a more pronounced increase compared to the red (50°C) and yellow (100°C) lines. By the time the frequency reaches 10^9 Hz, all three lines converge and show a PSRR close to 20 dB.

The graph indicates that PSRR improves with increasing frequency and that temperature has an impact on the PSRR, with higher temperatures generally showing slightly better PSRR performance at higher frequencies.
```

**FIGURE 11: The PSRR of the core with a two-stage op amp.**

Authorized licensed use limited to: UCLA Library. Downloaded on November 30,2021 at 21:02:47 UTC from IEEE Xplore. Restrictions apply.

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (a) on the left and a graph (b) on the right.

(a) The circuit diagram is a detailed schematic of an electronic circuit. It includes the following components and connections:
- Two PMOS transistors labeled M1 and M2, with their sources connected to V_DD and their drains connected to a common node P.
- A current source providing 35 µA connected to the drain of M1 and another 35 µA current source connected to the drain of M2.
- An operational amplifier A1 with its non-inverting input connected to node X and its inverting input connected to node Y. The output of the operational amplifier is connected to the gate of M1.
- Two NPN bipolar junction transistors Q1 and Q2, with Q1 having a 4x multiplier and Q2 having a 64x multiplier. The emitter of Q1 is connected to ground through a 13 kΩ resistor (R2), and the emitter of Q2 is connected to ground through a 2 kΩ resistor (R1).
- The base of Q1 is connected to node X, and the base of Q2 is connected to node Y.
- A resistor R3 (13 kΩ) is connected between node Y and ground.
- A PMOS transistor M3 with its source connected to V_DD, its gate connected to node P, and its drain connected to a load resistor R_L (5.5 kΩ) and the output node V_out.
- The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.

(b) The graph on the right shows the relationship between the drain current (|I_D2|) in microamperes (µA) and temperature in degrees Celsius (°C). The graph is a plot of |I_D2| versus temperature, showing an increasing trend. The current starts at approximately 93.3 µA at 0°C and increases to about 93.65 µA at 100°C, indicating a positive temperature coefficient.

Overall, the image illustrates a temperature-dependent current source circuit and its performance characteristics as a function of temperature.
```

**FIGURE 12: (a) The bandgap reference with** *R***2 and** *R***3 added and (b) the drain current of** *M***2 versus** *T***.**

Here is the image describtion:
```
The image is a graph that plots voltage (V) against temperature (°C). The x-axis represents temperature, ranging from 0°C to 100°C, while the y-axis represents voltage, ranging from 0.5V to 0.8V. 

There are two lines on the graph:
1. A blue line labeled \( V_Y \) which starts at approximately 0.77V at 0°C and decreases linearly to about 0.58V at 100°C.
2. A red line labeled \( V_{out} \) which starts at approximately 0.6V at 0°C and decreases linearly to about 0.54V at 100°C.

The background of the graph is light pink, and the grid lines are gray, aiding in the readability of the data points. The legend in the top right corner identifies the blue line as \( V_Y \) and the red line as \( V_{out} \).
```

**FIGURE 13: The voltages at node** *Y* **and at the output of the bandgap circuit versus** *T***.**

Here is the image describtion:
```
The image depicts a detailed schematic of an electronic circuit involving operational amplifiers, transistors, resistors, and current sources. Here is a detailed description of the components and their connections:

1. **Operational Amplifiers (Op-Amps)**:
   - **A1**: This op-amp has its inverting input connected to node X and its non-inverting input connected to node Y. The output of A1 is connected to the gate of transistor M1.
   - **A2**: This op-amp has its inverting input connected to node N and its non-inverting input connected to the junction of resistor R3 and the output node V_out. The output of A2 is connected to the gate of transistor M4.

2. **Transistors**:
   - **M1 and M2**: These are NMOS transistors with their sources connected to ground. The drain of M1 is connected to node P, and the drain of M2 is connected to node Y.
   - **M3 and M4**: These are PMOS transistors with their sources connected to the positive supply voltage V_DD. The drain of M3 is connected to node N, and the drain of M4 is connected to the output node V_out.

3. **Current Sources**:
   - Two current sources are shown, each providing a current of 35 µA. One current source is connected to node P, and the other is connected to node Y.

4. **Resistors**:
   - **R1**: 2 kΩ resistor connected between node Y and the emitter of transistor Q2.
   - **R2**: 13 kΩ resistor connected between node X and ground.
   - **R3**: 13 kΩ resistor connected between node N and the output node V_out.
   - **R_L**: 5.5 kΩ load resistor connected between the output node V_out and ground.

5. **Transistors Q1 and Q2**:
   - **Q1**: Connected with its collector to node X, its base to ground, and its emitter to ground through a 4x multiplier.
   - **Q2**: Connected with its collector to node Y, its base to ground, and its emitter to ground through a 64x multiplier.

6. **Dimensions**:
   - The width-to-length ratio (W/L) of the transistors is given as 50 µm / 120 nm.

The circuit appears to be a complex analog design, possibly a part of a larger system such as an amplifier or a current mirror circuit. The use of multiple transistors, resistors, and operational amplifiers suggests it is designed for precise control and amplification of signals.
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
The image is a graph that plots the relationship between temperature (in degrees Celsius) and output voltage (V_out in volts). The x-axis represents the temperature, ranging from 0°C to 100°C, while the y-axis represents the output voltage, ranging from 0.513V to 0.5155V. 

The graph shows a single blue line that starts at approximately 0.513V when the temperature is 0°C and gradually increases as the temperature rises. The line is smooth and slightly curved upwards, indicating a positive correlation between temperature and output voltage. The output voltage reaches about 0.515V at 100°C. The background of the graph is light pink, and the grid lines are grey, providing a clear view of the plotted data.
```

**FIGURE 15: The output voltage of the final design versus** *T***.**

Here is the image describtion:
```
The image is a graph that plots Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from 10^5 Hz (100,000 Hz) to 10^9 Hz (1,000,000,000 Hz), and is displayed on a logarithmic scale. The y-axis represents the PSRR, ranging from -50 dB to 20 dB.

The graph shows a blue line that starts at around -40 dB at 10^5 Hz and remains relatively flat until it reaches approximately 10^7 Hz. After this point, the line begins to rise sharply, indicating a decrease in PSRR as the frequency increases. The line continues to rise and reaches around 0 dB at approximately 10^8 Hz, and then continues to increase steeply, reaching around 20 dB at 10^9 Hz.

The background of the graph is light pink, and the grid lines are in gray, providing a clear reference for the plotted data. The overall trend depicted by the graph indicates that the PSRR decreases as the frequency increases, particularly after the 10^7 Hz mark.
```

**FIGURE 16: The PSRR of the final design.**

If the output noise is unacceptably high for a given application, we can pursue three methods to reduce it. First, to lower the flicker noise, the channel areas of *M*1–*M*3 can be increased while maintaining their *W L*/ ratio. Second, the widths and bias currents of *M*1–*M*3 and the areas of *Q*1 and *Q*2 can be scaled up, and the values of all of the resistors can be scaled down by the same factor to reduce the output thermal noise. This remedy trades noise for area and power. Third, the output lowpass filter can incorporate larger capacitors, but at the cost of area.

The op amp offset, *V*OS, arises primarily from the first stage in Figure 9. Writing the threshold mismatch as T*V A* TH = VTH / *WL* and assuming

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b).

Part (a) is a schematic diagram of an electronic circuit. The circuit includes a MOSFET transistor labeled M4, with its source connected to ground. The drain of M4 is connected to a 5.5 kΩ resistor, which is also connected to the output node labeled Vout. The output node Vout is connected to two 1 pF capacitors, one to ground and the other to the input node. The input node is connected to another 5.5 kΩ resistor, which is also connected to ground. The gate of the MOSFET M4 is not explicitly shown to be connected to any other component in this diagram.

Part (b) is a graph plotting Power Supply Rejection Ratio (PSRR) in decibels (dB) against Frequency in Hertz (Hz). The x-axis represents the frequency, ranging from 10^5 Hz to 10^9 Hz, and the y-axis represents the PSRR, ranging from -54 dB to -44 dB. The graph shows a curve that starts at around -44 dB at 10^5 Hz, dips to about -52 dB around 10^8 Hz, and then rises slightly towards -50 dB as it approaches 10^9 Hz. The curve indicates how the PSRR varies with frequency for the given circuit.
```

**FIGURE 17: (a) The addition of a low-pass filter and (b) the resulting PSRR.**

Here is the image describtion:
```
The image is a graph that plots Output Noise (in nV/√Hz) against Frequency (in Hz). The x-axis represents the frequency on a logarithmic scale ranging from 10^4 Hz (10,000 Hz) to 10^9 Hz (1,000,000,000 Hz). The y-axis represents the output noise, also on a logarithmic scale, ranging from 0 to 700 nV/√Hz.

The graph shows a curve that starts at around 600 nV/√Hz at 10^4 Hz and decreases sharply as the frequency increases. The curve continues to decline until it reaches a minimum value of around 100 nV/√Hz between 10^5 Hz and 10^6 Hz. After this point, the curve remains relatively flat, maintaining a noise level close to 100 nV/√Hz up to around 10^8 Hz. Beyond this frequency, the curve starts to rise slightly, indicating an increase in output noise as the frequency approaches 10^9 Hz.

The background of the graph is light pink, and the grid lines are dashed, aiding in the visualization of the data points. The overall trend depicted by the graph is a decrease in output noise with increasing frequency up to a certain point, followed by a slight increase at very high frequencies.
```

**FIGURE 18: The output noise voltage of the bandgap reference.**

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), both of which appear to be related to electronic circuits involving transistors and other components.

**Diagram (a):**
- The circuit is powered by a voltage source labeled "1 V" at the top left, which can switch between 0 and 1 V.
- A capacitor labeled \( C_S \) is connected to the voltage source.
- The gate of a transistor labeled \( M_S \) is connected to the junction of \( C_S \) and a resistor labeled \( R_S \), which is connected to ground.
- The source of \( M_S \) is connected to ground.
- The drain of \( M_S \) is connected to the source of another transistor labeled \( M_1 \).
- The drain of \( M_1 \) is connected to a node labeled \( P \).
- The node \( P \) is connected to the source of another transistor labeled \( M_2 \).
- The drain of \( M_2 \) is connected to a voltage supply labeled \( V_{DD} \).

**Diagram (b):**
- The circuit is also powered by a voltage supply labeled \( V_{DD} \) at the top.
- The transistors \( M_1 \) and \( M_2 \) are connected in the same configuration as in diagram (a), with a node \( P \) between them.
- The source of \( M_1 \) is connected to the drain of a transistor labeled \( M_S \), whose source is connected to ground.
- The gate of \( M_S \) is connected to the output of an operational amplifier labeled \( A_3 \).
- The non-inverting input of \( A_3 \) is connected to a node labeled "From \( V_{out} \)".
- The inverting input of \( A_3 \) is connected to a reference voltage labeled \( V_r \).
- The output of \( A_3 \) is connected to the input of an inverter, whose output is connected to the gate of \( M_S \).

Both diagrams involve a pair of transistors \( M_1 \) and \( M_2 \) with a common node \( P \), and a transistor \( M_S \) whose gate is controlled by different means in each diagram. Diagram (a) uses a capacitor and resistor network, while diagram (b) uses an operational amplifier and inverter to control the gate of \( M_S \).
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
The image consists of two graphs, labeled (a) and (b), each depicting voltage (V) versus time (ns). Both graphs have a common x-axis representing time in nanoseconds (ns) ranging from 0 to 1,000 ns, and a common y-axis representing voltage in volts (V) ranging from 0 to 1 V.

In both graphs, three voltage curves are plotted:
1. \( V_{DD} \) (blue line)
2. \( V_P \) (red line)
3. \( V_{out} \) (yellow line)

Graph (a):
- The blue line (\( V_{DD} \)) shows a linear increase from 0 V at 0 ns to 1 V at 1,000 ns.
- The red line (\( V_P \)) starts at 0 V and increases linearly, but at a slower rate than \( V_{DD} \), reaching approximately 0.8 V at around 1,000 ns.
- The yellow line (\( V_{out} \)) remains at 0 V until around 800 ns, after which it rapidly spikes to approximately 1 V and then quickly drops back to 0 V.

Graph (b):
- The blue line (\( V_{DD} \)) again shows a linear increase from 0 V at 0 ns to 1 V at 1,000 ns.
- The red line (\( V_P \)) starts at 0 V and increases non-linearly, with several fluctuations, reaching approximately 0.6 V at around 1,000 ns.
- The yellow line (\( V_{out} \)) also starts at 0 V and follows a similar non-linear pattern with fluctuations, reaching approximately 0.4 V at around 1,000 ns.

Both graphs are set against a light pink background, and a legend at the bottom center indicates the color coding for the three voltage curves: \( V_{DD} \) (blue), \( V_P \) (red), and \( V_{out} \) (yellow).
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