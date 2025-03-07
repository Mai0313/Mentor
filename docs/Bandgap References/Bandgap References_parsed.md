# CHAPTER

Razavi-3930640 book December 17, 201517:21 509

Here is the image describtion:
```
The image shows the number "12" in white, centered on a solid dark gray background. The font used is simple and sans-serif, making the number clear and easy to read. The overall design is minimalistic, with no additional elements or decorations present in the image.
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
The image consists of two circuit diagrams labeled (a) and (b).

(a) The circuit diagram on the left features three MOSFET transistors labeled M1, M2, and M3. The source of M1 is connected to ground, and its gate is connected to a current source labeled I_REF. The drain of M1 is connected to the positive supply voltage V_DD. The gate of M2 is connected to the drain of M1, and the source of M2 is connected to ground. The drain of M2 is connected to the gate of M3. The source of M3 is also connected to ground, and its drain is connected to the positive supply voltage V_DD. The currents through M2 and M3 are labeled I_D2 and I_D3, respectively.

(b) The circuit diagram on the right features two MOSFET transistors labeled M1 and M2. The source of M1 is connected to ground, and its gate is connected to a current source labeled I_REF. The drain of M1 is connected to the positive supply voltage V_DD through a resistor labeled R1. The gate of M2 is connected to the drain of M1, and the source of M2 is connected to ground. The drain of M2 is connected to the positive supply voltage V_DD. The current through M2 is labeled I_out.

Both circuits are examples of current mirror configurations, with (a) showing a more complex arrangement involving three transistors and (b) showing a simpler arrangement with two transistors and a resistor.
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

- M1 and M2 are NMOS transistors, with their sources connected to the ground.
- M3 and M4 are PMOS transistors, with their sources connected to the supply voltage \( V_{DD} \).
- The gate of M1 is connected to the gate of M2, and similarly, the gate of M3 is connected to the gate of M4.
- The drain of M1 is connected to the gate of M3 and the source of M4.
- The drain of M2 is connected to the gate of M4 and the source of M3.
- The current \( I_{REF} \) flows through M1, and the current \( I_{out} \) flows through M2.
- The width-to-length ratios of the transistors are indicated as \( \left( \frac{W}{L} \right)_N \) for NMOS transistors and \( \left( \frac{W}{L} \right)_P \) for PMOS transistors, with a scaling factor \( K \) applied to the transistors M2 and M3.

The circuit is designed to create a stable current that is independent of the supply voltage \( V_{DD} \).
```

supply-independent currents.

Since *Iout* and *IREF* in Fig. 12.2 display little dependence on *VDD*, their magnitude is set by other parameters. How do we calculate these currents? Interestingly, if *M*1–*M*<sup>4</sup> operate in saturation and λ ≈ 0, then the circuit is governed by only one equation, *Iout* = *K IREF* , and hence can support *any* current level! For example, if we initially force *IREF* to be 10 *µ*A, the resulting *Iout* of *K* × 10 *µ*A "circulates" around the loop, sustaining these current levels in the left and right branches indefinitely.

To uniquely define the currents, we add another constraint to the circuit, e.g., as shown in Fig. 12.3(a). Here, resistor *RS* decreases the current of *M*<sup>2</sup> while the PMOS devices require that *Iout* = *IREF* because they have identical dimensions and thresholds. We can write *VG S*<sup>1</sup> = *VG S*<sup>2</sup> + *ID*2*RS*, or

$$\sqrt{\frac{2I\_{\text{out}}}{\mu\_{n}\text{C}\_{ox}(W/L)\_{N}}} + V\_{TH1} = \sqrt{\frac{2I\_{\text{out}}}{\mu\_{n}\text{C}\_{ox}K(W/L)\_{N}}} + V\_{TH2} + I\_{\text{out}}R\_{S} \tag{12.2}$$

Neglecting body effect, we have

$$\sqrt{\frac{2I\_{\text{out}}}{\mu\_n C\_{ox}(W/L)\_N}} \left(1 - \frac{1}{\sqrt{K}}\right) = I\_{\text{out}} R\_S \tag{12.3}$$

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams depict current mirror circuits, which are commonly used in analog integrated circuits to copy current from one active device to another.

### Diagram (a):
- **Transistors**: The circuit includes four MOSFETs labeled M1, M2, M3, and M4.
  - M1 and M2 are NMOS transistors.
  - M3 and M4 are PMOS transistors.
- **Connections**:
  - The source of M1 is connected to the ground.
  - The drain of M1 is connected to the gate of M1 and the gate of M2.
  - The source of M2 is also connected to the ground.
  - The drain of M2 is connected to a resistor labeled Rs, which is connected to the ground.
  - The drain of M1 is connected to the source of M3.
  - The drain of M3 is connected to the source of M4.
  - The drain of M4 is connected to V_DD (the positive supply voltage).
  - The gate of M3 is connected to the gate of M4.
  - The output current I_out is taken from the drain of M2.
- **Labels**:
  - The width-to-length ratios of the transistors are indicated as (W/L)_N for NMOS and (W/L)_P for PMOS.
  - I_REF is the reference current flowing through M1.
  - K is a scaling factor for the width-to-length ratio of M2.

### Diagram (b):
- **Transistors**: Similar to diagram (a), this circuit also includes four MOSFETs labeled M1, M2, M3, and M4.
  - M1 and M2 are NMOS transistors.
  - M3 and M4 are PMOS transistors.
- **Connections**:
  - The source of M1 is connected to the ground.
  - The drain of M1 is connected to the gate of M1 and the gate of M2.
  - The source of M2 is also connected to the ground.
  - The drain of M2 is connected to the drain of M3.
  - The source of M3 is connected to a resistor labeled Rs, which is connected to V_DD.
  - The drain of M3 is connected to the source of M4.
  - The drain of M4 is connected to V_DD.
  - The gate of M3 is connected to the gate of M4.
  - The output current I_out is taken from the drain of M2.
- **Labels**:
  - The width-to-length ratios of the transistors are indicated as (W/L)_N for NMOS and (W/L)_P for PMOS.
  - I_REF is the reference current flowing through M1.
  - K is a scaling factor for the width-to-length ratio of M3.

### Summary:
Both diagrams illustrate current mirror circuits with slight variations in their configurations. Diagram (a) uses a resistor Rs connected to the source of M2, while diagram (b) uses a resistor Rs connected to the source of M3. The purpose of these circuits is to replicate the reference current I_REF through the output current I_out, with the scaling factor K determining the proportionality between the two currents.
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
The image depicts an electronic circuit diagram featuring a MOSFET-based amplifier configuration. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a DC voltage source labeled V_DD, with its positive terminal connected to the top horizontal line and the negative terminal grounded.

2. **Transistors (M4 and M2)**: The circuit includes two MOSFET transistors:
   - **M4**: The drain of M4 is connected to the power supply line (V_DD). The source of M4 is connected to a node that also connects to the drain of M2.
   - **M2**: The source of M2 is connected to a resistor labeled R_S, which is grounded. The gate of M2 is connected to a node that also connects to the drain of M4.

3. **Resistors**:
   - **R1**: Connected between the node labeled X and ground.
   - **R3**: Connected between the power supply line (V_DD) and the node where the drain of M2 and the source of M4 meet.
   - **R_S**: Connected between the source of M2 and ground.
   - **r_o2**: Connected between the node where the drain of M2 and the source of M4 meet and the source of M2.
   - **r_o4**: Connected between the drain of M4 and the power supply line (V_DD).

4. **Current Source (I_out)**: The output current, labeled I_out, is taken from the node where the drain of M2 and the source of M4 meet.

5. **Node X**: This node is connected to the gate of M4 and the resistor R1.

The circuit appears to be a type of amplifier, possibly a cascode amplifier, which is known for its high gain and high output impedance. The use of MOSFETs (M4 and M2) and the arrangement of resistors suggest that the circuit is designed to amplify an input signal applied at node X, with the amplified output current (I_out) taken from the node where the drain of M2 and the source of M4 meet.
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
The image consists of two parts labeled (a) and (b).

(a) The left part of the image shows a schematic diagram of an electronic circuit. The circuit includes five MOSFET transistors labeled M1, M2, M3, M4, and M5. The transistors M3 and M4 are connected to the positive supply voltage V_DD at their drains. The source of M1 is connected to the ground, while the source of M2 is connected to a resistor labeled R_S, which is also connected to the ground. The gate of M1 is connected to the drain of M2, and the gate of M2 is connected to the drain of M1. The transistor M5 is connected between the gates of M1 and M2, forming a feedback loop. The circuit appears to be a differential amplifier or a similar analog circuit.

(b) The right part of the image shows a graph with the vertical axis labeled I_D2 (representing the drain current of transistor M2) and the horizontal axis labeled V_DD (representing the supply voltage). The graph depicts a curve that starts at the origin (0,0), rises steeply, and then levels off, indicating the relationship between the drain current I_D2 and the supply voltage V_DD. A point on the curve is labeled "Degenerate Point," which likely indicates a critical operating point of the circuit.

Overall, the image illustrates an electronic circuit and its corresponding characteristic curve, highlighting the behavior of the circuit with respect to changes in the supply voltage.
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
The image depicts a differential amplifier circuit using bipolar junction transistors (BJTs). Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a voltage source labeled \( V_{DD} \) at the top of the diagram.

2. **Current Sources**: There are two current sources in the circuit:
   - The left current source is labeled \( nI_0 \).
   - The right current source is labeled \( I_0 \).

3. **Transistors**: The circuit includes two NPN bipolar junction transistors:
   - The left transistor is labeled \( Q_1 \).
   - The right transistor is labeled \( Q_2 \).

4. **Connections**:
   - The collector of \( Q_1 \) is connected to the current source \( nI_0 \) and then to \( V_{DD} \).
   - The collector of \( Q_2 \) is connected to the current source \( I_0 \) and then to \( V_{DD} \).
   - The emitters of both \( Q_1 \) and \( Q_2 \) are connected to the ground.

