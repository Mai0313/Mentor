# CHAPTER

Razavi-3930640 book December 17, 201517:21 509

Here is the image describtion:
```
The image shows the number "12" displayed in white on a dark gray background. The font used for the number is simple and sans-serif, with clean and straight lines. The number is centered within the image, and the overall design is minimalistic with no additional elements or decorations.
```

# *Bandgap References*

Analog circuits incorporate voltage and current references extensively. Such references are dc quantities that exhibit little dependence on supply and process parameters and a *well-defined* dependence on the temperature. For example, the bias current of a differential pair must be generated according to a reference, for it affects the voltage gain and noise of the circuit. We have also seen the need for precise voltages to define common-mode levels in op amps. Moreover, in systems such as A/D and D/A converters, a reference is required to define the input or output full-scale range.

In this chapter, we deal with the design of reference generators in CMOS technology, focusing on well-established "bandgap" techniques. First, we study supply-independent biasing and the problem of start-up. Next, we describe temperature-independent references and examine issues such as the effect of offset voltages. Finally, we present constant-*Gm* biasing and study an example of state-of-the-art bandgap references.

## **12.1 General Considerations**

As mentioned above, the objective of reference generation is to establish a dc voltage or current that is independent of the supply and process and has a well-defined behavior with temperature. In most applications, the required temperature dependence assumes one of three forms: (1) proportional to absolute temperature (PTAT); (2) constant-*Gm* behavior, i.e., such that the transconductance of certain transistors remains constant; (3) temperature independent. We can therefore divide the task into two design problems: supply-independent biasing and definition of the temperature variation.

In addition to supply, process, and temperature variability, several other parameters of reference generators may be critical as well. These include output impedance, output noise, and power dissipation. We return to these issues later in this chapter.

# **12.2 Supply-Independent Biasing**

Our use of bias currents and current mirrors in previous chapters has implicitly assumed that a "golden" reference current is available. As shown in Fig. 12.1(a), if *IREF* does not vary with *VDD*, and channellength modulation of *M*<sup>2</sup> and *M*<sup>3</sup> is neglected, then *ID*<sup>2</sup> and *ID*<sup>3</sup> remain independent of the supply voltage. The question then is—How do we generate *IREF*?

Here is the image describtion:
```
The image shows two different circuit diagrams, labeled (a) and (b), which appear to be related to current mirror configurations using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).

### Circuit (a):
1. **Components**:
   - **Current Source (I_REF)**: Provides a reference current.
   - **MOSFETs (M1, M2, M3)**: Three n-channel MOSFETs are used.
   - **Voltage Source (V_DD)**: Provides the supply voltage.

2. **Connections**:
   - The drain of M1 is connected to the current source I_REF and the supply voltage V_DD.
   - The gate of M1 is connected to its drain, forming a diode-connected MOSFET.
   - The gate of M1 is also connected to the gates of M2 and M3, ensuring that all three MOSFETs have the same gate-source voltage (V_GS).
   - The sources of M1, M2, and M3 are connected to ground.
   - The drains of M2 and M3 are labeled with currents I_D2 and I_D3, respectively, indicating the currents flowing through these transistors.

### Circuit (b):
1. **Components**:
   - **Current Source (I_REF)**: Provides a reference current.
   - **Resistor (R1)**: Connected between the supply voltage V_DD and the drain of M1.
   - **MOSFETs (M1, M2)**: Two n-channel MOSFETs are used.
   - **Voltage Source (V_DD)**: Provides the supply voltage.

2. **Connections**:
   - The drain of M1 is connected to one end of the resistor R1, with the other end of R1 connected to the supply voltage V_DD.
   - The gate of M1 is connected to its drain, forming a diode-connected MOSFET.
   - The gate of M1 is also connected to the gate of M2, ensuring that both MOSFETs have the same gate-source voltage (V_GS).
   - The sources of M1 and M2 are connected to ground.
   - The drain of M2 is labeled with the current I_out, indicating the output current flowing through this transistor.

### Analysis:
- **Circuit (a)**: This is a basic current mirror configuration where the reference current I_REF sets the gate-source voltage for M1, which is mirrored to M2 and M3. The currents I_D2 and I_D3 are ideally equal to I_REF, assuming identical MOSFETs and neglecting channel length modulation.
- **Circuit (b)**: This is another current mirror configuration, but with a resistor R1 added to the drain of M1. The resistor helps to set the voltage at the drain of M1, which in turn sets the gate-source voltage for both M1 and M2. The output current I_out through M2 is ideally equal to the reference current I_REF, assuming identical MOSFETs and neglecting channel length modulation.

Both circuits are used to replicate a reference current in multiple branches, which is a common technique in analog integrated circuit design.
```

**Figure 12.1** Current mirror biasing using (a) an ideal current source and (b) a resistor.

As an approximation of a current source, we tie a resistor from *VDD* to the gate of *M*<sup>1</sup> [Fig. 12.1(b)]. However, the output current of this circuit is quite sensitive to *VDD*:

$$
\Delta I\_{\rm out} = \frac{\Delta V\_{DD}}{R\_1 + 1/\text{g}\_{m1}} \cdot \frac{(W/L)\_2}{(W/L)\_1} \tag{12.1}
$$

In order to arrive at a less sensitive solution, we postulate that the circuit must bias *itself*, i.e., *IREF* must be somehow derived from *Iout* . The idea is that if *Iout* is to be ultimately independent of *VDD*, then *IREF* can be a replica of *Iout* . Figure 12.2 illustrates an implementation where *M*<sup>3</sup> and *M*<sup>4</sup> copy *Iout* , thereby defining *IREF* . In essence, *IREF* is "bootstrapped" to *Iout* . With the sizes chosen here, we have *Iout* = *K IREF* if channel-length modulation is neglected. Note that, since each diode-connected device feeds from a current source, *Iout* and *IREF* are relatively independent of *VDD*.

Here is the image describtion:
```
The image depicts a simple electronic circuit designed to establish supply-independent currents. The circuit consists of four MOSFET transistors labeled M1, M2, M3, and M4. 

- M1 and M2 are NMOS transistors, while M3 and M4 are PMOS transistors.
- The transistors are arranged in a specific configuration to achieve the desired current characteristics.
- The width-to-length ratios (W/L) of the transistors are indicated next to each transistor. For M1 and M2, the ratio is (W/L)N, and for M3 and M4, the ratio is (W/L)P.
- Additionally, the width-to-length ratios for M2 and M3 are scaled by a factor of K, denoted as K(W/L)N and K(W/L)P, respectively.
- The circuit is powered by a supply voltage V_DD.
- I_REF is the reference current flowing through M1 and M4.
- I_out is the output current flowing through M2 and M3.

The circuit is designed to ensure that the currents are independent of the supply voltage, making it useful for applications requiring stable current sources.
```

supply-independent currents.

Since *Iout* and *IREF* in Fig. 12.2 display little dependence on *VDD*, their magnitude is set by other parameters. How do we calculate these currents? Interestingly, if *M*1–*M*<sup>4</sup> operate in saturation and λ ≈ 0, then the circuit is governed by only one equation, *Iout* = *K IREF* , and hence can support *any* current level! For example, if we initially force *IREF* to be 10 *µ*A, the resulting *Iout* of *K* × 10 *µ*A "circulates" around the loop, sustaining these current levels in the left and right branches indefinitely.

To uniquely define the currents, we add another constraint to the circuit, e.g., as shown in Fig. 12.3(a). Here, resistor *RS* decreases the current of *M*<sup>2</sup> while the PMOS devices require that *Iout* = *IREF* because they have identical dimensions and thresholds. We can write *VG S*<sup>1</sup> = *VG S*<sup>2</sup> + *ID*2*RS*, or

$$\sqrt{\frac{2I\_{\text{out}}}{\mu\_{n}\text{C}\_{ox}(W/L)\_{N}}} + V\_{TH1} = \sqrt{\frac{2I\_{\text{out}}}{\mu\_{n}\text{C}\_{ox}K(W/L)\_{N}}} + V\_{TH2} + I\_{\text{out}}R\_{S} \tag{12.2}$$

Neglecting body effect, we have

$$\sqrt{\frac{2I\_{\text{out}}}{\mu\_n C\_{ox}(W/L)\_N}} \left(1 - \frac{1}{\sqrt{K}}\right) = I\_{\text{out}} R\_S \tag{12.3}$$

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b). Both circuits are current mirrors, which are used to copy a current from one active device to another, maintaining a constant current.

### Circuit (a):
1. **Transistors:**
   - There are four MOSFET transistors labeled \( M_1, M_2, M_3, \) and \( M_4 \).
   - \( M_1 \) and \( M_2 \) are NMOS transistors, while \( M_3 \) and \( M_4 \) are PMOS transistors.
   - The width-to-length ratios of the transistors are indicated as \( \left(\frac{W}{L}\right)_N \) for NMOS and \( \left(\frac{W}{L}\right)_P \) for PMOS.

2. **Connections:**
   - The source of \( M_1 \) is connected to a reference current source \( I_{REF} \).
   - The drain of \( M_1 \) is connected to the gate of \( M_2 \) and the source of \( M_3 \).
   - The source of \( M_2 \) is connected to a resistor \( R_S \) which is grounded.
   - The drain of \( M_2 \) is connected to the output current \( I_{out} \).
   - The gate of \( M_3 \) is connected to the gate of \( M_4 \).
   - The source of \( M_4 \) is connected to \( V_{DD} \), the positive supply voltage.
   - The drain of \( M_4 \) is connected to the drain of \( M_3 \).

3. **Current Flow:**
   - The reference current \( I_{REF} \) flows through \( M_1 \).
   - The current through \( M_2 \) is mirrored to \( M_3 \) and \( M_4 \), producing the output current \( I_{out} \).

### Circuit (b):
1. **Transistors:**
   - Similar to circuit (a), there are four MOSFET transistors labeled \( M_1, M_2, M_3, \) and \( M_4 \).
   - \( M_1 \) and \( M_2 \) are NMOS transistors, while \( M_3 \) and \( M_4 \) are PMOS transistors.
   - The width-to-length ratios of the transistors are indicated as \( \left(\frac{W}{L}\right)_N \) for NMOS and \( \left(\frac{W}{L}\right)_P \) for PMOS.

2. **Connections:**
   - The source of \( M_1 \) is connected to a reference current source \( I_{REF} \).
   - The drain of \( M_1 \) is connected to the gate of \( M_2 \) and the source of \( M_3 \).
   - The source of \( M_2 \) is grounded.
   - The drain of \( M_2 \) is connected to the output current \( I_{out} \).
   - The gate of \( M_3 \) is connected to the gate of \( M_4 \).
   - The source of \( M_4 \) is connected to \( V_{DD} \), the positive supply voltage.
   - The drain of \( M_4 \) is connected to the drain of \( M_3 \) and a resistor \( R_S \) which is also connected to \( V_{DD} \).

3. **Current Flow:**
   - The reference current \( I_{REF} \) flows through \( M_1 \).
   - The current through \( M_2 \) is mirrored to \( M_3 \) and \( M_4 \), producing the output current \( I_{out} \).

### Differences:
- In circuit (a), the resistor \( R_S \) is connected to the source of \( M_2 \) and grounded.
- In circuit (b), the resistor \( R_S \) is connected to the drain of \( M_3 \) and \( V_{DD} \).

Both circuits are designed to mirror the reference current \( I_{REF} \) to the output current \( I_{out} \) using MOSFET transistors. The placement of the resistor \( R_S \) differentiates the two configurations.
```

**Figure 12.3** (a) Addition of *RS* to define the currents; (b) alternative implementation eliminating body effect.

and hence

$$I\_{\rm out} = \frac{2}{\mu\_n C\_{\rm ox} (W/L)\_N} \cdot \frac{1}{R\_S^2} \left(1 - \frac{1}{\sqrt{K}}\right)^2 \tag{12.4}$$

As expected, the current is independent of the supply voltage (but still a function of process and temperature).

The assumption *VT H*<sup>1</sup> = *VT H*<sup>2</sup> introduces some error in the foregoing calculations because the sources of *M*<sup>1</sup> and *M*<sup>2</sup> are at different voltages. Shown in Fig. 12.3(b) is to place the resistor in the source of *M*<sup>3</sup> while eliminating body effect by tying the source and bulk of each PMOS transistor. Another solution is described in Problem 12.1.

The circuits of Figs. 12.3(a) and (b) exhibit little supply dependence if channel-length modulation is negligible. For this reason, relatively long channels are used for all of the transistors in the circuit. This also helps reduce their flicker noise.

#### ▲**Example 12.1**

Assuming λ =% 0 in Fig. 12.3(a), estimate the change in *Iout* for a small change !*VDD* in the supply voltage.

## **Solution**

Simplifying the circuit as depicted in Fig. 12.4, where *R*<sup>1</sup> = *rO*<sup>1</sup>&*(*1*/gm*1*)* and *R*<sup>3</sup> = *rO*<sup>3</sup>&*(*1*/gm*3*)*, we calculate the "gain" from *VDD* to *Iout* . The small-signal gate-source voltage of *M*<sup>4</sup> equals −*Iout R*3, and the current through *rO*<sup>4</sup> is *(VDD* − *VX )/rO*4. Thus,

$$\frac{V\_{DD} - V\_X}{r\_{O4}} + I\_{out}R\_3g\_{m4} = \frac{V\_X}{R\_1} \tag{12.5}$$

Here is the image describtion:
```
The image depicts a common-source amplifier circuit with a current mirror load. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a DC voltage source labeled \( V_{DD} \), which is connected to the top rail of the circuit.

2. **Transistor M4**: 
   - This is an NMOS transistor with its drain connected to \( V_{DD} \) through a small-signal output resistance \( r_{o4} \).
   - The source of M4 is connected to node X.
   - The gate of M4 is connected to the drain of M4, forming a diode-connected configuration.

3. **Resistor R1**: 
   - This resistor is connected between node X and ground.

4. **Transistor M2**: 
   - This is another NMOS transistor with its source connected to ground through a source degeneration resistor \( R_S \).
   - The drain of M2 is connected to the output node through a small-signal output resistance \( r_{o2} \).
   - The gate of M2 is connected to node X.

5. **Resistor R3**: 
   - This resistor is connected between the output node and \( V_{DD} \).

6. **Output Node**: 
   - The output current \( I_{out} \) is taken from the drain of M2, which is also connected to the drain of M4 through \( r_{o2} \) and \( R_3 \).

In summary, the circuit is a common-source amplifier with a current mirror load. The current mirror is formed by transistors M4 and M2, with M4 acting as the reference transistor and M2 as the output transistor. The resistor \( R_1 \) sets the bias current for the current mirror, and \( R_S \) provides source degeneration for M2, which helps in stabilizing the operating point and improving linearity. The output is taken from the drain of M2, where the amplified signal can be observed.
```

▲

If we denote the equivalent transconductance of *M*<sup>2</sup> and *RS* by *Gm*<sup>2</sup> = *Iout /VX* , then

$$\frac{I\_{out}}{V\_{DD}} = \frac{1}{r\_{O4}} \left[ \frac{1}{G\_{m2}(r\_{O4} \| R\_1)} - g\_{m4} R\_3 \right]^{-1} \tag{12.6}$$

Note from Chapter 3 that

Razavi-3930640 book December 17, 201517:21 512

$$G\_{m2} = \frac{g\_{m2}r\_{O2}}{R\_S + r\_{O2} + (g\_{m2} + g\_{mb2})R\_Sr\_{O2}}\tag{12.7}$$

Interestingly, the sensitivity vanishes if *rO*<sup>4</sup> = ∞.

In some applications, the sensitivity given by (12.6) is prohibitively large. Also, owing to various capacitive paths, the supply sensitivity of the circuit rises at high frequencies. For these reasons, the supply voltage of the core is often derived from a locally-generated, less sensitive voltage. We return to this point in Sec. 12.8.

An important issue in supply-independent biasing is the existence of "degenerate" bias points. In the circuit of Fig. 12.3(a), for example, if all of the transistors carry zero current when the supply is turned on, they may remain off indefinitely because the loop can support a zero current in both branches. This condition is not predicted by (12.4) because in manipulating (12.3), we divided both sides by <sup>√</sup>*Iout* , tacitly assuming that *Iout* =% 0. In other words, the circuit can settle in one of *two* different operating conditions.

Called the "start-up" problem, the above issue is resolved by adding a mechanism that drives the circuit out of the degenerate bias point when the supply is turned on. Shown in Fig. 12.5(a) is a simple example, where the diode-connected device *M*<sup>5</sup> provides a current path from *VDD* through *M*<sup>3</sup> and *M*<sup>1</sup> to ground upon start-up. Thus, *M*<sup>3</sup> and *M*1, and hence *M*<sup>2</sup> and *M*4, cannot remain off. Of course, this technique is practical only if *VT H*<sup>1</sup> + *VT H*<sup>5</sup> + |*VT H*3| *< VDD* and *VG S*<sup>1</sup> + *VT H*<sup>5</sup> + |*VG S*3| *> VDD*, the latter to ensure that *M*<sup>5</sup> remains off after start-up. Another start-up circuit is analyzed in Problem 12.2.

The problem of start-up generally requires careful analysis and simulation. The supply voltage must be ramped from zero in a dc sweep simulation (such that parasitic capacitances do not cause false start-up) as well as in a transient simulation and the behavior of the circuit examined for each supply voltage. Figure 12.5(b) depicts an example of the observed behavior in the presence of the start-up circuit. In complex implementations, more than one degenerate point may exist.

Here is the image describtion:
```
The image consists of two parts: a circuit diagram (labeled as (a)) and a graph (labeled as (b)).

