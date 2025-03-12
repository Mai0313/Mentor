# CHAPTER

Razavi-3930640 book December 17, 201516:59 344

**9**

# *Operational Amplifiers*

Operational amplifiers (op amps) are an integral part of many analog and mixed-signal systems. Op amps with vastly different levels of complexity are used to realize functions ranging from dc bias generation to high-speed amplification or filtering. The design of op amps continues to pose a challenge as the supply voltage and transistor channel lengths scale down with each generation of CMOS technologies.

This chapter deals with the analysis and design of CMOS op amps. Following a review of performance parameters, we describe simple op amps such as telescopic and folded-cascode topologies. Next, we study two-stage and gain-boosting configurations and the problem of common-mode feedback. Finally, we introduce the concept of slew rate and analyze the effect of supply rejection and noise in op amps. The reader is encouraged to read this chapter before dealing with more advanced designs in Chapter 11.

# **9.1 General Considerations**

We loosely define an op amp as a "high-gain differential amplifier." By "high," we mean a value that is adequate for the application, typically in the range of 101 to 105. Since op amps are usually employed to implement a feedback system, their open-loop gain is chosen according to the precision required of the closed-loop circuit.

Up to three decades ago, most op amps were designed to serve as "general-purpose" building blocks, satisfying the requirements of many different applications. Such efforts sought to create an "ideal" op amp, e.g., with a very high voltage gain (several hundred thousand), high input impedance, and low output impedance, but at the cost of many other aspects of the performance, e.g., speed, output voltage swings, and power dissipation.

By contrast, today's op amp design proceeds with the recognition that the trade-offs between the parameters eventually require a multi dimensional compromise in the overall implementation, making it necessary to know the *adequate* value that must be achieved for each parameter. For example, if the speed is critical while the gain error is not, a topology is chosen that favors the former, possibly sacrificing the latter.

### **9.1.1 Performance Parameters**

In this section, we describe a number of op amp design parameters, providing an understanding of why and where each may become important. For this discussion, we consider the differential cascode circuit

Here is the image describtion:
```
The image depicts a multi-stage CMOS (Complementary Metal-Oxide-Semiconductor) amplifier circuit. The circuit consists of three stages of transistors, each stage containing a pair of MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Transistor Pairs**:
   - The circuit has three pairs of MOSFETs, labeled as M1-M2, M3-M4, and M5-M6, and an additional pair M7-M8 at the top.
   - Each pair of transistors is arranged in a differential configuration.

2. **Bias Voltages**:
   - The gates of M3 and M4 are connected to a bias voltage Vb1.
   - The gates of M5 and M6 are connected to a bias voltage Vb2.
   - The gates of M7 and M8 are connected to a bias voltage Vb3.

3. **Input and Output**:
   - The input signal, Vin, is applied to the gate of M1.
   - The output signal, Vout, is taken from the common node between M5 and M6.

4. **Current Source**:
   - There is a current source, Iss, connected to the source terminals of M1 and M2, providing a constant current to the circuit.

5. **Power Supply**:
   - The circuit is powered by a supply voltage, VDD, connected to the drain terminals of M7 and M8.

6. **Connections**:
   - The source terminals of M1 and M2 are connected together and to the current source Iss.
   - The drain terminals of M1 and M2 are connected to the source terminals of M3 and M4, respectively.
   - The drain terminals of M3 and M4 are connected to the source terminals of M5 and M6, respectively.
   - The drain terminals of M5 and M6 are connected to the source terminals of M7 and M8, respectively.
   - The drain terminals of M7 and M8 are connected to VDD.

This configuration is typically used in analog circuits for amplification purposes, providing high gain and improved performance due to the multiple stages of amplification. The bias voltages Vb1, Vb2, and Vb3 are used to set the operating points of the transistors, ensuring proper operation of the amplifier.
```

Here is the image describtion:
```
The image is a caption for a figure labeled "Figure 9.1" and it describes the content of the figure as a "Cascode op amp." This suggests that the figure itself, which is not shown in the image, likely depicts a cascode operational amplifier circuit. A cascode op amp is a type of amplifier that combines a common-emitter stage with a common-base stage to improve performance characteristics such as gain, bandwidth, and output resistance. The caption indicates that the figure is part of a larger document, likely a textbook or technical paper, discussing electronic circuits or amplifier design.
```

shown in Fig. 9.1 as a representative op amp design.<sup>1</sup> The voltages *Vb*1−*Vb*<sup>3</sup> are generated by the current mirror techniques described in Chapter 5.

**Gain** The open-loop gain of an op amp determines the precision of the feedback system employing the op amp. As mentioned before, the required gain may vary by four orders of magnitude according to the application. Trading with such parameters as speed and output voltage swings, the minimum required gain must therefore be known. As explained in Chapter 14, a high open-loop gain may also be necessary to suppress nonlinearity.

#### ▲**Example 9.1**

The circuit of Fig. 9.2 is designed for a nominal gain of 10, i.e., 1 + *R*1*/R*<sup>2</sup> = 10. Determine the minimum value of *A*<sup>1</sup> for a gain error of 1%.

Here is the image describtion:
```
The image depicts a non-inverting operational amplifier (op-amp) configuration. Here is a detailed description of the circuit:

1. **Operational Amplifier (A1)**: The central component of the circuit is an operational amplifier labeled as A1. It has two input terminals: the inverting input (marked with a minus sign, -) and the non-inverting input (marked with a plus sign, +). The output terminal is labeled as Vout.

2. **Input Voltage (Vin)**: The input voltage, Vin, is applied to the non-inverting input (+) of the op-amp.

3. **Feedback Resistor (R1)**: There is a resistor, R1, connected between the output terminal (Vout) and the inverting input (-) of the op-amp. This resistor is part of the feedback loop that determines the gain of the amplifier.

4. **Grounded Resistor (R2)**: Another resistor, R2, is connected between the inverting input (-) of the op-amp and the ground. This resistor, along with R1, helps set the gain of the amplifier.

5. **Output Voltage (Vout)**: The output voltage, Vout, is taken from the output terminal of the op-amp.

In this configuration, the op-amp amplifies the input voltage (Vin) without inverting its phase. The gain of the amplifier is determined by the values of the resistors R1 and R2. The relationship between the input and output voltages can be expressed as:

\[ V_{out} = V_{in} \left(1 + \frac{R1}{R2}\right) \]

This formula shows that the output voltage is a scaled version of the input voltage, with the scaling factor determined by the ratio of the resistors R1 and R2.
```

**Solution**

The closed-loop gain is obtained from Chapter 8 as

$$\frac{V\_{out}}{V\_{in}} = \frac{A\_1}{1 + \frac{R\_2}{R\_1 + R\_2}A\_1} \tag{9.1}$$

$$\eta = \frac{R\_1 + R\_2}{R\_2} \frac{A\_1}{\frac{R\_1 + R\_2}{R\_2} + A\_1} \tag{9.2}$$

<sup>1</sup>Since op amps of this type have a high output impedance, they are sometimes called "operational transconductance amplifiers" (OTAs). In the limit, the circuit can be represented by a single voltage-dependent current source and called a "*Gm* stage."

Predicting that *A*<sup>1</sup> " 10, we approximate (9.2) as

Razavi-3930640 book December 17, 201516:59 346

$$\frac{V\_{out}}{V\_{in}} \approx \left(1 + \frac{R\_1}{R\_2}\right) \left(1 - \frac{R\_1 + R\_2}{R\_2} \frac{1}{A\_1}\right) \tag{9.3}$$

The term *(R*<sup>1</sup> + *R*2*)/(R*<sup>2</sup> *A*1*)* = *(*1 + *R*1*/R*2*)/A*<sup>1</sup> represents the relative gain error. To achieve a gain error less than 1%, we must have *A*<sup>1</sup> *>* 1000. ▲

It is instructive to compare the circuit of Fig. 9.2 with an open-loop implementation such as that in Fig. 9.3. While it is possible to obtain a nominal gain of *gm RD* = 10 by a common-source stage, it is extremely difficult to guarantee an error less than 1%. The variations in the mobility and gate-oxide thickness of the transistor and the value of the resistor typically yield an error greater than 20%.

Here is the image describtion:
```
The image depicts a simple common-source amplifier stage using a MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor). Here is a detailed description of the circuit:

1. **MOSFET (M1)**: The transistor is labeled as M1. It has three terminals: the gate (G), the drain (D), and the source (S).
   - The gate (G) is connected to the input voltage \( V_{in} \).
   - The source (S) is connected to ground.
   - The drain (D) is connected to a resistor \( R_D \).

2. **Resistor (R_D)**: This resistor is connected between the drain of the MOSFET and the positive supply voltage \( V_{DD} \).

3. **Power Supply (V_{DD})**: This is the positive supply voltage connected to the top of the resistor \( R_D \).

4. **Output Voltage (V_{out})**: The output voltage is taken from the node between the drain of the MOSFET and the resistor \( R_D \).

5. **Ground**: The source of the MOSFET is connected to ground, which is the reference point for the circuit.

The circuit operates as follows:
- The input signal \( V_{in} \) is applied to the gate of the MOSFET.
- The MOSFET amplifies the input signal, and the amplified output signal is taken from the drain, across the resistor \( R_D \).
- The output voltage \( V_{out} \) is inversely related to the input voltage \( V_{in} \) due to the common-source configuration, which typically provides a phase inversion.

This common-source amplifier is a basic building block in analog electronics, used for amplifying small signals.
```

**Small-Signal Bandwidth** The high-frequency behavior of op amps plays a critical role in many applications. For example, as the frequency of operation increases, the open-loop gain begins to drop (Fig. 9.4), creating larger errors in the feedback system. The small-signal bandwidth is usually defined as the "unitygain" frequency, *fu*, which can reach several gigahertz in today's CMOS op amps. The 3-dB frequency, *f*3-dB, may also be specified to allow easier prediction of the closed-loop frequency response.

Here is the image describtion:
```
The image is a graph that illustrates the gain roll-off with frequency. The x-axis represents frequency (f) on a logarithmic scale, while the y-axis represents the gain in decibels, denoted as 20log|A_V|.

The graph starts with a flat region at the left, indicating a constant gain at lower frequencies. This flat region extends up to a point labeled f_3-dB. At f_3-dB, the gain begins to decrease, marking the start of the roll-off. The gain decreases at a certain rate as the frequency increases, forming a downward slope. This slope continues until it reaches a point labeled f_u, beyond which the gain continues to decrease more steeply.

The graph shows that the gain remains constant at lower frequencies, then starts to roll off at f_3-dB, and continues to decrease as the frequency increases further. The point f_3-dB is where the gain has dropped by 3 decibels from its maximum value, and f_u represents the upper cutoff frequency where the gain has significantly decreased.
```

▲**Example 9.2**

In the circuit of Fig. 9.5, assume that the op amp is a single-pole voltage amplifier. If *Vin* is a small step, calculate the time required for the output voltage to reach within 1% of its final value. What unity-gain bandwidth must the

Here is the image describtion:
```
The image consists of two parts: a circuit diagram on the left and a graph on the right.

### Circuit Diagram (Left Side):
1. **Operational Amplifier (Op-Amp)**: The central component is an operational amplifier labeled as \( A(s) \). It has two input terminals and one output terminal.
   - The non-inverting input (+) is connected to the input voltage \( V_{in} \).
   - The inverting input (-) is connected to a resistor \( R_1 \) and a resistor \( R_2 \).

2. **Resistors**:
   - **\( R_1 \)**: This resistor is connected between the inverting input (-) of the op-amp and the output \( V_{out} \).
   - **\( R_2 \)**: This resistor is connected between the inverting input (-) of the op-amp and the ground.

3. **Connections**:
   - The input voltage \( V_{in} \) is applied directly to the non-inverting input (+) of the op-amp.
   - The output voltage \( V_{out} \) is taken from the output terminal of the op-amp.
   - The inverting input (-) is connected to a voltage divider formed by \( R_1 \) and \( R_2 \).

### Graph (Right Side):
1. **Axes**:
   - The horizontal axis represents time \( t \).
   - The vertical axis represents voltage.

2. **Input Voltage \( V_{in} \)**:
   - The input voltage \( V_{in} \) is shown as a step function. It starts at a lower value and then abruptly increases to a higher value at time \( t = 0 \).

3. **Output Voltage \( V_{out} \)**:
   - The output voltage \( V_{out} \) starts at a lower value and then gradually increases, following an exponential curve, to reach a steady-state value after the input voltage step at \( t = 0 \).

### Interpretation:
- The circuit is a non-inverting amplifier configuration with a feedback network consisting of \( R_1 \) and \( R_2 \).
- The graph indicates the response of the output voltage \( V_{out} \) to a step change in the input voltage \( V_{in} \). The output voltage rises exponentially towards a new steady-state value, characteristic of the behavior of an op-amp with feedback.
```

**Figure 9.5**

### Sec. 9.1 General Considerations **347**

Razavi-3930640 book December 17, 201516:59 347

op amp provide if 1 + *R*1*/R*<sup>2</sup> ≈ 10 and the settling time is to be less than 5 ns? For simplicity, assume that the low-frequency gain is much greater than unity.

### **Solution**

Since

$$\left(V\_{in} - V\_{out}\frac{R\_2}{R\_1 + R\_2}\right)A(\mathbf{s}) = V\_{out} \tag{9.4}$$

we have

$$\frac{V\_{out}}{V\_{in}}(s) = \frac{A(s)}{1 + \frac{R\_2}{R\_1 + R\_2}A(s)}\tag{9.5}$$

For a one-pole system, *A(s)* = *A*0*/(*1+*s/*ω0*)*, where ω<sup>0</sup> is the 3-dB bandwidth and *A*0ω<sup>0</sup> the unity-gain bandwidth. Thus,

$$\frac{V\_{out}}{V\_{in}}(s) = \frac{A\_0}{1 + \frac{R\_2}{R\_1 + R\_2}A\_0 + \frac{s}{\alpha\_0}}\tag{9.6}$$

$$t = \frac{\frac{A\_0}{1 + \frac{R\_2}{R\_1 + R\_2} A\_0}}{1 + \frac{s}{\left(1 + \frac{R\_2}{R\_1 + R\_2} A\_0\right) a\_0}}\tag{9.7}$$

indicating that the closed-loop amplifier is also a one-pole system with a time constant equal to

$$\pi = \frac{1}{\left(1 + \frac{R\_2}{R\_1 + R\_2} A\_0\right) \rho\_0} \tag{9.8}$$

Recognizing that the quantity *R*<sup>2</sup> *A*0*/(R*<sup>1</sup> + *R*2*)* is the low-frequency loop gain and usually much greater than unity, we have

$$
\sigma \approx \left( \mathrm{l} + \frac{R\_1}{R\_2} \right) \frac{\mathrm{l}}{A\_0 \omega\_0} \tag{9.9}
$$

The output step response for *Vin* = *au(t)* can now be expressed as

$$V\_{out}(t) \approx a \left( 1 + \frac{R\_1}{R\_2} \right) \left( 1 - \exp\frac{-t}{\tau} \right) u(t) \tag{9.10}$$

with the final value *VF* ≈ *a(*1 + *R*1*/R*2*)*. For 1% settling, *Vout* = 0*.*99*VF* , and hence

$$1\text{ l}-\text{exp}\,\frac{-t\_{1\%}}{\text{tr}}=0.99,\tag{9.11}$$

yielding *t*1% = τ ln 100 ≈ 4*.*6τ . For a 1% settling of 5 ns, τ ≈ 1*.*09 ns, and from (9.9), *A*0ω<sup>0</sup> ≈ *(*1+*R*1*/R*2*)/*τ = 9*.*21 Grad/s (1.47 GHz). ▲

The key point in the above example is that the bandwidth is dictated by both the required settling accuracy (e.g., *Vout* = 0*.*99*VF* ) and the closed-loop gain (1 + *R*1*/R*2).

▲

#### ▲**Example 9.3**

Razavi-3930640 book December 17, 201516:59 348

A student mistakenly swaps the inverting and non-inverting inputs of the op amp in Fig. 9.5. Explain how the circuit behaves.

### **Solution**

Positive feedback may destabilize the circuit. For a one-pole op amp, we have

$$\left(V\_{out}\frac{R\_2}{R\_1+R\_2} - V\_{in}\right)\frac{A\_0}{1+\frac{s}{\alpha\alpha}} = V\_{out}\tag{9.12}$$

and hence

$$\frac{A\_0}{V\_{in}}(s) = \frac{\frac{A\_0}{1 - \frac{R\_2}{R\_1 + R\_2}A\_0}}{1 - \frac{S}{(1 + \frac{R\_2}{R\_1 + R\_2}A\_0)\omega\omega\_0}}\tag{9.13}$$

Interestingly, the closed-loop amplifier contains a pole in the *right half* plane, exhibiting a step response that grows exponentially with time:

$$V\_{out}(t) \approx a \left( \mathbf{l} + \frac{R\_1}{R\_2} \right) \left( \exp\frac{t}{\tau} - \mathbf{l} \right) u(t) \tag{9.14}$$

This growth continues until the op amp output saturates.

**Large-Signal Behavior** In many of today's applications, op amps must operate with large transient signals. Under these conditions, nonlinear phenomena make it difficult to characterize the speed merely by small-signal properties such as the open-loop response shown in Fig. 9.4. As an example, suppose the feedback circuit of Fig. 9.5 incorporates a realistic op amp (i.e., with finite output impedance) while driving a large load capacitance. How does the circuit behave if we apply a 1-V step at the input? Since the output voltage cannot change instantaneously, the voltage difference sensed by the op amp itself at *t* ≥ 0 is equal to 1 V. Such a large difference momentarily drives the op amp into a nonlinear region of operation. (Otherwise, with an open-loop gain of, say, 1000, the op amp would produce 1000 V at the output.)

As explained in Sec. 9.9, the large-signal behavior is usually quite complex, calling for careful simulations.

**Output Swing** Most systems employing op amps require large voltage swings to accommodate a wide range of signal amplitudes. For example, a high-quality microphone that senses the music produced by an orchestra may generate instantaneous voltages that vary by more than four orders of magnitude, demanding that subsequent amplifiers and filters handle large swings (and/or achieve a low noise).

The need for large output swings has made fully differential op amps popular. Similar to the circuits described in Chapter 4, such op amps generate "complementary" outputs, roughly doubling the available swing. Nonetheless, as mentioned in Chapters 3 and 4 and explained later in this chapter, the maximum voltage swing trades with device size and bias currents and hence speed. Achieving large swings is the principal challenge in today's op amp design.

**Linearity** Open-loop op amps suffer from substantial nonlinearity. In the circuit of Fig. 9.1, for example, the input pair *M*1–*M*<sup>2</sup> exhibits a nonlinear relationship between its differential drain current and its input voltage. As explained in Chapter 14, the issue of nonlinearity is tackled by two approaches: using fully

differential implementations to suppress even-order harmonics and allowing sufficient open-loop gain for the closed-loop feedback system to achieve adequate linearity. It is interesting to note that in many feedback circuits, the linearity requirement, rather than the gain error requirement, governs the choice of the open-loop gain.

**Noise and Offset** The input noise and offset of op amps determine the minimum signal level that can be processed with reasonable quality. In a typical op amp topology, several devices contribute noise and offset, necessitating large dimensions or bias currents. For example, in the circuit of Fig. 9.1, *M*1–*M*<sup>2</sup> and *M*7-*M*<sup>8</sup> contribute the most.

We should also recognize a trade-off between noise and *output swing*. For a given bias current, as the overdrive voltage of *M*<sup>7</sup> and *M*<sup>8</sup> in Fig. 9.1 is lowered to allow larger swings at the output, their transconductance increases and so does their drain noise current.

**Supply Rejection** Op amps are often employed in mixed-signal systems and sometimes connected to noisy digital supply lines. Thus, the performance of op amps in the presence of supply noise, especially as the noise frequency increases, is important. For this reason, fully differential topologies are preferred.

# **9.2 One-Stage Op Amps**

# **9.2.1 Basic Topologies**

All of the differential amplifiers studied in Chapters 4 and 5 can be considered op amps. Figure 9.6 shows two such topologies with single-ended and differential outputs. The small-signal, low-frequency gain of both circuits is equal to *gmN (rO N* %*rO P )*, where the subscripts *N* and *P* denote NMOS and PMOS, respectively. This value hardly exceeds 10 in nanometer technologies. The bandwidth is usually determined by the load capacitance, *CL* . Note that the circuit of Fig. 9.6(a) exhibits a mirror pole (Chapter 6) whereas that of Fig. 9.6(b) does not, a critical difference in terms of the stability of feedback systems using these topologies (Chapter 10).

Here is the image describtion:
```
The image shows two different configurations of MOSFET differential amplifier circuits. Let's describe each one in detail:

### Circuit (a):
1. **Transistors**:
   - There are four MOSFETs labeled M1, M2, M3, and M4.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the load transistors.

2. **Connections**:
   - The source terminals of M1 and M2 are connected together and to a current source labeled ISS, which is connected to the ground.
   - The drain of M1 is connected to the drain of M3.
   - The drain of M2 is connected to the drain of M4.
   - The gates of M1 and M2 are the input terminals, with M1 receiving the input signal Vin.
   - The gates of M3 and M4 are connected to their respective drains, indicating that they are configured as active loads (current mirrors).

3. **Power Supply**:
   - The top of the circuit is connected to VDD, the positive power supply voltage.

4. **Output**:
   - The output voltage Vout is taken from the drain of M2 (which is also the drain of M4).
   - A load capacitor CL is connected from the output node to the ground.

### Circuit (b):
1. **Transistors**:
   - There are four MOSFETs labeled M1, M2, M3, and M4.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the load transistors.

2. **Connections**:
   - The source terminals of M1 and M2 are connected together and to a current source labeled ISS, which is connected to the ground.
   - The drain of M1 is connected to the drain of M3.
   - The drain of M2 is connected to the drain of M4.
   - The gates of M1 and M2 are the input terminals, with M1 receiving the input signal Vin1 and M2 receiving the input signal Vin2.
   - The gates of M3 and M4 are connected together and to a bias voltage Vb.

3. **Power Supply**:
   - The top of the circuit is connected to VDD, the positive power supply voltage.

4. **Output**:
   - The output voltages Vout1 and Vout2 are taken from the drains of M1 and M2, respectively.
   - Load capacitors CL are connected from each output node (Vout1 and Vout2) to the ground.

### Summary:
- Both circuits are differential amplifiers using MOSFETs.
- Circuit (a) has a single-ended output, while Circuit (b) has a differential output.
- Circuit (a) uses active loads with the gates of M3 and M4 connected to their drains, whereas Circuit (b) uses a bias voltage Vb for the gates of M3 and M4.
- Both circuits use a current source ISS to set the tail current for the differential pair.
```

**Figure 9.6** Simple op amp topologies.

The circuits of Fig. 9.6 suffer from noise contributions of *M*1–*M*4, as calculated in Chapter 7. Interestingly, in all op amp topologies, at least four devices contribute to the input noise: two input transistors and two "load" transistors.

#### ▲**Example 9.4**

Calculate the input common-mode voltage range and the closed-loop output impedance of the unity-gain buffer depicted in Fig. 9.7.

Here is the image describtion:
```
The image consists of two diagrams. 

The first diagram on the left is a simple operational amplifier (op-amp) circuit. It shows an op-amp with its inverting input (-) connected to its output (V_out), forming a negative feedback loop. The non-inverting input (+) is connected to an input voltage source (V_in).

The second diagram on the right is a more complex circuit, specifically a differential amplifier using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). The circuit is powered by a supply voltage (V_DD) of 1V. The components and their connections are as follows:

- M1 and M2 are NMOS transistors with their sources connected to a current source (I_SS) that is grounded.
- The gate of M1 is connected to the input voltage (V_in).
- The gate of M2 is connected to a reference voltage (not shown in the diagram).
- The drains of M1 and M2 are connected to the sources of PMOS transistors M3 and M4, respectively.
- The gates of M3 and M4 are connected together and to the drain of M4, forming a current mirror.
- The drain of M3 is connected to V_DD.
- The output voltage (V_out) is taken from the drain of M2.

This circuit is a typical differential amplifier configuration used in analog electronics to amplify the difference between two input voltages.
```

### **Solution**

Razavi-3930640 book December 17, 201516:59 350

The minimum allowable input voltage is equal to *VISS* + *VG S*1, where *VISS* is the voltage required across the current source. The maximum voltage is given by the level that places *M*<sup>1</sup> at the edge of the triode region: *Vin,max* = *VDD* − |*VG S*<sup>3</sup>| + *VT H*1. For example, if each device (including the current source) has a threshold voltage of 0.3 V and an overdrive of 0.1 V, then *Vin,min* = 0*.*1 + 0*.*1 + 0*.*3 = 0*.*5 V and *Vin,max* = 1 − *(*0*.*1 + 0*.*3*)* + 0*.*3 = 0*.*9 V. Thus, the input CM range equals 0.4 V with a 1-V supply.

Since the circuit employs voltage feedback at the output, the output impedance is equal to the open-loop value, *rO P* %*rO N* , divided by one plus the loop gain, 1 + *gmN (rO P* %*rO N )*. In other words, for large open-loop gain, the closed-loop output impedance is approximately equal to *(rO P* %*rO N )/*[*gmN (rO P* %*rO N )*] = 1*/gmN* .

It is interesting to note that the closed-loop output impedance is relatively *independent* of the open-loop output impedance. This is an important observation, allowing us to design high-gain op amps by *increasing* the open-loop output impedance while still achieving a relatively low closed-loop output impedance. We also observe that, if driving a load capacitance of *CL* , the op amp incurs a closed-loop output pole approximately given by *gmN /CL* . ▲

In order to achieve a high gain, the differential cascode topologies of Chapters 4 and 5 can be used. Shown in Figs. 9.8(a) and (b) for single-ended and differential output generation, respectively, such circuits display a gain on the order of *gmN* [*(gmNr* <sup>2</sup> *O N )*%*(gm Pr* <sup>2</sup> *O P )*], but at the cost of output swing and

Here is the image describtion:
```
The image shows two different configurations of a CMOS (Complementary Metal-Oxide-Semiconductor) amplifier circuit. Both circuits are differential amplifiers with additional stages for increased gain or other performance enhancements. Let's describe each circuit in detail:

### Circuit (a):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the input differential pair. The gate of M1 is connected to the input voltage \( V_{in} \), and the gate of M2 is connected to a reference voltage.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair M1 and M2. The gates of M3 and M4 are connected to a bias voltage \( V_b \).
   - **M5 and M6:** These are NMOS transistors forming a current mirror load for the differential pair. The source of M5 is connected to the drain of M3, and the source of M6 is connected to the drain of M4. The gates of M5 and M6 are connected together and to the drain of M5.
   - **M7 and M8:** These are PMOS transistors forming another current mirror stage. The source of M7 is connected to \( V_{DD} \), and the source of M8 is also connected to \( V_{DD} \). The gates of M7 and M8 are connected together and to the drain of M7. The drain of M8 is connected to the output \( V_{out} \).

2. **Nodes:**
   - **X:** The node between the drain of M7 and the gate of M8.
   - **Y:** The node between the drain of M5 and the gate of M6.

3. **Current Source:**
   - **I_{SS}:** A current source connected to the common source node of M1 and M2, providing the tail current for the differential pair.

### Circuit (b):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the input differential pair, similar to circuit (a). The gate of M1 is connected to the input voltage \( V_{in} \), and the gate of M2 is connected to a reference voltage.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair M1 and M2. The gates of M3 and M4 are connected to a bias voltage \( V_{b1} \).
   - **M5 and M6:** These are NMOS transistors forming a current mirror load for the differential pair. The source of M5 is connected to the drain of M3, and the source of M6 is connected to the drain of M4. The gates of M5 and M6 are connected together and to the drain of M5. The gates of M5 and M6 are connected to a bias voltage \( V_{b2} \).
   - **M7 and M8:** These are PMOS transistors forming another current mirror stage. The source of M7 is connected to \( V_{DD} \), and the source of M8 is also connected to \( V_{DD} \). The gates of M7 and M8 are connected together and to the drain of M7. The gates of M7 and M8 are connected to a bias voltage \( V_{b3} \). The drain of M8 is connected to the output \( V_{out} \).

2. **Current Source:**
   - **I_{SS}:** A current source connected to the common source node of M1 and M2, providing the tail current for the differential pair.

### Key Differences:
- In circuit (a), the gates of M5 and M6, as well as M7 and M8, are connected to the drains of M5 and M7, respectively, forming self-biased current mirrors.
- In circuit (b), the gates of M5 and M6, as well as M7 and M8, are connected to external bias voltages \( V_{b2} \) and \( V_{b3} \), respectively, allowing for more precise control of the operating points of these transistors.

Both circuits are designed to amplify the differential input signal \( V_{in} \) and provide a single-ended output \( V_{out} \). The additional stages in each circuit are intended to enhance the gain and performance of the amplifier.
```

**Figure 9.8** Cascode op amps.

additional poles. These configurations are also called "telescopic" cascode op amps to distinguish them from another cascode op amp described below. The circuit providing a single-ended output suffers from a mirror pole at node *X* (and a pole at *Y* ), creating stability issues (Chapter 10).

As calculated in Chapter 4 , the output swings of telescopic op amps are relatively limited. In the fully differential version of Fig. 9.8(b), for example, the output swing is given by 2[*VDD* − *(VO D*<sup>1</sup> + *VO D*<sup>3</sup> + *VISS* + |*VO D*5|+|*VO D*7|*)*], where *VODj* denotes the overdrive voltage of *Mj* and *VISS* the minimum allowable voltage across *ISS*. We must recognize the three conditions necessary for allowing this much swing: (1) the input CM level, *Vin,C M* , is chosen *low* enough and equal to *VG S*<sup>1</sup> + *VISS*, (2) *Vb*<sup>1</sup> is also chosen low enough and equal to *VG S*<sup>3</sup> + *(Vin,C M* − *VT H*1*)*, placing *M*<sup>1</sup> at the edge of saturation, and (3) *Vb*<sup>2</sup> is chosen high enough and equal to *VDD* − |*VO D*7| − |*VG S*5|, placing *M*<sup>7</sup> at the edge of saturation. Thus, *Vin,C M* (and *Vb*<sup>1</sup> and *Vb*2) must be controlled tightly, a serious issue.

Another drawback of telescopic cascodes is the difficulty in shorting their inputs and outputs, e.g., to implement a unity-gain buffer similar to the circuit of Fig. 9.7. To understand the issue, let us consider the unity-gain feedback topology shown in Fig. 9.9. Under what conditions are both *M*<sup>2</sup> and *M*<sup>4</sup> in saturation? We must have *Vout* ≤ *VX* +*VT H*<sup>2</sup> and *Vout* ≥ *Vb* −*VT H*4. Since *VX* = *Vb* −*VG S*4, *Vb* −*VT H*<sup>4</sup> ≤ *Vout* ≤ *Vb* − *VG S*<sup>4</sup> + *VT H*2. Depicted in Fig. 9.9, this voltage range is simply equal to *Vmax* − *Vmin* = *VT H*<sup>4</sup> − *(VG S*<sup>4</sup> − *VT H*2*)* (one threshold minus one overdrive), maximized by minimizing the overdrive of *M*<sup>4</sup> but always less than *VT H*2.

Here is the image describtion:
```
The image consists of two parts: a schematic diagram of a telescopic cascode operational amplifier (op-amp) and a graphical representation of the allowable voltage range for the circuit.

### Schematic Diagram:
1. **Transistors:**
   - The circuit includes eight MOSFET transistors labeled M1 through M8.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the cascode transistors for M1 and M2, respectively.
   - M5 and M6 are the load transistors.
   - M7 and M8 are the cascode transistors for M5 and M6, respectively.

2. **Connections:**
   - The source of M1 is connected to a current source labeled I_SS, which is connected to ground.
   - The gate of M1 is connected to the input voltage V_in.
   - The source of M2 is also connected to the current source I_SS.
   - The gate of M2 is connected to node X.
   - The drain of M1 is connected to the source of M3.
   - The drain of M2 is connected to the source of M4.
   - The gates of M3 and M4 are connected to a bias voltage V_b.
   - The drain of M3 is connected to the source of M5.
   - The drain of M4 is connected to the source of M6.
   - The gates of M5 and M6 are connected to the drains of M7 and M8, respectively.
   - The sources of M7 and M8 are connected to V_DD.
   - The drain of M5 is connected to the source of M7.
   - The drain of M6 is connected to the source of M8.
   - The output voltage V_out is taken from the drain of M6.

### Graphical Representation:
- The graph shows the allowable range for the voltage at node X.
- The vertical axis represents voltage levels.
- The horizontal axis represents the bias voltage V_b.
- The allowable range is shown as a shaded region.
- The upper limit of the allowable range is V_b.
- The lower limit of the allowable range is V_b - V_TH4, where V_TH4 is the threshold voltage of transistor M4.
- The height of the allowable range is V_GS4 - V_TH2, where V_GS4 is the gate-source voltage of transistor M4 and V_TH2 is the threshold voltage of transistor M2.

### Labels:
- V_DD: Supply voltage.
- V_b: Bias voltage.
- V_in: Input voltage.
- V_out: Output voltage.
- I_SS: Current source.
- V_GS4: Gate-source voltage of M4.
- V_TH2: Threshold voltage of M2.
- V_TH4: Threshold voltage of M4.

### Figure Caption:
- The figure is labeled as "Figure 9.9 Telescopic cascode op-amp with input and output shorted."

This detailed description covers the components, connections, and the graphical representation of the allowable voltage range in the telescopic cascode op-amp circuit.
```

**Figure 9.9** Telescopic cascode op amp with input and output shorted.

#### ▲**Example 9.5**

For the circuit of Fig. 9.9, explain in which region each transistor operates as *Vin* varies from below *Vb* − *VT H*<sup>4</sup> to above *Vb* − *VG S*<sup>4</sup> + *VT H*2.

### **Solution**

Since the op amp attempts to force *Vout* to be equal to *Vin*, for *Vin < Vb* − *VT H*4, we have *Vout* ≈ *Vin*, and *M*<sup>4</sup> is in the triode region while other transistors are saturated. Under this condition, the open-loop gain of the op amp is reduced.

As *Vin* and hence *Vout* exceed *Vb* − *VT H*4, *M*<sup>4</sup> enters saturation and the open-loop gain reaches a maximum. For *Vb* − *VT H*<sup>4</sup> *< Vin < Vb* − *(VG S*<sup>4</sup> − *VT H*2*)*, both *M*<sup>2</sup> and *M*<sup>4</sup> are saturated, and for *Vin > Vb* − *(VG S*<sup>4</sup> − *VT H*2*)*, *M*<sup>2</sup> and *M*<sup>1</sup> enter the triode region, degrading the gain.

▲

While a cascode op amp is rarely used as a unity-gain buffer, some other topologies (such as the switched-capacitor circuits of Chapter 13) reduce to the configuration shown in Fig. 9.9 for part of their operation period, as illustrated by the following example.

#### ▲**Example 9.6**

Razavi-3930640 book December 17, 201516:59 352

Figure 9.10(a) shows a closed-loop amplifier utilizing a telescopic op amp.<sup>2</sup> Assuming that the op amp has a high open-loop gain, determine the maximum allowable output voltage swing.

Here is the image describtion:
```
The image consists of four parts labeled (a), (b), (c), and (d), each depicting different aspects of electronic circuits and their behavior.

(a) The first part shows a differential amplifier circuit using an operational amplifier (op-amp). The circuit includes resistors R1, R2, R3, and R4. The non-inverting input of the op-amp is connected to a voltage source through resistor R2, and the inverting input is connected to another voltage source through resistor R1. Resistor R3 is connected between the output of the op-amp and the inverting input, forming a feedback loop. Resistor R4 is connected between the non-inverting input and ground.

(b) The second part shows a MOSFET-based differential amplifier circuit. It includes four MOSFETs labeled M1, M2, M3, and M4. The sources of M1 and M2 are connected to a current source that is grounded. The gates of M1 and M2 are connected to the input signals through capacitors. The drains of M1 and M2 are connected to the sources of M3 and M4, respectively. The gates of M3 and M4 are connected to a bias voltage Vb through resistor R3. The drains of M3 and M4 are connected to the output nodes X and Y, respectively. Resistor R4 is connected between the drain of M4 and the output node Y, and another resistor R2 is connected between the output node Y and ground.

(c) The third part shows a graph of the voltage VX versus time t. The graph indicates the behavior of VX with respect to a common-mode voltage VCM and a threshold voltage Vb - VTH3,4. The graph shows that when VX is above VCM, M3 and M4 are in the triode region. The waveform of VX oscillates around VCM and reaches a peak value above VCM and a minimum value below VCM.

(d) The fourth part shows another graph of the voltage VX versus time t. This graph also indicates the behavior of VX with respect to VCM, Vb - (VGS3,4 - VTH1,2), and Vb - VTH3,4. The waveform of VX oscillates around VCM, reaching a peak value above VCM and a minimum value below VCM. The graph shows the voltage levels Vb - (VGS3,4 - VTH1,2) and Vb - VTH3,4 as reference points for the behavior of VX.

Overall, the image illustrates the design and behavior of differential amplifier circuits using both op-amps and MOSFETs, along with the corresponding voltage waveforms and operating regions of the transistors.
```

### **Solution**

Let us draw the circuit as shown in Fig. 9.10(b), noting that its input and output common-mode levels are equal (why?). Recall from the foregoing discussion that the voltage at the drains of *M*<sup>3</sup> and *M*<sup>4</sup> is bounded by *Vb* − *VT H*<sup>3</sup>*,*<sup>4</sup> to keep *M*<sup>3</sup> and *M*<sup>4</sup> in saturation and *Vb* − *(VG S*<sup>3</sup>*,*<sup>4</sup> − *VT H*<sup>1</sup>*,*2*)* to keep *M*<sup>1</sup> and *M*<sup>2</sup> in saturation. How should we set the output CM level, *VC M* , in this range to maximize the output swing? If *VC M* = *Vb* − *VT H*<sup>3</sup>*,*4, then *M*<sup>3</sup> and *M*<sup>4</sup> reside at the edge of the triode region and cannot tolerate any *downward* swing [Fig. 9.10(c)]. On the other hand, if we select *VC M* = *Vb* − *(VG S*<sup>3</sup>*,*<sup>4</sup> − *VT H*<sup>1</sup>*,*2*)* (placing *M*<sup>1</sup> and *M*<sup>2</sup> at the edge), then *VX* or *VY* can fall to *Vb* − *VT H*<sup>3</sup>*,*<sup>4</sup> while maintaining *M*<sup>3</sup> and *M*<sup>4</sup> in saturation [Fig. 9.10(d)].

With the latter choice, how *high* can *VX* or *VY* go? If the gain of the op amp is large, the gate voltages of *M*<sup>1</sup> and *M*<sup>2</sup> swing negligibly. Thus, *VX* and *VY* can arbitrarily rise from *VC M* = *Vb* − *(VG S*<sup>3</sup>*,*<sup>4</sup> − *VT H*<sup>1</sup>*,*2*)* without driving *M*<sup>1</sup> and *M*<sup>2</sup> into the triode region. (Of course, the PMOS loads constrain the upswing.) For symmetric up- and downswings, therefore, the circuit allows a voltage excursion of ±(one threshold − one overdrive) around *VC M* . ▲

<sup>2</sup>The input capacitors ensure that the bias conditions are not disturbed by the preceding stage.

# **9.2.2 Design Procedure**

Razavi-3930640 book December 17, 201516:59 353

At this point, the reader may wonder how exactly we design an op amp. With so many devices and performance parameters, it may not be clear where the starting point is and how the numbers are chosen. Indeed, the actual design methodology of an op amp somewhat depends on the specifications that the circuit must meet. For example, a high-gain op amp may be designed quite differently from a low-noise op amp. Nevertheless, in most cases, some aspects of the performance, e.g., output voltage swings and open-loop gain, are of primary concern, pointing to a specific design procedure. We will deal extensively with five parameters for each transistor: *ID*, *VG S* − *VT H* , *W/L*, *gm*, and *rO* .

In the design of op amps (and many other circuits), it is helpful to begin with a power budget, even if none is specified. As seen later in this section, the resulting design can readily be "scaled" for lower or higher power dissipations. We describe a simple design here and deal with nanometer op amps in Chapter 11.

#### ▲**Example 9.7**

Design a fully differential telescopic op amp with the following specifications: *VDD* = 3 V, peak-to-peak differential output swing <sup>=</sup> 3 V, power dissipation <sup>=</sup> 10 mW, voltage gain <sup>=</sup> 2000. Assume that *<sup>µ</sup>nCox* <sup>=</sup> <sup>60</sup> *<sup>µ</sup>*A/V2, *<sup>µ</sup>pCox* <sup>=</sup> <sup>30</sup> *<sup>µ</sup>*A/V2, <sup>λ</sup>*<sup>n</sup>* <sup>=</sup> <sup>0</sup>*.*1 V−1, <sup>λ</sup>*<sup>p</sup>* <sup>=</sup> <sup>0</sup>*.*2 V−<sup>1</sup> (for an effective channel length of 0*.*<sup>5</sup> *<sup>µ</sup>*m), <sup>γ</sup> <sup>=</sup> 0, and *VTHN* = |*VTHP* | = 0*.*7 V.

### **Solution**

Figure 9.11 shows the op amp topology along with two current mirrors defining the drain currents of *M*7–*M*9.We begin with the power budget, allocating 3 mA to *M*<sup>9</sup> and the remaining 330 *µ*A to *Mb*<sup>1</sup> and *Mb*2. Thus, each cascode branch of the op amp carries a current of 1.5 mA. Next, we consider the required output swings. Each of nodes *X* and *Y* must be able to swing by 1.5 V*pp* without driving *M*3–*M*<sup>6</sup> into the triode region. With a 3-V supply, therefore, the total voltage available for *M*<sup>9</sup> and each cascode branch is equal to 1.5 V, i.e., |*VO D*<sup>7</sup>|+|*VO D*<sup>5</sup>| + *VO D*<sup>3</sup> + *VO D*<sup>1</sup> + *VO D*<sup>9</sup> = 1*.*5 V.

Here is the image describtion:
```
The image depicts a schematic diagram of a CMOS operational amplifier (op-amp) circuit. The circuit consists of multiple MOSFET transistors arranged in a specific configuration to achieve amplification. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1, M2, M3, M4, M5, M6, M7, M8, Mb1, Mb2, M9**: These are all MOSFET transistors. The transistors are labeled with 'M' followed by a number or letter to distinguish them.

2. **Current Sources:**
   - **I_REF1 and I_REF2**: These are current sources providing reference currents to the circuit.

3. **Voltage Nodes:**
   - **V_in**: This is the input voltage node.
   - **V_out**: This is the output voltage node.
   - **V_b1 and V_b2**: These are bias voltages applied to the gates of certain transistors to set their operating points.
   - **V_DD**: This is the positive supply voltage.

4. **Connections:**
   - **Mb1 and Mb2**: These transistors are connected to the current sources I_REF1 and I_REF2, respectively. They are likely used for biasing purposes.
   - **M1 and M2**: These transistors form a differential pair with their sources connected together and to the drain of M9.
   - **M3 and M4**: These transistors are connected as active loads for the differential pair M1 and M2.
   - **M5 and M6**: These transistors are connected in a similar manner to M3 and M4, forming another stage of amplification.
   - **M7 and M8**: These transistors are connected to the positive supply voltage V_DD and act as current mirrors or active loads for M5 and M6.
   - **M9**: This transistor is connected to the sources of M1 and M2 and to ground, likely serving as a current source or sink.

5. **Nodes X and Y**: These are intermediate nodes in the circuit, with node X being the output of the first differential pair (M1, M2) and node Y being the output of the second stage (M5, M6).

The overall configuration suggests a multi-stage amplifier with differential input (M1, M2) and multiple gain stages (M3, M4, M5, M6) to achieve high gain. The use of current mirrors (M7, M8) and biasing transistors (Mb1, Mb2) helps in setting the operating points and ensuring proper functionality of the amplifier.
```

Since *M*<sup>9</sup> carries the largest current, we choose *VO D*<sup>9</sup> ≈ 0*.*5 V, leaving 1 V for the four transistors in the cascode. Moreover, since *M*5–*M*<sup>8</sup> suffer from low mobility, we allocate an overdrive of approximately 300 mV to each, obtaining 400 mV for *VO D*<sup>1</sup> + *VO D*3. As an initial guess, *VO D*<sup>1</sup> = *VO D*<sup>3</sup> = 200 mV.

With the bias current and overdrive voltage of each transistor known, we can easily determine the aspect ratios from *ID* <sup>=</sup> *(*1*/*2*)µCox (W/L)(VG S* <sup>−</sup> *VT H )*<sup>2</sup> or simulated I/V characteristics. To minimize the device capacitances, we choose the minimum length for each transistor, obtaining a corresponding width. We then have *(W/L)*1−<sup>4</sup> = 1250, and *(W/L)*5−<sup>8</sup> = 1111*,* and *(W/L)*<sup>9</sup> = 400.

▲

The reader may think that the above choice of overdrives is arbitrary and leads to a wide design space. However, we must emphasize that each of the overdrives has but a small range. For example, we can change the allocated values by only a few tens of millivolts before the device dimensions become disproportionately large.

The design has thus far satisfied the swing, power dissipation, and supply voltage specifications. But, how about the gain? Using *A<sup>v</sup>* ≈ *gm*1[*(gm*3*rO*3*rO*1*)*%*(gm*5*rO*5*rO*7*)*] and assuming minimum channel length for all of the transistors, we have *A<sup>v</sup>* = 1416, quite a lot lower than the required value.

In order to increase the gain, we recognize that *gmrO* <sup>=</sup> <sup>√</sup>2*µCox (W/L)ID/(*λ*ID)*. Now, recall that <sup>λ</sup> <sup>∝</sup> <sup>1</sup>*/L*, and hence *gmrO* <sup>∝</sup> <sup>√</sup>*W L/ID*. We can therefore increase the width or length or *decrease* the bias current of the transistors. In practice, speed or noise requirements may dictate the bias current, leaving only the dimensions as the variables. Of course, the width of each transistor must at least scale with its length so as to maintain a constant overdrive voltage.

Which transistors in the circuit of Fig. 9.11 should be made longer? Since *M*1–*M*<sup>4</sup> appear in the signal path, it is desirable to keep their capacitances to a minimum. The PMOS devices, *M*5–*M*8, on the other hand, affect the signal to a much lesser extent and can therefore have larger dimensions.3 Doubling the (effective) length and width of each of these transistors in fact *doubles* their *gmrO* because *gm* remains constant while *rO* increases by a factor of 2. Choosing *(W/L)*5−<sup>8</sup> <sup>=</sup> <sup>2222</sup> *<sup>µ</sup>*m*/*1*.*<sup>0</sup> *<sup>µ</sup>*m and hence <sup>λ</sup>*<sup>p</sup>* <sup>=</sup> <sup>0</sup>*.*1 V−1, we obtain *<sup>A</sup><sup>v</sup>* <sup>≈</sup> 4000. Thus, the PMOS dimensions can be somewhat smaller. Note that with such large dimensions for PMOS transistors, we may revisit our earlier distribution of the overdrive voltages, possibly reducing that of *M*<sup>9</sup> by 100 to 200 mV and allocating more to the PMOS devices.

In the op amp of Fig. 9.11, the input CM level and the bias voltages *Vb*<sup>1</sup> and *Vb*<sup>2</sup> must be chosen so as to allow maximum output swings. The minimum allowable input CM level equals *VG S*<sup>1</sup> +*VO D*<sup>9</sup> = *VT H*<sup>1</sup> +*VO D*<sup>1</sup> +*VO D*<sup>9</sup> = 1*.*4 V. The minimum value of *Vb*<sup>1</sup> is given by *VG S*<sup>3</sup> + *VO D*<sup>1</sup> + *VO D*<sup>9</sup> = 1*.*6 V, placing *M*1–*M*<sup>2</sup> at the edge of the triode region. Similarly, *Vb*<sup>2</sup>*,max* = *VDD* − *(*|*VG S*<sup>5</sup>|+|*VO D*<sup>7</sup>|*)* = 1*.*7 V. In practice, some margin must be included in the value of *Vb*<sup>1</sup> and *Vb*<sup>2</sup> to allow for process variations. Also, the increase in the threshold voltages due to body effect must be taken into account. Finally, we should remark that this op amp requires common-mode feedback (CMFB) (Section 9.7). ▲

### **9.2.3 Linear Scaling**

How do we modify the above design if the power budget is different but all other specifications remain the same? Suppose we are allowed to double the power dissipation and hence the bias current of each transistor. The key concept behind "linear scaling" is to double the widths of all of the transistors in the circuit while keeping the lengths constant. Returning to our five device design parameters, we observe that, in this example, (1) *ID* is doubled, (2) *W/L* is doubled, (3) *VG S* − *VT H* is *constant*, and so are the allowable voltage swings, (4) *gm* is *doubled* because both the bias current and the width are doubled (as if two identical transistors were placed in parallel), and (5) *rO* is halved (for the same reason that *gm* is doubled). We therefore conclude that linear scaling by adjusting the transistor widths simply scales the power dissipation while retaining the gain and swing values. This concept is used in Chapter 11 to optimize the performance of op amps.

#### ▲**Example 9.8**

An engineer seeking a low-power op amp design scales down the transistor widths in Example 9.7 by a factor of 10. Explain what aspects of the performance degrade.

### **Solution**

Since the *gm* of each transistor falls by a factor of 10, two aspects are sacrificed: (1) the speed of the op amp in driving a capacitive load (e.g., the output pole in Example 9.4) degrades proportionally, and (2) the input-referred noise voltage of the op amp rises by a factor of <sup>√</sup>10 (Sec. 9.12).

<sup>3</sup>This point is studied in Chapter 10.

In nanometer technologies, op amp design can still follow the above procedure, but with greater reliance on simulated device characteristics. Unfortunately, the lower supply voltage severely limits the output swing, making the telescopic cascode less attractive. We return to these points in Chapter 11.

The gate bias voltages *Vb*<sup>1</sup> and *Vb*<sup>2</sup> in the telescopic cascode of Fig. 9.11 must be generated with some precision. We note that if, for example, *Vb*<sup>1</sup> is less than its nominal value, then *M*<sup>1</sup> and *M*<sup>2</sup> enter the triode region. The same occurs even if *Vb*<sup>1</sup> is fixed, but the input CM level is slightly higher than expected. To ensure that *Vb*<sup>1</sup> "tracks" the input CM level, we can generate *Vb*<sup>1</sup> as shown in Fig. 9.12(a). Here, a small current *I*<sup>1</sup> flows through the diode-connected device, *Mb*1, producing *Vb*<sup>1</sup> = *VP* + *VG S,<sup>b</sup>*1. Since *VP* tracks the input CM level (*VP* = *Vin,C M* − *VG S*<sup>1</sup>*,*2), we have

$$V\_{b1} = V\_{in,CM} - V\_{GS1,2} + V\_{GS,b1} \tag{9.15}$$

which should be chosen equal to *Vin,C M* − *VT H*<sup>1</sup>*,*<sup>2</sup> + *VG S*<sup>3</sup>*,*<sup>4</sup> to allow *M*<sup>1</sup> and *M*<sup>2</sup> to operate in saturation. It follows that

$$V\_{GS,b1} = (V\_{GS1,2} - V\_{TH1,2}) + V\_{GS3,4} \tag{9.16}$$

indicating that *Mb*<sup>1</sup> must be "weak" enough to sustain a *VG S* equal to one overdrive plus the gate-source voltage of *M*<sup>3</sup> and *M*4. This is accomplished by choosing *Mb*<sup>1</sup> to be a narrrow, long device.

Here is the image describtion:
```
The image depicts a circuit diagram used for the generation of a cascode gate voltage. The circuit consists of several MOSFET transistors and current sources. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors with their sources connected to a common node labeled "P," which is also connected to a current source \( I_{SS} \) that goes to ground.
   - **M3 and M4:** These are PMOS transistors with their sources connected to the supply voltage \( V_{DD} \).
   - **M_{b1}:** This is an NMOS transistor with its source connected to the common node "P" and its gate connected to its drain, forming a diode-connected configuration.

2. **Current Sources:**
   - **I1:** This current source is connected between the supply voltage \( V_{DD} \) and the drain of M3.
   - **I_{SS}:** This current source is connected between the common node "P" and ground.

3. **Connections:**
   - The gate of M3 is connected to the gate of M4, and this common gate voltage is labeled \( V_{b1} \).
   - The drain of M3 is connected to the gate of M_{b1} and the drain of M_{b1}.
   - The drain of M4 is connected to the drain of M2.
   - The source of M1 and M2 are connected to the common node "P."

4. **Voltage Labels:**
   - \( V_{DD} \) is the supply voltage.
   - \( V_{b1} \) is the gate voltage for the cascode transistors M3 and M4.
   - \( P \) is the common node where the sources of M1 and M2 are connected.

The circuit is designed to generate a stable gate voltage \( V_{b1} \) for the cascode transistors M3 and M4, which is crucial for maintaining the proper operation of the cascode configuration in analog circuits. The current sources \( I1 \) and \( I_{SS} \) help in setting the operating point of the transistors.
```

### **9.2.4 Folded-Cascode Op Amps**

In order to alleviate the drawbacks of telescopic cascode op amps, namely, limited output swings and difficulty in choosing equal input and output CM levels, a "folded-cascode" op amp can be used. As described in Chapter 3 and illustrated in Fig. 9.13, in an NMOS or PMOS cascode amplifier, the input device is replaced by the opposite type while still converting the input voltage to a current. In the four circuits shown in Fig. 9.13, the small-signal current generated by *M*<sup>1</sup> flows through *M*<sup>2</sup> and subsequently the load, producing an output voltage approximately equal to *gm*1*RoutVin*. The primary advantage of the folded structure lies in the choice of the voltage levels because it does not "stack" the cascode transistor on top of the input device. We will return to this point later.

The folding idea depicted in Fig. 9.13 can easily be applied to differential pairs, and hence to operational amplifiers as well. Shown in Fig. 9.14, the resulting circuit replaces the input NMOS pair with a PMOS counterpart. Note two important differences between the two circuits. (1) In Fig. 9.14(a), one bias current, *ISS*, provides the drain current of both the input transistors and the cascode devices, whereas in Fig. 9.14(b), the input pair requires an additional bias current. In other words, *ISS*<sup>1</sup> = *ISS/*2+ *ID*<sup>3</sup> = *ISS/*2+ *I*1. Thus, the folded-cascode configuration generally consumes more power. (2) In Fig. 9.14(a), the input CM level

Here is the image describtion:
```
The image consists of two parts, labeled (a) and (b), each showing a pair of circuit diagrams. These diagrams illustrate different configurations of MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) circuits.

### Part (a):
1. **Left Diagram:**
   - This circuit has two MOSFETs, labeled M1 and M2.
   - The source of M1 is connected to ground.
   - The gate of M1 is connected to an input voltage, Vin.
   - The drain of M1 is connected to the source of M2.
   - The gate of M2 is connected to a bias voltage, Vb.
   - The drain of M2 is connected to a current source, I1, which is connected to VDD (the supply voltage).
   - The output voltage, Vout, is taken from the drain of M2.

2. **Right Diagram:**
   - This circuit is a rearranged version of the left diagram.
   - The source of M1 is still connected to ground.
   - The gate of M1 is connected to Vin.
   - The drain of M1 is connected to the drain of M2.
   - The source of M2 is connected to a current source, I2, which is connected to ground.
   - The gate of M2 is connected to Vb.
   - The output voltage, Vout, is taken from the common drain connection of M1 and M2.
   - The drain of M2 is also connected to VDD through a current source, I1.

### Part (b):
1. **Left Diagram:**
   - This circuit has two MOSFETs, labeled M1 and M2.
   - The source of M1 is connected to ground.
   - The gate of M1 is connected to Vin.
   - The drain of M1 is connected to the source of M2.
   - The gate of M2 is connected to Vb.
   - The drain of M2 is connected to a current source, I1, which is connected to VDD.
   - The output voltage, Vout, is taken from the drain of M2.

2. **Right Diagram:**
   - This circuit is a rearranged version of the left diagram.
   - The source of M1 is connected to ground.
   - The gate of M1 is connected to Vin.
   - The drain of M1 is connected to the source of M2.
   - The gate of M2 is connected to Vb.
   - The drain of M2 is connected to a current source, I2, which is connected to VDD.
   - The output voltage, Vout, is taken from the source of M2.
   - The drain of M1 is also connected to a current source, I1, which is connected to ground.

In summary, the image shows different configurations of MOSFET circuits with current sources and how they can be rearranged while maintaining the same basic functionality.
```

**Figure 9.13** Folded-cascode amplifiers.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), which appear to be different configurations of a differential amplifier with current mirror loads.

### Circuit (a):
1. **Transistors:**
   - There are four MOSFETs labeled M1, M2, M3, and M4.
   - M1 and M2 form the differential pair.
   - M3 and M4 are the load transistors.

2. **Current Sources:**
   - There are three current sources labeled I1, I2, and Iss.
   - I1 and I2 are connected to the drains of M3 and M4, respectively, and to the positive supply voltage V_DD.
   - Iss is connected to the common source node of M1 and M2 and to ground.

3. **Voltage Inputs:**
   - The gate of M1 is connected to the input voltage Vin.
   - The gate of M2 is connected to a bias voltage Vb1.

4. **Output:**
   - The output voltage Vout is taken from the common node between the drains of M3 and M4.

### Circuit (b):
1. **Transistors:**
   - Similar to circuit (a), there are four MOSFETs labeled M1, M2, M3, and M4.
   - M1 and M2 form the differential pair.
   - M3 and M4 are the load transistors.

2. **Current Sources:**
   - There are four current sources labeled I1, I2, Iss, Iss1, and Iss2.
   - I1 and I2 are connected to the drains of M3 and M4, respectively, and to the positive supply voltage V_DD.
   - Iss is connected to the common source node of M1 and M2 and to the positive supply voltage V_DD.
   - Iss1 and Iss2 are connected to the sources of M3 and M4, respectively, and to ground.

3. **Voltage Inputs:**
   - The gate of M1 is connected to the input voltage Vin.
   - The gate of M2 is connected to a bias voltage Vb1.

4. **Output:**
   - The output voltage Vout is taken from the common node between the drains of M3 and M4.

### Differences between (a) and (b):
- In circuit (a), the current source Iss is connected to the common source node of M1 and M2 and to ground, whereas in circuit (b), Iss is connected to the common source node of M1 and M2 and to the positive supply voltage V_DD.
- Circuit (b) includes additional current sources Iss1 and Iss2 connected to the sources of M3 and M4, respectively, which are not present in circuit (a).

These circuits are likely used in analog signal processing, where the differential pair (M1 and M2) amplifies the difference between the input signals, and the current mirror loads (M3 and M4) help in achieving high gain and proper biasing.
```

**Figure 9.14** (a) Telescopic and (b) folded-cascode op amp topologies.

cannot exceed *Vb*<sup>1</sup> − *VG S*<sup>3</sup> + *VT H*1, whereas in Fig. 9.14(b), it cannot be *less* than *Vb*<sup>1</sup> − *VG S*<sup>3</sup> − |*VTHP* |. It is therefore possible to design the latter to allow shorting its input and output terminals with negligible swing limitation. This is in contrast to the behavior depicted in Fig. 9.9. In Fig. 9.14(b), it is possible to tie the *n*-wells of *M*<sup>1</sup> and *M*<sup>2</sup> to their common source point. We return to this idea in Chapters 14 and 19.

Let us now calculate the maximum output voltage swing of the folded-cascode op amp shown in Fig. 9.15, where *M*5–*M*<sup>10</sup> replace the ideal current sources of Fig. 9.14(b). With proper choice of *Vb*<sup>1</sup> and *Vb*2, the lower end of the swing is given by *VO D*<sup>3</sup> + *VO D*<sup>5</sup> and the upper end by *VDD* −*(*|*VO D*7|+|*VO D*9|*)*. Thus, the peak-to-peak swing on each side is equal to *VDD* − *(VO D*<sup>3</sup> + *VO D*<sup>5</sup> + |*VO D*7|+|*VO D*9|*)*. In the telescopic cascode of Fig. 9.14(a), on the other hand, the swing is less by the overdrive of the tail current source. We should nonetheless note that, carrying a large current, *M*<sup>5</sup> and *M*<sup>6</sup> in Fig. 9.15 may require a high overdrive voltage if their capacitance contribution to nodes *X* and *Y* is to be minimized.

We now determine the small-signal voltage gain of the folded-cascode op amp of Fig. 9.15. Using the half circuit depicted in Fig. 9.16(a) and writing |*Av*| = *Gm Rout*, we must calculate *Gm* and *Rout*. As shown in Fig. 9.16(b), the output short-circuit current is approximately equal to the drain current of *M*<sup>1</sup> because the impedance seen looking into the source of *<sup>M</sup>*3, that is, *(gm*<sup>3</sup> <sup>+</sup> *gmb*3*)*−<sup>1</sup>%*rO*3, is typically much lower than *rO*1%*rO*5. Thus, *Gm* ≈ *gm*1. To calculate *Rout*, we use Fig. 9.16(c), with *RO P* ≈ *(gm*<sup>7</sup> + *gmb*7*)rO*7*rO*9, to write *Rout* ≈ *RO P* %[*(gm*<sup>3</sup> + *gmb*3*)rO*3*(rO*1%*rO*5*)*]. It follows that

$$|A\_v| \approx g\_{m1} \{ [(g\_{m3} + g\_{mb3})r\_{O3}(r\_{O1} \| r\_{O5})] \} \| [(g\_{m7} + g\_{mb7})r\_{O7}r\_{O9}] \} \tag{9.17}$$

Here is the image describtion:
```
The image depicts a complex MOSFET-based differential amplifier circuit. Here is a detailed description of the circuit components and their connections:

1. **Current Source (I_SS)**: At the left side of the circuit, there is a current source labeled \( I_{SS} \). This current source is connected to the sources of two NMOS transistors, \( M_1 \) and \( M_2 \).

2. **Differential Pair (M_1 and M_2)**: The transistors \( M_1 \) and \( M_2 \) form a differential pair. The gate of \( M_1 \) is connected to the input voltage \( V_{in} \), while the gate of \( M_2 \) is connected to a reference voltage (not explicitly shown in the image). The sources of \( M_1 \) and \( M_2 \) are connected together and to the current source \( I_{SS} \).

3. **Load Transistors (M_3 and M_4)**: The drains of \( M_1 \) and \( M_2 \) are connected to the sources of two PMOS transistors, \( M_3 \) and \( M_4 \), respectively. The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_{b1} \).

4. **Intermediate Nodes (X and Y)**: The drain of \( M_3 \) is connected to node \( X \), and the drain of \( M_4 \) is connected to node \( Y \).

5. **Current Mirrors (M_5 and M_6)**: The sources of two NMOS transistors, \( M_5 \) and \( M_6 \), are connected to ground. The gates of \( M_5 \) and \( M_6 \) are connected to a bias voltage \( V_{b4} \). The drain of \( M_5 \) is connected to node \( X \), and the drain of \( M_6 \) is connected to node \( Y \).

6. **Cascoding Transistors (M_7, M_8, M_9, and M_{10})**: The circuit includes four additional PMOS transistors for cascoding. The sources of \( M_7 \) and \( M_8 \) are connected to the drains of \( M_3 \) and \( M_4 \), respectively. The gates of \( M_7 \) and \( M_8 \) are connected to a bias voltage \( V_{b2} \). The drains of \( M_7 \) and \( M_8 \) are connected to the sources of \( M_9 \) and \( M_{10} \), respectively. The gates of \( M_9 \) and \( M_{10} \) are connected to a bias voltage \( V_{b3} \). The drains of \( M_9 \) and \( M_{10} \) are connected to the supply voltage \( V_{DD} \).

7. **Output Node (V_{out})**: The output voltage \( V_{out} \) is taken from the common node between the drains of \( M_7 \) and \( M_8 \).

8. **Power Supply (V_{DD})**: The top of the circuit is connected to the positive power supply voltage \( V_{DD} \).

In summary, this circuit is a differential amplifier with cascoding stages to improve performance parameters such as gain and output resistance. The differential pair \( M_1 \) and \( M_2 \) amplify the difference between the input signals, and the cascoding transistors \( M_7 \), \( M_8 \), \( M_9 \), and \( M_{10} \) enhance the overall performance of the amplifier.
```

**Figure 9.15** Folded-cascode op amp with cascode PMOS loads.

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each circuit features MOSFET transistors and resistors, and they appear to be variations of a common-source amplifier with different configurations.

### Circuit (a):
1. **Transistors:**
   - **M1:** An NMOS transistor with its gate connected to the input voltage \( V_{in} \).
   - **M3:** A PMOS transistor with its gate connected to a bias voltage \( V_{b1} \).
   - **M7:** A PMOS transistor with its gate connected to a bias voltage \( V_{b2} \).
   - **M9:** A PMOS transistor with its gate connected to a bias voltage \( V_{b3} \).

2. **Connections:**
   - The source of M1 is connected to ground.
   - The drain of M1 is connected to node X.
   - Node X is connected to the source of M3.
   - The drain of M3 is connected to the source of M7.
   - The drain of M7 is connected to the source of M9.
   - The drain of M9 is connected to \( V_{DD} \).
   - The output voltage \( V_{out} \) is taken from the drain of M7.
   - There is a resistor \( r_{o5} \parallel r_{o1} \) connected between node X and ground.

### Circuit (b):
1. **Transistors:**
   - **M1:** An NMOS transistor with its gate connected to the input voltage \( V_{in} \).
   - **M3:** A PMOS transistor with its gate connected to a bias voltage \( V_{b1} \).

2. **Connections:**
   - The source of M1 is connected to ground.
   - The drain of M1 is connected to node X.
   - Node X is connected to the source of M3.
   - The drain of M3 is connected to the output current \( I_{out} \).
   - There is a resistor \( r_{o5} \parallel r_{o1} \) connected between node X and ground.

### Circuit (c):
1. **Transistors:**
   - **M1:** An NMOS transistor with its gate connected to the input voltage \( V_{in} \).
   - **M3:** A PMOS transistor with its gate connected to a bias voltage \( V_{b1} \).

2. **Connections:**
   - The source of M1 is connected to ground.
   - The drain of M1 is connected to node X.
   - Node X is connected to the source of M3.
   - The drain of M3 is connected to a resistor \( R_{OP} \).
   - The other end of \( R_{OP} \) is connected to \( V_{DD} \).
   - The output resistance \( R_{out} \) is taken from the drain of M3.
   - There is a resistor \( r_{o5} \parallel r_{o1} \) connected between node X and ground.

### Summary:
- **Circuit (a)** is a multi-stage amplifier with three PMOS transistors stacked on top of each other, providing a high gain configuration.
- **Circuit (b)** is a simpler configuration with a single PMOS transistor acting as a current source.
- **Circuit (c)** is similar to (b) but includes an additional resistor \( R_{OP} \) for output resistance measurement.

Each circuit uses a combination of NMOS and PMOS transistors to achieve different amplification and output characteristics.
```

**Figure 9.16** (a) Half circuit of folded cascode op amp, (b) equivalent circuit for *Gm* calculation, and (c) equivalent circuit for *Rout* calculation.

The reader is encouraged to repeat this calculation without neglecting the current drawn by *rO*5||*rO*<sup>1</sup> in Fig. 9.16(b).

How does this value compare with the gain of a telescopic op amp? For comparable device dimensions and bias currents, the PMOS input differential pair exhibits a lower transconductance than does an NMOS pair. Furthermore, *rO*<sup>1</sup> and *rO*<sup>5</sup> appear in parallel, reducing the output impedance, especially because *M*<sup>5</sup> carries the currents of both the input device and the cascode branch. As a consequence, the gain in (9.17) is usually two to three times lower than that of a comparable telescopic cascode.

It is also worth noting that the pole at the "folding point," i.e., the sources of *M*<sup>3</sup> and *M*4, is quite closer to the origin than that associated with the source of cascode devices in a telescopic topology. In Fig. 9.17(a), *Ctot* arises from *CG S*3*,CSB*3*,CDB*1, and *CG D*1. By contrast, in Fig. 9.17(b), *Ctot* contains additional contributions due to *CG D*<sup>5</sup> and *CDB*5, typically significant components because *M*<sup>5</sup> must be wide enough to carry a large current with a small overdrive.

Here is the image describtion:
```
The image shows two different transistor circuits labeled as (a) and (b). Both circuits appear to be configurations involving MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) and are likely used in analog signal processing or amplification.

### Circuit (a):
1. **Transistors**: 
   - There are two MOSFETs labeled M1 and M3.
2. **Voltage Sources**:
   - \( V_{in} \): This is the input voltage applied to the gate of M1.
   - \( V_b \): This is a bias voltage applied to the gate of M3.
3. **Current Source**:
   - \( I_{SS} \): A current source connected to the source of M1 and ground.
4. **Capacitor**:
   - \( C_{tot} \): A capacitor connected between the drain of M3 and ground.
5. **Connections**:
   - The drain of M1 is connected to the source of M3.
   - The source of M1 is connected to the current source \( I_{SS} \) which is grounded.
   - The drain of M3 is connected to \( C_{tot} \) and also serves as the output node.

### Circuit (b):
1. **Transistors**:
   - There are three MOSFETs labeled M1, M3, and M5.
2. **Voltage Sources**:
   - \( V_{in} \): This is the input voltage applied to the gate of M1.
   - \( V_{b1} \): This is a bias voltage applied to the gate of M3.
   - \( V_{b4} \): This is a bias voltage applied to the gate of M5.
3. **Current Source**:
   - \( I_{SS} \): A current source connected to the drain of M1.
4. **Capacitor**:
   - \( C_{tot} \): A capacitor connected between the drain of M3 and ground.
5. **Connections**:
   - The drain of M1 is connected to the current source \( I_{SS} \).
   - The source of M1 is connected to the drain of M5.
   - The source of M5 is grounded.
   - The drain of M3 is connected to \( C_{tot} \) and also serves as the output node.
   - The source of M3 is connected to the drain of M1.

### General Observations:
- Both circuits use MOSFETs in configurations that suggest they are amplifiers or active loads.
- The capacitors \( C_{tot} \) in both circuits are likely used for filtering or stabilization purposes.
- The bias voltages \( V_b \), \( V_{b1} \), and \( V_{b4} \) are used to set the operating points of the transistors.
- The current sources \( I_{SS} \) provide a constant current, which is crucial for the operation of these circuits.

These circuits are typical in analog design, particularly in applications like amplifiers, oscillators, or other signal processing components.
```

**Figure 9.17** Effect of device capacitance on the nondominant pole in telescopic and folded-cascode op amps.

A folded-cascode op amp may incorporate NMOS input devices and PMOS cascode transistors. Illustrated in Fig. 9.18, such a circuit potentially provides a higher gain than the op amp of Fig. 9.15 because of the greater mobility of NMOS devices, but at the cost of lowering the pole at the folding points. To understand why, note that the pole at node *X* is given by the product of 1*/(gm*<sup>3</sup> + *gmb*3*)* and the total capacitance at this node (if the output pole is dominant). The magnitude of both of these components is relatively high: *M*<sup>3</sup> suffers from a low transconductance, and *M*<sup>5</sup> contributes substantial capacitance because it must be wide enough to carry the drain currents of both *M*<sup>1</sup> and *M*3. In fact, for comparable bias currents, *M*5–*M*<sup>6</sup> in Fig. 9.18 may be several times wider than *M*5–*M*<sup>6</sup> in Fig. 9.15. For applications sensitive to flicker noise, the PMOS-input op amp is preferable (Sec. 9.12).

Here is the image describtion:
```
The image depicts a complex CMOS (Complementary Metal-Oxide-Semiconductor) analog circuit, likely an operational amplifier or a similar analog signal processing circuit. Here is a detailed description of the circuit:

1. **Transistors and Connections:**
   - The circuit consists of multiple MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) labeled M1 through M11 and Mb1 through Mb3.
   - The transistors are arranged in a differential amplifier configuration with current mirrors and active loads.

2. **Input Stage:**
   - The input stage is formed by transistors M1 and M2, which are configured as a differential pair. The input signal \( V_{in} \) is applied to the gate of M1.
   - The source of M1 and M2 are connected together and to the drain of M11, which acts as a current source.

3. **Current Sources:**
   - Transistor Mb1, connected to the current source \( I_{REF1} \), provides a bias current for the differential pair M1 and M2.
   - Transistors Mb2 and Mb3 are connected to current sources \( I_{REF2} \) and \( I_{REF3} \) respectively, providing bias currents for other parts of the circuit.

4. **Active Loads and Current Mirrors:**
   - Transistors M3 and M4 form an active load for the differential pair M1 and M2. The output of the differential pair is taken from the drain of M2 and M4, labeled as \( V_{out} \).
   - Transistors M5 and M6 form a current mirror, with the gate of M5 connected to the gate and drain of M6. This current mirror is connected to the node X.
   - Transistors M7 and M8 form another current mirror, with the gate of M7 connected to the gate and drain of M8. This current mirror is connected to the node Y.

5. **Biasing:**
   - The circuit includes bias voltages \( V_{b1} \) and \( V_{b2} \) applied to the gates of M3, M4, M7, and M8 to set the operating points of these transistors.
   - The biasing ensures that the transistors operate in the correct region (typically the saturation region for analog circuits) to achieve the desired amplification and signal processing.

6. **Power Supply:**
   - The circuit is powered by a supply voltage \( V_{DD} \) connected to the drains of M5, M6, and Mb2.

7. **Output:**
   - The output voltage \( V_{out} \) is taken from the drain of M4, which is the output of the differential amplifier stage.

8. **Ground Connections:**
   - The sources of M9 and M10 are connected to ground, providing a reference point for the circuit.

Overall, this circuit appears to be a differential amplifier with current mirrors and active loads, commonly used in analog signal processing applications such as operational amplifiers, comparators, and other analog integrated circuits.
```

**Figure 9.18** Realization of a folded-cascode op amp.

### **9.2.5 Folded-Cascode Properties**

Our study thus far suggests that the overall voltage swing of a folded-cascode op amp is only slightly higher than that of a telescopic configuration. This advantage comes at the cost of higher power dissipation, lower voltage gain, lower pole frequencies, and, as explained in Sec. 9.12, higher noise. Nonetheless, folded-cascode op amps are used more widely for two reasons: (1) their input and output CM levels can be chosen equal without limiting the output swings, and (2) compared to telescopic cascodes, they can accommodate a wider input CM range. Let us elaborate on these properties.

Consider the closed-loop amplifier of Fig. 9.19(a), assuming a folded-cascode op amp. We can draw the circuit as shown in Fig. 9.19(b) or Fig. 9.19(c), noting that the input and output CM levels are equal. With a high open-loop gain, the gate voltages of *M*<sup>1</sup> and *M*<sup>2</sup> swing negligibly while *VX* and *VY* can reach within two overdrives of ground or *VDD*. This should be compared with the swings in Fig. 9.10.

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c).

(a) The first diagram is a simplified representation of an operational amplifier (op-amp) with feedback resistors. It shows an op-amp with two input terminals (one inverting and one non-inverting) and one output terminal. The inverting input is connected to a resistor R1, which is then connected to an input signal. The non-inverting input is connected to a resistor R2, which is also connected to another input signal. The output of the op-amp is connected back to the inverting input through a resistor R3, and there is another resistor R4 connected from the inverting input to ground.

(b) The second diagram is a more complex circuit involving multiple MOSFETs (M1 to M10) and resistors (R1 to R4). The circuit appears to be a differential amplifier with additional stages for current mirroring and amplification. The left side of the circuit shows two MOSFETs (M1 and M2) with their sources connected to a current source. The gates of M1 and M2 are connected to resistors R3 and R4, respectively, which are then connected to the input signals. The drains of M1 and M2 are connected to the sources of M3 and M4, respectively. M3 and M4 are connected in a current mirror configuration with M9 and M10, which are connected to the power supply V_DD. The circuit also includes additional MOSFETs (M5 to M8) connected in a configuration that likely provides further amplification or current mirroring.

(c) The third diagram is a simplified version of the second diagram, focusing on the differential amplifier stage. It shows two MOSFETs (M1 and M2) with their sources connected to a current source. The gates of M1 and M2 are connected to resistors R3 and R4, respectively, which are then connected to the input signals. The drains of M1 and M2 are connected to the sources of M3 and M4, respectively. M3 and M4 are connected in a current mirror configuration, similar to the previous diagram, but without the additional MOSFETs and complexity.

Overall, the image illustrates different stages and configurations of amplifiers, from a basic op-amp with feedback to more complex MOSFET-based differential amplifiers.
```

**Figure 9.19** (a) Feedback amplifier, (b) implementation using a folded-cascode op amp, and (c) alternative drawing to find allowable swings.

In feedback topologies where the input and output CM levels need not be equal, the folded cascode allows a wider input CM range than does the telescopic cascode. In Fig. 9.18, for example, *Vin,C M* must exceed *VG S*<sup>1</sup>*,*<sup>2</sup> +*(VG S*<sup>11</sup> − *VT H*11*)*, but it can be as high as *Vb*<sup>2</sup> + |*VG S*3| + *VT H*<sup>1</sup>*,*<sup>2</sup> before *M*<sup>1</sup> and *M*<sup>2</sup> enter the triode region. Note that this upper bound can be *greater* than *VDD* (why?). Similarly, a PMOS-input configuration can handle input CM levels as low as zero.

### **9.2.6 Design Procedure**

We now deal with the design of folded-cascode op amps to reinforce the foregoing concepts.

#### ▲**Example 9.9**

Design a folded-cascode op amp with an NMOS input pair (Fig. 9.18) to satisfy the following specifications: *VDD* = 3 V, differential output swing = 3 V, power dissipation = 10 mW, and voltage gain = 2000. Use the same device parameters as in Example 9.5.

### **Solution**

As with the telescopic cascode of the previous example, we begin with the power and swing specifications. Allocating 1.5 mA to the input pair, 1.5 mA to the two cascode branches, and the remaining 330 *µ*A to the three current mirrors, we first consider the devices in each cascode branch. Since *M*<sup>5</sup> and *M*<sup>6</sup> must each carry 1.5 mA, we allow an overdrive of 500 mV for these transistors so as to keep their width to a reasonable value. To *M*3–*M*4, we allocate 400 mV and to *M*7–*M*10, 300 mV. Thus, *(W/L)*5*,*<sup>6</sup> = 400*, (W/L)*3*,*<sup>4</sup> = 313, and *(W/L)*7−<sup>10</sup> = 278*.* Since the minimum and maximum output levels are equal to 0.6 V and 2.1 V, respectively, the optimum output common-mode level is 1.35 V.

The minimum dimensions of *M*1–*M*<sup>2</sup> are dictated by the minimum input common-mode level, *VG S*<sup>1</sup> + *VO D*11. For example, if the input and the output CM levels are equal (Fig. 9.20), then *VG S*<sup>2</sup> + *VO D*<sup>11</sup> = 1*.*35 V. With

Here is the image describtion:
```
The image depicts a schematic diagram of a MOSFET-based electronic circuit. Here is a detailed description of the components and their connections:

1. **Transistors**: The circuit consists of several MOSFET transistors labeled as M1, M2, M4, M6, M8, M10, and M11.
   - **M1**: The gate of M1 is connected to the input voltage \( V_{in} \). The source of M1 is connected to the drain of M11, and the drain of M1 is connected to the drain of M2.
   - **M2**: The source of M2 is connected to the ground through M11, and its drain is connected to the drain of M1.
   - **M4**: The drain of M4 is connected to the node Y, and its source is connected to the drain of M8.
   - **M6**: The drain of M6 is connected to the supply voltage \( V_{DD} \), and its source is connected to the node Y.
   - **M8**: The drain of M8 is connected to the source of M4, and its source is connected to the drain of M10.
   - **M10**: The drain of M10 is connected to the source of M8, and its source is connected to the ground.
   - **M11**: The drain of M11 is connected to the source of M1 and M2, and its source is connected to the ground.

2. **Connections**:
   - The gate of M2 is connected to the drain of M1.
   - The gate of M4 is connected to the node Y.
   - The gate of M6 is connected to the node Y.
   - The gate of M8 is connected to the node Y.
   - The gate of M10 is connected to the node Y.
   - The gate of M11 is connected to the source of M1 and M2.

3. **Power Supply**: The circuit is powered by a supply voltage \( V_{DD} \) connected to the drain of M6.

4. **Ground**: The sources of M10 and M11 are connected to the ground.

5. **Node Y**: This is a critical node in the circuit where the sources of M6 and M4, and the gates of M4, M6, M8, and M10 are connected.

This circuit appears to be a complex analog circuit, possibly a part of a larger system such as an amplifier or a current mirror, given the arrangement of the MOSFETs and the connections. The exact function would depend on the specific design and the values of the components used.
```

**Figure 9.20** Folded-cascode op amp with input and output shorted.

*VO D*<sup>11</sup> = 0*.*4 V as an initial guess, we have *VG S*<sup>1</sup> = 0*.*95 V, obtaining *VO D*<sup>1</sup>*,*<sup>2</sup> = 0*.*95 − 0*.*7 = 0*.*25 V, and hence *(W/L)*1*,*<sup>2</sup> = 400*.* The maximum dimensions of *M*<sup>1</sup> and *M*<sup>2</sup> are determined by the tolerable input capacitance and the capacitance at nodes *X* and *Y* in Fig. 9.18.

We now calculate the small-signal gain. Using *gm* = 2*ID/(VG S* − *VT H )*, we have *gm*<sup>1</sup>*,*<sup>2</sup> = 0*.*006 A/V*, gm*<sup>3</sup>*,*<sup>4</sup> = 0*.*0038 A/V, and *gm*<sup>7</sup>*,*<sup>8</sup> = 0*.*05 A/V. For *L* = 0*.*5 *µ*m, *rO*<sup>1</sup>*,*<sup>2</sup> = *rO*<sup>7</sup>−<sup>10</sup> = 13*.*3 k%, and *rO*<sup>3</sup>*,*<sup>4</sup> = 2*rO*<sup>5</sup>*,*<sup>6</sup> = 6*.*67 k%. It follows that the impedance seen looking into the drain of *M*<sup>7</sup> (or *M*8) is equal to 8.8 M% whereas, owing to the limited intrinsic gain of *M*<sup>3</sup> (or *M*4), that seen looking into the drain of *M*<sup>3</sup> is equal to 66.5 k%. The overall gain is therefore limited to about 400.

In order to increase the gain, we first observe that *rO*<sup>5</sup>*,*<sup>6</sup> is quite lower than *rO*<sup>1</sup>*,*2. Thus, the length of *M*5– *M*<sup>6</sup> must be increased. Also, the transconductance of *M*1–*M*<sup>2</sup> is relatively low and can be increased by widening these transistors. Finally, we may decide to double the intrinsic gain of *M*<sup>3</sup> and *M*<sup>4</sup> by doubling both their length and their width, but at the cost of increasing the capacitance at nodes *X* and *Y* . We leave the exact choice of the device dimensions as an exercise for the reader. Note that the op amp must incorporate common-mode feedback (Sec. 9.7). ▲

Telescopic and folded-cascode op amps can also be designed to provide a single-ended output. Shown in Fig. 9.21(a) is an example, where a PMOS cascode current mirror converts the differential currents of *M*<sup>3</sup>

Here is the image describtion:
```
The image shows two different configurations of a CMOS (Complementary Metal-Oxide-Semiconductor) operational amplifier circuit. Both circuits are differential amplifiers with active loads and cascode stages. Let's describe each circuit in detail:

### Circuit (a):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the input differential pair. The gate of M1 is connected to the input voltage \( V_{in} \), and the gate of M2 is connected to a reference voltage.
   - **M3 and M4:** These are NMOS transistors acting as cascode transistors for M1 and M2, respectively. Their gates are connected to a bias voltage \( V_b \).
   - **M5 and M6:** These are PMOS transistors acting as the active load for the differential pair. They are connected in a current mirror configuration.
   - **M7 and M8:** These are PMOS transistors forming the cascode stage for M5 and M6, respectively. They are connected to the supply voltage \( V_{DD} \).

2. **Connections:**
   - The source of M1 and M2 are connected together and to a current source \( I_{SS} \) which is connected to the ground.
   - The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
   - The drain of M3 is connected to the source of M5, and the drain of M4 is connected to the source of M6.
   - The drain of M5 is connected to the source of M7, and the drain of M6 is connected to the source of M8.
   - The gates of M5 and M6 are connected together to the node X.
   - The output voltage \( V_{out} \) is taken from the drain of M6.

### Circuit (b):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the input differential pair, similar to circuit (a).
   - **M3 and M4:** These are NMOS transistors acting as cascode transistors for M1 and M2, respectively. Their gates are connected to a bias voltage \( V_{b1} \).
   - **M5 and M6:** These are PMOS transistors acting as the active load for the differential pair, similar to circuit (a).
   - **M7 and M8:** These are PMOS transistors forming the cascode stage for M5 and M6, respectively, similar to circuit (a).

2. **Connections:**
   - The source of M1 and M2 are connected together and to a current source \( I_{SS} \) which is connected to the ground.
   - The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
   - The drain of M3 is connected to the source of M5, and the drain of M4 is connected to the source of M6.
   - The drain of M5 is connected to the source of M7, and the drain of M6 is connected to the source of M8.
   - The gates of M5 and M6 are connected together to the node X.
   - The output voltage \( V_{out} \) is taken from the drain of M6.
   - The gates of M5 and M6 are connected to a bias voltage \( V_{b2} \).

### Differences:
- In circuit (a), the gates of M5 and M6 are connected to a single bias voltage \( V_b \).
- In circuit (b), the gates of M5 and M6 are connected to a different bias voltage \( V_{b2} \), while the gates of M3 and M4 are connected to \( V_{b1} \).

These circuits are used in analog design to achieve high gain and high output impedance, which are desirable characteristics for operational amplifiers.
```

**Figure 9.21** Cascode op amps with single-ended output.

and *M*<sup>4</sup> to a single-ended output voltage. In this implementation, however, *VX* = *VDD* −|*VG S*5|−|*VG S*7|, limiting the maximum value of *Vout* to *VDD* − |*VG S*5| − |*VG S*7|+|*VT H*6| and "wasting" one PMOS threshold voltage in the swing (Chapter 5). To resolve this issue, the PMOS load can be modified to a low-voltage cascode (Chapter 5), as shown in Fig. 9.21(b), so that *M*<sup>7</sup> and *M*<sup>8</sup> are biased at the edge of the triode region. Similar ideas apply to folded-cascode op amps as well.

The circuit of Fig. 9.21(a) suffers from two disadvantages with respect to its differential counterpart in Fig. 9.8(b). First, it provides only half the output voltage swing. Second, it contains a mirror pole at node *X* (Chapter 5), thus limiting the speed of feedback systems employing such an amplifier. It is therefore preferable to use the differential topology, although it requires a feedback loop to define the output common-mode level (Sec. 9.7).

# **9.3 Two-Stage Op Amps**

The op amps studied thus far exhibit a "one-stage" nature in that they allow the small-signal current produced by the input pair to flow directly through the output impedance, i.e., they perform voltage-tocurrent conversion only once. The gain of these topologies is therefore limited to the product of the input pair transconductance and the output impedance. We have also observed that cascoding in such circuits increases the gain while limiting the output swings.

In some applications, the gain and/or the output swings provided by cascode op amps are not adequate. For example, a modern op amp must operate with supply voltages as low as 0.9 V while delivering singleended output swings as large as 0.8 V. In such cases, we resort to "two-stage" op amps, with the first stage providing a high gain and the second, large swings (Fig. 9.22). In contrast to cascode op amps, a two-stage configuration isolates the gain and swing requirements.

Here is the image describtion:
```
The image is a block diagram of a two-stage operational amplifier (op-amp). It consists of two main stages:

1. **Stage 1**: This is labeled as "High Gain." It has an input labeled \( V_{in} \) and two outputs that feed into the next stage. The purpose of this stage is to provide a high gain to the input signal.

2. **Stage 2**: This is labeled as "High Swing." It receives the outputs from Stage 1 and produces the final output labeled \( V_{out} \). The purpose of this stage is to provide a high output voltage swing.

The diagram is simple and uses rectangular blocks to represent each stage. The connections between the stages are shown with arrows indicating the direction of signal flow from Stage 1 to Stage 2. The input and output terminals are depicted as small circles on the left and right sides of the diagram, respectively.

The figure is labeled as "Figure 9.22" and is titled "Two-stage op amp."
```

Each stage in Fig. 9.22 can incorporate various amplifier topologies studied in previous sections, but the second stage is typically configured as a simple common-source stage so as to allow maximum output swings. Figure 9.23 shows an example, where the first and second stages exhibit gains equal to *gm*<sup>1</sup>*,*<sup>2</sup>*(rO*<sup>1</sup>*,*<sup>2</sup>%*rO*<sup>3</sup>*,*<sup>4</sup>*)* and *gm*<sup>5</sup>*,*<sup>6</sup>*(rO*<sup>5</sup>*,*<sup>6</sup>%*rO*<sup>7</sup>*,*<sup>8</sup>*)*, respectively. The overall gain is therefore comparable to that

Here is the image describtion:
```
The image depicts a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Power Supply and Ground:**
   - The circuit is powered by a voltage source \( V_{DD} \) at the top.
   - The bottom of the circuit is connected to the ground.

2. **Transistors:**
   - The circuit consists of eight MOSFETs labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the active load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the current mirror transistors.
   - \( M_7 \) and \( M_8 \) are the tail current source transistors.

3. **Connections:**
   - The gates of \( M_1 \) and \( M_2 \) are the differential input terminals. \( M_1 \) gate is connected to \( V_{in} \), and \( M_2 \) gate is connected to a reference voltage.
   - The sources of \( M_1 \) and \( M_2 \) are connected together and to a current source \( I_{SS} \) which is connected to the ground.
   - The drains of \( M_1 \) and \( M_2 \) are connected to the drains of \( M_3 \) and \( M_4 \) respectively, forming nodes \( X \) and \( Y \).
   - The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_{b1} \).
   - The sources of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The drains of \( M_5 \) and \( M_6 \) are connected to nodes \( X \) and \( Y \) respectively.
   - The gates of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_3 \) and \( M_4 \) respectively.
   - The sources of \( M_5 \) and \( M_6 \) are connected to the output nodes \( V_{out1} \) and \( V_{out2} \) respectively.
   - The gates of \( M_7 \) and \( M_8 \) are connected to a bias voltage \( V_{b2} \).
   - The sources of \( M_7 \) and \( M_8 \) are connected to the ground.

4. **Outputs:**
   - The output voltages are taken from the drains of \( M_5 \) and \( M_6 \), labeled as \( V_{out1} \) and \( V_{out2} \) respectively.

This differential amplifier circuit is designed to amplify the difference between the input signals applied to \( M_1 \) and \( M_2 \). The current mirror formed by \( M_5 \) and \( M_6 \) helps in maintaining a constant current through the differential pair, while \( M_3 \) and \( M_4 \) act as active loads to improve the gain of the amplifier.
```

**Figure 9.23** Simple implementation of a two-stage op amp.

of a cascode op amp, but the swing at *Vout*<sup>1</sup> and *Vout*<sup>2</sup> is equal to *VDD* − |*VO D*<sup>5</sup>*,*<sup>6</sup>| − *VO D*<sup>7</sup>*,*8, the highest possible value.<sup>4</sup>

To obtain a higher gain, the first stage can incorporate cascode devices, as depicted in Fig. 9.24. With a gain of, say, 10 in the output stage, the voltage swings at *X* and *Y* are quite small, allowing optimization of *M*1–*M*<sup>8</sup> for higher gain. The overall voltage gain can be expressed as

$$A\_v \approx \{ g\_{m1,2} \| (g\_{m3,4} + g\_{mb3,4}) r\_{O3,4} r\_{O1,2} \} \| \| (g\_{m5,6} + g\_{mb5,6}) r\_{O5,6} r\_{O7,8} \| \} \tag{9.18}$$
 
$$\times \left[ g\_{m9,10} (r\_{O9,10} \| r\_{O11,12}) \right] \tag{9.18}$$

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with active loads and current mirrors. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The source terminals of M1 and M2 are connected together and to a current source ISS, which is connected to ground.
   - **M3 and M4:** These are NMOS transistors acting as current mirrors. The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4. The gates of M3 and M4 are connected together and to the drain of M3.
   - **M5 and M6:** These are PMOS transistors forming the active load for the differential pair. The source terminals of M5 and M6 are connected to VDD. The drain of M5 is connected to the drain of M3 (node X), and the drain of M6 is connected to the drain of M4 (node Y). The gates of M5 and M6 are connected together and to a bias voltage Vb2.
   - **M7 and M8:** These are PMOS transistors forming a current mirror. The source terminals of M7 and M8 are connected to VDD. The drain of M7 is connected to the drain of M5, and the drain of M8 is connected to the drain of M6. The gates of M7 and M8 are connected together and to the drain of M7.
   - **M9 and M10:** These are NMOS transistors acting as output buffers. The drain of M9 is connected to the drain of M7, and the drain of M10 is connected to the drain of M8. The gates of M9 and M10 are connected together and to a bias voltage Vb3.
   - **M11 and M12:** These are NMOS transistors connected as current sources. The source terminals of M11 and M12 are connected to ground. The drain of M11 is connected to the source of M9, and the drain of M12 is connected to the source of M10. The gates of M11 and M12 are connected together and to a bias voltage Vb4.

2. **Nodes and Connections:**
   - **Node X:** The connection point between the drain of M3 and the drain of M5.
   - **Node Y:** The connection point between the drain of M4 and the drain of M6.
   - **Vout1:** The output voltage taken from the drain of M9.
   - **Vout2:** The output voltage taken from the drain of M10.
   - **Vin:** The input voltage applied to the gate of M1.
   - **Vb1, Vb2, Vb3, Vb4:** Bias voltages applied to the gates of M3/M4, M5/M6, M7/M8, and M11/M12 respectively.
   - **ISS:** The current source connected to the common source node of M1 and M2, providing a constant current.

3. **Power Supply:**
   - **VDD:** The positive power supply voltage connected to the source terminals of the PMOS transistors (M5, M6, M7, M8).
   - **Ground:** The reference voltage connected to the source terminals of the NMOS transistors (M1, M2, M11, M12) and the current source ISS.

This circuit is a typical example of a differential amplifier with active loads and current mirrors, commonly used in analog integrated circuits for amplification and signal processing.
```

**Figure 9.24** Two-stage op amp employing cascoding.

A two-stage op amp can provide a single-ended output. One method is to convert the differential currents of the two output stages to a single-ended voltage. Illustrated in Fig. 9.25, this approach maintains the differential nature of the first stage, using only the current mirror *M*7–*M*<sup>8</sup> to generate a single-ended output.

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage operational amplifier (op-amp) with a single-ended output. The circuit consists of several MOSFET transistors and a current source. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential input pair. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a reference voltage (often ground or another input).
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair. The source of M3 is connected to \( V_{DD} \), and its drain is connected to the drain of M1. Similarly, the source of M4 is connected to \( V_{DD} \), and its drain is connected to the drain of M2.
   - **M5 and M6:** These are PMOS transistors forming a current mirror. The source of M5 is connected to \( V_{DD} \), and its gate is connected to the gate and drain of M6. The drain of M5 is connected to the drain of M3, and the drain of M6 is connected to the drain of M4.
   - **M7 and M8:** These are NMOS transistors forming another current mirror. The source of M7 is connected to ground, and its gate is connected to the gate and drain of M8. The drain of M7 is connected to the source of M1 and M2, and the drain of M8 is connected to the output node \( V_{out} \).

2. **Current Source:**
   - **I_{SS}:** This is a current source connected between the common source node of M1 and M2 and ground. It sets the tail current for the differential pair.

3. **Bias Voltage:**
   - **V_b:** This is a bias voltage applied to the gate of M3 and M4 to set their operating point.

4. **Power Supply:**
   - **V_{DD}:** This is the positive power supply voltage connected to the sources of the PMOS transistors (M3, M4, M5, and M6).

5. **Output:**
   - **V_{out}:** This is the single-ended output voltage taken from the drain of M6.

The circuit operates as follows:
- The differential input voltage \( V_{in} \) is applied to the gate of M1, while the gate of M2 is connected to a reference voltage.
- The differential pair (M1 and M2) converts the input voltage difference into a current difference.
- The current mirror formed by M5 and M6 ensures that the current through M3 and M4 is mirrored accurately.
- The second stage, consisting of M7 and M8, amplifies the signal further and provides the single-ended output \( V_{out} \).

This two-stage op-amp configuration is commonly used in analog circuit design for its high gain and good performance characteristics.
```

single-ended output.

<sup>4</sup>One can replace *M*<sup>7</sup> and *M*<sup>8</sup> with resistors to allow greater swings, but the gain would be limited.

Can we cascade more than two stages to achieve a higher gain? As explained in Chapter 10, each gain stage introduces at least one pole in the open-loop transfer function, making it difficult to guarantee stability in a feedback system using such an op amp. For this reason, op amps having more than two stages are rarely used. Exceptions are described in [1, 2, 3].

### **9.3.1 Design Procedure**

The design of two-stage op amps is somewhat more complex. We present a simple example here and more detailed designs in Chapter 11.

#### ▲**Example 9.10**

Design the two-stage op amp of Fig. 9.23 for *VDD* = 1 V, *P* = 1 mW, a differential output swing of 1 V*pp*, and a gain of 100. Use the same device parameters as in Example 9.7, but assume that *VTHN* = 0*.*3 V and *VTHP* = −0*.*35 V.

### **Solution**

We allocate a bias current of 960 *µ*A to *M*1–*M*8, leaving 40 *µ*A for the bias branches that generate *Vb*<sup>1</sup> and *Vb*2. Let us split the current budget equally between the first and second stages, i.e., assume that *ID*<sup>1</sup> =···= *I*<sup>8</sup> = 120 *µ*A.

Since the second stage is likely to provide a voltage gain of 5 to 10, the output swing of the *first* stage need not be large. Specifically, if the second stage is designed for a gain of 5 and a single-ended output swing of 0.5 V*pp*, the first stage need only sustain 0.1 V*pp* at *X* (or *Y* ). The choice of overdrive voltages for *M*1–*M*<sup>4</sup> and *ISS* is therefore quite relaxed, i.e., |*VO D*<sup>3</sup>|+|*VO D*<sup>1</sup>| + *VISS* = 1 V − 0*.*1 V = 0*.*9 V. But we must consider two points: (1) recall from Chapter 7 that the noise contributed by current sources *M*<sup>3</sup> and *M*<sup>4</sup> is minimized by maximizing their overdrive voltage, and (2) the gain (and noise) requirements dictate a high *gm* for *M*<sup>1</sup> and *M*<sup>2</sup> and, inevitably, a low overdrive voltage. In fact, the latter point typically translates to subthreshold operation for the input devices, yielding a maximum *gm* of *ID/(*ξ*VT )* <sup>≈</sup> *(*<sup>325</sup> %*)*−<sup>1</sup> with <sup>ξ</sup> <sup>=</sup> <sup>1</sup>*.*5. But, we ignore subthreshold operation in this example.

How large can the overdrive of *M*<sup>3</sup> and *M*<sup>4</sup> be? Since *VDS*<sup>3</sup>*,*<sup>4</sup> = *VG S*<sup>5</sup>*,*<sup>6</sup> in this case, the upper bound may be imposed by *M*<sup>5</sup> and *M*<sup>6</sup> rather than by the first stage. For example, if the design of the second stage eventually yields |*VG S*<sup>5</sup>*,*6| = 400 mV, and if *VX* (or *VY* ) can rise by 50 mV (for a 100-mV*pp* swing), then *M*<sup>3</sup> and *M*<sup>4</sup> experience a minimum |*VDS*| of 350 mV. We must therefore revisit this allocation after the second stage is designed.

For a single-ended output swing of 0.5 V*pp*, we can choose 200 mV and 300 mV for the overdrives of the output NMOS and PMOS devices, respectively. With *ID* = 120 *µ*A, we then compute the *W/L* values of these transistors. However, this allocation faces two issues: (1) the large overdrive of *M*<sup>5</sup> and *M*<sup>6</sup> may translate to an inadequately low *gm* = 2*ID/(VG S* − *VT H )*, and (2) the small overdrive of *M*<sup>7</sup> and *M*<sup>8</sup> gives them a high noise current. For these reasons, we swap the overdrive allocation, giving 300 mV to *M*<sup>7</sup> and *M*<sup>8</sup> and 200 mV to *M*<sup>5</sup> and *M*6. The penalty is the larger *W/L* of the latter pair and hence a greater capacitance at *X* and *Y* .

We begin the calculations from the output stage. With |*ID*| = 120 *µ*A and the above overdrives, we have *gm*<sup>5</sup>*,*<sup>6</sup> <sup>=</sup> <sup>2</sup>|*ID/(VG S* <sup>−</sup> *VT H )*| = *(*<sup>833</sup> %*)*−1*,rO*<sup>5</sup>*,*<sup>6</sup> <sup>=</sup> <sup>1</sup>*/(*λ|*ID*|*)* <sup>=</sup> 42 k%, and *rO*<sup>7</sup>*,*<sup>8</sup> <sup>=</sup> 83 k% (for the minimum channel length of 0.5 *µ*m). The second stage thus provides a gain of about 33, allowing even smaller voltage swings for the first stage. The corresponding device dimensions are *(W/L)*5*,*<sup>6</sup> = 200 and *(W/L)*7*,*<sup>8</sup> = 44.

Returning to the first stage in Fig. 9.23, we note that *VDS*<sup>3</sup>*,*<sup>4</sup> = |*VG S*<sup>5</sup>*,*6| = 550 mV. Transistors *M*<sup>3</sup> and *M*<sup>4</sup> can therefore operate with an overdrive as high as 500 mV (if we still assume *VX* or *VY* can rise by 50 mV from the bias value) but require a |*VG S*| of 500 mV + |*VTHP* | = 850 mV, and hence *Vb*<sup>1</sup> = 150 mV. Such a low *Vb*<sup>1</sup> may cause difficulty in the design of the current mirror driving *M*<sup>3</sup> and *M*4. Instead, we choose |*VG S*<sup>3</sup>*,*<sup>4</sup> − *VTHP* | = 400 mV, obtaining *(W/L)*3*,*<sup>4</sup> = 50*, gm*<sup>3</sup>*,*<sup>4</sup> = 1*/(*1*.*7 k%*),* and *rO*<sup>3</sup>*,*<sup>4</sup> = 83 k% (for *L* = 0*.*5 *µ*m).

The input transistors, *M*<sup>1</sup> and *M*2, exhibit an output resistance of 83 k% (with *L* = 0*.*5 *µ*m) and can have an overdrive as large as 0.5 V. However, with such an overdrive, *gm*<sup>1</sup>*,*2*/gm*<sup>3</sup>*,*<sup>4</sup> = |*VG S*<sup>3</sup>*,*<sup>4</sup> − *VTHP* |*/(VG S*<sup>1</sup>*,*<sup>2</sup> − *VTHN )* = 4*/*5, implying that the PMOS devices contribute substantial noise. For this reason, we choose an overdrive of 100 mV for *M*<sup>1</sup> and *M*2, arriving at *gm*<sup>1</sup>*,*<sup>2</sup> = 1*/(*420 %*), (W/L)*1*,*<sup>2</sup> = 400*,* and a voltage gain of *gm*<sup>1</sup>*,*2*(rO*<sup>1</sup>||*rO*3*)* = 66 for the first stage.

This design provides an overall gain of more than 2,000, primarily because of the low bias current and the use of an older technology. As explained in Chapter 11, nanometer two-stage op amps suffer from much lower gains.

▲

# **9.4 Gain Boosting**

### **9.4.1 Basic Idea**

Razavi-3930640 book December 17, 201516:59 364

The limited gain of the one-stage op amps studied in Sec. 9.2 and the difficulties in using two-stage op amps at high speeds have motivated extensive work on new topologies. Recall that in one-stage op amps, such as telescopic and folded-cascode topologies, the objective is to maximize the output impedance so as to attain a high voltage gain. The idea behind gain boosting is to further increase the output impedance without adding more cascode devices [4, 5]. We neglect body effect for simplicity, but it can be readily included at the end.

**First Perspective** Suppose a transistor is preceded by an ideal voltage amplifier as shown in Fig. 9.26(a).

Here is the image describtion:
```
The image consists of two parts, labeled (a) and (b), which depict different stages of an electronic circuit involving an operational amplifier and a MOSFET transistor.

### Part (a):
1. **Circuit Components**:
   - **Operational Amplifier (A1)**: This is represented by a triangle with a positive (+) and negative (-) input terminal.
   - **MOSFET Transistor (M2)**: This is connected to the output of the operational amplifier. The MOSFET has three terminals: the gate (connected to the output of A1), the source (connected to ground), and the drain (where the output current \( I_{out} \) is measured).

2. **Connections**:
   - The input voltage \( V_{in} \) is applied to the positive terminal of the operational amplifier A1.
   - The negative terminal of A1 is connected to ground.
   - The output of A1 is connected to the gate of the MOSFET M2.
   - The source of M2 is connected to ground.
   - The drain of M2 is where the output current \( I_{out} \) is measured.

### Part (b):
1. **Circuit Representation**:
   - The left side of part (b) shows the same circuit as in part (a) but enclosed in a dashed box, indicating that it is being considered as a single entity or block.
   - The right side of part (b) shows the equivalent small-signal model of the circuit.

2. **Small-Signal Model**:
   - **Voltage Source \( V_1 \)**: This represents the small-signal input voltage.
   - **Current Source \( A_1 g_m V_1 \)**: This represents the transconductance of the operational amplifier and MOSFET combination, where \( A_1 \) is the gain of the operational amplifier, \( g_m \) is the transconductance of the MOSFET, and \( V_1 \) is the small-signal input voltage.
   - **Resistor \( r_o \)**: This represents the output resistance of the MOSFET.
   - The current source and resistor are connected in parallel, and the output current \( I_{out} \) is measured at the same point as in the original circuit.

### Summary:
The image illustrates the transformation of a circuit involving an operational amplifier and a MOSFET into its small-signal equivalent model. The original circuit (a) is simplified into a block representation and then further into a small-signal model (b) to analyze the behavior of the circuit in response to small input signals.
```

**Figure 9.26** (a) Transistor preceded by a voltage amplifier, and (b) equivalent circuit.

We note that the overall circuit exhibits a transconductance of *A*1*gm* and a voltage gain of−*A*1*gmrO* (why?). We thus surmise that this arrangement can be viewed as a three-terminal device (a "supertransistor") having a transconductance of *A*1*gm* and an output resistance of *rO* [Fig. 9.26(b)]. We neglect body effect in this section.

Let us now incorporate this new device in a familiar topology and examine the circuit's behavior. We begin with the degenerated stage depicted in Fig. 9.27(a) and wish to compute its transconductance (with the output shorted to ac ground). Since *RS* carries *Iout*, the small-signal gate voltage is given by *(Vin* − *RS Iout)A*1, yielding a gate-source voltage of *(Vin* − *RS Iout)A*<sup>1</sup> − *RS Iout* and hence *Iout* = *gm*[*(Vin* − *RS Iout)A*<sup>1</sup> − *RS Iout*]. It follows that

$$\frac{I\_{\rm out}}{V\_{in}} = \frac{A\_1 \mathbf{g}\_m}{1 + (A\_1 + 1)\mathbf{g}\_m R\_S} \tag{9.19}$$

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), both featuring an operational amplifier (op-amp) and a MOSFET transistor. Here is a detailed description of each diagram:

### Diagram (a):
1. **Operational Amplifier (A1)**: The op-amp has its non-inverting input (+) connected to an input voltage source labeled \( V_{in} \). The inverting input (-) is connected to the source of the MOSFET transistor \( M_2 \).
2. **MOSFET Transistor (M2)**: The gate of the MOSFET is connected to the output of the op-amp \( A1 \). The source of the MOSFET is connected to a resistor \( R_S \) which is grounded. The drain of the MOSFET is connected to the output current \( I_{out} \) which is directed upwards towards a positive supply voltage.
3. **Resistor (R_S)**: This resistor is connected between the source of the MOSFET and ground.

### Diagram (b):
1. **Operational Amplifier (A1)**: Similar to diagram (a), the op-amp has its non-inverting input (+) connected to ground. The inverting input (-) is connected to the source of the MOSFET transistor \( M_2 \).
2. **MOSFET Transistor (M2)**: The gate of the MOSFET is connected to the output of the op-amp \( A1 \). The source of the MOSFET is connected to a resistor \( R_S \) which is grounded. The drain of the MOSFET is connected to a resistor \( r_o \) and a current source \( I_0 \) which is directed downwards.
3. **Resistor (R_S)**: This resistor is connected between the source of the MOSFET and ground.
4. **Resistor (r_o)**: This resistor is connected between the drain of the MOSFET and a node where the current \( I_x \) flows towards a voltage source \( V_x \).
5. **Voltage Source (V_x)**: This voltage source is connected to the node where the current \( I_x \) flows, with its positive terminal connected to the node and its negative terminal grounded.

### Summary:
- Both diagrams feature an op-amp \( A1 \) and a MOSFET \( M_2 \) with a source resistor \( R_S \).
- Diagram (a) shows a basic configuration with an input voltage \( V_{in} \) and an output current \( I_{out} \).
- Diagram (b) adds complexity with an additional resistor \( r_o \), a current source \( I_0 \), and a voltage source \( V_x \), illustrating a more detailed circuit analysis scenario.
```

**Figure 9.27** Arrangements for calculation of (a) transconductance, and (b) output resistance.

Without *A*1, the transconductance would be equal to *gm/(*1+*gm RS)*. Interestingly, the equivalent transconductance has risen by a factor of *A*<sup>1</sup> in the numerator and *A*<sup>1</sup> + 1 in the denominator, revealing that the model shown in Fig. 9.26(b) is not quite correct. However, since in practice *A*<sup>1</sup> " 1, the error introduced by this model is acceptably low.

How about the output resistance of the degenerated stage? From the setup in Fig. 9.27(b), we can express the voltage drop across *RS* as *IX RS* and the gate voltage of *M*<sup>2</sup> as −*A*<sup>1</sup> *IX RS*. That is, *I*<sup>0</sup> = *(*−*A*1*RS IX* − *RS IX )gm*. Also, *rO* carries a current equal to *(VX* − *RS IX )/rO* . We now have

$$I\_X = (-A\_1 R\_S - R\_S) g\_m I\_X + \frac{V\_X - R\_S I\_X}{r\_O} \tag{9.20}$$

and

$$R\_{out} = r\_O + (A\_1 + 1)\mathbf{g}\_m r\_O R\_S + R\_S \tag{9.21}$$

Without *A*1, the output resistance would be equal to *rO* + *gmrO RS* + *RS*.

Equation (9.21) is a remarkable result, suggesting that the output resistance of the circuit is "boosted," as if the transconductance of *M*<sup>2</sup> were raised by a factor of *A*<sup>1</sup> +1. This increase in *Rout* is afforded while the degenerated stage retains its voltage headroom. We can see that the allowable voltage swing at the drain of *M*<sup>2</sup> is approximately the same for this structure and a simple degenerated transistor.

#### ▲**Example 9.11**

Determine the resistance seen at the source of *M*<sup>2</sup> in Fig. 9.28(a) if γ = 0.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled as (a) and (b), both featuring an operational amplifier (op-amp) and a MOSFET transistor. Here is a detailed description of each circuit:

### Circuit (a):
1. **Operational Amplifier (A1)**: The op-amp has its non-inverting input (+) connected to an input voltage source labeled \( V_{in} \). The inverting input (-) is connected to the source of the MOSFET transistor \( M_2 \).
2. **MOSFET Transistor (M2)**: The gate of \( M_2 \) is connected to the output of the op-amp \( A1 \). The drain of \( M_2 \) is connected to a resistor \( R_D \), which is in turn connected to a positive supply voltage \( V_{DD} \). The source of \( M_2 \) is connected to a resistor \( R_X \), which is grounded.
3. **Resistors**: \( R_D \) is connected between the drain of \( M_2 \) and \( V_{DD} \). \( R_X \) is connected between the source of \( M_2 \) and ground.

### Circuit (b):
1. **Operational Amplifier (A1)**: Similar to circuit (a), the op-amp has its non-inverting input (+) grounded and its inverting input (-) connected to the source of the MOSFET transistor \( M_2 \).
2. **MOSFET Transistor (M2)**: The gate of \( M_2 \) is connected to the output of the op-amp \( A1 \). The drain of \( M_2 \) is connected to a resistor \( R_D \), which is in turn connected to a current source \( I_X \). The source of \( M_2 \) is connected to a resistor \( r_O \), which is connected to a voltage source \( V_X \).
3. **Resistors and Current Source**: \( R_D \) is connected between the drain of \( M_2 \) and the current source \( I_X \). \( r_O \) is connected between the source of \( M_2 \) and the voltage source \( V_X \). The current source \( I_X \) is connected to the positive supply voltage.

### Additional Details:
- Both circuits feature a feedback loop where the op-amp controls the gate of the MOSFET to regulate the voltage at the source of the MOSFET.
- In circuit (a), the input voltage \( V_{in} \) is applied directly to the non-inverting input of the op-amp.
- In circuit (b), the non-inverting input of the op-amp is grounded, and the circuit includes an additional current source \( I_X \) and a voltage source \( V_X \).

These circuits are likely used for different applications involving voltage regulation and current control using the combination of an op-amp and a MOSFET.
```

Here is the image describtion:
```
The image is a text label that reads "Figure 9.28." It appears to be a reference to a specific figure within a document, book, or article, likely used to identify and refer to a particular illustration, chart, graph, or diagram that is labeled as Figure 9.28. The text is in a bold font, indicating its importance as a figure reference.
```

### **Solution**

In the setup shown in Fig. 9.28(b), the small-signal gate voltage is equal to−*A*1*VX* , and hence *I*<sup>0</sup> = *(*−*A*1*VX*−*VX )gm*. Also, *RD* carries a current of *IX* , generating a voltage equal to *IX RD* at the drain with respect to ground. Since the current flowing downward through *rO* is given by *(IX RD* − *VX )/rO* , we have at the source node

$$\frac{I\_X R\_D - V\_X}{r\_O} + (-A\_1 V\_X - V\_X) g\_m + I\_X = 0\tag{9.22}$$

and

$$R\_X = \frac{R\_D + r\_O}{1 + (A\_1 + 1)g\_m r\_O} \tag{9.23}$$

Without *A*1, this resistance would be equal to *(RD* + *rO )/(*1 + *gmrO )*. This example too suggests that the transconductance of *M*<sup>2</sup> is raised by a factor of *A*<sup>1</sup> + 1. ▲

In summary, the addition of the auxiliary amplifier in Fig. 9.26(b) raises the equivalent *gm* of *M*<sup>2</sup> by a factor of *A*<sup>1</sup> + 1, thereby boosting the output impedance of the stage. We surmise from *A<sup>v</sup>* = −*Gm Rout* that the voltage gain can also be boosted, but where should the input be applied? As in a simple cascode stage, let us replace the degeneration resistor with a voltage-to-current converter (Fig. 9.29), obtaining an output impedance equal to *rO*<sup>2</sup> + *(A*<sup>1</sup> + 1*)gm*2*rO*2*rO*<sup>1</sup> + *rO*1. The short-circuit transconductance is nearly equal to *gm*<sup>1</sup> because the resistance seen looking into the source of *M*<sup>2</sup> is obtained from (9.23) with *RD* = 0 and is given by *rO*2*/*[1 + *(A*<sup>1</sup> + 1*)gm*2*rO*2] ≈ [*(A*<sup>1</sup> + 1*)gm*2] <sup>−</sup>1, a value much less than *rO*1. It follows that

$$|A\_v| \approx g\_{m1} [r\_{O2} + (A\_1 + 1)g\_{m2}r\_{O2}r\_{O1} + r\_{O1}] \tag{9.24}$$

$$\approx g\_{m1} g\_{m2} r\_{O1} r\_{O2} (A\_1 + 1) \tag{9.25}$$

As explained later in this section, this "gain-boosting" technique can be applied to cascode differential pairs and op amps as well.

Here is the image describtion:
```
The image depicts a circuit diagram featuring a "Super Transistor" configuration. Here's a detailed description of the components and their connections:

1. **Super Transistor Block**: The circuit is enclosed in a dashed box labeled "Super Transistor." This block includes an operational amplifier (A1) and two MOSFET transistors (M1 and M2).

2. **Operational Amplifier (A1)**: 
   - The operational amplifier has two inputs: a non-inverting input (+) and an inverting input (-).
   - The non-inverting input is connected to a voltage source labeled \( V_b \).
   - The inverting input is connected to a node labeled \( P \), which is also the connection point between the source of M2 and the drain of M1.

3. **MOSFET Transistors**:
   - **M1**: This is an NMOS transistor with its source connected to ground and its gate connected to the input voltage \( V_{in} \).
   - **M2**: This is a PMOS transistor with its source connected to the positive supply voltage \( V_{DD} \) and its gate connected to the output of the operational amplifier A1. The drain of M2 is connected to the node \( P \).

4. **Current Source**: There is a current source connected between \( V_{DD} \) and the output node \( V_{out} \).

5. **Connections**:
   - The node \( P \) is the common point where the drain of M1 and the source of M2 meet.
   - The output voltage \( V_{out} \) is taken from the same node where the current source connects to \( V_{DD} \).

In summary, the circuit uses an operational amplifier to control the gate of a PMOS transistor (M2) based on the voltage \( V_b \). The NMOS transistor (M1) is controlled by the input voltage \( V_{in} \). The current source provides a constant current, and the output voltage \( V_{out} \) is taken from the top of the current source. The configuration aims to create a precise control mechanism for the output voltage using the operational amplifier and the transistors.
```

**Figure 9.29** Basic gain-boosted stage.

**Second Perspective** Consider the degenerated stage shown in Fig. 9.30(a). We wish to increase the output resistance without stacking more cascode devices. Recall from Chapter 3 that if the drain voltage changes by '*V*, then the source voltage changes by '*VS* = *RS/*[*rO* + *(*1 + *gmrO )RS*] (with γ = 0), producing a change in the voltage across *RS* and hence in the drain current. We can loosely view the effect as voltage division between *RS* and *gmrO RS*.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), each with their corresponding small-signal equivalent circuits.

### Circuit (a):
1. **Left Side (Original Circuit):**
   - The circuit features a MOSFET labeled \( M_2 \) with its gate connected to a bias voltage \( V_b \).
   - The source of \( M_2 \) is connected to a resistor \( R_S \) which is grounded.
   - The drain of \( M_2 \) is connected to a current source \( I_0 \) and a resistor \( r_O \) which is also grounded.
   - A small signal voltage \( \Delta V_S \) is applied to the source of \( M_2 \).
   - The node at the source of \( M_2 \) is labeled as point \( P \).
   - The current \( I_X \) flows from the drain of \( M_2 \) through \( r_O \) to ground.
   - The voltage at the drain of \( M_2 \) is labeled \( V_X \).

2. **Right Side (Small-Signal Equivalent Circuit):**
   - The small-signal equivalent circuit shows a voltage source \( \Delta V \) in series with a resistor \( R_S \).
   - The voltage across \( R_S \) is \( V_X \).
   - The current through the circuit is \( g_m r_O R_S \), where \( g_m \) is the transconductance of the MOSFET.

### Circuit (b):
1. **Left Side (Original Circuit with Amplifier):**
   - This circuit is similar to (a) but includes an operational amplifier \( A_1 \).
   - The non-inverting input of \( A_1 \) is connected to the bias voltage \( V_b \).
   - The inverting input of \( A_1 \) is connected to the source of \( M_2 \) at point \( P \).
   - The output of \( A_1 \) is connected to the gate of \( M_2 \).
   - The source of \( M_2 \) is connected to a resistor \( R_S \) which is grounded.
   - The drain of \( M_2 \) is connected to a current source \( I_0 \) and a resistor \( r_O \) which is also grounded.
   - A small signal voltage \( \Delta V_S \) is applied to the source of \( M_2 \).
   - The current \( I_X \) flows from the drain of \( M_2 \) through \( r_O \) to ground.
   - The voltage at the drain of \( M_2 \) is labeled \( V_X \).

2. **Right Side (Small-Signal Equivalent Circuit):**
   - The small-signal equivalent circuit shows a voltage source \( \Delta V \) in series with a resistor \( R_S \).
   - The voltage across \( R_S \) is \( V_X \).
   - The current through the circuit is \( A_1 g_m r_O R_S \), where \( A_1 \) is the gain of the operational amplifier and \( g_m \) is the transconductance of the MOSFET.

### Summary:
- Both circuits depict a MOSFET with a source resistor and a drain resistor, with the second circuit incorporating an operational amplifier to enhance the gain.
- The small-signal equivalent circuits simplify the analysis by showing the effective resistance and voltage relationships.
- The key difference between the two circuits is the presence of the operational amplifier in (b), which increases the overall gain by a factor of \( A_1 \).
```

**Figure 9.30** Response of (a) degenerated CS stage and (b) gain-boosted stage to a change in output voltage.

We now make an important observation. The change in the drain current in response to '*V* can be suppressed if two conditions hold: (a) the voltage across *RS* remains constant, and (b) the current flowing through *RS* remains equal to the drain current.<sup>5</sup> How should we keep *VP* constant? We can compare *VP* to

<sup>5</sup>A constant voltage source tied from *P* to ground allows the former condition but not the latter.

### Sec. 9.4 Gain Boosting **367**

Razavi-3930640 book December 17, 201516:59 367

a "reference" voltage by means of an op amp and return the resulting error to a point in the circuit so as to ensure that *VP* "tracks" the reference. Illustrated in Fig. 9.30(b), the idea is to apply the error, *A*1*(Vb*−*VP )*, to the gate of *M*2, forcing *VP* to be equal to *Vb* if the loop gain is large. The above two conditions are thus satisfied. For example, if the drain voltage rises, *VP* also tends to rise, but, as a result, the gate voltage falls, reducing the current drawn by *M*2. As derived below, this effect can be approximately viewed as voltage division between *RS* and *A*1*gmrO RS*. For *A*<sup>1</sup> → +, *VP* is "pinned" to *Vb* and the drain current is exactly equal to *Vb/RS* regardless of the drain voltage. This topology is also called a "regulated cascode" as amplifier *A*<sup>1</sup> monitors and regulates the output current.

#### ▲**Example 9.12**

Figure 9.31 shows the regulated cascode subjected to an output impedance test. Determine the small-signal values of *VP* , *VG*, *I*0, and *Ir o*. Assume that *(A*<sup>1</sup> + 1*)gmrO RS* is large.

Here is the image describtion:
```
The image depicts an electronic circuit involving an operational amplifier (op-amp), a MOSFET transistor, and several other components. Here is a detailed description of the circuit:

1. **Operational Amplifier (A1)**: 
   - The op-amp is labeled as A1.
   - It has two input terminals: the inverting input (-) and the non-inverting input (+).
   - The non-inverting input is connected to a reference voltage (not shown in the image).
   - The output of the op-amp is connected to the gate (G) of the MOSFET transistor M2.

2. **MOSFET Transistor (M2)**:
   - The MOSFET is labeled as M2.
   - The gate (G) of M2 is connected to the output of the op-amp A1.
   - The source (S) of M2 is connected to a point labeled P.
   - The drain (D) of M2 is connected to a resistor labeled rO.

3. **Resistor (rO)**:
   - The resistor rO is connected between the drain of M2 and a node where the current IX flows towards a voltage source VX.
   - The other end of rO is connected to the node where the current I0 flows from the drain of M2.

4. **Voltage Source (VX)**:
   - The voltage source VX is connected to the node where the current IX flows.
   - The positive terminal of VX is connected to the node, and the negative terminal is grounded.

5. **Resistor (RS)**:
   - The resistor RS is connected between the point P and ground.
   - The current Iro flows through RS from point P to ground.

6. **Currents**:
   - I0 is the current flowing from the drain of M2 through rO.
   - IX is the current flowing towards the voltage source VX.
   - Iro is the current flowing through the resistor rO.

The circuit appears to be a feedback configuration where the op-amp controls the gate voltage VG of the MOSFET M2 to regulate the current through the resistor rO and the voltage VX. The resistor RS provides a feedback path to the op-amp, helping to stabilize the circuit operation.
```

### **Solution**

We know from our analysis of Fig. 9.27(b) that

$$V\_X = \left[r\_O + (A\_1 + \text{l})g\_m r\_O R\_S + R\_S\right] I\_X \tag{9.26}$$

and hence

$$V\_P = I\_X R\_S \tag{9.27}$$

$$\eta = \frac{R\_S}{r\_O + (A\_1 + 1)g\_m r\_O R\_S + R\_S} V\_X \tag{9.28}$$

If *(A*<sup>1</sup> + 1*)gmrO RS* is large, then *VP* ≈ *VX /*[*(A*<sup>1</sup> + 1*)gmrO* ], implying that the amplifier suppresses the change in the voltage across *RS* by another factor of *A*<sup>1</sup> + 1 compared to the case of a simple degenerated transistor. We also have

$$V\_G = -A\_1 V\_P \tag{9.29}$$

$$\eta = \frac{-A\_1 R\_S}{r o + (A\_1 + 1) g\_m r o R\_S + R\_S} V\_X \tag{9.30}$$

The small-signal gate-source voltage is equal to *VG* − *VP* ≈ −*VX /(gmrO )*, yielding *I*<sup>0</sup> ≈ −*VX /rO* . Moreover,

$$I\_{ro} = \frac{V\_X - V\_P}{r\_O} \tag{9.31}$$

$$\eta = \frac{r\_O + (A\_1 + \text{l}) g\_m r\_O R\_S}{r\_O + (A\_1 + \text{l}) g\_m r\_O R\_S + R\_S} \frac{V\_X}{r\_O} \tag{9.32}$$

$$
\gamma \approx \frac{V\_X}{r o} \tag{9.33}
$$

Interestingly, *I*<sup>0</sup> and *Ir o* are nearly equal and opposite. That is, the amplifier adjusts the gate voltage such that the change in the intrinsic drain current, *I*0, almost cancels the current drawn by *rO* . We say that the small-signal current of *M*<sup>2</sup> circulates through *rO* .

In summary, the above two perspectives portray two principles behind the gain-boosting technique: the amplifier boosts the *gm* of the cascode device, or the amplifier regulates the output current by monitoring and pinning the source voltage.

### **9.4.2 Circuit Implementation**

Razavi-3930640 book December 17, 201516:59 368

In this section, we deal with the implementation of the auxiliary amplifier in the regulated cascode and extend the gain-boosting technique to op amps. The simplest realization of *A*<sup>1</sup> is a common-source stage, as shown in Fig. 9.32(a). If *I*<sup>1</sup> is ideal, then |*A*1| = *gm*3*rO*3, yielding |*Vout/Vin*| ≈ *gm*1*rO*1*gm*2*rO*2*(gm*3*rO*3+1*)*, as in a *triple* cascode. However, this topology limits the output voltage swing because the minimum voltage at node *P* is dictated by *VG S*<sup>3</sup> rather than the overdrive of *M*1. We note that *Vout* must remain above *VG S*<sup>3</sup> + *(VG S*<sup>2</sup> − *VT H*2*)* here.

Here is the image describtion:
```
The image contains three different circuit diagrams labeled (a), (b), and (c). Each circuit diagram features a combination of MOSFET transistors, current sources, and voltage sources. Let's describe each circuit in detail:

### Circuit (a):
- **Transistors**: There are three MOSFET transistors labeled M1, M2, and M3.
  - M1: The gate is connected to the input voltage \( V_{in} \), the source is grounded, and the drain is connected to node P.
  - M2: The gate is connected to node G, the source is connected to node P, and the drain is connected to the output voltage \( V_{out} \) and a current source \( I_2 \) which is connected to \( V_{DD} \).
  - M3: The gate is connected to node G, the source is grounded, and the drain is connected to a current source \( I_1 \) which is connected to \( V_{DD} \).
- **Current Sources**: There are two current sources:
  - \( I_1 \) is connected between \( V_{DD} \) and the drain of M3.
  - \( I_2 \) is connected between \( V_{DD} \) and the drain of M2.
- **Voltage Source**: \( V_{DD} \) is the supply voltage.
- **Nodes**: 
  - Node G connects the gate of M2 and the drain of M3.
  - Node P connects the source of M2 and the drain of M1.

### Circuit (b):
- **Transistors**: There are three MOSFET transistors labeled M1, M2, and M3.
  - M1: The gate is connected to the input voltage \( V_{in} \), the source is grounded, and the drain is connected to node P.
  - M2: The gate is connected to node G, the source is connected to node P, and the drain is connected to the output voltage \( V_{out} \) and a current source \( I_2 \) which is connected to \( V_{DD} \).
  - M3: The gate is connected to node G, the source is grounded, and the drain is connected to a current source \( I_1 \) which is connected to \( V_{DD} \).
- **Current Sources**: There are two current sources:
  - \( I_1 \) is connected between \( V_{DD} \) and the drain of M3.
  - \( I_2 \) is connected between \( V_{DD} \) and the drain of M2.
- **Voltage Source**: \( V_{DD} \) is the supply voltage.
- **Nodes**: 
  - Node G connects the gate of M2 and the drain of M3.
  - Node P connects the source of M2 and the drain of M1.

### Circuit (c):
- **Transistors**: There are four MOSFET transistors labeled M1, M2, M3, and M4.
  - M1: The gate is connected to the input voltage \( V_{in} \), the source is grounded, and the drain is connected to node P.
  - M2: The gate is connected to node G, the source is connected to node P, and the drain is connected to the output voltage \( V_{out} \) and a current source \( I_2 \) which is connected to \( V_{DD} \).
  - M3: The gate is connected to node G, the source is connected to the drain of M4, and the drain is connected to a current source \( I_1 \) which is connected to \( V_{DD} \).
  - M4: The gate is connected to a bias voltage \( V_b \), the source is grounded, and the drain is connected to the source of M3.
- **Current Sources**: There are three current sources:
  - \( I_1 \) is connected between \( V_{DD} \) and the drain of M3.
  - \( I_2 \) is connected between \( V_{DD} \) and the drain of M2.
  - \( I_3 \) is connected between \( V_{DD} \) and the node G.
- **Voltage Sources**: 
  - \( V_{DD} \) is the supply voltage.
  - \( V_b \) is a bias voltage.
- **Nodes**: 
  - Node G connects the gate of M2, the drain of M3, and the current source \( I_3 \).
  - Node P connects the source of M2 and the drain of M1.

Each circuit diagram is enclosed in a dashed box labeled \( A_1 \), indicating a specific part of the circuit.
```

**Figure 9.32** Gain-boosted amplifier using (a) an NMOS CS stage, (b) a PMOS CS stage, and (c) a folded-cascode stage.

To avoid this headroom limitation, we consider a PMOS common-source stage for *A*<sup>1</sup> [Fig. 9.32(b)]. The operation and gain-boosting properties remain the same, but *VP* can now be as low as the overdrive of *M*1. Unfortunately, *M*<sup>3</sup> may enter the triode region here because the gate voltage of *M*<sup>2</sup> tends to be too high for the drain of *M*3. Specifically, if we target *VP* = *VG S*<sup>1</sup> − *VT H*1, then *VG* = *VG S*<sup>2</sup> + *VG S*<sup>1</sup> − *VT H*1,

▲

revealing that the drain of *M*<sup>3</sup> is higher than its gate by *VG S*2. If *VG S*<sup>2</sup> *>* |*VT H*3|, *M*<sup>3</sup> resides in the triode region.

The above analysis implies that we must insert one more stage in the feedback loop so as to reach compatible bias levels between consecutive stages. Let us interpose an NMOS common-gate stage between *M*<sup>3</sup> and the gate of *M*<sup>2</sup> [Fig. 9.32(c)]. The reader recognizes the resulting *A*<sup>1</sup> topology as a folded cascode, but we also observe that *M*<sup>4</sup> provides an upward level shift from its source to its drain, allowing *VG* to be higher than the drain voltage of *M*3.

#### ▲**Example 9.13**

Determine the allowable range for *Vb* in Fig. 9.32(c).

### **Solution**

The minimum value of *Vb* places *I*<sup>1</sup> at the edge of the triode region, i.e., *Vb,min* = *VG S*<sup>4</sup> + *VI* 1. The maximum value biases *M*<sup>4</sup> at the edge of the triode region, i.e., *Vb,max* = *VG S*<sup>2</sup> + *VP* + *VT H*4. Thus, *Vb* has a comfortably wide range and need not be precise. ▲

We now apply gain boosting to a differential cascode stage, as shown in Fig. 9.33(a). Since the signals at nodes *X* and *Y* are differential, we surmise that the two single-ended gain-boosting amplifiers *A*<sup>1</sup> and *A*<sup>2</sup> can be replaced by one differential amplifier [Fig. 9.33(b)]. Following the topology of Fig. 9.32(a), we implement the differential auxiliary amplifier as shown in Fig. 9.33(c), but noting that the minimum level at the drain of *M*<sup>3</sup> is equal to *VO D*<sup>3</sup> + *VG S*<sup>5</sup> + *VISS*2, where *VISS*<sup>2</sup> denotes the voltage required across *ISS*2. In a simple differential cascode, on the other hand, the minimum would be approximately one threshold voltage lower.

Here is the image describtion:
```
The image shows three different configurations of differential amplifier circuits using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Each configuration is labeled (a), (b), and (c).

### Configuration (a):
- **Transistors**: There are four MOSFETs labeled M1, M2, M3, and M4.
- **Amplifiers**: Two amplifiers labeled A1 and A2 are connected to the gates of M3 and M4, respectively.
- **Current Source**: A current source labeled Iss is connected to the common source node of M1 and M2.
- **Connections**:
  - The input voltage \( V_{in} \) is applied to the gates of M1 and M2.
  - The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
  - The drains of M3 and M4 are connected to the outputs of amplifiers A1 and A2, respectively.
  - The sources of M1 and M2 are connected to the current source Iss, which is grounded.

### Configuration (b):
- **Transistors**: There are four MOSFETs labeled M1, M2, M3, and M4.
- **Amplifier**: A single amplifier is connected between the gates of M3 and M4.
- **Current Source**: A current source labeled Iss is connected to the common source node of M1 and M2.
- **Connections**:
  - The input voltage \( V_{in} \) is applied to the gates of M1 and M2.
  - The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
  - The drains of M3 and M4 are connected to the output nodes X and Y, respectively.
  - The sources of M1 and M2 are connected to the current source Iss, which is grounded.

### Configuration (c):
- **Transistors**: There are six MOSFETs labeled M1, M2, M3, M4, M5, and M6.
- **Current Sources**: Three current sources labeled I1, I2, and Iss1, and Iss2.
- **Connections**:
  - The input voltage \( V_{in} \) is applied to the gates of M1 and M2.
  - The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
  - The drains of M3 and M4 are connected to the output nodes X and Y, respectively.
  - The sources of M1 and M2 are connected to the current source Iss1, which is grounded.
  - The sources of M3 and M4 are connected to the drains of M5 and M6, respectively.
  - The sources of M5 and M6 are connected to the current sources I1 and I2, respectively.
  - The gates of M5 and M6 are connected to the common source node of M1 and M2, which is also connected to the current source Iss2.

In summary, these configurations represent different ways to design differential amplifiers using MOSFETs, with variations in the use of amplifiers, current sources, and transistor connections.
```

**Figure 9.33** Boosting the output impedance of a differential cascode stage.

The voltage swing limitation in Fig. 9.33(c) results from the fact that the gain-boosting amplifier incorporates an NMOS differential pair. If nodes *X* and *Y* are sensed by a PMOS pair, the minimum value of *VX* and *VY* is not dictated by the gain-boosting amplifier. Now recall from Sec. 9.2 that the minimum input CM level of a folded-cascode stage using a PMOS input pair can be zero. Thus, we employ such a topology for the gain-boosting amplifier, arriving at the circuit shown in Fig. 9.34. Here, the minimum allowable level of *VX* and *VY* is given by *VO D*<sup>1</sup>*,*<sup>2</sup> + *VISS*1.

▲

Here is the image describtion:
```
The image depicts a complex MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) circuit, likely a differential amplifier with active loads and current mirrors. Here is a detailed description of the circuit:

1. **Transistors and Current Sources:**
   - The circuit consists of eight MOSFETs labeled M1 through M8.
   - There are three current sources labeled I1, I2, and Iss1, and one labeled Iss2.

2. **Differential Pair:**
   - Transistors M1 and M2 form the differential pair. Their sources are connected together and to the current source Iss1, which is connected to ground.
   - The gates of M1 and M2 are the differential input terminals.

3. **Active Loads:**
   - Transistors M3 and M4 act as active loads for the differential pair. Their drains are connected to the drains of M1 and M2, respectively.
   - The sources of M3 and M4 are connected to the current source Iss2, which is connected to a positive supply voltage.

4. **Current Mirrors:**
   - Transistors M5, M6, M7, and M8 form current mirrors.
   - M5 and M6 are connected to the drains of M1 and M2, respectively, and their sources are connected to ground.
   - The gates of M5 and M6 are connected to the gates of M7 and M8, respectively, which are also connected to a bias voltage Vb.
   - The sources of M7 and M8 are connected to ground, and their drains are connected to current sources I1 and I2, respectively.

5. **Nodes:**
   - Node X is the connection point between the drain of M1 and the drain of M5.
   - Node Y is the connection point between the drain of M2 and the drain of M6.

6. **Biasing:**
   - The gates of M7 and M8 are connected to a common bias voltage Vb, which sets the operating point for the current mirrors.

7. **Operation:**
   - The differential input signal is applied to the gates of M1 and M2.
   - The differential output can be taken from nodes X and Y.
   - The current mirrors (M5, M6, M7, M8) ensure that the currents through M1 and M2 are mirrored and controlled, providing high gain and improved performance.

This circuit is typically used in analog signal processing applications, such as amplifiers, where precise control of current and high gain are required.
```

**Figure 9.34** Folded-cascode circuit used as auxiliary amplifier.

#### ▲**Example 9.14**

Razavi-3930640 book December 17, 201516:59 370

Calculate the output impedance of the circuit shown in Fig. 9.34.

### **Solution**

Using the half-circuit concept and replacing the ideal current sources with transistors, we obtain the equivalent depicted in Fig. 9.35. The voltage gain from *X* to *P* is approximately equal to *gm*5*Rout*1, where *Rout*<sup>1</sup> ≈ [*gm*7*rO*<sup>7</sup> *(rO*<sup>9</sup>%*rO*5*)*]%*(gm*11*rO*11*rO*13*)*. Thus, *Rout* ≈ *gm*3*rO*3*rO*1*gm*5*Rout*1. In essence, since the output impedance of a cascode is boosted by a folded-cascode stage, the overall output impedance is similar to that of a "quadruple" cascode.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a type of amplifier circuit. The circuit includes several MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) components and is divided into two main sections: the auxiliary amplifier and the main amplifier.

### Auxiliary Amplifier Section:
- **Transistors:**
  - **M13:** Connected to a bias voltage \( V_{b4} \) at its gate.
  - **M11:** Connected to a bias voltage \( V_{b3} \) at its gate and the drain of M13.
  - **M7:** Connected to a bias voltage \( V_{b2} \) at its gate.
  - **M5:** Connected to the source of M7 and the drain of M9.
  - **M9:** Connected to a bias voltage \( V_{b1} \) at its gate.

### Main Amplifier Section:
- **Transistors:**
  - **M1:** The gate is connected to the input signal \( V_{in} \), the source is grounded, and the drain is connected to node X.
  - **M3:** The gate is connected to node X, the source is connected to node P, and the drain is connected to \( R_{out} \).

### Nodes and Connections:
- **Node X:** The drain of M1 and the source of M5 are connected here.
- **Node P:** The source of M3 is connected here.
- **\( R_{out} \):** Connected to the drain of M3.

### Bias Voltages:
- **\( V_{b1} \):** Bias voltage for the gate of M9.
- **\( V_{b2} \):** Bias voltage for the gate of M7.
- **\( V_{b3} \):** Bias voltage for the gate of M11.
- **\( V_{b4} \):** Bias voltage for the gate of M13.

### Functionality:
- The auxiliary amplifier section is likely used to provide additional gain or to set the operating point of the main amplifier.
- The main amplifier section amplifies the input signal \( V_{in} \) and provides an output at \( R_{out} \).

The diagram is labeled as "Figure 9.35" and includes a dashed box around the auxiliary amplifier section to distinguish it from the main amplifier section.
```

Regulated cascodes can also be utilized in the load current sources of a cascode op amp. Shown in Fig. 9.36(a), such a topology boosts the output impedance of the PMOS current sources as well, thereby achieving a very high voltage gain. To allow maximum swings at the output, amplifier *A*<sup>2</sup> must employ an NMOS-input folded-cascode differential pair. Similar ideas apply to folded-cascode op amps [Fig. 9.36(b)].

Here is the image describtion:
```
The image consists of two circuit diagrams labeled as (a) and (b), both illustrating gain-boosting techniques applied to signal path and load devices in a differential amplifier configuration. Below the diagrams, the caption reads "Figure 9.36 Gain boosting applied to both signal path and load devices."

### Diagram (a):
1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors with their sources connected to a current source labeled \( I_{SS} \) and their gates connected to the input signal \( V_{in} \).
   - **M3 and M4:** These are the cascode transistors connected to the drains of M1 and M2, respectively.
   - **M5 and M6:** These are the load transistors connected to the drains of M3 and M4, respectively.
   - **M7 and M8:** These are additional transistors connected to the drains of M5 and M6, respectively, with their gates connected to a bias voltage \( V_b \).

2. **Amplifiers:**
   - **A1:** This amplifier is connected between the drain of M1 and the gate of M3.
   - **A2:** This amplifier is connected between the drain of M2 and the gate of M4.

3. **Power Supply:**
   - The positive power supply is labeled \( V_{DD} \).

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the common node between M5 and M6.

### Diagram (b):
1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors with their sources connected to a current source labeled \( I_{SS} \) and their gates connected to the input signal \( V_{in} \).
   - **M3 and M4:** These are the cascode transistors connected to the drains of M1 and M2, respectively.
   - **M5 and M6:** These are the load transistors connected to the drains of M3 and M4, respectively.
   - **M7 and M8:** These are additional transistors connected to the drains of M5 and M6, respectively, with their gates connected to a bias voltage \( V_{b1} \).
   - **M9 and M10:** These are additional transistors connected to the sources of M1 and M2, respectively, with their gates connected to a bias voltage \( V_{b2} \).

2. **Amplifiers:**
   - **A1:** This amplifier is connected between the drain of M1 and the gate of M3.
   - **A2:** This amplifier is connected between the drain of M2 and the gate of M4.

3. **Power Supply:**
   - The positive power supply is labeled \( V_{DD} \).

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the common node between M5 and M6.

### Summary:
Both diagrams illustrate differential amplifier circuits with gain-boosting techniques. Diagram (a) shows gain boosting applied to the signal path, while diagram (b) shows gain boosting applied to both the signal path and load devices. The use of additional amplifiers (A1 and A2) and transistors (M7, M8, M9, and M10) helps to enhance the overall gain of the circuits.
```

### **9.4.3 Frequency Response**

Recall that the premise behind gain boosting is to increase the gain without adding a second stage or more cascode devices. Does this mean that the op amps of Fig. 9.36 have a one-stage nature? After all, the gain-boosting amplifier introduces its own pole(s). In contrast to two-stage op amps, where the entire signal experiences the poles associated with each stage, in a gain-boosted op amp, most of the signal flows directly through the cascode devices to the output. Only a small "error" component is processed by the auxiliary amplifier and "slowed down."

In order to analyze the frequency response of the regulated cascode, we simplify the circuit to that shown in Fig. 9.37, where the auxiliary amplifier contains one pole at ω0, *A*1*(s)* = *A*0*/(*1 + *s/*ω0*)*, and only the load capacitance, *CL* , is included. We wish to determine *Vout/Vin* = −*Gm Zout*. To compute *Gm(s)* (with the output node grounded), we note from Example 9.11 that the impedance seen looking into the source of *M*<sup>2</sup> is equal to *rO*2*/*[1 + *(A*<sup>1</sup> + 1*)gm*2*rO*2], and divide the drain current of *M*<sup>1</sup> between this impedance and *rO*1:

$$G\_m(s) = g\_{m1} \frac{r\_{O1}}{r\_{O1} + \frac{r\_{O2}}{1 + (A\_1 + 1)g\_{m2}r\_{O2}}} \tag{9.34}$$

$$=\frac{g\_{m1}r\_{O1}[1+(A\_1+1)g\_{m2}r\_{O2}]}{r\_{O1}+(A\_1+1)g\_{m2}r\_{O2}r\_{O1}+r\_{O2}}\tag{9.35}$$

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage operational amplifier (op-amp) circuit. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1(s))**: 
   - The op-amp is represented by a triangle symbol with a positive (+) and negative (-) input terminal.
   - The positive input terminal is connected to a bias voltage \( V_b \).
   - The negative input terminal is connected to a node labeled \( P \).

2. **Transistors (M1 and M2)**:
   - **M1**: This is an NMOS transistor with its gate connected to the input voltage \( V_{in} \), its source connected to ground, and its drain connected to node \( P \).
   - **M2**: This is a PMOS transistor with its gate connected to the output of the op-amp \( A1(s) \), its source connected to the supply voltage, and its drain connected to the output node \( V_{out} \).

3. **Capacitor (C_L)**:
   - A capacitor \( C_L \) is connected between the output node \( V_{out} \) and ground. This capacitor represents the load capacitance.

4. **Output Impedance (Z_{out})**:
   - The output impedance \( Z_{out} \) is indicated at the output node \( V_{out} \).

5. **Connections**:
   - The output of the op-amp \( A1(s) \) is connected to the gate of the PMOS transistor \( M2 \).
   - The drain of the PMOS transistor \( M2 \) is connected to the output node \( V_{out} \).
   - The node \( P \) is a common connection point for the drain of the NMOS transistor \( M1 \) and the negative input of the op-amp \( A1(s) \).

This circuit is a typical configuration for a two-stage op-amp, where the first stage is a differential amplifier (formed by the op-amp \( A1(s) \) and transistor \( M1 \)), and the second stage is a common-source amplifier (formed by transistor \( M2 \)). The capacitor \( C_L \) represents the load capacitance, and the output impedance \( Z_{out} \) is shown at the output node \( V_{out} \).
```

**Figure 9.37** Circuit for analysis of frequency response.

Now, we calculate *Zout(s)* as the parallel combination of *CL* and the impedance seen looking into the drain of *M*2. From Eq. (9.21), we have

$$Z\_{out} = \left[r\_{O1} + (A\_1 + 1)g\_{m2}r\_{O2}r\_{O1} + r\_{O2}\right] || \frac{1}{C\_L s} \tag{9.36}$$

It follows that

Razavi-3930640 book December 17, 201516:59 372

$$\frac{V\_{out}}{V\_{in}}(\mathbf{s}) = -G\_m(\mathbf{s})Z\_{out}(\mathbf{s})\tag{9.37}$$

$$=\frac{-g\_{m1}r\_{O1}[1+(A\_1+1)g\_{m2}r\_{O2}]}{(r\_{O1}+r\_{O2})C\_Ls+(A\_1+1)g\_{m2}r\_{O2}r\_{O1}C\_Ls+1}\tag{9.38}$$

While it is tempting to assume that *A*<sup>1</sup> " 1 and hence neglect some terms, we must bear in mind that *A*<sup>1</sup> falls at high frequencies. Replacing *A*<sup>1</sup> with *A*0*/(*1 + *s/*ω0*)* yields

$$\frac{V\_{\rm out}}{V\_{\rm in}}(\mathbf{s}) = \frac{-g\_{m1}r\_{O1}[(1+g\_{m2}r\_{O2})\frac{\mathbf{s}}{a\rho\_0} + (A\_0+1)g\_{m2}r\_{O2} + 1]}{a\rho\_0} \tag{9.39}$$

$$\frac{V\_{O1} + (r\_{O2})C\_L}{a\rho\_0}[1 + g\_{m2}(r\_{O2}||r\_{O1})]\mathbf{s}^2 + [(r\_{O1}+r\_{O2})C\_L + (A\_0+1)g\_{m2}r\_{O2}r\_{O1}C\_L + \frac{1}{a\rho\_0}]\mathbf{s} + 1} \tag{9.30}$$

It is interesting to note that, if we had assumed *A*<sup>1</sup> to be large for *Gm* and *Zout* calculations, we would have obtained a *first-order* transfer function. The circuit exhibits a zero in the left half plane given by

$$|\omega\_z| \approx (A\_0 + 1)\omega\_0 \tag{9.40}$$

if *gm*2*rO*<sup>2</sup> " 1. Produced by the path through *A*1, this zero is on the order of the unity-gain bandwidth of the auxiliary amplifier.

To estimate pole frequencies, we assume that one is much greater than the other and apply the dominantpole approximation (Chapter 6). The dominant pole is given by the inverse of the coefficient of *s* in the denominator of (9.39):

$$|\omega\_{p1}| = \frac{1}{[r\_{O1} + (A\_0 + 1)g\_{m2}r\_{O2}r\_{O1} + r\_{O2}]C\_L + \frac{1}{a\nu\_0}}\tag{9.41}$$

$$\approx \frac{1}{A\_0g\_mr\_{O2}r\_{O1}C\_L}\tag{9.42}$$

The first time constant in the denominator of (9.41) corresponds to the output pole if *A*<sup>1</sup> were ideal, i.e., if <sup>ω</sup><sup>0</sup> <sup>=</sup> <sup>+</sup>. The nondominant pole is equal to the ratio of the coefficients of *<sup>s</sup>* and *<sup>s</sup>*2:

$$|\omega\_{p2}| = \frac{[r\_{O1} + (A\_0 + 1)g\_{m2}r\_{O2}r\_{O1} + r\_{O2}]C\_L + \frac{1}{\alpha\_0}}{\frac{(r\_{O1} + r\_{O2})C\_L}{\alpha\_0}[1 + g\_{m2}(r\_{O1}||r\_{O2})]} \tag{9.43}$$

$$\approx (A\_0 + 1)\omega\_0 + \frac{1}{g\_{m2}r\_{O2}r\_{O1}C\_L} \tag{9.44}$$

if *gm*2*(rO*1||*rO*2*)* " 1 (not necessarily a good approximation, but just to see trends). We observe that the second pole is somewhat *above* the unity-gain bandwidth of the original cascode, *(gm*2*rO*2*rO*1*CL )*−1. Note that the term 1*/(gm*2*rO*2*rO*1*CL )* also represents the output pole in the absence of *A*1.

#### ▲**Example 9.15**

Razavi-3930640 book December 17, 201516:59 373

Is the dominant-pole approximation valid here?

### **Solution**

Assuming *(A*<sup>0</sup> + 1*)gm*2*rO*2*rO*<sup>1</sup> " *rO*1, *rO*2, we find the ratio of (9.44) and (9.41):

$$\frac{^{\alpha\phi\_{P2}}}{^{\alpha\phi\_{P1}}} \approx \left[ (A\_0 + \mathrm{l})\alpha\_0 + \frac{\mathrm{l}}{\mathrm{g}\_{m2}r\_{O2}r\_{O1}C\_L} \right] \left[ (A\_0 + \mathrm{l})\mathrm{g}\_{m2}r\_{O2}r\_{O1}C\_L + \frac{\mathrm{l}}{\mathrm{a}\_0} \right] \tag{9.45}$$

$$\approx \left(A0+\text{l}\right)^2 g\_{m2} r o\_2 r o\_1 \text{C}\_L a\_0 + \text{2}(A0+\text{l}) + \frac{\text{l}}{g\_{m2} r\_{O2} r\_{O1} \text{C}\_L a\_0} \tag{9.46}$$

The second term is typically much greater than unity, making the approximation valid.

Figure 9.38 plots the approximate frequency response of the cascode structure before and after gain boosting. The key point here is that the auxiliary amplifier contributes a second pole located above the original −3-dB bandwidth by an amount equal to *A*0ω0.

Here is the image describtion:
```
The image is a Bode plot that shows the frequency response of two different cascode amplifier configurations: the original cascode and the regulated cascode. The plot is on a logarithmic scale for both the magnitude (|Vout/Vin|) and the frequency (ω).

### Key Features of the Plot:

1. **Axes:**
   - The vertical axis represents the magnitude of the voltage gain (|Vout/Vin|) in decibels (dB).
   - The horizontal axis represents the angular frequency (ω) on a logarithmic scale.

2. **Gain Levels:**
   - The gain of the original cascode amplifier is represented by a horizontal dashed line at the level of \( g_{m1} r_{o1} g_{m2} r_{o2} \).
   - The gain of the regulated cascode amplifier is higher, represented by a horizontal solid line at the level of \( A_0 g_{m1} r_{o1} g_{m2} r_{o2} \).

3. **Breakpoints:**
   - The first breakpoint for the regulated cascode occurs at \( \frac{1}{A_0 g_{m1} r_{o1} g_{m2} r_{o2} C_L} \).
   - The first breakpoint for the original cascode occurs at \( \frac{1}{g_{m1} r_{o1} g_{m2} r_{o2} C_L} \).
   - The second breakpoint for both configurations occurs at \( \frac{1}{g_{m2} r_{o2} r_{o1} C_L} \).
   - There is an additional breakpoint for the regulated cascode at \( \frac{1}{g_{m2} r_{o2} r_{o1} C_L} + A_0 \omega_0 \).

4. **Frequency Response:**
   - For the regulated cascode, the gain remains constant at \( A_0 g_{m1} r_{o1} g_{m2} r_{o2} \) until the first breakpoint, after which it starts to decrease.
   - For the original cascode, the gain remains constant at \( g_{m1} r_{o1} g_{m2} r_{o2} \) until its first breakpoint, after which it starts to decrease.
   - Both configurations show a decrease in gain after their respective breakpoints, with the regulated cascode maintaining a higher gain over a wider frequency range compared to the original cascode.

### Notations:
- \( A_0 \): Open-loop gain of the amplifier.
- \( g_{m1}, g_{m2} \): Transconductance of the first and second transistors, respectively.
- \( r_{o1}, r_{o2} \): Output resistance of the first and second transistors, respectively.
- \( C_L \): Load capacitance.
- \( \omega_0 \): A specific angular frequency related to the regulated cascode.

### Summary:
The plot illustrates that the regulated cascode amplifier has a higher gain and a wider bandwidth compared to the original cascode amplifier. The regulated cascode maintains its gain over a larger frequency range before it starts to roll off, indicating better performance in terms of frequency response.
```

**Figure 9.38** Frequency response of gain-boosted stage.

# **9.5 Comparison**

Our study of op amps in this chapter has introduced four principal topologies: telescopic cascode, folded cascode, two-stage op amp, and gain boosting. It is instructive to compare various performance aspects of these circuits to gain a better view of their applicability. Table 9.1 comparatively presents important attributes of each op amp topology. We study the speed differences in Chapter 10.

# **9.6 Output Swing Calculations**

In today's low-voltage op amp designs, the output voltage swing proves the most important factor. We have seen in previous sections how to assume a certain required output swing and accordingly allocate overdrive voltages to the transistors. But how do we verify that the final design indeed accommodates the

▲

|                | Gain   | Output<br>Swing | Speed   | Power<br>Dissipation | Noise  |
|----------------|--------|-----------------|---------|----------------------|--------|
| Telescopic     | Medium | Medium          | Highest | Low                  | Low    |
| Folded−Cascode | Medium | Medium          | High    | Medium               | Medium |
| Two−Stage      | High   | Highest         | Low     | Medium               | Low    |
| Gain−Boosted   | High   | Medium          | Medium  | High                 | Medium |

**Table 9.1** Comparison of performance of various op amp topologies.

specified swing? To answer this question, we must first ask, what exactly happens if the circuit cannot sustain the swing? Since the border between the saturation and triode regions begins to diminish in nanometer devices, we cannot readily decide on the operation region of the transistors at the extremes of the output swing. A more rigorous approach is therefore necessary.

If the output voltage excursion pushes a transistor into the triode region, then the voltage gain drops. We can thus use simulations to examine the gain as the output swing grows. Illustrated in Fig. 9.39(a), the idea is to apply to the input a growing sinusoid (or different sinusoidal amplitudes in different simulations), monitor the resulting output, and calculate |*Vout/Vin*| as *Vin* and *Vout* grow. The gain begins to drop as the output swing reaches its maximum "allowable" voltage, *V*1. We may even choose *V*<sup>1</sup> to allow a small drop in the gain, say, 10% (about 1 dB). Beyond *V*1, the gain falls further, causing significant nonlinearity.

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b), each depicting different electronic circuit configurations and their corresponding behaviors.

(a) The first part of the image shows a basic operational amplifier (op-amp) configuration and its frequency response. The left side of (a) illustrates a sinusoidal input signal being fed into an op-amp. The op-amp is represented by a triangle with two input terminals (one marked with a plus sign for the non-inverting input and one with a minus sign for the inverting input) and one output terminal. The output signal is also sinusoidal but with a larger amplitude, indicating amplification.

To the right of the op-amp, there is a graph plotting the ratio of the output voltage to the input voltage (|V_out/V_in|) against the input voltage (V_in). The graph shows that the gain remains constant up to a certain input voltage (V1), after which it starts to decrease. This indicates that the op-amp has a limited linear operating range, and beyond a certain input voltage, the gain drops off.

(b) The second part of the image shows a specific op-amp circuit configuration known as a non-inverting amplifier. In this configuration, the input signal is applied to the non-inverting input (+) of the op-amp. The inverting input (-) is connected to a voltage divider network formed by two resistors, R1 and R2. R1 is connected between the inverting input and ground, while R2 is connected between the inverting input and the output of the op-amp (V_out).

This configuration provides a feedback mechanism that stabilizes the gain of the amplifier. The gain of the non-inverting amplifier is determined by the values of R1 and R2 and is given by the formula: Gain = 1 + (R2/R1). The output voltage (V_out) is an amplified version of the input voltage, with the amplification factor set by the resistor values.

Overall, the image illustrates the basic concept of op-amp amplification, the frequency response of an op-amp, and a specific non-inverting amplifier circuit configuration.
```

**Figure 9.39** (a) Simulation of gain versus input amplitude, and (b) feedback amplifier.

The reader may wonder how much gain reduction is acceptable. In some applications, the reduction of the open-loop gain, and hence the gain error of the closed-loop system, are critical (Chapter 13). In other applications, we are concerned with the output distortion of the *closed-loop* circuit. In such a case, we place the op amp in the closed-loop environment of interest, e.g., the inverting configuration of Fig. 9.39(b), apply a sinusoid to the input, and measure the distortion (harmonics) at the output in simulations. The maximum output amplitude that yields an acceptable distortion is considered the maximum output swing.

# **9.7 Common-Mode Feedback**

### **9.7.1 Basic Concepts**

In this and previous chapters, we have described many advantages of fully differential circuits over their single-ended counterparts. In addition to greater output swings, differential op amps avoid mirror poles, thus achieving a higher closed-loop speed. However, high-gain differential circuits require "commonmode feedback" (CMFB).

To understand the need for CMFB, let us begin with a simple realization of a differential amplifier [Fig. 9.40(a)]. In some applications, we short the inputs and outputs for part of the operation [Fig. 9.40(b)],

Here is the image describtion:
```
The image consists of two parts, labeled (a) and (b), each depicting a different electronic circuit involving a differential amplifier.

### Part (a):
1. **Top Symbol**: 
   - The top part shows a differential amplifier symbol with two inputs (positive and negative) and one output.
   
2. **Circuit Diagram**:
   - The circuit below the symbol is a differential amplifier using MOSFETs.
   - **Power Supply**: The circuit is powered by a voltage source \( V_{DD} \) at the top.
   - **Resistors**: Two resistors \( R_D \) are connected from \( V_{DD} \) to the drains of the MOSFETs \( M_1 \) and \( M_2 \).
   - **MOSFETs**: There are two NMOS transistors, \( M_1 \) and \( M_2 \), with their sources connected together and to a current source \( I_{SS} \) which is connected to ground.
   - **Input**: The gate of \( M_1 \) is connected to the input voltage \( V_{in} \).
   - **Output**: The output voltage \( V_{out} \) is taken from the common connection point of the drains of \( M_1 \) and \( M_2 \).

### Part (b):
1. **Top Symbol**: 
   - Similar to part (a), the top part shows a differential amplifier symbol with two inputs (positive and negative) and one output.
   
2. **Circuit Diagram**:
   - The circuit below the symbol is another differential amplifier using MOSFETs, but with a slight modification compared to part (a).
   - **Power Supply**: The circuit is powered by a voltage source \( V_{DD} \) at the top.
   - **Resistors**: Two resistors \( R_D \) are connected from \( V_{DD} \) to the drains of the MOSFETs \( M_1 \) and \( M_2 \).
   - **MOSFETs**: There are two NMOS transistors, \( M_1 \) and \( M_2 \), with their sources connected together and to a current source \( I_{SS} \) which is connected to ground.
   - **Input**: The gates of \( M_1 \) and \( M_2 \) are connected to the differential inputs of the amplifier symbol.
   - **Output**: The output voltage \( V_{out} \) is taken from the common connection point of the drains of \( M_1 \) and \( M_2 \).

### Key Differences:
- In part (a), the input \( V_{in} \) is applied only to the gate of \( M_1 \), while in part (b), the differential inputs are applied to both \( M_1 \) and \( M_2 \).
- The circuit in part (b) is a more complete representation of a differential amplifier with differential inputs, whereas part (a) shows a single-ended input configuration.
```

**Figure 9.40** (a) Simple differential pair; (b) circuit with inputs shorted to outputs.

providing *differential* negative feedback. The input and output common-mode levels in this case are fairly well defined, equal to *VDD* − *ISS RD/*2.

Now suppose the load resistors are replaced by PMOS current sources so as to increase the differential voltage gain [Fig. 9.41(a)]. What is the common-mode level at nodes *X* and *Y* ? Since each of the input transistors carries a current of *ISS/*2, the CM level depends on how close *ID*<sup>3</sup> and *ID*<sup>4</sup> are to this value. In practice, as exemplified by Fig. 9.41(b), mismatches in the PMOS and NMOS current mirrors defining *ISS* and *ID*<sup>3</sup>*,*<sup>4</sup> create a finite error between *ID*<sup>3</sup>*,*<sup>4</sup> and *ISS/*2. Suppose, for example, that the drain currents of *M*<sup>3</sup> and *M*<sup>4</sup> in the saturation region are slightly greater than *ISS/*2. As a result, to satisfy Kirchhoff's current law at nodes *X* and *Y* , both *M*<sup>3</sup> and *M*<sup>4</sup> must enter the triode region so that their drain currents fall to *ISS/*2. Conversely, if *ID*<sup>3</sup>*,*<sup>4</sup> *< ISS/*2, then both *VX* and *VY* must drop so that *M*<sup>5</sup> enters the triode region, thereby producing only 2*ID*<sup>3</sup>*,*4.

Here is the image describtion:
```
The image shows two different configurations of a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).

### (a) Basic Differential Amplifier
1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors. They receive the differential input signals at their gates (X and Y).
   - **M3 and M4:** These are the load transistors, typically acting as active loads for the differential pair.
2. **Current Source:**
   - **ISS:** This is a current source connected to the common source node of M1 and M2, providing a constant current.
3. **Biasing:**
   - **Vb:** This is the bias voltage applied to the gates of M3 and M4 to set their operating point.
4. **Power Supply:**
   - **VDD:** This is the positive power supply voltage.
5. **Output:**
   - **Vout:** This is the differential output voltage taken from the common drain node of M1 and M2.

### (b) Differential Amplifier with Improved Biasing
1. **Transistors:**
   - **M1 and M2:** Similar to (a), these are the input differential pair transistors.
   - **M3 and M4:** These are the load transistors, similar to (a).
   - **Mb1 and Mb2:** These are additional transistors used for improved biasing and current mirroring.
   - **M5:** This transistor is used to mirror the current from the current source ISS.
2. **Current Source:**
   - **ISS:** This is a current source connected to the source of M5, providing a constant current.
3. **Resistor:**
   - There is a resistor connected between the source of Mb2 and the ground, which helps in setting the bias current.
4. **Biasing:**
   - The gates of Mb1 and Mb2 are connected to the same node, ensuring that they operate in a current mirror configuration.
5. **Power Supply:**
   - **VDD:** This is the positive power supply voltage.
6. **Output:**
   - **Vout:** This is the differential output voltage taken from the common drain node of M1 and M2.

### Key Differences:
- The circuit in (b) includes additional transistors (Mb1, Mb2, and M5) and a resistor to improve the biasing and stability of the differential amplifier.
- The W/L ratios (Width/Length) of the transistors are indicated in (b), showing that M5 has twice the W/L ratio compared to M1 and M2, which affects the current mirroring and biasing.

Overall, the circuit in (b) is a more sophisticated version of the basic differential amplifier shown in (a), with enhanced biasing and current mirroring for better performance.
```

**Figure 9.41** (a) High-gain differential pair with inputs shorted to outputs, and (b) effect of current mismatches.

The above difficulties fundamentally arise because in high-gain amplifiers, we wish a *p*-type current source [e.g., *M*<sup>3</sup> and *M*<sup>4</sup> in Fig. 9.41(b)] to balance an *n*-type current source (e.g., *M*5). As illustrated in Fig. 9.42, the difference between *IP* and *IN* must flow through the intrinsic output impedance of the

Here is the image describtion:
```
The image depicts a simplified model of a high-gain amplifier circuit. The circuit consists of the following components:

1. **Current Sources**:
   - There are two current sources labeled \( I_P \) and \( I_N \).
   - \( I_P \) is connected to the positive supply voltage \( V_{DD} \) and is directed downwards.
   - \( I_N \) is connected to the ground and is directed upwards.

2. **Resistors**:
   - There are two resistors labeled \( R_P \) and \( R_N \).
   - \( R_P \) is connected between the node where \( I_P \) and \( I_N \) meet and the positive supply voltage \( V_{DD} \).
   - \( R_N \) is connected between the same node and the ground.

3. **Node**:
   - The node where \( I_P \) and \( I_N \) meet is indicated, and the current flowing through this node is \( I_P - I_N \).

4. **Voltage Supply**:
   - The positive supply voltage is labeled \( V_{DD} \).
   - The ground is indicated at the bottom of the circuit.

The figure is labeled as "Figure 9.42 Simplified model of high-gain amplifier." This suggests that the circuit is a basic representation of a high-gain amplifier, where the difference in currents \( I_P \) and \( I_N \) is used to amplify the signal. The resistors \( R_P \) and \( R_N \) likely play a role in setting the gain and biasing of the amplifier.
```

amplifier, creating an output voltage change of *(IP* − *IN )(RP* %*RN )*. Since the current error depends on mismatches and *RP* %*RN* is quite high, the voltage error may be large, thus driving the *p*-type or *n*-type current source into the triode region. As a general rule, if the output CM level cannot be determined by "visual inspection" and requires calculations based on device properties, then it is poorly defined. This is the case in Fig. 9.41 but not in Fig. 9.40. We emphasize that differential feedback cannot define the CM level.

Students often make two mistakes here. First, they assume that differential feedback corrects the output common-mode level. As explained for the simple circuit of Fig. 9.41(a), differential feedback from *X* and *Y* to the inputs cannot prohibit the output CM level from taking off toward *VDD* or ground. Second, they finely adjust *Vb* in simulations so as to bring *VX* and *VY* to around *VDD/*2 concluding that the circuit does not need CM feedback. We have recognized, however, that random mismatches between the top and bottom current sources cause the CM level to fall or rise considerably. Such mismatches are always present in actual circuits and cause the op amp to fail if no CMFB is used.

#### ▲**Example 9.16**

Razavi-3930640 book December 17, 201516:59 376

Consider the telescopic op amp designed in Example 9.5 and repeated in Fig. 9.43 with bias current mirrors. Suppose *M*<sup>9</sup> suffers from a 1% current mismatch with respect to *M*10, producing *ISS* = 2*.*97 mA rather than 3 mA. Assuming perfect matching for other transistors, explain what happens in the circuit.

Here is the image describtion:
```
The image depicts a complex CMOS (Complementary Metal-Oxide-Semiconductor) circuit, likely an operational amplifier or a similar analog circuit. Here is a detailed description of the circuit:

1. **Power Supply and Ground:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top.
   - The ground is at the bottom of the circuit.

2. **Transistors:**
   - The circuit consists of multiple MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors), labeled \( M_1 \) through \( M_{11} \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) form a current mirror load.
   - \( M_7 \) and \( M_8 \) are additional transistors connected to the output.
   - \( M_9 \) is a current source transistor with a current \( I_{SS} = 2.97 \) mA.
   - \( M_{10} \) and \( M_{11} \) are part of the biasing network.

3. **Biasing Network:**
   - A current source of 300 µA is connected to a resistor \( R_1 \) and the gate of \( M_{11} \).
   - The voltage across \( R_1 \) sets the bias voltage \( V_{b2} \) for the gate of \( M_5 \) and \( M_6 \).
   - \( V_{b1} \) is another bias voltage applied to the gates of \( M_3 \) and \( M_4 \).

4. **Current Source:**
   - \( M_9 \) acts as a current source with a specified current \( I_{SS} = 2.97 \) mA, providing the tail current for the differential pair \( M_1 \) and \( M_2 \).

5. **Input and Output:**
   - The input voltage \( V_{in} \) is applied to the gate of \( M_1 \).
   - The output voltage \( V_{out} \) is taken from the node between \( M_5 \) and \( M_6 \).

6. **Nodes:**
   - Node X is the connection point between \( M_3 \) and \( M_5 \).
   - Node Y is the connection point between \( M_4 \) and \( M_6 \).

7. **Operation:**
   - The circuit operates as a differential amplifier where the differential input voltage \( V_{in} \) is amplified and appears at the output \( V_{out} \).
   - The current mirrors and biasing network ensure proper operation and stability of the amplifier.

This detailed description covers the main components and their connections in the CMOS circuit shown in the image.
```

### **Solution**

From Example 9.5, the single-ended output impedance of the circuit equals 266 k%. Since the difference between the drain currents of *M*<sup>3</sup> and *M*<sup>5</sup> (and *M*<sup>4</sup> and *M*6) is 30 *µ*A*/*2 = 15 *µ*A, the output voltage error would be 266 k%×15 *µ*A= 3*.*99 V. Since this large error cannot be produced, *VX* and *VY* must rise so much that *M*5–*M*<sup>6</sup> and *M*7–*M*<sup>8</sup> enter the triode region, yielding *ID*<sup>7</sup>*,*<sup>8</sup> = 1*.*485 mA. We should also mention that another important source

of CM error in the simple biasing scheme of Fig. 9.43 is the *deterministic* error between *ID*<sup>7</sup>*,*<sup>8</sup> and *ID*<sup>11</sup> (and also between *ID*<sup>9</sup> and *ID*10) due to their different drain-source voltages. This error can nonetheless be reduced by means of the current mirror techniques of Chapter 5.

The foregoing study implies that in high-gain amplifiers, the output CM level is sensitive to device properties and mismatches and it cannot be stabilized by means of *differential* feedback. Thus, a commonmode feedback network must be added to sense the CM level of the two outputs and adjust one of the bias currents in the amplifier. Following our view of feedback systems in Chapter 8, we divide the task of CMFB into three operations: sensing the output CM level, comparison with a reference, and returning the error to the amplifier's bias network. Figure 9.44 conceptually illustrates the idea.

Here is the image describtion:
```
The image depicts a common-mode feedback (CMFB) circuit used in analog design, particularly in differential amplifiers. Here is a detailed description of the components and their connections:

1. **Transistors (M1 and M2)**: The circuit features two MOSFET transistors, labeled M1 and M2. These transistors are arranged in a differential pair configuration. The sources of both transistors are connected together and to a current source that is grounded.

2. **Current Sources**: There are three current sources in the circuit. One is connected to the common source node of M1 and M2, providing a bias current. The other two current sources are connected to the drains of M1 and M2, providing the necessary current for the differential pair operation.

3. **Output Nodes (Vout1 and Vout2)**: The drains of M1 and M2 are connected to the output nodes Vout1 and Vout2, respectively. These nodes are also connected to the current sources mentioned above.

4. **CM Level Sense Circuit**: The output nodes Vout1 and Vout2 are connected to a common-mode level sense circuit. This circuit is responsible for sensing the common-mode voltage of the differential pair outputs.

5. **Operational Amplifier**: The common-mode level sense circuit feeds into an operational amplifier (op-amp). The non-inverting input of the op-amp is connected to a reference voltage (VREF), while the inverting input is connected to the output of the common-mode level sense circuit.

6. **Feedback Loop**: The output of the op-amp is connected back to the common source node of M1 and M2, forming a feedback loop. This feedback loop adjusts the bias current to maintain the desired common-mode voltage at the output nodes.

7. **Power Supply (VDD)**: The circuit is powered by a supply voltage VDD, which is connected to the current sources at the drains of M1 and M2.

In summary, this circuit is designed to maintain a stable common-mode voltage at the output nodes of a differential pair by using a feedback mechanism involving a common-mode level sense circuit and an operational amplifier.
```

**Figure 9.44** Conceptual topology for common-mode feedback.

# **9.7.2 CM Sensing Techniques**

In order to sense the output CM level, we recall that *Vout,C M* = *(Vout*1+*Vout*2*)/*2, where *Vout*<sup>1</sup> and *Vout*<sup>2</sup> are the single-ended outputs. It therefore seems plausible to employ a resistive divider as shown in Fig. 9.45, generating *Vout,C M* = *(R*1*Vout*<sup>2</sup> + *R*2*Vout*1*)/(R*<sup>1</sup> + *R*2*)*, which reduces to *(Vout*<sup>1</sup> + *Vout*2*)/*2 if *R*<sup>1</sup> = *R*2. The difficulty, however, is that *R*<sup>1</sup> and *R*<sup>2</sup> must be much greater than the output impedance of the op amp so as to avoid lowering the open-loop gain. For example, in the design of Fig. 9.43, the output impedance equals 266 k%, necessitating a value of several megaohms for *R*<sup>1</sup> and *R*2. As explained in Chapter 18, such large resistors occupy a very large area and, more important, suffer from substantial parasitic capacitance to the substrate.

Here is the image describtion:
```
The image depicts a differential amplifier circuit with active loads. Here is a detailed description of the circuit:

1. **Transistors**: The circuit consists of six MOSFET transistors. The top and bottom pairs of transistors are arranged in a differential configuration.
   - The top pair of transistors are PMOS transistors.
   - The bottom pair of transistors are NMOS transistors.

2. **Differential Pair**: The middle transistors form the differential pair.
   - The left middle transistor is connected to the output node \( V_{out1} \).
   - The right middle transistor is connected to the output node \( V_{out2} \).

3. **Resistors**: There are two resistors, \( R_1 \) and \( R_2 \), connected between the output nodes.
   - \( R_1 \) is connected between \( V_{out1} \) and a common node.
   - \( R_2 \) is connected between the common node and \( V_{out2} \).

4. **Common-Mode Output**: There is a node labeled \( V_{out,CM} \) which is connected to the common node between \( R_1 \) and \( R_2 \).

5. **Power Supply**: The circuit is powered by a voltage source connected to the top and bottom of the circuit.
   - The top of the circuit is connected to the positive supply voltage.
   - The bottom of the circuit is connected to ground.

6. **Connections**:
   - The sources of the PMOS transistors are connected to the positive supply voltage.
   - The drains of the PMOS transistors are connected to the drains of the NMOS transistors.
   - The sources of the NMOS transistors are connected to ground.

7. **Operation**: 
   - The differential pair (middle transistors) amplifies the difference between the input signals applied to their gates.
   - The PMOS transistors act as active loads for the differential pair.
   - The resistors \( R_1 \) and \( R_2 \) help in setting the common-mode output voltage \( V_{out,CM} \).

This circuit is typically used in analog signal processing to amplify the difference between two input signals while rejecting any common-mode signals.
```

Here is the image describtion:
```
The image appears to be a caption for a figure labeled "Figure 9.45" from a technical or academic text. The caption describes the figure as illustrating "Common-mode feedback with resistive sensing." This suggests that the figure likely depicts a circuit or system that uses resistors to sense and provide feedback to control the common-mode voltage in an electronic circuit. Common-mode feedback is typically used in differential amplifiers to stabilize the common-mode output voltage and improve performance. The specific details of the circuit, such as the arrangement of resistors and other components, are not visible in the provided image.
```

To eliminate the resistive loading, we can interpose source followers between each output and its corresponding resistor. Illustrated in Fig. 9.46, this technique produces a CM level that is in fact lower than the output CM level by *VG S*<sup>7</sup>*,*8, but this shift can be taken into account in the comparison operation. Note that *R*<sup>1</sup> and *R*<sup>2</sup> or *I*<sup>1</sup> and *I*<sup>2</sup> must be large enough to ensure that *M*<sup>7</sup> or *M*<sup>8</sup> is not "starved" when

▲

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source \( V_{DD} \) at the top of the diagram.

2. **Transistors:**
   - The circuit consists of eight MOSFET transistors labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the current mirror load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the tail current source transistors.
   - \( M_7 \) and \( M_8 \) are the transistors used in the common-mode feedback (CMFB) circuit.

3. **Current Sources:**
   - There are two current sources, \( I_1 \) and \( I_2 \), connected to the sources of \( M_5 \) and \( M_6 \), and to the common-mode feedback circuit, respectively.

4. **Resistors:**
   - Two resistors, \( R_1 \) and \( R_2 \), are connected in series at the output of the CMFB circuit.

5. **Outputs:**
   - The differential outputs are labeled \( V_{out1} \) and \( V_{out2} \).
   - The common-mode output voltage is labeled \( V_{out,CM} \).

6. **Connections:**
   - The sources of \( M_1 \) and \( M_2 \) are connected to the drains of \( M_5 \) and \( M_6 \), respectively.
   - The gates of \( M_3 \) and \( M_4 \) are connected to the drains of \( M_1 \) and \( M_2 \), respectively.
   - The drains of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The sources of \( M_7 \) and \( M_8 \) are connected to the drains of \( M_3 \) and \( M_4 \), respectively.
   - The gates of \( M_7 \) and \( M_8 \) are connected to the common-mode feedback circuit.
   - The output of the common-mode feedback circuit is connected to the series combination of \( R_1 \) and \( R_2 \), and then to the current source \( I_2 \).

This circuit is designed to amplify the difference between the input signals while rejecting common-mode signals, with the common-mode feedback circuit ensuring that the common-mode output voltage is regulated.
```

**Figure 9.46** Common-mode feedback using source followers.

a large differential swing appears at the output. As conceptually depicted in Fig. 9.47, if, say, *Vout*<sup>2</sup> is quite higher than *Vout*1, then *I*<sup>1</sup> must sink both *IX* ≈ *(Vout*<sup>2</sup> − *Vout*1*)/(R*<sup>1</sup> + *R*2*)* and *ID*7. Consequently, if *R*<sup>1</sup> + *R*<sup>2</sup> or *I*<sup>1</sup> is not sufficiently large, *ID*<sup>7</sup> drops to zero and *Vout,C M* no longer represents the true output CM level.

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage (V_DD).

2. **Transistors (M7 and M8)**: 
   - M7 and M8 are NMOS transistors.
   - The source of M7 is connected to a current source I1, which is connected to ground.
   - The source of M8 is connected to a current source I2, which is also connected to ground.
   - The drain of M7 is connected to V_DD through a load (not shown explicitly).
   - The drain of M8 is connected to V_DD through a load (not shown explicitly).

3. **Input and Output Nodes**:
   - V_out1 is the input voltage applied to the gate of M7.
   - V_out2 is the input voltage applied to the gate of M8.
   - The output voltage V_out1 is taken from the drain of M7.
   - The output voltage V_out2 is taken from the drain of M8.

4. **Common-Mode Feedback (CMFB) Network**:
   - The CMFB network consists of two resistors, R1 and R2, connected in series between the sources of M7 and M8.
   - The node between R1 and R2 is labeled as V_out,CM, which represents the common-mode output voltage.
   - A current source I_X is connected between the node V_out,CM and ground.

5. **Current Sources (I1, I2, and I_X)**:
   - I1 and I2 are current sources connected to the sources of M7 and M8, respectively, providing bias currents.
   - I_X is a current source connected to the node V_out,CM, providing a feedback current to control the common-mode voltage.

6. **Connections**:
   - The gate of M7 is connected to the input voltage V_out1.
   - The gate of M8 is connected to the input voltage V_out2.
   - The sources of M7 and M8 are connected through the resistors R1 and R2, with the node between them connected to the current source I_X.

This circuit is designed to amplify the differential input signals (V_out1 and V_out2) while maintaining a stable common-mode output voltage (V_out,CM) through the feedback mechanism provided by the resistors R1, R2, and the current source I_X.
```

**Figure 9.47** Current starvation of source followers for large swings.

The sensing method of Fig. 9.46 nevertheless suffers from an important drawback: it limits the differential output swings (even if *R*<sup>1</sup>*,*<sup>2</sup> and *I*<sup>1</sup>*,*<sup>2</sup> are large enough). To understand why, let us determine the minimum allowable level of *Vout*<sup>1</sup> (and *Vout*2), noting that without CMFB, it would be equal to *VO D*<sup>3</sup> + *VO D*5. With the source followers in place, *Vout*<sup>1</sup>*,min* = *VG S*<sup>7</sup> + *VI* 1, where *VI* <sup>1</sup> denotes the minimum voltage required across *I*1. This is roughly equal to two overdrive voltages plus one threshold voltage. Thus, the swing at each output is reduced by approximately *VT H* , a significant value in low-voltage design.

Looking at Fig. 9.45, the reader may wonder if the output CM level can be sensed by means of *capacitors*, rather than resistors, so as to avoid degrading the low-frequency open-loop gain of the op amp. This is indeed possible in some cases and will be studied in Chapter 13.

Another type of CM sensing is depicted in Fig. 9.48(a). Here, identical transistors *M*<sup>7</sup> and *M*<sup>8</sup> operate in the deep triode region, introducing a total resistance between *P* and ground equal to

$$R\_{tot} = R\_{on7} \| R\_{on8} \tag{9.47}$$

$$=\frac{1}{\mu\_n C\_{ox} \frac{W}{L} (V\_{out1} - V\_{TH})} \left| \frac{1}{\mu\_n C\_{ox} \frac{W}{L} (V\_{out2} - V\_{TH})} \right. \tag{9.48}$$

$$\eta = \frac{1}{\mu\_n C\_{ox} \frac{W}{L} (V\_{out2} + V\_{out1} - 2V\_{TH})} \tag{9.49}$$

Here is the image describtion:
```
The image consists of two diagrams labeled (a) and (b), which appear to be circuit schematics involving MOSFET transistors.

### Diagram (a):
- This is a more complex circuit with multiple MOSFET transistors arranged in a specific configuration.
- The circuit includes several transistors connected in series and parallel.
- There are two output nodes labeled \( V_{out1} \) and \( V_{out2} \).
- The circuit also includes two transistors labeled \( M_7 \) and \( M_8 \) at the bottom right, which are connected to a node labeled \( P \).
- The source of \( M_7 \) is connected to \( V_{out1} \), and the source of \( M_8 \) is connected to \( V_{out2} \).
- The gates of \( M_7 \) and \( M_8 \) are connected together to the node \( P \).
- The drains of \( M_7 \) and \( M_8 \) are connected to ground.

### Diagram (b):
- This is a simplified version of the circuit focusing on the transistors \( M_7 \) and \( M_8 \).
- The source of \( M_7 \) is connected to \( V_{out1} + V_{TH} \), where \( V_{TH} \) is the threshold voltage.
- The gate of \( M_7 \) is connected to the node \( P \).
- The drain of \( M_7 \) is connected to ground.
- The source of \( M_8 \) is connected to the node \( P \).
- The gate of \( M_8 \) is connected to the node \( P \).
- The drain of \( M_8 \) is connected to \( V_{out2} \).

### General Observations:
- Both diagrams involve MOSFET transistors, which are commonly used in digital and analog circuits.
- The node \( P \) is a common point in both diagrams, indicating it plays a crucial role in the circuit's operation.
- The presence of \( V_{TH} \) in diagram (b) suggests that the circuit involves threshold voltage considerations, which are important in MOSFET operation.
- The connections to ground indicate that these transistors are likely part of a larger circuit where grounding is necessary for proper operation.

Overall, the image depicts a detailed and a simplified view of a circuit involving MOSFET transistors, highlighting the connections and roles of specific components within the circuit.
```

**Figure 9.48** (a) Common-mode sensing using MOSFETs operating in the deep triode region, and (b) output levels placing *M*<sup>7</sup> at the edge of saturation.

where *W/L* denotes the aspect ratio of *M*<sup>7</sup> and *M*8. Equation (9.49) indicates that *Rtot* is a function of *Vout*<sup>2</sup> + *Vout*<sup>1</sup> but independent of *Vout*<sup>2</sup> − *Vout*1. From Fig. 9.48(a), we observe that if the outputs rise together, then *Rtot* drops, whereas if they change differentially, one *Ron* increases and the other decreases. This resistance can thus be utilized as a measure of the output CM level.

In the circuit of Fig. 9.48(a), the use of *M*<sup>7</sup> and *M*<sup>8</sup> limits the output voltage swings. Here, it may seem that *Vout,min* = *VT H*<sup>7</sup>*,*8, which is relatively close to two overdrive voltages, but the difficulty arises from the assumption above that both *M*<sup>7</sup> and *M*<sup>8</sup> operate in the deep triode region. In fact, if, say, *Vout*<sup>1</sup> drops from the equilibrium CM level to about one threshold voltage above ground [Fig. 9.48(b)] and *Vout*<sup>2</sup> rises by the same amount, then *M*<sup>7</sup> enters the saturation region, thus exhibiting a variation in its on-resistance that is not counterbalanced by that of *M*8.

It is important to bear in mind that CM sensing must produce a quantity *independent* of the differential signals. The following example illustrates this point.

#### ▲**Example 9.17**

A student simulates the step response of a closed-loop op amp circuit [e.g., that in Fig. 9.48(a)] and observes the output waveforms shown in Fig. 9.49. Explain why *Vout*<sup>1</sup> and *Vout*<sup>2</sup> do not change symmetrically.

Here is the image describtion:
```
The image is a graph depicting the behavior of two output voltages, Vout1 and Vout2, over time (t). The graph shows the following details:

1. **Axes**: 
   - The horizontal axis represents time (t).
   - The vertical axis represents voltage.

2. **Curves**:
   - There are two main curves, Vout1 and Vout2, which represent the output voltages.
   - Vout1 starts at a lower voltage and increases over time, reaching a higher steady-state value.
   - Vout2 starts at a higher voltage and decreases over time, reaching a lower steady-state value.

3. **Key Points**:
   - At time t1, both Vout1 and Vout2 are at their initial values.
   - At time t2, Vout1 has reached its higher steady-state value, and Vout2 has reached its lower steady-state value.

4. **V_CM**:
   - There is a dashed horizontal line labeled V_CM, which represents a common-mode voltage.
   - V_CM is positioned between the steady-state values of Vout1 and Vout2.

5. **Behavior**:
   - The graph shows a transition period between t1 and t2 where Vout1 and Vout2 are changing.
   - After t2, both Vout1 and Vout2 appear to stabilize at their respective steady-state values.

The figure is labeled as "Figure 9.49" in the bottom right corner.
```

### **Solution**

As evident from the waveforms, the output CM level *changes*from *t*<sup>1</sup> to *t*2, indicating that the CM sensing mechanism is nonlinear and interprets the CM levels at *t*<sup>1</sup> and *t*<sup>2</sup> differently. For example, if *M*<sup>7</sup> or *M*<sup>8</sup> in Fig. 9.48 does not remain in the deep triode region at *t*2, then Eq. (9.49) no longer holds and *VC M* becomes a function of the *differential* signals. ▲

Another CM sensing method is illustrated in Fig. 9.50. Here, the differential pairs compare the inputs with *VREF*, generating a current, *IC M* , in proportion to the input CM level. To prove this point, we write the small-signal drain currents of *M*<sup>2</sup> and *M*<sup>4</sup> as *(gm/*2*)Vout*<sup>1</sup> and *(gm/*2*)Vout*2, respectively, concluding that *IC M* ∝ *Vout*<sup>1</sup> + *Vout*2. This current can be copied to current sources within the op amp with negative feedback so as to keep *Vout,C M* approximately equal to *VREF*.

Here is the image describtion:
```
The image depicts a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Transistors**: The circuit consists of four MOSFETs labeled M1, M2, M3, and M4. These transistors are arranged in a differential pair configuration with a current mirror load.

2. **Differential Pair**: 
   - M1 and M2 form the differential pair. The gate of M1 is connected to the input voltage \( V_{out1} \), and the gate of M2 is connected to a bias voltage \( V_b \).
   - The sources of M1 and M2 are connected together and to a current source that is connected to ground. This current source sets the tail current for the differential pair.

3. **Current Mirror Load**:
   - M3 and M4 form a current mirror. The drain of M2 is connected to the drain of M4, and the drain of M1 is connected to the drain of M3.
   - The gate of M3 is connected to the gate and drain of M4, ensuring that M3 and M4 mirror each other's currents.

4. **Output Nodes**:
   - The output voltage \( V_{out1} \) is taken from the drain of M1.
   - The output voltage \( V_{out2} \) is taken from the drain of M3.

5. **Biasing and Current Source**:
   - The circuit includes a bias current source \( I_{CM} \) that is connected to the common source node of M1 and M2. This current source is responsible for providing the necessary bias current for the differential pair.
   - The bias voltage \( V_b \) is applied to the gate of M2 to set the operating point of the differential pair.

6. **Connections to Op Amp**:
   - The circuit is part of a larger operational amplifier (op-amp) design. The current mirror load (M3 and M4) is connected to current sources within the op-amp, as indicated by the arrow labeled "To Current Sources in Op Amp."

In summary, this image shows a differential amplifier with a current mirror load, which is a common building block in analog circuit design, particularly in operational amplifiers. The differential pair (M1 and M2) amplifies the difference between the input signals, while the current mirror (M3 and M4) provides the necessary load and helps in maintaining the differential operation.
```

**Figure 9.50** CM sensing circuit with high nonlinearity.

The foregoing topology faces serious issues. As *Vout*<sup>1</sup> and *Vout*<sup>2</sup> experience large swings, *Iout* no longer remains proportional to *Vout*<sup>1</sup> +*Vout*<sup>2</sup> due to the nonlinearity of the differential pairs. In fact, if *ID*<sup>1</sup> and *ID*<sup>2</sup> are expressed as *f (Vout*<sup>1</sup> − *VREF)* and *f (Vout*<sup>2</sup> − *VREF)*, respectively, we observe that *ID*<sup>1</sup> + *ID*<sup>2</sup> depends on the individual values of *Vout*<sup>1</sup> and *Vout*<sup>2</sup> unless *f ()* is a linear function. As a result, the reconstructed CM level does not remain constant in the presence of large differential output swings.

### **9.7.3 CM Feedback Techniques**

We now study techniques of comparing the measured CM level with a reference and returning the error to the op amp's bias network. In the circuit of Fig. 9.51, we employ a simple amplifier to detect the difference between *Vout,C M* and a reference voltage, *VREF*, applying the result to the NMOS current sources with negative feedback. If both *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, so does *VE* , thereby increasing the drain currents of *M*3–*M*<sup>4</sup> and lowering the output CM level. In other words, if the loop gain is large, the feedback network forces the CM level of *Vout*<sup>1</sup> and *Vout*<sup>2</sup> to approach *VREF*. Note that the feedback can be applied to the PMOS current sources as well. Also, the feedback may control only a fraction of the current to allow optimization of

Here is the image describtion:
```
The image depicts a differential amplifier circuit with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the circuit components and their connections:

1. **Transistors M1 and M2**: These are NMOS transistors configured as a differential pair. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a reference voltage (often ground in differential amplifiers). The sources of M1 and M2 are connected together and to a current source \( I_{SS} \) which is connected to ground.

2. **Current Source \( I_{SS} \)**: This provides a constant current to the differential pair M1 and M2.

3. **Transistors M3 and M4**: These are also NMOS transistors, forming a current mirror. The drain of M3 is connected to the drain of M1, and the drain of M4 is connected to the drain of M2. The gates of M3 and M4 are connected together and to the drain of M3, forming the current mirror configuration.

4. **Load Resistors \( R1 \) and \( R2 \)**: These resistors are connected to the drains of M1 and M2, respectively, and to the positive supply voltage \( V_{DD} \). The voltage across these resistors forms the differential output voltages \( V_{out1} \) and \( V_{out2} \).

5. **Common-Mode Feedback (CMFB) Circuit**: This part of the circuit includes an operational amplifier (op-amp) and transistors M3 and M4. The op-amp senses the common-mode voltage \( V_{out,CM} \) (which is the average of \( V_{out1} \) and \( V_{out2} \)) and compares it to a reference voltage \( V_{REF} \). The output of the op-amp \( V_E \) is fed back to the gates of M3 and M4 to adjust the current through the differential pair, thereby stabilizing the common-mode voltage.

6. **Power Supply \( V_{DD} \)**: This is the positive supply voltage for the circuit.

In summary, the circuit is a differential amplifier with a common-mode feedback mechanism to stabilize the common-mode output voltage. The differential pair (M1 and M2) amplifies the difference between the input voltage \( V_{in} \) and the reference voltage, while the CMFB circuit ensures that the common-mode voltage remains stable.
```

**Figure 9.51** Sensing and controlling output CM level.

the settling behavior. For example, each of *M*<sup>3</sup> and *M*<sup>4</sup> can be decomposed into two parallel devices, one biased at a constant current and the other driven by the error amplifier.

In a folded-cascode op amp, the CM feedback may control the tail current of the input differential pair. Illustrated in Fig. 9.52, this method increases the tail current if *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, lowering the drain currents of *M*5–*M*<sup>6</sup> and restoring the output CM level.

Here is the image describtion:
```
The image depicts a schematic diagram of an analog circuit, likely a differential amplifier with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the components and their connections:

1. **Transistors M1 and M2**: These are NMOS transistors configured as a differential pair. The input signal \( V_{in} \) is applied to the gate of M1, while the gate of M2 is connected to a common-mode voltage.

2. **Current Source**: Below the differential pair, there is a current source that provides a constant current to the sources of M1 and M2. This current source is typically implemented using another transistor or a current mirror.

3. **Operational Amplifier (Op-Amp)**: An op-amp is shown with its inverting input connected to a reference voltage \( V_{REF} \) and its non-inverting input connected to the common-mode output voltage \( V_{out,CM} \). The output of the op-amp is connected to the gate of the current source transistor, forming a feedback loop to control the common-mode voltage.

4. **Transistors M5 and M6**: These are PMOS transistors acting as active loads for the differential pair. They are connected in a current mirror configuration, with their sources connected to the positive supply voltage \( V_{DD} \).

5. **Resistors R1 and R2**: These resistors are connected in series between the drains of M5 and M6. The voltage at the node between R1 and R2 is the differential output voltage \( V_{out2} \), while the voltage at the drain of M5 is \( V_{out1} \).

6. **Common-Mode Feedback (CMFB) Circuit**: The op-amp and the current source transistor form the CMFB circuit. The purpose of this circuit is to stabilize the common-mode output voltage \( V_{out,CM} \) to a desired value, typically \( V_{REF} \).

7. **Power Supply**: The circuit is powered by a positive supply voltage \( V_{DD} \) and a ground connection.

In summary, this circuit is a differential amplifier with a common-mode feedback mechanism to stabilize the common-mode output voltage. The differential pair (M1 and M2) amplifies the input signal \( V_{in} \), and the active loads (M5 and M6) convert the differential current to a differential voltage. The CMFB circuit ensures that the common-mode voltage remains stable.
```

**Figure 9.52** Alternative method of controlling output CM level.

How do we perform comparison and feedback with the sensing scheme of Fig. 9.48? Here, the output CM voltage is directly converted to a resistance or a current, prohibiting comparison with a reference voltage. A simple feedback topology utilizing this technique is depicted in Fig. 9.53, where *Ron*7%*Ron*<sup>8</sup> adjusts the bias current of *M*<sup>5</sup> and *M*6. The output CM level sets *Ron*7%*Ron*<sup>8</sup> such that *ID*<sup>5</sup> and *ID*<sup>6</sup> exactly balance *ID*<sup>9</sup> and *ID*10, respectively. For example, if *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, *Ron*7||*Ron*<sup>8</sup> falls and the drain currents of *M*<sup>5</sup> and *M*<sup>6</sup> increase, pulling *Vout*<sup>1</sup> and *Vout*<sup>2</sup> down. Assuming that *ID*<sup>9</sup> = *ID*<sup>10</sup> = *ID*, we must have *Vb* − *VG S*<sup>5</sup> = 2*ID(Ron*7%*Ron*8*)*, and hence *Ron*7%*Ron*<sup>8</sup> = *(Vb* − *VG S*5*)/(*2*ID)*. From (9.49),

$$\frac{1}{\mu\_n C\_{ox} \left(\frac{W}{L}\right)\_{7,8} (V\_{out2} + V\_{out1} - 2V\_{TH})} = \frac{V\_b - V\_{GS}}{2I\_D} \tag{9.50}$$

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, specifically a differential amplifier with a current mirror load. Here is a detailed description of the circuit:

1. **Transistors:**
   - The circuit consists of eight MOSFET transistors labeled M5, M6, M7, M8, M9, and M10.
   - M5 and M6 are NMOS transistors forming the differential pair.
   - M7 and M8 are NMOS transistors forming the current mirror.
   - M9 and M10 are PMOS transistors forming the active load for the differential pair.

2. **Connections:**
   - The sources of M5 and M6 are connected together and to the drain of M7.
   - The sources of M7 and M8 are connected to the ground.
   - The gates of M7 and M8 are connected together and to the drain of M8, forming a current mirror.
   - The drain of M5 is connected to the drain of M9, and the drain of M6 is connected to the drain of M10.
   - The sources of M9 and M10 are connected to V_DD (the positive supply voltage).
   - The gates of M9 and M10 are connected together and to the drain of M9, forming another current mirror.

3. **Inputs and Outputs:**
   - The gates of M5 and M6 are the differential inputs, typically denoted as V_in1 and V_in2.
   - The drains of M5 and M6 are the differential outputs, denoted as V_out1 and V_out2.

4. **Biasing:**
   - The gate of M7 and M8 is connected to a bias voltage V_b, which sets the current through the current mirror and thus the tail current of the differential pair.

5. **Operation:**
   - The differential pair (M5 and M6) amplifies the difference between the input voltages (V_in1 and V_in2).
   - The current mirror formed by M7 and M8 ensures that the current through M5 and M6 is mirrored, providing a stable bias current.
   - The active load formed by M9 and M10 converts the differential current into a differential voltage at the outputs (V_out1 and V_out2).

This configuration is commonly used in analog circuits for its high gain and differential signal processing capabilities.
```

**Figure 9.53** CMFB using triode devices.

that is,

Razavi-3930640 book December 17, 201516:59 382

$$V\_{out1} + V\_{out2} = \frac{2I\_D}{\mu\_n C\_{ox} \left(\frac{W}{L}\right)\_{7.8}} \frac{1}{V\_b - V\_{GSS}} + 2V\_{TH} \tag{9.51}$$

The CM level can thus be obtained by noting that *VG S*<sup>5</sup> <sup>=</sup> <sup>√</sup>2*ID/*[*µnCox (W/L)*5] <sup>+</sup> *VT H*5*.*

The CMFB network of Fig. 9.53 suffers from several drawbacks. First, the value of the output CM level is a function of device parameters. Second, the voltage drop across *Ron*7%*Ron*<sup>8</sup> limits the output voltage swings. Third, to minimize this drop, *M*<sup>7</sup> and *M*<sup>8</sup> are usually quite wide devices, introducing substantial capacitance at the output. The second issue can be alleviated by applying the feedback to the tail current of the input differential pair (Fig. 9.54), but the other two remain.

Here is the image describtion:
```
The image depicts a schematic diagram of a CMOS (Complementary Metal-Oxide-Semiconductor) differential amplifier circuit. The circuit consists of multiple MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) devices arranged in a specific configuration to achieve differential amplification. Here is a detailed description of the components and their connections:

1. **Input Stage:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The gate of M1 is connected to the input signal \( V_{in} \), while the gate of M2 is connected to a reference voltage or another input signal.
   - The sources of M1 and M2 are connected together and to the drain of M9.

2. **Current Mirror and Biasing:**
   - **M7 and M8:** These are NMOS transistors forming a current mirror. The gate and drain of M7 are connected together and to the gate of M8. The source of M7 is connected to ground, and the source of M8 is also connected to ground.
   - **M9:** This NMOS transistor acts as a current source. Its gate is connected to a bias voltage \( V_b \), and its source is connected to the common source node of M1 and M2.

3. **Load Stage:**
   - **M3 and M4:** These are PMOS transistors forming a current mirror load. The gate and drain of M3 are connected together and to the gate of M4. The source of M3 is connected to \( V_{DD} \), and the source of M4 is also connected to \( V_{DD} \).
   - The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.

4. **Output Stage:**
   - **M5 and M6:** These are PMOS transistors. The drain of M5 is connected to the drain of M1, and the drain of M6 is connected to the drain of M2. The sources of M5 and M6 are connected to \( V_{DD} \).
   - **M10 and M11:** These are NMOS transistors. The drain of M10 is connected to the source of M12, and the drain of M11 is connected to the source of M13. The sources of M10 and M11 are connected to ground.
   - **M12 and M13:** These are NMOS transistors. The gate of M12 is connected to the drain of M5 (output node \( V_{out1} \)), and the gate of M13 is connected to the drain of M6 (output node \( V_{out2} \)).

5. **Output Nodes:**
   - The output voltages are taken from the drains of M5 and M6, labeled as \( V_{out1} \) and \( V_{out2} \), respectively.

The circuit operates as a differential amplifier, where the difference between the input signals at the gates of M1 and M2 is amplified and appears at the output nodes \( V_{out1} \) and \( V_{out2} \). The current mirrors formed by M3, M4, M7, and M8 help in maintaining constant current through the differential pair and provide high output impedance, which is essential for amplification.
```

**Figure 9.54** Alternative method of controlling output CM level.

How is *Vb* generated in Fig. 9.54? We note that *Vout,C M* is somewhat sensitive to the value of *Vb*: if *Vb* is higher than expected, the tail current of *M*<sup>1</sup> and *M*<sup>2</sup> increases and the output CM level falls. Since the feedback through *M*<sup>7</sup> and *M*<sup>8</sup> attempts to correct this error, the overall change in *Vout,C M* depends on the loop gain in the CMFB network. This is studied in the following example.

#### ▲**Example 9.18**

For the circuit of Fig. 9.54, determine the sensitivity of *Vout,C M* to *Vb*, i.e., *dVout,C M /dVb*.

### **Solution**

Setting *Vin* to zero and opening the loop at the gates of *M*<sup>7</sup> and *M*8, we simplify the circuit as shown in Fig. 9.55. Note that *gm*<sup>7</sup> and *gm*<sup>8</sup> must be calculated in the triode region: *gm*<sup>7</sup> = *gm*<sup>8</sup> = *µnCox (W/L)*7*,*<sup>8</sup>*VDS*<sup>7</sup>*,*8, where *VDS*<sup>7</sup>*,*<sup>8</sup> denotes the bias value of the drain-source voltage of *M*<sup>7</sup> and *M*8. Since *M*<sup>7</sup> and *M*<sup>8</sup> operate in the deep triode region, *VDS*<sup>7</sup>*,*<sup>8</sup> is typically less than 100 mV.

In a well-designed circuit, the loop gain must be relatively high. We therefore surmise that the closed-loop gain is approximately equal to 1*/*(, where ( represents the feedback factor. We write from Chapter 8:

$$
\beta = \frac{V\_2}{V\_1}|\_{I2=0} \tag{9.52}
$$

$$\mathbf{g} = -(\mathbf{g}\_{m7} + \mathbf{g}\_{m8})(R\_{on7} \| R\_{on8}) \tag{9.53}$$

Here is the image describtion:
```
The image depicts a schematic diagram of an analog circuit, likely a differential amplifier with a common-mode feedback network. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are likely NMOS transistors connected in a differential pair configuration. Their sources are connected together and to the drain of transistor M9.
   - **M5 and M6:** These are PMOS transistors, forming a current mirror load for the differential pair M1 and M2. Their sources are connected to a positive supply voltage.
   - **M9:** This NMOS transistor acts as a current source for the differential pair M1 and M2. Its gate is connected to a bias voltage \( V_b \).

2. **Resistors:**
   - **\( r_{o3} \parallel r_{o4} \):** This notation indicates the parallel combination of the output resistances of transistors M3 and M4, which are not explicitly shown but are implied to be part of the circuit.
   - **\( r_{o3} \parallel r_{o4} \):** This is connected to the drain of M5 and M6, indicating the load resistance seen by the differential pair.

3. **Feedback Network:**
   - The feedback network is enclosed in a dashed box and includes:
     - **\( R_{on7} \parallel R_{on8} \):** The parallel combination of the on-resistances of transistors M7 and M8.
     - **Current Source \( I_F \):** This is defined as \( I_F = (g_{m7} + g_{m8}) V_{out,CM} \), where \( g_{m7} \) and \( g_{m8} \) are the transconductances of transistors M7 and M8, respectively, and \( V_{out,CM} \) is the common-mode output voltage.
     - **\( V_{out,CM} \):** The common-mode output voltage is fed back into the network to control the current source \( I_F \).

4. **Output:**
   - The output common-mode voltage \( V_{out,CM} \) is taken from the node where the drains of M5 and M6 are connected.
   - The output impedance is given by \( \frac{g_{m12} r_{o12} r_{o10}}{2} \), where \( g_{m12} \), \( r_{o12} \), and \( r_{o10} \) are parameters related to other transistors in the circuit, likely part of the feedback network or additional stages not fully shown in the diagram.

5. **Connections:**
   - The sources of M1 and M2 are connected to the drain of M9.
   - The gates of M1 and M2 are connected to differential input signals (not shown in the diagram).
   - The drains of M1 and M2 are connected to the drains of M5 and M6, respectively.
   - The feedback network is connected to the common-mode output voltage \( V_{out,CM} \) and provides a feedback current \( I_F \) to stabilize the common-mode voltage.

Overall, the circuit appears to be a differential amplifier with a common-mode feedback mechanism to ensure stable operation and control of the common-mode output voltage.
```

**Figure 9.55**

$$=-2\mu\_n C\_{ox} \left(\frac{W}{L}\right)\_{7,8} V\_{DS7,8} \cdot \frac{1}{2\mu\_n C\_{ox} (W/L)\_{7,8} (V\_{GS7,8} - V\_{TH7,8})}\tag{9.54}$$

$$\dot{\omega} = -\frac{V\_{DS7,8}}{V\_{GS7,8} - V\_{TH7,8}}\tag{9.55}$$

where *VG S*<sup>7</sup>*,*<sup>8</sup> − *VT H*<sup>7</sup>*,*<sup>8</sup> denotes the overdrive voltage of *M*<sup>7</sup> and *M*8. Thus,

$$
\left| \frac{dV\_{out,CM}}{dV\_b} \right|\_{closed} \approx \frac{V\_{GS7,8} - V\_{TH7,8}}{V\_{DS7,8}} \tag{9.56}
$$

This is an important result. Since *VG S*7*,*<sup>8</sup> (i.e., the output CM level) is typically in the vicinity of *VDD/*2, the above equation suggests that *VDS*<sup>7</sup>*,*<sup>8</sup> must be maximized to minimize this sensitivity, but at the cost of the loop gain.

We now introduce a modification to the circuit of Fig. 9.54 that both makes the output level relatively independent of device parameters and lowers the sensitivity to the value of *Vb*. Illustrated in Fig. 9.56(a), the idea is to define *Vb* by a current mirror arrangement such that *ID*<sup>9</sup> "tracks" *I*<sup>1</sup> and *VREF*. For simplicity, suppose *(W/L)*<sup>15</sup> = *(W/L)*<sup>9</sup> and *(W/L)*<sup>16</sup> = *(W/L)*7+*(W/L)*8. Thus, *ID*<sup>9</sup> = *I*<sup>1</sup> only if *Vout,C M* = *VREF*. In other words, as with Fig. 9.52, the circuit produces an output CM level equal to a reference but it requires no resistors in sensing *Vout,C M* . The overall design can be simplified as shown in Fig. 9.56(b).

In practice, since *VDS*<sup>15</sup> =, *VDS*9, channel-length modulation results in a finite error. Figure 9.57 depicts a modification that suppresses this error. Here, transistors *M*<sup>17</sup> and *M*<sup>18</sup> reproduce at the drain of *M*<sup>15</sup> a voltage equal to the source voltage of *M*<sup>1</sup> and *M*2, ensuring that *VDS*<sup>15</sup> = *VDS*9.

To arrive at another CM feedback topology, let us consider the simple differential pair shown in Fig. 9.58(a). Here, the output CM level, *VDD* − |*VG S*<sup>3</sup>*,*<sup>4</sup>|, is relatively well defined, but the voltage gain is quite low. To increase the differential gain, the PMOS devices must operate as current sources for *differential* signals. We therefore modify the circuit as depicted in Fig. 9.58(b), where for differential changes at *Vout*<sup>1</sup> and *Vout*2, node *P* is a virtual ground and the gain can be expressed as *gm*<sup>1</sup>*,*<sup>2</sup>*(rO*<sup>1</sup>*,*<sup>2</sup>%*rO*<sup>3</sup>*,*<sup>4</sup>%*RF )*. We preferably choose *RF* " *rO*<sup>1</sup>*,*<sup>2</sup>||*rO*<sup>3</sup>*,*4. For common-mode levels, on the other hand, *M*<sup>3</sup> and *M*<sup>4</sup> operate as diode-connected devices. The circuit proves useful in low-gain applications.

▲

Here is the image describtion:
```
The image depicts a complex CMOS (Complementary Metal-Oxide-Semiconductor) analog circuit, likely an operational amplifier or a similar analog signal processing circuit. Here is a detailed description of the circuit:

1. **Power Supply and Ground:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top and is grounded at the bottom.

2. **Current Source and Reference Voltage:**
   - A current source \( I_1 \) is connected to \( V_{DD} \) and supplies current to the circuit.
   - A reference voltage \( V_{REF} \) is provided at the bottom left, which is connected to the gate of transistor \( M_{16} \).

3. **Transistors:**
   - The circuit consists of 16 MOSFET transistors labeled \( M_1 \) to \( M_{16} \).
   - Transistors \( M_{15} \) and \( M_{16} \) form a current mirror with \( M_{16} \) receiving the reference voltage \( V_{REF} \) and \( M_{15} \) mirroring the current to the rest of the circuit.
   - Transistors \( M_1 \) and \( M_2 \) form a differential pair with their sources connected together and to the drain of \( M_9 \).
   - The gates of \( M_1 \) and \( M_2 \) are the input terminals \( V_{in} \) and a bias voltage \( V_b \), respectively.
   - Transistors \( M_3 \) and \( M_4 \) form a current mirror, as do \( M_5 \) and \( M_6 \).
   - Transistors \( M_7 \) and \( M_8 \) are connected in a diode configuration with their gates and drains shorted to ground.
   - Transistors \( M_{10} \) and \( M_{11} \) are connected in a similar configuration to \( M_7 \) and \( M_8 \).
   - Transistors \( M_{12} \) and \( M_{13} \) form another current mirror.

4. **Output Nodes:**
   - The circuit has two output nodes labeled \( V_{out1} \) and \( V_{out2} \).
   - \( V_{out1} \) is taken from the drain of \( M_6 \) and \( V_{out2} \) from the drain of \( M_5 \).

5. **Connections:**
   - The source of \( M_9 \) is connected to the common source of \( M_1 \) and \( M_2 \).
   - The drain of \( M_9 \) is connected to the sources of \( M_7 \) and \( M_8 \).
   - The gates of \( M_7 \) and \( M_8 \) are connected to the drain of \( M_9 \).
   - The drain of \( M_1 \) is connected to the gate of \( M_4 \) and the drain of \( M_2 \) to the gate of \( M_3 \).
   - The sources of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The drain of \( M_4 \) is connected to the gate of \( M_6 \) and the drain of \( M_3 \) to the gate of \( M_5 \).
   - The sources of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_{12} \) and \( M_{13} \), respectively.
   - The sources of \( M_{12} \) and \( M_{13} \) are connected to the drains of \( M_{10} \) and \( M_{11} \), respectively.

This circuit likely functions as a differential amplifier with current mirrors to provide biasing and gain stages. The exact function would depend on the specific design parameters and the intended application.
```

$$\left(\mathbb{B}\right)$$

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with a current mirror load. The circuit is composed of multiple MOSFET transistors arranged in a specific configuration to achieve amplification and differential output. Here is a detailed description of the components and their connections:

1. **Current Source**: On the left side of the diagram, there is a current source symbol, which provides a constant current to the circuit.

2. **Transistors M15 and M16**: These transistors are connected in a diode configuration with their gates and drains tied together. They are connected to the current source and ground, and they generate a reference voltage \( V_{REF} \).

3. **Transistors M1 and M2**: These are the input transistors of the differential pair. The gates of M1 and M2 are the input terminals \( V_{in} \). The sources of M1 and M2 are connected together and to the drain of transistor M9.

4. **Transistor M9**: This transistor acts as a current source for the differential pair M1 and M2. Its gate is connected to a bias voltage \( V_b \), and its source is connected to ground.

5. **Transistors M7 and M8**: These transistors form a current mirror with M9. The gates of M7 and M8 are connected to the gate of M9, and their sources are connected to ground. The drains of M7 and M8 are connected to the sources of M1 and M2, respectively.

6. **Transistors M3 and M4**: These transistors form a current mirror load for the differential pair. The gate of M3 is connected to the gate and drain of M4. The source of M3 is connected to \( V_{DD} \), and the drain of M3 is connected to the drain of M1.

7. **Transistors M5 and M6**: These transistors form another current mirror load. The gate of M5 is connected to the gate and drain of M6. The source of M5 is connected to \( V_{DD} \), and the drain of M5 is connected to the drain of M2.

8. **Output Nodes**: The drains of M3 and M5 are the output nodes of the differential amplifier, labeled as \( V_{out1} \) and \( V_{out2} \), respectively.

9. **Transistors M10, M11, M12, and M13**: These transistors form additional current mirrors. The gates of M10 and M11 are connected to the gate and drain of M12 and M13, respectively. The sources of M10 and M11 are connected to ground, and their drains are connected to the drains of M3 and M5, respectively.

Overall, this circuit is designed to amplify the difference between the input signals \( V_{in1} \) and \( V_{in2} \) and provide differential output signals \( V_{out1} \) and \( V_{out2} \). The current mirrors formed by M3, M4, M5, M6, M10, M11, M12, and M13 help to ensure that the currents through the differential pair are mirrored accurately, providing high gain and proper operation of the amplifier.
```

**Figure 9.56** Modification of CMFB for more accurate definition of output CM level.

Here is the image describtion:
```
The image depicts a complex circuit diagram, likely representing a differential amplifier or a similar analog circuit. Here is a detailed description of the components and their connections:

1. **Current Source**: At the top left, there is a current source symbol, which provides a constant current to the circuit.

2. **Transistors**: The circuit consists of multiple MOSFET transistors labeled M1 through M18. These transistors are arranged in various configurations to achieve the desired amplification and signal processing.

3. **Differential Pair**: Transistors M1 and M2 form a differential pair, with their gates connected to the input signal \( V_{in} \). This pair is responsible for amplifying the difference between the two input signals.

4. **Current Mirrors**: Several current mirrors are present in the circuit. For example, transistors M15 and M16 form a current mirror, which is used to replicate the current from one branch of the circuit to another. Similarly, M7 and M8 form another current mirror.

5. **Biasing Network**: Transistors M15, M16, M7, and M8 are part of the biasing network, which sets the operating point of the differential pair. The voltage \( V_b \) is used to bias the gates of M9 and M10.

6. **Load Transistors**: Transistors M3, M4, M5, and M6 act as load transistors for the differential pair. They are connected to the power supply \( V_{DD} \) and provide the necessary load resistance for proper operation.

7. **Output Nodes**: The circuit has two output nodes, \( V_{out1} \) and \( V_{out2} \), which are taken from the drains of M6 and M5, respectively. These outputs represent the amplified differential signal.

8. **Additional Transistors**: Transistors M9, M10, M11, M12, M13, M17, and M18 are part of the circuit's additional stages and current mirrors, which further process the signal and ensure proper operation.

9. **Reference Voltage**: A reference voltage \( V_{REF} \) is applied to the gate of M15, which helps in setting the bias current for the differential pair.

10. **Power Supply**: The circuit is powered by a supply voltage \( V_{DD} \), which is connected to the drains of the load transistors and other parts of the circuit.

Overall, the circuit is a sophisticated analog design, likely used for high-precision amplification and signal processing in applications such as operational amplifiers, analog-to-digital converters, or other mixed-signal integrated circuits.
```

**Figure 9.57** Modification to suppress error due to channel-length modulation.

Here is the image describtion:
```
The image shows three different configurations of a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Each configuration is labeled (a), (b), and (c).

### Configuration (a):
- **Transistors**: There are four MOSFETs labeled M1, M2, M3, and M4.
  - M1 and M2 are NMOS transistors.
  - M3 and M4 are PMOS transistors.
- **Power Supply**: The circuit is powered by a voltage source labeled V_DD.
- **Current Source**: There is a current source labeled I_SS connected to the source terminals of M1 and M2, which is grounded.
- **Input and Output**:
  - The input voltage V_in is applied to the gate terminals of M1 and M2.
  - The output voltage V_out is taken from the common drain connection of M1 and M2.
- **Operation**: This is a basic differential amplifier where M1 and M2 form the differential pair, and M3 and M4 act as active loads.

### Configuration (b):
- **Transistors**: Similar to configuration (a), it has four MOSFETs labeled M1, M2, M3, and M4.
  - M1 and M2 are NMOS transistors.
  - M3 and M4 are PMOS transistors.
- **Power Supply**: The circuit is powered by a voltage source labeled V_DD.
- **Current Source**: There is a current source labeled I_SS connected to the source terminals of M1 and M2, which is grounded.
- **Input and Output**:
  - The input voltage V_in is applied to the gate terminals of M1 and M2.
  - The output voltage V_out is taken from the common drain connection of M1 and M2.
- **Feedback Resistors**: There are two feedback resistors labeled R_F connected between the drain terminals of M1 and M2 and the gate terminals of M3 and M4.
- **Operation**: This configuration includes feedback resistors to improve the linearity and stability of the differential amplifier.

### Configuration (c):
- **Transistors**: Similar to configurations (a) and (b), it has four MOSFETs labeled M1, M2, M3, and M4.
  - M1 and M2 are NMOS transistors.
  - M3 and M4 are PMOS transistors.
- **Power Supply**: The circuit is powered by a voltage source labeled V_DD.
- **Current Source**: There is a current source labeled I_1 connected to the source terminals of M1 and M2, which is grounded.
- **Input and Output**:
  - The input voltage V_in is applied to the gate terminals of M1 and M2.
  - The output voltage V_out is taken from the common drain connection of M1 and M2.
- **Feedback Resistors**: There are two feedback resistors labeled R_F connected between the drain terminals of M1 and M2 and the gate terminals of M3 and M4.
- **Additional Transistor**: There is an additional PMOS transistor labeled P connected between the drain terminals of M1 and M2 and the feedback resistors R_F.
- **Operation**: This configuration includes an additional PMOS transistor P and feedback resistors to further enhance the performance of the differential amplifier.

In summary, the image shows three variations of a differential amplifier circuit with increasing complexity and additional components to improve performance characteristics such as linearity and stability.
```

**Figure 9.58** (a) Differential pair using diode-connected loads, (b) resistive CMFB, and (c) modification to allow low-voltage operation.

#### ▲**Example 9.19**

Determine the maximum allowable output swings in Fig. 9.58(b).

### **Solution**

Each output can fall to two overdrive voltages above ground if *Vin,C M* is chosen to place *ISS* at the edge of the triode region. The highest level allowed at the output is equal to the output CM level plus |*VT H*<sup>3</sup>*,*4|, i.e., *VDD* − |*VG S*<sup>3</sup>*,*4|+|*VT H*<sup>3</sup>*,*4| = *VDD* − |*VG S*<sup>3</sup>*,*<sup>4</sup> − *VT H*<sup>3</sup>*,*4|. ▲

In some applications, we wish to operate the circuit of Fig. 9.58(b) with a low supply voltage, but for small signals. This stage dictates a minimum *VDD* of |*VG S*<sup>3</sup>*,*4| plus two overdrive voltages. We modify the circuit by drawing a small current from the two resistors and PMOS devices as illustrated in Fig. 9.58(c). Here, *VP* is still equal to *VDD* − |*VG S*<sup>3</sup>*,*4|, but the drain voltages are *higher* than *VP* by an amount equal to *I*1*RF /*2. For example, if *I*1*RF /*2 = |*VT H*<sup>3</sup>*,*4|, then the PMOS devices operate at the edge of saturation, allowing a minimum *VDD* of three overdrive voltages.

#### ▲**Example 9.20**

Facing voltage headroom limitations, a student constructs the circuit shown in Fig. 9.59(a), where the tail current source is replaced by two triode devices that sense the output CM level, *Vout,C M* . Determine the small-signal gain from the input CM level to the output CM level.

Here is the image describtion:
```
The image consists of three subfigures (a), (b), and (c), each depicting different stages or representations of a differential amplifier circuit.

### Subfigure (a):
This is a schematic diagram of a differential amplifier with active loads. The circuit includes the following components:
- **Transistors M1 and M2**: These are the input differential pair transistors.
- **Transistors M3 and M4**: These are the active load transistors.
- **Transistors M5 and M6**: These are the tail current source transistors.
- **Current Source**: Provides a constant current to the tail transistors M5 and M6.
- **V_DD**: The positive supply voltage.
- **Ground**: The common reference point for the circuit.

The differential input is applied to the gates of M1 and M2, and the differential output is taken from the drains of M3 and M4.

### Subfigure (b):
This is a simplified small-signal model of the differential amplifier focusing on the common-mode analysis. The components are:
- **V_DD**: The positive supply voltage.
- **Transistors M3 + M4**: Representing the combined effect of the active load transistors.
- **V_out,CM**: The common-mode output voltage.
- **Vin,CM**: The common-mode input voltage.
- **Transistors M1 + M2**: Representing the combined effect of the input differential pair transistors.
- **Transistors M5 + M6**: Representing the combined effect of the tail current source transistors.
- **P**: A node in the circuit.

### Subfigure (c):
This is an equivalent small-signal model of the differential amplifier for common-mode analysis. The components are:
- **r_o3,4 / 2**: Represents the output resistance of the active load transistors divided by 2.
- **Vin,CM**: The common-mode input voltage.
- **Transistors M1 + M2**: Representing the combined effect of the input differential pair transistors.
- **P**: A node in the circuit.
- **R_tail**: The resistance of the tail current source.
- **g_m,tail V_out,CM**: Represents the transconductance of the tail current source multiplied by the common-mode output voltage.
- **V_out,CM**: The common-mode output voltage.

The dashed box in subfigure (c) encloses the tail current source and its associated components, indicating the common-mode feedback mechanism.

Overall, the image illustrates the progression from a detailed transistor-level schematic to a simplified small-signal model for analyzing the common-mode behavior of a differential amplifier.
```

**Figure 9.59**

### **Solution**

Razavi-3930640 book December 17, 201516:59 386

If the circuit is symmetric, the output nodes can be shorted, leading to the topology in Fig. 9.59(b).6 To model the composite transistor *M*<sup>5</sup> + *M*6, we define a transconductance *gm,tail* = *gm*<sup>5</sup> + *gm*<sup>6</sup> = 2*µnCox (W/L)*5*,*6*VP* , where *VP* is the dc voltage at node *P*.We also approximate their total channel resistance by *Rtail* = [2*µnCox (W/L)*5*,*6*(Vout,C M* − *VT H*<sup>5</sup>*,*6*)*] <sup>−</sup>1. The circuit therefore reduces to that shown in Fig. 9.59(c).

Assuming for simplicity that λ = γ = 0 for *M*<sup>1</sup> and *M*2, we express the small-signal current drawn by *M*<sup>1</sup> + *M*<sup>2</sup> as −*Vout,C M /(rO*<sup>3</sup>*,*4*/*2*)*. This current translates to a gate-source voltage of −*Vout/(*2*gm*<sup>1</sup>*,*<sup>2</sup>*rO*<sup>3</sup>*,*4*/*2*)* = −*Vout/(gm*<sup>1</sup>*,*<sup>2</sup>*rO*<sup>3</sup>*,*4*)*, yielding a voltage of *Vin,C M* + *Vout/(gm*<sup>1</sup>*,*<sup>2</sup>*rO*<sup>3</sup>*,*4*)* at node *P* and hence a current of [*Vin,C M* + *Vout/(gm*<sup>1</sup>*,*<sup>2</sup>*rO*<sup>3</sup>*,*4*)*]*/Rtail* through *Rtail* . Since this current and *gm,tailVout,C M* must add up to −*Vout,C M /(rO*<sup>3</sup>*,*4*/*2*)*, we obtain

$$\frac{V\_{out,CM}}{V\_{in,CM}} = -\frac{1}{\frac{2R\_{tail}}{r\_{O3,4}} + g\_{m,tail}R\_{tail} + (g\_{m1,2}r\_{O3,4})^{-1}}\tag{9.57}$$

It is important to note that all of the three terms in the denominator are less than one (why?), revealing that *Vout,C M /Vin,C M* is roughly around unity. That is, an error in the input CM level reaches the output without significant attenuation. This observation suggests a poor CMRR; the reader is encouraged to assume a *gm* mismatch between *M*<sup>1</sup> and *M*<sup>2</sup> and compute the CMRR as outlined in Chapter 4. ▲

### **9.7.4 CMFB in Two-Stage Op Amps**

Offering nearly rail-to-rail output swings, two-stage op amps find wider application than other topologies in today's designs. However, such op amps require more complex common-mode feedback. To understand the issues, we consider three different CMFB methods in the context of the simple circuit shown in Fig. 9.60(a).

First, suppose the CM level of *Vout*<sup>1</sup> and *Vout*<sup>2</sup> is sensed and the result is used to control only *Vb*2; i.e., the second stage incorporates CMFB, but not the first stage [Fig. 9.60(b)]. In this case, no mechanism exists that controls the CM level at *X* and *Y* . For example, if *ISS* happens to be less than the sum of the currents that *M*<sup>3</sup> and *M*<sup>4</sup> wish to draw, then *VX* and *VY* rise, driving these transistors into the triode region so that *ID*<sup>3</sup> + *ID*<sup>4</sup> eventually becomes equal to *ISS*. This effect also reduces |*VG S*<sup>5</sup>*,*6|, establishing in *M*5–*M*<sup>8</sup> a current that may be well below the nominal value. This CMFB method is therefore not desired.

Second, we still sense the CM level *Vout*<sup>1</sup> and *Vout*<sup>2</sup> but return the result to the first stage, e.g., to *ISS* [Fig. 9.60(c)]. Suppose, for example, that *Vout*<sup>1</sup> and *Vout*<sup>2</sup> begin too high. Then, the error amplifier, *Ae*, reduces *ISS*, allowing *VX* and *VY* to rise, |*ID*5| and |*ID*6| to fall, and *Vout*<sup>1</sup> and *Vout*<sup>2</sup> to go down. It is interesting to note that here *M*<sup>5</sup> and *M*<sup>6</sup> in fact sense the CM level at *X* and *Y* , helping the global loop control both stages' CM level. (If *M*<sup>3</sup> and *M*<sup>4</sup> had a tail current, as in a regular differential pair, this property would vanish and the CMFB loop would fail.)

While used in some designs, the second technique suffers from a critical drawback. Let us draw the equivalent circuit for common-mode levels (Fig. 9.61). How many poles does the CM feedback loop contain? We count one pole at *X* or *Y* , one at the main output, and at least one associated with the error amplifier. Moreover, since *RC M* is so large as not to load the second stage, it forms with the input capacitance of *Ae* a pole that may not be negligible. Thus, even if the pole at the source of *M*<sup>1</sup> and *M*<sup>2</sup> is discounted, the CMFB loop still contains three or four poles. As explained in Chapter 10, this many poles make it difficult for the loop be stable.

In order to avoid stability issues, we can employ two separate CMFB loops for the first and second stages of the op amp. Figure 9.62 illustrates a simple example [7], where, in a manner similar to Fig. 9.58(b),

<sup>6</sup>We use the notation *Mj* <sup>+</sup> *Mj*+<sup>1</sup> to denote the parallel combination of *Mj* and *Mj*+1.

Here is the image describtion:
```
The image consists of three subfigures (a), (b), and (c), each depicting different configurations of a differential amplifier circuit with common-mode feedback (CMFB) mechanisms.

### Subfigure (a):
This subfigure shows a basic differential amplifier circuit without explicit common-mode feedback. The circuit includes the following components:
- **Transistors M1 and M2**: These are the input differential pair transistors. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a reference voltage.
- **Transistors M3 and M4**: These are the load transistors for the differential pair, forming a current mirror.
- **Transistors M5 and M6**: These transistors are connected to the drains of M3 and M4, respectively, and provide the differential output voltages \( V_{out1} \) and \( V_{out2} \).
- **Transistors M7 and M8**: These are the tail current sources for the differential pair, connected to the common source node of M1 and M2.
- **Current Source \( I_{SS} \)**: This provides the bias current for the differential pair.
- **Bias Voltages \( V_{b1} \) and \( V_{b2} \)**: These are the bias voltages for the transistors M3, M4, M5, M6, M7, and M8.

### Subfigure (b):
This subfigure introduces a common-mode feedback (CMFB) mechanism to the differential amplifier. The additional components include:
- **CM Sense Block**: This block senses the common-mode voltage of the differential outputs \( V_{out1} \) and \( V_{out2} \).
- **Error Amplifier \( A_e \)**: This amplifier compares the sensed common-mode voltage with a reference voltage \( V_{REF} \) and generates a feedback signal to control the common-mode voltage.

### Subfigure (c):
This subfigure integrates the CMFB mechanism into the differential amplifier circuit. The components are similar to those in subfigure (a) with the addition of the CMFB components from subfigure (b):
- **CM Sense Block**: Senses the common-mode voltage of \( V_{out1} \) and \( V_{out2} \).
- **Error Amplifier \( A_e \)**: Compares the sensed common-mode voltage with \( V_{REF} \) and adjusts the biasing of the tail current source \( I_{SS} \) to maintain the desired common-mode voltage.

In summary, the image illustrates the evolution of a differential amplifier circuit from a basic configuration (subfigure a) to one with an explicit common-mode feedback mechanism (subfigure c) to stabilize the common-mode output voltage.
```

**Figure 9.60** (a) Two-stage op amp, (b) CMFB around second stage, and (c) CMFB from second stage to first stage.

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with common-mode feedback. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors connected in a differential pair configuration. Their sources are connected together and to a current source (represented by a circle with an arrow pointing upwards).
   - **M3 and M4:** These are PMOS transistors connected as the load for the differential pair M1 and M2. Their sources are connected to the supply voltage \( V_{DD} \), and their drains are connected to the drains of M1 and M2, respectively.
   - **M5 and M6:** These are PMOS transistors connected in a current mirror configuration. Their sources are connected to \( V_{DD} \), and their gates are connected together. The drain of M5 is connected to the drain of M3, and the drain of M6 is connected to the drain of M4.
   - **M7 and M8:** These are NMOS transistors connected in a current mirror configuration. Their sources are connected to ground, and their gates are connected together. The drain of M7 is connected to the drain of M5, and the drain of M8 is connected to the drain of M6.

2. **Nodes:**
   - **X and Y:** These are the input nodes of the differential amplifier, connected to the gates of M1 and M2, respectively.
   - **\( V_{out1} \) and \( V_{out2} \):** These are the output nodes of the differential amplifier, taken from the drains of M3 and M4, respectively.

3. **Common-Mode Feedback (CMFB) Circuit:**
   - **Error Amplifier (A_e):** This is an operational amplifier used for common-mode feedback. It has a non-inverting input connected to a reference voltage \( V_{REF} \) and an inverting input connected to a common-mode sense circuit.
   - **\( R_{CM} \):** This is a resistor used in the common-mode sense circuit to sense the common-mode voltage of the outputs \( V_{out1} \) and \( V_{out2} \).
   - The output of the error amplifier is connected to the current source that biases the differential pair M1 and M2.

4. **Power Supply:**
   - **\( V_{DD} \):** This is the positive supply voltage connected to the sources of the PMOS transistors M3, M4, M5, and M6.
   - **Ground:** The negative supply voltage (ground) is connected to the sources of the NMOS transistors M1, M2, M7, and M8.

The circuit operates as follows:
- The differential pair M1 and M2 amplifies the difference between the input signals at nodes X and Y.
- The PMOS transistors M3 and M4 act as active loads for the differential pair, converting the differential current into a differential voltage at nodes \( V_{out1} \) and \( V_{out2} \).
- The current mirrors formed by M5, M6, M7, and M8 ensure that the currents through the differential pair are mirrored and balanced.
- The common-mode feedback circuit senses the common-mode voltage of the outputs and adjusts the bias current through the differential pair to maintain a stable common-mode output voltage.

This configuration is commonly used in analog integrated circuits to achieve high gain and common-mode rejection.
```

**Figure 9.61** Equivalent CMFB loop to determine the number of poles.

*R*<sup>1</sup> and *R*<sup>2</sup> provide CMFB for the first stage and *R*<sup>3</sup> and *R*<sup>4</sup> for the second. Interestingly, all of the drain currents in this topology are copied from *ISS*. Assuming a symmetric circuit, we recognize that (1) resistors *R*<sup>1</sup> and *R*<sup>2</sup> adjust *VG S*<sup>3</sup>*,*<sup>4</sup> until |*ID*3|=|*ID*4| = *ISS/*2; (2) since *VG S*<sup>3</sup>*,*<sup>4</sup> = *VG S*<sup>5</sup>*,*6, *M*<sup>5</sup> and *M*<sup>6</sup> copy their currents from *M*<sup>3</sup> and *M*<sup>4</sup> as in a current mirror; and (3) resistors *R*<sup>3</sup> and *R*<sup>4</sup> adjust *VG S*<sup>7</sup>*,*<sup>8</sup> until *ID*<sup>7</sup> = *ID*<sup>8</sup> = |*ID*5|=|*ID*6|. The differential voltage gain is equal to *gm*1*(rO*1||*rO*3||*R*1*)gm*5*(rO*5||*rO*7||*R*3*)*.

Another CMFB technique for two-stage op amps is described in Chapter 11.

▲

Here is the image describtion:
```
The image depicts a CMOS (Complementary Metal-Oxide-Semiconductor) differential amplifier circuit with active loads. Here is a detailed description of the circuit components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source \( V_{DD} \) at the top.

2. **Transistors:**
   - The circuit consists of eight MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are NMOS transistors forming the differential pair.
   - \( M_3 \) and \( M_4 \) are PMOS transistors acting as active loads for the differential pair.
   - \( M_5 \) and \( M_6 \) are PMOS transistors connected to the drains of \( M_3 \) and \( M_4 \) respectively, providing additional current paths.
   - \( M_7 \) and \( M_8 \) are NMOS transistors connected to the outputs \( V_{out1} \) and \( V_{out2} \) respectively, providing current sinks.

3. **Resistors:**
   - \( R_1 \) and \( R_2 \) are resistors connected between the drains of \( M_1 \) and \( M_2 \) and the sources of \( M_3 \) and \( M_4 \) respectively.
   - \( R_3 \) and \( R_4 \) are resistors connected between the sources of \( M_7 \) and \( M_8 \) and ground.

4. **Current Source:**
   - A current source \( I_{SS} \) is connected to the common source node of \( M_1 \) and \( M_2 \) and ground, providing a constant current.

5. **Nodes and Connections:**
   - The input signal \( V_{in} \) is applied to the gate of \( M_1 \).
   - The node \( X \) is the drain of \( M_1 \) and the source of \( M_3 \), connected through \( R_1 \).
   - The node \( Y \) is the drain of \( M_2 \) and the source of \( M_4 \), connected through \( R_2 \).
   - The output \( V_{out1} \) is taken from the drain of \( M_5 \).
   - The output \( V_{out2} \) is taken from the drain of \( M_6 \).
   - The node \( Q \) is the common source node of \( M_7 \) and \( M_8 \), connected to ground through \( R_3 \) and \( R_4 \).

This circuit is a differential amplifier with active loads, designed to amplify the difference between the input signals applied to the gates of \( M_1 \) and \( M_2 \). The active loads (PMOS transistors \( M_3 \) and \( M_4 \)) improve the gain and performance of the amplifier. The resistors \( R_1 \) and \( R_2 \) help in setting the operating point and stabilizing the circuit. The current source \( I_{SS} \) ensures a constant current through the differential pair, which is crucial for the proper functioning of the differential amplifier.
```

**Q Figure 9.62** Simple CMFB loops around each stage.

#### ▲**Example 9.21**

Razavi-3930640 book December 17, 201516:59 388

A student delighted by the simplicity of the op amp in Fig. 9.62 designs the circuit for a given power budget, but realizes that the output CM level is inevitably well below *VDD/*2, and hence the output swings are limited. Explain why and devise a solution.

### **Solution**

The output CM level is equal to *VG*7*,*<sup>8</sup> (recall that *R*<sup>3</sup> and *R*<sup>4</sup> carry no current in the absence of signals). Since *M*<sup>7</sup> and *M*<sup>8</sup> are chosen wide enough for a small overdrive voltage, *VG S*<sup>7</sup>*,*<sup>8</sup> is only slightly greater than one threshold voltage and far from *VDD/*2.

This issue can be resolved by drawing a small current from node *Q* (Fig. 9.63). Now, *R*<sup>3</sup> and *R*<sup>4</sup> sustain a drop of *R*<sup>3</sup> *IQ/*2 (= *R*<sup>4</sup> *IQ/*2), producing an upward shift of the same amount in the output CM level [7]. Thus, *IQ* can be chosen to create an output CM level around *VDD/*2.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring a differential pair of MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). The circuit includes the following components and connections:

1. **MOSFETs (M7 and M8)**: There are two MOSFETs labeled M7 and M8. The source terminals of both MOSFETs are connected to the ground.

2. **Resistors (R3 and R4)**: There are two resistors labeled R3 and R4. Resistor R3 is connected between the drain of M7 and a node labeled Q. Similarly, resistor R4 is connected between the drain of M8 and the same node Q.

3. **Current Source (IQ)**: There is a current source labeled IQ connected to the node Q. The other terminal of the current source is connected to the ground.

4. **Output Nodes (Vout1 and Vout2)**: The circuit has two output nodes labeled Vout1 and Vout2. Vout1 is connected to the drain of M7, and Vout2 is connected to the drain of M8.

5. **Connections**: The gate of M7 is connected to the left side of the circuit, and the gate of M8 is connected to the right side of the circuit. The node Q is a common point where the current source IQ, resistors R3 and R4, and the sources of M7 and M8 are connected.

The circuit appears to be a differential amplifier, where the differential input is applied to the gates of M7 and M8, and the differential output is taken from the drains of M7 and M8 (Vout1 and Vout2). The current source IQ provides a constant current, which is split between the two branches of the circuit.
```

If the first stage incorporates a telescopic cascode to achieve a high gain, then the CMFB loops can be realized as shown in Fig. 9.64. While not precise, the CM sensing of *X* and *Y* avoids loading the high impedances at these nodes, thereby maintaining a high voltage gain.

# **9.8 Input Range Limitations**

The op amp circuits studied thus far have evolved to achieve large differential output swings. While the differential input swings are usually much smaller (by a factor equal to the open-loop gain), the input *common-mode* level may need to vary over a wide range in some applications. For example, consider the simple unity-gain buffer shown in Fig. 9.65, where the input swing is nearly equal to the output swing. Interestingly, in this case the voltage swings are limited by the input differential pair rather than the output

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit, which is a common configuration in analog electronics. Here is a detailed description of the circuit:

1. **Power Supply**: The circuit is powered by a voltage source labeled \( V_{DD} \) at the top of the diagram.

2. **Transistors**: The circuit consists of multiple MOSFET transistors arranged in a specific configuration:
   - At the top, there are two pairs of transistors connected in a cascode configuration. Each pair consists of two transistors stacked on top of each other.
   - The middle section has two transistors labeled X and Y, which are the main differential pair. These transistors receive the differential input signals.
   - Below the differential pair, there are two more transistors connected to the sources of the differential pair transistors. These transistors are part of the current mirror configuration.
   - At the bottom, there is a current source connected to the common source of the differential pair transistors.

3. **Resistors**: There are two resistors connected to the sources of the transistors in the middle section. These resistors are part of the biasing network and help set the operating point of the transistors.

4. **Capacitors**: The circuit includes several capacitors, which are used for coupling and bypassing purposes. These capacitors help in stabilizing the circuit and improving its frequency response.

5. **Output Nodes**: The circuit has two output nodes labeled \( V_{out1} \) and \( V_{out2} \). These nodes provide the differential output signals of the amplifier.

6. **Current Source**: At the bottom of the circuit, there is a current source symbol, which provides a constant current to the differential pair transistors. This current source is crucial for the proper operation of the differential amplifier.

7. **Connections**: The circuit is interconnected with various nodes and wires, ensuring that the transistors, resistors, capacitors, and current source are properly connected to form the differential amplifier.

Overall, this schematic represents a differential amplifier with a cascode configuration, which is designed to amplify the difference between two input signals while rejecting common-mode signals. The use of cascode transistors helps improve the gain and bandwidth of the amplifier.
```

**Figure 9.64** CMFB loops around cascode and output stages.

Here is the image describtion:
```
The image consists of two parts: a simplified operational amplifier (op-amp) symbol on the left and a detailed transistor-level circuit diagram on the right.

### Left Side: Simplified Op-Amp Symbol
- The left side of the image shows a simplified symbol of an operational amplifier (op-amp).
- The op-amp has two input terminals: the non-inverting input (+) and the inverting input (-).
- The input voltage \( V_{in} \) is applied to the non-inverting input (+).
- The output voltage \( V_{out} \) is taken from the output terminal of the op-amp.
- There is a feedback loop from the output to the inverting input (-), indicating a negative feedback configuration.

### Right Side: Transistor-Level Circuit Diagram
- The right side of the image shows a detailed transistor-level circuit diagram, which appears to be a differential amplifier with a current mirror load and additional stages for amplification.

#### Components and Connections:
1. **Transistors M1 and M2:**
   - These are NMOS transistors forming the differential pair.
   - The gate of M1 is connected to the input voltage \( V_{in} \).
   - The source terminals of M1 and M2 are connected together and to a current source \( I_{SS} \) which is connected to ground.

2. **Current Source \( I_{SS} \):**
   - This is a constant current source connected to the common source node of M1 and M2, providing a bias current.

3. **Transistors M3 and M4:**
   - These are PMOS transistors forming a current mirror load for the differential pair.
   - The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.
   - The gates of M3 and M4 are connected together and to the drain of M3, forming the current mirror.

4. **Transistors M5, M6, M7, and M8:**
   - These are NMOS transistors forming another stage of amplification.
   - The drain of M4 is connected to the gate of M6, and the drain of M3 is connected to the gate of M5.
   - The sources of M5 and M6 are connected to the drains of M7 and M8, respectively.
   - The sources of M7 and M8 are connected to ground.

5. **Transistors M9 and M10:**
   - These are PMOS transistors forming another current mirror.
   - The drain of M9 is connected to the drain of M5, and the drain of M10 is connected to the drain of M6.
   - The gates of M9 and M10 are connected together and to the drain of M9.
   - The sources of M9 and M10 are connected to the positive supply voltage \( V_{DD} \).

6. **Output Node:**
   - The output voltage \( V_{out} \) is taken from the common drain connection of M6 and M10.

### Summary:
- The circuit on the right is a multi-stage amplifier with a differential input stage (M1 and M2), a current mirror load (M3 and M4), and additional amplification stages (M5 to M10).
- The left side shows a simplified op-amp symbol with negative feedback, representing the overall function of the detailed circuit on the right.
```

**Figure 9.65** Unity-gain buffer.

cascode branch. Specifically, *Vin,min* ≈ *Vout,min* = *VG S*<sup>1</sup>*,*<sup>2</sup> + *VISS*, approximately one threshold voltage higher than the allowable minimum provided by *M*5–*M*8.

What happens if *Vin* falls below the minimum given above? The MOS transistor operating as *ISS* enters the triode region, decreasing the bias current of the differential pair and hence lowering the transconductance. We then postulate that the limitation is overcome if the transconductance can somehow be restored.

A simple approach to extending the input CM range is to incorporate both NMOS and PMOS differential pairs such that when one is "dead," the other is "alive." Illustrated in Fig. 9.66, the idea is to combine two folded-cascode op amps with NMOS and PMOS input differential pairs. Here, as the input CM level approaches the ground potential, the NMOS pair's transconductance drops, eventually falling to zero. Nonetheless, the PMOS pair remains active, allowing normal operation. Conversely, if the input CM level approaches *VDD*, *M*<sup>1</sup>*<sup>P</sup>* and *M*<sup>2</sup>*<sup>P</sup>* begin to turn off, but *M*<sup>1</sup> and *M*<sup>2</sup> function properly.

An important concern in the circuit of Fig. 9.66 is the *variation* of the overall transconductance of the two pairs as the input CM level changes. Considering the operation of each pair, we anticipate the behavior depicted in Fig. 9.67. Thus, many properties of the circuit, including gain, speed, and noise, vary. More sophisticated techniques of minimizing this variation are described in [8].

Here is the image describtion:
```
The image depicts a complex CMOS (Complementary Metal-Oxide-Semiconductor) operational amplifier (op-amp) circuit. The circuit consists of multiple MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) transistors arranged in a specific configuration to achieve amplification and other desired electrical characteristics. Here is a detailed description of the circuit:

1. **Input Stage:**
   - The circuit has two input terminals labeled \( V_{in1} \) and \( V_{in2} \).
   - Transistors \( M_1 \) and \( M_2 \) are NMOS transistors forming a differential pair. The gates of \( M_1 \) and \( M_2 \) are connected to \( V_{in1} \) and \( V_{in2} \), respectively.
   - The sources of \( M_1 \) and \( M_2 \) are connected to a current source \( I_{SS1} \), which is connected to the ground.

2. **Current Mirrors:**
   - Transistors \( M_1p \) and \( M_2p \) are PMOS transistors forming a current mirror. The sources of \( M_1p \) and \( M_2p \) are connected to a current source \( I_{SS2} \), which is connected to the ground.
   - The gates of \( M_1p \) and \( M_2p \) are connected together and to the drain of \( M_1p \). The drain of \( M_2p \) is connected to the drain of \( M_2 \).

3. **Intermediate Stage:**
   - The drains of \( M_1 \) and \( M_2 \) are connected to the sources of PMOS transistors \( M_3 \) and \( M_4 \), respectively.
   - The gates of \( M_3 \) and \( M_4 \) are connected to a node labeled \( X \) and \( Y \), respectively.
   - The sources of \( M_3 \) and \( M_4 \) are connected to the drains of NMOS transistors \( M_5 \) and \( M_6 \), respectively.

4. **Output Stage:**
   - The drains of \( M_5 \) and \( M_6 \) are connected to the output terminal \( V_{out} \).
   - The sources of \( M_5 \) and \( M_6 \) are connected to the drains of NMOS transistors \( M_7 \) and \( M_8 \), respectively.
   - The gates of \( M_7 \) and \( M_8 \) are connected together and to the source of \( M_7 \), forming a current mirror.

5. **Load Stage:**
   - The circuit includes PMOS transistors \( M_9 \) and \( M_{10} \) connected in a cascode configuration.
   - The sources of \( M_9 \) and \( M_{10} \) are connected to the positive supply voltage \( V_{DD} \).
   - The gates of \( M_9 \) and \( M_{10} \) are connected together and to the node \( X \).
   - The drains of \( M_9 \) and \( M_{10} \) are connected to the nodes \( X \) and \( Y \), respectively.

Overall, this circuit is a multi-stage CMOS operational amplifier with differential input, current mirrors, and cascode configurations to enhance performance characteristics such as gain, bandwidth, and output swing.
```

**Figure 9.66** Extension of input CM range.

Here is the image describtion:
```
The image is a graph that illustrates the variation of equivalent transconductance (Gm,tot) with respect to the input common-mode (CM) level (Vin,CM). The horizontal axis represents the input CM level, ranging from 0 to VDD. The vertical axis represents the equivalent transconductance.

Key points on the graph:
- At Vin,CM = 0, the transconductance is labeled as gmp.
- At Vin,CM = VDD, the transconductance is labeled as gmn.
- The transconductance curve starts at gmp when Vin,CM is 0, rises to a peak value labeled as Gm,tot, and then decreases to gmn as Vin,CM approaches VDD.

The graph shows a smooth, bell-shaped curve indicating that the equivalent transconductance increases from gmp, reaches a maximum value (Gm,tot), and then decreases to gmn as the input CM level increases from 0 to VDD. The figure caption reads: "Figure 9.67 Variation of equivalent transconductance with the input CM level."
```

# **9.9 Slew Rate**

Op amps used in feedback circuits exhibit a large-signal behavior called "slewing." We first describe an interesting property of *linear* systems that vanishes during slewing. Consider the simple RC network shown in Fig. 9.68, where the input is an ideal voltage step of height *V*0. Since *Vout* = *V*0[1−exp*(*−*t/*τ *)*], where τ = *RC*, we have

$$\frac{dV\_{out}}{dt} = \frac{V\_0}{\tau} \exp\frac{-t}{\tau} \tag{9.58}$$

That is, the slope of the step response is proportional to the final value of the output; if we apply a larger input step, the output rises more rapidly. This is a fundamental property of linear systems: if the input amplitude is, say, doubled while other parameters remain constant, the output signal level must double at *every* point, leading to a twofold increase in the slope.

Here is the image describtion:
```
The image consists of two main parts: a circuit diagram on the left and two graphs on the right.

### Circuit Diagram:
- The circuit is a simple RC (resistor-capacitor) low-pass filter.
- It consists of a resistor \( R_1 \) and a capacitor \( C_1 \).
- The input voltage \( V_{in} \) is applied across the series combination of \( R_1 \) and \( C_1 \).
- The output voltage \( V_{out} \) is taken across the capacitor \( C_1 \).

### Graphs:
- There are two graphs, each showing the behavior of the input voltage \( V_{in} \) and the output voltage \( V_{out} \) over time \( t \).

#### Left Graph:
- The input voltage \( V_{in} \) is shown as a step function, where it suddenly jumps from a lower value to a higher value and remains constant.
- The output voltage \( V_{out} \) starts at a lower value and gradually increases towards the higher value of \( V_{in} \).
- The curve of \( V_{out} \) shows an exponential rise, indicating the charging behavior of the capacitor \( C_1 \) through the resistor \( R_1 \).
- A dotted line represents the initial slope of the exponential rise, showing the rate of change at the beginning.

#### Right Graph:
- The input voltage \( V_{in} \) is shown as a step function, where it suddenly drops from a higher value to a lower value and remains constant.
- The output voltage \( V_{out} \) starts at a higher value and gradually decreases towards the lower value of \( V_{in} \).
- The curve of \( V_{out} \) shows an exponential decay, indicating the discharging behavior of the capacitor \( C_1 \) through the resistor \( R_1 \).
- A dotted line represents the initial slope of the exponential decay, showing the rate of change at the beginning.

### Summary:
- The circuit diagram represents an RC low-pass filter.
- The graphs illustrate the time response of the output voltage \( V_{out} \) to a step change in the input voltage \( V_{in} \).
- The left graph shows the charging process of the capacitor when \( V_{in} \) steps up.
- The right graph shows the discharging process of the capacitor when \( V_{in} \) steps down.
```

**Figure 9.68** Response of a linear circuit to an input step.

Here is the image describtion:
```
The image depicts a circuit diagram featuring a linear operational amplifier (op-amp) configuration. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (Op-Amp)**:
   - The op-amp is represented by a triangular symbol with two input terminals and one output terminal.
   - The non-inverting input is marked with a "+" sign, and the inverting input is marked with a "-" sign.
   - The op-amp has an open-loop gain denoted by "A".

2. **Input Voltage (Vin)**:
   - The input voltage, labeled as \( V_{in} \), is applied to the non-inverting input of the op-amp.

3. **Output Resistance (Rout)**:
   - The op-amp has an output resistance, denoted as \( R_{out} \), which is shown as a resistor connected in series with the output terminal of the op-amp.

4. **Feedback Network**:
   - The feedback network consists of two resistors, \( R_1 \) and \( R_2 \), and a capacitor, \( C_L \).
   - \( R_1 \) is connected between the output of the op-amp (after \( R_{out} \)) and the junction point where \( R_2 \) and \( C_L \) are connected.
   - \( R_2 \) is connected between the junction point and ground.
   - \( C_L \) is connected in parallel with \( R_2 \), also between the junction point and ground.

5. **Output Voltage (Vout)**:
   - The output voltage, labeled as \( V_{out} \), is taken from the junction point where \( R_1 \), \( R_2 \), and \( C_L \) meet.

The circuit appears to be a typical configuration for an op-amp with a feedback network that includes resistors and a capacitor, which could be used for various applications such as filtering, amplification, or frequency compensation. The presence of \( R_{out} \) indicates that the op-amp has a non-zero output impedance, which can affect the overall performance of the circuit.
```

**Figure 9.69** Response of linear op amp to step response.

The foregoing observation applies to linear feedback systems as well. Shown in Fig. 9.69 is an example, where the op amp is assumed linear. Here, we can write

$$\left[\left(V\_{in} - V\_{out}\frac{R\_2}{R\_1 + R\_2}\right)A - V\_{out}\right]\frac{1}{R\_{out}} = \frac{V\_{out}}{R\_1 + R\_2} + V\_{out}C\_L\,\text{s}\tag{9.59}$$

Assuming *R*<sup>1</sup> + *R*<sup>2</sup> " *Rout*, we have

$$\frac{V\_{out}}{V\_{in}}(s) \approx \frac{A}{\left(1 + A\frac{R\_2}{R\_1 + R\_2}\right)\left[1 + \frac{R\_{ow}C\_L}{1 + AR\_2/(R\_1 + R\_2)}s\right]}\tag{9.60}$$

As expected, both the low-frequency gain and the time constant are divided by 1 + *AR*2*/(R*<sup>1</sup> + *R*2*)*. The step response is therefore given by

$$V\_{out} \approx V\_0 \frac{A}{1 + A \frac{R\_2}{R\_1 + R\_2}} \left[ 1 - \exp\frac{-t}{\frac{C\_L R\_{out}}{1 + A R\_2 / (R\_1 + R\_2)}} \right] u(t) \tag{9.61}$$

indicating that the slope is proportional to the final value. This type of response is called "linear settling."

With a realistic op amp, on the other hand, the step response of the circuit begins to deviate from (9.61) as the input amplitude increases. Illustrated in Fig. 9.70, the response to sufficiently small inputs follows the exponential of Eq. (9.61), but with large input steps, the output displays a linear *ramp* having a *constant slope.* Under this condition, we say that the op amp experiences slewing and call the slope of the ramp the "slew rate."

Here is the image describtion:
```
The image consists of two main parts: a circuit diagram on the left and a graph on the right.

### Circuit Diagram (Left Side):
1. **Op-Amp Configuration**:
   - The circuit features an operational amplifier (op-amp) with a non-ideal characteristic, indicated by the label "Actual Op Amp."
   - The op-amp has an input labeled \( V_{in} \) connected to the non-inverting input (+).
   - The inverting input (-) is connected to a feedback network.

2. **Feedback Network**:
   - The feedback network consists of two resistors, \( R_1 \) and \( R_2 \), and a capacitor \( C_L \).
   - \( R_1 \) is connected between the output of the op-amp and the junction of \( R_2 \) and \( C_L \).
   - \( R_2 \) is connected from the junction of \( R_1 \) and \( C_L \) to the ground.
   - \( C_L \) is connected from the junction of \( R_1 \) and \( R_2 \) to the ground.

3. **Output Resistance**:
   - The op-amp has an output resistance labeled \( R_{out} \), which is in series with the output terminal of the op-amp.

4. **Output Voltage**:
   - The output voltage is labeled \( V_{out} \), taken from the junction of \( R_{out} \) and \( R_1 \).

### Graph (Right Side):
1. **Input Voltage (\( V_{in} \))**:
   - The graph shows a step input voltage \( V_{in} \), which is a sudden change from a lower value to a higher value, represented by a vertical line.

2. **Output Voltage (\( V_{out} \))**:
   - The output voltage \( V_{out} \) is plotted against time \( t \).
   - The graph shows two different response curves for \( V_{out} \):
     - **Ramp Response**: This curve starts at the same point as the step input but rises linearly over time, indicating a ramp-like behavior.
     - **Exponential Response**: This curve starts at the same point as the step input but rises in an exponential manner, indicating a typical RC charging behavior.

3. **Labels**:
   - The graph is labeled to indicate the nature of the responses:
     - "Ramp" points to the linear rising curve.
     - "Exponential" points to the curve that rises exponentially.

### Summary:
The image illustrates the behavior of an actual op-amp circuit with a feedback network consisting of resistors and a capacitor. The graph shows how the output voltage \( V_{out} \) responds to a step input voltage \( V_{in} \), highlighting both ramp and exponential response characteristics. The presence of \( R_{out} \) indicates the non-ideal nature of the op-amp, affecting the output response.
```

**Figure 9.70** Slewing in an op amp circuit.

To understand the origin of slewing, let us replace the op amp of Fig. 9.70 by a simple CMOS implementation (Fig. 9.71), assuming for simplicity that *R*<sup>1</sup> + *R*<sup>2</sup> is very large. We first examine the circuit with a small input step. If *Vin* experiences a change of '*V*, *ID*<sup>1</sup> increases by *gm*'*V/*2 and *ID*<sup>2</sup> decreases by *gm*'*V/*2. Since the mirror action of *M*<sup>3</sup> and *M*<sup>4</sup> raises |*ID*4| by *gm*'*V/*2, the total smallsignal current provided by the op amp equals *gm*'*V*. This current begins to charge *CL* , but as *Vout* rises, so does *VX* , reducing the difference between *VG*<sup>1</sup> and *VG*<sup>2</sup> and hence the output current of the op amp. As a result, *Vout* varies according to (9.61).

Here is the image describtion:
```
The image depicts a differential amplifier circuit with a current mirror load. Here is a detailed description of the circuit components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The gate of M1 is connected to the input voltage \( V_{in} \) with a small signal \( \Delta V \) superimposed on it. The gate of M2 is connected to a reference voltage (often ground or a fixed bias voltage).
   - **M3 and M4:** These are PMOS transistors forming the current mirror load. The source of M3 and M4 are connected to the supply voltage \( V_{DD} \). The drain of M3 is connected to the drain of M1, and the drain of M4 is connected to the drain of M2.

2. **Current Source:**
   - **I_{SS}:** This is a current source connected to the common source node of M1 and M2, providing a constant current \( I_{SS} \).

3. **Resistors and Capacitor:**
   - **R1 and R2:** These resistors are connected in series between the drain of M2 and ground. The node between R1 and R2 is labeled as point X.
   - **C_L:** This is a load capacitor connected between the output node \( V_{out} \) and ground.

4. **Voltage Nodes:**
   - **V_{DD}:** The positive supply voltage.
   - **V_{out}:** The output voltage taken from the node where the drain of M2 connects to the series combination of R1 and R2.

5. **Small Signal Analysis:**
   - The small signal voltage \( \Delta V \) applied to the gate of M1 results in a differential voltage across M1 and M2.
   - The transconductance \( g_m \) of the transistors converts this differential voltage into a differential current.
   - The current mirror formed by M3 and M4 ensures that the current through M2 is mirrored from M1, maintaining the differential operation.
   - The differential current through M2 is then converted to a voltage across the resistors R1 and R2, which is further filtered by the load capacitor \( C_L \).

6. **Output Response:**
   - The output voltage \( V_{out} \) is shown to have a step response, indicating the circuit's behavior to a step input signal.

This circuit is commonly used in analog signal processing for amplifying differential signals while rejecting common-mode noise.
```

**Figure 9.71** Small-signal operation of a simple op amp.

Now suppose '*V* is so large that *M*<sup>1</sup> absorbs all of *ISS*, turning off *M*2. The circuit then reduces to that shown in Fig. 9.72(a), generating a ramp output with a slope equal to *ISS/CL* (if the channel-length modulation of *M*<sup>4</sup> and the current drawn by *R*<sup>1</sup> + *R*<sup>2</sup> are neglected). Note that so long as *M*<sup>2</sup> remains off, the feedback loop is broken and the current charging *CL* is constant and independent of the input level. As *Vout* rises, *VX* eventually approaches *Vin*, *M*<sup>2</sup> turns on, and the circuit returns to linear operation.

Here is the image describtion:
```
The image shows two circuit diagrams labeled (a) and (b), each representing a different configuration of a differential amplifier with active loads. Both circuits include MOSFET transistors, resistors, capacitors, and current sources. Here is a detailed description of each circuit:

### Circuit (a):
1. **Transistors:**
   - **M1**: An NMOS transistor with its gate connected to the input voltage \( V_{in} \).
   - **M2**: An NMOS transistor (grayed out, indicating it is not active in this configuration).
   - **M3**: A PMOS transistor with its source connected to \( V_{DD} \) and its drain connected to the drain of M1.
   - **M4**: A PMOS transistor with its source connected to \( V_{DD} \) and its drain connected to the output node \( V_{out} \).

2. **Current Source:**
   - A current source \( I_{SS} \) is connected to the source of M1 and to ground, providing a constant current.

3. **Resistors and Capacitor:**
   - **R1** and **R2**: Resistors connected in series between the output node \( V_{out} \) and ground.
   - **C_L**: A capacitor connected in parallel with R2, also between the output node \( V_{out} \) and ground.

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the node between the drain of M4 and the series combination of R1 and R2.
   - The graph next to the circuit shows the output voltage \( V_{out} \) as a function of time, with a slope indicating the rate of change of \( V_{out} \) given by \( \frac{I_{SS}}{C_L} \).

### Circuit (b):
1. **Transistors:**
   - **M1**: An NMOS transistor (grayed out, indicating it is not active in this configuration).
   - **M2**: An NMOS transistor with its gate connected to the input voltage \( V_{in} \).
   - **M3**: A PMOS transistor with its source connected to \( V_{DD} \) and its drain connected to the drain of M2.
   - **M4**: A PMOS transistor with its source connected to \( V_{DD} \) and its drain connected to the output node \( V_{out} \).

2. **Current Source:**
   - A current source \( I_{SS} \) is connected to the source of M2 and to ground, providing a constant current.

3. **Resistors and Capacitor:**
   - **R1** and **R2**: Resistors connected in series between the output node \( V_{out} \) and ground.
   - **C_L**: A capacitor connected in parallel with R2, also between the output node \( V_{out} \) and ground.

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the node between the drain of M4 and the series combination of R1 and R2.
   - The graph next to the circuit shows the output voltage \( V_{out} \) as a function of time, with a slope indicating the rate of change of \( V_{out} \) given by \( \frac{I_{SS}}{C_L} \).

### Common Elements:
- Both circuits use a differential amplifier configuration with active loads (PMOS transistors M3 and M4).
- Both circuits have a current source \( I_{SS} \) providing a constant current.
- Both circuits have a resistive load (R1 and R2) and a capacitive load (C_L) at the output.
- The output voltage \( V_{out} \) in both circuits is influenced by the current \( I_{SS} \) and the load capacitor \( C_L \), as indicated by the slope \( \frac{I_{SS}}{C_L} \) in the output voltage graphs.

The main difference between the two circuits is the active NMOS transistor (M1 in circuit (a) and M2 in circuit (b)) and the corresponding inactive transistor (grayed out).
```

**Figure 9.72** Slewing during (a) low-to-high and (b) high-to-low transitions.

In Fig. 9.71, slewing occurs for falling edges at the input as well. If the input drops so much that *M*<sup>1</sup> turns off, then the circuit is simplified as in Fig. 9.72(b), discharging *CL* by a current approximately equal to *ISS*. After *Vout* decreases sufficiently, the difference between *VX* and *Vin* is small enough to allow *M*<sup>1</sup> to turn on, leading to linear behavior thereafter.

The foregoing observations explain why slewing is a nonlinear phenomenon. If the input amplitude, say, doubles, the output level does not double at *all* points because the ramp exhibits a slope independent of the input.

Slewing is an undesirable effect in high-speed circuits that process large signals. While the small-signal bandwidth of a circuit may suggest a fast time-domain response, the large-signal speed may be limited by the slew rate simply because the current available to charge and discharge the dominant capacitor in the circuit is small. Moreover, since the input-output relationship during slewing is nonlinear, the output of a slewing amplifier exhibits substantial distortion. For example, if a circuit is to amplify a sinusoid *V*<sup>0</sup> sin ω0*t* (in the steady state), then its slew rate must exceed *V*0ω0.

#### ▲**Example 9.22**

Consider the feedback amplifier depicted in Fig. 9.73(a), where *C*<sup>1</sup> and *C*<sup>2</sup> set the closed-loop gain. (The bias network for the gate of *M*<sup>2</sup> is not shown.) (a) Determine the small-signal step response of the circuit. (b) Calculate the positive and negative slew rates.

Here is the image describtion:
```
The image consists of four sub-images labeled (a), (b), (c), and (d), each depicting different configurations or representations of a MOSFET-based amplifier circuit. Here is a detailed description of each sub-image:

### Sub-image (a):
- This is a schematic diagram of a differential amplifier circuit.
- The circuit consists of four MOSFETs labeled M1, M2, M3, and M4.
- M1 and M2 are the input transistors, with M1 receiving the input signal \( V_{in} \).
- M3 and M4 are the load transistors.
- The current source \( I_{SS} \) is connected to the source terminals of M1 and M2.
- The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.
- The output voltage \( V_{out} \) is taken from the drain of M2.
- Capacitors \( C1 \) and \( C2 \) are connected in series between the output node and ground, with node X being the junction between \( C1 \) and \( C2 \).

### Sub-image (b):
- This is a small-signal equivalent circuit of the differential amplifier.
- The input voltage \( V_{in} \) is applied to the positive terminal of a voltage-controlled current source.
- The voltage-controlled current source is represented by \( A_v V_1 \), where \( A_v \) is the voltage gain and \( V_1 \) is the input voltage.
- The current source is connected to a resistor \( R_{out} \), which represents the output resistance.
- The output voltage \( V_{out} \) is taken across \( R_{out} \).
- Capacitors \( C1 \) and \( C2 \) are connected in series between the output node and ground, with node X being the junction between \( C1 \) and \( C2 \).

### Sub-image (c):
- This is a modified version of the differential amplifier circuit shown in sub-image (a).
- The circuit is similar to (a), but the MOSFET M2 is shown in a lighter shade, indicating it is not active or is being ignored in this configuration.
- The current source \( I_{SS} \) is shown with an arrow pointing towards \( V_{out} \), indicating the direction of current flow.
- The rest of the circuit components and connections remain the same as in sub-image (a).

### Sub-image (d):
- This is another modified version of the differential amplifier circuit shown in sub-image (a).
- In this configuration, the MOSFETs M3 and M4 are shown in a lighter shade, indicating they are not active or are being ignored.
- The MOSFET M2 is active, and the current source \( I_{SS} \) is shown with an arrow pointing towards \( V_{out} \), indicating the direction of current flow.
- The rest of the circuit components and connections remain the same as in sub-image (a).

Overall, the image illustrates different configurations and representations of a differential amplifier circuit, highlighting the roles of various components and their interactions in the circuit.
```

Here is the image describtion:
```
The image is a text snippet that reads "Figure 9.73." It appears to be a label or caption typically found in academic or technical documents, such as textbooks, research papers, or manuals. This label likely refers to a specific figure or illustration within the document, indicating its sequential number (73) in Chapter 9. The text is in a standard font and is clear and legible.
```

### **Solution**

(a) Modeling the op amp as in Fig. 9.73(b), where *A<sup>v</sup>* = *gm*<sup>1</sup>*,*2*(rO*<sup>2</sup>%*rO*4*)* and *Rout* = *rO*<sup>2</sup>%*rO*4, we have *VX* = *C*1*Vout/(C*<sup>1</sup> + *C*2*)*, and hence

$$V\_P = \left(V\_{in} - \frac{C\_1}{C\_1 + C\_2}V\_{out}\right)A\_v\tag{9.62}$$

obtaining

$$\left[ \left( V\_{in} - \frac{C\_1}{C\_1 + C\_2} V\_{out} \right) A\_v - V\_{out} \right] \frac{1}{R\_{out}} = V\_{out} \frac{C\_1 C\_2}{C\_1 + C\_2} s \tag{9.63}$$

It follows that

Razavi-3930640 book December 17, 201516:59 394

$$\frac{V\_{out}}{V\_{in}}(s) = \frac{A\_v}{1 + A\_v \frac{C\_1}{C\_1 + C\_2} + \frac{C\_1 C\_2}{C\_1 + C\_2} R\_{out}s} \tag{9.64}$$

$$=\frac{A\_v/\left(1+A\_v\frac{C\_1}{C\_1+C\_2}\right)}{1+\frac{C\_1C\_2}{C\_1+C\_2}R\_{out}s/\left(1+A\_v\frac{C\_1}{C\_1+C\_2}\right)}\tag{9.65}$$

revealing that both the low-frequency gain and the time constant of the circuit have decreased by a factor of 1 + *AvC*1*/(C*<sup>1</sup> + *C*2*)*. The response to a step of height *V*<sup>0</sup> is thus given by

$$V\_{out}(t) = \frac{A\_v}{1 + A\_v \frac{C\_1}{C\_1 + C\_2}} V\_0 \left(1 - \exp\frac{-t}{\tau}\right) u(t) \tag{9.66}$$

where

$$\tau = \frac{C\_1 C\_2}{C\_1 + C\_2} R\_{out} / \left( \mathrm{l} + A\_v \frac{C\_1}{C\_1 + C\_2} \right) \tag{9.67}$$

(b) Suppose a large positive step is applied to the gate of *M*<sup>1</sup> in Fig. 9.73(a) while the initial voltage across *C*<sup>1</sup> is zero. Then, *M*<sup>2</sup> turns off and, as shown in Fig. 9.73(c), *Vout* rises according to *Vout(t)* = *ISS/*[*C*1*C*2*/(C*<sup>1</sup> + *C*2*)*]*t*. Similarly, for a large negative step at the input, Fig. 9.73(d) yields *Vout* = −*ISS/*[*C*1*C*2*/(C*<sup>1</sup> + *C*2*)*]*t*. ▲

As another example, let us find the slew rate of the telescopic op amp shown in Fig. 9.74(a). When a large differential input is applied, *M*<sup>1</sup> or *M*<sup>2</sup> turns off, reducing the circuit to that shown in Fig. 9.74(b). Thus, *Vout*<sup>1</sup> and *Vout*<sup>2</sup> appear as ramps with slopes equal to ±*ISS/(*2*CL )*, and consequently *Vout*<sup>1</sup> − *Vout*<sup>2</sup> exhibits a slew rate equal to *ISS/CL* . (Of course, the circuit is usually used in closed-loop form.)

Here is the image describtion:
```
The image shows two diagrams labeled (a) and (b), each depicting a differential amplifier circuit with active loads. Both circuits are built using MOSFET transistors and are designed to amplify differential signals.

### Diagram (a):
1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors. The gate of M1 is connected to the input signal \( V_{in} \), while the gate of M2 is connected to a reference voltage (often ground).
   - **M3 and M4:** These are the current mirror load transistors for the differential pair. The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.
   - **M5 and M6:** These transistors form the active load for the differential pair. The source of M5 is connected to the drain of M3, and the source of M6 is connected to the drain of M4.
   - **M7 and M8:** These transistors are part of the current mirror that provides the biasing current for the active load. The source of M7 is connected to \( V_{DD} \), and the source of M8 is also connected to \( V_{DD} \).

2. **Currents:**
   - The current source \( I_{SS} \) provides the tail current for the differential pair.
   - The current \( I_{SS} \) splits equally between M1 and M2, with each transistor carrying \( I_{SS}/2 \).
   - Similarly, the current through M5 and M6 is \( I_{SS}/2 \).

3. **Capacitors:**
   - Two capacitors \( C_L \) are connected to the output nodes to represent the load capacitance.

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the common node between M3 and M5.

### Diagram (b):
1. **Transistors:**
   - The configuration is similar to diagram (a), but M2 is shown in a lighter shade, indicating it is not active in this configuration.
   - M1 is still connected to the input signal \( V_{in} \).
   - M3, M5, M6, M7, and M8 are configured similarly to diagram (a).

2. **Currents:**
   - The current source \( I_{SS} \) still provides the tail current.
   - The current \( I_{SS} \) splits, with \( I_{SS}/2 \) flowing through M1 and M3, and the other \( I_{SS}/2 \) flowing through M5 and M6.

3. **Capacitors:**
   - The load capacitors \( C_L \) are connected similarly to diagram (a).

4. **Output:**
   - The output is taken from the same node as in diagram (a), between M3 and M5.

### Summary:
Both diagrams illustrate differential amplifier circuits with active loads, using MOSFET transistors. Diagram (a) shows a fully differential configuration, while diagram (b) shows a single-ended configuration with M2 inactive. The circuits are designed to amplify differential signals with the help of current mirrors and active loads to improve performance.
```

**Figure 9.74** Slewing in telescopic op amp.

It is also instructive to study the slewing behavior of a folded-cascode op amp with single-ended output [Fig. 9.75(a)]. Figures 9.75(a) and (b) depict the equivalent circuit for positive and negative input steps,

Here is the image describtion:
```
The image shows two different configurations of a CMOS (Complementary Metal-Oxide-Semiconductor) operational amplifier circuit. Both circuits are differential amplifiers with active loads and current mirrors, but they have different arrangements of transistors.

### Circuit (a):
1. **Input Stage:**
   - The input differential pair consists of transistors M1 and M2.
   - The tail current source is provided by a current source labeled ISS, which is connected to the sources of M1 and M2.

2. **Current Mirrors:**
   - Transistors M3 and M4 form a current mirror that mirrors the current from the differential pair to the next stage.
   - Transistors M5 and M6 form another current mirror that mirrors the current from the differential pair to the output stage.

3. **Active Loads:**
   - Transistors M7 and M8 are connected as active loads for the differential pair.
   - Transistors M9 and M10 are connected as active loads for the current mirrors.

4. **Output Stage:**
   - The output voltage (Vout) is taken from the drain of M6.
   - A load capacitor (CL) is connected to the output node to stabilize the circuit.

5. **Biasing:**
   - The circuit is biased with a current source ISS, which sets the operating point of the differential pair and the current mirrors.

### Circuit (b):
1. **Input Stage:**
   - The input differential pair consists of transistors M1 and M2.
   - The tail current source is provided by a current source labeled ISS, which is connected to the sources of M1 and M2.

2. **Current Mirrors:**
   - Transistors M3 and M4 form a current mirror that mirrors the current from the differential pair to the next stage.
   - Transistors M5 and M6 form another current mirror that mirrors the current from the differential pair to the output stage.

3. **Active Loads:**
   - Transistors M7 and M8 are connected as active loads for the differential pair.
   - Transistors M9 and M10 are connected as active loads for the current mirrors.

4. **Output Stage:**
   - The output voltage (Vout) is taken from the drain of M6.
   - A load capacitor (CL) is connected to the output node to stabilize the circuit.

5. **Biasing:**
   - The circuit is biased with a current source ISS, which sets the operating point of the differential pair and the current mirrors.

### Differences:
- In circuit (a), the current mirror formed by M3 and M4 is connected to the node X, while in circuit (b), it is connected to the node Y.
- The arrangement of the transistors and the connections between the nodes X and Y differ between the two circuits, which may affect the performance and characteristics of the amplifier.

Overall, both circuits are designed to amplify differential signals with high gain and low power consumption, typical of CMOS operational amplifiers.
```

**Figure 9.75** Slewing in folded-cascode op amp.

respectively. Here, the PMOS current sources provide a current of *IP* , and the current that charges or discharges *CL* is equal to *ISS*, yielding a slew rate of *ISS/CL* . Note that the slew rate is independent of *IP* if *IP* ≥ *ISS*. In practice, we choose *IP* ≈ *ISS*.

In Fig. 9.75(a), if *ISS > IP* , then during slewing, *M*<sup>3</sup> turns off and *VX* falls to a low level such that *M*<sup>1</sup> and the tail current source enter the triode region. Thus, for the circuit to return to equilibrium after *M*<sup>2</sup> turns on, *VX* must experience a large swing, slowing down the settling. This phenomenon is illustrated in Fig. 9.76.

Here is the image describtion:
```
The image depicts a schematic diagram of a transistor circuit, likely part of an analog or mixed-signal integrated circuit. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1:** This is an NMOS transistor with its gate connected to an input signal (represented by a line entering from the left). The source of M1 is connected to a current source labeled \( I_{SS} \) which is grounded.
   - **M9:** This is a PMOS transistor with its source connected to a positive supply voltage (typically denoted as \( V_{DD} \)). The drain of M9 is connected to node X.
   - **M3:** This is an NMOS transistor with its drain connected to node X and its source connected to a signal path that continues to the right.

2. **Current Sources:**
   - There are two current sources labeled \( I_{SS} \). One is connected to the source of M1 and grounded, providing a constant current through M1.
   - The other current source is not explicitly shown but is implied to be part of the circuit, likely providing a bias current.

3. **Node X:**
   - Node X is a critical point in the circuit where the drain of M1, the drain of M3, and the source of M9 are connected.

4. **Currents:**
   - \( I_{SS} \): This represents the current supplied by the current source connected to the source of M1.
   - \( I_P \): This represents the current flowing through the PMOS transistor M9.

5. **Signal Path:**
   - The input signal is applied to the gate of M1.
   - The output signal is taken from the drain of M3, which is connected to a signal path that continues to the right.

6. **Power Supply:**
   - The positive supply voltage \( V_{DD} \) is connected to the source of the PMOS transistor M9.

The circuit appears to be a part of a differential amplifier or a current mirror configuration, commonly used in analog circuits for amplification or biasing purposes. The exact function would depend on the surrounding circuitry and the specific application.
```

**Figure 9.76** Long settling due to overdrive recovery after slewing.

To alleviate this issue, two "clamp" transistors can be added as shown in Fig. 9.77(a) [9]. The idea is that the difference between *ISS* and *IP* now flows through *M*<sup>11</sup> or *M*12, requiring only enough drop in *VX* or *VY* to turn on one of these transistors. Figure 9.77(b) illustrates a more aggressive approach, where *M*<sup>11</sup> and *M*<sup>12</sup> clamp the two nodes directly to *VDD*. Since the equilibrium value of *VX* and *VY* is usually higher than *VDD* − *VTHN* , *M*<sup>11</sup> and *M*<sup>12</sup> are off during small-signal operation.

What trade-offs are encountered in increasing the slew rate? In the examples of Figs. 9.74 and 9.75, for a given load capacitance, *ISS* must be increased, and to maintain the same maximum output swing, all of the transistors must be made proportionally wider. As a result, the power dissipation and the input capacitance are increased. Note that if the device currents and widths scale together, *gmrO* of each transistor, and hence the open-loop gain of the op amp, remain constant.

How does an op amp leave the slewing regime and enter the linear-settling regime? Since the point at which one of the input transistors "turns on" is ambiguous, the distinction between slewing and linear settling is somewhat arbitrary. The following example illustrates the point.

Here is the image describtion:
```
The image shows two different configurations of a CMOS differential amplifier circuit. Both circuits are designed using MOSFET transistors and are labeled as (a) and (b).

### Circuit (a):
1. **Transistors M9 and M10**: These are PMOS transistors connected to the supply voltage \( V_{DD} \). They act as active loads for the differential pair.
2. **Transistors M11 and M12**: These are NMOS transistors forming the differential pair. The gates of M11 and M12 are the input terminals labeled as X and Y, respectively.
3. **Transistors M3 and M4**: These are NMOS transistors connected to the sources of M11 and M12, respectively. They are connected to the ground.
4. **Connections**:
   - The drain of M11 is connected to the drain of M9.
   - The drain of M12 is connected to the drain of M10.
   - The sources of M11 and M12 are connected together and then to the drains of M3 and M4, respectively.
   - The sources of M3 and M4 are connected to the ground.

### Circuit (b):
1. **Transistors M9 and M10**: Similar to circuit (a), these are PMOS transistors connected to the supply voltage \( V_{DD} \). They act as active loads for the differential pair.
2. **Transistors M11 and M12**: These are NMOS transistors forming the differential pair. The gates of M11 and M12 are the input terminals labeled as X and Y, respectively.
3. **Transistors M3 and M4**: These are NMOS transistors connected to the sources of M11 and M12, respectively. They are connected to the ground.
4. **Connections**:
   - The drain of M11 is connected to the drain of M9.
   - The drain of M12 is connected to the drain of M10.
   - The sources of M11 and M12 are connected together and then to the drains of M3 and M4, respectively.
   - The sources of M3 and M4 are connected to the ground.
   - Additionally, there is a direct connection between the sources of M11 and M12, forming a common-source node.

### Differences:
- The primary difference between the two circuits is the way the sources of the differential pair (M11 and M12) are connected. In circuit (a), the sources are connected through a common node, whereas in circuit (b), there is a direct connection between the sources of M11 and M12, forming a common-source node.

Both circuits are designed to amplify the difference between the input signals applied at X and Y. The configurations are typical in analog circuit design, particularly in operational amplifiers and other differential amplifier applications.
```

**Figure 9.77** Clamp circuit to limit swings at *X* and *Y* .

#### ▲**Example 9.23**

Razavi-3930640 book December 17, 201516:59 396

Consider the circuit of Fig. 9.73(a) in the slewing regime [Fig. 9.73(c)]. As *Vout* rises, so does *VX* , eventually turning *M*<sup>2</sup> on. As *ID*<sup>2</sup> increases from zero, the differential pair becomes more linear. Considering *M*<sup>1</sup> and *M*<sup>2</sup> to operate linearly if the difference between their drain currents is less than )*ISS* (e.g., ) = 0*.*1), determine how long the circuit takes to enter linear settling. Assume the input step has an amplitude of *V*0.

### **Solution**

The circuit displays a slew rate of *ISS/*[*C*1*C*2*/(C*<sup>1</sup> + *C*2*)*] until |*Vin*<sup>1</sup> − *Vin*<sup>2</sup>| is sufficiently small. From Chapter 4, we can write

$$
\alpha I\_{SS} = \frac{1}{2} \mu\_n C\_{ox} \frac{W}{L} (V\_{in1} - V\_{in2}) \sqrt{\frac{4I\_{SS}}{\mu\_n C\_{ox} \frac{W}{L}} - (V\_{in1} - V\_{in2})^2} \tag{9.68}
$$

obtaining

$$
\Delta V\_G^4 - \Delta V\_G^2 \frac{4I\_{SS}}{\mu\_n C\_{ox} \frac{W}{L}} + \left(\frac{2\alpha I\_{SS}}{\mu\_n C\_{ox} \frac{W}{L}}\right)^2 = 0\tag{9.69}
$$

where '*VG* = *Vin*<sup>1</sup> − *Vin*2. Thus,

$$
\Delta V\_G \approx \alpha \sqrt{\frac{I\_{SS}}{\mu\_n C\_{ox} \frac{W}{L}}} \tag{9.70}
$$

(Recall that <sup>√</sup>*ISS/*[*µnCox (W/L)*] is the equilibrium overdrive voltage of each transistor in the differential pair.) Alternatively, we recognize that for a small difference, )*ISS*, between *ID*<sup>1</sup> and *ID*2, a small-signal approximation is valid: )*ISS* = *gm*'*VG*. Thus, '*VG* = )*ISS/gm* ≈ )*ISS/* <sup>√</sup>*µnCox (W/L)ISS*. Note that this is a rough calculation because as *M*<sup>2</sup> turns on, the current charging the load capacitance is no longer constant.

Since *VX* must rise to *V*<sup>0</sup> −'*VG* for *M*<sup>2</sup> to carry the required current, *Vout* increases by *(V*<sup>0</sup> −'*VG)(*1+*C*2*/C*1*)*, requiring a time given by

$$t = \frac{C\_2}{I\_{SS}} \left( V\_0 - \alpha \sqrt{\frac{I\_{SS}}{\mu\_n C\_{ox} \frac{W}{L}}} \right) \tag{9.71}$$

▲

In the earlier example, the value of ) that determines the onset of linear settling depends, among other things, on the actual required linearity. In other words, for a nonlinearity of 1%, ) can be quite a lot larger than for a nonlinearity of 0.1%.

The slewing behavior of two-stage op amps is somewhat different from that of the circuits studied earlier. This case is studied in Chapter 10.

# **9.10 High-Slew-Rate Op Amps**

Our formulation of the slew rate in various op amp topologies implies that, for a given capacitance, slewlimited settling can be improved only by raising the bias current and hence the power consumption. This trade-off can be mitigated if the current available to charge the capacitor of interest automatically rises during slewing and falls back to its original value thereafter. In this section, we study op amp topologies that exploit this idea.

### **9.10.1 One-Stage Op Amps**

We begin with a simple common-source stage incorporating a current-source load biased at a value of *I*<sup>0</sup> [Fig. 9.78(a)]. In the absence of an input signal, *ID*<sup>1</sup> = *I*0, but if *Vin* jumps down to turn *M*<sup>1</sup> off, then *I*<sup>0</sup> flows through *CL* , yielding a slew rate of *I*0*/CL* . <sup>7</sup> Can we automatically increase the drain current of *M*<sup>2</sup> during this transient? To this end, we must allow *Vb* to change and, in fact, follow the jump in *Vin*. For example, as shown in Fig. 9.78(b), we can simply apply *Vin* to both transistors so that a downward jump in *Vin* also raises |*ID*2|. This complementary topology was studied in Chapter 3 and found to suffer from poor power supply rejection. We pursue other topologies here.

Here is the image describtion:
```
The image shows two different configurations of MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) circuits, labeled as (a) and (b).

**Circuit (a):**
- This is a common-source amplifier with a current source load.
- The circuit consists of two MOSFETs, labeled M1 and M2.
- M1 is an NMOS transistor with its source connected to ground, its gate connected to the input voltage \( V_{in} \), and its drain connected to the drain of M2.
- M2 is a PMOS transistor with its source connected to \( V_{DD} \) (the positive supply voltage), its gate connected to a bias voltage \( V_b \), and its drain connected to the drain of M1.
- There is a current source \( I_0 \) connected between \( V_{DD} \) and the drain of M2.
- The output voltage \( V_{out} \) is taken from the common drain connection of M1 and M2.
- A load capacitor \( C_L \) is connected between the output node and ground.

**Circuit (b):**
- This is a CMOS (Complementary Metal-Oxide-Semiconductor) inverter.
- The circuit consists of two MOSFETs, labeled M1 and M2.
- M1 is an NMOS transistor with its source connected to ground, its gate connected to the input voltage \( V_{in} \), and its drain connected to the output node \( V_{out} \).
- M2 is a PMOS transistor with its source connected to \( V_{DD} \), its gate connected to the input voltage \( V_{in} \), and its drain connected to the output node \( V_{out} \).
- The output voltage \( V_{out} \) is taken from the common drain connection of M1 and M2.
- A load capacitor \( C_L \) is connected between the output node and ground.

In summary, circuit (a) is a common-source amplifier with a current source load, while circuit (b) is a CMOS inverter. Both circuits use MOSFETs and have a load capacitor connected to the output node.
```

**Figure 9.78** Slewing in (a) a simple CS stage and (b) a complementary CS stage.

Let us control *M*<sup>2</sup> in Fig. 9.78(a) by current mirror action, as depicted in Fig. 9.79(a), and ask how *Ib* must be controlled by *Vin*. Can *Ib* be derived from another common-source device [Fig. 9.79(b)]? No; as *Vin* jumps down in this circuit, *Ib decreases*. We must therefore include an additional signal inversion in the path controlling *Ib*. Alternatively, we can consider a differential topology, where both the input signal, *V* <sup>+</sup> *in* , and its inverted version, *V* <sup>−</sup> *in* , are available. Illustrated in Fig. 9.79(c), the idea is to control the bias current of *M*<sup>2</sup> by *V* <sup>−</sup> *in* and that of *M*<sup>4</sup> by *V* <sup>+</sup> *in* . For example, if *V* <sup>+</sup> *in* jumps down and *V* <sup>−</sup> *in* jumps up, then (1) *M*<sup>5</sup> draws less current from *M*8, lowering |*ID*4|, (2) *M*<sup>3</sup> draws more current, discharging its load capacitance, (3) *M*<sup>6</sup> draws more current from *M*7, raising |*ID*2|, and (4) *M*<sup>1</sup> draws less current, allowing its drain capacitance to be charged by *M*2.

The circuits of Figs. 9.78(b) and 9.79(c) are called "push-pull" stages as they turn the load current source into an "active" pull-up device. Loosely speaking, we also refer to them as "class-AB" amplifiers.<sup>8</sup>

<sup>7</sup>If *Vin* jumps *up*, *M*<sup>1</sup> must absorb both *I*<sup>0</sup> and the current flowing out of *CL* .

<sup>8</sup>By contrast, topologies with a constant bias current are called "class-A" amplifiers.

Here is the image describtion:
```
The image consists of four different circuit diagrams labeled (a), (b), (c), and (d). Each circuit appears to be a type of MOSFET amplifier or differential amplifier. Here is a detailed description of each circuit:

### Circuit (a)
- **Components**: 
  - Three MOSFETs labeled M1, M2, and M3.
  - A current source labeled I_b.
  - A capacitor labeled C_L.
- **Connections**:
  - The source of M1 is connected to ground.
  - The gate of M1 is connected to the input voltage V_in.
  - The drain of M1 is connected to the source of M2.
  - The gate of M2 is connected to the drain of M3.
  - The source of M3 is connected to the current source I_b, which is connected to ground.
  - The drain of M2 is connected to V_DD (positive supply voltage) and also to the output voltage V_out through the capacitor C_L.

### Circuit (b)
- **Components**: 
  - Four MOSFETs labeled M1, M2, M3, and M4.
  - A current source labeled I_b.
  - A capacitor labeled C_L.
- **Connections**:
  - The source of M1 is connected to ground.
  - The gate of M1 is connected to the input voltage V_in.
  - The drain of M1 is connected to the source of M2.
  - The gate of M2 is connected to the drain of M3.
  - The source of M3 is connected to the current source I_b, which is connected to ground.
  - The drain of M2 is connected to V_DD and also to the output voltage V_out through the capacitor C_L.
  - The gate of M4 is connected to the input voltage V_in, and its source is connected to ground.

### Circuit (c)
- **Components**: 
  - Eight MOSFETs labeled M1, M2, M3, M4, M5, M6, M7, and M8.
  - Two capacitors labeled C_L.
- **Connections**:
  - The sources of M1 and M5 are connected to ground.
  - The gates of M1 and M5 are connected to the input voltage V_in+.
  - The drains of M1 and M5 are connected to the sources of M2 and M7, respectively.
  - The gates of M2 and M7 are connected to the nodes X and Y, respectively.
  - The drains of M2 and M7 are connected to V_DD.
  - The sources of M3 and M6 are connected to ground.
  - The gates of M3 and M6 are connected to the input voltage V_in.
  - The drains of M3 and M6 are connected to the sources of M4 and M8, respectively.
  - The gates of M4 and M8 are connected to the nodes X and Y, respectively.
  - The drains of M4 and M8 are connected to V_DD.
  - The output voltages V_out1 and V_out2 are taken from the drains of M2 and M4, respectively, through the capacitors C_L.

### Circuit (d)
- **Components**: 
  - Eight MOSFETs labeled M1, M2, M3, M4, M5, M6, M7, and M8.
  - Two current sources labeled I_ss1 and I_ss2.
  - Two capacitors labeled C_L.
- **Connections**:
  - The sources of M1 and M5 are connected to the current source I_ss2, which is connected to ground.
  - The gates of M1 and M5 are connected to the input voltage V_in+.
  - The drains of M1 and M5 are connected to the sources of M2 and M7, respectively.
  - The gates of M2 and M7 are connected to the nodes X and Y, respectively.
  - The drains of M2 and M7 are connected to V_DD.
  - The sources of M3 and M6 are connected to the current source I_ss1, which is connected to ground.
  - The gates of M3 and M6 are connected to the input voltage V_in.
  - The drains of M3 and M6 are connected to the sources of M4 and M8, respectively.
  - The gates of M4 and M8 are connected to the nodes X and Y, respectively.
  - The drains of M4 and M8 are connected to V_DD.
  - The output voltages V_out1 and V_out2 are taken from the drains of M2 and M4, respectively, through the capacitors C_L.

Each circuit represents a different configuration of MOSFET amplifiers, with variations in the number of transistors, connections, and additional components like current sources and capacitors.
```

**Figure 9.79** (a) CS stage with current mirror biasing, (b) injection of signal into the mirror with incorrect polarity, (c) injection of signal into the mirror with ccrrect polarity, and (d) addition of tail current sources.

By virtue of the temporary boost in the slew rate, such circuits alleviate the trade-off between the speed and the average power consumption.

In order to improve the input common-mode rejection, we add tail current sources to *M*<sup>1</sup> and *M*<sup>3</sup> and to *M*<sup>5</sup> and *M*<sup>6</sup> [Fig. 9.79(d)]. We now wish to calculate the circuit's slew rate with a large input step. If, for example, *V* <sup>+</sup> *in* jumps up and *M*<sup>1</sup> and *M*<sup>5</sup> absorb all of their respective tail currents, then *M*<sup>2</sup> is off and *Vout*<sup>1</sup> falls at a rate of *ISS*1*/CL* while *M*<sup>3</sup> is off and *Vout*<sup>2</sup> rises at a rate of *ISS*2*(W*4*/W*8*)/CL* (if *L*<sup>4</sup> = *L*8). The differential slew rate is thus equal to [*ISS*<sup>1</sup> + *ISS*2*(W*4*/W*8*)*]*/CL* . Without the push-pull action, on the other hand, this slew rate would be limited to *ISS*1*/CL* . If we choose *W*4*/W*<sup>8</sup> equal to, say, 5 and *ISS*<sup>2</sup> equal to *ISS*1, then the SR increases by a factor of 6 with a twofold power penalty.<sup>9</sup>

#### ▲**Example 9.24**

Calculate the small-signal voltage gain of the class-AB op amp shown in Fig. 9.79(d).

### **Solution**

In addition to the main path, the mirror path contributes gain as well. Since the mirror action amplifies the drain currents of *M*<sup>5</sup> and *M*<sup>6</sup> by a factor of *W*4*/W*8, we approximate the gain in this path as *(W*4*/W*8*)gm*5*(rO*<sup>3</sup>||*rO*4*)* and add it to that of the main path:

$$|A\_v| \approx g\_{m1}(r\_{O3}||r\_{O4}) + (W\_4/W\_8)g\_{m5}(r\_{O3}||r\_{O4})\tag{9.72}$$

$$\approx \left[ \text{g}\_{m1} + (W4/W8)\text{g}\_{m5} \right] (r\_{O3} || r\_{O4}) \tag{9.73}$$

▲

The mirror path thus raises the apparent transconductance from *gm*<sup>1</sup> to *gm*<sup>1</sup> + *(W*4*/W*8*)gm*5.

<sup>9</sup>One can argue that the fixed tail currents no longer allow class-AB operation, but we disregard this subtlety for now.

Let us now determine the transfer function of the above circuit and examine the effect of the mirror pole. We write the transfer function from the input through the mirror path to the output as

$$H\_{mirr}(\mathbf{s}) = \frac{W\_4}{W\_8} \mathbf{g}\_{m\mathbf{\hat{s}}}(r\_{O3}||r\_{O4}) \frac{1}{1 + \frac{s}{\alpha\_{p,X}}} \frac{1}{1 + \frac{s}{\alpha\_{out}}} \tag{9.74}$$

where ω*p,<sup>X</sup>* ≈ *gm*8*/CY* and ω*out* = [*(rO*3||*rO*4*)CL* ] <sup>−</sup>1. For the main path, we simply have

$$H\_{\rm main}(\mathbf{s}) = \mathbf{g}\_{m1}(r\_{O3}||r\_{O4})\frac{1}{1 + \frac{s}{\alpha\_{out}}}\tag{9.75}$$

It follows that

$$H\_{tot}(\mathbf{s}) = H\_{main}(\mathbf{s}) + H\_{mirr}(\mathbf{s})\tag{9.76}$$

$$\eta\_1 = \frac{r\_{O3}||r\_{O4}}{1 + \frac{s}{\omega\_{out}}} \left[ \frac{W\_4}{W\_8} \frac{g\_{mS}}{1 + \frac{s}{\omega\_{p,X}}} + g\_{m1} \right] \tag{9.77}$$

$$\eta\_1 = \frac{r\_{O3}||r\_{O4}}{1 + \frac{\mathcal{S}}{\alpha\_{\rm out}}} \cdot \frac{(W\_4/W\_8)\mathcal{g}\_{m\mathcal{S}} + \mathcal{g}\_{m1} + \mathcal{g}\_{m1}s/\omega\_{p,X}}{1 + \frac{\mathcal{S}}{\omega\_{p,X}}} \tag{9.78}$$

As seen in other examples in Chapter 6, the presence of the additional signal path leads to a zero in the transfer function. This zero frequency is given by

$$|\boldsymbol{\omega}\_{\boldsymbol{z}}| = \left(\frac{W\_4}{W\_8}\frac{\mathbf{g}\_{m\boldsymbol{\Re}}}{\mathbf{g}\_{m1}} + 1\right)\boldsymbol{\omega}\_{p,\boldsymbol{X}}\tag{9.79}$$

Unfortunately, it is not possible to equate ω*<sup>z</sup>* to ω*<sup>p</sup>,<sup>X</sup>* because *(W*4*/W*8*)(gm*5*/gm*1*)* is typically around unity or higher. Also, in practice, ω*out <* ω*<sup>p</sup>,<sup>X</sup>* .

It is tempting to raise the SR in Fig. 9.79(d) by increasing *W*4*/W*8, but we must note that, as a result, the pole frequency associated with the mirror nodes falls. Approximating this pole by *gm*8*/CY* and writing *gm*<sup>8</sup> <sup>=</sup> <sup>√</sup>*ISS*2*µnCox (W/L)*<sup>8</sup> and *CY* <sup>≈</sup> <sup>2</sup>*(W*<sup>4</sup> <sup>+</sup> *<sup>W</sup>*8*)LCox* <sup>+</sup> *CDB*<sup>8</sup> <sup>+</sup> *CDB*5, we recognize that the mirror pole frequency is inversely proportional to *W*4.

### **9.10.2 Two-Stage Op Amps**

In order to achieve a high slew rate, we can apply push-pull operation to the second stage of a twostage op amp. To this end, we view the arrangement shown in Fig. 9.79(c) as the second stage and precede it with a differential pair, arriving at the topology depicted in Fig. 9.80. This circuit provides a voltage gain of

$$|A\_v| = g\_{m\theta}(r\_{O\theta}||r\_{O11})[g\_{m1} + (W\_4/W\_8)g\_{m5}](r\_{O1}||r\_{O2})\tag{9.80}$$

But how about the slew rate? Suppose, for example, *Vin*<sup>1</sup> and *Vin*<sup>2</sup> experience a large differential step such that the entire *ISS* flows through node *P*. If this node is "agile" enough, i.e., if its capacitance is relatively small, *VP* rises rapidly, applying a large overdrive to *M*<sup>1</sup> and *M*<sup>5</sup> and creating a high slew rate at the output. In other words, since *VP* (or *VQ*) can reach near *VDD* when only *M*<sup>9</sup> (or *M*10) is on, the available current is much larger than the bias current of the output stage. This behavior stands in contrast to that

Here is the image describtion:
```
The image depicts a schematic diagram of a fully differential operational amplifier (op-amp) circuit. Here is a detailed description of the components and their connections:

1. **Current Source (Iss)**: At the top left, there is a current source labeled \( I_{ss} \). This current source is connected to the drains of two NMOS transistors, \( M_9 \) and \( M_{10} \).

2. **Differential Pair (M9 and M10)**: The transistors \( M_9 \) and \( M_{10} \) form a differential pair. The gates of \( M_9 \) and \( M_{10} \) are connected to the input signals \( V_{in1} \) and \( V_{in2} \), respectively. The sources of \( M_9 \) and \( M_{10} \) are connected together and to the current source \( I_{ss} \).

3. **Current Mirrors (M11 and M12)**: Below the differential pair, there are two NMOS transistors, \( M_{11} \) and \( M_{12} \), with their gates connected to a bias voltage \( V_b \). The sources of \( M_{11} \) and \( M_{12} \) are connected to ground. The drains of \( M_{11} \) and \( M_{12} \) are connected to the sources of \( M_9 \) and \( M_{10} \), respectively, forming current mirrors.

4. **Intermediate Nodes (P and Q)**: The drains of \( M_9 \) and \( M_{10} \) are labeled as nodes \( P \) and \( Q \), respectively. These nodes are connected to the gates of NMOS transistors \( M_5 \) and \( M_1 \) (for node \( P \)) and \( M_3 \) and \( M_6 \) (for node \( Q \)).

5. **Load Transistors (M5, M1, M3, M6)**: The transistors \( M_5 \), \( M_1 \), \( M_3 \), and \( M_6 \) are connected in a configuration that forms the load for the differential pair. The sources of \( M_5 \) and \( M_1 \) are connected to ground, and their drains are connected to the intermediate nodes \( P \) and \( Q \), respectively. Similarly, the sources of \( M_3 \) and \( M_6 \) are connected to ground, and their drains are connected to the intermediate nodes \( Q \) and \( P \), respectively.

6. **Capacitive Loads (CL)**: There are capacitors labeled \( C_L \) connected from the drains of \( M_1 \) and \( M_3 \) to ground. These capacitors represent the load capacitance.

7. **Output Nodes (X and Y)**: The drains of \( M_1 \) and \( M_3 \) are labeled as nodes \( X \) and \( Y \), respectively. These nodes are connected to the gates of PMOS transistors \( M_7 \) and \( M_2 \) (for node \( X \)) and \( M_4 \) and \( M_8 \) (for node \( Y \)).

8. **PMOS Transistors (M7, M2, M4, M8)**: The transistors \( M_7 \), \( M_2 \), \( M_4 \), and \( M_8 \) are connected in a configuration that forms the output stage of the amplifier. The sources of these PMOS transistors are connected to the supply voltage \( V_{DD} \). The drains of \( M_7 \) and \( M_2 \) are connected together, and the drains of \( M_4 \) and \( M_8 \) are connected together.

9. **Power Supply (VDD)**: The topmost line in the schematic represents the positive power supply voltage \( V_{DD} \).

In summary, this circuit is a fully differential operational amplifier with a differential input stage, current mirrors, and a differential output stage. The capacitive loads \( C_L \) are connected to the output nodes to represent the load capacitance.
```

**Figure 9.80** Two-stage op amp with slew enhancement.

of the circuit in Fig. 9.79(d), where the available current is a multiple of the tail currents and cannot be raised further "upon demand."

We return to this two-stage op amp in Chapter 10 and analyze its slew rate in the presence of frequency compensation.

# **9.11 Power Supply Rejection**

As with other analog circuits, op amps are often supplied from noisy lines and must therefore "reject" the noise adequately. For this reason, it is important to understand how noise on the supply manifests itself at the output of an op amp.

Let us consider the simple op amp shown in Fig. 9.81, assuming that the supply voltage varies slowly. If the circuit is perfectly symmetric, *Vout* = *VX* . Since the diode-connected device "clamps" node *X* to *VDD*, *VX* and hence *Vout* experience approximately the same change as does *VDD*. In other words, the gain from *VDD* to *Vout* is close to unity. The power supply rejection ratio (PSRR) is defined as the gain from the input to the output divided by the gain from the supply to the output. At low frequencies:

$$\text{PSRR} \approx \text{g}\_{mN}(r\_{OP} \| r\_{ON}) \tag{9.81}$$

Here is the image describtion:
```
The image depicts a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Transistors**: The circuit consists of four MOSFETs labeled M1, M2, M3, and M4.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the load transistors.

2. **Power Supply**: The circuit is powered by a voltage source labeled V_DD at the top.

3. **Current Source**: At the bottom of the circuit, there is a current source labeled I_SS, which provides a constant current.

4. **Connections**:
   - The source terminals of M1 and M2 are connected together and to the current source I_SS.
   - The drain of M1 is connected to the drain of M3.
   - The drain of M2 is connected to the drain of M4.
   - The gates of M3 and M4 are connected to their respective drains, indicating that they are configured as diode-connected loads.

5. **Inputs**:
   - The gate of M1 is connected to an input signal, which is represented by a wavy line indicating an AC signal.
   - The gate of M2 is connected to another input signal, also represented by a wavy line.

6. **Output**:
   - The output voltage, V_out, is taken from the drain of M2 and the source of M4.

7. **Node X**: There is a node labeled X at the connection between the drain of M1 and the source of M3.

This differential amplifier works by amplifying the difference between the two input signals applied to the gates of M1 and M2. The current source I_SS ensures that the total current through M1 and M2 remains constant, which helps in achieving high gain and common-mode rejection. The diode-connected load transistors M3 and M4 provide the necessary load resistance for the amplifier.
```

**Figure 9.81** Supply rejection of differential pair with active current mirror.

#### ▲**Example 9.25**

Calculate the low-frequency PSRR of the feedback circuit shown in Fig. 9.82(a).

Here is the image describtion:
```
The image consists of two parts, labeled (a) and (b), which depict a CMOS circuit and its small-signal equivalent model, respectively.

### Part (a): CMOS Circuit
This part shows a CMOS amplifier circuit with the following components:
- **Transistors:**
  - \( M_1 \) and \( M_2 \): These are NMOS transistors.
  - \( M_3 \) and \( M_4 \): These are PMOS transistors.
- **Current Source:**
  - \( I_{SS} \): A current source connected to the source terminals of \( M_1 \) and \( M_2 \).
- **Capacitors:**
  - \( C_1 \) and \( C_2 \): Capacitors connected in series between the output node \( V_{out} \) and ground, with a node \( P \) between them.
- **Voltage Supply:**
  - \( V_{DD} \): The positive supply voltage connected to the drain terminals of \( M_3 \) and \( M_4 \).

### Connections:
- The gate of \( M_1 \) is connected to the input voltage \( V_{in} \).
- The drain of \( M_1 \) is connected to the source of \( M_3 \) at node \( X \).
- The drain of \( M_2 \) is connected to the source of \( M_4 \) and also to the output node \( V_{out} \).
- The gate of \( M_3 \) is connected to \( V_{DD} \).
- The gate of \( M_4 \) is connected to node \( X \).

### Part (b): Small-Signal Equivalent Model
This part shows the small-signal equivalent model of the CMOS circuit in part (a). The components and their connections are as follows:
- **Voltage Source:**
  - \( V_{DD} \): The positive supply voltage.
- **Current Sources:**
  - \( g_{m1} V_1 \): A current source representing the transconductance of \( M_1 \).
  - \( g_{m2} V_2 \): A current source representing the transconductance of \( M_2 \).
  - \( g_{m3} V_4 \): A current source representing the transconductance of \( M_3 \).
  - \( g_{m4} V_4 \): A current source representing the transconductance of \( M_4 \).
- **Resistors:**
  - \( \frac{1}{g_{m3}} \): A resistor connected between \( V_{DD} \) and node \( X \).
  - \( r_{o4} \): A resistor connected between the output node \( V_{out} \) and ground.
- **Capacitors:**
  - \( C_1 \) and \( C_2 \): Capacitors connected in series between the output node \( V_{out} \) and ground, with a node \( P \) between them.

### Connections:
- The voltage \( V_1 \) is applied to the gate of \( M_1 \).
- The voltage \( V_2 \) is applied to the gate of \( M_2 \).
- The voltage \( V_4 \) is applied to the gate of \( M_4 \).
- The node \( X \) is connected to the source of \( M_3 \) and the gate of \( M_4 \).
- The output voltage \( V_{out} \) is taken from the drain of \( M_2 \) and \( M_4 \).

### Summary:
The image illustrates a CMOS amplifier circuit and its corresponding small-signal model, highlighting the relationships between the transistors, current sources, resistors, and capacitors in both the actual circuit and its small-signal representation.
```

### **Solution**

From the foregoing analysis, we may surmise that a change '*V* in *VDD* appears unattenuated at the output. But, we should note that if *Vout* changes, so do *VP* and *ID*2, thereby opposing the change. Using Fig. 9.82(b) and neglecting channel-length modulation in *M*1–*M*<sup>3</sup> for simplicity, we can write

$$V\_{\rm out} \frac{C\_1}{C\_1 + C\_2} - V\_2 = -V\_1 \tag{9.82}$$

and *gm*1*V*<sup>1</sup> + *gm*2*V*<sup>2</sup> = 0. Thus, if the circuit is symmetric,

$$V\_2 = \frac{V\_{out}}{2} \frac{C\_1}{C\_1 + C\_2} \tag{9.83}$$

We also have

$$-\frac{g\_{m1}V\_1}{g\_{m3}}g\_{m4} - \frac{V\_{DD} - V\_{out}}{r\_{O4}} + g\_{m2}V\_2 = 0\tag{9.84}$$

It follows that

$$\frac{V\_{out}}{V\_{DD}} = \frac{1}{g\_{m2}r\_{O4}\frac{C\_1}{C\_1 + C\_2} + 1} \tag{9.85}$$

Thus,

$$\text{PSRR} \approx (\text{l} + \frac{C\_2}{C\_1})(g\_{m2}r\_{O4}\frac{C\_1}{C\_1 + C\_2} + \text{l})\tag{9.86}$$

$$
\approx \text{ } \S{m2}{}^{r}O4\text{ }\tag{9.87}
$$

▲

The denominator of Eq. (9.85) looks like one plus a loop gain. Is that true? Let us set the main input in Fig. 9.82(a) to zero and view the path from *VDD* to *Vout* as an amplifier [Fig. 9.83(a)], omitting *C*<sup>1</sup> and *C*2. In this case, the gain, ∂*Vout/*∂*VDD*, is equal to unity. Now, as depicted in Fig. 9.83(b), we sense *Vout* by means of a capacitive divider and return the result to some node within the amplifier. We expect the gain to drop by one plus the loop gain associated with the feedback loop. Indeed, this loop gain is equal to [*C*1*/(C*<sup>1</sup> + *C*2*)*]*gm*2*rO*<sup>4</sup> if channel-length modulation is neglected for *M*1–*M*3. We therefore recognize that feedback reduces ∂*Vout/*∂*VDD* and ∂*Vout/*∂*Vin* by the same factor, leaving the PSRR relatively constant.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b).

(a) The first circuit diagram shows a simple inverter. It consists of a single logic gate (inverter) with its input connected to a voltage source labeled \( V_{DD} \). The output of the inverter is labeled \( V_{out} \). There are no additional components connected to the inverter.

(b) The second circuit diagram is a more complex version of the first. It also features an inverter with its input connected to a voltage source labeled \( V_{DD} \). However, the output of the inverter, labeled \( V_{out} \), is connected to a network of capacitors. Specifically, the output is connected to a capacitor labeled \( C_1 \), which is in turn connected to another capacitor labeled \( C_2 \). The other end of \( C_2 \) is connected to the ground. This configuration suggests a capacitive load on the inverter's output.

In summary, diagram (a) shows a basic inverter circuit, while diagram (b) shows an inverter with a capacitive load consisting of two capacitors in series.
```

**Figure 9.83** Equivalent circuits for path from *VDD* to output.

# **9.12 Noise in Op Amps**

Razavi-3930640 book December 17, 201516:59 402

In low-noise applications, the input-referred noise of op amps becomes critical. We now extend the noise analysis of differential amplifiers in Chapter 7 to more sophisticated topologies. With many transistors in an op amp, it may seem difficult to intuitively identify the dominant sources of noise. A simple rule for inspection is to (mentally) change the gate voltage of each transistor by a small amount and predict the effect at the output.

Let us first consider the telescopic op amp shown in Fig. 9.84. At relatively low frequencies, the cascode devices contribute negligible noise, leaving *M*1–*M*<sup>2</sup> and *M*7–*M*<sup>8</sup> as the primary noise sources. The input-referred noise voltage per unit bandwidth is therefore similar to that in Fig. 7.59(a) and given by

$$\overline{V\_n^2} = 4kT \left( 2 \frac{\mathcal{Y}}{\mathcal{g}\_{m1,2}} + 2 \frac{\mathcal{Y} \mathcal{g}\_{m7,8}}{\mathcal{g}\_{m1,2}^2} \right) + 2 \frac{K\_N}{(WL)\_{1,2} C\_{ox} f} + 2 \frac{K\_P}{(WL)\_{7,8} C\_{ox} f} \frac{\mathcal{g}\_{m7,8}^2}{\mathcal{g}\_{m1,2}^2} \tag{9.88}$$

where *KN* and *KP* denote the 1*/ f* noise coefficients of NMOS and PMOS devices, respectively.

Here is the image describtion:
```
The image depicts a schematic diagram of a telescopic operational amplifier (op-amp). The circuit consists of multiple Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFETs) arranged in a specific configuration to form the op-amp. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.

2. **Transistors:**
   - There are eight MOSFETs labeled \( M_1 \) through \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input transistors, with their gates connected to the input voltage \( V_{in} \).
   - \( M_3 \) and \( M_4 \) are connected in series with \( M_1 \) and \( M_2 \), respectively, and their gates are connected to a bias voltage \( V_{b1} \).
   - \( M_5 \) and \( M_6 \) are connected in series with \( M_3 \) and \( M_4 \), respectively, and their gates are connected to another bias voltage \( V_{b2} \).
   - \( M_7 \) and \( M_8 \) are connected in series with \( M_5 \) and \( M_6 \), respectively, and their gates are connected to a third bias voltage \( V_{b3} \).

3. **Current Source:**
   - There is a current source labeled \( I_{SS} \) connected to the source terminals of \( M_1 \) and \( M_2 \), providing a constant current to the circuit.

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the node between \( M_5 \) and \( M_6 \).

5. **Connections:**
   - The drain of \( M_1 \) is connected to the source of \( M_3 \), and the drain of \( M_2 \) is connected to the source of \( M_4 \).
   - The drain of \( M_3 \) is connected to the source of \( M_5 \), and the drain of \( M_4 \) is connected to the source of \( M_6 \).
   - The drain of \( M_5 \) is connected to the source of \( M_7 \), and the drain of \( M_6 \) is connected to the source of \( M_8 \).
   - The drains of \( M_7 \) and \( M_8 \) are connected to the power supply \( V_{DD} \).

The figure is labeled as "Figure 9.84 Noise in a telescopic op amp," indicating that the focus of the figure is on analyzing noise in this specific type of operational amplifier configuration.
```

Next, we study the noise behavior of the folded-cascode op amp of Fig. 9.85(a), considering only thermal noise at this point. Again, the noise of the cascode devices is negligible at low frequencies, leaving *M*1–*M*2, *M*7–*M*8, and *M*9–*M*<sup>10</sup> as potentially significant sources. Do both pairs *M*7–*M*<sup>8</sup> and *M*9–*M*<sup>10</sup> contribute noise? Using our simple rule, we change the gate voltage of *M*<sup>7</sup> by a small amount [Fig. 9.85(b)], noting that the output indeed changes considerably. The same observation applies to *M*8– *M*<sup>10</sup> as well. To determine the input-referred thermal noise, we first refer the noise of *M*7–*M*<sup>8</sup> to the

Here is the image describtion:
```
The image shows two diagrams labeled (a) and (b), which appear to be schematics of a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). 

### Diagram (a):
- **Transistors:**
  - **M1 and M2**: These are the input transistors, with their gates connected to the input voltage \( V_{in} \).
  - **M11**: This transistor is connected to the sources of M1 and M2, and its gate is grounded, indicating it is likely acting as a current source.
  - **M3, M4, M5, and M6**: These transistors form the differential pair and the active load. M3 and M4 are connected to the sources of M1 and M2, respectively, and their gates are connected to a bias voltage \( V_{b1} \). M5 and M6 are connected to the drains of M3 and M4, respectively, and their gates are connected to another bias voltage \( V_{b2} \).
  - **M7 and M8**: These transistors are connected in parallel to the drains of M5 and M6, respectively, and their gates are connected to a bias voltage \( V_{b3} \). They are connected to the power supply \( V_{DD} \).
  - **M9 and M10**: These transistors are connected to the sources of M3 and M4, respectively, and their gates are connected to a bias voltage \( V_{b4} \). They are connected to ground.
- **Connections:**
  - The output voltage \( V_{out} \) is taken from the common node between the drains of M5 and M6.
  - The circuit is powered by \( V_{DD} \) at the top and grounded at the bottom.

### Diagram (b):
- This diagram is similar to (a) but includes an additional symbol between the drain of M7 and the source of M8, which looks like a current source symbol with a plus and minus sign, indicating a controlled current source or a current mirror.
- The rest of the connections and components are the same as in diagram (a).

### General Description:
- The circuit is a differential amplifier with a current mirror load.
- The input differential pair (M1 and M2) amplifies the difference between the input signals.
- The current mirror formed by M7 and M8 ensures that the current through the differential pair is mirrored and provides high output impedance.
- The active loads (M5 and M6) and the current sources (M9, M10, and M11) help in setting the operating point and improving the gain of the amplifier.
- Bias voltages \( V_{b1}, V_{b2}, V_{b3}, \) and \( V_{b4} \) are used to set the operating points of the transistors.

This type of circuit is commonly used in analog integrated circuits for its high gain and differential operation, which helps in rejecting common-mode noise.
```

(b) **Figure 9.85** Noise in a folded-cascode op amp.

output:

$$\overline{\left|V\_{n,out}^2\right|}\Big|\_{M7,8} = 2\left(4kT\frac{\mathcal{V}}{\mathcal{g}\_{m7,8}}\mathcal{g}\_{m7,8}^2 R\_{out}^2\right) \tag{9.89}$$

where the factor 2 accounts for the (uncorrelated) noise of *M*<sup>7</sup> and *M*<sup>8</sup> and *Rout* denotes the open-loop output resistance of the op amp. Similarly,

$$\left. \overline{V\_{n,out}^2} \right|\_{M9,10} = 2 \left( 4kT \frac{\nu}{g\_{m9,10}} \mathbf{g}\_{m9,10}^2 \mathbf{R}\_{out}^2 \right) \tag{9.90}$$

Dividing these quantities by *g*<sup>2</sup> *m*1*,*2*R*<sup>2</sup> *out* and adding the contribution of *M*1–*M*2, we obtain the overall noise:

$$\overline{V\_{n,int}^2} = 8kT \left( \frac{\chi}{g\_{m1,2}} + \nu \frac{g\_{m7,8}}{g\_{m1,2}^2} + \nu \frac{g\_{m9,10}}{g\_{m1,2}^2} \right) \tag{9.91}$$

The effect of flicker noise can be included in a similar manner (Problem 9.15). Note that the foldedcascode topology potentially suffers from greater noise than its telescopic counterpart. In applications where flicker noise is critical, we opt for a PMOS-input op amp as PMOS transistors typically exhibit less flicker noise than do NMOS devices.

As observed for the differential amplifiers in Chapter 7, the noise contribution of the PMOS and NMOS current sources *increases* in proportion to their transconductance. This trend results in a tradeoff between output voltage swings and input-referred noise: for a given current, as implied by *gm* = 2*ID/(VG S* − *VT H )*, if the overdrive voltage of the current sources is minimized to allow large swings, then their transconductance is maximized.

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Power Supply and Ground:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top.
   - The ground is represented at the bottom of the circuit.

2. **Transistors:**
   - The circuit consists of eight MOSFETs labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) form the differential pair, with their sources connected together and to a current source \( I_{SS} \) that is connected to ground.
   - \( M_3 \) and \( M_4 \) are connected as active loads for the differential pair. Their sources are connected to \( V_{DD} \), and their gates are connected to a bias voltage \( V_b \).
   - \( M_5 \) and \( M_6 \) are connected as cascode transistors to improve the gain and output resistance. Their sources are connected to the drains of \( M_3 \) and \( M_4 \), respectively, and their gates are connected to \( V_b \).
   - \( M_7 \) and \( M_8 \) are connected as current sources or sinks, with their gates connected to \( V_b \) and their sources connected to ground.

3. **Inputs and Outputs:**
   - The input signal \( V_{in} \) is applied to the gate of \( M_1 \).
   - The output signals are taken from the drains of \( M_5 \) and \( M_6 \), labeled as \( V_{out1} \) and \( V_{out2} \), respectively.

4. **Biasing:**
   - The bias voltage \( V_b \) is used to set the operating point of the transistors \( M_3 \), \( M_4 \), \( M_5 \), \( M_6 \), \( M_7 \), and \( M_8 \).

5. **Operation:**
   - The differential pair \( M_1 \) and \( M_2 \) amplifies the difference between the input signal \( V_{in} \) and a reference voltage (typically ground or another input signal).
   - The current source \( I_{SS} \) ensures a constant current through the differential pair.
   - The active loads \( M_3 \) and \( M_4 \) convert the differential current into a differential voltage.
   - The cascode transistors \( M_5 \) and \( M_6 \) enhance the gain and output resistance of the amplifier.
   - The current sources \( M_7 \) and \( M_8 \) provide the necessary biasing currents for the cascode transistors.

Overall, this circuit is a typical example of a differential amplifier with cascode transistors to improve performance characteristics such as gain and output resistance.
```

**Figure 9.86** Noise in a two-stage op amp.

As another case, we calculate the input-referred thermal noise of the two-stage op amp shown in Fig. 9.86. Beginning with the second stage, we note that the noise current of *M*<sup>5</sup> and *M*<sup>7</sup> flows through *rO*5%*rO*7. Dividing the resulting output noise voltage by the total gain, *gm*1*(rO*1%*rO*3*)* × *gm*5*(rO*5%*rO*7*)*, and doubling the power, we obtain the input-referred contribution of *M*5–*M*8:

$$\left. \overline{V\_n^2} \right|\_{M\\$-8} = 2 \times 4kT \gamma \left( \mathbf{g}\_{m5} + \mathbf{g}\_{m7} \right) \left( r\_{O5} \| r\_{O7} \right)^2 \frac{1}{\mathbf{g}\_{m1}^2 (r\_{O1} \| r\_{O3})^2 \mathbf{g}\_{m5}^2 (r\_{O5} \| r\_{O7})^2} \tag{9.92}$$

$$\dot{\lambda} = 8kT\gamma \frac{\text{g}\_{m\text{S}} + \text{g}\_{m\text{7}}}{\text{g}\_{m1}^2 \text{g}\_{m\text{S}}^2 (r\_{O1} \| r\_{O3})^2} \tag{9.93}$$

The noise due to *M*1–*M*<sup>4</sup> is simply equal to

$$\left. \overline{V\_n^2} \right|\_{M1-4} = 2 \times 4kT \gamma \frac{\text{g}\_{m1} + \text{g}\_{m3}}{\text{g}\_{m1}^2} \tag{9.94}$$

It follows that

$$\overline{V\_{n,tot}^2} = 8kT\gamma \frac{1}{g\_{m1}^2} \left[ \mathbf{g}\_{m1} + \mathbf{g}\_{m3} + \frac{\mathbf{g}\_{m5} + \mathbf{g}\_{m7}}{g\_{m5}^2 (r\_{O1} \| r\_{O3})^2} \right] \tag{9.95}$$

Note that the noise resulting from the second stage is usually negligible because it is divided by the gain of the first stage when referred to the main input.

#### ▲**Example 9.26**

A simple amplifier is constructed as shown in Fig. 9.87. Note that the first stage incorporates diode-connected—rather than current-source—loads. Assuming that all of the transistors are in saturation and *(W/L)*1*,*<sup>2</sup> = 50*/*0*.*6*, (W/L)*3*,*<sup>4</sup> = 10*/*0*.*6, *(W/L)*5*,*<sup>6</sup> = 20*/*0*.*6, and *(W/L)*7*,*<sup>8</sup> = 56*/*0*.*6, calculate the input-referred noise voltage if *µnCox* = <sup>75</sup> *<sup>µ</sup>*A/V2, *<sup>µ</sup>pCox* <sup>=</sup> <sup>30</sup> *<sup>µ</sup>*A/V2, and <sup>γ</sup> <sup>=</sup> <sup>2</sup>*/*3.

Here is the image describtion:
```
The image depicts a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the circuit:

1. **Power Supply and Ground:**
   - The circuit is powered by a voltage source \( V_{DD} \) at the top.
   - The ground is represented at the bottom of the circuit.

2. **Transistors:**
   - The circuit consists of eight MOSFETs labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the current mirror transistors.
   - \( M_7 \) and \( M_8 \) are the tail current source transistors.

3. **Current Source:**
   - There is a current source \( I_{SS} \) providing a constant current of 0.5 mA, connected to the source terminals of \( M_1 \) and \( M_2 \).

4. **Connections:**
   - The drain of \( M_1 \) is connected to the drain of \( M_3 \), and the drain of \( M_2 \) is connected to the drain of \( M_4 \).
   - The sources of \( M_1 \) and \( M_2 \) are connected together and to the current source \( I_{SS} \).
   - The gates of \( M_3 \) and \( M_4 \) are connected to the drains of \( M_5 \) and \( M_6 \), respectively.
   - The sources of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The gates of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_3 \) and \( M_4 \), respectively, forming a current mirror.
   - The sources of \( M_5 \) and \( M_6 \) are connected to \( V_{DD} \).
   - The gates of \( M_7 \) and \( M_8 \) are connected to a bias voltage \( V_b \).
   - The sources of \( M_7 \) and \( M_8 \) are connected to ground.

5. **Inputs and Outputs:**
   - The input signal \( V_{in} \) is applied to the gate of \( M_1 \).
   - The output signals are taken from the drains of \( M_5 \) and \( M_6 \), labeled as \( V_{out1} \) and \( V_{out2} \), respectively.

6. **Operation:**
   - The differential pair \( M_1 \) and \( M_2 \) amplifies the difference between the input signals.
   - The current mirror formed by \( M_5 \) and \( M_6 \) ensures that the current through \( M_3 \) and \( M_4 \) is mirrored, providing a balanced load for the differential pair.
   - The tail current source \( I_{SS} \) sets the total current through the differential pair, ensuring stable operation.

This circuit is a typical example of a differential amplifier used in analog integrated circuits for amplifying the difference between two input signals while rejecting common-mode signals.
```

### **Solution**

We first calculate the small-signal gain of the first stage:

$$A\_{v1} \approx \frac{\mathcal{g}\_{m1}}{\mathcal{g}\_{m3}}\tag{9.96}$$

$$
\lambda = \sqrt{\frac{50 \times 75}{10 \times 30}}\tag{9.97}
$$

$$
\approx \mathbf{3.54} \tag{9.98}
$$

The noise of *<sup>M</sup>*<sup>5</sup> and *<sup>M</sup>*<sup>7</sup> referred to the gate of *<sup>M</sup>*<sup>5</sup> is equal to 4*kT (*2*/*3*)(gm*<sup>5</sup> <sup>+</sup> *gm*7*)/g*<sup>2</sup> *<sup>m</sup>*<sup>5</sup> <sup>=</sup> <sup>2</sup>*.*<sup>87</sup> <sup>×</sup> <sup>10</sup>−<sup>17</sup> <sup>V</sup>2/Hz, which is divided by *A*<sup>2</sup> *<sup>v</sup>*<sup>1</sup> when referred to the main input: *<sup>V</sup>*<sup>2</sup> *<sup>n</sup>* <sup>|</sup>*M*5*,*<sup>7</sup> <sup>=</sup> <sup>2</sup>*.*<sup>29</sup> <sup>×</sup> <sup>10</sup>−<sup>18</sup> V2/Hz. Transistors *<sup>M</sup>*<sup>1</sup> and *<sup>M</sup>*<sup>3</sup> produce an input-referred noise of *V*<sup>2</sup> *<sup>n</sup>* <sup>|</sup>*M*1*,*<sup>3</sup> <sup>=</sup> *(*8*kT/*3*)(gm*<sup>3</sup> <sup>+</sup> *gm*1*)/g*<sup>2</sup> *<sup>m</sup>*<sup>1</sup> <sup>=</sup> <sup>1</sup>*.*<sup>10</sup> <sup>×</sup> <sup>10</sup>−<sup>17</sup> V2/Hz. Thus, the total input-referred noise equals

$$\overline{V\_{n,in}^2} = 2(2.29 \times 10^{-18} + 1.10 \times 10^{-17})\tag{9.99}$$

$$=2.66 \times 10^{-17} \text{ V}^2/\text{Hz} \tag{9.100}$$

where the factor of 2 accounts for the noise produced by both odd-numbered and even-numbered transistors in the circuit. This value corresponds to an input noise voltage of 5.16 nV/√Hz.

The noise-power trade-off described in Chapter 7 is present in op amps as well. Specifically, the devices and bias currents in an op amp can be linearly scaled so as to trade power consumption for noise. For example, if all of the transistor widths and *ISS* in Fig. 9.87 are halved, then so is the power, while *V*2 *<sup>n</sup>,in* is doubled and the voltage gain and swings remain unchanged. This simple scaling can be applied to all of the op amps studied in this chapter. We exploit this principle in the nanometer op amps designed in Chapter 11.

# **References**

- [1] R. G. Eschauzier, L. P. T. Kerklaan, and J. H. Huising, "A 100-MHz 100-dB Operational Amplifier with Multipath Nested Miller Compensation Structure," *IEEE J. of Solid-State Circuits*, vol. 27, pp. 1709–1717, December 1992.
- [2] R. M. Ziazadeh, H. T. Ng, and D. J. Allstot, "A Multistage Amplifier Topology with Embedded Tracking Compensation," *CICC Proc.*, pp. 361–364, May 1998.

▲