5. **Base Terminals**:
   - The base of \( Q_1 \) is connected to a node marked with a plus sign (+).
   - The base of \( Q_2 \) is connected to a node marked with a minus sign (−).

6. **Voltage Difference (\( \Delta V_{BE} \))**: The voltage difference between the bases of \( Q_1 \) and \( Q_2 \) is labeled as \( \Delta V_{BE} \).

This differential amplifier circuit is designed to amplify the difference in voltage (\( \Delta V_{BE} \)) between the bases of the two transistors \( Q_1 \) and \( Q_2 \). The current sources \( nI_0 \) and \( I_0 \) help in setting the operating point of the transistors.
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
The image depicts an electronic circuit diagram, specifically a current mirror circuit with bipolar junction transistors (BJTs). Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a voltage source labeled \( V_{DD} \) at the top of the diagram.

2. **Current Sources**: 
   - On the left side, there is a current source labeled \( nI_0 \).
   - On the right side, there is another current source labeled \( I_0 \).

3. **Transistors**:
   - There are two NPN bipolar junction transistors, labeled \( Q_1 \) and \( Q_2 \).
   - The base of \( Q_1 \) is connected to the base of \( Q_2 \), and this common node is also connected to the collector of \( Q_1 \).

4. **Emitter Connections**:
   - The emitter of \( Q_1 \) is connected to ground through a current labeled \( I_S \).
   - The emitter of \( Q_2 \) is connected to ground through a current labeled \( mI_S \).

5. **Voltage Difference**:
   - There is a voltage difference \( \Delta V_{BE} \) indicated between the bases of \( Q_1 \) and \( Q_2 \), with the positive side on \( Q_1 \) and the negative side on \( Q_2 \).

6. **Collector Connections**:
   - The collector of \( Q_1 \) is connected to the current source \( nI_0 \).
   - The collector of \( Q_2 \) is connected to the current source \( I_0 \).

7. **Ground Connections**:
   - The emitters of both transistors \( Q_1 \) and \( Q_2 \) are connected to ground.

The circuit is likely used to generate a precise current ratio between \( Q_1 \) and \( Q_2 \) based on the current sources and the properties of the transistors. The notation \( mI_S \) suggests that the current through \( Q_2 \) is a multiple \( m \) of the current \( I_S \) through \( Q_1 \). The figure is labeled as "Figure 12.7".
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
The image contains two figures, Figure 12.8 and Figure 12.9, which illustrate concepts related to the generation of temperature-independent voltage.

**Figure 12.8: Conceptual generation of temperature-independent voltage**
- This figure shows a simple circuit with two transistors, Q1 and Q2.
- Both transistors have their emitters connected to the ground.
- The base-emitter voltages are labeled as V_BE1 for Q1 and V_BE2 for Q2.
- The collector of Q1 is connected to a current source labeled "I" and to a node labeled V_O1.
- The collector of Q2 is connected to another current source labeled "I" and to a resistor "R" which is connected to a node labeled V_O2.
- The current source and resistor are connected to a supply voltage labeled V_DD.
- The base of Q1 is connected to a point labeled "A" and the base of Q2 is connected to a point labeled "nA".

**Figure 12.9: Actual implementation**
- This figure shows a more detailed circuit implementation.
- It includes two transistors, Q1 and Q2, similar to Figure 12.8.
- The emitters of Q1 and Q2 are connected to the ground.
- The bases of Q1 and Q2 are connected to points labeled "A" and "nA" respectively.
- The collector of Q1 is connected to a resistor R1 and the collector of Q2 is connected to a resistor R2.
- The resistors R1 and R2 are connected to a node labeled "Y".
- An operational amplifier (A1) is included in the circuit with its non-inverting input connected to the node "Y".
- The inverting input of the operational amplifier is connected to a resistor R3 and a voltage source labeled V_T ln n.
- The output of the operational amplifier is labeled V_out and is connected to the ground.

These figures illustrate the conceptual and practical approaches to generating a temperature-independent voltage using transistors and operational amplifiers.
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
The image depicts a cross-sectional view of a semiconductor structure, specifically a PNP bipolar junction transistor (BJT) integrated within a p-type substrate. The structure includes the following key components:

1. **P-Substrate**: The base material of the semiconductor, which is of p-type doping.

2. **N-Well**: A region within the p-substrate that is doped with n-type impurities, creating an n-type well.

3. **P+ Regions**: Heavily doped p-type regions within the n-well and p-substrate. There are two p+ regions shown:
   - One p+ region is located within the n-well and is connected to the emitter (E).
   - Another p+ region is located outside the n-well and is connected to the collector (C).

4. **N+ Region**: A heavily doped n-type region within the n-well, connected to the base (B).

5. **Contacts**: Metal contacts are shown connected to each of the regions:
   - The collector (C) contact is connected to the p+ region outside the n-well.
   - The emitter (E) contact is connected to the p+ region within the n-well.
   - The base (B) contact is connected to the n+ region within the n-well.

The diagram illustrates the typical layout of a PNP transistor, where the emitter (E) is p-type, the base (B) is n-type, and the collector (C) is p-type. The n-well serves to isolate the p+ emitter and n+ base regions from the p-type substrate.
```

**Figure 12.10** Realization of a *pnp* bipolar transistor in CMOS technology.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) labeled as A1. The circuit includes three resistors, labeled R1, R2, and R3, and two transistors, labeled Q1 and Q2.

Here is a detailed description of the circuit:

1. **Resistors:**
   - **R1** is connected between a node labeled X and the positive supply voltage.
   - **R2** is connected between a node labeled Y and the positive supply voltage.
   - **R3** is connected between node Y and the emitter of transistor Q2.

2. **Transistors:**
   - **Q1** is an NPN transistor with its collector connected to node X, its base connected to a node labeled A, and its emitter connected to ground.
   - **Q2** is an NPN transistor with its collector connected to node Y, its base connected to a node labeled nA, and its emitter connected to ground.

3. **Operational Amplifier (A1):**
   - The non-inverting input (+) of the op-amp is connected to node Y.
   - The inverting input (-) of the op-amp is connected to node X.
   - The output of the op-amp is labeled as Vout and is connected to a node with a ground symbol.

The circuit appears to be a differential amplifier configuration, where the op-amp amplifies the difference between the voltages at nodes X and Y. The transistors Q1 and Q2 are likely used to control the voltages at nodes X and Y, respectively, based on the input signals at nodes A and nA.
```

**Figure 12.11** Circuit of Fig. 12.9 implemented with *pnp* transistors.

**Op Amp Offset and Output Impedance** As explained in Chapter 14, owing to asymmetries, op amps suffer from input "offsets," i.e., the output voltage of the op amp is not zero if the input is set to zero. The input offset voltage of the op amp in Fig. 12.9 introduces error in the output voltage. Included in Fig. 12.12, the effect is quantified as *VB E*<sup>1</sup> − *VO S* ≈ *VB E*<sup>2</sup> + *R*<sup>3</sup> *IC*<sup>2</sup> (if *A*<sup>1</sup> is large) and *Vout* = *VB E*<sup>2</sup> +*(R*<sup>3</sup> + *R*2*)IC*2. Thus,

$$V\_{out} = V\_{BE2} + (R\_3 + R\_2)\frac{V\_{BE1} - V\_{BE2} - V\_{OS}}{R\_3} \tag{12.32}$$

$$\dot{\lambda} = V\_{BE2} + \left(1 + \frac{R\_2}{R\_3}\right) (V\_T \ln n - V\_{OS}) \tag{12.33}$$

where we have assumed that *IC*<sup>2</sup> ≈ *IC*<sup>1</sup> despite the offset voltage. The key point here is that *VO S* is amplified by 1+ *R*2*/R*3, introducing error in *Vout* . More important, as explained in Chapter 14, *VO S* itself varies with temperature, raising the temperature coefficient of the output voltage.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) labeled as A1. Here is a detailed description of the components and their connections:

1. **Resistors:**
   - **R1**: Connected to node X.
   - **R2**: Connected between node Y and the inverting input (-) of the op-amp A1.
   - **R3**: Connected between node Y and the non-inverting input (+) of the op-amp A1.

2. **Transistors:**
   - **Q1**: An NPN transistor with its emitter connected to ground and its base connected to node X.
   - **Q2**: Another NPN transistor with its emitter connected to ground and its base connected to node Y.

3. **Voltage Source:**
   - **Vos**: A voltage source connected between the non-inverting input (+) of the op-amp A1 and node Y.

4. **Operational Amplifier (A1):**
   - The op-amp has its inverting input (-) connected to node Y through resistor R2.
   - The non-inverting input (+) is connected to node Y through resistor R3 and to the voltage source Vos.
   - The output of the op-amp is labeled as Vout, which is connected to a ground symbol indicating a reference point.

5. **Nodes:**
   - **X**: A node where R1, the base of Q1, and the left side of the circuit meet.
   - **Y**: A node where R2, R3, the base of Q2, and the voltage source Vos meet.

6. **Ground Connections:**
   - The emitters of both transistors Q1 and Q2 are connected to ground.
   - The output Vout is also referenced to ground.

The circuit appears to be a differential amplifier configuration with transistors Q1 and Q2, resistors R1, R2, and R3, and an op-amp A1. The voltage source Vos introduces an offset voltage to the non-inverting input of the op-amp.
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
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) and a set of transistors. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1)**:
   - The op-amp is labeled as A1.
   - It has two input terminals: the inverting input (-) and the non-inverting input (+).
   - The output of the op-amp is labeled as Vout.

2. **Resistors**:
   - There are three resistors in the circuit.
   - Resistor R1 is connected between point X and the inverting input of the op-amp. It is labeled with a resistance value of R.
   - Resistor R2 is connected between the output of the op-amp and the inverting input. It is labeled with a resistance value of mR.
   - Resistor R3 is connected between the inverting input of the op-amp and point Y.