### Part (a): Circuit Diagram
The circuit diagram features a configuration of five MOSFET transistors and a resistor. Here are the details:

1. **Transistors:**
   - **M1 and M2:** These are the two MOSFETs at the bottom of the circuit. M1 has its source connected to ground, and M2 has its source connected to a resistor \( R_S \) which is grounded.
   - **M3 and M4:** These MOSFETs are at the top of the circuit. Both have their drains connected to \( V_{DD} \) (the positive supply voltage). The source of M3 is connected to the drain of M2, and the source of M4 is connected to the drain of M1.
   - **M5:** This MOSFET is in the middle of the circuit. Its gate is connected to the gate of M1, and its source is connected to the source of M1. The drain of M5 is connected to the gate of M2 and the source of M3.

2. **Resistor \( R_S \):**
   - This resistor is connected between the source of M2 and ground.

### Part (b): Graph
The graph plots \( I_{D2} \) (the drain current of M2) on the vertical axis against \( V_{DD} \) (the supply voltage) on the horizontal axis. The curve starts at the origin and rises steeply before leveling off, indicating the behavior of the drain current as the supply voltage increases.

- **Degenerate Point:** This point is marked on the graph where the curve starts to rise from the origin. It represents a critical point in the operation of the circuit.

### Summary
The image illustrates a specific MOSFET circuit configuration and its corresponding current-voltage characteristic. The circuit diagram shows the interconnections of five MOSFETs and a resistor, while the graph depicts how the drain current \( I_{D2} \) varies with the supply voltage \( V_{DD} \), highlighting a degenerate point where the current begins to increase.
```

**Figure 12.5** (a) Addition of start-up device to the circuit of Fig. 12.3(a), and (b) illustration of degenerate point.

# **12.3 Temperature-Independent References**

Reference voltages or currents that exhibit little dependence on temperature prove essential in many analog circuits. It is interesting to note that, since most process parameters vary with temperature, if a reference is temperature-independent, then it is usually process-independent as well.

How do we generate a quantity that remains constant with temperature? We postulate that if two quantities having opposite temperature coefficients (TCs) are added with proper weighting, the result displays a zero TC. For example, for two voltages *V*<sup>1</sup> and *V*<sup>2</sup> that vary in opposite directions with temperature, we choose α<sup>1</sup> and α<sup>2</sup> such that α1∂*V*1*/*∂*T* + α2∂*V*2*/*∂*T* = 0, obtaining a reference voltage, *VREF* = α1*V*<sup>1</sup> + α2*V*2, with zero TC.

We must now identify two voltages that have positive and negative TCs. Among various device parameters in semiconductor technologies, the characteristics of bipolar transistors have proven the most reproducible and well-defined quantities that can provide positive and negative TCs. Even though many parameters of MOS devices have been considered for the task of reference generation [1, 2], bipolar operation still forms the core of such circuits.

## **12.3.1 Negative-TC Voltage**

The base-emitter voltage of bipolar transistors or, more generally, the forward voltage of a *pn*-junction diode exhibits a negative TC. We first obtain the expression for the TC in terms of readily-available quantities.

For a bipolar device, we can write *IC* = *IS* exp*(VB E /VT )*, where *VT* = *kT/q*. The saturation current *IS* is proportional to *µkTn*<sup>2</sup> *<sup>i</sup>* , where *µ* denotes the mobility of minority carriers and *ni* is the intrinsic carrier concentration of silicon. The temperature dependence of these quantities is represented as *<sup>µ</sup>* <sup>∝</sup> *<sup>µ</sup>*0*<sup>T</sup> <sup>m</sup>*, where *<sup>m</sup>* ≈ −3*/*2, and *<sup>n</sup>*<sup>2</sup> *<sup>i</sup>* <sup>∝</sup> *<sup>T</sup>* <sup>3</sup> exp[−*Eg/(kT )*], where *Eg* <sup>≈</sup> <sup>1</sup>*.*12 eV is the bandgap energy of silicon. Thus,

$$I\_S = bT^{4+m} \exp\frac{-E\_g}{kT} \tag{12.8}$$

where *b* is a proportionality factor. Writing *VB E* = *VT* ln*(IC/IS)*, we can now compute the TC of the base-emitter voltage. In taking the derivative of *VB E* with respect to *T* , we must know the behavior of *IC* as a function of the temperature. To simplify the analysis, we assume for now that *IC* is held *constant*. Thus,

$$\frac{\partial V\_{BE}}{\partial T} = \frac{\partial V\_T}{\partial T} \ln \frac{I\_C}{I\_S} - \frac{V\_T}{I\_S} \frac{\partial I\_S}{\partial T} \tag{12.9}$$

From (12.8), we have

$$\frac{\partial I\_S}{\partial T} = b(4+m)T^{3+m} \exp\frac{-E\_\text{g}}{kT} + bT^{4+m} \left(\exp\frac{-E\_\text{g}}{kT}\right) \left(\frac{E\_\text{g}}{kT^2}\right) \tag{12.10}$$

Therefore,

$$\frac{V\_T}{I\_S} \frac{\partial I\_S}{\partial T} = (4+m)\frac{V\_T}{T} + \frac{E\_g}{kT^2} V\_T \tag{12.11}$$

With the aid of (12.9) and (12.11), we can write

$$\frac{\partial V\_{BE}}{\partial T} = \frac{V\_T}{T} \ln \frac{I\_C}{I\_S} - (4+m)\frac{V\_T}{T} - \frac{E\_g}{kT^2} V\_T \tag{12.12}$$

$$t = \frac{V\_{BE} - (4+m)V\_T - E\_g/q}{T} \tag{12.13}$$

Equation (12.13) gives the temperature coefficient of the base-emitter voltage at a given temperature *T* , revealing dependence on the magnitude of *VB E* itself. With *VB E* ≈ 750 mV and *T* = 300 K, we have ∂*VB E /*∂*T* ≈ −1*.*5 mV/K.

In old bipolar technologies, where *IC/IS* was relatively small (because the transistors were large), *VB E* ≈ 700 mV and ∂*VB E /*∂*T* ≈ −1*.*9 mV/K at room temperature. Modern bipolar transistors typically operate at much higher current densities, exhibiting *VB E* ≈ 800 mV and hence ∂*VB E /*∂*T* ≈ −1*.*5 mV/K at *T* = 300 K.

From (12.13), we note that the temperature coefficient of *VB E* itself depends on the temperature, creating error in constant reference generation if the positive-TC quantity exhibits a *constant* temperature coefficient.

Here is the image describtion:
```
The image depicts a differential amplifier circuit using bipolar junction transistors (BJTs). Here is a detailed description of the circuit:

1. **Power Supply (V_DD)**: The circuit is powered by a DC voltage source labeled \( V_{DD} \) at the top of the diagram.

2. **Current Sources**: There are two current sources in the circuit:
   - The left current source provides a current of \( nI_0 \).
   - The right current source provides a current of \( I_0 \).

3. **Transistors (Q1 and Q2)**: The circuit includes two NPN bipolar junction transistors:
   - \( Q_1 \) is on the left side.
   - \( Q_2 \) is on the right side.

4. **Connections**:
   - The collector of \( Q_1 \) is connected to the current source providing \( nI_0 \).
   - The collector of \( Q_2 \) is connected to the current source providing \( I_0 \).
   - The emitters of both \( Q_1 \) and \( Q_2 \) are connected to the ground.

5. **Base Voltages**:
   - The base of \( Q_1 \) is connected to a node labeled with a positive sign (+).
   - The base of \( Q_2 \) is connected to a node labeled with a negative sign (-).

6. **Voltage Difference (\( \Delta V_{BE} \))**: The voltage difference between the bases of \( Q_1 \) and \( Q_2 \) is denoted as \( \Delta V_{BE} \).

In summary, this is a differential amplifier circuit where the difference in base-emitter voltages (\( \Delta V_{BE} \)) of the transistors \( Q_1 \) and \( Q_2 \) controls the differential output. The current sources ensure that the transistors operate in their active regions, and the circuit amplifies the difference between the input signals applied to the bases of \( Q_1 \) and \( Q_2 \).
```

**Figure 12.6** Generation of PTAT voltage.

## **12.3.2 Positive-TC Voltage**

It was recognized in 1964 [3] that if two bipolar transistors operate at unequal current densities,<sup>1</sup> then the *difference* between their base-emitter voltages is directly proportional to the absolute temperature. For example, as shown in Fig. 12.6, if two identical transistors (*IS*<sup>1</sup> = *IS*2) are biased at collector currents of *n I*<sup>0</sup> and *I*<sup>0</sup> and their base currents are negligible, then

$$
\Delta V\_{BE} = V\_{BE1} - V\_{BE2} \tag{12.14}
$$

$$I = V\_T \ln \frac{nI\_0}{I\_{S1}} - V\_T \ln \frac{I\_0}{I\_{S2}} \tag{12.15}$$

$$l = V\_T \ln n \tag{12.16}$$

Thus, the *VB E* difference exhibits a positive temperature coefficient:

$$\frac{\partial \Delta V\_{BE}}{\partial T} = \frac{k}{q} \ln n \tag{12.17}$$

▲

Interestingly, this TC is independent of the temperature or behavior of the collector currents.2

#### ▲**Example 12.2**

How must *n* be chosen to yield a TC of +1*.*5 mV/K so as to cancel the TC of the base-emitter voltage at *T* = 300 K?

#### **Solution**

We choose *n* so that *(k/q)*ln *n* = 1*.*5 mV/K. Since *k/q* = *VT /T* = 0*.*087 mV/K, we have ln *n* ≈ 17*.*2 and hence *<sup>n</sup>* <sup>=</sup> <sup>2</sup>*.*<sup>95</sup> <sup>×</sup> <sup>10</sup>7!! We must therefore modify the circuit to avoid such a large disparity between the two currents.

<sup>1</sup>Current density is defined as the ratio of the collector current, *IC* , and the saturation current, *IS* .

<sup>2</sup>Nonidealities in the characteristics of bipolar transistors introduce a small temperature dependence in this TC.

#### ▲**Example 12.3**

Razavi-3930640 book December 17, 201517:21 515

Calculate !*VB E* in the circuit of Fig. 12.7, where *Q*<sup>2</sup> is formed as the parallel combination of *m* units, each identical to *Q*1.

Here is the image describtion:
```
The image depicts a circuit diagram featuring two bipolar junction transistors (BJTs), labeled Q1 and Q2. The circuit is designed to illustrate a current mirror or a differential pair configuration. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a voltage source labeled V_DD, which is connected to the top of the diagram.

2. **Current Sources**:
   - There are two current sources in the circuit. The left current source is labeled as \( nI_0 \), where \( n \) is a multiplier factor, and it is connected to the collector of transistor Q1.
   - The right current source is labeled as \( I_0 \) and is connected to the collector of transistor Q2.

3. **Transistors (Q1 and Q2)**:
   - **Q1**: The left transistor, Q1, has its collector connected to the current source \( nI_0 \) and its emitter connected to ground through a current \( I_S \).
   - **Q2**: The right transistor, Q2, has its collector connected to the current source \( I_0 \) and its emitter connected to ground through a current \( mI_S \), where \( m \) is another multiplier factor.

4. **Base-Emitter Voltage Difference (\( \Delta V_{BE} \))**:
   - The bases of Q1 and Q2 are connected together, and there is a voltage difference \( \Delta V_{BE} \) between the base-emitter junctions of Q1 and Q2. This voltage difference is indicated by the \( + \) and \( - \) signs near the bases of Q1 and Q2, respectively.

5. **Ground Connections**:
   - The emitters of both Q1 and Q2 are connected to ground through their respective currents \( I_S \) and \( mI_S \).

6. **Current Flow**:
   - The current \( I_S \) flows from the emitter of Q1 to ground.
   - The current \( mI_S \) flows from the emitter of Q2 to ground.

The circuit likely functions as a current mirror or a differential amplifier, where the current through Q1 is mirrored or compared to the current through Q2, with the factors \( n \) and \( m \) determining the scaling of the currents. The voltage difference \( \Delta V_{BE} \) between the base-emitter junctions of Q1 and Q2 plays a crucial role in the operation of the circuit.
```

#### **Solution**

Neglecting base currents, we can write

$$
\Delta V\_{BE} = V\_T \ln \frac{nI\_0}{I\_S} - V\_T \ln \frac{I\_0}{mI\_S} \tag{12.18}
$$

$$
\lambda = Vr \ln(nm) \tag{12.19}
$$

The temperature coefficient is therefore equal to *(k/q)*ln*(nm)*. In this circuit, the two transistors' current densities differ by a factor of *nm*.

## **12.3.3 Bandgap Reference**

With the negative- and positive-TC voltages obtained above, we can now develop a reference that has a nominally zero temperature coefficient. We write *VREF* = α1*VB E* + α2*(VT* ln *n)*, where *VT* ln *n* is the difference between the base-emitter voltages of the two bipolar transistors operating at different current densities. How do we choose α<sup>1</sup> and α2? Since at room temperature, ∂*VB E /*∂*T* ≈ −1*.*5 mV/K whereas ∂*VT /*∂*T* ≈ +0*.*087 mV/K, we may set α<sup>1</sup> = 1 and choose α<sup>2</sup> ln *n* such that*(*α<sup>2</sup> ln *n)(*0*.*087 mV*/*K*)* = 1*.*5 mV/K. That is, α<sup>2</sup> ln *n* ≈ 17*.*2, indicating that for zero TC

$$V\_{REF} \approx V\_{BE} + 17.2V\_T \tag{12.20}$$

$$
\approx 1.25\,\text{V} \tag{12.21}
$$

Let us now devise a circuit that adds *VB E* to 17*.*2*VT* . First, consider the circuit shown in Fig. 12.8, where the base currents are assumed to be negligible, transistor *Q*<sup>2</sup> consists of *n* unit transistors in parallel, and *Q*<sup>1</sup> is a unit transistor. Suppose we somehow force *VO*<sup>1</sup> and *VO*<sup>2</sup> to be equal. Then, *VB E*<sup>1</sup> = *R I* + *VB E*<sup>2</sup> and *R I* = *VB E*<sup>1</sup> − *VB E*<sup>2</sup> = *VT* ln *n*. Thus, *VO*<sup>2</sup> = *VB E*<sup>2</sup> + *VT* ln *n*, suggesting that *VO*<sup>2</sup> can serve as a temperature-independent reference if ln *n* ≈ 17*.*2 (while *VO*<sup>1</sup> and *VO*<sup>2</sup> remain equal).

The circuit of Fig. 12.8 requires three modifications to become practical. First, a mechanism must be added to guarantee that *VO*<sup>1</sup> = *VO*2. Second, since ln *n* = 17*.*2 translates to a prohibitively large *n*, the term *R I* = *VT* ln *n* must be scaled up by a reasonable factor. Third, *VO*2, which is somehow forced to be equal to *VO*1, *cannot* become temperature-independent because *VO*<sup>2</sup> ≈ *VB E*<sup>1</sup> ≈ 800 mV whereas, for temperature independence, we must have *VO*<sup>2</sup> = *VB E*<sup>2</sup> + 17*.*2*VT* ≈ 1*.*25 V. Shown in Fig. 12.9 is an implementation accomplishing all tasks [4]. Here, amplifier *A*<sup>1</sup> senses *VX* and *VY* , driving the top terminals of *R*<sup>1</sup> and *R*<sup>2</sup> (*R*<sup>1</sup> = *R*2) such that *X* and *Y* settle to approximately equal voltages. The

▲

Here is the image describtion:
```
The image consists of two circuit diagrams labeled as Figure 12.8 and Figure 12.9, which illustrate the conceptual generation and actual implementation of a temperature-independent voltage, respectively.

**Figure 12.8: Conceptual generation of temperature-independent voltage**
- The circuit is powered by a voltage source labeled \( V_{DD} \).
- Two current sources, each providing a current \( I \), are connected to the top of the circuit.
- The left side of the circuit features a transistor \( Q_1 \) with its base connected to a voltage \( V_{BE1} \) and its emitter grounded. The collector of \( Q_1 \) is connected to the current source.
- The right side of the circuit features another transistor \( Q_2 \) with its base connected to a voltage \( V_{BE2} \) and its emitter grounded. The collector of \( Q_2 \) is connected to the current source through a resistor \( R \).
- The collector of \( Q_1 \) is labeled \( V_{O1} \), and the collector of \( Q_2 \) is labeled \( V_{O2} \).
- The emitter area of \( Q_2 \) is \( n \) times that of \( Q_1 \).

**Figure 12.9: Actual implementation**
- The circuit includes two transistors \( Q_1 \) and \( Q_2 \) similar to Figure 12.8, with \( Q_1 \) having an emitter area \( A \) and \( Q_2 \) having an emitter area \( nA \).
- The bases of \( Q_1 \) and \( Q_2 \) are connected to a node \( X \) and a node \( Y \), respectively.
- Resistors \( R_1 \) and \( R_2 \) are connected in series between nodes \( X \) and \( Y \).
- An operational amplifier \( A_1 \) has its non-inverting input connected to node \( Y \) and its inverting input connected to a node where a resistor \( R_3 \) is connected to ground. The voltage at this node is \( V_T \ln n \).
- The output of the operational amplifier \( A_1 \) is labeled \( V_{out} \).