3. **Transistors**:
   - There are four transistors labeled Q1, Q2, Q3, and Q4.
   - Q1 and Q2 form a pair, with their emitters connected to ground and their collectors connected to point X.
   - Q3 and Q4 form another pair, with their emitters connected to ground and their collectors connected to point Y.
   - The bases of Q1 and Q2 are connected together and labeled as point A.
   - The bases of Q3 and Q4 are connected together and labeled as point nA.

4. **Currents**:
   - The current flowing through Q1 and Q2 is labeled as I1.
   - The current flowing through Q3 and Q4 is labeled as I2.

5. **Voltage Source**:
   - There is a voltage source labeled as Vos connected between the non-inverting input of the op-amp and ground.

6. **Ground Connections**:
   - The circuit has multiple ground connections, indicated by the ground symbols.

The circuit appears to be a differential amplifier configuration with transistors used for current mirroring or amplification purposes. The resistors R1 and R2 set the gain of the amplifier, while R3 and the transistors help in controlling the currents I1 and I2. The voltage source Vos introduces an offset voltage to the non-inverting input of the op-amp.
```

**Figure 12.13** Reduction of the effect of op amp offset.

Thus, the effect of the offset voltage is reduced by increasing the first term in the square brackets. The issue, however, is that *Vout* ≈ 2 × 1*.*25 V = 2*.*5 V, a value difficult to generate by the op amp at low supply voltages.

In the circuits studied above, the op amp drives two resistive branches and must therefore provide a low output impedance. Fortunately, it is possible to avoid this issue by a simple modification described below.

The implementation of Fig. 12.13 is not feasible in a standard CMOS technology because the collectors of *Q*<sup>2</sup> and *Q*<sup>4</sup> are not grounded. In order to utilize the bipolar structure shown in Fig. 12.10, we modify the series combination of the diodes as illustrated in Fig. 12.14(a), converting one of the diodes to an emitter follower. However, we must ensure that the bias currents of both transistors have the same behavior with temperature. Thus, we bias each transistor by a PMOS current source rather than a resistor [Fig. 12.14(b)]. The overall circuit then assumes the topology shown in Fig. 12.15, where the op amp adjusts the gate voltage of the PMOS devices so as to equalize *VX* and *VY* . Interestingly, in this circuit, the op amp experiences no resistive loading, but the mismatch and channel-length modulation of the PMOS devices introduce error at the output (Problem 12.3).

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b), each depicting different transistor circuit configurations.

(a) The left side of the image shows two equivalent representations of a simple transistor circuit. The first representation on the far left includes two NPN bipolar junction transistors (BJTs), labeled Q1 and Q2. The emitters of both transistors are connected to the ground. The collector of Q1 is connected to the base of Q2, and the collector of Q2 is connected to a node labeled 2V_BE. The base of Q1 is connected to the collector of Q2, forming a feedback loop. The second representation on the right side of (a) simplifies the circuit by showing Q1 and Q2 in a more straightforward configuration, with the same connections: the emitters to ground, the collector of Q1 to the base of Q2, and the collector of Q2 to the node labeled 2V_BE.

(b) The right side of the image shows a more complex transistor circuit. It includes two NPN BJTs, Q1 and Q2, similar to part (a). The emitters of both transistors are connected to the ground. The collector of Q1 is connected to the base of Q2, and the collector of Q2 is connected to a node labeled 2V_BE. Additionally, there is a power supply voltage V_DD connected to the top of the circuit. Two capacitors are connected in series between V_DD and a node labeled V_b. The node V_b is connected to the base of Q2. The circuit also includes a connection from the node labeled 2V_BE to the base of Q2.

Overall, the image illustrates different configurations of transistor circuits, highlighting the connections and components involved in each configuration.
```

**Figure 12.14** (a) Conversion of series diodes to a topology with grounded collectors; (b) circuit of part (a) biased by PMOS current sources.

An important concern in the circuit of Fig. 12.15 is the relatively low current gain of the "native" *pnp* transistors. Since the base currents of *Q*<sup>2</sup> and *Q*<sup>4</sup> generate an error in the emitter currents of *Q*<sup>1</sup> and *Q*3, a means of base current cancellation may be necessary (Problem 12.5).

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with active load and current mirror. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.

2. **Transistors:**
   - There are four MOSFET transistors labeled \( M_1 \), \( M_2 \), \( M_3 \), and \( M_4 \).
   - \( M_1 \) and \( M_2 \) form the differential pair.
   - \( M_3 \) and \( M_4 \) are the active load transistors.

3. **Current Mirror:**
   - The current mirror is formed by the bipolar junction transistors (BJTs) \( Q_2 \) and \( Q_4 \).
   - \( Q_1 \) and \( Q_3 \) are additional BJTs connected to the emitters of \( Q_2 \) and \( Q_4 \) respectively.

4. **Operational Amplifier:**
   - An operational amplifier \( A_1 \) is shown with its inverting input connected to the node \( X \) and its non-inverting input connected to the node \( Y \).

5. **Resistors:**
   - Two resistors \( R_1 \) and \( R_2 \) are connected in series between the output node \( V_{out} \) and the node \( Y \).

6. **Connections:**
   - The source of \( M_1 \) is connected to the collector of \( Q_2 \), and the source of \( M_2 \) is connected to the collector of \( Q_4 \).
   - The gates of \( M_3 \) and \( M_4 \) are connected together and to the drain of \( M_1 \).
   - The drain of \( M_2 \) is connected to the output node \( V_{out} \).
   - The emitters of \( Q_2 \) and \( Q_4 \) are connected to ground through \( Q_1 \) and \( Q_3 \) respectively.
   - The bases of \( Q_2 \) and \( Q_4 \) are connected to the input signals \( A \) and \( nA \) respectively.

This circuit is typically used in analog signal processing for amplifying differential signals while rejecting common-mode noise. The active load and current mirror configuration help in improving the gain and linearity of the amplifier.
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
The image depicts a graph with a horizontal axis labeled "T" and a vertical axis labeled "V_REF." The graph features a single, smooth, concave-down curve that starts from the horizontal axis, rises to a peak, and then descends back towards the horizontal axis. The peak of the curve is marked by a dashed vertical line that intersects the horizontal axis at a point labeled "T_0." The curve is symmetrical around this vertical line, indicating that "T_0" represents the point at which "V_REF" reaches its maximum value. The overall shape of the curve suggests a parabolic relationship between "V_REF" and "T."
```

**Figure 12.16** Curvature in temperature dependence of a bandgap voltage.

Many curvature correction techniques have been devised to suppress the variation of *VREF* [5, 6] in bipolar bandgap circuits, but they are seldom used in CMOS counterparts. This is because, due to large offsets and process variations, samples of a bandgap reference display substantially different zero-TC temperatures (Fig. 12.17), making it difficult to correct the curvature reliably.

Here is the image describtion:
```
The image depicts a graph with the horizontal axis labeled "T" and the vertical axis labeled "V_REF." The graph features five distinct curves that all exhibit a similar shape, resembling a parabolic arc. Each curve starts at a lower value on the left, rises to a peak in the middle, and then descends towards the right. The curves are closely grouped together, indicating that they follow a similar trend but with slight variations in their exact positions and shapes. The overall pattern suggests a relationship between the variables represented by "T" and "V_REF," where "V_REF" increases to a maximum point and then decreases as "T" progresses.
```

**Figure 12.17** Variation of the zero-TC temperature for different samples.

# **12.4 PTAT Current Generation**

In the analysis of bandgap circuits, we noted that the bias currents of the bipolar transistors are in fact proportional to absolute temperature. Useful in many applications, PTAT currents can be generated by a topology such as that shown in Fig. 12.18. Alternatively, we can combine the supply-independent biasing scheme of Fig. 12.2 with a bipolar core, arriving at Fig. 12.19.3 Assuming for simplicity that *M*1-*M*<sup>2</sup> and *M*3-*M*<sup>4</sup> are identical pairs, we note that for *ID*<sup>1</sup> = *ID*2, the circuit must ensure that *VX* = *VY* . Thus, *ID*<sup>1</sup> = *ID*<sup>2</sup> = *(VT* ln *n)/R*1, yielding the same behavior for *ID*5. In practice, due to mismatches between the transistors and, more important, the temperature coefficient of *R*1, the variation of *ID*<sup>5</sup> deviates from the ideal equation. For low-voltage operation, the topology of Fig. 12.18 is preferred.

Here is the image describtion:
```
The images depict two different circuit configurations for generating a Proportional To Absolute Temperature (PTAT) current.

**Figure 12.18: Generation of a PTAT Current**
- This circuit includes an operational amplifier (op-amp) with its inverting input connected to the base of transistor Q1 and its non-inverting input connected to the base of transistor Q2.
- The emitters of Q1 and Q2 are grounded.
- The collectors of Q1 and Q2 are connected to the sources of PMOS transistors M3 and M4, respectively.
- The drains of M3 and M4 are connected to the positive supply voltage (V_DD).
- A resistor R1 is connected between the collector of Q2 and the ground.
- The PTAT current is drawn from the node between the drain of M4 and the collector of Q2.

**Figure 12.19: Alternative Method of Generating a PTAT Current**
- This circuit does not use an op-amp.
- It includes two NMOS transistors, M1 and M2, with their sources connected to the emitters of Q1 and Q2, respectively.
- The gates of M1 and M2 are connected to nodes X and Y, respectively.
- The drains of M1 and M2 are connected to the sources of PMOS transistors M3 and M4, respectively.
- The drains of M3 and M4 are connected to V_DD.
- An additional PMOS transistor, M5, is connected with its source to V_DD and its drain to the node between the drain of M4 and the collector of Q2.
- A resistor R1 is connected between the collector of Q2 and the ground.
- The PTAT current is drawn from the node between the drain of M4 and the collector of Q2.

Both circuits aim to generate a current that is proportional to the absolute temperature, but they use different configurations and components to achieve this.
```

The circuit of Fig. 12.18 can be readily modified to provide a bandgap reference voltage as well. Illustrated in Fig. 12.20, the idea is to add a PTAT voltage *ID*5*R*<sup>2</sup> to a base-emitter voltage. The output therefore equals

$$|V\_{REF} = |V\_{BE3}| + \frac{R\_2}{R\_1} V\_T \ln n\tag{12.51}$$

<sup>3</sup>The two circuits in Figs. 12.18 and 12.19 exhibit different supply rejections. With a carefully-designed op amp, the former achieves a higher rejection.

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with a current mirror load. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **Q1, Q2, and Q3**: These are NPN bipolar junction transistors (BJTs). 
     - Q1 has its collector connected to node X and its emitter grounded.
     - Q2 has its collector connected to node Y and its emitter grounded.
     - Q3 has its collector connected to the output node (Vout) and its emitter grounded.
   
2. **MOSFETs:**
   - **M3, M4, and M5**: These are PMOS transistors.
     - M3 has its source connected to V_DD, its gate connected to node X, and its drain connected to the negative input of the operational amplifier (op-amp).
     - M4 has its source connected to V_DD, its gate connected to the positive input of the op-amp, and its drain connected to node Y.
     - M5 has its source connected to V_DD, its gate connected to the positive input of the op-amp, and its drain connected to the output node (Vout).

3. **Resistors:**
   - **R1**: Connected between node Y and the ground.
   - **R2**: Connected between the output node (Vout) and the ground.

4. **Operational Amplifier (Op-Amp):**
   - The op-amp has its inverting input (-) connected to node X and its non-inverting input (+) connected to node Y.

5. **Nodes and Connections:**
   - **Node X**: Connected to the collector of Q1, the gate of M3, and the inverting input of the op-amp.
   - **Node Y**: Connected to the collector of Q2, the gate of M4, the non-inverting input of the op-amp, and one end of resistor R1.
   - **Output Node (Vout)**: Connected to the drain of M5, the collector of Q3, and one end of resistor R2.

6. **Power Supply:**
   - **V_DD**: The positive power supply voltage connected to the sources of M3, M4, and M5.

7. **Inputs:**
   - **A**: The base of Q1.
   - **nA**: The base of Q2.

The circuit is a differential amplifier with a current mirror load, where the differential pair (Q1 and Q2) amplifies the difference between the input signals A and nA. The current mirror formed by M3 and M4 ensures that the currents through Q1 and Q2 are mirrored, and M5 acts as a load transistor providing the output voltage (Vout). The resistors R1 and R2 are used for biasing and stabilization.
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
The image depicts a schematic diagram of an electronic circuit. The circuit includes a combination of MOSFET transistors, capacitors, and switches. Here is a detailed description of the components and their connections:

1. **MOSFET Transistors:**
   - There are four MOSFET transistors labeled as M1, M2, M3, and M4.
   - M1 and M2 are connected in series with their sources connected to ground.
   - M3 and M4 are connected in series with their drains connected to the power supply voltage V_DD.

2. **Capacitors:**
   - There is a capacitor labeled C_B connected between the drain of M4 and the source of M2.
   - Another capacitor labeled C_S is shown in a separate dashed box, connected to the source of M1 and the drain of M2.

3. **Switches:**
   - Two switches, S1 and S2, are shown within a dashed box.
   - S1 is connected between the capacitor C_S and ground.
   - S2 is connected between the source of M2 and ground.
   - Both switches are controlled by clock signals CK and CK (complementary clock signals).

4. **Resistor:**
   - A resistor labeled R_S is shown on the right side of the image, represented by a standard resistor symbol.

5. **Connections:**
   - The gate of M1 is connected to the source of M3.
   - The gate of M2 is connected to the source of M4.
   - The gate of M3 is connected to the drain of M1.
   - The gate of M4 is connected to the drain of M2.

The circuit appears to be a part of a larger system, possibly a sample-and-hold circuit or a switched-capacitor circuit, commonly used in analog-to-digital conversion or signal processing applications. The dashed box indicates a sub-circuit that includes the switches and capacitor C_S, which might be used for sampling or holding a voltage. The resistor R_S could be part of a feedback network or load.
```

**Figure 12.21** Constant-*Gm* biasing by means of a switched-capacitor "resistor."

The switched-capacitor approach of Fig. 12.21 can be applied to other circuits as well. For example, as shown in Fig. 12.22, a voltage-to-current converter with a relatively high accuracy can be constructed.

Here is the image describtion:
```
The image depicts a circuit diagram used for voltage-to-current conversion by means of a switched-capacitor resistor. The key components and their connections are as follows:

1. **Operational Amplifier (Op-Amp)**: The circuit includes an operational amplifier with its non-inverting input connected to a reference voltage \( V_{REF} \). The inverting input is connected to a node that links to other components in the circuit.

2. **Capacitors**: There are two capacitors in the circuit:
   - \( C_B \): Connected between the inverting input of the op-amp and ground.
   - \( C_S \): Connected between a node and ground, with switches \( S_1 \) and \( S_2 \) controlling its connection.

3. **Switches**: Two switches, \( S_1 \) and \( S_2 \), are controlled by clock signals \( CK \) and \( \overline{CK} \) (the complement of \( CK \)), respectively.
   - \( S_1 \): Connects the node between the op-amp output and the source of the transistor \( M_1 \) to the top plate of \( C_S \).
   - \( S_2 \): Connects the bottom plate of \( C_S \) to ground.

4. **Transistor \( M_1 \)**: A transistor \( M_1 \) is connected with its gate to the output of the op-amp, its source to the node shared with \( S_1 \) and \( C_S \), and its drain to a current source \( I_{REF} \).

5. **Reference Voltage \( V_{REF} \)**: The reference voltage \( V_{REF} \) is applied to the non-inverting input of the op-amp.

The circuit operates by switching the capacitors in synchronization with the clock signals to achieve the desired voltage-to-current conversion. The caption of the image, "Figure 12.22 Voltage-to-current conversion by means of a switched-capacitor resistor," indicates the purpose and function of the circuit.
```

Here is the image describtion:
```
The image shows a section header from a document or book. The section is labeled "12.6" and is titled "Speed and Noise Issues." The title is preceded by a small black square bullet point. The text is in a standard, readable font, and the layout suggests it is part of a larger structured document, likely a technical or academic text.
```

Even though reference generators are low-frequency circuits, they may affect the speed of the circuits that they feed. Furthermore, various building blocks may experience "crosstalk" through reference lines. These difficulties arise because of the finite output impedance of reference voltage generators, especially if they incorporate op amps. As an example, let us consider the configuration shown in Fig. 12.23, assuming that the voltage at node *N* is heavily disturbed by the circuit fed by *M*5. For fast changes in *VN* , the op amp cannot maintain *VP* constant, and the bias currents of *M*<sup>5</sup> and *M*<sup>6</sup> experience large transient changes. Also, the duration of the transient at node *P* may be quite long if the op amp suffers from a slow response. For this reason, many applications may require a high-speed op amp in the reference generator.

In systems where the power consumed by the reference circuit must be small, the use of a high-speed op amp may not be feasible. Alternatively, the critical node, e.g., node *P* in Fig. 12.23, can be bypassed to ground by means of a large capacitor (*CB*) so as to suppress the effect of external disturbances. This approach involves two issues. First, the stability of the op amp must not degrade with the addition of the capacitor, requiring the op amp to be of a one-stage nature (Chapter 10). Second, since *CB* generally slows down the transient response of the op amp, its value must be much greater than the capacitance that couples the disturbance to node *P*. As illustrated in Fig. 12.24, if *CB* is not sufficiently large, then *VP*

Here is the image describtion:
```
The image consists of two main parts: a circuit diagram at the top and a graph at the bottom.

### Circuit Diagram:
1. **Components and Connections:**
   - **Operational Amplifier (Op-Amp):** The central component is an operational amplifier with its inverting input (-) connected to point A and its non-inverting input (+) connected to point B.
   - **Resistor (R1):** Connected between points A and B.
   - **Transistors:** There are two transistors connected to the ground, one at point A and one at point B.
   - **Capacitors (C_B):** There is a capacitor labeled C_B connected to the ground, but it is shown in a lighter shade, indicating it might be optional or for reference.
   - **MOSFETs (M5 and M6):** Two MOSFETs are connected in series between the power supply (V_DD) and point N.
   - **Point P:** Connected to the output of the operational amplifier and to the gates of the MOSFETs M5 and M6.
   - **Voltage Source (V_DD):** The power supply is labeled V_DD.

2. **Waveform:**
   - A waveform is shown next to point N, indicating the voltage at this point varies over time (t).

### Graph:
1. **Voltage vs. Time:**
   - The graph shows the voltage (V_P) at point P over time (t).
   - Three different curves are plotted, labeled C_B1, C_B2, and C_B3, representing different capacitance values.
   - The curve labeled "Very Large C_B" shows a more gradual change in voltage compared to the other curves, indicating the effect of a large capacitance.

2. **Behavior of Curves:**
   - The curves demonstrate how the voltage at point P changes over time for different capacitance values.
   - The larger the capacitance (C_B), the slower the voltage change, indicating a damping effect.

### Summary:
The image illustrates a circuit involving an operational amplifier, resistors, transistors, MOSFETs, and capacitors. The graph below the circuit shows how the voltage at a specific point in the circuit (P) changes over time for different capacitance values, highlighting the impact of capacitance on the circuit's response.
```

**Figure 12.23** Effect of circuit transients on reference voltages and currents.

**Figure 12.24** Effect of increasing bypass capacitor on the response of a reference generator.

experiences a change and takes a long time to return to its original value, possibly degrading the settling speed of the circuits biased by the reference generator. In other words, depending on the environment, it may be preferable to leave node *P* agile so that it can quickly recover from transients. In general, as depicted in Fig. 12.25, the response of the circuit must be analyzed by applying a disturbance at the output and observing the settling behavior.