The diagrams illustrate the conceptual and practical approaches to generating a voltage that is independent of temperature variations by using transistors with different emitter areas and an operational amplifier to stabilize the output voltage.
```

temperature-independent voltage.

**Figure 12.9** Actual implementation of the concept shown in Fig. 12.8.

reference voltage is obtained at the output of the amplifier (rather than at node *Y* ). Following the analysis of Fig. 12.8, we have *VB E*<sup>1</sup> − *VB E*<sup>2</sup> = *VT* ln *n*, arriving at a current equal to *VT* ln *n/R*<sup>3</sup> through the right branch and hence an output voltage of

$$V\_{out} = V\_{BE2} + \frac{V\_T \ln n}{R\_3} (R\_3 + R\_2) \tag{12.22}$$

$$=V\_{BE2} + (V\_T \ln n) \left(1 + \frac{R\_2}{R\_3}\right) \tag{12.23}$$

For a zero TC, we must have *(*1 + *R*2*/R*3*)*ln *n* ≈ 17*.*2. For example, we may choose *n* = 31 and *R*2*/R*<sup>3</sup> = 4. Note that these results do not depend on the TC of the resistors.

It is interesting to understand how the third issue mentioned above is resolved in the topology of Fig. 12.9: we do not attempt to make *VY* (≈ *VB E*1) temperature-independent; rather, we amplify the PTAT voltage drop across *R*<sup>3</sup> by a factor of 1 + *R*2*/R*<sup>3</sup> and then add the result to *VB E*2.

#### ▲**Example 12.4**

**Q1**

In Fig. 12.9, *R*<sup>1</sup> and *R*<sup>2</sup> are equal and sustain equal voltages, each carrying a current of *(VT* ln *n)/R*3. We therefore have

$$V\_{out} = V\_{BE1} + (V\_T \ln n) \frac{R\_1}{R\_3} \tag{12.24}$$

But the second term is *not* equal to 17*.*2*VT* if we have already chosen *(VT* ln *n)(*1 + *R*2*/R*3*)* = 17*.*2*VT* . Explain this discrepancy.

#### **Solution**

Razavi-3930640 book December 17, 201517:21 517

The first terms in (12.23) and (12.24) are different. We substitute *VB E*<sup>1</sup> = *VB E*<sup>2</sup> + *VT* ln *n* in Eq. (12.13):

$$\frac{\partial V\_{BE1}}{\partial T} = \frac{V\_{BE2} + V\_T \ln n - (4 + m)V\_T - E\_g/q}{T} \tag{12.25}$$

$$\dot{\delta} = \frac{\partial V\_{BE2}}{\partial T} + \frac{k}{q} \ln n \tag{12.26}$$

Thus,

$$\frac{\partial V\_{out}}{\partial T} = \frac{\partial V\_{BE1}}{\partial T} + \left(\frac{k}{q} \ln n\right) \frac{R\_1}{R\_3} \tag{12.27}$$

$$=\frac{\partial V\_{BE2}}{\partial T} + \left(\frac{k}{q}\ln n\right)\left(1 + \frac{R\_1}{R\_3}\right) \tag{12.28}$$

which is consistent with (12.23).

The circuit of Fig. 12.9 entails a number of design issues. We consider each one below.

**Collector Current Variation** The circuit of Fig. 12.9 violates one of our earlier assumptions: the collector currents of *Q*<sup>1</sup> and *Q*2, given by *(VT* ln *n)/R*3, are proportional to *T* , whereas ∂*VB E /*∂*T* ≈ −1*.*5 mV/K was derived for a *constant* current. What happens to the temperature coefficient of *VB E* if the collector currents are PTAT? As a first-order iterative solution, let us assume that *IC*<sup>1</sup> = *IC*<sup>2</sup> ≈ *(VT* ln *n)/R*3. Returning to Eq. (12.9) and including ∂ *IC/*∂*T* , we have

$$\frac{\partial V\_{BE}}{\partial T} = \frac{\partial V\_T}{\partial T} \ln \frac{I\_C}{I\_S} + V\_T \left( \frac{1}{I\_C} \frac{\partial I\_C}{\partial T} - \frac{1}{I\_S} \frac{\partial I\_S}{\partial T} \right) \tag{12.29}$$

Since ∂ *IC/*∂*T* ≈ *(VT* ln *n)/(R*3*T )* = *IC/T* , we can write

$$\frac{\partial V\_{BE}}{\partial T} = \frac{\partial V\_T}{\partial T} \ln \frac{I\_C}{I\_S} + \frac{V\_T}{T} - \frac{V\_T}{I\_S} \frac{\partial I\_S}{\partial T} \tag{12.30}$$

Equation (12.13) is therefore modified as

$$\frac{\partial V\_{BE}}{\partial T} = \frac{V\_{BE} - (3+m)V\_T - E\_g/q}{T} \tag{12.31}$$

indicating that the TC is slightly less negative than −1*.*5 mV/K. In practice, accurate simulations are necessary to predict the temperature coefficient.

**Compatibility with CMOS Technology** Our derivation of a temperature-independent voltage relies on the exponential characteristics of bipolar devices for both negative- and positive-TC quantities. We must therefore seek structures in a standard CMOS technology that exhibit such characteristics.

In *n*-well processes, a *pnp* transistor can be formed as depicted in Fig. 12.10. A *p*<sup>+</sup> region (the same as the S/D region of PFETs) inside an *n*-well serves as the emitter and the *n*-well itself as the base. The *p*-type substrate acts as the collector and it is inevitably connected to the most negative supply (usually ground). The circuit of Fig. 12.9 can therefore be redrawn as shown in Fig. 12.11.

▲

Here is the image describtion:
```
The image depicts a cross-sectional view of a semiconductor device, specifically a PNP bipolar junction transistor (BJT) integrated into a silicon substrate. Here is a detailed description of the image:

1. **Substrate and Wells**:
   - The base material is labeled as a "p-substrate," indicating that the primary substrate is doped with acceptor impurities, making it a p-type semiconductor.
   - There is an "n-well" region within the p-substrate. This n-well is doped with donor impurities, making it an n-type region.

2. **Regions and Contacts**:
   - There are three distinct regions labeled C, E, and B, which correspond to the collector, emitter, and base of the transistor, respectively.
   - The collector (C) is a p+ region, indicating a heavily doped p-type region.
   - The emitter (E) is also a p+ region, indicating another heavily doped p-type region.
   - The base (B) is an n+ region, indicating a heavily doped n-type region.

3. **Transistor Structure**:
   - The PNP transistor is formed with the emitter (E) and collector (C) being p+ regions, and the base (B) being an n+ region.
   - The emitter (E) is situated within the n-well, and the base (B) is adjacent to the emitter within the same n-well.
   - The collector (C) is located outside the n-well in the p-substrate.

4. **Connections**:
   - Each region (C, E, and B) has a metal contact on the surface for external electrical connections.
   - The collector (C) contact is connected to the p+ region in the p-substrate.
   - The emitter (E) contact is connected to the p+ region within the n-well.
   - The base (B) contact is connected to the n+ region within the n-well.

5. **Transistor Operation**:
   - In a PNP transistor, the emitter (E) injects holes into the base (B), and these holes are collected by the collector (C).
   - The n-well serves as the base region for the PNP transistor, with the p+ regions acting as the emitter and collector.

This cross-sectional view illustrates the physical layout and doping profile of a PNP bipolar junction transistor within a silicon substrate, highlighting the different regions and their respective doping types.
```

**Figure 12.10** Realization of a *pnp* bipolar transistor in CMOS technology.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring a differential amplifier configuration. Here is a detailed description of the components and their connections:

1. **Resistors**:
   - **R1**: Connected between point X and the positive supply voltage.
   - **R2**: Connected between point Y and the positive supply voltage.
   - **R3**: Connected between point Y and the emitter of transistor Q2.

2. **Transistors**:
   - **Q1**: An NPN transistor with its emitter connected to ground. The base of Q1 is labeled as point A.
   - **Q2**: Another NPN transistor with its emitter connected to ground. The base of Q2 is labeled as point nA.

3. **Operational Amplifier (A1)**:
   - The inverting input (-) of the op-amp is connected to point Y.
   - The non-inverting input (+) of the op-amp is connected to ground.
   - The output of the op-amp is labeled as V_out.

4. **Connections**:
   - Point X is connected to the collector of transistor Q1.
   - Point Y is connected to the collector of transistor Q2 and to resistor R2.
   - The output of the op-amp (V_out) is connected to the circuit's output node.

5. **Ground Connections**:
   - The emitters of both transistors Q1 and Q2 are connected to ground.
   - The non-inverting input of the op-amp is also connected to ground.

This circuit appears to be a differential amplifier where the transistors Q1 and Q2 form a differential pair. The op-amp A1 is used to amplify the difference between the voltages at points X and Y. The resistors R1, R2, and R3 set the biasing and gain of the circuit. The output voltage (V_out) is taken from the output of the op-amp.
```

**Figure 12.11** Circuit of Fig. 12.9 implemented with *pnp* transistors.

**Op Amp Offset and Output Impedance** As explained in Chapter 14, owing to asymmetries, op amps suffer from input "offsets," i.e., the output voltage of the op amp is not zero if the input is set to zero. The input offset voltage of the op amp in Fig. 12.9 introduces error in the output voltage. Included in Fig. 12.12, the effect is quantified as *VB E*<sup>1</sup> − *VO S* ≈ *VB E*<sup>2</sup> + *R*<sup>3</sup> *IC*<sup>2</sup> (if *A*<sup>1</sup> is large) and *Vout* = *VB E*<sup>2</sup> +*(R*<sup>3</sup> + *R*2*)IC*2. Thus,

$$V\_{out} = V\_{BE2} + (R\_3 + R\_2)\frac{V\_{BE1} - V\_{BE2} - V\_{OS}}{R\_3} \tag{12.32}$$

$$\dot{\lambda} = V\_{BE2} + \left(1 + \frac{R\_2}{R\_3}\right) (V\_T \ln n - V\_{OS}) \tag{12.33}$$

where we have assumed that *IC*<sup>2</sup> ≈ *IC*<sup>1</sup> despite the offset voltage. The key point here is that *VO S* is amplified by 1+ *R*2*/R*3, introducing error in *Vout* . More important, as explained in Chapter 14, *VO S* itself varies with temperature, raising the temperature coefficient of the output voltage.

Here is the image describtion:
```
The image depicts an electronic circuit involving an operational amplifier (op-amp) and several resistors and transistors. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1)**: The op-amp is the central component in the circuit, represented by a triangle with two input terminals (inverting "-" and non-inverting "+") and one output terminal. The output terminal is labeled as \( V_{out} \).

2. **Resistors**: There are three resistors in the circuit:
   - \( R_1 \): Connected between point X and the base of transistor \( Q_1 \).
   - \( R_2 \): Connected between point Y and the non-inverting input of the op-amp.
   - \( R_3 \): Connected between point Y and the base of transistor \( Q_2 \).

3. **Transistors**: There are two NPN transistors in the circuit:
   - \( Q_1 \): The emitter is grounded, the base is connected to point X through \( R_1 \), and the collector is connected to point A.
   - \( Q_2 \): The emitter is grounded, the base is connected to point Y through \( R_3 \), and the collector is connected to point nA.

4. **Voltage Sources**:
   - \( V_{os} \): A voltage source connected between the inverting input of the op-amp and point Y.

5. **Ground Connections**: The emitters of both transistors \( Q_1 \) and \( Q_2 \) are connected to the ground.

6. **Nodes**:
   - Point X: The junction where \( R_1 \), the base of \( Q_1 \), and the inverting input of the op-amp meet.
   - Point Y: The junction where \( R_2 \), \( R_3 \), and the non-inverting input of the op-amp meet.

7. **Output**: The output of the op-amp is labeled as \( V_{out} \), which is connected to an unspecified load or further circuitry.

In summary, the circuit consists of an op-amp with its inverting input connected to a node X through a resistor \( R_1 \) and a voltage source \( V_{os} \). The non-inverting input is connected to node Y through a resistor \( R_2 \). Two NPN transistors \( Q_1 \) and \( Q_2 \) are connected to nodes X and Y, respectively, with their emitters grounded and their collectors connected to points A and nA. The output of the op-amp is labeled \( V_{out} \).
```

**Figure 12.12** Effect of op amp offset on the reference voltage.

#### ▲**Example 12.5**

Razavi-3930640 book December 17, 201517:21 519

Assuming an ideal op amp, determine the small-signal gain from *VO S* to *Vout* in Fig. 12.12.

### **Solution**

In the absence of the op amp offset, the two diode-connected bipolar transistors carry equal bias currents, exhibiting a transconductance of *gm*. Replacing *Q*<sup>1</sup> and *Q*<sup>2</sup> with a small-signal resistance equal to 1*/gm* and noting that *VX* − *VO S* ≈ *VY* , we write the following small-signal equation:

$$\frac{1/\text{g}\_m}{1/\text{g}\_m + R\_1}V\_{out} - V\_{OS} = \frac{1/\text{g}\_m + R\_3}{1/\text{g}\_m + R\_3 + R\_2}V\_{out} \tag{12.34}$$

Since *R*<sup>1</sup> = *R*2,

$$\frac{V\_{out}}{V\_{OS}} = -\left[1 + \frac{1}{g\_m R\_2} + \frac{\left(1/g\_m + R\_2\right)^2}{R\_2 R\_3}\right] \tag{12.35}$$

If *gm R*<sup>2</sup> ) 1, then *Vout /VO S* ≈ −*(*1+*R*2*/R*3*)*, agreeing with the results obtained previously. (After all, if 1*/gm* ≈ 0, *VO S* simply sees a noninverting amplifier with a gain of 1 + *R*2*/R*3.)

Why does (12.35) not completely agree with the −*VO S(*1 + *R*2*/R*3*)* component in (12.33)? Recall that (12.33) was derived with the assumption that *IC*<sup>1</sup> ≈ *IC*<sup>2</sup> despite the offset voltage. Since *VX* − *VO S* = *VY* , we have *IC*1*R*<sup>1</sup> − *VO S* = *IC*2*R*2, and hence *IC*<sup>1</sup> = *IC*<sup>2</sup> + *VO S/R*2. Let us return to (12.32) and write

$$V\_{BE1} - V\_{BE2} - V\_{OS} = V\_T \ln \frac{I\_{C1}}{I\_{S1}} - V\_T \ln \frac{I\_{C2}}{I\_{S2}} - V\_{OS} \tag{12.36}$$

$$=V\_T \ln n - V\_T \ln \frac{I\_{C1}}{I\_{C2}} - V\_{OS} \tag{12.37}$$

$$=Vr\ln n - Vr\ln\left(1 + \frac{V\_{OS}}{R\_2I\_{C2}}\right) - Vos \tag{12.38}$$

$$\approx V\_T \ln n - V\_T \frac{V\_{OS}}{R\_2 I\_{C2}} - V\_{OS} \tag{12.39}$$

$$\approx V\_T \ln n - \left( 1 + \frac{1}{g\_m R\_2} \right) V\_{OS} \tag{12.40}$$

The output offset contribution therefore amounts to −[1 + 1*/(gm R*2*)*]*(*1 + *R*2*/R*3*)VO S*, which is approximately the same as (12.35). ▲

Several methods are employed to lower the effect of *VO S*. First, the op amp incorporates large devices in a carefully chosen topology so as to minimize the offset (Chapter 19). Second, as illustrated in Fig. 12.7, the collector currents of *Q*<sup>1</sup> and *Q*<sup>2</sup> can be ratioed by a factor of *m* such that !*VB E* = *VT* ln*(mn)*. Third, each branch may use two *pn* junctions in series to double !*VB E* . Figure 12.13 depicts a realization using the last two techniques. Here, *R*<sup>1</sup> and *R*<sup>2</sup> are ratioed by a factor of *m*, producing *I*<sup>1</sup> ≈ *m I*2. Neglecting base currents and assuming that *A*<sup>1</sup> is large, we can now write *VB E*1+*VB E*2−*VO S* = *VB E*3+*VB E*4+ *R*<sup>3</sup> *I*<sup>2</sup> and *Vout* = *VB E*<sup>3</sup> + *VB E*<sup>4</sup> + *(R*<sup>3</sup> + *R*2*)I*2. It follows that

$$V\_{out} = V\_{BE3} + V\_{BE4} + (R\_3 + R\_2)\frac{2V\_T\ln(mn) - V\_{OS}}{R\_3} \tag{12.41}$$

$$\dot{\lambda} = 2V\_{BE} + \left(1 + \frac{R\_2}{R\_3}\right) \left[2V\_T \ln(mn) - V\_{OS}\right] \tag{12.42}$$

Here is the image describtion:
```
The image depicts a circuit diagram that includes an operational amplifier (A1), resistors, and a set of transistors. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1)**:
   - The operational amplifier has two input terminals: the inverting input (-) and the non-inverting input (+).
   - The inverting input is connected to a node labeled Y.
   - The non-inverting input is connected to a voltage source labeled \( V_{OS} \).
   - The output of the operational amplifier is labeled \( V_{out} \).

2. **Resistors**:
   - There are three resistors in the circuit:
     - \( R_1 \) with a resistance value of \( R \) is connected between a node labeled X and a node labeled Y.
     - \( R_2 \) with a resistance value of \( mR \) is connected between node Y and the output of the operational amplifier.
     - \( R_3 \) is connected between node Y and the non-inverting input of the operational amplifier.

3. **Transistors**:
   - There are four transistors labeled \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \).
   - Transistors \( Q_1 \) and \( Q_2 \) form a pair, with their emitters connected to ground and their bases connected together to a node labeled A.
   - Transistors \( Q_3 \) and \( Q_4 \) form another pair, with their emitters connected to ground and their bases connected together to a node labeled nA.
   - The collector of \( Q_2 \) is connected to node X, and the collector of \( Q_4 \) is connected to node Y.

4. **Currents**:
   - \( I_1 \) is the current flowing through the collector of \( Q_2 \) into node X.
   - \( I_2 \) is the current flowing through the collector of \( Q_4 \) into node Y.

5. **Nodes**:
   - Node X is a junction point where \( R_1 \), the collector of \( Q_2 \), and the base of \( Q_1 \) are connected.
   - Node Y is a junction point where \( R_1 \), \( R_2 \), \( R_3 \), and the collector of \( Q_4 \) are connected.

6. **Ground**:
   - The ground symbol is used to indicate the reference point for the circuit, connected to the emitters of all transistors and the output voltage \( V_{out} \).

The circuit appears to be a differential amplifier configuration with transistors and an operational amplifier, likely designed to amplify the difference between the currents \( I_1 \) and \( I_2 \) and produce an output voltage \( V_{out} \).
```

**Figure 12.13** Reduction of the effect of op amp offset.

Thus, the effect of the offset voltage is reduced by increasing the first term in the square brackets. The issue, however, is that *Vout* ≈ 2 × 1*.*25 V = 2*.*5 V, a value difficult to generate by the op amp at low supply voltages.

In the circuits studied above, the op amp drives two resistive branches and must therefore provide a low output impedance. Fortunately, it is possible to avoid this issue by a simple modification described below.

The implementation of Fig. 12.13 is not feasible in a standard CMOS technology because the collectors of *Q*<sup>2</sup> and *Q*<sup>4</sup> are not grounded. In order to utilize the bipolar structure shown in Fig. 12.10, we modify the series combination of the diodes as illustrated in Fig. 12.14(a), converting one of the diodes to an emitter follower. However, we must ensure that the bias currents of both transistors have the same behavior with temperature. Thus, we bias each transistor by a PMOS current source rather than a resistor [Fig. 12.14(b)]. The overall circuit then assumes the topology shown in Fig. 12.15, where the op amp adjusts the gate voltage of the PMOS devices so as to equalize *VX* and *VY* . Interestingly, in this circuit, the op amp experiences no resistive loading, but the mismatch and channel-length modulation of the PMOS devices introduce error at the output (Problem 12.3).

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b), each depicting different transistor circuit configurations.

**Part (a):**
- The left side of part (a) shows a circuit with two NPN bipolar junction transistors (BJTs), labeled Q1 and Q2.
- The emitter of Q1 is connected to ground.
- The base of Q1 is connected to the emitter of Q2.
- The base of Q2 is connected to the collector of Q1.
- The collector of Q2 is connected to a node labeled 2V_BE, which indicates a voltage equal to twice the base-emitter voltage (V_BE) of a single transistor.

- The right side of part (a) shows a simplified version of the same circuit.
- Q1 and Q2 are still present, with Q1's emitter connected to ground.
- Q1's base is connected to the emitter of Q2.
- Q2's base is connected to the collector of Q1.
- The collector of Q2 is connected to the node labeled 2V_BE.

**Part (b):**
- This part shows a more complex circuit involving both BJTs and MOSFETs.
- Q1 and Q2 are present as in part (a), with Q1's emitter connected to ground and its base connected to the emitter of Q2.
- Q2's base is connected to the collector of Q1, and its collector is connected to the node labeled 2V_BE.
- Additionally, there are two MOSFETs in the circuit.
- The source of the first MOSFET is connected to ground, and its gate is connected to a voltage source labeled V_b.
- The drain of the first MOSFET is connected to the source of the second MOSFET.
- The gate of the second MOSFET is also connected to V_b.
- The drain of the second MOSFET is connected to a voltage source labeled V_DD.
- The node between the drain of the first MOSFET and the source of the second MOSFET is connected to the base of Q2.

In summary, the image shows two configurations of transistor circuits, with part (a) focusing on a simpler BJT arrangement and part (b) incorporating additional MOSFETs to form a more complex circuit.
```

**Figure 12.14** (a) Conversion of series diodes to a topology with grounded collectors; (b) circuit of part (a) biased by PMOS current sources.

An important concern in the circuit of Fig. 12.15 is the relatively low current gain of the "native" *pnp* transistors. Since the base currents of *Q*<sup>2</sup> and *Q*<sup>4</sup> generate an error in the emitter currents of *Q*<sup>1</sup> and *Q*3, a means of base current cancellation may be necessary (Problem 12.5).

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, which appears to be a differential amplifier with active load and current mirror. Here is a detailed description of the circuit:

1. **Power Supply:**
   - The circuit is powered by a voltage source \( V_{DD} \) at the top.

2. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The gates of M1 and M2 are the inputs of the differential amplifier.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair M1 and M2.
   - **Q1, Q2, Q3, and Q4:** These are bipolar junction transistors (BJTs). Q1 and Q2 form a current mirror, and Q3 and Q4 form another current mirror. The current mirrors are used to provide biasing and to mirror the current through the differential pair.

3. **Operational Amplifier (A1):**
   - The circuit includes an operational amplifier (A1) with its inverting input connected to the drain of M1 and its non-inverting input connected to the drain of M2. The output of the operational amplifier is connected to the gate of M2.

4. **Resistors:**
   - **R1 and R2:** These resistors are connected in series between the output node \( V_{out} \) and ground. They form a voltage divider network.

5. **Nodes:**
   - **X and Y:** These are intermediate nodes in the circuit. Node X is connected to the source of M1 and the collector of Q2. Node Y is connected to the source of M2 and the collector of Q4.

6. **Inputs:**
   - The inputs to the differential amplifier are labeled as \( A \) and \( nA \). The input \( A \) is connected to the gate of M1 and the base of Q1. The input \( nA \) is connected to the gate of M2 and the base of Q3.

7. **Output:**
   - The output of the circuit is labeled as \( V_{out} \), which is taken from the drain of M2.

8. **Current Mirrors:**
   - The current mirror formed by Q1 and Q2 ensures that the current through M1 is mirrored to M2. Similarly, the current mirror formed by Q3 and Q4 ensures that the current through M2 is mirrored to M1.

In summary, this circuit is a differential amplifier with an active load and current mirrors, designed to amplify the difference between the input signals \( A \) and \( nA \). The operational amplifier A1 helps to stabilize the circuit and improve its performance.
```

**nA Figure 12.15** Reference generator incorporating two series base-emitter voltages.

**Feedback Polarity** In the circuit of Fig. 12.9, the feedback signal produced by the op amp returns to both of its inputs. The negative-feedback factor is given by

$$\beta\_N = \frac{1/g\_{m2} + R\_3}{1/g\_{m2} + R\_3 + R\_2} \tag{12.43}$$

and the positive-feedback factor by

$$\beta\_P = \frac{1/g\_{m1}}{1/g\_{m1} + R\_1} \tag{12.44}$$

To ensure an overall negative feedback, β*<sup>P</sup>* must be less than β*<sup>N</sup>* , preferably by roughly a factor of two so that the circuit's transient response remains well behaved with large capacitive loads.

**Bandgap Reference** The voltage generated according to (12.20) is called a "bandgap reference." To understand the origin of this terminology, let us write the output voltage as

$$V\_{REF} = V\_{BE} + V\_T \ln n\tag{12.45}$$

and hence:

$$\frac{\partial V\_{REF}}{\partial T} = \frac{\partial V\_{BE}}{\partial T} + \frac{V\_T}{T} \ln n \tag{12.46}$$