**CB1 < CB2 < CB3**

**t**

Here is the image describtion:
```
The image is a schematic diagram labeled as "Figure 12.25 Setup for testing the transient response of a reference generator." The diagram illustrates the setup used to test the transient response of a reference generator.

- On the left side of the diagram, there is a box labeled "Reference Generator."
- A line extends from the reference generator to a node where it splits into three paths.
- The first path goes to a capacitor symbol, which is connected to ground.
- The second path goes to a symbol representing a voltage source with a square wave input, which is also connected to ground.
- The third path leads to a point labeled "Vout," which is connected to ground.
- The output waveform is depicted as a sinusoidal wave with a peak, indicating the transient response being measured.

The diagram is a simplified representation of the components and connections used to test the transient response of the reference generator, showing the key elements involved in the setup.
```

#### ▲**Example 12.7**

Determine the small-signal output impedance of the bandgap reference shown in Fig. 12.23 and examine its behavior with frequency.

## **Solution**

Figure 12.26 depicts the equivalent circuit, modeling the open-loop op amp by a one-pole transfer function *A(s)* = *A*0*/(*1 + *s/*ω0*)* and an output resistance *Rout* and each bipolar transistor by a resistance 1*/gmN* . If *M*<sup>1</sup> and *M*<sup>2</sup> are identical, each having a transconductance of *gm P* , then their drain currents are equal to *gm P VX* , producing a differential voltage at the input of the op amp equal to

$$V\_{AB} = -g\_{mP} V\_X \frac{1}{g\_{mN}} + g\_{mP} V\_X \left(\frac{1}{g\_{mN}} + R\_1\right) \tag{12.55}$$

$$=\,\_{m}\mathbf{g}\_{m}\,V\_{X}\,\mathbf{R}\_{1}\tag{12.56}$$

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with a feedback network. Here is a detailed description of the components and their connections:

1. **Transistors M1 and M2**: 
   - These are MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) with their sources connected to a common node.
   - The drains of M1 and M2 are connected to the positive supply voltage \( V_{DD} \).

2. **Node P**:
   - The common node where the drains of M1 and M2 meet is labeled as P.
   - A resistor \( R_{out} \) is connected between node P and the output of an operational amplifier (op-amp) labeled \( A(s) \).

3. **Operational Amplifier A(s)**:
   - The op-amp has a negative feedback configuration.
   - The inverting input (-) of the op-amp is connected to node A.
   - The non-inverting input (+) of the op-amp is connected to node B.

4. **Resistors and Conductances**:
   - There are two resistors connected to the ground from nodes A and B.
   - The resistor connected to node A has a value of \( \frac{1}{g_{mN}} \).
   - The resistor connected to node B has a value of \( \frac{1}{g_{mN}} + R_1 \).

5. **Voltage Source \( V_X \)**:
   - A voltage source \( V_X \) is connected to the gate of transistor M2.
   - The positive terminal of \( V_X \) is connected to the gate of M2, and the negative terminal is grounded.

6. **Current \( I_X \)**:
   - The current \( I_X \) flows through the circuit from the node P to the voltage source \( V_X \).

7. **Voltage Contributions**:
   - The voltage \( g_{mP} V_X \) is indicated at the gates of both transistors M1 and M2, suggesting that the transconductance \( g_{mP} \) and the input voltage \( V_X \) are contributing to the operation of the transistors.

Overall, the circuit is a differential amplifier with feedback, utilizing MOSFETs, an operational amplifier, and resistive elements to achieve amplification and stability. The feedback network helps in controlling the gain and improving the performance of the amplifier.
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
The image is a graph that plots the magnitude of the output impedance (|Z_out|) on the vertical axis against the angular frequency (ω) on the horizontal axis. The graph is divided into three distinct regions:

1. **Low-Frequency Region**: At low frequencies, the output impedance is constant and equal to \( \frac{R_{out}}{1 + g_m P R_1 A_0} \). This value is represented by a horizontal line at the lower part of the graph.

2. **Mid-Frequency Region**: As the frequency increases, the output impedance starts to rise. This transition begins at the angular frequency \( \omega_0 \). The graph shows a smooth, upward curve starting from \( \omega_0 \).

3. **High-Frequency Region**: At high frequencies, the output impedance reaches a maximum value of \( R_{out} \). This is represented by a horizontal line at the upper part of the graph. The transition to this maximum value occurs around the angular frequency \( (1 + g_m P R_1 A_0) \omega_0 \).

The graph also indicates a specific point where the output impedance is \( \frac{R_{out}}{\sqrt{2}} \), which is typically associated with the -3dB point in frequency response analysis.

Key notations on the graph:
- \( R_{out} \): The maximum output impedance.
- \( g_m \): Transconductance.
- \( P \): A parameter related to the circuit.
- \( R_1 \): A resistance value.
- \( A_0 \): Open-loop gain.
- \( \omega_0 \): A specific angular frequency where the transition begins.
- \( (1 + g_m P R_1 A_0) \omega_0 \): The angular frequency where the output impedance reaches its maximum value.

The graph effectively illustrates how the output impedance varies with frequency, showing a low value at low frequencies, increasing through a mid-frequency range, and stabilizing at a higher value at high frequencies.
```

Here is the image describtion:
```
The image is a caption for Figure 12.27, which describes the content of the figure. The caption reads: "Variation of the reference generator output impedance with frequency." This suggests that the figure likely contains a graph or chart illustrating how the output impedance of a reference generator changes as the frequency varies. The specific details of the graph, such as the axes, data points, and trends, are not visible in the provided image.
```

▲

The output noise of reference generators may affect the performance of low-noise circuits considerably. Figure 12.28 illustrates an example: the load current source of a common-source stage is driven by a bandgap circuit with a current multiplication factor of *N*. Thus, the noise current of *M*<sup>1</sup> (or *M*2) is amplified by the same factor as it appears in *M*3. Note that *M*1–*M*<sup>3</sup> carry noise due to the op amp *A*<sup>1</sup> as well.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a current mirror with an operational amplifier (op-amp) and MOSFET transistors. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The circuit is powered by a voltage source labeled V_DD, which is connected to the top of the diagram.

2. **Transistors (M1, M2, M3, M4)**: There are four MOSFET transistors labeled M1, M2, M3, and M4.
   - **M1**: The source of M1 is connected to the drain of Q1 and the inverting input of the op-amp (A1). The drain of M1 is connected to V_DD.
   - **M2**: The source of M2 is connected to the non-inverting input of the op-amp (A1) and the resistor R1. The drain of M2 is connected to V_DD.
   - **M3**: The source of M3 is connected to the output node labeled V_out. The drain of M3 is connected to V_DD.
   - **M4**: The source of M4 is connected to ground. The gate of M4 is connected to the input node labeled V_in. The drain of M4 is connected to the output node V_out.

3. **Operational Amplifier (A1)**: The op-amp has its inverting input connected to the source of M1 and the drain of Q1. The non-inverting input is connected to the source of M2 and one end of the resistor R1. The output of the op-amp is connected to the gate of M1.

4. **Resistor (R1)**: The resistor R1 is connected between the source of M2 (and the non-inverting input of the op-amp) and the drain of Q2.

5. **Bipolar Junction Transistors (Q1, Q2)**: There are two BJTs labeled Q1 and Q2.
   - **Q1**: The emitter of Q1 is connected to ground. The base of Q1 is connected to a node labeled A. The collector of Q1 is connected to the source of M1 and the inverting input of the op-amp.
   - **Q2**: The emitter of Q2 is connected to ground. The base of Q2 is connected to a node labeled nA. The collector of Q2 is connected to the resistor R1 and the non-inverting input of the op-amp.

6. **Input and Output Nodes**:
   - **V_in**: The input voltage is applied to the gate of M4.
   - **V_out**: The output voltage is taken from the source of M3 and the drain of M4.

The circuit appears to be a current mirror with an op-amp used to improve accuracy and stability. The op-amp ensures that the voltage at the inverting input matches the voltage at the non-inverting input, thereby controlling the current through the transistors and maintaining a stable output.
```

**Figure 12.28** Effect of bandgap circuit noise on a CS stage.

As another example, if a high-precision A/D converter employs a bandgap voltage as the reference with which the analog input signal is compared (Fig. 12.29), then the noise in the reference is directly added to the input.

Here is the image describtion:
```
The image depicts a simplified block diagram of an Analog-to-Digital (A/D) conversion system. The diagram includes the following components:

1. **A/D Converter**: This is the central component of the diagram, represented by a rectangular box labeled "A/D Converter." It is responsible for converting the analog input signal into a digital output signal.

2. **Vin**: This is the analog input signal to the A/D converter, denoted by "Vin." It is shown entering the A/D converter from the left side.

3. **Digital Output**: This is the output of the A/D converter, represented by an arrow pointing to the right, labeled "Digital Output." This indicates that the A/D converter produces a digital signal as its output.

4. **Reference Generator**: This is another rectangular box labeled "Reference Generator," connected to the A/D converter. The reference generator provides a reference voltage or signal necessary for the A/D conversion process.

The diagram illustrates the basic flow of an analog signal being converted into a digital signal with the help of a reference generator.
```

**Figure 12.29** A/D converter using a reference generator.

As a simple example, let us calculate the output noise voltage of the circuit shown in Fig. 12.30, taking into account only the input-referred noise voltage of the op amp, *Vn,op*. Since the small-signal drain currents of *<sup>M</sup>*<sup>1</sup> and *<sup>M</sup>*<sup>2</sup> are equal to *Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*, we have *VP* <sup>=</sup> <sup>−</sup>*g*−<sup>1</sup> *m P Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*, obtaining the differential voltage at the input of the op amp as <sup>−</sup>*g*−<sup>1</sup> *m P A*−<sup>1</sup> <sup>0</sup> *Vn,out/(R*<sup>1</sup> <sup>+</sup> *<sup>g</sup>*−<sup>1</sup> *mN )*. Beginning

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with a current mirror load. Here is a detailed description of the components and their connections:

1. **Transistors (M1 and M2)**: 
   - There are two MOSFET transistors labeled M1 and M2. 
   - The source terminals of both transistors are connected to the positive supply voltage, V_DD.
   - The drain terminals of M1 and M2 are connected to a common node labeled P.

2. **Current Sources**:
   - There are two current sources, each labeled g_mP V_P, connected to the drain terminals of M1 and M2, respectively. These current sources are pointing upwards towards the node P.

3. **Operational Amplifier (A0)**:
   - An operational amplifier (op-amp) is depicted with its inverting input (-) connected to node A and its non-inverting input (+) connected to node B.
   - The output of the op-amp is connected to node P.

4. **Resistors**:
   - There are two resistors, each with a value of 1/g_mN, connected to nodes A and B, respectively. 
   - The resistor connected to node A is grounded.
   - The resistor connected to node B is in series with another resistor labeled R1, which is also grounded.

5. **Voltage Sources**:
   - There is a voltage source labeled V_n,op connected between nodes A and B.
   - The output voltage of the circuit is labeled V_n,out and is taken from node B.

6. **Ground Connections**:
   - The ground symbol is used to indicate the reference point for the circuit, connected to the bottom of the resistors.

In summary, the circuit is a differential amplifier with a current mirror load, utilizing MOSFETs, an operational amplifier, and resistors to achieve amplification. The output voltage is taken from node B, and the circuit is powered by a supply voltage V_DD.
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
The image depicts an electrical circuit diagram that illustrates the summation of two currents with opposite temperature coefficients (TC) to achieve a result with zero temperature coefficient. 

In the diagram:
- There is a voltage source labeled \( V_{DD} \) connected to a resistor \( R_1 \).
- The voltage across the resistor \( R_1 \) is given by the equation \( V = (I_1 + I_2)R_1 \), where \( I_1 \) and \( I_2 \) are the currents flowing through the circuit.
- The temperature coefficient (TC) of the voltage across \( R_1 \) is indicated to be zero (TC = 0).
- Two current sources, \( I_1 \) and \( I_2 \), are shown connected to the node between \( V_{DD} \) and \( R_1 \), with their other ends connected to the ground.
- The current \( I_1 \) has a positive temperature coefficient (TC > 0), while the current \( I_2 \) has a negative temperature coefficient (TC < 0).

The figure is labeled as "Figure 12.31" and is accompanied by a caption that reads: "Summation of two currents with opposite TCs to obtain a result with zero TC."
```

Let us return to the circuit of Fig. 12.18, assume that *M*<sup>3</sup> and *M*<sup>4</sup> are identical, and note that |*ID*4| = *VT* ln *n/R*<sup>1</sup> is a PTAT current. We place a resistor in parallel with *Q*<sup>2</sup> as shown in Fig. 12.32(a). We recognize that *R*<sup>1</sup> now carries an additional current equal to |*VB E*2|*/R*2, i.e., a current with a negative TC. Unfortunately, however, the PTAT behavior is now disturbed because *IC*<sup>1</sup> =% *IC*2. Fortunately, a simple modification resolves this issue: as shown in Fig. 12.32(b), we tie *R*<sup>2</sup> from *Y* to ground and place another resistor in parallel with *Q*1. Proposed by Banba et al. [8], this topology lends itself to low-voltage implementation, requiring a minimum *VDD* of *VB E*<sup>1</sup> + |*VDS*3|.

To analyze the circuit, we observe that *VX* ≈ *VY* ≈ |*VB E*1| and *ID*<sup>3</sup> = *ID*4. Thus,

$$I\_{C1} + \frac{|V\_{BE1}|}{R\_3} = I\_{C2} + \frac{|V\_{BE1}|}{R\_2} \tag{12.66}$$

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each circuit features a combination of transistors, resistors, and an operational amplifier. Here is a detailed description of each circuit:

### Circuit (a):
- **Power Supply**: The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.
- **Transistors**: There are two PMOS transistors labeled \( M_3 \) and \( M_4 \) connected in parallel at the top.
- **Operational Amplifier**: An operational amplifier labeled \( A_1 \) is placed in the middle with its inverting input (-) connected to node X and its non-inverting input (+) connected to node Y.
- **Nodes**: 
  - Node X is connected to the source of \( M_3 \) and the collector of an NPN transistor \( Q_1 \).
  - Node Y is connected to the source of \( M_4 \) and the collector of another NPN transistor \( Q_2 \).
- **Transistors \( Q_1 \) and \( Q_2 \)**: 
  - The emitter of \( Q_1 \) is grounded, and its base is connected to a point labeled A.
  - The emitter of \( Q_2 \) is grounded, and its base is connected to a point labeled nA.
- **Resistors**: 
  - A resistor \( R_1 \) is connected between node Y and ground.
  - Another resistor \( R_2 \) is connected between the base of \( Q_2 \) and ground.

### Circuit (b):
- **Power Supply**: Similar to circuit (a), it is powered by \( V_{DD} \).
- **Transistors**: The same PMOS transistors \( M_3 \) and \( M_4 \) are used.
- **Operational Amplifier**: The operational amplifier \( A_1 \) is configured similarly.
- **Nodes**: 
  - Node X is connected to the source of \( M_3 \) and the collector of \( Q_1 \).
  - Node Y is connected to the source of \( M_4 \) and the collector of \( Q_2 \).
- **Transistors \( Q_1 \) and \( Q_2 \)**: 
  - The emitter of \( Q_1 \) is grounded, and its base is connected to point A.
  - The emitter of \( Q_2 \) is grounded, and its base is connected to point nA.
- **Resistors**: 
  - A resistor \( R_1 \) is connected between node Y and ground.
  - Another resistor \( R_2 \) is connected between the base of \( Q_2 \) and ground.
  - An additional resistor \( R_3 \) is connected between node X and ground.

### Circuit (c):
- **Power Supply**: The circuit is powered by \( V_{DD} \).
- **Transistors**: In addition to \( M_3 \) and \( M_4 \), there is an extra PMOS transistor \( M_5 \) connected in parallel with \( M_4 \).
- **Operational Amplifier**: The operational amplifier \( A_1 \) is configured similarly.
- **Nodes**: 
  - Node X is connected to the source of \( M_3 \) and the collector of \( Q_1 \).
  - Node Y is connected to the source of \( M_4 \) and the collector of \( Q_2 \).
- **Transistors \( Q_1 \) and \( Q_2 \)**: 
  - The emitter of \( Q_1 \) is grounded, and its base is connected to point A.
  - The emitter of \( Q_2 \) is grounded, and its base is connected to point nA.
- **Resistors**: 
  - A resistor \( R_1 \) is connected between node Y and ground.
  - Another resistor \( R_2 \) is connected between the base of \( Q_2 \) and ground.
  - A resistor \( R_3 \) is connected between node X and ground.
  - An additional resistor \( R_4 \) is connected between the source of \( M_5 \) and ground, with a voltage labeled \( V_{BG} \) connected to the gate of \( M_5 \).

Each circuit shows a different configuration of the same basic components, with variations in the connections and the addition of extra resistors and transistors.
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
The image depicts an electronic circuit diagram, specifically a bandgap voltage reference circuit. Here is a detailed description of the components and their connections:

1. **Power Supply and Ground:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.
   - The ground symbols are used at various points in the circuit to indicate connections to the ground.

2. **Transistors:**
   - There are five MOSFET transistors labeled \( M_3 \), \( M_4 \), and \( M_5 \) at the top, and two bipolar junction transistors (BJTs) labeled \( Q_1 \) and \( Q_2 \) at the bottom.
   - \( Q_1 \) and \( Q_2 \) are connected to ground through their emitters, with their bases connected to nodes \( X \) and \( Y \) respectively.

3. **Operational Amplifier:**
   - An operational amplifier \( A_1 \) is present in the circuit with its inverting input (-) connected to node \( X \) and its non-inverting input (+) connected to node \( Y \).
   - The output of the operational amplifier is connected to the gates of transistors \( M_3 \) and \( M_4 \).

4. **Resistors:**
   - There are four resistors labeled \( R_1 \), \( R_2 \), \( R_3 \), and \( R_4 \).
   - \( R_1 \) is connected between node \( Y \) and the ground.
   - \( R_2 \) is connected between node \( Y \) and the ground.
   - \( R_3 \) is connected between node \( X \) and the ground.
   - \( R_4 \) is connected between the source of \( M_5 \) and the ground.

5. **Voltage Reference:**
   - The circuit generates a bandgap voltage reference labeled \( V_{BG} \) at the output node connected to the source of \( M_5 \).

6. **Offset Voltage:**
   - There is a symbol \( V_{os} \) indicating an offset voltage between the inverting and non-inverting inputs of the operational amplifier \( A_1 \).

7. **Current Sources:**
   - The circuit includes current sources labeled \( A \) and \( nA \) connected to the collectors of \( Q_1 \) and \( Q_2 \) respectively.

8. **Figure Label:**
   - The figure is labeled as "Figure 12.33" at the bottom.

This circuit is typically used to generate a stable reference voltage that is independent of temperature variations and power supply fluctuations.
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
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams depict electronic circuits involving transistors, resistors, and current sources.

**Diagram (a):**
- The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.
- There are four MOSFET transistors labeled \( M_3 \), \( M_4 \), \( M_c \), and \( M_d \) connected in a specific configuration.
- Transistors \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \) and form a current mirror.
- Transistors \( M_c \) and \( M_d \) are connected in a differential pair configuration with their sources connected together and to the drain of transistor \( M_b \).
- The circuit includes two bipolar junction transistors (BJTs) labeled \( Q_1 \) and \( Q_2 \).
- \( Q_1 \) has its base connected to node \( A \), its emitter grounded, and its collector connected to node \( X \).
- \( Q_2 \) has its base connected to node \( nA \), its emitter grounded, and its collector connected to node \( Y \).
- Resistors \( R_3 \), \( R_1 \), and \( R_2 \) are connected to nodes \( X \), \( Y \), and the ground, respectively.
- A current source labeled \( I_{SS} \) is connected between the source of transistor \( M_a \) and ground.

**Diagram (b):**
- This circuit is also powered by a voltage source labeled \( V_{DD} \) at the top.
- It includes three MOSFET transistors labeled \( M_3 \), \( M_e \), and \( M_c \).
- Transistor \( M_3 \) is connected to \( V_{DD} \) and forms part of a current mirror.
- Transistor \( M_e \) is connected to the gate of \( M_c \) and forms part of a differential pair with \( M_c \).
- The circuit includes one bipolar junction transistor (BJT) labeled \( Q_1 \).
- \( Q_1 \) has its base connected to node \( X \), its emitter grounded, and its collector connected to node \( X \).
- Resistor \( R_3 \) is connected to node \( X \) and ground.
- A current source labeled \( I_{SS} \) is connected between the source of transistor \( M_a \) and ground.

Both circuits appear to be variations of differential amplifier configurations, with diagram (a) being more complex with additional components compared to diagram (b).
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
The image depicts a schematic diagram of an electronic circuit, likely an operational amplifier (op-amp) based circuit. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **Q1, Q2, Q3:** These are NPN bipolar junction transistors (BJTs). 
     - Q1 has its base connected to a node labeled "A" and its emitter connected to ground.
     - Q2 has its base connected to a node labeled "nA" and its emitter connected to ground.
     - Q3 has its base connected to a node and its emitter connected to ground.

2. **Resistors:**
   - **R1:** Connected between the collector of Q2 and the source of M4.
   - **R2:** Connected between the node leading to Vout and ground.
   - **R3:** Connected in series with R2 to ground.

3. **MOSFETs:**
   - **M3, M4, M5:** These are NMOS transistors.
     - M3 has its drain connected to VDD and its source connected to the drain of M4.
     - M4 has its source connected to the collector of Q2 and the resistor R1.
     - M5 has its drain connected to VDD and its source connected to the node leading to Vout.

4. **Operational Amplifier (A1):**
   - The op-amp has its inverting input (-) connected to the source of M3.
   - The non-inverting input (+) is connected to the source of M4.
   - The output of the op-amp is connected to the gate of M4.

5. **Power Supply:**
   - **VDD:** The positive power supply voltage connected to the drains of M3 and M5.

6. **Output:**
   - **Vout:** The output voltage is taken from the node between the source of M5 and the resistors R2 and R3.

The circuit appears to be a differential amplifier with an active load, utilizing both BJTs and MOSFETs, and incorporating an operational amplifier for feedback control. The resistors R2 and R3 form a voltage divider network at the output.
```