Setting this to zero and substituting for ∂*VB E /*∂*T* from (12.13), we have

$$\frac{V\_{BE} - (4+m)V\_T - E\_g/q}{T} = -\frac{V\_T}{T} \ln n \tag{12.47}$$

If *VT* ln *n* is found from this equation and inserted in (12.45), we obtain

$$V\_{REF} = \frac{E\_{\rm g}}{q} + (4+m)V\_T \tag{12.48}$$

Thus, the reference voltage exhibiting a nominally-zero TC is given by a few *fundamental* numbers: the bandgap voltage of silicon, *Eg/q*, the temperature exponent of mobility, *m*, and the thermal voltage, *VT* . The term "bandgap" is used here because as *T* →0, *VREF* → *Eg/q*.

▲

#### ▲**Example 12.6**

Razavi-3930640 book December 17, 201517:21 522

Prove directly that, as *T* → 0, *VB E* → *Eg/q*, and hence *VREF* = *VB E* + *VT* ln *n* → *Eg/q*.

## **Solution**

From Eq. (12.8), we have

$$V\_{BE} = V\_T \ln{\frac{I\_C}{I\_S}}\tag{12.49}$$

$$=Vr\left[\ln Ic - \ln b - (4+m)\ln T + \frac{E\_g}{kT}\right] \tag{12.50}$$

Thus, *VB E* → *Eg/q* if *T* → 0 and *IC* is constant.

**Supply Dependence and Start-Up** In the circuit of Fig. 12.9, the output voltage is relatively independent of the supply voltage so long as the open-loop gain of the op amp is sufficiently high. The circuit may require a start-up mechanism because if *VX* and *VY* are equal to zero, the input differential pair of the op amp may turn off. Start-up techniques similar to those of Fig. 12.5 can be added to ensure that the op amp turns on when the supply is applied.

The supply rejection of the circuit typically degrades at high frequencies owing to the op amp's rejection properties, often mandating "supply regulation." An example is described in Sec. 12.8.

**Curvature Correction** If plotted as a function of temperature, bandgap voltages exhibit a finite "curvature," i.e., their TC is typically zero at one temperature and positive or negative at other temperatures (Fig. 12.16). The curvature arises from temperature variation of base-emitter voltages, collector currents, and offset voltages.

Here is the image describtion:
```
The image is a graph with a horizontal axis labeled "T" and a vertical axis labeled "V_REF." The graph depicts a curve that starts at a low value on the left, rises to a peak at a point labeled "T_0" in the middle, and then descends back to a low value on the right. The curve is symmetrical around the peak at "T_0," indicating that "V_REF" increases as "T" approaches "T_0" from either direction and decreases as "T" moves away from "T_0." The peak at "T_0" is marked with a dashed vertical line, emphasizing its significance as the maximum point of the curve.
```

**Figure 12.16** Curvature in temperature dependence of a bandgap voltage.

Many curvature correction techniques have been devised to suppress the variation of *VREF* [5, 6] in bipolar bandgap circuits, but they are seldom used in CMOS counterparts. This is because, due to large offsets and process variations, samples of a bandgap reference display substantially different zero-TC temperatures (Fig. 12.17), making it difficult to correct the curvature reliably.

Here is the image describtion:
```
The image is a graph with two axes. The horizontal axis is labeled "T," which typically represents temperature. The vertical axis is labeled "V_REF," which usually stands for reference voltage. 

The graph features multiple curves that are all concave down, meaning they have a peak and then slope downwards on either side. These curves are not identical but follow a similar general shape, suggesting that they represent different scenarios or conditions under which the reference voltage changes with temperature. The curves intersect at various points, indicating that the reference voltage varies with temperature in a non-linear fashion and that the relationship between V_REF and T is complex.
```

**Figure 12.17** Variation of the zero-TC temperature for different samples.

# **12.4 PTAT Current Generation**

In the analysis of bandgap circuits, we noted that the bias currents of the bipolar transistors are in fact proportional to absolute temperature. Useful in many applications, PTAT currents can be generated by a topology such as that shown in Fig. 12.18. Alternatively, we can combine the supply-independent biasing scheme of Fig. 12.2 with a bipolar core, arriving at Fig. 12.19.3 Assuming for simplicity that *M*1-*M*<sup>2</sup> and *M*3-*M*<sup>4</sup> are identical pairs, we note that for *ID*<sup>1</sup> = *ID*2, the circuit must ensure that *VX* = *VY* . Thus, *ID*<sup>1</sup> = *ID*<sup>2</sup> = *(VT* ln *n)/R*1, yielding the same behavior for *ID*5. In practice, due to mismatches between the transistors and, more important, the temperature coefficient of *R*1, the variation of *ID*<sup>5</sup> deviates from the ideal equation. For low-voltage operation, the topology of Fig. 12.18 is preferred.

Here is the image describtion:
```
The image consists of two circuit diagrams, each illustrating a method for generating a Proportional To Absolute Temperature (PTAT) current. Let's describe each diagram in detail:

**Figure 12.18: Generation of a PTAT Current**

1. **Components:**
   - Two NPN bipolar junction transistors (BJTs), labeled \( Q_1 \) and \( Q_2 \).
   - Two PMOS transistors, labeled \( M_3 \) and \( M_4 \).
   - An operational amplifier (op-amp) with inverting (-) and non-inverting (+) inputs.
   - A resistor, labeled \( R_1 \).
   - A current source labeled "PTAT Current".
   - A power supply voltage, \( V_{DD} \).

2. **Connections:**
   - The emitters of \( Q_1 \) and \( Q_2 \) are connected to the ground.
   - The base of \( Q_1 \) is connected to node A.
   - The base of \( Q_2 \) is connected to node nA.
   - The collector of \( Q_1 \) is connected to the inverting input of the op-amp.
   - The collector of \( Q_2 \) is connected to the non-inverting input of the op-amp.
   - The output of the op-amp is connected to the gates of \( M_3 \) and \( M_4 \).
   - The source of \( M_3 \) is connected to \( V_{DD} \).
   - The source of \( M_4 \) is connected to \( V_{DD} \).
   - The drain of \( M_3 \) is connected to the collector of \( Q_1 \).
   - The drain of \( M_4 \) is connected to the collector of \( Q_2 \) and one end of \( R_1 \).
   - The other end of \( R_1 \) is connected to the ground.
   - The PTAT current is drawn from the drain of \( M_4 \).

**Figure 12.19: Alternative Method of Generating a PTAT Current**

1. **Components:**
   - Two NPN bipolar junction transistors (BJTs), labeled \( Q_1 \) and \( Q_2 \).
   - Five PMOS transistors, labeled \( M_1 \), \( M_2 \), \( M_3 \), \( M_4 \), and \( M_5 \).
   - A resistor, labeled \( R_1 \).
   - A current source labeled "PTAT Current".
   - A power supply voltage, \( V_{DD} \).

2. **Connections:**
   - The emitters of \( Q_1 \) and \( Q_2 \) are connected to the ground.
   - The base of \( Q_1 \) is connected to node A.
   - The base of \( Q_2 \) is connected to node nA.
   - The collector of \( Q_1 \) is connected to the drain of \( M_1 \).
   - The collector of \( Q_2 \) is connected to the drain of \( M_2 \) and one end of \( R_1 \).
   - The other end of \( R_1 \) is connected to the ground.
   - The source of \( M_1 \) is connected to node X.
   - The source of \( M_2 \) is connected to node Y.
   - The gate of \( M_1 \) is connected to node Y.
   - The gate of \( M_2 \) is connected to node X.
   - The source of \( M_3 \) is connected to \( V_{DD} \).
   - The source of \( M_4 \) is connected to \( V_{DD} \).
   - The source of \( M_5 \) is connected to \( V_{DD} \).
   - The drain of \( M_3 \) is connected to node X.
   - The drain of \( M_4 \) is connected to node Y.
   - The gate of \( M_3 \) is connected to the gate of \( M_4 \).
   - The drain of \( M_5 \) is connected to the drain of \( M_4 \).
   - The PTAT current is drawn from the drain of \( M_5 \).

In both figures, the circuits are designed to generate a current that is proportional to the absolute temperature (PTAT), which is useful in various analog and mixed-signal applications, such as temperature sensors and biasing circuits.
```

The circuit of Fig. 12.18 can be readily modified to provide a bandgap reference voltage as well. Illustrated in Fig. 12.20, the idea is to add a PTAT voltage *ID*5*R*<sup>2</sup> to a base-emitter voltage. The output therefore equals

$$|V\_{REF} = |V\_{BE3}| + \frac{R\_2}{R\_1} V\_T \ln n\tag{12.51}$$

<sup>3</sup>The two circuits in Figs. 12.18 and 12.19 exhibit different supply rejections. With a carefully-designed op amp, the former achieves a higher rejection.

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with a current mirror load. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a positive voltage supply \( V_{DD} \).

2. **Transistors:**
   - **Q1, Q2, and Q3** are NPN bipolar junction transistors (BJTs).
   - **M3, M4, and M5** are PMOS transistors.

3. **Differential Pair:**
   - **Q1** and **Q2** form the differential pair.
   - The base of **Q1** is connected to input signal \( A \).
   - The base of **Q2** is connected to input signal \( nA \) (which is typically the inverted or complementary signal of \( A \)).

4. **Current Mirror:**
   - **M3** and **M4** form a current mirror.
   - The source of **M3** and **M4** are connected to \( V_{DD} \).
   - The drain of **M3** is connected to the collector of **Q1** at node \( X \).
   - The gate of **M3** is connected to the gate and drain of **M4**.

5. **Load Resistors:**
   - **R1** is connected between the collector of **Q2** and \( V_{DD} \).
   - **R2** is connected between the collector of **Q3** and \( V_{DD} \).

6. **Output:**
   - The output voltage \( V_{out} \) is taken from the collector of **Q3**.

7. **Additional Components:**
   - **M5** is another PMOS transistor with its source connected to \( V_{DD} \) and its drain connected to the collector of **Q3**.
   - The gate of **M5** is connected to the gate of **M4**.

8. **Operational Amplifier:**
   - There is an operational amplifier symbol with its inverting input connected to node \( X \) and its non-inverting input connected to node \( Y \).

9. **Connections:**
   - The emitter of **Q1**, **Q2**, and **Q3** are all connected to the ground.
   - Node \( X \) is the connection point between the collector of **Q1** and the drain of **M3**.
   - Node \( Y \) is the connection point between the collector of **Q2** and the resistor \( R1 \).

This circuit is typically used in analog signal processing, where the differential pair (Q1 and Q2) amplifies the difference between the input signals \( A \) and \( nA \). The current mirror (M3 and M4) ensures that the current through Q1 and Q2 is mirrored, providing a balanced operation. The output is taken from the collector of Q3, which is influenced by the differential pair and the current mirror.
```

**Figure 12.20** Generation of a temperature-independent voltage.

where all of the PMOS transistors are assumed identical. Note that the value of *VB E*<sup>3</sup> and hence the size of *Q*<sup>3</sup> are somewhat arbitrary so long as the sum of the two terms in (12.51) gives a zero TC. In reality, mismatches of the PMOS devices introduce error in *Vout* .

# **12.5 Constant-***Gm* **Biasing**

The transconductance of MOSFETs plays a critical role in analog circuits, determining such performance parameters as noise, small-signal gain, and speed. For this reason, it is often desirable to bias the transistors such that their transconductance does not depend on the temperature, process, or supply voltage.

A simple circuit used to define the transconductance is the supply-independent bias topology of Fig. 12.3. Recall that the bias current is given by

$$I\_{\rm out} = \frac{2}{\mu\_n C\_{ox} (W/L)\_N} \frac{1}{R\_S^2} \left(1 - \frac{1}{\sqrt{K}}\right)^2 \tag{12.52}$$

Thus, the transconductance of *M*<sup>1</sup> equals

$$\mathbf{g}\_{m1} = \sqrt{2\mu\_n \mathbf{C}\_{ox} \left(\frac{W}{L}\right)\_N I\_{D1}}\tag{12.53}$$

$$\eta = \frac{2}{R\_S} \left( 1 - \frac{1}{\sqrt{K}} \right) \tag{12.54}$$

a value independent of the supply voltage and MOS device parameters.

In reality, the value of *RS* in (12.54) does vary with temperature and process. If the temperature coefficient of the resistor is known, bandgap and PTAT reference generation techniques can be utilized to cancel the temperature dependence. *Process* variations, however, limit the accuracy with which *gm*<sup>1</sup> is defined.

In systems where a precise clock frequency is available, the resistor *RS* in Fig. 12.3 can be replaced by a switched-capacitor equivalent (Chapter 13) to achieve a somewhat higher accuracy. Depicted in Fig. 12.21, the idea is to establish an average resistance equal to *(CS fC K )*−<sup>1</sup> between the source of *M*<sup>2</sup> and ground, where *fC K* denotes the clock frequency. Capacitor *CB* is added to shunt the high-frequency components resulting from switching to ground. Since the absolute value of capacitors is typically more tightly controlled and since the TC of capacitors is much smaller than that of resistors, this technique provides a higher reproducibility in the bias current and transconductance.

Here is the image describtion:
```
The image shows a schematic diagram of an electronic circuit, which appears to be a sample-and-hold circuit commonly used in analog-to-digital conversion systems. The circuit can be broken down into two main parts: the transistor network and the switch-capacitor network.

1. **Transistor Network:**
   - The circuit includes four MOSFET transistors labeled \( M_1, M_2, M_3, \) and \( M_4 \).
   - \( M_1 \) and \( M_2 \) are connected in a configuration that suggests they are part of a differential pair. The sources of \( M_1 \) and \( M_2 \) are connected to ground.
   - \( M_3 \) and \( M_4 \) are connected to the power supply \( V_{DD} \). The drains of \( M_3 \) and \( M_4 \) are connected to the drains of \( M_1 \) and \( M_2 \), respectively.
   - The gate of \( M_3 \) is connected to the drain of \( M_1 \), and the gate of \( M_4 \) is connected to the drain of \( M_2 \), forming a positive feedback loop.

2. **Capacitor and Resistor:**
   - There is a capacitor \( C_B \) connected between the common source of \( M_3 \) and \( M_4 \) and ground.
   - The right side of the circuit shows a capacitor \( C_S \) and two switches \( S_1 \) and \( S_2 \). The switches are controlled by clock signals \( CK \) and \( \overline{CK} \) (the complement of \( CK \)).
   - When \( S_1 \) is closed (CK is high), the capacitor \( C_S \) charges to the input voltage. When \( S_2 \) is closed (CK is low), the capacitor \( C_S \) holds the sampled voltage.

3. **Equivalent Circuit:**
   - The rightmost part of the image shows an equivalent circuit representation of the switch-capacitor network. It consists of a resistor \( R_S \) connected to ground, which models the on-resistance of the switches when they are closed.

In summary, the image depicts a sample-and-hold circuit with a differential pair of MOSFETs and a switch-capacitor network. The circuit is used to sample an input voltage and hold it for a certain period, which is essential in analog-to-digital conversion processes.
```

**Figure 12.21** Constant-*Gm* biasing by means of a switched-capacitor "resistor."

The switched-capacitor approach of Fig. 12.21 can be applied to other circuits as well. For example, as shown in Fig. 12.22, a voltage-to-current converter with a relatively high accuracy can be constructed.

Here is the image describtion:
```
The image depicts a circuit diagram used for voltage-to-current conversion by means of a switched-capacitor resistor. The key components and their connections are as follows:

1. **Operational Amplifier (Op-Amp)**: The circuit includes an operational amplifier with its non-inverting input (+) connected to a reference voltage \( V_{REF} \). The inverting input (-) is connected to the source of a MOSFET transistor \( M_1 \).

2. **MOSFET Transistor (M1)**: The drain of the MOSFET \( M_1 \) is connected to the reference voltage \( V_{REF} \), and the source is connected to the inverting input of the Op-Amp. The current flowing through the MOSFET is labeled as \( I_{REF} \).

3. **Capacitors (C_B and C_S)**: There are two capacitors in the circuit. Capacitor \( C_B \) is connected between the inverting input of the Op-Amp and ground. Capacitor \( C_S \) is connected between the source of the MOSFET and ground through two switches.

4. **Switches (S1 and S2)**: The circuit includes two switches, \( S_1 \) and \( S_2 \), which are controlled by clock signals \( CK \) and \( \overline{CK} \) (the complement of \( CK \)), respectively. Switch \( S_1 \) is connected between the source of the MOSFET and one terminal of capacitor \( C_S \). Switch \( S_2 \) is connected between the other terminal of capacitor \( C_S \) and ground.

5. **Clock Signals (CK and \(\overline{CK}\))**: The switches \( S_1 \) and \( S_2 \) are alternately controlled by the clock signals \( CK \) and \( \overline{CK} \). When \( CK \) is high, \( S_1 \) is closed, and when \( \overline{CK} \) is high, \( S_2 \) is closed.

The circuit operates by alternately charging and discharging the capacitor \( C_S \) through the switches \( S_1 \) and \( S_2 \), effectively creating a switched-capacitor resistor. This configuration allows the conversion of the reference voltage \( V_{REF} \) into a corresponding current \( I_{REF} \) through the MOSFET \( M_1 \).
```

Here is the image describtion:
```
The image shows a section header from a document or book. The section is numbered "12.6" and is titled "Speed and Noise Issues." The title is preceded by a small black square bullet point. The text is in a serif font, and the numbering and title are in bold. The background is white, and the text is black.
```

Even though reference generators are low-frequency circuits, they may affect the speed of the circuits that they feed. Furthermore, various building blocks may experience "crosstalk" through reference lines. These difficulties arise because of the finite output impedance of reference voltage generators, especially if they incorporate op amps. As an example, let us consider the configuration shown in Fig. 12.23, assuming that the voltage at node *N* is heavily disturbed by the circuit fed by *M*5. For fast changes in *VN* , the op amp cannot maintain *VP* constant, and the bias currents of *M*<sup>5</sup> and *M*<sup>6</sup> experience large transient changes. Also, the duration of the transient at node *P* may be quite long if the op amp suffers from a slow response. For this reason, many applications may require a high-speed op amp in the reference generator.

In systems where the power consumed by the reference circuit must be small, the use of a high-speed op amp may not be feasible. Alternatively, the critical node, e.g., node *P* in Fig. 12.23, can be bypassed to ground by means of a large capacitor (*CB*) so as to suppress the effect of external disturbances. This approach involves two issues. First, the stability of the op amp must not degrade with the addition of the capacitor, requiring the op amp to be of a one-stage nature (Chapter 10). Second, since *CB* generally slows down the transient response of the op amp, its value must be much greater than the capacitance that couples the disturbance to node *P*. As illustrated in Fig. 12.24, if *CB* is not sufficiently large, then *VP*

Here is the image describtion:
```
The image consists of two parts: a schematic diagram of an electronic circuit and a graph showing the behavior of a voltage over time.

### Schematic Diagram:
1. **Components and Connections:**
   - **Operational Amplifier (Op-Amp):** The central component is an operational amplifier with its inverting input (-) connected to point A and its non-inverting input (+) connected to point B.
   - **Resistor (R1):** There is a resistor R1 connected between points A and B.
   - **Transistors:** There are two transistors connected to ground, one at point A and one at point B.
   - **Capacitors (C_B):** There is a capacitor labeled C_B connected to ground, but it is shown in a lighter shade, indicating it might be optional or for a specific condition.
   - **MOSFETs (M5 and M6):** Two MOSFETs, M5 and M6, are connected in series between the power supply voltage (V_DD) and ground. The gate of M5 is connected to point P, and the gate of M6 is connected to point N.
   - **Point P and N:** Point P is connected to the output of the operational amplifier, and point N is connected to the gate of M6.

2. **Voltage and Time Graph:**
   - The graph shows the voltage (V_P) at point P over time (t).
   - There are three curves labeled C_B1, C_B2, and C_B3, representing different capacitance values.
   - The curve labeled "Very Large C_B" shows a smooth, gradual change in voltage, indicating a large capacitance value.
   - The other curves (C_B1, C_B2, and C_B3) show varying degrees of voltage change, with C_B1 having the steepest change and C_B3 having a more gradual change.

### Interpretation:
- The circuit appears to be a feedback loop involving an operational amplifier, resistors, capacitors, and MOSFETs.
- The graph indicates how the voltage at point P changes over time for different capacitance values of C_B.
- A larger capacitance (Very Large C_B) results in a smoother voltage transition, while smaller capacitances (C_B1, C_B2, C_B3) result in steeper transitions.
- The operational amplifier likely controls the voltage at point P, which in turn affects the gate voltages of the MOSFETs M5 and M6, influencing the overall behavior of the circuit.

This detailed description covers the components, their connections, and the behavior of the circuit as depicted in the image.
```

**Figure 12.23** Effect of circuit transients on reference voltages and currents.

**Figure 12.24** Effect of increasing bypass capacitor on the response of a reference generator.

experiences a change and takes a long time to return to its original value, possibly degrading the settling speed of the circuits biased by the reference generator. In other words, depending on the environment, it may be preferable to leave node *P* agile so that it can quickly recover from transients. In general, as depicted in Fig. 12.25, the response of the circuit must be analyzed by applying a disturbance at the output and observing the settling behavior.

**CB1 < CB2 < CB3**

**t**

Here is the image describtion:
```
The image depicts a circuit setup used for testing the transient response of a reference generator. The setup includes the following components:

1. **Reference Generator**: This is the main component being tested. It is connected to the rest of the circuit and is responsible for generating a reference signal.

2. **Capacitor**: Connected in series with the reference generator, the capacitor is used to filter or smooth the signal. It is depicted with the standard symbol for a capacitor.

3. **Voltage Source**: Represented by a circle with a plus and minus sign, indicating the positive and negative terminals, respectively. This voltage source is connected in parallel with the capacitor.

4. **Ground**: The circuit includes a ground connection, which is a common reference point for the voltages in the circuit.

5. **Output Voltage (Vout)**: The output voltage is taken across the capacitor and the voltage source. It is labeled as Vout and is connected to a ground symbol.

6. **Waveform**: The output voltage (Vout) is shown as a waveform, indicating the transient response of the reference generator. The waveform suggests that the output voltage varies over time, which is typical in transient response analysis.

7. **Square Wave Input**: There is a square wave symbol near the voltage source, indicating that the input to the reference generator might be a square wave signal. This is often used in testing to observe how the system responds to sudden changes in input.

The figure is labeled as "Figure 12.25" and is described as the setup for testing the transient response of a reference generator. The transient response refers to how the output voltage (Vout) changes over time in reaction to changes in the input signal.
```

#### ▲**Example 12.7**

Determine the small-signal output impedance of the bandgap reference shown in Fig. 12.23 and examine its behavior with frequency.

## **Solution**

Figure 12.26 depicts the equivalent circuit, modeling the open-loop op amp by a one-pole transfer function *A(s)* = *A*0*/(*1 + *s/*ω0*)* and an output resistance *Rout* and each bipolar transistor by a resistance 1*/gmN* . If *M*<sup>1</sup> and *M*<sup>2</sup> are identical, each having a transconductance of *gm P* , then their drain currents are equal to *gm P VX* , producing a differential voltage at the input of the op amp equal to

$$V\_{AB} = -g\_{mP} V\_X \frac{1}{g\_{mN}} + g\_{mP} V\_X \left(\frac{1}{g\_{mN}} + R\_1\right) \tag{12.55}$$

$$=\,\_{m}\mathbf{g}\_{m}\,V\_{X}\,\mathbf{R}\_{1}\tag{12.56}$$

Here is the image describtion:
```
The image depicts a small-signal equivalent circuit of a differential amplifier with active load. Here is a detailed description of the components and their connections:

1. **Transistors M1 and M2**: These are the two MOSFETs forming the differential pair. The sources of both transistors are connected to a common node, which is typically connected to a current source (not shown in the image).

2. **V_DD**: This is the positive supply voltage connected to the drains of both transistors M1 and M2.

3. **Node P**: This is the common drain node of transistors M1 and M2, connected to the output resistance \( R_{out} \).

4. **Output Resistance (R_out)**: This resistor is connected between node P and the output of the operational amplifier \( A(s) \).

5. **Operational Amplifier (A(s))**: This represents the gain stage of the amplifier. The inverting input (-) is connected to node A, and the non-inverting input (+) is connected to node B.

6. **Nodes A and B**: These are the input nodes of the operational amplifier. Node A is connected to the source of transistor M1, and node B is connected to the source of transistor M2.

7. **Resistors \( \frac{1}{g_{mN}} \) and \( \frac{1}{g_{mN}} + R_1 \)**: These resistors are connected to the sources of transistors M1 and M2, respectively. \( g_{mN} \) represents the transconductance of the transistors.

8. **Voltage Source \( V_X \)**: This is an external voltage source connected to the gate of transistor M2. It provides the differential input voltage \( V_X \).

9. **Current Source \( I_X \)**: This is the current flowing through the circuit due to the applied voltage \( V_X \).

10. **Transconductance \( g_{mP} \)**: This represents the transconductance of the transistors M1 and M2. The current through the transistors is given by \( g_{mP} V_X \).

In summary, the image shows a differential amplifier with an active load, where the differential input voltage \( V_X \) is applied to the gate of transistor M2, and the resulting differential current is amplified by the operational amplifier \( A(s) \). The output is taken from node P, which is connected to the drains of both transistors M1 and M2.
```

**Figure 12.26** Circuit for calculation of the output impedance of a reference generator.

The current flowing through *Rout* is therefore given by

$$I\_X = \frac{V\_X + g\_{mP} V\_X R\_1 A(s)}{R\_{out}} \tag{12.57}$$

yielding

$$\frac{V\_X}{I\_X} = \frac{R\_{out}}{1 + g\_{mP}R\_1A(s)}\tag{12.58}$$

$$=\frac{R\_{out}}{1+g\_{mP}R\_1\frac{A\_0}{1+s/\alpha\_0}}\tag{12.59}$$

$$\eta = \frac{R\_{out}}{1 + \, \_{g\,m\,P}R\_1A\_0} \frac{1 + \frac{s}{\alpha\_0}}{1 + \frac{s}{(1 + \, g\_{mP}R\_1A\_0)\alpha\_0}} \tag{12.60}$$

Thus, the output impedance exhibits a zero at ω<sup>0</sup> and a pole at *(*1 + *gm P R*<sup>1</sup> *A*0*)*ω0, with the magnitude behavior plotted in Fig. 12.27. Note that |*Zout*| is small for ω *<* ω0, but it rises to a high value as the frequency approaches the pole. In fact, setting ω = *(*1 + *gm P R*<sup>1</sup> *A*0*)*ω<sup>0</sup> and assuming *gm P R*<sup>1</sup> *A*<sup>0</sup> ) 1, we have

$$|Z\_{out}| = \frac{R\_{out}}{1 + g\_m \rho\_1 R\_1 A\_0} \left| \frac{1 + j\left(1 + g\_m \rho\_1 R\_1 A\_0\right)}{1 + j} \right| \tag{12.61}$$

$$= \frac{R\_{out}}{\sqrt{2}}\tag{12.62}$$

which is only 30% lower than the open-loop value.

Here is the image describtion:
```
The image is a graph that depicts the magnitude of the output impedance (\(|Z_{out}|\)) of a system as a function of angular frequency (\(\omega\)). The graph is plotted on a logarithmic scale for the frequency axis (\(\omega\)) and a linear scale for the impedance axis (\(|Z_{out}|\)).

Key features of the graph include:

1. **Y-Axis (|Zout|)**: This axis represents the magnitude of the output impedance. It is labeled as \(|Z_{out}|\).

2. **X-Axis (\(\omega\))**: This axis represents the angular frequency. It is labeled as \(\omega\).

3. **Horizontal Lines**:
   - The lowest horizontal line is labeled as \(\frac{R_{out}}{1 + g_m P R_1 A_0}\).
   - The middle horizontal line is labeled as \(\frac{R_{out}}{\sqrt{2}}\).
   - The highest horizontal line is labeled as \(R_{out}\).

4. **Vertical Lines**:
   - The first vertical line intersects the x-axis at \(\omega_0\).
   - The second vertical line intersects the x-axis at \((1 + g_m P R_1 A_0) \omega_0\).

5. **Curve**: The curve starts at the lowest horizontal line (\(\frac{R_{out}}{1 + g_m P R_1 A_0}\)) at low frequencies. As the frequency increases, the curve rises and transitions smoothly through the middle horizontal line (\(\frac{R_{out}}{\sqrt{2}}\)) at a frequency of \(\omega_0\). It continues to rise and eventually levels off at the highest horizontal line (\(R_{out}\)) at a frequency of \((1 + g_m P R_1 A_0) \omega_0\).

The graph illustrates how the output impedance changes with frequency, starting from a lower value at low frequencies, increasing through a mid-point, and reaching a higher value at high frequencies. The parameters \(R_{out}\), \(g_m\), \(P\), \(R_1\), and \(A_0\) are constants that define the behavior of the system.
```

Here is the image describtion:
```
The image is a caption for a figure labeled "Figure 12.27." The caption reads: "Variation of the reference generator output impedance with frequency." This suggests that the figure likely contains a graph or chart that illustrates how the output impedance of a reference generator changes as the frequency varies. However, the actual graph or chart is not visible in the provided image. The caption is written in a standard font, with "Figure 12.27" in bold, followed by the description in regular font.
```

▲

The output noise of reference generators may affect the performance of low-noise circuits considerably. Figure 12.28 illustrates an example: the load current source of a common-source stage is driven by a bandgap circuit with a current multiplication factor of *N*. Thus, the noise current of *M*<sup>1</sup> (or *M*2) is amplified by the same factor as it appears in *M*3. Note that *M*1–*M*<sup>3</sup> carry noise due to the op amp *A*<sup>1</sup> as well.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, which appears to be a part of an analog integrated circuit, possibly a current mirror or a differential amplifier with a current mirror load. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage, labeled as V_DD.

2. **Transistors**:
   - **M1, M2, M3, M4**: These are MOSFET transistors. M1 and M2 are connected in a differential pair configuration, with their sources tied together and connected to the drain of a current source transistor (Q1).
   - **Q1, Q2**: These are bipolar junction transistors (BJTs). Q1 is connected to a current source labeled "A" at its emitter, and Q2 is connected to a current source labeled "nA" at its emitter. The collectors of Q1 and Q2 are connected to the sources of M1 and M2, respectively.

3. **Operational Amplifier (A1)**: There is an operational amplifier (A1) with its inverting input (-) connected to the drain of M1 and its non-inverting input (+) connected to the drain of M2. The output of A1 is connected to the gate of M1.

4. **Resistor (R1)**: There is a resistor (R1) connected between the drain of M2 and the gate of M2.

5. **Output Stage**:
   - **M3**: The drain of M3 is connected to V_DD, and its source is connected to the output node (V_out).
   - **M4**: The gate of M4 is connected to the input voltage (V_in), and its source is connected to ground. The drain of M4 is connected to the gate of M3.

6. **Connections**:
   - The source of M1 and M2 are connected together and to the collector of Q1.
   - The drain of M1 is connected to the inverting input of A1.
   - The drain of M2 is connected to the non-inverting input of A1 and one end of R1.
   - The other end of R1 is connected to the gate of M2.
   - The source of M3 is connected to V_out.
   - The gate of M3 is connected to the drain of M4.
   - The source of M4 is connected to ground, and its gate is connected to V_in.

This circuit likely functions as a differential amplifier with a current mirror load, where the operational amplifier A1 ensures that the differential pair (M1 and M2) operates correctly. The output stage involving M3 and M4 forms a common-source amplifier with M4 acting as a voltage follower to drive the gate of M3.
```

**Figure 12.28** Effect of bandgap circuit noise on a CS stage.

As another example, if a high-precision A/D converter employs a bandgap voltage as the reference with which the analog input signal is compared (Fig. 12.29), then the noise in the reference is directly added to the input.

Here is the image describtion:
```
The image is a block diagram representing an Analog-to-Digital (A/D) conversion system. The diagram consists of three main components:

1. **A/D Converter**: This is the central block in the diagram. It has two inputs and one output.
   - The first input is labeled "V_in," which represents the analog input voltage that needs to be converted to a digital signal.
   - The second input comes from the "Reference Generator."
   - The output of the A/D Converter is labeled "Digital Output," indicating that the converter produces a digital representation of the analog input voltage.

2. **Reference Generator**: This block is connected to the A/D Converter. It provides a reference voltage or signal necessary for the A/D conversion process. The reference signal helps the A/D Converter to accurately convert the analog input voltage to a corresponding digital value.

3. **Connections**:
   - The "V_in" input is shown as a single line entering the A/D Converter.
   - The Reference Generator is connected to the A/D Converter with a line indicating the reference signal input.
   - The output of the A/D Converter is shown as a line leading to the "Digital Output," which signifies the final digital signal produced by the conversion process.

Overall, the diagram illustrates the basic components and connections involved in converting an analog signal to a digital output using an A/D Converter with a reference signal provided by a Reference Generator.
```

**Figure 12.29** A/D converter using a reference generator.

As a simple example, let us calculate the output noise voltage of the circuit shown in Fig. 12.30, taking into account only the input-referred noise voltage of the op amp, *Vn,op*. Since the small-signal drain currents of *<sup>M</sup>*<sup>1</sup> and *<sup>M</sup>*<sup>2</sup> are equal to *Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*, we have *VP* <sup>=</sup> <sup>−</sup>*g*−<sup>1</sup> *m P Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*, obtaining the differential voltage at the input of the op amp as <sup>−</sup>*g*−<sup>1</sup> *m P A*−<sup>1</sup> <sup>0</sup> *Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*. Beginning

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with an operational amplifier (op-amp) and MOSFET transistors. Here is a detailed description of the components and their connections:

1. **MOSFET Transistors (M1 and M2)**:
   - There are two MOSFET transistors labeled M1 and M2.
   - The sources of both M1 and M2 are connected to the positive supply voltage \( V_{DD} \).
   - The drains of M1 and M2 are connected to a common node labeled \( P \).

2. **Operational Amplifier (A0)**:
   - An operational amplifier (op-amp) is present in the circuit, labeled \( A_0 \).
   - The inverting input (−) of the op-amp is connected to node \( A \).
   - The non-inverting input (+) of the op-amp is connected to node \( B \).
   - The output of the op-amp is connected to node \( P \).

3. **Current Sources**:
   - There are two current sources represented by \( g_{mP} V_P \) connected to nodes \( A \) and \( B \).
   - The current source \( g_{mP} V_P \) at node \( A \) is connected to the drain of M1.
   - The current source \( g_{mP} V_P \) at node \( B \) is connected to the drain of M2.

4. **Resistors**:
   - There are two resistors connected to the sources of the MOSFETs.
   - The resistor connected to the source of M1 is labeled \( \frac{1}{g_{mN}} \) and is connected to ground.
   - The resistor connected to the source of M2 is labeled \( \frac{1}{g_{mN}} + R_1 \) and is also connected to ground.

5. **Voltage Sources**:
   - There is a voltage source labeled \( V_{n,op} \) connected between nodes \( B \) and \( V_{n,out} \).
   - The voltage at node \( B \) is labeled \( V_{n,op} \).
   - The voltage at the output node is labeled \( V_{n,out} \).

6. **Nodes**:
   - Node \( P \) is the common node where the drains of M1 and M2 and the output of the op-amp are connected.
   - Node \( A \) is connected to the inverting input of the op-amp and the current source \( g_{mP} V_P \).
   - Node \( B \) is connected to the non-inverting input of the op-amp, the current source \( g_{mP} V_P \), and the voltage source \( V_{n,op} \).

In summary, the circuit is a differential amplifier with an op-amp and MOSFETs, where the op-amp controls the voltage at the common node \( P \), and the current sources and resistors set the operating points of the MOSFETs. The output voltage \( V_{n,out} \) is taken from node \( B \).
```

**Figure 12.30** Circuit for calculation of noise in a reference generator.

## Sec. 12.7 Low-Voltage Bandgap References **529**

from node *A*, we can then write

Razavi-3930640 book December 17, 201517:21 529

$$\frac{V\_{n,out}}{R\_1 + g\_{mN}^{-1}} \cdot \frac{1}{g\_{mN}} - \frac{V\_{n,out}}{g\_{mP}A\_0 \left(R\_1 + g\_{mN}^{-1}\right)} = V\_{n,op} + V\_{n,out} \tag{12.63}$$

and hence

$$V\_{n,out} \left[ \frac{1}{R\_1 + g\_{mN}^{-1}} \left( \frac{1}{g\_{mN}} - \frac{1}{g\_{mP} A\_0} \right) - 1 \right] = V\_{n,op} \tag{12.64}$$

Since typically *gm P <sup>A</sup>*<sup>0</sup> ) *gmN* ) *<sup>R</sup>*−<sup>1</sup> <sup>1</sup> ,

$$|V\_{n,out}| \approx V\_{n,op} \tag{12.65}$$

suggesting that the noise of the op amp directly appears at the output. Note that even the addition of a large capacitor from the output to ground may not suppress low-frequency 1*/f* noise components, a serious difficulty in low-noise applications. The noise contributed by other devices in the circuit is studied in Problem 12.6.

## **12.7 Low-Voltage Bandgap References**

The bandgap voltage expressed by Eq. (12.20) is around 1.25 V, eluding implementation with today's low supplies. The fundamental limitation is that we must add about 17*.*2*VT* to one *VB E* so as to achieve a net zero temperature coefficient.

Is it possible to add two *currents* with positive and negative TCs and then convert the result to an arbitrary voltage that has a zero TC (Fig. 12.31)? Recall from Fig. 12.18 that we can readily generate a PTAT current given by *VT* ln *n/R*. We also envision another current of the form *VB E /R* serving as that with a negative TC, but how can we generate such a current with minimal complexity?

Here is the image describtion:
```
The image is a schematic diagram of an electrical circuit, specifically designed to illustrate the summation of two currents with opposite temperature coefficients (TC) to achieve a result with zero temperature coefficient. Here is a detailed description of the components and their arrangement in the circuit:

1. **Power Supply (V_DD)**: At the top of the diagram, there is a power supply labeled \( V_{DD} \).

2. **Resistor (R1)**: Connected to the power supply is a resistor labeled \( R_1 \). The positive terminal of the power supply is connected to one end of the resistor.

3. **Voltage Across Resistor (V)**: The voltage across the resistor \( R_1 \) is denoted as \( V \), and it is given by the equation \( V = (I_1 + I_2)R_1 \). This indicates that the voltage is the product of the total current flowing through the resistor and the resistance \( R_1 \).

4. **Current Sources (I1 and I2)**: Below the resistor, there are two current sources:
   - The first current source is labeled \( I_1 \) and has a positive temperature coefficient (TC > 0).
   - The second current source is labeled \( I_2 \) and has a negative temperature coefficient (TC < 0).

5. **Ground Connections**: Both current sources \( I_1 \) and \( I_2 \) are connected to the ground.

6. **Summation Point**: The point where the currents \( I_1 \) and \( I_2 \) combine is connected to the lower end of the resistor \( R_1 \).

7. **Temperature Coefficient (TC)**: The diagram indicates that the combined effect of the currents \( I_1 \) and \( I_2 \) results in a voltage \( V \) with zero temperature coefficient (TC = 0). This is achieved by summing the currents with opposite temperature coefficients, effectively canceling out the temperature dependence.

The accompanying text, "Figure 12.31 Summation of two currents with opposite TCs to obtain a result with zero TC," explains the purpose of the circuit, which is to balance the temperature coefficients of the two currents to achieve a stable voltage that does not vary with temperature.
```

Let us return to the circuit of Fig. 12.18, assume that *M*<sup>3</sup> and *M*<sup>4</sup> are identical, and note that |*ID*4| = *VT* ln *n/R*<sup>1</sup> is a PTAT current. We place a resistor in parallel with *Q*<sup>2</sup> as shown in Fig. 12.32(a). We recognize that *R*<sup>1</sup> now carries an additional current equal to |*VB E*2|*/R*2, i.e., a current with a negative TC. Unfortunately, however, the PTAT behavior is now disturbed because *IC*<sup>1</sup> =% *IC*2. Fortunately, a simple modification resolves this issue: as shown in Fig. 12.32(b), we tie *R*<sup>2</sup> from *Y* to ground and place another resistor in parallel with *Q*1. Proposed by Banba et al. [8], this topology lends itself to low-voltage implementation, requiring a minimum *VDD* of *VB E*<sup>1</sup> + |*VDS*3|.

To analyze the circuit, we observe that *VX* ≈ *VY* ≈ |*VB E*1| and *ID*<sup>3</sup> = *ID*4. Thus,

$$I\_{C1} + \frac{|V\_{BE1}|}{R\_3} = I\_{C2} + \frac{|V\_{BE1}|}{R\_2} \tag{12.66}$$

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each circuit features a combination of transistors, resistors, and an operational amplifier. Here is a detailed description of each circuit:

### Circuit (a):
1. **Transistors**:
   - Two PMOS transistors labeled M3 and M4 are connected at the top, with their sources connected to V_DD (positive supply voltage).
   - The drains of M3 and M4 are connected to nodes X and Y, respectively.
2. **Operational Amplifier**:
   - An operational amplifier labeled A1 is placed between nodes X and Y.
   - The inverting input (-) of A1 is connected to node X.
   - The non-inverting input (+) of A1 is connected to node Y.
3. **BJTs**:
   - Two NPN bipolar junction transistors (BJTs) labeled Q1 and Q2 are connected at the bottom.
   - The emitter of Q1 is grounded, and its base is connected to node A.
   - The emitter of Q2 is grounded, and its base is connected to node nA.
4. **Resistors**:
   - A resistor R1 is connected between node Y and the collector of Q2.
   - A resistor R2 is connected between the collector of Q2 and ground.

### Circuit (b):
1. **Transistors**:
   - Similar to circuit (a), it has two PMOS transistors labeled M3 and M4 connected at the top with their sources connected to V_DD.
   - The drains of M3 and M4 are connected to nodes X and Y, respectively.
2. **Operational Amplifier**:
   - The operational amplifier A1 is placed between nodes X and Y.
   - The inverting input (-) of A1 is connected to node X.
   - The non-inverting input (+) of A1 is connected to node Y.
3. **BJTs**:
   - Two NPN BJTs labeled Q1 and Q2 are connected at the bottom.
   - The emitter of Q1 is grounded, and its base is connected to node A.
   - The emitter of Q2 is grounded, and its base is connected to node nA.
4. **Resistors**:
   - A resistor R1 is connected between node Y and the collector of Q2.
   - A resistor R2 is connected between the collector of Q2 and ground.
   - An additional resistor R3 is connected between node X and ground.

### Circuit (c):
1. **Transistors**:
   - Similar to circuits (a) and (b), it has two PMOS transistors labeled M3 and M4 connected at the top with their sources connected to V_DD.
   - The drains of M3 and M4 are connected to nodes X and Y, respectively.
   - An additional PMOS transistor labeled M5 is connected with its source to V_DD and its drain to a node connected to resistor R4.
2. **Operational Amplifier**:
   - The operational amplifier A1 is placed between nodes X and Y.
   - The inverting input (-) of A1 is connected to node X.
   - The non-inverting input (+) of A1 is connected to node Y.
3. **BJTs**:
   - Two NPN BJTs labeled Q1 and Q2 are connected at the bottom.
   - The emitter of Q1 is grounded, and its base is connected to node A.
   - The emitter of Q2 is grounded, and its base is connected to node nA.
4. **Resistors**:
   - A resistor R1 is connected between node Y and the collector of Q2.
   - A resistor R2 is connected between the collector of Q2 and ground.
   - An additional resistor R3 is connected between node X and ground.
   - A resistor R4 is connected between the drain of M5 and ground, with a node labeled V_BG connected to the drain of M5.