**Figure 12.35** Alternative low-voltage BG circuit.

It is possible to add other bias branches to the foregoing circuits so as to provide curvature correction, but such schemes typically rely on trimming because the various mismatches within the circuit tend to shift the zero-TC temperature randomly. Other low-voltage bandgaps are described in [10].

## **12.8 Case Study**

In this section, we study a bandgap reference circuit designed for high-precision analog systems [7]. The reference generator incorporates the topology of Fig. 12.19, but with two series base-emitter voltages in each branch so as to reduce the effect of MOSFET mismatches. A simplified version of the core is depicted in Fig. 12.36, where the PMOS current mirror arrangement ensures equal collector currents for *Q*1–*Q*4. While requiring a high supply voltage, this design exemplifies issues that prove important in practice.

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with active loads. The circuit consists of several MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) and a resistor. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage, labeled as V_DD.

2. **MOSFETs**:
   - **M1 and M2**: These are the main differential pair transistors. Their sources are connected together and to the resistor R1, which is connected to the ground.
   - **M3 and M4**: These transistors form the active load for the differential pair. The drains of M1 and M2 are connected to the drains of M3 and M4, respectively.
   - **M5 and M6**: These transistors are connected in a current mirror configuration. The source of M5 is connected to V_DD, and its gate is connected to the gate and drain of M6. The source of M6 is also connected to V_DD.

3. **Resistor (R1)**: This resistor is connected between the common source of M1 and M2 and the ground. It provides the necessary biasing for the differential pair.

4. **Bipolar Junction Transistors (BJTs)**:
   - **Q1 and Q2**: These are the input transistors of the differential amplifier. The base of Q1 is connected to the input signal nA, and the base of Q2 is connected to the input signal A. The emitters of Q1 and Q2 are connected to the sources of M1 and M2, respectively.
   - **Q3 and Q4**: These transistors are connected to the ground. The base of Q3 is connected to the input signal nA, and the base of Q4 is connected to the input signal A. The emitters of Q3 and Q4 are connected to the ground.

5. **Connections**:
   - The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.
   - The gates of M3 and M4 are connected together and to the drain of M4.
   - The gates of M1 and M2 are connected to the sources of Q1 and Q2, respectively.
   - The sources of M3 and M4 are connected to the sources of M5 and M6, respectively.

This circuit is a typical differential amplifier with active loads, which is commonly used in analog integrated circuits for amplifying differential signals. The active loads (M3 and M4) provide high output impedance, which increases the gain of the amplifier. The current mirror (M5 and M6) ensures that the current through the differential pair is constant, improving the performance of the amplifier.
```

**Figure 12.36** Simplified core of the bandgap circuit reported in [7].

Channel-length modulation of the MOS devices in Fig. 12.36 still results in significant supply dependence. To resolve this issue, each branch can employ both NMOS and PMOS cascode topologies. Figure 12.37(a) shows an example in which the low-voltage cascode current mirror described in Chapter 5

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams depict configurations of transistors and resistors connected to a power supply voltage \( V_{DD} \).

### Diagram (a):
- The circuit is composed of two branches, each containing a series of three transistors.
- The topmost transistors in each branch are connected to \( V_{DD} \).
- The middle transistors in each branch have their gates connected to bias voltages \( V_{b1} \) and \( V_{b2} \), respectively.
- The bottom transistors in each branch are connected to the resistors \( R_1 \) and the emitters of transistors \( Q_1 \) and \( Q_2 \).
- The emitters of \( Q_1 \) and \( Q_2 \) are connected to ground.
- The output nodes are labeled \( nA \) and \( A \).

### Diagram (b):
- This circuit is similar to diagram (a) but includes additional components.
- The topmost transistors in each branch are connected to \( V_{DD} \).
- The middle transistors in each branch have their gates connected to resistors \( R_2 \) and \( R_3 \), respectively.
- The bottom transistors in each branch are connected to the resistor \( R_1 \) and the emitters of transistors \( Q_1 \) and \( Q_2 \).
- The emitters of \( Q_1 \) and \( Q_2 \) are connected to ground.
- The output nodes are labeled \( nA \) and \( A \).
- Additional current paths are indicated by \( I_1 \) and \( I_2 \) flowing through \( R_2 \) and \( R_3 \).

Both diagrams illustrate complex transistor-resistor networks, likely representing parts of a larger electronic circuit, such as a differential amplifier or a current mirror configuration.
```

**Figure 12.37** (a) Addition of cascode devices to improve supply rejection; (b) use of self-biased cascode to eliminate *Vb*<sup>1</sup> and *Vb*2.

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, likely representing a differential amplifier or a similar analog circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.

2. **Transistors:**
   - The circuit includes multiple MOSFET transistors labeled \( M_2 \), \( M_{10} \), \( M_{11} \), and \( M_9 \).
   - There are also bipolar junction transistors (BJTs) labeled \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \).

3. **Resistors:**
   - Several resistors are present in the circuit, labeled \( R_1 \), \( R_2 \), \( R_3 \), \( R_4 \), \( R_5 \), and \( R_6 \).

4. **Operational Amplifier:**
   - An operational amplifier (op-amp) is depicted on the right side of the diagram, labeled \( A_1 \). It has inverting (-) and non-inverting (+) inputs labeled \( E \) and \( F \), respectively.
   - The output of the op-amp is labeled \( V_{out} \).

5. **Connections:**
   - The sources of \( M_2 \) and \( M_{10} \) are connected to \( V_{DD} \).
   - The gates of \( M_2 \) and \( M_{10} \) are connected to the drains of \( M_2 \) and \( M_{11} \), respectively.
   - The drains of \( M_2 \) and \( M_{10} \) are connected to the resistors \( R_2 \) and \( R_3 \), respectively.
   - The sources of \( M_{11} \) and \( M_9 \) are connected to the emitters of \( Q_2 \) and \( Q_4 \), respectively.
   - The bases of \( Q_1 \) and \( Q_3 \) are connected to a node labeled \( nA \), while the bases of \( Q_2 \) and \( Q_4 \) are connected to a node labeled \( A \).
   - The emitters of \( Q_1 \) and \( Q_3 \) are connected to ground through \( R_1 \).
   - The emitters of \( Q_2 \) and \( Q_4 \) are connected to ground.
   - The op-amp inputs \( E \) and \( F \) are connected to the drains of \( M_{11} \) and \( M_9 \), respectively.
   - The resistors \( R_4 \) and \( R_5 \) are connected to the op-amp inputs and the output \( V_{out} \).
   - The resistor \( R_6 \) is connected to the source of \( M_9 \) and ground.

This circuit appears to be a differential amplifier with active loads and an operational amplifier stage for further amplification or buffering. The use of both MOSFETs and BJTs suggests a design that leverages the advantages of both types of transistors.
```

**Figure 12.38** Generation of a floating reference voltage.

is utilized. To obviate the need for *Vb*<sup>1</sup> and *Vb*2, this design actually introduces a "self-biased" cascode, shown in Fig. 12.37(b), where *R*<sup>2</sup> and *R*<sup>3</sup> sustain proper voltages to allow all MOSFETs to remain in saturation. This cascode topology is analyzed in Problem 12.7.

The bandgap circuit reported in [7] is designed to generate a *floating* reference. This is accomplished by the modification shown in Fig. 12.38, where the drain currents of *M*<sup>9</sup> and *M*<sup>10</sup> flow through *R*<sup>4</sup> and *R*5, respectively. Note that *M*<sup>11</sup> sets the gate voltage of *M*<sup>9</sup> at *VB E*<sup>4</sup> + *VG S*11, establishing a voltage equal to *VB E*<sup>4</sup> across *R*<sup>6</sup> if *M*<sup>9</sup> and *M*<sup>11</sup> are identical. Thus, *ID*<sup>9</sup> = *VB E*4*/R*6, yielding *VR*<sup>4</sup> = *VB E*4*(R*4*/R*6*)*. Also, if *M*<sup>10</sup> is identical to *M*2, then |*ID*10| = 2*(VT* ln *n)/R*1, and hence *VR*<sup>5</sup> = 2*(VT* ln *n)(R*5*/R*1*)*. Since the op amp ensures that *VE* ≈ *VF* , we have

$$V\_{out} = \frac{R\_4}{R\_6} V\_{BE4} + 2\frac{R\_5}{R\_1} V\_T \ln n \tag{12.76}$$

Proper choice of the resistor ratios and *n* therefore provides a zero temperature coefficient.

In order to further enhance the supply rejection, this design regulates the supply voltage of the core and the op amp. Illustrated in Fig. 12.39, the idea is to generate a local supply, *VDDL* , that is defined by a reference *VR*<sup>1</sup> and the ratio of *Rr*<sup>1</sup> and *Rr*<sup>2</sup> and hence remains relatively independent of the global supply voltage. But how is *VR*<sup>1</sup> itself generated? To minimize the dependence of *VR*<sup>1</sup> upon the supply,

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring operational amplifiers and resistors. Here is a detailed description of the components and their connections:

1. **Input Voltage (V_R1)**: The circuit starts with an input voltage labeled as V_R1.

2. **Operational Amplifier (Op-Amp)**: The input voltage V_R1 is fed into the non-inverting input (+) of an operational amplifier. The inverting input (-) of this op-amp is connected to the output of the same op-amp, indicating a voltage follower configuration.

3. **Voltage Divider**: The output of the first op-amp is connected to a voltage divider made up of two resistors, R_r1 and R_r2. The junction between these two resistors is connected to ground.

4. **Core Component**: The output of the voltage divider is connected to a block labeled "Core," which is grounded. This block likely represents a more complex part of the circuit, possibly a processing or control unit.

5. **Power Supply (V_DDL)**: The output of the first op-amp is also connected to a power supply labeled V_DDL, which is connected to the core component.

6. **Second Operational Amplifier (A1)**: The output from the core component is fed into the non-inverting input (+) of a second operational amplifier labeled A1. The inverting input (-) of this op-amp is connected to ground.

7. **Ground Connections**: Several points in the circuit are connected to ground, including the junction between R_r1 and R_r2, the core component, and the inverting input of the second op-amp A1.

The circuit appears to be designed for signal processing or conditioning, with the first op-amp acting as a buffer, the voltage divider providing a scaled voltage, and the core component performing some intermediate function before the signal is further processed by the second op-amp A1.
```

**Figure 12.39** Regulation of the supply voltage of the core and op amp to improve supply rejection.

this voltage is established *inside* the core, as depicted in Fig. 12.40. In fact, *RM* is chosen such that *VR*<sup>1</sup> is a bandgap reference.

Figure 12.41 shows the overall implementation, omitting a few details for simplicity. A start-up circuit is also used. Operating from a 5-V supply, the reference generator produces a 2.00-V output while consuming 2.2 mW. The supply rejection is 94 dB at low frequencies, dropping to 58 dB at 100 kHz [7].

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, likely representing a voltage reference or a similar analog circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DDL} \) at the top of the diagram.

2. **Transistors:**
   - The circuit includes multiple MOSFET transistors labeled \( M_9 \), \( M_{10} \), and \( M_{11} \).
   - There are also bipolar junction transistors (BJTs) labeled \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \).

3. **Resistors:**
   - Several resistors are present in the circuit, labeled \( R_1 \), \( R_2 \), \( R_3 \), \( R_4 \), \( R_5 \), \( R_6 \), and \( R_M \).

4. **Voltage Source:**
   - A voltage source labeled \( V_{R1} \) is connected to the left side of the circuit.

5. **Current Sources:**
   - There are current sources labeled \( nA \) connected to the emitters of transistors \( Q_1 \) and \( Q_3 \).

6. **Operational Amplifier:**
   - An operational amplifier (op-amp) labeled \( A_1 \) is present on the right side of the circuit. The non-inverting input is labeled \( E \), and the inverting input is labeled \( F \).
   - The output of the op-amp is labeled \( V_{out} \).

7. **Connections:**
   - The circuit shows various connections between the components, including the gates, drains, and sources of the MOSFETs, as well as the bases, collectors, and emitters of the BJTs.
   - The resistors are connected in different configurations to the transistors and the voltage source.

8. **Ground:**
   - The ground symbol is present at the bottom of the diagram, indicating the common reference point for the circuit.

Overall, the circuit appears to be a sophisticated analog design, possibly for generating a stable reference voltage or for use in a precision analog application. The combination of MOSFETs, BJTs, resistors, and an operational amplifier suggests a design focused on stability and accuracy.
```

**Figure 12.40** Generation of *VR*1, used in Fig. 12.39.

Here is the image describtion:
```
The image depicts a detailed schematic of an electronic circuit, specifically a bandgap voltage reference circuit with a start-up circuit. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (Op-Amp)**:
   - There is an operational amplifier on the left side of the circuit. The non-inverting input is connected to a voltage divider formed by resistors \( R_1 \) and \( R_2 \).
   - The output of the op-amp is connected to the gate of a PMOS transistor \( M_{10} \).

2. **Transistors**:
   - The circuit includes multiple MOSFETs (both PMOS and NMOS). 
   - PMOS transistors \( M_{10} \) and \( M_{11} \) are connected to the positive supply voltage \( V_{DDL} \).
   - NMOS transistors \( M_9 \) and \( M_{11} \) are connected to the ground.
   - Bipolar Junction Transistors (BJTs) \( Q_1 \), \( Q_2 \), \( Q_3 \), and \( Q_4 \) are also present. \( Q_1 \) and \( Q_2 \) are connected in a differential pair configuration, while \( Q_3 \) and \( Q_4 \) are connected to the ground.

3. **Resistors**:
   - Resistors \( R_1 \), \( R_2 \), \( R_3 \), \( R_4 \), \( R_5 \), and \( R_6 \) are used throughout the circuit.
   - \( R_1 \) and \( R_2 \) form a voltage divider.
   - \( R_3 \) is connected between the sources of \( M_{10} \) and \( M_{11} \).
   - \( R_4 \) and \( R_5 \) are connected to the output of the second operational amplifier \( A_1 \).
   - \( R_6 \) is connected to the source of \( M_9 \).

4. **Start-up Circuit**:
   - The start-up circuit is enclosed in a dashed box on the left side of the schematic.
   - It is connected to the supply voltage \( V_{DD} \) and ensures that the circuit starts up correctly by providing an initial current to the main circuit.

5. **Voltage Nodes**:
   - \( V_{DD} \) and \( V_{DDL} \) are the supply voltages.
   - \( V_{R1} \) is the voltage at the node between \( R_1 \) and \( R_2 \).
   - \( V_{out} \) is the output voltage of the circuit, taken from the output of the second operational amplifier \( A_1 \).

6. **Connections**:
   - The output of the first op-amp is connected to the gate of \( M_{10} \).
   - The sources of \( M_{10} \) and \( M_{11} \) are connected through \( R_3 \).
   - The drain of \( M_{11} \) is connected to the gate of \( M_9 \).
   - The sources of \( Q_1 \) and \( Q_2 \) are connected to \( R_M \), which is connected to the ground.
   - The emitters of \( Q_3 \) and \( Q_4 \) are connected to the ground.

This circuit is designed to provide a stable reference voltage that is independent of temperature variations and supply voltage changes, which is crucial for many analog and digital applications.
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
The image depicts a circuit diagram of a current mirror with a cascode configuration. The circuit consists of four MOSFET transistors labeled M1, M2, M3, and M4, and a resistor labeled Rs. 

- M1 and M2 are connected in a common-source configuration.
- The source of M1 is connected to ground, and its gate is connected to the source of M4.
- The drain of M1 is connected to one end of the resistor Rs, and the other end of Rs is connected to the drain of M4.
- The gate of M1 is also connected to the gate of M2, indicating that M1 and M2 are matched transistors.
- The source of M2 is connected to ground, and its drain is connected to the drain of M3.
- The gate of M3 is connected to the gate of M4, indicating that M3 and M4 are also matched transistors.
- The source of M3 is connected to the drain of M4.
- The drain of M3 is connected to the positive supply voltage V_DD.
- The output current I_out is taken from the drain of M2.

This configuration is typically used to improve the output resistance and accuracy of the current mirror. The cascode arrangement of M3 and M4 helps to increase the output impedance and reduce the effect of channel length modulation.
```

- **Figure 12.42**
- **12.2.** Explain how the start-up circuit shown in Fig. 12.43 operates. Derive a relationship that guarantees that *VX < VT H* after the circuit turns on.
- **12.3.** Consider the circuit of Fig. 12.15.
	- **(a)** If *M*<sup>1</sup> and *M*<sup>2</sup> suffer from channel-length modulation, what is the error in the output voltage?
	- **(b)** Repeat part (a) for *M*<sup>3</sup> and *M*4.
	- **(c)** If *M*<sup>1</sup> and *M*<sup>2</sup> have a threshold mismatch of !*V*, i.e., *VT H*<sup>1</sup> = *VT H* and *VT H*<sup>2</sup> = *VT H* + !*V*, what is the error in the output voltage?
	- **(d)** Repeat part (c) for *M*<sup>3</sup> and *M*4.