Each circuit shows a different configuration of components, likely representing variations of a specific electronic design, possibly a bandgap reference or a similar analog circuit.
```

**Figure 12.32** (a) Attempt to make drain current of *M*<sup>4</sup> temperature-independent, (b) circuit modification resulting in a zero-TC current, and (c) generation of arbitrarily small voltage with zero TC.

which yields *IC*<sup>1</sup> = *IC*<sup>2</sup> if *R*<sup>2</sup> = *R*3. We still have |*VB E*1|=|*VB E*2| + *IC*2*R*<sup>1</sup> and hence *IC*<sup>2</sup> = *VT* ln *n/R*1. This current and the current flowing through *R*2, |*VB E*1|*/R*2, constitute |*ID*4|:

$$|I\_{D4}| = \frac{V\_T \ln n}{R\_1} + \frac{|V\_{BE1}|}{R\_2} \tag{12.67}$$

$$\eta = \frac{1}{R\_2} \left( |V\_{BE1}| + \frac{R\_2}{R\_1} V\_T \ln n \right) \tag{12.68}$$

Selecting *(R*2*/R*1*)VT* ln *n* approximately equal to 17*.*2*VT* renders a zero TC for *ID*4. This current is then copied and passed through a resistor to generate a zero-TC voltage [Fig. 12.32(c)] [8]:

$$V\_{BG} = \frac{R\_4}{R\_2} \left( |V\_{BE1}| + \frac{R\_2}{R\_1} V\_T \ln n \right) \tag{12.69}$$

(if *M*<sup>5</sup> is identical to *M*4). We choose *(R*2*/R*1*)*ln *n* ≈ 17*.*2, observing that *VBG* has a zero TC and its value can be lower than the conventional limit of 1.25 V.

#### ▲**Example 12.8**

If the op amp in Fig. 12.32(c) has an input-referred offset voltage, *VO S*, determine *VBG*.

Here is the image describtion:
```
The image depicts a bandgap voltage reference circuit, which is commonly used in analog integrated circuits to provide a stable reference voltage that is independent of temperature, power supply variations, and process variations. The circuit consists of several key components and connections:

1. **Transistors Q1 and Q2**: These are bipolar junction transistors (BJTs) with their emitters connected to ground. The base of Q1 is connected to node X, and the base of Q2 is connected to node Y. The collector of Q1 is connected to node X through resistor R3, and the collector of Q2 is connected to node Y through resistor R1.

2. **Resistors R1, R2, R3, and R4**: 
   - R1 is connected between node Y and the ground.
   - R2 is connected between node Y and the ground.
   - R3 is connected between node X and the ground.
   - R4 is connected between the output voltage V_BG and the ground.

3. **Operational Amplifier A1**: The op-amp A1 has its inverting input (-) connected to node Y and its non-inverting input (+) connected to node X. The output of the op-amp is connected to the gates of transistors M3 and M4.

4. **MOSFETs M3, M4, and M5**: 
   - M3 and M4 are NMOS transistors with their sources connected to ground and their gates connected to the output of the op-amp A1. The drains of M3 and M4 are connected to the power supply V_DD.
   - M5 is a PMOS transistor with its source connected to V_DD, its gate connected to the output of the op-amp A1, and its drain connected to the output voltage V_BG through resistor R4.

5. **Voltage Source V_DD**: This is the power supply voltage for the circuit.

6. **Output Voltage V_BG**: This is the bandgap reference voltage output of the circuit.

7. **Offset Voltage Vos**: This represents the offset voltage of the operational amplifier A1.

The circuit operates by generating a stable reference voltage (V_BG) that is independent of temperature variations. The op-amp A1 ensures that the voltage at node X is equal to the voltage at node Y, compensating for the base-emitter voltage differences of Q1 and Q2. The resistors and transistors are configured to create a temperature-independent voltage at the output V_BG.
```

#### **Solution**

As shown in Fig. 12.33, we now have *VX* ≈ *VY* + *VO S* ≈ |*VB E*<sup>1</sup>| and

$$I\_{C1} + \frac{|V\_{BE1}|}{R\_3} = I\_{C2} + \frac{|V\_{BE1}| - V\_{OS}}{R\_2} \tag{12.70}$$

which implies that *IC*<sup>1</sup> = *IC*<sup>2</sup> − *VO S/R*<sup>2</sup> if *R*<sup>2</sup> = *R*3. Since |*VB E*<sup>1</sup>|=|*VB E*<sup>2</sup>| + *R*<sup>1</sup> *IC*<sup>2</sup> + *VO S*, we have *IC*<sup>2</sup> = *(VT* ln *n* − *VO S)/R*1. This current and the current flowing through *R*2, *(*|*VB E*<sup>1</sup>| − *VO S)/R*2, add up to |*ID*<sup>4</sup>|:

$$|I\_{D4}| = \frac{V\_T \ln n - V\_{OS}}{R\_1} + \frac{|V\_{BE1}| - V\_{OS}}{R\_2} \tag{12.71}$$

It follows that

$$V\_{BG} = \frac{R\_4}{R\_2} \left( |V\_{BE1}| + \frac{R\_2}{R\_1} V\_T \ln n \right) - \frac{R\_4}{R\_1 || R\_2} V\_{OS} \tag{12.72}$$

revealing that the op amp offset is amplified by a factor of *R*4*/(R*1||*R*2*)*. Alternatively, we can write

$$V\_{BG} = \frac{R\_4}{R\_2} \left[ |V\_{BE1}| + \frac{R\_2}{R\_1} V\_T \ln n - \left( 1 + \frac{R\_2}{R\_1} \right) V\_{OS} \right] \tag{12.73}$$

concluding that the effect of *VO S* can be minimized only by maximizing *n*.

It is instructive to estimate the lowest supply voltage with which the circuit of Fig. 12.32(c) can operate properly. With large bipolar transistors and a small bias current, e.g., 10 *µ*A, the base-emitter voltage can be as low as 0.7 V. Similarly, wide PMOS devices allow a |*VDS*| of about 50 mV. The circuit can thus operate with a minimum *VDD* of around 0.75 V. In this case, *R*<sup>4</sup> tends to be a large resistor, e.g., 50 k', producing significant noise and requiring a bypass capacitor at the output. Also, if the PMOS drain currents are copied to generate a larger current, say, 0.5 mA, then their noise is amplified by the same factor. This noise contains thermal and flicker components due to the PMOS devices and the noise of the op amp. In Problem 12.24, we analyze the noise behavior of this circuit, but from Example 12.8, we observe that the op amp input noise is amplified by a factor of *R*4*/(R*1||*R*2*)*.

The op amp in Fig. 12.32(c) can be realized as a five-transistor OTA. Depicted in Fig. 12.34(a) is an example. The OTA design proceeds according to the following guidelines. (1) Large transistor dimensions are chosen so as to minimize their flicker noise and offset. (2) The gate-source voltage of *Ma* and *Mb*

▲

Here is the image describtion:
```
The image shows two different circuit diagrams, labeled (a) and (b), which appear to be configurations of differential amplifiers using MOSFETs and BJTs.

### Circuit (a):
1. **Transistors:**
   - **Q1 and Q2:** These are NPN bipolar junction transistors (BJTs) with their emitters connected to ground.
   - **Ma and Mb:** These are NMOS transistors forming a differential pair with their sources connected together and to a current source \( I_{SS} \).
   - **Mc and Md:** These are PMOS transistors forming a current mirror load for the differential pair.
   - **M3 and M4:** These are PMOS transistors connected as active loads for the differential pair.

2. **Connections:**
   - The base of Q1 is connected to node A, and the base of Q2 is connected to node nA.
   - The collector of Q1 is connected to node X, which is also connected to the drain of Ma and the gate of M3.
   - The collector of Q2 is connected to node Y, which is also connected to the drain of Mb and the gate of M4.
   - The sources of Mc and Md are connected to \( V_{DD} \), the positive supply voltage.
   - The gates of Mc and Md are connected together and to the drain of Mc, forming a current mirror.
   - The drain of M3 is connected to \( V_{DD} \), and the drain of M4 is connected to \( V_{DD} \).

3. **Resistors:**
   - \( R3 \) is connected between the base of Q1 and ground.
   - \( R1 \) is connected between the base of Q2 and ground.
   - \( R2 \) is connected between the collector of Q2 and ground.

4. **Current Source:**
   - \( I_{SS} \) is a current source connected to the common source node of Ma and Mb and to ground.

### Circuit (b):
1. **Transistors:**
   - **Q1:** This is an NPN BJT with its emitter connected to ground.
   - **Ma:** This is an NMOS transistor with its source connected to a current source \( I_{SS} \).
   - **Mc and Me:** These are PMOS transistors forming a current mirror load for the differential pair.
   - **M3:** This is a PMOS transistor connected as an active load for the differential pair.

2. **Connections:**
   - The base of Q1 is connected to node A.
   - The collector of Q1 is connected to node X, which is also connected to the drain of Ma and the gate of M3.
   - The source of Mc is connected to \( V_{DD} \), the positive supply voltage.
   - The gate of Mc is connected to the drain of Mc and to the gate of Me, forming a current mirror.
   - The drain of Me is connected to the drain of Ma.
   - The source of Me is connected to \( V_{DD} \).
   - The drain of M3 is connected to \( V_{DD} \).

3. **Resistors:**
   - \( R3 \) is connected between the base of Q1 and ground.

4. **Current Source:**
   - \( I_{SS} \) is a current source connected to the source of Ma and to ground.

### General Observations:
- Both circuits are differential amplifier configurations.
- Circuit (a) uses a more complex differential pair with two BJTs and two NMOS transistors, while circuit (b) uses a simpler configuration with one BJT and one NMOS transistor.
- Both circuits use PMOS transistors as active loads and current mirrors to provide high impedance loads for the differential pair.
- The current source \( I_{SS} \) is used to set the tail current for the differential pair in both circuits.
```

**Figure 12.34** (a) Implementation of low-voltage BG circuit using a five-transistor OTA, and (b) addition of start-up device.

plus the headroom required by *ISS* must not exceed |*VB E*1|. (3) The transistors are chosen long enough to yield a reasonable loop gain, e.g., 5 to 10.

The foregoing topology must incorporate a start-up mechanism. Otherwise, the circuit begins with *VX* = *VY* = 0, *Ma* and *Mb* remain off, and so do *M*<sup>3</sup> and *M*4. Since, with *VDD <* 1 V, the voltage difference between node *P* and node *X* is initially positive but finally negative (why?), we can tie a diode-connected NMOS transistor between these two nodes to ensure start-up [Fig. 12.34(b)]. Alternatively, the NMOS device can be connected between *X* and *VDD*.

Another low-voltage bandgap circuit can be derived from the topology of Fig. 12.20 by simply tying a resistor from the output node to ground [9]. Shown in Fig. 12.35, the circuit now allows some of *ID*<sup>5</sup> to flow through *R*3:

$$|I\_{D5}| = \frac{V\_{out}}{R\_3} + \frac{V\_{out} - |V\_{BE3}|}{R\_2} \tag{12.74}$$

If the PMOS devices are identical, |*ID*5| = *VT* ln *n/R*1, yielding

$$V\_{out} = \frac{R\_3}{R\_2 + R\_3} \left( |V\_{BE3}| + \frac{R\_2}{R\_1} V\_T \ln n \right) \tag{12.75}$$

The standard bandgap voltage is thus scaled down by a factor of *R*3*/(R*<sup>2</sup> + *R*3*)*. The reader is encouraged to compute the effect of the op amp offset at the output and compare the result with (12.72).

Here is the image describtion:
```
The image depicts a circuit diagram that appears to be a part of an analog electronic circuit, possibly a current mirror or a differential amplifier with an active load. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **Q1, Q2, Q3:** These are NPN bipolar junction transistors (BJTs). The emitters of all three transistors are connected to the ground.
   - **M3, M4, M5:** These are NMOS transistors. The source of M3 is connected to the drain of Q1, the source of M4 is connected to the drain of Q2, and the source of M5 is connected to the drain of Q3.

2. **Resistors:**
   - **R1:** Connected between the collector of Q2 and the ground.
   - **R2:** Connected between the drain of M5 and the output node (Vout).
   - **R3:** Connected between the output node (Vout) and the ground.

3. **Operational Amplifier (A1):**
   - The operational amplifier (A1) has its inverting input (-) connected to the drain of M3 and its non-inverting input (+) connected to the drain of M4.
   - The output of the operational amplifier (A1) is connected to the gate of M4.

4. **Power Supply:**
   - **VDD:** The positive power supply voltage is connected to the sources of M3, M4, and M5.

5. **Connections:**
   - The base of Q1 is connected to a node labeled "A."
   - The base of Q2 is connected to a node labeled "nA."
   - The base of Q3 is connected to the output node (Vout).
   - The drain of M5 is connected to the output node (Vout).

6. **Output:**
   - The output voltage (Vout) is taken from the node where the drain of M5, R2, and R3 are connected.

The circuit seems to be designed for current amplification or mirroring, with the operational amplifier ensuring that the voltage at the drains of M3 and M4 are equal, thus forcing the currents through Q1 and Q2 to be proportional. The output stage involving Q3 and M5 likely serves to provide the final output current or voltage.
```

**Figure 12.35** Alternative low-voltage BG circuit.

It is possible to add other bias branches to the foregoing circuits so as to provide curvature correction, but such schemes typically rely on trimming because the various mismatches within the circuit tend to shift the zero-TC temperature randomly. Other low-voltage bandgaps are described in [10].

## **12.8 Case Study**

In this section, we study a bandgap reference circuit designed for high-precision analog systems [7]. The reference generator incorporates the topology of Fig. 12.19, but with two series base-emitter voltages in each branch so as to reduce the effect of MOSFET mismatches. A simplified version of the core is depicted in Fig. 12.36, where the PMOS current mirror arrangement ensures equal collector currents for *Q*1–*Q*4. While requiring a high supply voltage, this design exemplifies issues that prove important in practice.

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, specifically a differential amplifier with active load. Here is a detailed description of the circuit:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The sources of M1 and M2 are connected together and to a current source (not shown in the image) through resistor R1.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair. The drains of M3 and M4 are connected to the drains of M1 and M2, respectively.
   - **M5 and M6:** These are PMOS transistors connected in a current mirror configuration. The source of M5 and M6 is connected to V_DD (the positive supply voltage). The gate of M5 is connected to the gate and drain of M6, forming the current mirror.
   - **Q1 and Q2:** These are bipolar junction transistors (BJTs) connected in a differential pair configuration. The emitters of Q1 and Q2 are connected together and to the resistor R1.
   - **Q3 and Q4:** These are additional BJTs connected to the inputs nA and A, respectively. The collectors of Q3 and Q4 are connected to the ground.

2. **Connections:**
   - The gates of M1 and M2 are the differential inputs of the amplifier.
   - The drains of M1 and M2 are connected to the drains of M3 and M4, respectively, forming the output nodes.
   - The sources of M3 and M4 are connected to the sources of M5 and M6, respectively, which are connected to V_DD.
   - The resistor R1 is connected between the common source of M1 and M2 and the common emitter of Q1 and Q2.
   - The bases of Q1 and Q2 are connected to the gates of M1 and M2, respectively.
   - The bases of Q3 and Q4 are connected to the inputs nA and A, respectively.

3. **Power Supply:**
   - The circuit is powered by a positive supply voltage V_DD.

4. **Inputs and Outputs:**
   - The differential inputs are applied to the gates of M1 and M2 and the bases of Q1 and Q2.
   - The outputs are taken from the drains of M1 and M2.

This circuit is a typical example of a differential amplifier with active load, which is commonly used in analog integrated circuits for amplifying small differential signals. The active load (M3 and M4) provides high gain and the current mirror (M5 and M6) ensures proper biasing and current distribution.
```

**Figure 12.36** Simplified core of the bandgap circuit reported in [7].

Channel-length modulation of the MOS devices in Fig. 12.36 still results in significant supply dependence. To resolve this issue, each branch can employ both NMOS and PMOS cascode topologies. Figure 12.37(a) shows an example in which the low-voltage cascode current mirror described in Chapter 5

Here is the image describtion:
```
The image shows two different circuit diagrams, labeled (a) and (b), which appear to be configurations of bipolar junction transistors (BJTs) and MOSFETs in a certain arrangement. Here is a detailed description of each circuit:

### Circuit (a):
1. **Power Supply**: Both circuits are powered by a voltage source labeled \( V_{DD} \) at the top.
2. **Transistors**: 
   - There are two BJTs at the bottom, labeled \( Q_1 \) and \( Q_2 \).
   - Above the BJTs, there are two sets of MOSFETs arranged in a cascode configuration.
3. **Biasing**:
   - The gates of the upper MOSFETs are connected to bias voltages \( V_{b1} \) and \( V_{b2} \).
   - The source of the upper MOSFETs is connected to the drain of the lower MOSFETs.
4. **Resistors**:
   - There is a resistor \( R_1 \) connected between the emitter of \( Q_1 \) and ground.
5. **Inputs and Outputs**:
   - The base of \( Q_1 \) is connected to an input labeled \( nA \).
   - The base of \( Q_2 \) is connected to an input labeled \( A \).
   - The emitters of both \( Q_1 \) and \( Q_2 \) are connected to ground.

### Circuit (b):
1. **Power Supply**: Similar to circuit (a), it is powered by \( V_{DD} \).
2. **Transistors**:
   - The same configuration of BJTs \( Q_1 \) and \( Q_2 \) at the bottom.
   - The same cascode configuration of MOSFETs above the BJTs.
3. **Biasing**:
   - The gates of the upper MOSFETs are connected to bias voltages.
4. **Resistors**:
   - There is a resistor \( R_1 \) connected between the emitter of \( Q_1 \) and ground.
   - Additional resistors \( R_2 \) and \( R_3 \) are connected in series between the drain of the upper MOSFETs and \( V_{DD} \).
5. **Currents**:
   - Currents \( I_1 \) and \( I_2 \) are indicated flowing through the resistors \( R_2 \) and \( R_3 \) respectively.
6. **Inputs and Outputs**:
   - The base of \( Q_1 \) is connected to an input labeled \( nA \).
   - The base of \( Q_2 \) is connected to an input labeled \( A \).
   - The emitters of both \( Q_1 \) and \( Q_2 \) are connected to ground.

### Summary:
Both circuits are similar in their basic structure, with BJTs at the bottom and MOSFETs in a cascode configuration above them. Circuit (b) includes additional resistors and current paths, which are not present in circuit (a). The inputs and outputs are labeled the same in both circuits, with \( nA \) and \( A \) as inputs to the bases of \( Q_1 \) and \( Q_2 \) respectively.
```

**Figure 12.37** (a) Addition of cascode devices to improve supply rejection; (b) use of self-biased cascode to eliminate *Vb*<sup>1</sup> and *Vb*2.

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, which appears to be a part of an analog integrated circuit, possibly an operational amplifier or a differential amplifier with additional stages. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - There are several MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) labeled as M2, M10, M11, and M9.
   - There are also bipolar junction transistors (BJTs) labeled as Q1, Q2, Q3, and Q4.

2. **Resistors:**
   - The circuit includes resistors labeled as R1, R2, R3, R4, R5, and R6.

3. **Power Supply:**
   - The circuit is powered by a voltage source labeled V_DD at the top of the diagram.

4. **Connections:**
   - The MOSFETs M2 and M10 are connected to the V_DD line.
   - The sources of M2 and M10 are connected to the drains of other MOSFETs and BJTs in the circuit.
   - The gates of M2 and M10 are connected to the same node, indicating they might be part of a current mirror or differential pair.
   - The BJTs Q1 and Q2 form a differential pair with their emitters connected through resistor R1 to ground.
   - The bases of Q1 and Q2 are connected to input signals labeled nA and A, respectively.
   - The collectors of Q1 and Q2 are connected to the drains of MOSFETs through resistors R2 and R3.
   - The MOSFET M11 is connected to the output of the differential pair and drives the gate of M9.
   - The MOSFET M9 is connected to the output stage, which includes an operational amplifier (A1).

5. **Operational Amplifier:**
   - The operational amplifier A1 has its inverting input (labeled E) connected to the node between R5 and the output of M9.
   - The non-inverting input (labeled F) is connected to the node between R4 and ground.
   - The output of the operational amplifier is labeled V_out.

6. **Additional Components:**
   - Resistors R5 and R4 are part of the feedback network for the operational amplifier.
   - Resistor R6 is connected to the source of M9 and ground.

Overall, the circuit appears to be a differential amplifier with a current mirror load, followed by an output stage that includes an operational amplifier for further amplification and feedback control. The use of both MOSFETs and BJTs suggests a mixed-signal design, leveraging the advantages of both types of transistors.
```

**Figure 12.38** Generation of a floating reference voltage.

is utilized. To obviate the need for *Vb*<sup>1</sup> and *Vb*2, this design actually introduces a "self-biased" cascode, shown in Fig. 12.37(b), where *R*<sup>2</sup> and *R*<sup>3</sup> sustain proper voltages to allow all MOSFETs to remain in saturation. This cascode topology is analyzed in Problem 12.7.

The bandgap circuit reported in [7] is designed to generate a *floating* reference. This is accomplished by the modification shown in Fig. 12.38, where the drain currents of *M*<sup>9</sup> and *M*<sup>10</sup> flow through *R*<sup>4</sup> and *R*5, respectively. Note that *M*<sup>11</sup> sets the gate voltage of *M*<sup>9</sup> at *VB E*<sup>4</sup> + *VG S*11, establishing a voltage equal to *VB E*<sup>4</sup> across *R*<sup>6</sup> if *M*<sup>9</sup> and *M*<sup>11</sup> are identical. Thus, *ID*<sup>9</sup> = *VB E*4*/R*6, yielding *VR*<sup>4</sup> = *VB E*4*(R*4*/R*6*)*. Also, if *M*<sup>10</sup> is identical to *M*2, then |*ID*10| = 2*(VT* ln *n)/R*1, and hence *VR*<sup>5</sup> = 2*(VT* ln *n)(R*5*/R*1*)*. Since the op amp ensures that *VE* ≈ *VF* , we have

$$V\_{out} = \frac{R\_4}{R\_6} V\_{BE4} + 2\frac{R\_5}{R\_1} V\_T \ln n \tag{12.76}$$

Proper choice of the resistor ratios and *n* therefore provides a zero temperature coefficient.

In order to further enhance the supply rejection, this design regulates the supply voltage of the core and the op amp. Illustrated in Fig. 12.39, the idea is to generate a local supply, *VDDL* , that is defined by a reference *VR*<sup>1</sup> and the ratio of *Rr*<sup>1</sup> and *Rr*<sup>2</sup> and hence remains relatively independent of the global supply voltage. But how is *VR*<sup>1</sup> itself generated? To minimize the dependence of *VR*<sup>1</sup> upon the supply,

Here is the image describtion:
```
The image depicts a circuit diagram that includes several key components:

1. **Operational Amplifier (Op-Amp)**: On the left side of the diagram, there is an operational amplifier with its non-inverting input (+) connected to a voltage source labeled \( V_{R1} \). The inverting input (-) is connected to a feedback loop from the output of the op-amp.

2. **Voltage Divider**: The output of the op-amp is connected to a voltage divider made up of two resistors, \( R_{r1} \) and \( R_{r2} \). The junction between these two resistors is connected to ground.

3. **Core**: The output of the op-amp also connects to a block labeled "Core". This block is connected to ground and has an output labeled \( V_{DDL} \).

4. **Second Operational Amplifier (A1)**: The output from the "Core" block is fed into another operational amplifier labeled \( A1 \). The non-inverting input (+) of \( A1 \) is connected to the output of the "Core" block, while the inverting input (-) is connected to ground.

5. **Ground Connections**: Multiple ground connections are present in the circuit, including the junction between \( R_{r1} \) and \( R_{r2} \), the "Core" block, and the inverting input of the second op-amp \( A1 \).

The circuit appears to be a feedback control system where the first op-amp regulates the voltage \( V_{DDL} \) through the "Core" block, and the second op-amp \( A1 \) might be used for further amplification or buffering of the signal.
```

**Figure 12.39** Regulation of the supply voltage of the core and op amp to improve supply rejection.

this voltage is established *inside* the core, as depicted in Fig. 12.40. In fact, *RM* is chosen such that *VR*<sup>1</sup> is a bandgap reference.

Figure 12.41 shows the overall implementation, omitting a few details for simplicity. A start-up circuit is also used. Operating from a 5-V supply, the reference generator produces a 2.00-V output while consuming 2.2 mW. The supply rejection is 94 dB at low frequencies, dropping to 58 dB at 100 kHz [7].

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, likely representing a part of an integrated circuit or a specific analog circuit design. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DDL} \) at the top of the diagram.

2. **Transistors:**
   - The circuit includes multiple MOSFET transistors, labeled \( M_9 \), \( M_{10} \), and \( M_{11} \).
   - There are also bipolar junction transistors (BJTs) labeled \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \).

3. **Resistors:**
   - Several resistors are present in the circuit, labeled \( R_1 \), \( R_2 \), \( R_3 \), \( R_4 \), \( R_5 \), and \( R_6 \).
   - There is also a resistor labeled \( R_M \) connected to a voltage source \( V_{R1} \).

4. **Current Sources:**
   - The circuit includes current sources labeled \( nA \), which are connected to the emitters of transistors \( Q_1 \) and \( Q_3 \).

5. **Operational Amplifier:**
   - An operational amplifier (op-amp) labeled \( A_1 \) is present in the circuit. The op-amp has inverting (-) and non-inverting (+) inputs, and an output labeled \( V_{out} \).
   - The inverting input is connected to node \( F \) through resistor \( R_4 \).
   - The non-inverting input is connected to node \( E \) through resistor \( R_5 \).

6. **Connections:**
   - The sources of the MOSFETs \( M_9 \) and \( M_{11} \) are connected to the emitters of BJTs \( Q_2 \) and \( Q_4 \), respectively.
   - The gates of the MOSFETs \( M_9 \) and \( M_{11} \) are connected to the same node, which is also connected to the collector of \( Q_2 \).
   - The drain of \( M_{11} \) is connected to the source of \( M_{10} \), and the drain of \( M_{10} \) is connected to \( V_{DDL} \).
   - The bases of \( Q_1 \) and \( Q_2 \) are connected to resistors \( R_2 \) and \( R_3 \), respectively.
   - The emitters of \( Q_1 \) and \( Q_3 \) are connected to the current sources \( nA \).

7. **Nodes:**
   - Nodes \( A \), \( E \), and \( F \) are significant points in the circuit, with node \( A \) being connected to the bases of \( Q_2 \) and \( Q_4 \).

This circuit appears to be a part of a differential amplifier or a similar analog circuit, with the op-amp \( A_1 \) providing feedback and amplification. The combination of MOSFETs and BJTs suggests a design that leverages the advantages of both types of transistors.
```

**Figure 12.40** Generation of *VR*1, used in Fig. 12.39.

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, which appears to be a bandgap voltage reference circuit with a start-up circuit. Here is a detailed description of the various components and their connections:

1. **Operational Amplifier (Op-Amp):**
   - There is an operational amplifier at the top left of the diagram. The non-inverting input (+) is connected to a voltage divider formed by resistors \( R_1 \) and \( R_2 \).
   - The output of the op-amp is connected to the gates of a series of PMOS transistors.

2. **PMOS Transistors:**
   - A series of PMOS transistors (M10, M11, and M9) are connected in a configuration that appears to be part of a current mirror or biasing network.
   - The source of M10 is connected to \( V_{DDL} \), and its drain is connected to the drain of M11.
   - The source of M11 is connected to the drain of M9, and the source of M9 is connected to ground through resistor \( R_6 \).

3. **Resistors:**
   - \( R_1 \) and \( R_2 \) form a voltage divider connected to the non-inverting input of the op-amp.
   - \( R_3 \) is connected between the drain of M11 and the base of transistor \( Q_2 \).
   - \( R_M \) is connected between the base of \( Q_1 \) and the emitter of \( Q_2 \).
   - \( R_4 \) and \( R_5 \) are connected to the inputs of another op-amp \( A_1 \) on the right side of the diagram.
   - \( R_6 \) is connected to the source of M9 and ground.

4. **BJTs (Bipolar Junction Transistors):**
   - \( Q_1 \) and \( Q_2 \) are NPN transistors with their emitters connected to ground through resistors \( R_1 \) and \( R_2 \), respectively.
   - \( Q_3 \) and \( Q_4 \) are also NPN transistors with their emitters connected to ground and their bases connected to the same node as \( Q_1 \) and \( Q_2 \).

5. **Start-up Circuit:**
   - The start-up circuit is enclosed in a dashed box on the left side of the diagram. It is connected to \( V_{DD} \) and ensures that the circuit starts up correctly by providing an initial current or voltage to the main circuit.

6. **Output Stage:**
   - The output stage consists of another op-amp \( A_1 \) with its inverting input (-) connected to the junction of resistors \( R_4 \) and \( R_5 \).
   - The non-inverting input (+) of \( A_1 \) is connected to the node labeled \( E \).
   - The output of \( A_1 \) is labeled \( V_{out} \).

7. **Connections and Nodes:**
   - The node labeled \( VR_1 \) is the voltage at the junction of \( R_1 \) and \( R_2 \).
   - The node labeled \( A \) is a common connection point for the bases of \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \).
   - The node labeled \( E \) is connected to the non-inverting input of \( A_1 \).
   - The node labeled \( F \) is connected to the inverting input of \( A_1 \).

Overall, this circuit is designed to provide a stable reference voltage that is independent of temperature and supply voltage variations, typically used in analog and mixed-signal integrated circuits.
```

**Figure 12.41** Overall circuit of the bandgap generator reported in [7].

# **References**

Razavi-3930640 book December 17, 201517:21 536

- [1] R. A. Blauschild et al., "A New NMOS Temperature-Stable Voltage Reference," *IEEE J. of Solid-State Circuits,* vol. 13, pp. 767–774, December 1978.
- [2] Y. P. Tsividis and R. W. Ulmer, "A CMOS Voltage Reference," *IEEE J. of Solid-State Circuits*, vol. 13, pp. 774– 778, December 1978.
- [3] D. Hilbiber, "A New Semiconductor Voltage Standard," *ISSCC Dig. of Tech. Papers*, pp. 32–33, February 1964.
- [4] K. E. Kujik, "A Precision Reference Voltage Source," *IEEE J. of Solid-State Circuits*, vol. 8, pp. 222–226, June 1973.
- [5] G. C. M. Meijer, P. C. Schmall, and K. van Zalinge, "A New Curvature-Corrected Bandgap Reference," *IEEE J. of Solid-State Circuits*, vol. 17, pp. 1139–1143, December 1982.
- [6] M. Gunawan et al., "A Curvature-Corrected Low-Voltage Bandgap Reference," *IEEE J. of Solid-State Circuits*, vol. 28, pp. 667–670, June 1993.
- [7] T. Brooks and A. L. Westwisk, "A Low-Power Differential CMOS Bandgap Reference," *ISSCC Dig. of Tech. Papers,* pp. 248–249, February 1994.
- [8] H. Banba et al., "A CMOS Bandgap Reference Circuit with Sub-1-V Operation," *IEEE J. of Solid-State Circuits*, vol. 34, pp. 670–674, May 1999.
- [9] H. Neuteboom et al., "A DSP-Based Hearing Instrument IC," *IEEE J. of Solid-State Circuits*, vol. 32, pp. 1790– 1806, November 1997.
- [10] C. J. B. Fayomi et al., "Sub-1-V CMOS Bandgap Reference Design Techniques: A Survey," *Analog Integrated Circuits and Signal Processing*, vol. 62, pp. 141–157, February 2010.
- [11] B. Gilbert, "Monolithic Voltage and Current References: Themes and Variations," pp. 269–352 in *Analog Circuit Design*, J. H. Huijsing, R. J. van de Plassche, and W. M. C. Sansen, eds. (Boston: Kluwer Academic Publishers, 1996).

# **Problems**

Unless otherwise stated, in the following problems, use the device data shown in Table 2.1 and assume that *VDD* = 3 V where necessary.

**12.1.** Derive an expression for *Iout* in Fig. 12.42.

Here is the image describtion:
```
The image depicts a MOSFET-based current mirror circuit. Here is a detailed description of the circuit:

1. **Transistors**: The circuit consists of four MOSFET transistors labeled M1, M2, M3, and M4.
   - M1 and M2 are NMOS transistors.
   - M3 and M4 are PMOS transistors.

2. **Power Supply**: The circuit is powered by a voltage source labeled V_DD, which is connected to the drain terminals of M3 and M4.

3. **Current Source**: There is a resistor labeled R_S connected between the source of M1 and ground. This resistor is used to set the reference current through M1.

4. **Connections**:
   - The gate of M1 is connected to the gate of M2.
   - The drain of M1 is connected to the drain of M3.
   - The source of M1 is connected to one end of R_S, with the other end of R_S connected to ground.
   - The source of M2 is connected to ground.
   - The drain of M2 is connected to the drain of M4.
   - The gate of M3 is connected to the gate of M4.
   - The source of M3 and M4 are connected to V_DD.

5. **Output Current**: The output current, I_out, is taken from the drain of M2.

6. **Operation**: 
   - The current through M1 (set by R_S) is mirrored to M2.
   - M3 and M4 form a current mirror that ensures the same current flows through M1 and M2.
   - The current through M2 (I_out) is ideally equal to the current through M1.

This circuit is commonly used in analog integrated circuits to generate a stable current reference or to mirror currents from one branch of the circuit to another.
```

- **Figure 12.42**
- **12.2.** Explain how the start-up circuit shown in Fig. 12.43 operates. Derive a relationship that guarantees that *VX < VT H* after the circuit turns on.
- **12.3.** Consider the circuit of Fig. 12.15.
	- **(a)** If *M*<sup>1</sup> and *M*<sup>2</sup> suffer from channel-length modulation, what is the error in the output voltage?
	- **(b)** Repeat part (a) for *M*<sup>3</sup> and *M*4.
	- **(c)** If *M*<sup>1</sup> and *M*<sup>2</sup> have a threshold mismatch of !*V*, i.e., *VT H*<sup>1</sup> = *VT H* and *VT H*<sup>2</sup> = *VT H* + !*V*, what is the error in the output voltage?
	- **(d)** Repeat part (c) for *M*<sup>3</sup> and *M*4.