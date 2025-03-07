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
The image depicts a schematic diagram of a multi-stage amplifier circuit, specifically a differential amplifier with a current mirror load. The circuit consists of several MOSFET transistors arranged in a specific configuration to achieve amplification.

Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a reference voltage.
   - **M3 and M4:** These transistors form the current mirror load for the differential pair. The gate of M3 is connected to a bias voltage \( V_{b1} \), and the gate of M4 is connected to the drain of M3.
   - **M5 and M6:** These transistors form another current mirror stage. The gate of M5 is connected to a bias voltage \( V_{b2} \), and the gate of M6 is connected to the drain of M5.
   - **M7 and M8:** These transistors form the final current mirror stage. The gate of M7 is connected to a bias voltage \( V_{b3} \), and the gate of M8 is connected to the drain of M7.

2. **Connections:**
   - The source of M1 and M2 are connected together and to a current source \( I_{SS} \) which is connected to the ground.
   - The drain of M1 is connected to the drain of M3, and the drain of M2 is connected to the drain of M4.
   - The source of M3 and M4 are connected to the drain of M5 and M6, respectively.
   - The source of M5 and M6 are connected to the drain of M7 and M8, respectively.
   - The source of M7 and M8 are connected to the power supply voltage \( V_{DD} \).

3. **Output:**
   - The output voltage \( V_{out} \) is taken from the connection between the drain of M6 and the source of M8.

4. **Bias Voltages:**
   - \( V_{b1} \), \( V_{b2} \), and \( V_{b3} \) are bias voltages applied to the gates of M3, M5, and M7, respectively, to set the operating points of the transistors.

This configuration is typically used in analog integrated circuits to provide high gain and good common-mode rejection ratio (CMRR). The current mirrors (M3-M4, M5-M6, and M7-M8) help in maintaining constant current through the differential pair and provide the necessary load for amplification.
```

Here is the image describtion:
```
The image is a caption that reads "Figure 9.1 Cascode op amp." This suggests that the image is likely part of a technical document or textbook, specifically in a section discussing a cascode operational amplifier (op amp). The caption indicates that the figure is the first one in chapter 9, and it is focused on illustrating or explaining a cascode op amp circuit. However, the actual image of the cascode op amp circuit is not provided here, only the caption describing it.
```

shown in Fig. 9.1 as a representative op amp design.<sup>1</sup> The voltages *Vb*1−*Vb*<sup>3</sup> are generated by the current mirror techniques described in Chapter 5.

**Gain** The open-loop gain of an op amp determines the precision of the feedback system employing the op amp. As mentioned before, the required gain may vary by four orders of magnitude according to the application. Trading with such parameters as speed and output voltage swings, the minimum required gain must therefore be known. As explained in Chapter 14, a high open-loop gain may also be necessary to suppress nonlinearity.

#### ▲**Example 9.1**

The circuit of Fig. 9.2 is designed for a nominal gain of 10, i.e., 1 + *R*1*/R*<sup>2</sup> = 10. Determine the minimum value of *A*<sup>1</sup> for a gain error of 1%.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) configuration. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1)**: The op-amp is represented by a triangle with two input terminals and one output terminal. The positive input terminal is marked with a plus sign (+), and the negative input terminal is marked with a minus sign (-). The output terminal is at the point of the triangle.

2. **Input Voltage (Vin)**: The input voltage (Vin) is applied to the positive input terminal of the op-amp.

3. **Resistor (R2)**: A resistor (R2) is connected between the negative input terminal of the op-amp and the ground. This resistor is used to set the reference voltage for the negative input.

4. **Resistor (R1)**: Another resistor (R1) is connected between the output terminal of the op-amp and the negative input terminal. This resistor is part of the feedback loop, which is essential for determining the gain and stability of the op-amp circuit.

5. **Output Voltage (Vout)**: The output voltage (Vout) is taken from the output terminal of the op-amp.

The circuit appears to be a non-inverting amplifier configuration, where the input signal is applied to the non-inverting input of the op-amp, and the feedback resistor (R1) and reference resistor (R2) help to set the gain of the amplifier.

The figure is labeled as "Figure 9.2" in the bottom right corner.
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
The image depicts a simple common-source amplifier stage, which is a basic configuration in analog electronics. The circuit consists of the following components:

1. **Transistor (M1)**: This is an N-channel MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor). The source of the MOSFET is connected to ground, the gate is connected to the input voltage \( V_{in} \), and the drain is connected to the resistor \( R_D \).

2. **Resistor (R_D)**: This resistor is connected between the drain of the MOSFET and the positive supply voltage \( V_{DD} \).

3. **Power Supply (V_{DD})**: This is the positive supply voltage connected to the top of the resistor \( R_D \).

4. **Input Voltage (V_{in})**: This is the input signal applied to the gate of the MOSFET.

5. **Output Voltage (V_{out})**: The output voltage is taken from the drain of the MOSFET, which is the point between the resistor \( R_D \) and the drain of the MOSFET.

The circuit operates as follows: The input voltage \( V_{in} \) controls the gate-source voltage of the MOSFET, which in turn controls the current flowing through the MOSFET from drain to source. This current creates a voltage drop across the resistor \( R_D \), and the output voltage \( V_{out} \) is taken from the drain of the MOSFET. The common-source configuration is known for providing voltage amplification.

The figure is labeled as "Figure 9.3 Simple common-source stage."
```

**Small-Signal Bandwidth** The high-frequency behavior of op amps plays a critical role in many applications. For example, as the frequency of operation increases, the open-loop gain begins to drop (Fig. 9.4), creating larger errors in the feedback system. The small-signal bandwidth is usually defined as the "unitygain" frequency, *fu*, which can reach several gigahertz in today's CMOS op amps. The 3-dB frequency, *f*3-dB, may also be specified to allow easier prediction of the closed-loop frequency response.

Here is the image describtion:
```
The image is a graph illustrating the gain roll-off with frequency. The x-axis represents the frequency on a logarithmic scale, denoted as \( f(\text{log axis}) \). The y-axis represents the gain in decibels, specifically \( 20 \log |A_V| \).

The graph starts with a flat line at a high gain level, indicating that the gain remains constant over a range of low frequencies. This flat region extends up to a point labeled \( f_{3-\text{dB}} \), where the gain begins to decrease. The point \( f_{3-\text{dB}} \) marks the frequency at which the gain has dropped by 3 decibels from its maximum value.

Beyond \( f_{3-\text{dB}} \), the graph shows a downward slope, indicating that the gain decreases as the frequency increases. This slope continues until it reaches a point labeled \( f_u \), where the gain approaches zero.

The graph is labeled as "Figure 9.4 Gain roll-off with frequency," indicating that it is part of a larger document or book, specifically in the ninth chapter.
```

▲**Example 9.2**

In the circuit of Fig. 9.5, assume that the op amp is a single-pole voltage amplifier. If *Vin* is a small step, calculate the time required for the output voltage to reach within 1% of its final value. What unity-gain bandwidth must the

Here is the image describtion:
```
The image consists of two parts: a circuit diagram on the left and a graph on the right.

1. **Circuit Diagram (Left Side):**
   - The circuit features an operational amplifier (op-amp) with the label "A(s)" inside the triangular symbol, indicating a frequency-dependent gain.
   - The non-inverting input (+) of the op-amp is connected to the input voltage \( V_{in} \).
   - The inverting input (-) of the op-amp is connected to a resistor \( R_1 \), which is then connected to the output voltage \( V_{out} \).
   - The inverting input is also connected to a resistor \( R_2 \), which is grounded.
   - This configuration suggests a non-inverting amplifier with feedback.

2. **Graph (Right Side):**
   - The graph plots voltage against time (t).
   - The input voltage \( V_{in} \) is shown as a step function, where it suddenly increases from a lower value to a higher value at time \( t = 0 \).
   - The output voltage \( V_{out} \) starts at a lower value and then gradually increases, following an exponential curve, until it reaches a steady state that matches the new level of \( V_{in} \).
   - This indicates the response of the output voltage \( V_{out} \) to a step change in the input voltage \( V_{in} \), showing the characteristic behavior of the op-amp circuit in response to a step input.

Overall, the image illustrates a non-inverting op-amp circuit and its step response, highlighting how the output voltage \( V_{out} \) reacts over time to a sudden change in the input voltage \( V_{in} \).
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
The image contains two circuit diagrams labeled (a) and (b), which appear to be differential amplifier circuits.

**Circuit (a):**
- This is a single-ended differential amplifier.
- It consists of four MOSFETs labeled M1, M2, M3, and M4.
- The input signal \( V_{in} \) is applied to the gate of M1.
- M1 and M2 form the differential pair, with their sources connected together and to a current source \( I_{SS} \) that is connected to ground.
- The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
- M3 and M4 are connected in a current mirror configuration, with their gates tied together and connected to the drain of M3.
- The drain of M4 is connected to the positive supply voltage \( V_{DD} \).
- The output voltage \( V_{out} \) is taken from the drain of M2.
- A load capacitor \( C_L \) is connected between \( V_{out} \) and ground.

**Circuit (b):**
- This is a fully differential amplifier.
- It also consists of four MOSFETs labeled M1, M2, M3, and M4.
- The input signals \( V_{in1} \) and \( V_{in2} \) are applied to the gates of M1 and M2, respectively.
- M1 and M2 form the differential pair, with their sources connected together and to a current source \( I_{SS} \) that is connected to ground.
- The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
- M3 and M4 are connected in a current mirror configuration, with their gates tied together and connected to a bias voltage \( V_b \).
- The drain of M4 is connected to the positive supply voltage \( V_{DD} \).
- The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drains of M1 and M2, respectively.
- Load capacitors \( C_L \) are connected between \( V_{out1} \) and ground, and \( V_{out2} \) and ground.

Both circuits use a current source \( I_{SS} \) to set the tail current for the differential pairs. The main difference between the two circuits is that (a) is a single-ended output configuration, while (b) is a fully differential output configuration.
```

**Figure 9.6** Simple op amp topologies.

The circuits of Fig. 9.6 suffer from noise contributions of *M*1–*M*4, as calculated in Chapter 7. Interestingly, in all op amp topologies, at least four devices contribute to the input noise: two input transistors and two "load" transistors.

#### ▲**Example 9.4**

Calculate the input common-mode voltage range and the closed-loop output impedance of the unity-gain buffer depicted in Fig. 9.7.

Here is the image describtion:
```
The image consists of two diagrams labeled as Figure 9.7. 

On the left side, there is a simple operational amplifier (op-amp) circuit. The op-amp is represented by a triangle with a positive input (+) and a negative input (-). The positive input is connected to a voltage source labeled \( V_{in} \). The output of the op-amp is labeled \( V_{out} \). There is a feedback loop from the output back to the negative input of the op-amp.

On the right side, there is a more complex circuit diagram. This circuit includes four MOSFET transistors labeled \( M_1 \), \( M_2 \), \( M_3 \), and \( M_4 \). The circuit is powered by a voltage source \( V_{DD} = 1V \) at the top. The input voltage \( V_{in} \) is connected to the gate of transistor \( M_1 \). The source of \( M_1 \) is connected to a current source labeled \( I_{SS} \) which is grounded. The drain of \( M_1 \) is connected to the drain of \( M_3 \). The gate of \( M_3 \) is connected to its drain, forming a diode-connected transistor. The source of \( M_3 \) is connected to \( V_{DD} \). 

Similarly, the gate of \( M_2 \) is connected to the input voltage \( V_{in} \), and its source is connected to the current source \( I_{SS} \). The drain of \( M_2 \) is connected to the drain of \( M_4 \). The gate of \( M_4 \) is connected to its drain, forming another diode-connected transistor. The source of \( M_4 \) is connected to \( V_{DD} \). The output voltage \( V_{out} \) is taken from the connection between the drains of \( M_2 \) and \( M_4 \).

Overall, the image shows a basic op-amp circuit and a more detailed MOSFET-based differential amplifier circuit.
```

### **Solution**

Razavi-3930640 book December 17, 201516:59 350

The minimum allowable input voltage is equal to *VISS* + *VG S*1, where *VISS* is the voltage required across the current source. The maximum voltage is given by the level that places *M*<sup>1</sup> at the edge of the triode region: *Vin,max* = *VDD* − |*VG S*<sup>3</sup>| + *VT H*1. For example, if each device (including the current source) has a threshold voltage of 0.3 V and an overdrive of 0.1 V, then *Vin,min* = 0*.*1 + 0*.*1 + 0*.*3 = 0*.*5 V and *Vin,max* = 1 − *(*0*.*1 + 0*.*3*)* + 0*.*3 = 0*.*9 V. Thus, the input CM range equals 0.4 V with a 1-V supply.

Since the circuit employs voltage feedback at the output, the output impedance is equal to the open-loop value, *rO P* %*rO N* , divided by one plus the loop gain, 1 + *gmN (rO P* %*rO N )*. In other words, for large open-loop gain, the closed-loop output impedance is approximately equal to *(rO P* %*rO N )/*[*gmN (rO P* %*rO N )*] = 1*/gmN* .

It is interesting to note that the closed-loop output impedance is relatively *independent* of the open-loop output impedance. This is an important observation, allowing us to design high-gain op amps by *increasing* the open-loop output impedance while still achieving a relatively low closed-loop output impedance. We also observe that, if driving a load capacitance of *CL* , the op amp incurs a closed-loop output pole approximately given by *gmN /CL* . ▲

In order to achieve a high gain, the differential cascode topologies of Chapters 4 and 5 can be used. Shown in Figs. 9.8(a) and (b) for single-ended and differential output generation, respectively, such circuits display a gain on the order of *gmN* [*(gmNr* <sup>2</sup> *O N )*%*(gm Pr* <sup>2</sup> *O P )*], but at the cost of output swing and

Here is the image describtion:
```
The image contains two circuit diagrams labeled (a) and (b), each representing a different configuration of a multi-stage amplifier circuit.

### Circuit (a):
- **Transistors:**
  - There are eight transistors labeled M1 to M8.
  - M1 and M2 are at the bottom, connected to the input voltage \( V_{in} \) and a current source \( I_{SS} \) to ground.
  - M3 and M4 are connected above M1 and M2, respectively, with their gates connected to a bias voltage \( V_b \).
  - M5 and M6 are connected above M3 and M4, respectively, with their sources connected to the drains of M3 and M4.
  - M7 and M8 are at the top, connected to the power supply \( V_{DD} \), with their sources connected to the drains of M5 and M6.
- **Connections:**
  - The output voltage \( V_{out} \) is taken from the node between the drains of M6 and M4.
  - Nodes X and Y are intermediate nodes between the stages.
  - The gates of M5 and M6 are connected to nodes X and Y, respectively.

### Circuit (b):
- **Transistors:**
  - Similar to circuit (a), there are eight transistors labeled M1 to M8.
  - M1 and M2 are at the bottom, connected to the input voltage \( V_{in} \) and a current source \( I_{SS} \) to ground.
  - M3 and M4 are connected above M1 and M2, respectively, with their gates connected to a bias voltage \( V_{b1} \).
  - M5 and M6 are connected above M3 and M4, respectively, with their gates connected to a different bias voltage \( V_{b2} \).
  - M7 and M8 are at the top, connected to the power supply \( V_{DD} \), with their gates connected to yet another bias voltage \( V_{b3} \).
- **Connections:**
  - The output voltage \( V_{out} \) is taken from the node between the drains of M6 and M4.
  - The gates of M5 and M6 are connected to \( V_{b2} \), and the gates of M7 and M8 are connected to \( V_{b3} \).

### Summary:
Both circuits are multi-stage amplifiers with different biasing configurations. Circuit (a) uses a single bias voltage \( V_b \) for the gates of M3 and M4, while circuit (b) uses three different bias voltages \( V_{b1} \), \( V_{b2} \), and \( V_{b3} \) for the gates of M3, M4, M5, M6, M7, and M8. The output voltage \( V_{out} \) is taken from the same node in both circuits.
```

**Figure 9.8** Cascode op amps.

additional poles. These configurations are also called "telescopic" cascode op amps to distinguish them from another cascode op amp described below. The circuit providing a single-ended output suffers from a mirror pole at node *X* (and a pole at *Y* ), creating stability issues (Chapter 10).

As calculated in Chapter 4 , the output swings of telescopic op amps are relatively limited. In the fully differential version of Fig. 9.8(b), for example, the output swing is given by 2[*VDD* − *(VO D*<sup>1</sup> + *VO D*<sup>3</sup> + *VISS* + |*VO D*5|+|*VO D*7|*)*], where *VODj* denotes the overdrive voltage of *Mj* and *VISS* the minimum allowable voltage across *ISS*. We must recognize the three conditions necessary for allowing this much swing: (1) the input CM level, *Vin,C M* , is chosen *low* enough and equal to *VG S*<sup>1</sup> + *VISS*, (2) *Vb*<sup>1</sup> is also chosen low enough and equal to *VG S*<sup>3</sup> + *(Vin,C M* − *VT H*1*)*, placing *M*<sup>1</sup> at the edge of saturation, and (3) *Vb*<sup>2</sup> is chosen high enough and equal to *VDD* − |*VO D*7| − |*VG S*5|, placing *M*<sup>7</sup> at the edge of saturation. Thus, *Vin,C M* (and *Vb*<sup>1</sup> and *Vb*2) must be controlled tightly, a serious issue.

Another drawback of telescopic cascodes is the difficulty in shorting their inputs and outputs, e.g., to implement a unity-gain buffer similar to the circuit of Fig. 9.7. To understand the issue, let us consider the unity-gain feedback topology shown in Fig. 9.9. Under what conditions are both *M*<sup>2</sup> and *M*<sup>4</sup> in saturation? We must have *Vout* ≤ *VX* +*VT H*<sup>2</sup> and *Vout* ≥ *Vb* −*VT H*4. Since *VX* = *Vb* −*VG S*4, *Vb* −*VT H*<sup>4</sup> ≤ *Vout* ≤ *Vb* − *VG S*<sup>4</sup> + *VT H*2. Depicted in Fig. 9.9, this voltage range is simply equal to *Vmax* − *Vmin* = *VT H*<sup>4</sup> − *(VG S*<sup>4</sup> − *VT H*2*)* (one threshold minus one overdrive), maximized by minimizing the overdrive of *M*<sup>4</sup> but always less than *VT H*2.

Here is the image describtion:
```
The image consists of two main parts: a circuit diagram on the left and a graphical representation of an allowable range on the right.

### Circuit Diagram (Left Side):
- **Components:**
  - The circuit is a telescopic cascode operational amplifier (op-amp).
  - It includes eight MOSFET transistors labeled M1 through M8.
  - A current source labeled Iss is connected to the source of M1 and M2.
  - The power supply voltage is labeled VDD at the top.
  - The bias voltage is labeled Vb.
  - The input voltage is labeled Vin and is connected to the gate of M1.
  - The output voltage is labeled Vout and is taken from the drain of M6.
  - The node X is the connection point between the drain of M4 and the source of M6.

- **Connections:**
  - M1 and M2 form the differential pair with their sources connected to the current source Iss.
  - The gates of M3 and M4 are connected to the bias voltage Vb.
  - The drains of M3 and M4 are connected to the sources of M5 and M6, respectively.
  - The gates of M5 and M6 are connected to the drains of M7 and M8, respectively.
  - The sources of M7 and M8 are connected to VDD.
  - The drains of M5 and M6 are connected to the sources of M7 and M8, respectively.

### Graphical Representation (Right Side):
- **Allowable Range:**
  - The graph shows the allowable range for the voltage at node X.
  - The vertical axis represents voltage levels.
  - The top of the allowable range is defined by Vb.
  - The bottom of the allowable range is defined by Vb - VTH4.
  - The height of the allowable range is given by VGS4 - VTH2.
  - VTH4 and VTH2 are the threshold voltages for transistors M4 and M2, respectively.

### Figure Caption:
- The caption below the image reads: "Figure 9.9 Telescopic cascode op amp with input and output shorted."

This image illustrates the structure and operating constraints of a telescopic cascode operational amplifier, highlighting the importance of maintaining the voltage at node X within a specific range to ensure proper operation.
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
The image consists of four subfigures labeled (a), (b), (c), and (d), and is identified as Figure 9.10.

(a) The first subfigure (a) shows a schematic diagram of an operational amplifier (op-amp) circuit. The op-amp has two input resistors, \( R_1 \) and \( R_2 \), connected to its inverting (-) and non-inverting (+) inputs, respectively. The feedback network consists of resistors \( R_3 \) and \( R_4 \), which are connected between the output and the inverting input, and between the inverting input and ground, respectively.

(b) The second subfigure (b) depicts a MOSFET-based circuit. It includes four MOSFETs labeled \( M_1 \), \( M_2 \), \( M_3 \), and \( M_4 \). The gates of \( M_1 \) and \( M_2 \) are connected to the input signal through a resistor \( R_1 \). The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_b \) through a resistor \( R_3 \). The sources of \( M_1 \) and \( M_2 \) are connected to a current source that is grounded. The drains of \( M_1 \) and \( M_3 \) are connected to node X, while the drains of \( M_2 \) and \( M_4 \) are connected to node Y. The output is taken from nodes X and Y through capacitors.

(c) The third subfigure (c) shows a waveform labeled \( V_X \) as a function of time \( t \). The waveform is a sinusoidal signal centered around a common-mode voltage \( V_{CM} \). The lower part of the waveform is labeled with the voltage \( V_b - V_{TH3,4} \), indicating the threshold voltage of transistors \( M_3 \) and \( M_4 \). The region where \( M_3 \) and \( M_4 \) are in the triode region is indicated.

(d) The fourth subfigure (d) also shows a waveform labeled \( V_X \) as a function of time \( t \). This waveform is similar to the one in (c) but includes an additional voltage level labeled \( V_b - (V_{GS3,4} - V_{TH1,2}) \), indicating the gate-source voltage of transistors \( M_3 \) and \( M_4 \) minus the threshold voltage of transistors \( M_1 \) and \( M_2 \).

Overall, the image appears to illustrate the behavior of an op-amp circuit and a MOSFET-based circuit, along with their respective voltage waveforms under certain conditions.
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
The image depicts a schematic diagram of a CMOS operational amplifier circuit. The circuit consists of multiple MOSFET transistors arranged in a specific configuration to achieve amplification. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **Mb1 and Mb2:** These are biasing transistors connected to the current sources \( I_{REF1} \) and \( I_{REF2} \) respectively.
   - **M1, M2, M3, and M4:** These transistors form the differential pair and the active load of the amplifier. M1 and M2 are the input transistors, with M1 receiving the input voltage \( V_{in} \). M3 and M4 are the load transistors.
   - **M5 and M6:** These transistors are part of the second stage of the amplifier, providing additional gain.
   - **M7 and M8:** These transistors are connected to the power supply \( V_{DD} \) and form the output stage of the amplifier.
   - **M9:** This transistor is connected to the source of M2 and is grounded.

2. **Connections:**
   - The gates of M1 and M2 are connected to the input voltage \( V_{in} \) and a bias voltage \( V_{b1} \) respectively.
   - The drains of M1 and M2 are connected to the sources of M3 and M4 respectively.
   - The gates of M3 and M4 are connected to a bias voltage \( V_{b1} \).
   - The drains of M3 and M4 are connected to the sources of M5 and M6 respectively.
   - The gates of M5 and M6 are connected to a bias voltage \( V_{b2} \).
   - The drains of M5 and M6 are connected to the sources of M7 and M8 respectively.
   - The gates of M7 and M8 are connected to the power supply \( V_{DD} \).
   - The output voltage \( V_{out} \) is taken from the node between the drains of M5 and M6.

3. **Biasing:**
   - The current sources \( I_{REF1} \) and \( I_{REF2} \) provide the necessary biasing currents for the transistors.
   - The bias voltages \( V_{b1} \) and \( V_{b2} \) are used to set the operating points of the transistors.

4. **Nodes:**
   - Node X is the connection point between the drain of M3 and the source of M5.
   - Node Y is the connection point between the drain of M4 and the source of M6.
   - The output voltage \( V_{out} \) is taken from the node between X and Y.

Overall, this circuit is a typical example of a multi-stage CMOS operational amplifier, designed to provide high gain and drive capability.
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
The image is a schematic diagram of a circuit used for the generation of cascode gate voltage. The circuit consists of several MOSFET transistors and current sources. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors connected in parallel. The source of M1 is connected to a current source labeled \( I_{SS} \) which is grounded. The source of M2 is also connected to the same node as M1.
   - **M3 and M4:** These are PMOS transistors connected in parallel. The source of M3 is connected to the drain of M1, and the source of M4 is connected to the drain of M2.
   - **Mb1:** This is an NMOS transistor with its source connected to the same node as the sources of M1 and M2. The gate of Mb1 is connected to its drain, which is also connected to the gates of M3 and M4.

2. **Current Sources:**
   - **I1:** This current source is connected between the drain of M3 and the positive supply voltage \( V_{DD} \).
   - **I_{SS}:** This current source is connected between the sources of M1, M2, and Mb1, and ground.

3. **Voltage Nodes:**
   - **V_{DD}:** The positive supply voltage.
   - **Vb1:** The voltage at the gate of M3 and M4, which is also the drain of Mb1.
   - **P:** The node where the sources of M1, M2, and Mb1 are connected.

The circuit is labeled as "Figure 9.12 Generation of cascode gate voltage." The purpose of this circuit is to generate a stable gate voltage for the cascode transistors (M3 and M4) to improve the performance of the amplifier by increasing the output resistance and gain.
```

### **9.2.4 Folded-Cascode Op Amps**

In order to alleviate the drawbacks of telescopic cascode op amps, namely, limited output swings and difficulty in choosing equal input and output CM levels, a "folded-cascode" op amp can be used. As described in Chapter 3 and illustrated in Fig. 9.13, in an NMOS or PMOS cascode amplifier, the input device is replaced by the opposite type while still converting the input voltage to a current. In the four circuits shown in Fig. 9.13, the small-signal current generated by *M*<sup>1</sup> flows through *M*<sup>2</sup> and subsequently the load, producing an output voltage approximately equal to *gm*1*RoutVin*. The primary advantage of the folded structure lies in the choice of the voltage levels because it does not "stack" the cascode transistor on top of the input device. We will return to this point later.

The folding idea depicted in Fig. 9.13 can easily be applied to differential pairs, and hence to operational amplifiers as well. Shown in Fig. 9.14, the resulting circuit replaces the input NMOS pair with a PMOS counterpart. Note two important differences between the two circuits. (1) In Fig. 9.14(a), one bias current, *ISS*, provides the drain current of both the input transistors and the cascode devices, whereas in Fig. 9.14(b), the input pair requires an additional bias current. In other words, *ISS*<sup>1</sup> = *ISS/*2+ *ID*<sup>3</sup> = *ISS/*2+ *I*1. Thus, the folded-cascode configuration generally consumes more power. (2) In Fig. 9.14(a), the input CM level

Here is the image describtion:
```
The image consists of two parts, labeled (a) and (b), each showing a sequence of circuit diagrams with MOSFET transistors and current sources. 

In part (a):
1. The first diagram shows a simple MOSFET circuit with two transistors, M1 and M2, and a current source I1. The source of M1 is connected to ground, its gate is connected to the input voltage Vin, and its drain is connected to the source of M2. The gate of M2 is connected to a bias voltage Vb, and its drain is connected to the current source I1, which is connected to the supply voltage VDD. The output voltage Vout is taken from the drain of M2.
2. An arrow points to the right, indicating a transformation or modification of the circuit.
3. The second diagram shows a similar configuration but with an additional current source I2 connected to the source of M2 and ground. The rest of the connections remain the same as in the first diagram.

In part (b):
1. The first diagram shows a different configuration with two MOSFET transistors, M1 and M2, and a current source I1. The source of M1 is connected to ground, its gate is connected to the input voltage Vin, and its drain is connected to the source of M2. The gate of M2 is connected to a bias voltage Vb, and its drain is connected to the current source I1, which is connected to the supply voltage VDD. The output voltage Vout is taken from the source of M2.
2. An arrow points to the right, indicating a transformation or modification of the circuit.
3. The second diagram shows a similar configuration but with an additional current source I2 connected to the drain of M2 and the supply voltage VDD. The rest of the connections remain the same as in the first diagram.

Overall, the image illustrates the transformation of MOSFET circuits by adding additional current sources to the existing configurations.
```

**Figure 9.13** Folded-cascode amplifiers.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), which appear to be different configurations of a differential amplifier circuit.

**Diagram (a):**
- The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.
- There are two current sources, \( I_1 \) and \( I_2 \), connected to the \( V_{DD} \) line.
- The output voltage \( V_{out} \) is taken from the node between \( I_1 \) and \( I_2 \).
- The circuit includes four MOSFET transistors labeled \( M_1 \), \( M_2 \), \( M_3 \), and \( M_4 \).
- The gates of \( M_1 \) and \( M_2 \) are connected to the input voltage \( V_{in} \).
- The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_{b1} \).
- The sources of \( M_1 \) and \( M_2 \) are connected together and to a current source \( I_{SS} \) which is grounded.

**Diagram (b):**
- This circuit is also powered by a voltage source \( V_{DD} \) at the top.
- Similar to diagram (a), there are two current sources \( I_1 \) and \( I_2 \) connected to the \( V_{DD} \) line.
- The output voltage \( V_{out} \) is taken from the node between \( I_1 \) and \( I_2 \).
- The circuit includes four MOSFET transistors labeled \( M_1 \), \( M_2 \), \( M_3 \), and \( M_4 \).
- The gates of \( M_1 \) and \( M_2 \) are connected to the input voltage \( V_{in} \).
- The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_{b1} \).
- The sources of \( M_1 \) and \( M_2 \) are connected together and to a current source \( I_{SS} \) which is connected to \( V_{DD} \).
- Additionally, there are two more current sources \( I_{SS1} \) and \( I_{SS2} \) connected to the sources of \( M_3 \) and \( M_4 \) respectively, and these current sources are grounded.

The main difference between the two diagrams is the configuration of the current sources and the connections of the MOSFET transistors. Diagram (b) appears to be a more complex version of diagram (a) with additional current sources \( I_{SS1} \) and \( I_{SS2} \).
```

**Figure 9.14** (a) Telescopic and (b) folded-cascode op amp topologies.

cannot exceed *Vb*<sup>1</sup> − *VG S*<sup>3</sup> + *VT H*1, whereas in Fig. 9.14(b), it cannot be *less* than *Vb*<sup>1</sup> − *VG S*<sup>3</sup> − |*VTHP* |. It is therefore possible to design the latter to allow shorting its input and output terminals with negligible swing limitation. This is in contrast to the behavior depicted in Fig. 9.9. In Fig. 9.14(b), it is possible to tie the *n*-wells of *M*<sup>1</sup> and *M*<sup>2</sup> to their common source point. We return to this idea in Chapters 14 and 19.

Let us now calculate the maximum output voltage swing of the folded-cascode op amp shown in Fig. 9.15, where *M*5–*M*<sup>10</sup> replace the ideal current sources of Fig. 9.14(b). With proper choice of *Vb*<sup>1</sup> and *Vb*2, the lower end of the swing is given by *VO D*<sup>3</sup> + *VO D*<sup>5</sup> and the upper end by *VDD* −*(*|*VO D*7|+|*VO D*9|*)*. Thus, the peak-to-peak swing on each side is equal to *VDD* − *(VO D*<sup>3</sup> + *VO D*<sup>5</sup> + |*VO D*7|+|*VO D*9|*)*. In the telescopic cascode of Fig. 9.14(a), on the other hand, the swing is less by the overdrive of the tail current source. We should nonetheless note that, carrying a large current, *M*<sup>5</sup> and *M*<sup>6</sup> in Fig. 9.15 may require a high overdrive voltage if their capacitance contribution to nodes *X* and *Y* is to be minimized.

We now determine the small-signal voltage gain of the folded-cascode op amp of Fig. 9.15. Using the half circuit depicted in Fig. 9.16(a) and writing |*Av*| = *Gm Rout*, we must calculate *Gm* and *Rout*. As shown in Fig. 9.16(b), the output short-circuit current is approximately equal to the drain current of *M*<sup>1</sup> because the impedance seen looking into the source of *<sup>M</sup>*3, that is, *(gm*<sup>3</sup> <sup>+</sup> *gmb*3*)*−<sup>1</sup>%*rO*3, is typically much lower than *rO*1%*rO*5. Thus, *Gm* ≈ *gm*1. To calculate *Rout*, we use Fig. 9.16(c), with *RO P* ≈ *(gm*<sup>7</sup> + *gmb*7*)rO*7*rO*9, to write *Rout* ≈ *RO P* %[*(gm*<sup>3</sup> + *gmb*3*)rO*3*(rO*1%*rO*5*)*]. It follows that

$$|A\_v| \approx g\_{m1} \{ [(g\_{m3} + g\_{mb3})r\_{O3}(r\_{O1} \| r\_{O5})] \} \| [(g\_{m7} + g\_{mb7})r\_{O7}r\_{O9}] \} \tag{9.17}$$

Here is the image describtion:
```
The image depicts a complex CMOS (Complementary Metal-Oxide-Semiconductor) operational amplifier circuit. Here is a detailed description of the circuit:

1. **Transistors:**
   - The circuit consists of ten MOSFET transistors labeled M1 through M10.
   - M1 and M2 are NMOS transistors at the input stage.
   - M3, M4, M5, and M6 are also NMOS transistors.
   - M7, M8, M9, and M10 are PMOS transistors.

2. **Current Source:**
   - There is a current source labeled Iss connected to the source of M1 and M2.

3. **Voltage Inputs:**
   - The input voltage is labeled Vin and is applied to the gate of M1.
   - The gate of M2 is connected to a reference voltage.

4. **Bias Voltages:**
   - The circuit has four bias voltages labeled Vb1, Vb2, Vb3, and Vb4.
   - Vb1 is connected to the gates of M3 and M4.
   - Vb2 is connected to the gates of M7 and M8.
   - Vb3 is connected to the gates of M9 and M10.
   - Vb4 is connected to the gates of M5 and M6.

5. **Power Supply:**
   - The circuit is powered by a supply voltage labeled VDD at the top.

6. **Connections:**
   - The drain of M1 is connected to the drain of M3 at node X.
   - The drain of M2 is connected to the drain of M4 at node Y.
   - The sources of M3 and M4 are connected to the drains of M5 and M6, respectively.
   - The sources of M5 and M6 are connected to ground.
   - The sources of M7 and M8 are connected to the drains of M3 and M4, respectively.
   - The sources of M9 and M10 are connected to the drains of M7 and M8, respectively.
   - The output voltage Vout is taken from the common node between the drains of M7 and M8.

7. **Ground:**
   - The sources of M5 and M6 are connected to ground.

This circuit is likely a multi-stage amplifier with differential input (M1 and M2) and multiple current mirrors (M3-M6, M7-M10) to provide high gain and proper biasing. The output is taken from the middle stage, indicating a possible high-gain configuration suitable for operational amplifier applications.
```

**Figure 9.15** Folded-cascode op amp with cascode PMOS loads.

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each diagram features a combination of MOSFET transistors and resistors, and they appear to be variations of a common-source amplifier with different configurations.

### Diagram (a):
- **Transistors**: There are four MOSFET transistors labeled M1, M3, M7, and M9.
  - M1 is an NMOS transistor with its gate connected to the input voltage \( V_{in} \), its source connected to ground, and its drain connected to node X.
  - M3 is a PMOS transistor with its gate connected to a bias voltage \( V_{b1} \), its source connected to node X, and its drain connected to node \( V_{out} \).
  - M7 is a PMOS transistor with its gate connected to a bias voltage \( V_{b2} \), its source connected to \( V_{out} \), and its drain connected to the drain of M9.
  - M9 is a PMOS transistor with its gate connected to a bias voltage \( V_{b3} \), its source connected to \( V_{DD} \), and its drain connected to the drain of M7.
- **Resistors**: There is a resistor labeled \( r_{o5} \parallel r_{o1} \) connected between node X and ground.
- **Power Supply**: The circuit is powered by a voltage source \( V_{DD} \).

### Diagram (b):
- **Transistors**: There are two MOSFET transistors labeled M1 and M3.
  - M1 is an NMOS transistor with its gate connected to the input voltage \( V_{in} \), its source connected to ground, and its drain connected to node X.
  - M3 is a PMOS transistor with its gate connected to a bias voltage \( V_{b1} \), its source connected to node X, and its drain connected to the output current \( I_{out} \).
- **Resistors**: There is a resistor labeled \( r_{o5} \parallel r_{o1} \) connected between node X and ground.

### Diagram (c):
- **Transistors**: There are two MOSFET transistors labeled M1 and M3.
  - M1 is an NMOS transistor with its gate connected to the input voltage \( V_{in} \), its source connected to ground, and its drain connected to node X.
  - M3 is a PMOS transistor with its gate connected to a bias voltage \( V_{b1} \), its source connected to node X, and its drain connected to the output resistance \( R_{out} \).
- **Resistors**: There are two resistors:
  - One labeled \( r_{o5} \parallel r_{o1} \) connected between node X and ground.
  - Another labeled \( R_{OP} \) connected between the drain of M3 and the power supply \( V_{DD} \).

### Common Elements:
- **Node X**: In all three diagrams, node X is a common point where the drain of M1 and the source of M3 are connected.
- **Bias Voltages**: Each diagram uses bias voltages \( V_{b1} \), \( V_{b2} \), and \( V_{b3} \) to control the gates of the PMOS transistors.
- **Resistor \( r_{o5} \parallel r_{o1} \)**: This resistor configuration is present in all three diagrams, connected between node X and ground.

These circuits are likely used in analog signal processing, with each configuration serving a different purpose in terms of amplification and output characteristics.
```

**Figure 9.16** (a) Half circuit of folded cascode op amp, (b) equivalent circuit for *Gm* calculation, and (c) equivalent circuit for *Rout* calculation.

The reader is encouraged to repeat this calculation without neglecting the current drawn by *rO*5||*rO*<sup>1</sup> in Fig. 9.16(b).

How does this value compare with the gain of a telescopic op amp? For comparable device dimensions and bias currents, the PMOS input differential pair exhibits a lower transconductance than does an NMOS pair. Furthermore, *rO*<sup>1</sup> and *rO*<sup>5</sup> appear in parallel, reducing the output impedance, especially because *M*<sup>5</sup> carries the currents of both the input device and the cascode branch. As a consequence, the gain in (9.17) is usually two to three times lower than that of a comparable telescopic cascode.

It is also worth noting that the pole at the "folding point," i.e., the sources of *M*<sup>3</sup> and *M*4, is quite closer to the origin than that associated with the source of cascode devices in a telescopic topology. In Fig. 9.17(a), *Ctot* arises from *CG S*3*,CSB*3*,CDB*1, and *CG D*1. By contrast, in Fig. 9.17(b), *Ctot* contains additional contributions due to *CG D*<sup>5</sup> and *CDB*5, typically significant components because *M*<sup>5</sup> must be wide enough to carry a large current with a small overdrive.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), each depicting different configurations of transistor-based circuits.

**Diagram (a):**
- The circuit features three main components: two transistors (M1 and M3) and a current source (Iss).
- The transistor M1 is an NMOS transistor with its gate connected to the input voltage (Vin), its source connected to the current source (Iss), and its drain connected to the drain of transistor M3.
- The transistor M3 is a PMOS transistor with its gate connected to a bias voltage (Vb) and its source connected to a higher potential (likely Vdd, though not explicitly shown).
- The drain of M3 is connected to the drain of M1 and also to a capacitor (Ctot) which is connected to ground.
- The current source (Iss) is connected between the source of M1 and ground.

**Diagram (b):**
- This circuit also features three transistors (M1, M3, and M5) and a current source (Iss).
- The transistor M1 is an NMOS transistor with its gate connected to the input voltage (Vin), its source connected to ground, and its drain connected to the current source (Iss).
- The current source (Iss) is connected between the drain of M1 and a higher potential (likely Vdd, though not explicitly shown).
- The transistor M3 is a PMOS transistor with its gate connected to a bias voltage (Vb1), its source connected to the drain of M1, and its drain connected to a node that also connects to the capacitor (Ctot) and the drain of transistor M5.
- The transistor M5 is an NMOS transistor with its gate connected to another bias voltage (Vb4), its source connected to ground, and its drain connected to the node shared with the drain of M3 and one terminal of the capacitor (Ctot).
- The capacitor (Ctot) is connected between this shared node and ground.

Both diagrams illustrate different configurations of transistor circuits, likely used for analog signal processing or amplification purposes, with specific biasing and current source arrangements.
```

**Figure 9.17** Effect of device capacitance on the nondominant pole in telescopic and folded-cascode op amps.

A folded-cascode op amp may incorporate NMOS input devices and PMOS cascode transistors. Illustrated in Fig. 9.18, such a circuit potentially provides a higher gain than the op amp of Fig. 9.15 because of the greater mobility of NMOS devices, but at the cost of lowering the pole at the folding points. To understand why, note that the pole at node *X* is given by the product of 1*/(gm*<sup>3</sup> + *gmb*3*)* and the total capacitance at this node (if the output pole is dominant). The magnitude of both of these components is relatively high: *M*<sup>3</sup> suffers from a low transconductance, and *M*<sup>5</sup> contributes substantial capacitance because it must be wide enough to carry the drain currents of both *M*<sup>1</sup> and *M*3. In fact, for comparable bias currents, *M*5–*M*<sup>6</sup> in Fig. 9.18 may be several times wider than *M*5–*M*<sup>6</sup> in Fig. 9.15. For applications sensitive to flicker noise, the PMOS-input op amp is preferable (Sec. 9.12).

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, specifically a CMOS operational amplifier (op-amp) design. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - The circuit consists of multiple MOSFET transistors labeled M1 through M11 and Mb1 through Mb3.
   - M1 and M2 are connected in a differential pair configuration with their sources tied together and connected to the drain of M11.
   - M3 and M4 form a current mirror, with their sources connected to the drain of M7 and M8, respectively.
   - M5 and M6 are connected in a cascode configuration with their sources connected to the drain of M3 and M4, respectively.
   - M7 and M8 are connected in a differential pair configuration with their sources tied together and connected to the drain of M9.
   - M9 and M10 are connected in a current mirror configuration with their sources grounded.
   - Mb1, Mb2, and Mb3 are bias transistors providing reference currents I_REF1, I_REF2, and I_REF3, respectively.

2. **Connections:**
   - The input voltage \( V_{in} \) is applied to the gate of M1.
   - The output voltage \( V_{out} \) is taken from the drain of M4.
   - The gate of M2 is connected to a bias voltage \( V_{b1} \).
   - The gate of M3 is connected to a bias voltage \( V_{b2} \).
   - The gate of M4 is connected to the drain of M3.
   - The gate of M5 is connected to the drain of M5 (forming a diode-connected transistor).
   - The gate of M6 is connected to the drain of M6 (forming a diode-connected transistor).
   - The gate of M7 is connected to the drain of M7 (forming a diode-connected transistor).
   - The gate of M8 is connected to the drain of M8 (forming a diode-connected transistor).
   - The gate of M9 is connected to the drain of M9 (forming a diode-connected transistor).
   - The gate of M10 is connected to the drain of M10 (forming a diode-connected transistor).

3. **Power Supply:**
   - The circuit is powered by a supply voltage \( V_{DD} \).

4. **Bias Currents:**
   - The bias currents \( I_{REF1} \), \( I_{REF2} \), and \( I_{REF3} \) are provided by the bias transistors Mb1, Mb2, and Mb3, respectively.

5. **Nodes:**
   - Node X is the connection point between the drain of M5 and the source of M3.
   - Node Y is the connection point between the drain of M6 and the source of M4.

This circuit is a typical representation of a CMOS operational amplifier with differential input stages, current mirrors, and cascode configurations to enhance performance characteristics such as gain and bandwidth.
```

**Figure 9.18** Realization of a folded-cascode op amp.

### **9.2.5 Folded-Cascode Properties**

Our study thus far suggests that the overall voltage swing of a folded-cascode op amp is only slightly higher than that of a telescopic configuration. This advantage comes at the cost of higher power dissipation, lower voltage gain, lower pole frequencies, and, as explained in Sec. 9.12, higher noise. Nonetheless, folded-cascode op amps are used more widely for two reasons: (1) their input and output CM levels can be chosen equal without limiting the output swings, and (2) compared to telescopic cascodes, they can accommodate a wider input CM range. Let us elaborate on these properties.

Consider the closed-loop amplifier of Fig. 9.19(a), assuming a folded-cascode op amp. We can draw the circuit as shown in Fig. 9.19(b) or Fig. 9.19(c), noting that the input and output CM levels are equal. With a high open-loop gain, the gate voltages of *M*<sup>1</sup> and *M*<sup>2</sup> swing negligibly while *VX* and *VY* can reach within two overdrives of ground or *VDD*. This should be compared with the swings in Fig. 9.10.

Here is the image describtion:
```
The image consists of three different circuit diagrams labeled (a), (b), and (c).

(a) The first diagram (a) is a simple operational amplifier (op-amp) circuit. It shows an op-amp with two input terminals (one positive and one negative) and one output terminal. The op-amp is connected to four resistors: R1, R2, R3, and R4. R1 and R2 are connected to the input terminals, while R3 and R4 are connected to the output terminal and the input terminals, forming a feedback loop.

(b) The second diagram (b) is a more complex circuit involving multiple transistors and resistors. It includes:
- Two resistors, R3 and R4, connected to the gates of transistors M1 and M2, respectively.
- Transistors M1 and M2 are connected to a current source and capacitors.
- The circuit also includes transistors M3, M4, M5, M6, M7, M8, M9, and M10, which are connected in a specific configuration to form a more complex network.
- The circuit has two nodes labeled X and Y, which are connected to the gates of transistors M3 and M4, respectively.
- The power supply voltage V_DD is connected to the drains of transistors M9 and M10.

(c) The third diagram (c) is similar to diagram (b) but slightly simplified. It includes:
- Resistors R3 and R4 connected to the gates of transistors M1 and M2, respectively.
- Transistors M1 and M2 are connected to a current source and capacitors.
- Transistors M3 and M4 are connected to the gates of transistors M1 and M2, respectively.
- The circuit has two nodes labeled X and Y, which are connected to the gates of transistors M3 and M4, respectively.

Overall, the image shows different configurations of electronic circuits involving operational amplifiers, resistors, and transistors.
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
The image depicts a schematic diagram of a CMOS (Complementary Metal-Oxide-Semiconductor) circuit, specifically a current mirror circuit with additional transistors for improved performance. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1, M2, M4, M6, M8, M10, M11:** These are MOSFET transistors. The specific type (NMOS or PMOS) is not explicitly indicated, but based on typical current mirror configurations, we can infer their types.
   - **M1 and M2:** Likely NMOS transistors, as they are connected to the input voltage \( V_{in} \) and ground.
   - **M4 and M6:** Likely PMOS transistors, as they are connected to the supply voltage \( V_{DD} \).
   - **M8 and M10:** Likely NMOS transistors, as they are connected to ground.
   - **M11:** Likely an NMOS transistor, as it is connected to ground.

2. **Connections:**
   - The input voltage \( V_{in} \) is applied to the gate of transistor M1.
   - The source of M1 is connected to the drain of M11, which is grounded.
   - The drain of M1 is connected to the gate of M2.
   - The source of M2 is connected to the drain of M11, which is grounded.
   - The drain of M2 is connected to the gate of M4 and the source of M6.
   - The drain of M6 is connected to the supply voltage \( V_{DD} \).
   - The source of M4 is connected to the drain of M8.
   - The source of M8 is connected to the drain of M10, which is grounded.
   - The gate of M8 is connected to the gate of M10, forming a current mirror.
   - The node Y is the connection point between the drain of M4 and the source of M6.

3. **Functionality:**
   - This circuit is likely designed to mirror the current from one branch to another, with M1 and M2 forming the input stage, and M4, M6, M8, and M10 forming the current mirror and output stage.
   - The additional transistors (M11, M8, M10) are used to improve the performance of the current mirror, possibly by enhancing the output resistance and matching characteristics.

Overall, this is a complex current mirror circuit with additional transistors to improve its performance, commonly used in analog integrated circuits for precise current replication.
```

**Figure 9.20** Folded-cascode op amp with input and output shorted.

*VO D*<sup>11</sup> = 0*.*4 V as an initial guess, we have *VG S*<sup>1</sup> = 0*.*95 V, obtaining *VO D*<sup>1</sup>*,*<sup>2</sup> = 0*.*95 − 0*.*7 = 0*.*25 V, and hence *(W/L)*1*,*<sup>2</sup> = 400*.* The maximum dimensions of *M*<sup>1</sup> and *M*<sup>2</sup> are determined by the tolerable input capacitance and the capacitance at nodes *X* and *Y* in Fig. 9.18.

We now calculate the small-signal gain. Using *gm* = 2*ID/(VG S* − *VT H )*, we have *gm*<sup>1</sup>*,*<sup>2</sup> = 0*.*006 A/V*, gm*<sup>3</sup>*,*<sup>4</sup> = 0*.*0038 A/V, and *gm*<sup>7</sup>*,*<sup>8</sup> = 0*.*05 A/V. For *L* = 0*.*5 *µ*m, *rO*<sup>1</sup>*,*<sup>2</sup> = *rO*<sup>7</sup>−<sup>10</sup> = 13*.*3 k%, and *rO*<sup>3</sup>*,*<sup>4</sup> = 2*rO*<sup>5</sup>*,*<sup>6</sup> = 6*.*67 k%. It follows that the impedance seen looking into the drain of *M*<sup>7</sup> (or *M*8) is equal to 8.8 M% whereas, owing to the limited intrinsic gain of *M*<sup>3</sup> (or *M*4), that seen looking into the drain of *M*<sup>3</sup> is equal to 66.5 k%. The overall gain is therefore limited to about 400.

In order to increase the gain, we first observe that *rO*<sup>5</sup>*,*<sup>6</sup> is quite lower than *rO*<sup>1</sup>*,*2. Thus, the length of *M*5– *M*<sup>6</sup> must be increased. Also, the transconductance of *M*1–*M*<sup>2</sup> is relatively low and can be increased by widening these transistors. Finally, we may decide to double the intrinsic gain of *M*<sup>3</sup> and *M*<sup>4</sup> by doubling both their length and their width, but at the cost of increasing the capacitance at nodes *X* and *Y* . We leave the exact choice of the device dimensions as an exercise for the reader. Note that the op amp must incorporate common-mode feedback (Sec. 9.7). ▲

Telescopic and folded-cascode op amps can also be designed to provide a single-ended output. Shown in Fig. 9.21(a) is an example, where a PMOS cascode current mirror converts the differential currents of *M*<sup>3</sup>

Here is the image describtion:
```
The image contains two circuit diagrams labeled (a) and (b), both of which are differential amplifier circuits with cascode stages. Here is a detailed description of each circuit:

### Circuit (a):
1. **Transistors:**
   - The circuit consists of eight MOSFETs labeled M1 to M8.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the cascode transistors for M1 and M2, respectively.
   - M5 and M6 are the load transistors.
   - M7 and M8 are the cascode transistors for M5 and M6, respectively.

2. **Connections:**
   - The source terminals of M1 and M2 are connected together and to a current source labeled I_SS, which is connected to ground.
   - The gate of M1 is connected to the input voltage V_in.
   - The gate of M2 is connected to a bias voltage V_b.
   - The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
   - The gates of M3 and M4 are connected to a bias voltage V_b.
   - The drain of M3 is connected to the source of M5, and the drain of M4 is connected to the source of M6.
   - The gates of M5 and M6 are connected to the node X.
   - The drain of M5 is connected to the source of M7, and the drain of M6 is connected to the source of M8.
   - The gates of M7 and M8 are connected to the node X.
   - The drains of M7 and M8 are connected to the supply voltage V_DD.
   - The output voltage V_out is taken from the drain of M6.

### Circuit (b):
1. **Transistors:**
   - Similar to circuit (a), this circuit also consists of eight MOSFETs labeled M1 to M8.
   - M1 and M2 are the input transistors.
   - M3 and M4 are the cascode transistors for M1 and M2, respectively.
   - M5 and M6 are the load transistors.
   - M7 and M8 are the cascode transistors for M5 and M6, respectively.

2. **Connections:**
   - The source terminals of M1 and M2 are connected together and to a current source labeled I_SS, which is connected to ground.
   - The gate of M1 is connected to the input voltage V_in.
   - The gate of M2 is connected to a bias voltage V_b1.
   - The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
   - The gates of M3 and M4 are connected to the bias voltage V_b1.
   - The drain of M3 is connected to the source of M5, and the drain of M4 is connected to the source of M6.
   - The gate of M5 is connected to a bias voltage V_b2.
   - The gate of M6 is connected to the node X.
   - The drain of M5 is connected to the source of M7, and the drain of M6 is connected to the source of M8.
   - The gates of M7 and M8 are connected to the node X.
   - The drains of M7 and M8 are connected to the supply voltage V_DD.
   - The output voltage V_out is taken from the drain of M6.

### Key Differences:
- In circuit (a), the gates of M5 and M6 are connected to the node X, whereas in circuit (b), the gate of M5 is connected to a separate bias voltage V_b2.
- The biasing of the cascode transistors M3 and M4 is different in the two circuits. In circuit (a), both gates are connected to the same bias voltage V_b, while in circuit (b), they are connected to V_b1.

These circuits are typically used in analog design for high-gain differential amplification with improved output resistance and reduced Miller effect.
```

**Figure 9.21** Cascode op amps with single-ended output.

and *M*<sup>4</sup> to a single-ended output voltage. In this implementation, however, *VX* = *VDD* −|*VG S*5|−|*VG S*7|, limiting the maximum value of *Vout* to *VDD* − |*VG S*5| − |*VG S*7|+|*VT H*6| and "wasting" one PMOS threshold voltage in the swing (Chapter 5). To resolve this issue, the PMOS load can be modified to a low-voltage cascode (Chapter 5), as shown in Fig. 9.21(b), so that *M*<sup>7</sup> and *M*<sup>8</sup> are biased at the edge of the triode region. Similar ideas apply to folded-cascode op amps as well.

The circuit of Fig. 9.21(a) suffers from two disadvantages with respect to its differential counterpart in Fig. 9.8(b). First, it provides only half the output voltage swing. Second, it contains a mirror pole at node *X* (Chapter 5), thus limiting the speed of feedback systems employing such an amplifier. It is therefore preferable to use the differential topology, although it requires a feedback loop to define the output common-mode level (Sec. 9.7).

# **9.3 Two-Stage Op Amps**

The op amps studied thus far exhibit a "one-stage" nature in that they allow the small-signal current produced by the input pair to flow directly through the output impedance, i.e., they perform voltage-tocurrent conversion only once. The gain of these topologies is therefore limited to the product of the input pair transconductance and the output impedance. We have also observed that cascoding in such circuits increases the gain while limiting the output swings.

In some applications, the gain and/or the output swings provided by cascode op amps are not adequate. For example, a modern op amp must operate with supply voltages as low as 0.9 V while delivering singleended output swings as large as 0.8 V. In such cases, we resort to "two-stage" op amps, with the first stage providing a high gain and the second, large swings (Fig. 9.22). In contrast to cascode op amps, a two-stage configuration isolates the gain and swing requirements.

Here is the image describtion:
```
The image is a diagram of a two-stage operational amplifier (op amp). It consists of two rectangular blocks labeled "Stage 1" and "Stage 2," which are connected in series. 

- The first block, "Stage 1," is labeled "High Gain" at the top. It has an input labeled "Vin" on the left side, with two input terminals.
- The second block, "Stage 2," is labeled "High Swing" at the top. It receives the output from "Stage 1" and has an output labeled "Vout" on the right side, with two output terminals.

The diagram is labeled as "Figure 9.22 Two-stage op amp." at the bottom right corner. The arrows between the stages indicate the direction of the signal flow from "Stage 1" to "Stage 2."
```

Each stage in Fig. 9.22 can incorporate various amplifier topologies studied in previous sections, but the second stage is typically configured as a simple common-source stage so as to allow maximum output swings. Figure 9.23 shows an example, where the first and second stages exhibit gains equal to *gm*<sup>1</sup>*,*<sup>2</sup>*(rO*<sup>1</sup>*,*<sup>2</sup>%*rO*<sup>3</sup>*,*<sup>4</sup>*)* and *gm*<sup>5</sup>*,*<sup>6</sup>*(rO*<sup>5</sup>*,*<sup>6</sup>%*rO*<sup>7</sup>*,*<sup>8</sup>*)*, respectively. The overall gain is therefore comparable to that

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top.

2. **Transistors:**
   - The circuit consists of eight MOSFET transistors labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the active load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the current mirror load transistors.
   - \( M_7 \) and \( M_8 \) are the tail current source transistors.

3. **Connections:**
   - The gates of \( M_1 \) and \( M_2 \) are connected to the input voltage \( V_{in} \).
   - The sources of \( M_1 \) and \( M_2 \) are connected together and to a current source \( I_{SS} \) which is grounded.
   - The drains of \( M_1 \) and \( M_2 \) are connected to the drains of \( M_3 \) and \( M_4 \) respectively, forming nodes \( X \) and \( Y \).
   - The gates of \( M_3 \) and \( M_4 \) are connected to a bias voltage \( V_{b1} \).
   - The sources of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The drains of \( M_5 \) and \( M_6 \) are connected to \( V_{DD} \), and their sources are connected to nodes \( X \) and \( Y \) respectively.
   - The gates of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_3 \) and \( M_4 \) respectively.
   - The sources of \( M_7 \) and \( M_8 \) are grounded, and their gates are connected to a bias voltage \( V_{b2} \).
   - The drains of \( M_7 \) and \( M_8 \) are connected to the sources of \( M_5 \) and \( M_6 \) respectively, forming the output nodes \( V_{out1} \) and \( V_{out2} \).

4. **Outputs:**
   - The differential output voltages are taken from nodes \( V_{out1} \) and \( V_{out2} \).

This circuit is a typical differential amplifier with a current mirror load, which is commonly used in analog integrated circuits for amplifying differential signals.
```

**Figure 9.23** Simple implementation of a two-stage op amp.

of a cascode op amp, but the swing at *Vout*<sup>1</sup> and *Vout*<sup>2</sup> is equal to *VDD* − |*VO D*<sup>5</sup>*,*<sup>6</sup>| − *VO D*<sup>7</sup>*,*8, the highest possible value.<sup>4</sup>

To obtain a higher gain, the first stage can incorporate cascode devices, as depicted in Fig. 9.24. With a gain of, say, 10 in the output stage, the voltage swings at *X* and *Y* are quite small, allowing optimization of *M*1–*M*<sup>8</sup> for higher gain. The overall voltage gain can be expressed as

$$A\_v \approx \{ g\_{m1,2} \| (g\_{m3,4} + g\_{mb3,4}) r\_{O3,4} r\_{O1,2} \} \| \| (g\_{m5,6} + g\_{mb5,6}) r\_{O5,6} r\_{O7,8} \| \} \tag{9.18}$$
 
$$\times \left[ g\_{m9,10} (r\_{O9,10} \| r\_{O11,12}) \right] \tag{9.18}$$

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). Here is a detailed description of the components and their connections:

1. **Power Supply and Ground:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top.
   - The bottom of the circuit is connected to the ground.

2. **Transistors:**
   - The circuit consists of 12 MOSFETs labeled \( M_1 \) to \( M_{12} \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the cascode transistors for \( M_3 \) and \( M_4 \), respectively.
   - \( M_7 \) and \( M_8 \) are the cascode transistors for \( M_5 \) and \( M_6 \), respectively.
   - \( M_9 \) and \( M_{10} \) are the output transistors.
   - \( M_{11} \) and \( M_{12} \) are the tail current source transistors.

3. **Bias Voltages:**
   - \( V_{b1} \), \( V_{b2} \), \( V_{b3} \), and \( V_{b4} \) are the bias voltages applied to the gates of the respective transistors.
   - \( V_{b1} \) is applied to the gates of \( M_3 \) and \( M_4 \).
   - \( V_{b2} \) is applied to the gates of \( M_5 \) and \( M_6 \).
   - \( V_{b3} \) is applied to the gates of \( M_7 \) and \( M_8 \).
   - \( V_{b4} \) is applied to the gates of \( M_{11} \) and \( M_{12} \).

4. **Input and Output:**
   - The input signal \( V_{in} \) is applied to the gate of \( M_1 \).
   - The differential output signals are taken from the drains of \( M_9 \) and \( M_{10} \), labeled as \( V_{out1} \) and \( V_{out2} \), respectively.

5. **Current Source:**
   - A current source \( I_{SS} \) is connected to the sources of \( M_1 \) and \( M_2 \), providing a constant current.

6. **Connections:**
   - The source of \( M_1 \) is connected to the source of \( M_2 \) and then to the current source \( I_{SS} \).
   - The drain of \( M_1 \) is connected to the source of \( M_3 \), and the drain of \( M_2 \) is connected to the source of \( M_4 \).
   - The drain of \( M_3 \) is connected to the source of \( M_5 \), and the drain of \( M_4 \) is connected to the source of \( M_6 \).
   - The drain of \( M_5 \) is connected to the source of \( M_7 \), and the drain of \( M_6 \) is connected to the source of \( M_8 \).
   - The drains of \( M_7 \) and \( M_8 \) are connected to \( V_{DD} \).
   - The drain of \( M_9 \) is connected to \( V_{out1} \), and the drain of \( M_{10} \) is connected to \( V_{out2} \).

This circuit is a typical example of a high-gain differential amplifier with cascode stages to improve gain and output impedance.
```

**Figure 9.24** Two-stage op amp employing cascoding.

A two-stage op amp can provide a single-ended output. One method is to convert the differential currents of the two output stages to a single-ended voltage. Illustrated in Fig. 9.25, this approach maintains the differential nature of the first stage, using only the current mirror *M*7–*M*<sup>8</sup> to generate a single-ended output.

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage operational amplifier (op-amp) with a single-ended output. The circuit consists of multiple MOSFET transistors and other components arranged in a specific configuration to achieve amplification.

Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.

2. **Transistors:**
   - There are eight MOSFET transistors labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the current mirror transistors.
   - \( M_7 \) and \( M_8 \) are the transistors in the second stage of the amplifier.

3. **Connections:**
   - The gate of \( M_1 \) is connected to the input voltage \( V_{in} \).
   - The source of \( M_1 \) and \( M_2 \) are connected together and to a current source \( I_{SS} \) which is connected to ground.
   - The drain of \( M_1 \) is connected to the drain of \( M_3 \), and the drain of \( M_2 \) is connected to the drain of \( M_4 \).
   - The gates of \( M_3 \) and \( M_4 \) are connected together to a bias voltage \( V_b \).
   - The source of \( M_3 \) is connected to the drain of \( M_5 \), and the source of \( M_4 \) is connected to the drain of \( M_6 \).
   - The gates of \( M_5 \) and \( M_6 \) are connected together and to the drain of \( M_5 \).
   - The source of \( M_5 \) is connected to \( V_{DD} \), and the source of \( M_6 \) is connected to the drain of \( M_7 \).
   - The gate of \( M_7 \) is connected to the drain of \( M_8 \), and the source of \( M_7 \) is connected to ground.
   - The gate of \( M_8 \) is connected to the output voltage \( V_{out} \), and the source of \( M_8 \) is connected to ground.

4. **Output:**
   - The output voltage \( V_{out} \) is taken from the drain of \( M_6 \).

The figure is labeled as "Figure 9.25 Two-stage op amp with single-ended output," indicating that this is a two-stage operational amplifier design with a single-ended output configuration.
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
The image consists of two parts labeled (a) and (b), each depicting different stages of an electronic circuit involving an operational amplifier and a transistor.

(a) The first part shows a simple circuit diagram. It includes:
- An operational amplifier labeled \( A_1 \) with its inverting input (-) connected to ground and its non-inverting input (+) receiving an input voltage \( V_{in} \).
- The output of the operational amplifier is connected to the gate of an NMOS transistor labeled \( M_2 \).
- The source of the NMOS transistor \( M_2 \) is connected to ground.
- The drain of the NMOS transistor is labeled as \( I_{out} \), indicating the output current.

(b) The second part shows a more detailed representation of the circuit in (a) and its equivalent model:
- The left side of (b) repeats the circuit from (a) but includes a dashed box around the operational amplifier \( A_1 \) and the NMOS transistor \( M_2 \), indicating that they form a single functional block.
- The right side of (b) shows the equivalent small-signal model of the circuit:
  - The input voltage \( V_1 \) is applied to the non-inverting input of the operational amplifier.
  - The output of the operational amplifier is represented as a current source \( A_1 g_m V_1 \) in parallel with a resistor \( r_o \).
  - The current source and resistor are connected to the output node labeled \( I_{out} \).

Overall, the image illustrates the transformation of a simple operational amplifier and transistor circuit into its small-signal equivalent model, highlighting the relationship between the input voltage and the output current.
```

**Figure 9.26** (a) Transistor preceded by a voltage amplifier, and (b) equivalent circuit.

We note that the overall circuit exhibits a transconductance of *A*1*gm* and a voltage gain of−*A*1*gmrO* (why?). We thus surmise that this arrangement can be viewed as a three-terminal device (a "supertransistor") having a transconductance of *A*1*gm* and an output resistance of *rO* [Fig. 9.26(b)]. We neglect body effect in this section.

Let us now incorporate this new device in a familiar topology and examine the circuit's behavior. We begin with the degenerated stage depicted in Fig. 9.27(a) and wish to compute its transconductance (with the output shorted to ac ground). Since *RS* carries *Iout*, the small-signal gate voltage is given by *(Vin* − *RS Iout)A*1, yielding a gate-source voltage of *(Vin* − *RS Iout)A*<sup>1</sup> − *RS Iout* and hence *Iout* = *gm*[*(Vin* − *RS Iout)A*<sup>1</sup> − *RS Iout*]. It follows that

$$\frac{I\_{\rm out}}{V\_{in}} = \frac{A\_1 \mathbf{g}\_m}{1 + (A\_1 + 1)\mathbf{g}\_m R\_S} \tag{9.19}$$

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b).

(a) The first circuit diagram shows a configuration with an operational amplifier (A1) and a MOSFET (M2). The input voltage (Vin) is applied to the non-inverting input of the operational amplifier (A1). The inverting input of A1 is connected to the source of the MOSFET (M2). The drain of M2 is connected to the output current (Iout) and a positive supply voltage. The source of M2 is connected to a resistor (RS) which is grounded. The operational amplifier (A1) and MOSFET (M2) are enclosed in a dashed box, indicating they form a single functional block.

(b) The second circuit diagram is an extension of the first one. It includes the same operational amplifier (A1) and MOSFET (M2) configuration as in (a). Additionally, it shows the output current (I0) flowing through a resistor (ro) connected to the drain of M2. The other end of the resistor (ro) is connected to a node where a current (Ix) flows into a voltage source (Vx). The voltage source (Vx) is grounded on its negative terminal. The source of M2 is again connected to a resistor (RS) which is grounded.

Both diagrams illustrate different stages of a circuit involving an operational amplifier and a MOSFET, with the second diagram (b) building upon the first (a) by adding additional components to the output stage.
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
The image consists of two circuit diagrams labeled as (a) and (b), both featuring an operational amplifier (op-amp) and a MOSFET transistor. Here is a detailed description of each diagram:

**Diagram (a):**
- The circuit includes an operational amplifier labeled as A1.
- The non-inverting input (+) of the op-amp A1 is connected to an input voltage source labeled \( V_{in} \).
- The inverting input (-) of the op-amp A1 is connected to the source terminal of an n-channel MOSFET transistor labeled M2.
- The drain terminal of the MOSFET M2 is connected to a resistor labeled \( R_D \), which is in turn connected to a positive supply voltage labeled \( V_{DD} \).
- The source terminal of the MOSFET M2 is connected to a resistor labeled \( R_X \), which is connected to ground.
- The output of the op-amp A1 is connected to the gate terminal of the MOSFET M2.
- The entire circuit is enclosed in a dashed box, indicating it is a single module or block.

**Diagram (b):**
- This circuit is similar to diagram (a) but includes additional components and connections.
- The operational amplifier A1 and MOSFET M2 are configured in the same manner as in diagram (a).
- The drain terminal of the MOSFET M2 is connected to a resistor \( R_D \), which is connected to a current source labeled \( I_X \).
- The source terminal of the MOSFET M2 is connected to a resistor labeled \( r_O \), which is connected to a voltage source labeled \( V_X \).
- The current through the MOSFET M2 is labeled \( I_0 \).
- The current through the resistor \( r_O \) is labeled \( I_X \).
- The voltage source \( V_X \) is connected to ground.

Both diagrams illustrate different configurations of an op-amp and MOSFET circuit, with diagram (b) showing a more complex setup involving additional current and voltage sources.
```

Here is the image describtion:
```
The image is a simple text label that reads "Figure 9.28". It appears to be a reference to a specific figure in a document, book, or article, indicating that it is the 28th figure in the 9th chapter or section. The text is in a standard font and is likely used to identify and refer to a particular visual element within the larger context of the document.
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
The image depicts a circuit diagram featuring a "Super Transistor" configuration. The circuit includes the following components and connections:

1. **Super Transistor Block**: This block is outlined with a dashed line and contains an operational amplifier (A1) and two MOSFET transistors (M1 and M2).

2. **Operational Amplifier (A1)**: The op-amp has two input terminals, labeled as the inverting input (-) and the non-inverting input (+). The non-inverting input is connected to a voltage source labeled \( V_b \).

3. **MOSFET Transistors**:
   - **M1**: This transistor is an N-channel MOSFET with its source connected to ground and its gate connected to the output of the operational amplifier (A1).
   - **M2**: This transistor is a P-channel MOSFET with its source connected to the positive supply voltage \( V_{DD} \) and its gate connected to the output of the operational amplifier (A1). The drain of M2 is connected to the drain of M1 at a node labeled \( P \).

4. **Input and Output**:
   - **\( V_{in} \)**: The input voltage is applied to the source of M1.
   - **\( V_{out} \)**: The output voltage is taken from the drain of M2, which is also connected to the node \( P \).

5. **Power Supply**: The circuit is powered by a positive supply voltage \( V_{DD} \).

The overall configuration suggests that the operational amplifier (A1) controls the gate voltages of the MOSFETs (M1 and M2) to regulate the output voltage \( V_{out} \) based on the input voltage \( V_{in} \) and the reference voltage \( V_b \). This setup is often used in analog circuits for applications such as voltage regulation, amplification, or as part of a more complex analog signal processing system.
```

**Figure 9.29** Basic gain-boosted stage.

**Second Perspective** Consider the degenerated stage shown in Fig. 9.30(a). We wish to increase the output resistance without stacking more cascode devices. Recall from Chapter 3 that if the drain voltage changes by '*V*, then the source voltage changes by '*VS* = *RS/*[*rO* + *(*1 + *gmrO )RS*] (with γ = 0), producing a change in the voltage across *RS* and hence in the drain current. We can loosely view the effect as voltage division between *RS* and *gmrO RS*.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), each accompanied by their respective equivalent circuits.

**Diagram (a):**
- The left side of diagram (a) shows a MOSFET (M2) with its gate connected to a bias voltage (Vb) and its source connected to a small signal voltage source (ΔVs) through a resistor (Rs).
- The drain of the MOSFET is connected to a current source (I0) and a resistor (ro) in parallel.
- The node at the drain is labeled as point P.
- The voltage at the drain (Vx) is measured with respect to ground.
- The current flowing through the drain is labeled as Ix.
- The right side of diagram (a) shows the small-signal equivalent circuit.
- The equivalent circuit consists of a voltage source (ΔV) in series with a resistor (Rs) and a dependent current source (gm ro Rs) in parallel with the resistor (Rs).
- The voltage across the resistor (Rs) is labeled as Vx.

**Diagram (b):**
- The left side of diagram (b) shows a similar MOSFET (M2) configuration as in diagram (a), but with an operational amplifier (A1) added.
- The non-inverting input of the operational amplifier is connected to the bias voltage (Vb).
- The inverting input is connected to the source of the MOSFET (M2).
- The output of the operational amplifier is connected to the gate of the MOSFET (M2).
- The source of the MOSFET is connected to the small signal voltage source (ΔVs) through a resistor (Rs).
- The drain of the MOSFET is connected to a current source (I0) and a resistor (ro) in parallel.
- The node at the drain is labeled as point P.
- The voltage at the drain (Vx) is measured with respect to ground.
- The current flowing through the drain is labeled as Ix.
- The right side of diagram (b) shows the small-signal equivalent circuit.
- The equivalent circuit consists of a voltage source (ΔV) in series with a resistor (Rs) and a dependent current source (A1 gm ro Rs) in parallel with the resistor (Rs).
- The voltage across the resistor (Rs) is labeled as Vx.

In summary, both diagrams illustrate the small-signal analysis of a MOSFET circuit, with diagram (b) incorporating an operational amplifier to enhance the gain. The equivalent circuits show how the small-signal parameters are represented in each case.
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
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) and a MOSFET transistor. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (A1)**: 
   - The op-amp has its inverting input (-) connected to its output, forming a feedback loop.
   - The non-inverting input (+) is connected to an unspecified input signal.

2. **MOSFET Transistor (M2)**:
   - The gate (G) of the MOSFET is connected to the output of the op-amp, labeled as \( V_G \).
   - The source (S) of the MOSFET is connected to a node labeled \( P \).
   - The drain (D) of the MOSFET is connected to a resistor \( r_O \).

3. **Resistors**:
   - \( r_O \) is connected between the drain of the MOSFET and a node where current \( I_X \) flows towards a voltage source \( V_X \).
   - \( R_S \) is connected between node \( P \) and ground.

4. **Voltage Source (V_X)**:
   - \( V_X \) is connected to ground, with the positive terminal connected to the node where \( I_X \) flows.

5. **Currents**:
   - \( I_O \) is the current flowing through the MOSFET from the drain to the source.
   - \( I_{r_O} \) is the current flowing through the resistor \( r_O \).
   - \( I_X \) is the current flowing towards the voltage source \( V_X \).

The circuit appears to be a feedback configuration involving the op-amp and the MOSFET, likely for controlling the current or voltage at specific nodes. The resistor \( R_S \) sets a reference voltage at node \( P \), and the op-amp adjusts the gate voltage \( V_G \) of the MOSFET to maintain the desired operating conditions.
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
The image consists of three sub-circuits labeled (a), (b), and (c), each depicting different configurations of a transistor-based circuit. Here is a detailed description of each sub-circuit:

### Sub-circuit (a):
- **Components**:
  - Three transistors labeled M1, M2, and M3.
  - Two current sources labeled I1 and I2.
  - A voltage source labeled VDD.
  - An input voltage labeled Vin.
  - An output voltage labeled Vout.
- **Configuration**:
  - Transistor M1 is connected to the input voltage Vin at its gate, with its source connected to ground and its drain connected to node P.
  - Transistor M2 has its gate connected to node G, its source connected to node P, and its drain connected to the output voltage Vout.
  - Transistor M3 is part of a sub-circuit labeled A1, with its source connected to ground, its gate connected to node G, and its drain connected to the current source I1, which is connected to the voltage source VDD.
  - The current source I2 is connected between the voltage source VDD and the output voltage Vout.

### Sub-circuit (b):
- **Components**:
  - Three transistors labeled M1, M2, and M3.
  - Two current sources labeled I1 and I2.
  - A voltage source labeled VDD.
  - An input voltage labeled Vin.
  - An output voltage labeled Vout.
- **Configuration**:
  - Transistor M1 is connected to the input voltage Vin at its gate, with its source connected to ground and its drain connected to node P.
  - Transistor M2 has its gate connected to node G, its source connected to node P, and its drain connected to the output voltage Vout.
  - Transistor M3 is part of a sub-circuit labeled A1, with its source connected to ground, its gate connected to node G, and its drain connected to the current source I1, which is connected to the voltage source VDD.
  - The current source I2 is connected between the voltage source VDD and the output voltage Vout.

### Sub-circuit (c):
- **Components**:
  - Four transistors labeled M1, M2, M3, and M4.
  - Three current sources labeled I1, I2, and I3.
  - Two voltage sources labeled VDD and Vb.
  - An input voltage labeled Vin.
  - An output voltage labeled Vout.
- **Configuration**:
  - Transistor M1 is connected to the input voltage Vin at its gate, with its source connected to ground and its drain connected to node P.
  - Transistor M2 has its gate connected to node G, its source connected to node P, and its drain connected to the output voltage Vout.
  - Transistor M3 is part of a sub-circuit labeled A1, with its source connected to ground, its gate connected to node G, and its drain connected to node G.
  - Transistor M4 has its gate connected to the voltage source Vb, its source connected to node G, and its drain connected to the current source I3, which is connected to the voltage source VDD.
  - The current source I1 is connected between the voltage source VDD and the source of transistor M3.
  - The current source I2 is connected between the voltage source VDD and the output voltage Vout.

In all three sub-circuits, the transistors are arranged in a manner that suggests they are part of an amplifier or similar analog circuit, with the current sources providing biasing currents and the voltage sources providing the necessary supply voltages.
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
The image consists of three different circuit diagrams labeled (a), (b), and (c). Each circuit diagram features a differential amplifier configuration with various components and connections. Here is a detailed description of each circuit:

### Circuit (a):
- **Transistors**: The circuit includes four MOSFET transistors labeled M1, M2, M3, and M4.
- **Amplifiers**: Two amplifiers are present, labeled A1 and A2.
- **Current Source**: There is a current source labeled Iss connected to the source terminals of M1 and M2.
- **Connections**:
  - The gate of M1 is connected to the input voltage Vin.
  - The drain of M1 is connected to node X, which is also connected to the input of amplifier A1.
  - The output of amplifier A1 is connected to the gate of M3.
  - The drain of M3 is connected to a positive supply voltage.
  - The source of M3 is connected to node X.
  - The gate of M2 is connected to ground.
  - The drain of M2 is connected to node Y, which is also connected to the input of amplifier A2.
  - The output of amplifier A2 is connected to the gate of M4.
  - The drain of M4 is connected to a positive supply voltage.
  - The source of M4 is connected to node Y.

### Circuit (b):
- **Transistors**: The circuit includes four MOSFET transistors labeled M1, M2, M3, and M4.
- **Amplifier**: One amplifier is present in the circuit.
- **Current Source**: There is a current source labeled Iss connected to the source terminals of M1 and M2.
- **Connections**:
  - The gate of M1 is connected to the input voltage Vin.
  - The drain of M1 is connected to node X.
  - The gate of M2 is connected to ground.
  - The drain of M2 is connected to node Y.
  - The source of M3 is connected to node X.
  - The gate of M3 is connected to the output of the amplifier.
  - The drain of M3 is connected to a positive supply voltage.
  - The source of M4 is connected to node Y.
  - The gate of M4 is connected to the output of the amplifier.
  - The drain of M4 is connected to a positive supply voltage.
  - The input of the amplifier is connected to node X and node Y.

### Circuit (c):
- **Transistors**: The circuit includes six MOSFET transistors labeled M1, M2, M3, M4, M5, and M6.
- **Current Sources**: There are three current sources labeled Iss1, Iss2, I1, and I2.
- **Connections**:
  - The gate of M1 is connected to the input voltage Vin.
  - The drain of M1 is connected to node X.
  - The source of M1 is connected to the current source Iss1.
  - The gate of M2 is connected to ground.
  - The drain of M2 is connected to node Y.
  - The source of M2 is connected to the current source Iss1.
  - The source of M3 is connected to node X.
  - The gate of M3 is connected to the drain of M5.
  - The drain of M3 is connected to the current source I1.
  - The source of M4 is connected to node Y.
  - The gate of M4 is connected to the drain of M6.
  - The drain of M4 is connected to the current source I2.
  - The source of M5 is connected to the current source Iss2.
  - The gate of M5 is connected to a positive supply voltage.
  - The drain of M5 is connected to the gate of M3.
  - The source of M6 is connected to the current source Iss2.
  - The gate of M6 is connected to a positive supply voltage.
  - The drain of M6 is connected to the gate of M4.

Each circuit represents a different configuration of a differential amplifier with various components and connections to achieve specific functionalities.
```

**Figure 9.33** Boosting the output impedance of a differential cascode stage.

The voltage swing limitation in Fig. 9.33(c) results from the fact that the gain-boosting amplifier incorporates an NMOS differential pair. If nodes *X* and *Y* are sensed by a PMOS pair, the minimum value of *VX* and *VY* is not dictated by the gain-boosting amplifier. Now recall from Sec. 9.2 that the minimum input CM level of a folded-cascode stage using a PMOS input pair can be zero. Thus, we employ such a topology for the gain-boosting amplifier, arriving at the circuit shown in Fig. 9.34. Here, the minimum allowable level of *VX* and *VY* is given by *VO D*<sup>1</sup>*,*<sup>2</sup> + *VISS*1.

▲

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with current mirrors. The circuit consists of multiple MOSFET transistors and current sources. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - There are eight MOSFET transistors labeled M1 through M8.
   - M1 and M2 form the differential pair at the bottom center of the circuit.
   - M3 and M4 are connected to the drains of M1 and M2, respectively, and act as active loads.
   - M5 and M6 are connected to the gates of M1 and M2, respectively, and are part of the current mirror configuration.
   - M7 and M8 are connected to the gates of M5 and M6, respectively, and are also part of the current mirror configuration.

2. **Current Sources:**
   - There are four current sources labeled I1, I2, Iss1, and Iss2.
   - I1 and I2 are connected to the sources of M3 and M4, respectively.
   - Iss1 is connected to the common source node of M1 and M2.
   - Iss2 is connected to the common drain node of M3 and M4.

3. **Nodes and Connections:**
   - The gates of M1 and M2 are connected to nodes X and Y, respectively.
   - The sources of M5 and M6 are connected to the gates of M1 and M2, respectively.
   - The gates of M5 and M6 are connected to the drains of M7 and M8, respectively.
   - The sources of M7 and M8 are connected to ground.
   - The gates of M7 and M8 are connected to a common bias voltage Vb.
   - The drains of M3 and M4 are connected to the current source Iss2.
   - The sources of M3 and M4 are connected to the current sources I1 and I2, respectively.

4. **Biasing:**
   - The bias voltage Vb is applied to the gates of M7 and M8 to set the operating point of the current mirrors.

This circuit is typically used in analog integrated circuits for amplifying differential signals while rejecting common-mode noise. The current mirrors formed by M5, M6, M7, and M8 help to ensure that the differential pair (M1 and M2) operates with a constant current, improving the performance of the amplifier.
```

**Figure 9.34** Folded-cascode circuit used as auxiliary amplifier.

#### ▲**Example 9.14**

Razavi-3930640 book December 17, 201516:59 370

Calculate the output impedance of the circuit shown in Fig. 9.34.

### **Solution**

Using the half-circuit concept and replacing the ideal current sources with transistors, we obtain the equivalent depicted in Fig. 9.35. The voltage gain from *X* to *P* is approximately equal to *gm*5*Rout*1, where *Rout*<sup>1</sup> ≈ [*gm*7*rO*<sup>7</sup> *(rO*<sup>9</sup>%*rO*5*)*]%*(gm*11*rO*11*rO*13*)*. Thus, *Rout* ≈ *gm*3*rO*3*rO*1*gm*5*Rout*1. In essence, since the output impedance of a cascode is boosted by a folded-cascode stage, the overall output impedance is similar to that of a "quadruple" cascode.

Here is the image describtion:
```
The image depicts a circuit diagram of an amplifier, specifically highlighting an auxiliary amplifier section. The circuit includes several MOSFET transistors and biasing voltages. Here is a detailed description of the components and their connections:

1. **Auxiliary Amplifier Section (dashed box):**
   - **Transistor M13:** Connected to bias voltage \( V_{b4} \) at its gate, with its source connected to the drain of transistor M11.
   - **Transistor M11:** Connected to bias voltage \( V_{b3} \) at its gate, with its source connected to the drain of transistor M7.
   - **Transistor M7:** Connected to bias voltage \( V_{b2} \) at its gate, with its source connected to the drain of transistor M5.
   - **Transistor M5:** Connected to the node labeled X at its drain, with its source connected to the drain of transistor M9.
   - **Transistor M9:** Connected to bias voltage \( V_{b1} \) at its gate, with its source connected to ground.

2. **Main Amplifier Section:**
   - **Transistor M1:** Connected to the input voltage \( V_{in} \) at its gate, with its source connected to ground.
   - **Transistor M3:** Connected to the node labeled P at its gate, with its source connected to the node labeled X and its drain connected to the output resistance \( R_{out} \).

3. **Connections:**
   - The node labeled P is connected to the gate of transistor M3.
   - The node labeled X is a common node where the drain of transistor M1, the source of transistor M3, and the drain of transistor M5 are connected.
   - The output resistance \( R_{out} \) is connected to the drain of transistor M3.

The circuit appears to be a complex amplifier design, possibly a cascode or a differential amplifier with an auxiliary amplifier section to enhance performance characteristics such as gain or bandwidth. The bias voltages \( V_{b1}, V_{b2}, V_{b3}, \) and \( V_{b4} \) are used to set the operating points of the transistors in the auxiliary amplifier section.
```

Regulated cascodes can also be utilized in the load current sources of a cascode op amp. Shown in Fig. 9.36(a), such a topology boosts the output impedance of the PMOS current sources as well, thereby achieving a very high voltage gain. To allow maximum swings at the output, amplifier *A*<sup>2</sup> must employ an NMOS-input folded-cascode differential pair. Similar ideas apply to folded-cascode op amps [Fig. 9.36(b)].

Here is the image describtion:
```
The image consists of two circuit diagrams labeled as (a) and (b), both illustrating gain boosting techniques applied to signal path and load devices. 

### Diagram (a):
- **Transistors**: The circuit includes ten MOSFET transistors labeled M1 through M8.
- **Amplifiers**: Two operational amplifiers labeled A1 and A2 are present.
- **Power Supply**: The circuit is powered by a voltage source labeled V_DD.
- **Current Source**: There is a current source labeled I_SS connected to the source of M1 and M2.
- **Connections**:
  - The input voltage V_in is applied to the gates of M1 and M2.
  - The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
  - The gates of M3 and M4 are connected to the output of amplifier A1.
  - The drains of M3 and M4 are connected to the sources of M5 and M6, respectively.
  - The gates of M5 and M6 are connected to the output of amplifier A2.
  - The drains of M5 and M6 are connected to the sources of M7 and M8, respectively.
  - The gates of M7 and M8 are connected to a bias voltage V_b.
  - The drains of M7 and M8 are connected to V_DD.
  - The output voltage V_out is taken from the connection between the drains of M5 and M6.

### Diagram (b):
- **Transistors**: The circuit includes twelve MOSFET transistors labeled M1 through M10.
- **Amplifiers**: Two operational amplifiers labeled A1 and A2 are present.
- **Power Supply**: The circuit is powered by a voltage source labeled V_DD.
- **Current Source**: There is a current source labeled I_SS connected to the source of M1 and M2.
- **Connections**:
  - The input voltage V_in is applied to the gates of M1 and M2.
  - The drains of M1 and M2 are connected to the sources of M3 and M4, respectively.
  - The gates of M3 and M4 are connected to the output of amplifier A1.
  - The drains of M3 and M4 are connected to the sources of M5 and M6, respectively.
  - The gates of M5 and M6 are connected to the output of amplifier A2.
  - The drains of M5 and M6 are connected to the sources of M7 and M8, respectively.
  - The gates of M7 and M8 are connected to a bias voltage V_b1.
  - The drains of M7 and M8 are connected to V_DD.
  - The output voltage V_out is taken from the connection between the drains of M5 and M6.
  - Additionally, the sources of M9 and M10 are connected to ground, and their gates are connected to a bias voltage V_b2.

### Caption:
The caption below the image reads: "Figure 9.36 Gain boosting applied to both signal path and load devices."

In summary, both diagrams illustrate different configurations of gain-boosted amplifiers, with diagram (b) including additional transistors M9 and M10 for further enhancement.
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
   - The op-amp is represented by a triangle with a positive (+) and negative (-) input terminal.
   - The positive input terminal is connected to a bias voltage \( V_b \).
   - The negative input terminal is connected to the source of transistor \( M_2 \).

2. **Transistors (M1 and M2)**:
   - **M1**: This is an NMOS transistor with its gate connected to the input voltage \( V_{in} \), its source connected to ground, and its drain connected to node P.
   - **M2**: This is a PMOS transistor with its gate connected to the output of the op-amp \( A1(s) \), its source connected to the positive supply voltage, and its drain connected to node P.

3. **Node P**:
   - Node P is the common connection point for the drain of \( M_1 \) and the source of \( M_2 \).

4. **Capacitor (C_L)**:
   - A capacitor \( C_L \) is connected between node P and ground.

5. **Output Voltage (V_{out})**:
   - The output voltage \( V_{out} \) is taken from node P.

6. **Output Impedance (Z_{out})**:
   - The output impedance \( Z_{out} \) is indicated at the output node \( V_{out} \).

The circuit is a typical configuration for a two-stage op-amp, where the first stage is a differential amplifier formed by the op-amp \( A1(s) \) and the second stage is a common-source amplifier formed by the transistors \( M_1 \) and \( M_2 \). The capacitor \( C_L \) is used for frequency compensation to ensure stability.
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
The image is a Bode plot that shows the frequency response of two different cascode amplifier configurations: the Original Cascode and the Regulated Cascode. The plot is on a logarithmic scale for both the magnitude (|Vout/Vin|) and the frequency (ω).

1. **Axes**:
   - The vertical axis represents the magnitude of the voltage gain (|Vout/Vin|) in decibels (dB).
   - The horizontal axis represents the frequency (ω) on a logarithmic scale.

2. **Original Cascode**:
   - The gain of the Original Cascode is represented by a dashed horizontal line at the level of \( g_{m1} r_{o1} g_{m2} r_{o2} \).
   - The bandwidth of the Original Cascode is indicated by the point where the dashed line intersects the vertical line at \( \frac{1}{g_{m2} r_{o2} r_{o1} C_L} \).

3. **Regulated Cascode**:
   - The gain of the Regulated Cascode is higher than that of the Original Cascode, represented by a solid horizontal line at the level of \( A_0 g_{m1} r_{o1} g_{m2} r_{o2} \).
   - The bandwidth of the Regulated Cascode is indicated by the point where the solid line starts to slope downwards, intersecting the vertical line at \( \frac{1}{A_0 g_{m1} r_{o1} g_{m2} r_{o2} C_L} \).
   - The slope of the Regulated Cascode's response decreases at higher frequencies, intersecting additional vertical lines at \( \frac{1}{g_{m2} r_{o2} r_{o1} C_L} \) and \( \frac{1}{g_{m2} r_{o2} r_{o1} C_L} + A_0 \omega_0 \).

4. **Key Parameters**:
   - \( A_0 \): Open-loop gain of the amplifier.
   - \( g_{m1}, g_{m2} \): Transconductance of the first and second transistors, respectively.
   - \( r_{o1}, r_{o2} \): Output resistance of the first and second transistors, respectively.
   - \( C_L \): Load capacitance.
   - \( \omega_0 \): A frequency term associated with the regulated cascode.

The plot illustrates that the Regulated Cascode configuration provides a higher gain compared to the Original Cascode, but with a more complex frequency response that includes additional poles, leading to a more gradual roll-off in gain at higher frequencies.
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
The image consists of two parts labeled (a) and (b), each depicting different electronic circuit diagrams and their corresponding characteristics.

(a) The first part shows a basic operational amplifier (op-amp) circuit and its frequency response. The diagram on the left side illustrates a sinusoidal input signal being fed into an op-amp. The op-amp is represented by a triangle with two input terminals (one marked with a plus sign for the non-inverting input and one with a minus sign for the inverting input) and one output terminal. The output signal is also sinusoidal but with a larger amplitude, indicating amplification. Next to this, there is a graph plotting the gain (|V_out/V_in|) against the input voltage (V_in). The graph shows that the gain remains constant up to a certain input voltage (V1) and then starts to decrease, indicating the frequency response of the op-amp.

(b) The second part shows a non-inverting amplifier circuit using an op-amp. The input signal is a sinusoidal wave fed into the non-inverting input of the op-amp. The inverting input is connected to a voltage divider formed by two resistors, R1 and R2. R1 is connected between the inverting input and ground, while R2 is connected between the inverting input and the output of the op-amp. The output voltage (V_out) is taken from the output terminal of the op-amp. This configuration indicates a feedback loop that sets the gain of the amplifier.

Overall, the image provides a visual representation of an op-amp's amplification properties and a specific non-inverting amplifier circuit configuration.
```

**Figure 9.39** (a) Simulation of gain versus input amplitude, and (b) feedback amplifier.

The reader may wonder how much gain reduction is acceptable. In some applications, the reduction of the open-loop gain, and hence the gain error of the closed-loop system, are critical (Chapter 13). In other applications, we are concerned with the output distortion of the *closed-loop* circuit. In such a case, we place the op amp in the closed-loop environment of interest, e.g., the inverting configuration of Fig. 9.39(b), apply a sinusoid to the input, and measure the distortion (harmonics) at the output in simulations. The maximum output amplitude that yields an acceptable distortion is considered the maximum output swing.

# **9.7 Common-Mode Feedback**

### **9.7.1 Basic Concepts**

In this and previous chapters, we have described many advantages of fully differential circuits over their single-ended counterparts. In addition to greater output swings, differential op amps avoid mirror poles, thus achieving a higher closed-loop speed. However, high-gain differential circuits require "commonmode feedback" (CMFB).

To understand the need for CMFB, let us begin with a simple realization of a differential amplifier [Fig. 9.40(a)]. In some applications, we short the inputs and outputs for part of the operation [Fig. 9.40(b)],

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), each depicting a differential amplifier configuration.

**Diagram (a):**
- The top part shows a simple operational amplifier symbol with a positive (+) and negative (-) input.
- Below the op-amp symbol, there is a detailed transistor-level circuit.
- The circuit includes two NMOS transistors labeled M1 and M2.
- The source terminals of M1 and M2 are connected together and to a current source labeled I_SS, which is connected to the ground.
- The drain terminals of M1 and M2 are connected to resistors labeled R_D, which are in turn connected to the positive supply voltage V_DD.
- The gate terminal of M1 is connected to the input voltage V_in.
- The output voltage V_out is taken from the common connection point of the drain terminals of M1 and M2.

**Diagram (b):**
- Similar to diagram (a), the top part shows an operational amplifier symbol with a positive (+) and negative (-) input.
- Below the op-amp symbol, there is a more detailed transistor-level circuit.
- This circuit also includes two NMOS transistors labeled M1 and M2.
- The source terminals of M1 and M2 are connected together and to a current source labeled I_SS, which is connected to the ground.
- The drain terminals of M1 and M2 are connected to resistors labeled R_D, which are in turn connected to the positive supply voltage V_DD.
- The gate terminals of M1 and M2 are connected to the input voltage V_in.
- The output voltage V_out is taken from the common connection point of the drain terminals of M1 and M2.

Both diagrams illustrate differential amplifier configurations with slight variations in the input connections to the transistors.
```

**Figure 9.40** (a) Simple differential pair; (b) circuit with inputs shorted to outputs.

providing *differential* negative feedback. The input and output common-mode levels in this case are fairly well defined, equal to *VDD* − *ISS RD/*2.

Now suppose the load resistors are replaced by PMOS current sources so as to increase the differential voltage gain [Fig. 9.41(a)]. What is the common-mode level at nodes *X* and *Y* ? Since each of the input transistors carries a current of *ISS/*2, the CM level depends on how close *ID*<sup>3</sup> and *ID*<sup>4</sup> are to this value. In practice, as exemplified by Fig. 9.41(b), mismatches in the PMOS and NMOS current mirrors defining *ISS* and *ID*<sup>3</sup>*,*<sup>4</sup> create a finite error between *ID*<sup>3</sup>*,*<sup>4</sup> and *ISS/*2. Suppose, for example, that the drain currents of *M*<sup>3</sup> and *M*<sup>4</sup> in the saturation region are slightly greater than *ISS/*2. As a result, to satisfy Kirchhoff's current law at nodes *X* and *Y* , both *M*<sup>3</sup> and *M*<sup>4</sup> must enter the triode region so that their drain currents fall to *ISS/*2. Conversely, if *ID*<sup>3</sup>*,*<sup>4</sup> *< ISS/*2, then both *VX* and *VY* must drop so that *M*<sup>5</sup> enters the triode region, thereby producing only 2*ID*<sup>3</sup>*,*4.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), which appear to be differential amplifier circuits using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).

### Circuit (a):
- **Transistors:**
  - M1 and M2 are NMOS transistors with their sources connected together and to a current source ISS, which is connected to ground.
  - M3 and M4 are PMOS transistors with their sources connected to VDD (the positive supply voltage).
- **Connections:**
  - The gates of M1 and M2 are the input nodes labeled X and Y, respectively.
  - The drains of M1 and M3 are connected together, forming the node X.
  - The drains of M2 and M4 are connected together, forming the node Y.
  - The gates of M3 and M4 are connected to a bias voltage Vb.
  - The output voltage Vout is taken from the node between the drains of M1 and M2.

### Circuit (b):
- **Transistors:**
  - M1 and M2 are NMOS transistors with their sources connected together and to the drain of another NMOS transistor M5.
  - M3 and M4 are PMOS transistors with their sources connected to VDD.
  - Mb1 and Mb2 are additional NMOS transistors used for biasing.
- **Connections:**
  - The gates of M1 and M2 are the input nodes labeled X and Y, respectively.
  - The drains of M1 and M3 are connected together, forming the node X.
  - The drains of M2 and M4 are connected together, forming the node Y.
  - The gates of M3 and M4 are connected to the drain of Mb2.
  - The source of Mb2 is connected to VDD, and its gate is connected to the drain of Mb1.
  - The source of Mb1 is connected to ground, and its gate is connected to a bias voltage.
  - The source of M5 is connected to a current source ISS, which is connected to ground.
  - The output voltage Vout is taken from the node between the drains of M1 and M2.
  - There is a resistor connected between the gate of Mb2 and the drain of Mb1.

### Additional Details:
- The transistors in circuit (b) have their width-to-length ratios (W/L) indicated, with M1, M2, Mb1, and Mb2 having a ratio of W/L, and M5 having a ratio of 2W/L.
- Both circuits are designed to amplify the difference between the input signals at nodes X and Y, with circuit (b) having additional biasing and current mirror configurations for improved performance.

These circuits are commonly used in analog integrated circuit design for applications requiring differential amplification.
```

**Figure 9.41** (a) High-gain differential pair with inputs shorted to outputs, and (b) effect of current mismatches.

The above difficulties fundamentally arise because in high-gain amplifiers, we wish a *p*-type current source [e.g., *M*<sup>3</sup> and *M*<sup>4</sup> in Fig. 9.41(b)] to balance an *n*-type current source (e.g., *M*5). As illustrated in Fig. 9.42, the difference between *IP* and *IN* must flow through the intrinsic output impedance of the

Here is the image describtion:
```
The image depicts a simplified model of a high-gain amplifier circuit. The circuit consists of two current sources, \( I_P \) and \( I_N \), and two resistors, \( R_P \) and \( R_N \). 

- \( I_P \) is a current source connected to the positive supply voltage \( V_{DD} \) and is directed downwards.
- \( R_P \) is a resistor connected between \( V_{DD} \) and the node where \( I_P \) and \( I_N \) meet.
- \( I_N \) is another current source connected to the ground and is directed upwards.
- \( R_N \) is a resistor connected between the node where \( I_P \) and \( I_N \) meet and the ground.

The node where \( I_P \) and \( I_N \) meet is labeled with the current \( I_P - I_N \) flowing through it. The circuit is labeled as "Figure 9.42 Simplified model of high-gain amplifier."
```

amplifier, creating an output voltage change of *(IP* − *IN )(RP* %*RN )*. Since the current error depends on mismatches and *RP* %*RN* is quite high, the voltage error may be large, thus driving the *p*-type or *n*-type current source into the triode region. As a general rule, if the output CM level cannot be determined by "visual inspection" and requires calculations based on device properties, then it is poorly defined. This is the case in Fig. 9.41 but not in Fig. 9.40. We emphasize that differential feedback cannot define the CM level.

Students often make two mistakes here. First, they assume that differential feedback corrects the output common-mode level. As explained for the simple circuit of Fig. 9.41(a), differential feedback from *X* and *Y* to the inputs cannot prohibit the output CM level from taking off toward *VDD* or ground. Second, they finely adjust *Vb* in simulations so as to bring *VX* and *VY* to around *VDD/*2 concluding that the circuit does not need CM feedback. We have recognized, however, that random mismatches between the top and bottom current sources cause the CM level to fall or rise considerably. Such mismatches are always present in actual circuits and cause the op amp to fail if no CMFB is used.

#### ▲**Example 9.16**

Razavi-3930640 book December 17, 201516:59 376

Consider the telescopic op amp designed in Example 9.5 and repeated in Fig. 9.43 with bias current mirrors. Suppose *M*<sup>9</sup> suffers from a 1% current mismatch with respect to *M*10, producing *ISS* = 2*.*97 mA rather than 3 mA. Assuming perfect matching for other transistors, explain what happens in the circuit.

Here is the image describtion:
```
The image depicts a schematic diagram of a CMOS operational amplifier circuit. The circuit consists of multiple MOSFET transistors arranged in a specific configuration to achieve amplification. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a positive supply voltage \( V_{DD} \) at the top.

2. **Current Source:**
   - A current source of 300 µA is connected to a resistor \( R_1 \), which is connected to the gate of transistor \( M_{11} \).

3. **Transistors:**
   - **\( M_{11} \)**: A PMOS transistor connected to \( V_{DD} \) and the current source.
   - **\( M_{10} \)**: An NMOS transistor connected to ground.
   - **\( M_7 \) and \( M_8 \)**: PMOS transistors connected in a current mirror configuration with their sources connected to \( V_{DD} \).
   - **\( M_5 \) and \( M_6 \)**: PMOS transistors connected in a differential pair configuration with their sources connected to the drains of \( M_7 \) and \( M_8 \), respectively.
   - **\( M_3 \) and \( M_4 \)**: NMOS transistors connected in a differential pair configuration with their sources connected to the drains of \( M_5 \) and \( M_6 \), respectively.
   - **\( M_1 \) and \( M_2 \)**: NMOS transistors connected in a differential pair configuration with their sources connected to the drain of \( M_9 \).
   - **\( M_9 \)**: An NMOS transistor acting as a current source with a current \( I_{SS} = 2.97 \) mA.

4. **Bias Voltages:**
   - \( V_{b1} \) and \( V_{b2} \) are bias voltages applied to the gates of \( M_3 \), \( M_4 \), \( M_5 \), and \( M_6 \).

5. **Input and Output:**
   - \( V_{in} \) is the input voltage applied to the gate of \( M_1 \).
   - \( V_{out} \) is the output voltage taken from the node between \( M_6 \) and \( M_8 \).

6. **Nodes:**
   - Nodes X and Y are intermediate points in the circuit, with X being the connection between \( M_5 \) and \( M_3 \), and Y being the connection between \( M_6 \) and \( M_4 \).

The circuit is designed to amplify the input signal \( V_{in} \) and produce an amplified output signal \( V_{out} \). The arrangement of transistors and current sources ensures proper biasing and operation of the amplifier.
```

### **Solution**

From Example 9.5, the single-ended output impedance of the circuit equals 266 k%. Since the difference between the drain currents of *M*<sup>3</sup> and *M*<sup>5</sup> (and *M*<sup>4</sup> and *M*6) is 30 *µ*A*/*2 = 15 *µ*A, the output voltage error would be 266 k%×15 *µ*A= 3*.*99 V. Since this large error cannot be produced, *VX* and *VY* must rise so much that *M*5–*M*<sup>6</sup> and *M*7–*M*<sup>8</sup> enter the triode region, yielding *ID*<sup>7</sup>*,*<sup>8</sup> = 1*.*485 mA. We should also mention that another important source

of CM error in the simple biasing scheme of Fig. 9.43 is the *deterministic* error between *ID*<sup>7</sup>*,*<sup>8</sup> and *ID*<sup>11</sup> (and also between *ID*<sup>9</sup> and *ID*10) due to their different drain-source voltages. This error can nonetheless be reduced by means of the current mirror techniques of Chapter 5.

The foregoing study implies that in high-gain amplifiers, the output CM level is sensitive to device properties and mismatches and it cannot be stabilized by means of *differential* feedback. Thus, a commonmode feedback network must be added to sense the CM level of the two outputs and adjust one of the bias currents in the amplifier. Following our view of feedback systems in Chapter 8, we divide the task of CMFB into three operations: sensing the output CM level, comparison with a reference, and returning the error to the amplifier's bias network. Figure 9.44 conceptually illustrates the idea.

Here is the image describtion:
```
The image depicts a circuit diagram that includes several key components and connections. Here is a detailed description:

1. **Power Supply (V_DD)**: The circuit is powered by a voltage source labeled V_DD at the top of the diagram.

2. **Current Sources**: There are two current sources depicted as circles with arrows inside them. One current source is connected to the node labeled V_out1, and the other is connected to the node labeled V_out2. Both current sources are connected to the V_DD line.

3. **Transistors (M1 and M2)**: The circuit includes two transistors, labeled M1 and M2. These transistors are positioned horizontally and are connected in a differential pair configuration. The source of M1 is connected to the source of M2, and this common source node is connected to a current source that is grounded.

4. **Output Nodes (V_out1 and V_out2)**: The drains of M1 and M2 are connected to the nodes V_out1 and V_out2, respectively. These nodes are also connected to the current sources mentioned earlier.

5. **CM Level Sense Circuit**: The V_out2 node is connected to a block labeled "CM Level Sense Circuit." This block is responsible for sensing the common-mode level of the output.

6. **Operational Amplifier**: The output of the CM Level Sense Circuit is connected to the non-inverting input (+) of an operational amplifier (op-amp). The inverting input (-) of the op-amp is connected to a reference voltage labeled V_REF.

7. **Feedback Loop**: The output of the op-amp is connected back to the gate of the transistor M2, forming a feedback loop that helps regulate the circuit.

Overall, this circuit appears to be a differential amplifier with a common-mode feedback mechanism to stabilize the common-mode output voltage. The CM Level Sense Circuit and the op-amp work together to ensure that the common-mode voltage is maintained at a desired level, as set by the reference voltage V_REF.
```

**Figure 9.44** Conceptual topology for common-mode feedback.

# **9.7.2 CM Sensing Techniques**

In order to sense the output CM level, we recall that *Vout,C M* = *(Vout*1+*Vout*2*)/*2, where *Vout*<sup>1</sup> and *Vout*<sup>2</sup> are the single-ended outputs. It therefore seems plausible to employ a resistive divider as shown in Fig. 9.45, generating *Vout,C M* = *(R*1*Vout*<sup>2</sup> + *R*2*Vout*1*)/(R*<sup>1</sup> + *R*2*)*, which reduces to *(Vout*<sup>1</sup> + *Vout*2*)/*2 if *R*<sup>1</sup> = *R*2. The difficulty, however, is that *R*<sup>1</sup> and *R*<sup>2</sup> must be much greater than the output impedance of the op amp so as to avoid lowering the open-loop gain. For example, in the design of Fig. 9.43, the output impedance equals 266 k%, necessitating a value of several megaohms for *R*<sup>1</sup> and *R*2. As explained in Chapter 18, such large resistors occupy a very large area and, more important, suffer from substantial parasitic capacitance to the substrate.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the components and their arrangement:

1. **Transistors**: The circuit consists of multiple transistors, which appear to be MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). There are six transistors in total, arranged in pairs.

2. **Resistors**: There are two resistors labeled R1 and R2. These resistors are connected in series between two nodes, Vout1 and Vout2.

3. **Nodes**: 
   - **Vout1**: This is the output node on the left side of the circuit.
   - **Vout2**: This is the output node on the right side of the circuit.
   - **Vout,CM**: This is the common-mode output node, which is connected to the midpoint between R1 and R2.

4. **Connections**:
   - The top pair of transistors are connected to a common power supply rail at the top.
   - The middle pair of transistors are connected to the output nodes Vout1 and Vout2.
   - The bottom pair of transistors are connected to the ground.

5. **Feedback Mechanism**: The common-mode feedback (CMFB) is implemented to stabilize the common-mode voltage. The Vout,CM node is used to sense the common-mode voltage and provide feedback to the circuit.

6. **Power Supply and Ground**: The circuit is powered by a supply voltage at the top and is grounded at the bottom.

This differential amplifier with CMFB is typically used in analog circuits to amplify the difference between two input signals while rejecting any common-mode signals. The resistors R1 and R2 help in setting the gain and the common-mode feedback ensures that the common-mode voltage is regulated.
```

Here is the image describtion:
```
The image is a caption for Figure 9.45, which describes a concept related to electrical engineering or electronics. The caption reads: "Figure 9.45 Common-mode feedback with resistive sensing." This suggests that the figure likely illustrates a circuit or system that employs common-mode feedback using resistive components to sense and control the common-mode signal. However, the actual diagram or visual representation of the circuit is not provided in the image.
```

To eliminate the resistive loading, we can interpose source followers between each output and its corresponding resistor. Illustrated in Fig. 9.46, this technique produces a CM level that is in fact lower than the output CM level by *VG S*<sup>7</sup>*,*8, but this shift can be taken into account in the comparison operation. Note that *R*<sup>1</sup> and *R*<sup>2</sup> or *I*<sup>1</sup> and *I*<sup>2</sup> must be large enough to ensure that *M*<sup>7</sup> or *M*<sup>8</sup> is not "starved" when

▲

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. The circuit consists of multiple MOSFET transistors, resistors, and current sources. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage (V_DD).

2. **MOSFET Transistors**:
   - **M1, M2, M3, M4, M5, M6, M7, and M8**: These are the MOSFET transistors used in the circuit. The transistors are arranged in pairs and connected in a specific configuration to form the differential amplifier.
   - **M1 and M2**: These transistors are connected in a differential pair configuration with their sources connected together and to the current source I1.
   - **M3 and M4**: These transistors are connected in a current mirror configuration to provide a constant current to the differential pair.
   - **M5 and M6**: These transistors are connected in another current mirror configuration to mirror the current from M3 and M4.
   - **M7 and M8**: These transistors are connected as load transistors for the differential pair, with their sources connected to the current mirrors formed by M3, M4, M5, and M6.

3. **Current Sources (I1 and I2)**:
   - **I1**: This current source is connected to the sources of M1 and M2, providing a constant current to the differential pair.
   - **I2**: This current source is connected to the output node V_out,CM through resistors R1 and R2, providing a constant current to the output stage.

4. **Resistors (R1 and R2)**: These resistors are connected in series between the drain of M8 and the output node V_out,CM. They form a voltage divider network to set the common-mode output voltage.

5. **Output Nodes (V_out1, V_out2, and V_out,CM)**:
   - **V_out1**: This is the output node connected to the drain of M7.
   - **V_out2**: This is the output node connected to the drain of M8.
   - **V_out,CM**: This is the common-mode output voltage node, which is the midpoint of the voltage divider formed by R1 and R2.

The circuit operates as a differential amplifier, amplifying the difference between the input signals applied to the gates of M1 and M2. The amplified differential signal is available at the output nodes V_out1 and V_out2, while the common-mode output voltage is available at V_out,CM.
```

**Figure 9.46** Common-mode feedback using source followers.

a large differential swing appears at the output. As conceptually depicted in Fig. 9.47, if, say, *Vout*<sup>2</sup> is quite higher than *Vout*1, then *I*<sup>1</sup> must sink both *IX* ≈ *(Vout*<sup>2</sup> − *Vout*1*)/(R*<sup>1</sup> + *R*2*)* and *ID*7. Consequently, if *R*<sup>1</sup> + *R*<sup>2</sup> or *I*<sup>1</sup> is not sufficiently large, *ID*<sup>7</sup> drops to zero and *Vout,C M* no longer represents the true output CM level.

Here is the image describtion:
```
The image depicts a circuit diagram of a differential amplifier with a common-mode feedback (CMFB) mechanism. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage, labeled as V_DD.

2. **Transistors (M7 and M8)**: 
   - M7 and M8 are NMOS transistors. 
   - The source of M7 is connected to a current source I1, which is grounded.
   - The source of M8 is connected to a current source I2, which is also grounded.
   - The gates of M7 and M8 are connected to the input voltages V_out1 and V_out2, respectively.
   - The drains of M7 and M8 are connected to the power supply V_DD.

3. **Resistors (R1 and R2)**:
   - R1 and R2 are resistors connected in series between the drains of M7 and M8.
   - The node between R1 and R2 is labeled as V_out,CM, which represents the common-mode output voltage.
   - A current Ix flows through the resistors R1 and R2.

4. **Current Sources (I1 and I2)**:
   - I1 and I2 are current sources connected to the sources of M7 and M8, respectively, and are grounded.

5. **Output Voltages (V_out1 and V_out2)**:
   - V_out1 is the voltage at the drain of M7.
   - V_out2 is the voltage at the drain of M8.

The circuit is designed to amplify the difference between the input voltages while maintaining a stable common-mode voltage through the feedback mechanism involving R1 and R2. The common-mode feedback helps to stabilize the operating point of the differential amplifier.
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
The image consists of two sub-images labeled (a) and (b), each depicting a different electronic circuit diagram.

(a) The first sub-image shows a more complex circuit with multiple transistors and connections. The circuit includes:
- Several transistors arranged in a stacked configuration.
- Two output nodes labeled Vout1 and Vout2.
- A connection from Vout1 to the gate of a transistor labeled M7.
- A connection from Vout2 to the gate of a transistor labeled M8.
- The source of M7 is connected to ground, and its drain is connected to a node labeled P.
- The source of M8 is also connected to ground, and its drain is connected to the same node P.
- The node P is connected to the gate of another transistor in the circuit.

(b) The second sub-image shows a simplified version of the circuit focusing on the transistors M7 and M8. It includes:
- Two transistors labeled M7 and M8.
- The gate of M7 is connected to Vout1 plus a threshold voltage (VTH).
- The source of M7 is connected to ground, and its drain is connected to a node labeled P.
- The gate of M8 is connected to the node P.
- The source of M8 is connected to ground, and its drain is connected to Vout2.

Overall, the image illustrates a detailed electronic circuit with specific focus on the interaction between the transistors M7 and M8 and their respective output nodes.
```

**Figure 9.48** (a) Common-mode sensing using MOSFETs operating in the deep triode region, and (b) output levels placing *M*<sup>7</sup> at the edge of saturation.

where *W/L* denotes the aspect ratio of *M*<sup>7</sup> and *M*8. Equation (9.49) indicates that *Rtot* is a function of *Vout*<sup>2</sup> + *Vout*<sup>1</sup> but independent of *Vout*<sup>2</sup> − *Vout*1. From Fig. 9.48(a), we observe that if the outputs rise together, then *Rtot* drops, whereas if they change differentially, one *Ron* increases and the other decreases. This resistance can thus be utilized as a measure of the output CM level.

In the circuit of Fig. 9.48(a), the use of *M*<sup>7</sup> and *M*<sup>8</sup> limits the output voltage swings. Here, it may seem that *Vout,min* = *VT H*<sup>7</sup>*,*8, which is relatively close to two overdrive voltages, but the difficulty arises from the assumption above that both *M*<sup>7</sup> and *M*<sup>8</sup> operate in the deep triode region. In fact, if, say, *Vout*<sup>1</sup> drops from the equilibrium CM level to about one threshold voltage above ground [Fig. 9.48(b)] and *Vout*<sup>2</sup> rises by the same amount, then *M*<sup>7</sup> enters the saturation region, thus exhibiting a variation in its on-resistance that is not counterbalanced by that of *M*8.

It is important to bear in mind that CM sensing must produce a quantity *independent* of the differential signals. The following example illustrates this point.

#### ▲**Example 9.17**

A student simulates the step response of a closed-loop op amp circuit [e.g., that in Fig. 9.48(a)] and observes the output waveforms shown in Fig. 9.49. Explain why *Vout*<sup>1</sup> and *Vout*<sup>2</sup> do not change symmetrically.

Here is the image describtion:
```
The image is a graph depicting the behavior of two output voltages, Vout1 and Vout2, over time (t). The graph includes three curves: Vout1, Vout2, and VCM. 

- Vout1 starts at a certain value and increases over time, reaching a higher steady-state value after time t2.
- Vout2 starts at a higher value than Vout1 and decreases over time, reaching a lower steady-state value after time t2.
- VCM is a dashed line that represents the common-mode voltage. It starts at a value between Vout1 and Vout2 and remains constant over time.

The graph has two vertical dashed lines at times t1 and t2, indicating specific moments in time. The horizontal axis represents time (t), and the vertical axis represents voltage. The figure is labeled as "Figure 9.49" in the bottom right corner.
```

### **Solution**

As evident from the waveforms, the output CM level *changes*from *t*<sup>1</sup> to *t*2, indicating that the CM sensing mechanism is nonlinear and interprets the CM levels at *t*<sup>1</sup> and *t*<sup>2</sup> differently. For example, if *M*<sup>7</sup> or *M*<sup>8</sup> in Fig. 9.48 does not remain in the deep triode region at *t*2, then Eq. (9.49) no longer holds and *VC M* becomes a function of the *differential* signals. ▲

Another CM sensing method is illustrated in Fig. 9.50. Here, the differential pairs compare the inputs with *VREF*, generating a current, *IC M* , in proportion to the input CM level. To prove this point, we write the small-signal drain currents of *M*<sup>2</sup> and *M*<sup>4</sup> as *(gm/*2*)Vout*<sup>1</sup> and *(gm/*2*)Vout*2, respectively, concluding that *IC M* ∝ *Vout*<sup>1</sup> + *Vout*2. This current can be copied to current sources within the op amp with negative feedback so as to keep *Vout,C M* approximately equal to *VREF*.

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit, commonly used in operational amplifiers (op-amps). The circuit consists of four MOSFET transistors labeled M1, M2, M3, and M4, and a current mirror configuration.

Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are the input transistors of the differential pair. The gate of M1 is connected to the input voltage \( V_{out1} \), and the gate of M2 is connected to a bias voltage \( V_b \).
   - **M3 and M4:** These transistors form the current mirror. The gate of M3 is connected to the gate of M4, and the drain of M3 is connected to the drain of M4.

2. **Current Sources:**
   - There are two current sources depicted as circles with arrows pointing downwards, connected to the sources of M1 and M3, respectively. These current sources are connected to the ground.

3. **Connections:**
   - The drain of M1 is connected to the source of M2.
   - The drain of M2 is connected to the gate of M4 and the drain of M4.
   - The source of M4 is connected to the drain of M3.
   - The source of M3 is connected to the current source and then to the ground.
   - The output voltage \( V_{out2} \) is taken from the drain of M3.

4. **Current Mirror:**
   - The current mirror is formed by M3 and M4, with the current \( I_{CM} \) flowing through M4 and mirrored to M3.

5. **Output:**
   - The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drain of M1 and the drain of M3, respectively.

6. **Additional Connections:**
   - There is a connection labeled "To Current Sources in Op Amp" indicating that the current mirror is connected to other current sources within the operational amplifier.

This differential amplifier circuit is used to amplify the difference between the input signals \( V_{out1} \) and \( V_b \), providing high gain and common-mode rejection.
```

**Figure 9.50** CM sensing circuit with high nonlinearity.

The foregoing topology faces serious issues. As *Vout*<sup>1</sup> and *Vout*<sup>2</sup> experience large swings, *Iout* no longer remains proportional to *Vout*<sup>1</sup> +*Vout*<sup>2</sup> due to the nonlinearity of the differential pairs. In fact, if *ID*<sup>1</sup> and *ID*<sup>2</sup> are expressed as *f (Vout*<sup>1</sup> − *VREF)* and *f (Vout*<sup>2</sup> − *VREF)*, respectively, we observe that *ID*<sup>1</sup> + *ID*<sup>2</sup> depends on the individual values of *Vout*<sup>1</sup> and *Vout*<sup>2</sup> unless *f ()* is a linear function. As a result, the reconstructed CM level does not remain constant in the presence of large differential output swings.

### **9.7.3 CM Feedback Techniques**

We now study techniques of comparing the measured CM level with a reference and returning the error to the op amp's bias network. In the circuit of Fig. 9.51, we employ a simple amplifier to detect the difference between *Vout,C M* and a reference voltage, *VREF*, applying the result to the NMOS current sources with negative feedback. If both *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, so does *VE* , thereby increasing the drain currents of *M*3–*M*<sup>4</sup> and lowering the output CM level. In other words, if the loop gain is large, the feedback network forces the CM level of *Vout*<sup>1</sup> and *Vout*<sup>2</sup> to approach *VREF*. Note that the feedback can be applied to the PMOS current sources as well. Also, the feedback may control only a fraction of the current to allow optimization of

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with common-mode feedback. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a common-mode feedback loop.
   - **M3 and M4:** These are the transistors used in the common-mode feedback circuit. The gate of M3 is connected to the source of M1, and the gate of M4 is connected to the source of M2.

2. **Current Source:**
   - **I_SS:** This is a current source connected to the common source node of M1 and M2, providing a constant current.

3. **Resistors:**
   - **R1 and R2:** These resistors are connected in series between the drains of M1 and M2, forming the load resistors for the differential pair. The node between R1 and R2 is connected to the common-mode feedback circuit.

4. **Capacitors:**
   - There are capacitors connected to the gates of M1, M2, M3, and M4, indicating AC coupling or bypass capacitors.

5. **Power Supply:**
   - **V_DD:** This is the positive power supply voltage connected to the drains of M1 and M2 through the load resistors R1 and R2.

6. **Common-Mode Feedback Circuit:**
   - **Operational Amplifier (Op-Amp):** The op-amp is used for common-mode feedback. The non-inverting input (+) is connected to a reference voltage \( V_{REF} \), and the inverting input (-) is connected to the common-mode output voltage \( V_{out,CM} \).
   - **V_E:** The output of the op-amp is connected to the gates of M3 and M4, providing the feedback control voltage.

7. **Output Nodes:**
   - **V_{out1} and V_{out2}:** These are the differential output voltages taken from the drains of M1 and M2, respectively.

The circuit operates as a differential amplifier with common-mode feedback to stabilize the common-mode output voltage. The op-amp adjusts the gate voltages of M3 and M4 to maintain the desired common-mode voltage at the output.
```

**Figure 9.51** Sensing and controlling output CM level.

the settling behavior. For example, each of *M*<sup>3</sup> and *M*<sup>4</sup> can be decomposed into two parallel devices, one biased at a constant current and the other driven by the error amplifier.

In a folded-cascode op amp, the CM feedback may control the tail current of the input differential pair. Illustrated in Fig. 9.52, this method increases the tail current if *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, lowering the drain currents of *M*5–*M*<sup>6</sup> and restoring the output CM level.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with a common-mode feedback (CMFB) circuit. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are the input transistors of the differential pair. The gate of M1 is connected to the input voltage \( V_{in} \), while the gate of M2 is connected to a common-mode feedback circuit.
   - **M5 and M6:** These transistors are part of the current mirror load for the differential pair. They are connected to the supply voltage \( V_{DD} \).
   - **Other transistors:** There are additional transistors connected to the sources of M1 and M2, and to the common-mode feedback circuit.

2. **Resistors:**
   - **R1 and R2:** These resistors are connected in series between the output nodes \( V_{out1} \) and \( V_{out2} \). They help in setting the common-mode voltage.

3. **Operational Amplifier:**
   - There is an operational amplifier with its non-inverting input connected to a reference voltage \( V_{REF} \) and its inverting input connected to the common-mode output voltage \( V_{out,CM} \). The output of the operational amplifier is connected to the gate of the transistor that controls the common-mode feedback.

4. **Voltage Nodes:**
   - **\( V_{DD} \):** The supply voltage for the circuit.
   - **\( V_{in} \):** The input voltage to the differential pair.
   - **\( V_{out1} \) and \( V_{out2} \):** The differential output voltages.
   - **\( V_{out,CM} \):** The common-mode output voltage.
   - **\( V_{REF} \):** The reference voltage for the common-mode feedback.

The circuit operates as follows:
- The differential input voltage \( V_{in} \) is applied to the gate of M1, while the gate of M2 is connected to the common-mode feedback circuit.
- The differential pair (M1 and M2) amplifies the difference between \( V_{in} \) and the common-mode voltage.
- The current mirror formed by M5 and M6 ensures that the differential output voltages \( V_{out1} \) and \( V_{out2} \) are properly balanced.
- The common-mode feedback circuit, including the operational amplifier and the resistors R1 and R2, stabilizes the common-mode voltage to the reference voltage \( V_{REF} \).

This configuration is commonly used in analog integrated circuits to ensure proper operation of differential amplifiers by controlling the common-mode voltage.
```

**Figure 9.52** Alternative method of controlling output CM level.

How do we perform comparison and feedback with the sensing scheme of Fig. 9.48? Here, the output CM voltage is directly converted to a resistance or a current, prohibiting comparison with a reference voltage. A simple feedback topology utilizing this technique is depicted in Fig. 9.53, where *Ron*7%*Ron*<sup>8</sup> adjusts the bias current of *M*<sup>5</sup> and *M*6. The output CM level sets *Ron*7%*Ron*<sup>8</sup> such that *ID*<sup>5</sup> and *ID*<sup>6</sup> exactly balance *ID*<sup>9</sup> and *ID*10, respectively. For example, if *Vout*<sup>1</sup> and *Vout*<sup>2</sup> rise, *Ron*7||*Ron*<sup>8</sup> falls and the drain currents of *M*<sup>5</sup> and *M*<sup>6</sup> increase, pulling *Vout*<sup>1</sup> and *Vout*<sup>2</sup> down. Assuming that *ID*<sup>9</sup> = *ID*<sup>10</sup> = *ID*, we must have *Vb* − *VG S*<sup>5</sup> = 2*ID(Ron*7%*Ron*8*)*, and hence *Ron*7%*Ron*<sup>8</sup> = *(Vb* − *VG S*5*)/(*2*ID)*. From (9.49),

$$\frac{1}{\mu\_n C\_{ox} \left(\frac{W}{L}\right)\_{7,8} (V\_{out2} + V\_{out1} - 2V\_{TH})} = \frac{V\_b - V\_{GS}}{2I\_D} \tag{9.50}$$

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. The circuit consists of several MOSFET transistors arranged in a specific configuration to achieve differential amplification. Here is a detailed description of the components and their connections:

1. **Transistors M9 and M10**: These are the topmost transistors in the circuit, connected to the supply voltage \( V_{DD} \). They are likely acting as active loads for the differential pair.

2. **Transistors M5 and M6**: These transistors are part of the differential pair. The gates of M5 and M6 are connected to the input signals, and their sources are connected to a common node labeled \( P \).

3. **Transistors M7 and M8**: These transistors are connected to the sources of M5 and M6, respectively, and their sources are connected to the ground. They are likely acting as current sources or sinks.

4. **Output Nodes \( V_{out1} \) and \( V_{out2} \)**: These nodes are the outputs of the differential amplifier, taken from the drains of M5 and M6, respectively.

5. **Bias Voltage \( V_b \)**: This voltage is applied to the gates of M7 and M8 to control their operation, ensuring proper biasing of the differential pair.

6. **Connections**: 
   - The drains of M9 and M10 are connected to \( V_{DD} \).
   - The sources of M9 and M10 are connected to the drains of M5 and M6, respectively.
   - The sources of M5 and M6 are connected to the drains of M7 and M8, respectively.
   - The sources of M7 and M8 are connected to the ground.
   - The gates of M5 and M6 are connected to the input signals.
   - The gates of M7 and M8 are connected to the bias voltage \( V_b \).

This configuration allows the circuit to amplify the difference between the input signals applied to the gates of M5 and M6, producing differential output signals at \( V_{out1} \) and \( V_{out2} \).
```

**Figure 9.53** CMFB using triode devices.

that is,

Razavi-3930640 book December 17, 201516:59 382

$$V\_{out1} + V\_{out2} = \frac{2I\_D}{\mu\_n C\_{ox} \left(\frac{W}{L}\right)\_{7.8}} \frac{1}{V\_b - V\_{GSS}} + 2V\_{TH} \tag{9.51}$$

The CM level can thus be obtained by noting that *VG S*<sup>5</sup> <sup>=</sup> <sup>√</sup>2*ID/*[*µnCox (W/L)*5] <sup>+</sup> *VT H*5*.*

The CMFB network of Fig. 9.53 suffers from several drawbacks. First, the value of the output CM level is a function of device parameters. Second, the voltage drop across *Ron*7%*Ron*<sup>8</sup> limits the output voltage swings. Third, to minimize this drop, *M*<sup>7</sup> and *M*<sup>8</sup> are usually quite wide devices, introducing substantial capacitance at the output. The second issue can be alleviated by applying the feedback to the tail current of the input differential pair (Fig. 9.54), but the other two remain.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with a current mirror load. The circuit consists of multiple MOSFET transistors labeled M1 through M13. Here is a detailed description of the circuit:

1. **Input Stage:**
   - The input signal \( V_{in} \) is applied to the gate of transistor M1.
   - Transistors M1 and M2 form a differential pair, with their sources connected together and to the drain of transistor M9.

2. **Current Mirror:**
   - Transistors M7 and M8 form a current mirror, with their sources connected to ground.
   - The gate of M7 is connected to the gate and drain of M8, and the drain of M7 is connected to the source of M9.
   - The gate of M9 is connected to a bias voltage \( V_b \).

3. **Load Stage:**
   - Transistors M3 and M4 form another current mirror, with their sources connected to the supply voltage \( V_{DD} \).
   - The gate of M3 is connected to the gate and drain of M4, and the drain of M3 is connected to the drain of M1.
   - The drain of M2 is connected to the drain of M4.

4. **Output Stage:**
   - The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drains of M5 and M6, respectively.
   - Transistors M5 and M6 are connected in a cascode configuration with M3 and M4, respectively.
   - The sources of M5 and M6 are connected to the drains of M1 and M2, respectively.

5. **Additional Transistors:**
   - Transistors M10 and M11 are connected in parallel with M1 and M2, respectively, with their sources connected to ground.
   - Transistors M12 and M13 are connected in parallel with M5 and M6, respectively, with their sources connected to the drains of M1 and M2, respectively.

Overall, this circuit is a differential amplifier with a current mirror load, which is commonly used in analog integrated circuits for amplifying differential signals while providing high gain and common-mode rejection.
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
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with a feedback network. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are paired transistors connected in parallel, with their sources connected to a common node.
   - **M5 and M6:** Another pair of transistors connected in parallel, with their sources connected to a common node.
   - **M9:** A single transistor with its gate connected to a bias voltage \( V_b \).

2. **Resistors:**
   - **\( r_{03} \parallel r_{04} \):** This notation indicates that resistors \( r_{03} \) and \( r_{04} \) are connected in parallel.
   - **\( R_{on7} \parallel R_{on8} \):** This indicates that resistors \( R_{on7} \) and \( R_{on8} \) are connected in parallel within the feedback network.

3. **Capacitors:**
   - There are capacitors connected to the gates of transistors M1, M2, M5, and M6, indicating coupling or bypass capacitors.

4. **Current Source:**
   - A current source \( I_F \) is shown within the feedback network, with the expression \( I_F = (g_{m7} + g_{m8}) V_{out,CM} \), where \( g_{m7} \) and \( g_{m8} \) are transconductance parameters, and \( V_{out,CM} \) is the common-mode output voltage.

5. **Feedback Network:**
   - The feedback network is enclosed in a dashed box and includes the parallel resistors \( R_{on7} \parallel R_{on8} \), the current source \( I_F \), and connections to ground and the common-mode output voltage \( V_{out,CM} \).

6. **Output:**
   - The output voltage \( V_{out,CM} \) is taken from a node connected to the sources of M5 and M6, and it is also connected to a resistor network \( \frac{g_{m12} r_{012} r_{010}}{2} \) which is grounded.

7. **Bias Voltage:**
   - A bias voltage \( V_b \) is applied to the gate of transistor M9.

The circuit appears to be designed for differential signal processing with a feedback mechanism to control the common-mode output voltage. The use of parallel transistors and resistors, along with the feedback network, suggests a design focused on stability and precise control of the output characteristics.
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
The image depicts a complex electronic circuit diagram, likely representing a differential amplifier or a similar analog circuit. Here is a detailed description of the components and their connections:

1. **Power Supply and Reference Voltage:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \).
   - There is a reference voltage \( V_{REF} \) connected to the gate of transistor \( M_{15} \).

2. **Current Source:**
   - A current source \( I_1 \) is connected to the drain of transistor \( M_{15} \).

3. **Transistors:**
   - The circuit consists of multiple MOSFET transistors labeled \( M_1 \) to \( M_{16} \).
   - \( M_{15} \) and \( M_{16} \) form a current mirror with \( M_{15} \) connected to \( V_{REF} \) and \( M_{16} \) connected to the current source \( I_1 \).
   - \( M_1 \) and \( M_2 \) are the input transistors with their gates connected to the input voltage \( V_{in} \).
   - \( M_9 \) is connected to the sources of \( M_1 \) and \( M_2 \), forming a differential pair.
   - \( M_7 \) and \( M_8 \) are connected to the source of \( M_9 \) and are grounded.
   - \( M_4 \) and \( M_3 \) are connected in series between \( V_{DD} \) and the drain of \( M_1 \).
   - \( M_6 \) and \( M_5 \) are connected in series between \( V_{DD} \) and the drain of \( M_2 \).
   - \( M_{12} \) and \( M_{13} \) are connected in series between the source of \( M_9 \) and ground.
   - \( M_{10} \) and \( M_{11} \) are connected in series between the source of \( M_9 \) and ground.

4. **Outputs:**
   - The circuit has two output nodes labeled \( V_{out1} \) and \( V_{out2} \).
   - \( V_{out1} \) is taken from the drain of \( M_6 \).
   - \( V_{out2} \) is taken from the drain of \( M_5 \).

5. **Connections:**
   - The gate of \( M_9 \) is connected to the source of \( M_{15} \) and the drain of \( M_{16} \), forming a bias voltage \( V_b \).
   - The sources of \( M_1 \) and \( M_2 \) are connected to the drain of \( M_9 \).
   - The gates of \( M_4 \) and \( M_3 \) are connected to the drain of \( M_1 \).
   - The gates of \( M_6 \) and \( M_5 \) are connected to the drain of \( M_2 \).

This circuit appears to be a differential amplifier with current mirror loads and possibly a cascode configuration to improve performance characteristics such as gain and output impedance.
```

$$\left(\mathbb{B}\right)$$

Here is the image describtion:
```
The image depicts a complex electronic circuit diagram, likely representing a differential amplifier or a similar analog circuit. The circuit is composed of multiple MOSFET transistors, labeled M1 through M16, and various connections between them.

Key components and connections in the circuit include:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage (V_DD).

2. **Current Source**: On the left side, there is a current source symbol connected to the power supply line.

3. **Transistors**:
   - **M1 and M2**: These transistors form a differential pair with their gates connected to the input voltage (V_in).
   - **M3 and M4**: These transistors are connected in a cascode configuration with M1 and M2.
   - **M5 and M6**: These transistors are connected to the drains of M1 and M2, respectively, and provide the output voltages (V_out1 and V_out2).
   - **M7 and M8**: These transistors are connected to the source of M9 and are part of a current mirror configuration.
   - **M9**: This transistor is connected to the sources of M1 and M2 and provides a bias voltage (V_b).
   - **M10 and M11**: These transistors are connected to the sources of M12 and M13, respectively, and are part of another current mirror configuration.
   - **M12 and M13**: These transistors are connected to the drains of M5 and M6, respectively.
   - **M15 and M16**: These transistors are connected to a reference voltage (V_REF) and provide a bias current.

4. **Connections**:
   - The gates of M1 and M2 are connected to the input voltage (V_in).
   - The sources of M1 and M2 are connected to the drain of M9.
   - The gates of M7 and M8 are connected to the drain of M9.
   - The sources of M7 and M8 are connected to ground.
   - The gates of M10 and M11 are connected to the drain of M12 and M13, respectively.
   - The sources of M10 and M11 are connected to ground.
   - The gates of M15 and M16 are connected to the reference voltage (V_REF).

Overall, the circuit appears to be a differential amplifier with cascode and current mirror configurations to improve performance characteristics such as gain, output resistance, and bandwidth.
```

**Figure 9.56** Modification of CMFB for more accurate definition of output CM level.

Here is the image describtion:
```
The image depicts a complex circuit diagram of a CMOS operational amplifier (op-amp). The circuit consists of multiple MOSFET transistors, labeled M1 through M18, arranged in a specific configuration to achieve amplification and other desired electrical characteristics.

Key components and their connections in the circuit include:

1. **Current Source**: At the top left, there is a current source symbol providing a constant current to the circuit.

2. **Differential Pair**: Transistors M1 and M2 form a differential pair, with their gates connected to the input voltage \( V_{in} \). This pair is responsible for the initial amplification of the input signal.

3. **Current Mirrors**: Several current mirrors are present in the circuit, such as the ones formed by M3, M4, M5, and M6, which help in copying and controlling currents through different branches of the circuit.

4. **Active Loads**: Transistors M3 and M4 act as active loads for the differential pair, enhancing the gain of the amplifier.

5. **Biasing Network**: Transistors M7, M8, M9, M10, M11, M12, M13, M15, and M16 form a biasing network that sets the operating point of the transistors in the circuit. The voltage \( V_b \) is a bias voltage that helps in setting the correct operating conditions.

6. **Output Stage**: The output stage consists of transistors M5 and M6, which provide the amplified output signals \( V_{out1} \) and \( V_{out2} \).

7. **Reference Voltage**: The circuit includes a reference voltage \( V_{REF} \) connected to the gates of M15 and M16, which helps in stabilizing the operating point of the amplifier.

8. **Power Supply**: The circuit is powered by a positive supply voltage \( V_{DD} \) at the top and a ground connection at the bottom.

Overall, the circuit is designed to amplify the differential input signal \( V_{in} \) and provide amplified output signals \( V_{out1} \) and \( V_{out2} \). The arrangement of MOSFETs and the use of current mirrors and active loads are typical in CMOS op-amp designs to achieve high gain, stability, and proper biasing.
```

**Figure 9.57** Modification to suppress error due to channel-length modulation.

Here is the image describtion:
```
The image consists of three circuit diagrams labeled (a), (b), and (c). Each diagram represents a different configuration of a differential amplifier circuit.

(a) The first circuit diagram shows a basic differential amplifier. It includes:
- Two NMOS transistors, M1 and M2, with their sources connected together and to a current source labeled ISS, which is connected to ground.
- The gates of M1 and M2 are the input terminals, labeled Vin.
- The drains of M1 and M2 are connected to the drains of two PMOS transistors, M3 and M4, respectively.
- The sources of M3 and M4 are connected to the positive supply voltage, VDD.
- The output voltage, Vout, is taken from the common node between the drains of M1 and M3, and M2 and M4.

(b) The second circuit diagram is similar to the first but includes additional components:
- It has the same basic structure with NMOS transistors M1 and M2, PMOS transistors M3 and M4, and the current source ISS.
- Additionally, it includes two resistors, RF, connected between the drains of M1 and M3, and M2 and M4, respectively.
- There is also a capacitor labeled P connected between the sources of M3 and M4.

(c) The third circuit diagram is a variation of the second:
- It includes the same NMOS transistors M1 and M2, PMOS transistors M3 and M4, and resistors RF.
- The capacitor P is also present, connected between the sources of M3 and M4.
- Instead of the current source ISS, there is a current source labeled I1 connected to the common source node of M1 and M2 and to ground.

Each circuit represents a different configuration of a differential amplifier with varying components to achieve different performance characteristics.
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
The image consists of three sub-images labeled (a), (b), and (c), each depicting different configurations of a transistor circuit.

(a) The first sub-image shows a detailed transistor circuit with six MOSFETs labeled M1, M2, M3, M4, M5, and M6. The circuit is powered by a voltage source labeled V_DD. The source of M3 is connected to the drain of M1, and the source of M4 is connected to the drain of M2. The gates of M1 and M2 are connected to a common point labeled P. The sources of M1 and M2 are connected to the drains of M5 and M6, respectively, which are grounded. The gate of M3 is connected to a current source, and the gate of M4 is connected to V_DD.

(b) The second sub-image simplifies the circuit from (a) by combining M3 and M4 into a single transistor and M5 and M6 into another single transistor. The circuit shows a common-mode input voltage labeled V_in,CM applied to the gates of M1 and M2. The output voltage V_out,CM is taken from the common point between the drains of M3 and M4. The sources of M1 and M2 are connected to the combined transistor M5 + M6, which is grounded.

(c) The third sub-image further simplifies the circuit into an equivalent small-signal model. It shows a resistor labeled r_o3,4/2 connected to the drain of M1 + M2. The common-mode input voltage V_in,CM is applied to the gate of M1 + M2. The source of M1 + M2 is connected to a block labeled P, which contains a resistor R_tail and a current source g_m,tail V_out,CM. The output voltage V_out,CM is taken from the common point between the resistor r_o3,4/2 and the drain of M1 + M2.

Overall, the image illustrates the progression from a detailed transistor circuit to a simplified equivalent small-signal model, highlighting the key components and their connections.
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
The image consists of three sub-images labeled (a), (b), and (c), each depicting different configurations of a differential amplifier circuit with common-mode feedback.

(a) The first sub-image shows a basic differential amplifier circuit. It includes:
- Two NMOS transistors, M1 and M2, forming the differential pair with their sources connected to a current source ISS.
- The gates of M1 and M2 are connected to the input signals Vin and a reference voltage.
- The drains of M1 and M2 are connected to the sources of PMOS transistors M3 and M4, respectively.
- The gates of M3 and M4 are connected to a bias voltage Vb1.
- The drains of M3 and M4 are connected to the power supply VDD.
- The output voltages Vout1 and Vout2 are taken from the drains of M5 and M6, respectively.
- M5 and M6 are PMOS transistors with their gates connected to Vb1 and their sources connected to VDD.
- M7 and M8 are NMOS transistors with their gates connected to Vb2 and their sources connected to ground.

(b) The second sub-image shows a common-mode feedback (CMFB) circuit. It includes:
- The output voltages Vout1 and Vout2 from the differential amplifier are fed into a common-mode sense circuit labeled "CM Sense."
- The CM Sense circuit is connected to an operational amplifier with a gain Ae.
- The output of the operational amplifier is connected to the gates of M7 and M8, providing the common-mode feedback to stabilize the output common-mode voltage to a reference voltage VREF.

(c) The third sub-image combines the differential amplifier circuit with the common-mode feedback circuit. It includes:
- The same differential amplifier configuration as in (a) with transistors M1 to M8.
- The output voltages Vout1 and Vout2 are fed into the CM Sense circuit.
- The CM Sense circuit is connected to the operational amplifier with gain Ae.
- The output of the operational amplifier is connected to the gates of M7 and M8, providing the common-mode feedback to stabilize the output common-mode voltage to VREF.

Overall, the image illustrates the implementation of a differential amplifier with common-mode feedback to ensure stable operation and control of the output common-mode voltage.
```

**Figure 9.60** (a) Two-stage op amp, (b) CMFB around second stage, and (c) CMFB from second stage to first stage.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a differential amplifier with common-mode feedback. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors connected in a current mirror configuration. The source of M1 is connected to the ground, and the gate of M1 is connected to the gate and drain of M2.
   - **M3 and M4:** These are PMOS transistors with their sources connected to the positive supply voltage (V_DD). The gates of M3 and M4 are connected together and to the drain of M2.
   - **M5 and M6:** These are PMOS transistors with their sources connected to V_DD. The gates of M5 and M6 are connected together and to the drain of M4.
   - **M7 and M8:** These are NMOS transistors with their sources connected to the ground. The gates of M7 and M8 are connected together and to the output of the error amplifier.

2. **Current Source:**
   - There is a current source connected to the source of M1 and the drain of M2, providing a constant current.

3. **Error Amplifier:**
   - The error amplifier (A_e) has a differential input with the non-inverting input (+) connected to a reference voltage (V_REF) and the inverting input (-) connected to the common-mode sense resistor (R_CM).

4. **Common-Mode Sense:**
   - The common-mode sense circuit includes a resistor (R_CM) connected between the output of the error amplifier and the inverting input of the error amplifier.

5. **Outputs:**
   - The circuit has two outputs, V_out1 and V_out2, taken from the drains of M5 and M6, respectively.

6. **Connections:**
   - The gates of M3 and M4 are connected to the nodes labeled X and Y, respectively.
   - The drains of M3 and M4 are connected to the sources of M5 and M6, respectively.

The circuit is designed to amplify the differential signal while rejecting the common-mode signal, with the error amplifier and common-mode sense circuit ensuring proper common-mode feedback.
```

**Figure 9.61** Equivalent CMFB loop to determine the number of poles.

*R*<sup>1</sup> and *R*<sup>2</sup> provide CMFB for the first stage and *R*<sup>3</sup> and *R*<sup>4</sup> for the second. Interestingly, all of the drain currents in this topology are copied from *ISS*. Assuming a symmetric circuit, we recognize that (1) resistors *R*<sup>1</sup> and *R*<sup>2</sup> adjust *VG S*<sup>3</sup>*,*<sup>4</sup> until |*ID*3|=|*ID*4| = *ISS/*2; (2) since *VG S*<sup>3</sup>*,*<sup>4</sup> = *VG S*<sup>5</sup>*,*6, *M*<sup>5</sup> and *M*<sup>6</sup> copy their currents from *M*<sup>3</sup> and *M*<sup>4</sup> as in a current mirror; and (3) resistors *R*<sup>3</sup> and *R*<sup>4</sup> adjust *VG S*<sup>7</sup>*,*<sup>8</sup> until *ID*<sup>7</sup> = *ID*<sup>8</sup> = |*ID*5|=|*ID*6|. The differential voltage gain is equal to *gm*1*(rO*1||*rO*3||*R*1*)gm*5*(rO*5||*rO*7||*R*3*)*.

Another CMFB technique for two-stage op amps is described in Chapter 11.

▲

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.

2. **Transistors:**
   - There are eight MOSFET transistors labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input transistors of the differential pair.
   - \( M_3 \) and \( M_4 \) are the load transistors connected in a current mirror configuration.
   - \( M_5 \) and \( M_6 \) are additional load transistors connected to \( M_3 \) and \( M_4 \) respectively.
   - \( M_7 \) and \( M_8 \) are the tail current transistors connected to the outputs \( V_{out1} \) and \( V_{out2} \) respectively.

3. **Resistors:**
   - There are four resistors labeled \( R_1 \) to \( R_4 \).
   - \( R_1 \) and \( R_2 \) are connected between the drains of \( M_1 \) and \( M_2 \) and the gates of \( M_3 \) and \( M_4 \) respectively.
   - \( R_3 \) and \( R_4 \) are connected between the sources of \( M_7 \) and \( M_8 \) and the common node \( Q \).

4. **Current Source:**
   - There is a current source labeled \( I_{SS} \) connected to the common source node of \( M_1 \) and \( M_2 \) and to ground.

5. **Connections:**
   - The input voltage \( V_{in} \) is applied to the gate of \( M_1 \).
   - The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drains of \( M_5 \) and \( M_6 \) respectively.
   - The sources of \( M_7 \) and \( M_8 \) are connected to ground.

6. **Nodes:**
   - Node \( X \) is the connection point between \( R_1 \) and the gate of \( M_3 \).
   - Node \( Y \) is the connection point between \( R_2 \) and the gate of \( M_4 \).
   - Node \( Q \) is the common connection point for the sources of \( M_7 \) and \( M_8 \) and the current source \( I_{SS} \).

This differential amplifier circuit is designed to amplify the difference between the input signals applied to \( M_1 \) and \( M_2 \), providing differential outputs at \( V_{out1} \) and \( V_{out2} \).
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
The image depicts an electronic circuit diagram, specifically a differential amplifier circuit. The circuit consists of the following components:

1. **Transistors (M7 and M8)**: There are two MOSFET transistors labeled M7 and M8. The source terminals of both transistors are connected to the ground.

2. **Resistors (R3 and R4)**: There are two resistors labeled R3 and R4. Resistor R3 is connected between the drain of transistor M7 and a node labeled Q. Similarly, resistor R4 is connected between the drain of transistor M8 and the same node Q.

3. **Current Source (IQ)**: There is a current source labeled IQ connected to the node Q and the ground.

4. **Output Nodes (Vout1 and Vout2)**: The circuit has two output nodes labeled Vout1 and Vout2. Vout1 is connected to the drain of transistor M7, and Vout2 is connected to the drain of transistor M8.

The circuit is likely used for amplifying the difference between two input signals applied to the gates of transistors M7 and M8. The current source IQ provides a constant current, which is split between the two branches of the circuit. The resistors R3 and R4 help in converting the current variations into voltage variations at the output nodes Vout1 and Vout2.
```

If the first stage incorporates a telescopic cascode to achieve a high gain, then the CMFB loops can be realized as shown in Fig. 9.64. While not precise, the CM sensing of *X* and *Y* avoids loading the high impedances at these nodes, thereby maintaining a high voltage gain.

# **9.8 Input Range Limitations**

The op amp circuits studied thus far have evolved to achieve large differential output swings. While the differential input swings are usually much smaller (by a factor equal to the open-loop gain), the input *common-mode* level may need to vary over a wide range in some applications. For example, consider the simple unity-gain buffer shown in Fig. 9.65, where the input swing is nearly equal to the output swing. Interestingly, in this case the voltage swings are limited by the input differential pair rather than the output

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit. The circuit is composed of multiple transistors, resistors, and a current source. Here is a detailed description of the components and their connections:

1. **Power Supply (V_DD)**: The top horizontal line represents the positive power supply voltage, labeled as V_DD.

2. **Transistors**: The circuit includes several MOSFET transistors arranged in a specific configuration:
   - There are two pairs of transistors at the top, connected in a cascode configuration. Each pair consists of two transistors in series.
   - The middle section has two transistors labeled X and Y, which are connected to the output nodes V_out1 and V_out2, respectively.
   - The bottom section has two transistors connected to the ground, forming the differential pair.

3. **Output Nodes (V_out1 and V_out2)**: The left and right sides of the circuit have output nodes labeled V_out1 and V_out2, respectively. These nodes are connected to the drains of the transistors in the middle section.

4. **Resistors**: There are two resistors connected to the sources of the transistors in the middle section. These resistors are connected to the ground.

5. **Current Source**: At the bottom center of the circuit, there is a current source symbol connected to the ground. This current source provides the bias current for the differential pair of transistors.

6. **Connections**: The circuit is symmetrical, with the left and right sides mirroring each other. The transistors in the middle section (X and Y) are connected to the output nodes and the cascode transistors at the top.

Overall, this schematic represents a differential amplifier with cascode transistors for improved performance, providing differential outputs at V_out1 and V_out2.
```

**Figure 9.64** CMFB loops around cascode and output stages.

Here is the image describtion:
```
The image consists of two distinct parts: a simple operational amplifier (op-amp) circuit on the left and a more complex MOSFET-based circuit on the right.

1. **Operational Amplifier Circuit (Left Side):**
   - The circuit features a standard operational amplifier symbol, which is a triangle pointing to the right.
   - The op-amp has two input terminals: the inverting input (marked with a minus sign) and the non-inverting input (marked with a plus sign).
   - The non-inverting input is connected to the input voltage \( V_{in} \).
   - The output of the op-amp is labeled \( V_{out} \).
   - There is a feedback loop from the output back to the inverting input, indicating a negative feedback configuration.

2. **MOSFET-Based Circuit (Right Side):**
   - The circuit is more complex and consists of multiple MOSFET transistors labeled \( M_1 \) through \( M_{10} \).
   - The input voltage \( V_{in} \) is connected to the gate of the MOSFET \( M_1 \).
   - The source of \( M_1 \) is connected to a current source labeled \( I_{SS} \), which is grounded.
   - The drain of \( M_1 \) is connected to the gate of \( M_2 \), and the source of \( M_2 \) is also connected to \( I_{SS} \).
   - The drain of \( M_2 \) is connected to the gates of \( M_3 \) and \( M_4 \).
   - The drain of \( M_3 \) is connected to the source of \( M_9 \), and the drain of \( M_4 \) is connected to the source of \( M_{10} \).
   - The sources of \( M_3 \) and \( M_4 \) are connected to the drain of \( M_5 \) and \( M_6 \), respectively.
   - The sources of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_7 \) and \( M_8 \), respectively, which are grounded.
   - The gates of \( M_5 \) and \( M_6 \) are connected to the output node \( V_{out} \).
   - The drains of \( M_9 \) and \( M_{10} \) are connected to the supply voltage \( V_{DD} \).
   - The output voltage \( V_{out} \) is taken from the node where the sources of \( M_5 \) and \( M_6 \) meet.

This complex circuit likely represents a differential amplifier or a similar analog circuit, utilizing multiple MOSFETs to achieve amplification and other desired electrical characteristics.
```

**Figure 9.65** Unity-gain buffer.

cascode branch. Specifically, *Vin,min* ≈ *Vout,min* = *VG S*<sup>1</sup>*,*<sup>2</sup> + *VISS*, approximately one threshold voltage higher than the allowable minimum provided by *M*5–*M*8.

What happens if *Vin* falls below the minimum given above? The MOS transistor operating as *ISS* enters the triode region, decreasing the bias current of the differential pair and hence lowering the transconductance. We then postulate that the limitation is overcome if the transconductance can somehow be restored.

A simple approach to extending the input CM range is to incorporate both NMOS and PMOS differential pairs such that when one is "dead," the other is "alive." Illustrated in Fig. 9.66, the idea is to combine two folded-cascode op amps with NMOS and PMOS input differential pairs. Here, as the input CM level approaches the ground potential, the NMOS pair's transconductance drops, eventually falling to zero. Nonetheless, the PMOS pair remains active, allowing normal operation. Conversely, if the input CM level approaches *VDD*, *M*<sup>1</sup>*<sup>P</sup>* and *M*<sup>2</sup>*<sup>P</sup>* begin to turn off, but *M*<sup>1</sup> and *M*<sup>2</sup> function properly.

An important concern in the circuit of Fig. 9.66 is the *variation* of the overall transconductance of the two pairs as the input CM level changes. Considering the operation of each pair, we anticipate the behavior depicted in Fig. 9.67. Thus, many properties of the circuit, including gain, speed, and noise, vary. More sophisticated techniques of minimizing this variation are described in [8].

Here is the image describtion:
```
The image depicts a schematic diagram of a CMOS operational amplifier (op-amp) circuit. The circuit consists of multiple MOSFET transistors arranged in a specific configuration to achieve amplification. Here is a detailed description of the components and their connections:

1. **Input Stage:**
   - **Transistors M1 and M2:** These are NMOS transistors forming a differential pair. The gates of M1 and M2 are connected to the input signals \( V_{in1} \) and \( V_{in2} \), respectively.
   - **Current Sources \( I_{SS1} \) and \( I_{SS2} \):** These provide biasing currents to the differential pair. \( I_{SS1} \) is connected to the source of M1, and \( I_{SS2} \) is connected to the source of M2.

2. **Active Load:**
   - **Transistors M1p and M2p:** These are PMOS transistors acting as active loads for the differential pair. The drains of M1 and M2 are connected to the drains of M1p and M2p, respectively.

3. **Second Stage:**
   - **Transistors M3 and M4:** These are PMOS transistors forming a current mirror. The source of M3 is connected to the drain of M1p, and the source of M4 is connected to the drain of M2p. The gates of M3 and M4 are connected together and to the drain of M3.
   - **Transistors M5 and M6:** These are NMOS transistors forming another differential pair. The gate of M5 is connected to the drain of M2 (node Y), and the gate of M6 is connected to the drain of M1 (node X).

4. **Output Stage:**
   - **Transistors M7 and M8:** These are NMOS transistors connected in a common-source configuration. The drain of M7 is connected to the drain of M5, and the drain of M8 is connected to the drain of M6.
   - **Transistors M9 and M10:** These are PMOS transistors forming a current mirror. The source of M9 is connected to \( V_{DD} \), and the source of M10 is connected to the drain of M8. The gates of M9 and M10 are connected together and to the drain of M9.

5. **Output:**
   - The output \( V_{out} \) is taken from the drain of M6.

The circuit is designed to amplify the difference between the input signals \( V_{in1} \) and \( V_{in2} \) and provide an amplified output at \( V_{out} \). The use of current mirrors and differential pairs helps in achieving high gain and proper biasing of the transistors.
```

**Figure 9.66** Extension of input CM range.

Here is the image describtion:
```
The image is a graph illustrating the variation of equivalent transconductance with the input common-mode (CM) level. The x-axis represents the input common-mode voltage (Vin,CM), ranging from 0 to VDD. The y-axis represents the transconductance values.

The graph shows a curve that starts at a value labeled gmp at Vin,CM = 0, rises to a peak labeled Gm,tot, and then descends to a value labeled gmn at Vin,CM = VDD. The curve is symmetrical and indicates how the equivalent transconductance changes as the input common-mode voltage varies from 0 to VDD.

The figure is labeled as "Figure 9.67" and is captioned "Variation of equivalent transconductance with the input CM level."
```

# **9.9 Slew Rate**

Op amps used in feedback circuits exhibit a large-signal behavior called "slewing." We first describe an interesting property of *linear* systems that vanishes during slewing. Consider the simple RC network shown in Fig. 9.68, where the input is an ideal voltage step of height *V*0. Since *Vout* = *V*0[1−exp*(*−*t/*τ *)*], where τ = *RC*, we have

$$\frac{dV\_{out}}{dt} = \frac{V\_0}{\tau} \exp\frac{-t}{\tau} \tag{9.58}$$

That is, the slope of the step response is proportional to the final value of the output; if we apply a larger input step, the output rises more rapidly. This is a fundamental property of linear systems: if the input amplitude is, say, doubled while other parameters remain constant, the output signal level must double at *every* point, leading to a twofold increase in the slope.

Here is the image describtion:
```
The image consists of three parts: a circuit diagram on the left and two graphs on the right.

1. **Circuit Diagram (Left Side):**
   - The circuit is a simple RC (resistor-capacitor) circuit.
   - It includes a resistor labeled \( R_1 \) and a capacitor labeled \( C_1 \).
   - The input voltage is labeled \( V_{in} \) and is applied across the series combination of \( R_1 \) and \( C_1 \).
   - The output voltage is labeled \( V_{out} \) and is taken across the capacitor \( C_1 \).

2. **Graph 1 (Middle):**
   - This graph shows the input voltage \( V_{in} \) and the output voltage \( V_{out} \) as functions of time \( t \).
   - The input voltage \( V_{in} \) is depicted as a step function, abruptly rising from a lower value to a higher constant value.
   - The output voltage \( V_{out} \) shows an exponential rise from the initial value to a higher value, following the step change in \( V_{in} \).
   - The dashed line represents the initial slope of the exponential rise of \( V_{out} \).

3. **Graph 2 (Right):**
   - This graph also shows the input voltage \( V_{in} \) and the output voltage \( V_{out} \) as functions of time \( t \).
   - The input voltage \( V_{in} \) is depicted as a step function, abruptly falling from a higher value to a lower constant value.
   - The output voltage \( V_{out} \) shows an exponential decay from the initial value to a lower value, following the step change in \( V_{in} \).
   - The dashed line represents the initial slope of the exponential decay of \( V_{out} \).

Overall, the image illustrates the behavior of an RC circuit in response to step changes in the input voltage, showing the characteristic exponential charging and discharging curves of the capacitor.
```

**Figure 9.68** Response of a linear circuit to an input step.

Here is the image describtion:
```
The image depicts a schematic diagram of a linear operational amplifier (op-amp) circuit. The key components and their connections are as follows:

1. **Op-Amp (A)**: The central component is an operational amplifier represented by a triangle with the label "A" inside it. The op-amp has two input terminals: the non-inverting input (+) and the inverting input (-). The non-inverting input is connected to the input voltage \( V_{in} \).

2. **Output Resistor (R_out)**: The output of the op-amp is connected to a resistor labeled \( R_{out} \).

3. **Voltage Divider Network**: After \( R_{out} \), the circuit splits into two paths:
   - One path goes through a resistor \( R_1 \) and then to the output voltage \( V_{out} \).
   - The other path goes through a capacitor \( C_L \) which is connected to the ground.

4. **Feedback Resistor (R_2)**: There is a resistor \( R_2 \) connected between the junction of \( R_1 \) and \( C_L \) and the ground.

5. **Connections**:
   - The input voltage \( V_{in} \) is applied to the non-inverting input of the op-amp.
   - The output voltage \( V_{out} \) is taken from the junction between \( R_1 \) and \( C_L \).

The diagram is labeled "Linear Op Amp" at the top, indicating that the op-amp is operating in its linear region. The figure is also labeled "Figure to step" at the bottom right corner, suggesting that it is part of a step-by-step explanation or tutorial.
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
The image consists of two main parts: a circuit diagram on the left and a set of graphs on the right.

**Circuit Diagram (Left Side):**
- The circuit diagram represents an operational amplifier (op-amp) configuration.
- The op-amp is labeled as "Actual Op Amp" and is enclosed in a dashed box.
- The op-amp has two input terminals: the inverting input (-) and the non-inverting input (+).
- The non-inverting input is connected to the input voltage \( V_{in} \).
- The output of the op-amp is connected to a resistor labeled \( R_{out} \).
- The other end of \( R_{out} \) is connected to a node that branches out to three components:
  - A resistor \( R_1 \) connected to ground.
  - A capacitor \( C_L \) connected to ground.
  - The output voltage \( V_{out} \).
- The inverting input of the op-amp is connected to the junction between \( R_1 \) and \( R_2 \), where \( R_2 \) is also connected to ground.

**Graphs (Right Side):**
- The top graph shows the input voltage \( V_{in} \) as a step function, indicating a sudden change in voltage.
- The bottom graph shows the output voltage \( V_{out} \) over time \( t \).
- The output voltage graph has two labeled curves:
  - "Ramp" indicates a linear increase in \( V_{out} \) over time.
  - "Exponential" indicates an exponential increase in \( V_{out} \) over time.
- The graph suggests that the output voltage \( V_{out} \) can follow different response patterns (ramp or exponential) depending on the circuit conditions.

Overall, the image illustrates the behavior of an actual op-amp circuit with a step input voltage and the corresponding output voltage response over time.
```

**Figure 9.70** Slewing in an op amp circuit.

To understand the origin of slewing, let us replace the op amp of Fig. 9.70 by a simple CMOS implementation (Fig. 9.71), assuming for simplicity that *R*<sup>1</sup> + *R*<sup>2</sup> is very large. We first examine the circuit with a small input step. If *Vin* experiences a change of '*V*, *ID*<sup>1</sup> increases by *gm*'*V/*2 and *ID*<sup>2</sup> decreases by *gm*'*V/*2. Since the mirror action of *M*<sup>3</sup> and *M*<sup>4</sup> raises |*ID*4| by *gm*'*V/*2, the total smallsignal current provided by the op amp equals *gm*'*V*. This current begins to charge *CL* , but as *Vout* rises, so does *VX* , reducing the difference between *VG*<sup>1</sup> and *VG*<sup>2</sup> and hence the output current of the op amp. As a result, *Vout* varies according to (9.61).

Here is the image describtion:
```
The image depicts a schematic diagram of a differential amplifier circuit with a current mirror load. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. The source terminals of M1 and M2 are connected together and to a current source labeled \( I_{SS} \) which is connected to ground.
   - **M3 and M4:** These are PMOS transistors forming the current mirror load. The source terminals of M3 and M4 are connected to the supply voltage \( V_{DD} \). The drain of M3 is connected to the drain of M1, and the drain of M4 is connected to the drain of M2.

2. **Input and Output:**
   - **Vin:** The input voltage \( \Delta V \) is applied to the gate of M1.
   - **Vout:** The output voltage is taken from the drain of M2.

3. **Resistors and Capacitor:**
   - **R1 and R2:** These resistors are connected in series between the output node (drain of M2) and ground. The node between R1 and R2 is labeled as X.
   - **CL:** This is a load capacitor connected between the output node (drain of M2) and ground.

4. **Voltage and Current Labels:**
   - The voltage difference \( \Delta V \) is applied to the gate of M1.
   - The transconductance \( g_m \) and the voltage difference \( \Delta V \) are used to label the currents through the transistors and resistors. For example, \( g_m \Delta V / 2 \) is labeled at the drain of M1 and M2, and \( g_m \Delta V \) is labeled at the output node.

5. **Graph:**
   - To the right of the circuit, there is a graph showing the output voltage \( V_{out} \) as a function of time or input voltage, indicating a step response or a transition from low to high voltage.

This circuit is typically used in analog signal processing to amplify the difference between two input voltages while rejecting any common-mode signals. The current mirror formed by M3 and M4 ensures that the differential pair operates correctly by providing a constant current source.
```

**Figure 9.71** Small-signal operation of a simple op amp.

Now suppose '*V* is so large that *M*<sup>1</sup> absorbs all of *ISS*, turning off *M*2. The circuit then reduces to that shown in Fig. 9.72(a), generating a ramp output with a slope equal to *ISS/CL* (if the channel-length modulation of *M*<sup>4</sup> and the current drawn by *R*<sup>1</sup> + *R*<sup>2</sup> are neglected). Note that so long as *M*<sup>2</sup> remains off, the feedback loop is broken and the current charging *CL* is constant and independent of the input level. As *Vout* rises, *VX* eventually approaches *Vin*, *M*<sup>2</sup> turns on, and the circuit returns to linear operation.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b), each depicting a different configuration of a differential amplifier with active loads. Both circuits are designed to amplify an input signal \( V_{in} \) and produce an output signal \( V_{out} \).

### Circuit (a):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. M1 is active, while M2 is shown in a lighter shade, indicating it is not active in this configuration.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair.
   
2. **Current Source:**
   - A current source \( I_{SS} \) is connected to the source of M1, providing a constant current.

3. **Resistors and Capacitor:**
   - **R1 and R2:** These resistors are connected in series between the output node and ground. The node between R1 and R2 is labeled as X.
   - **C_L:** A load capacitor is connected between the output node and ground.

4. **Power Supply:**
   - The circuit is powered by a voltage source \( V_{DD} \).

5. **Output:**
   - The output voltage \( V_{out} \) is taken from the drain of M4. A waveform is shown next to the output node, indicating the response of the circuit with a slope of \( \frac{I_{SS}}{C_L} \).

### Circuit (b):
1. **Transistors:**
   - **M1 and M2:** These are NMOS transistors forming the differential pair. M2 is active, while M1 is shown in a lighter shade, indicating it is not active in this configuration.
   - **M3 and M4:** These are PMOS transistors acting as active loads for the differential pair.
   
2. **Current Source:**
   - A current source \( I_{SS} \) is connected to the source of M2, providing a constant current.

3. **Resistors and Capacitor:**
   - **R1 and R2:** These resistors are connected in series between the output node and ground. The node between R1 and R2 is labeled as X.
   - **C_L:** A load capacitor is connected between the output node and ground.

4. **Power Supply:**
   - The circuit is powered by a voltage source \( V_{DD} \).

5. **Output:**
   - The output voltage \( V_{out} \) is taken from the drain of M4. A waveform is shown next to the output node, indicating the response of the circuit with a slope of \( \frac{I_{SS}}{C_L} \).

### Common Elements:
- Both circuits share a similar structure with a differential pair of NMOS transistors and PMOS active loads.
- The output voltage \( V_{out} \) is influenced by the current \( I_{SS} \) and the load capacitor \( C_L \), as indicated by the waveform slope \( \frac{I_{SS}}{C_L} \).

### Differences:
- In circuit (a), M1 is active, while in circuit (b), M2 is active.
- The configuration of the differential pair changes between the two circuits, affecting which transistor is conducting.

Overall, the image illustrates two configurations of a differential amplifier with active loads, highlighting the behavior of the output voltage in response to the input signal.
```

**Figure 9.72** Slewing during (a) low-to-high and (b) high-to-low transitions.

In Fig. 9.71, slewing occurs for falling edges at the input as well. If the input drops so much that *M*<sup>1</sup> turns off, then the circuit is simplified as in Fig. 9.72(b), discharging *CL* by a current approximately equal to *ISS*. After *Vout* decreases sufficiently, the difference between *VX* and *Vin* is small enough to allow *M*<sup>1</sup> to turn on, leading to linear behavior thereafter.

The foregoing observations explain why slewing is a nonlinear phenomenon. If the input amplitude, say, doubles, the output level does not double at *all* points because the ramp exhibits a slope independent of the input.

Slewing is an undesirable effect in high-speed circuits that process large signals. While the small-signal bandwidth of a circuit may suggest a fast time-domain response, the large-signal speed may be limited by the slew rate simply because the current available to charge and discharge the dominant capacitor in the circuit is small. Moreover, since the input-output relationship during slewing is nonlinear, the output of a slewing amplifier exhibits substantial distortion. For example, if a circuit is to amplify a sinusoid *V*<sup>0</sup> sin ω0*t* (in the steady state), then its slew rate must exceed *V*0ω0.

#### ▲**Example 9.22**

Consider the feedback amplifier depicted in Fig. 9.73(a), where *C*<sup>1</sup> and *C*<sup>2</sup> set the closed-loop gain. (The bias network for the gate of *M*<sup>2</sup> is not shown.) (a) Determine the small-signal step response of the circuit. (b) Calculate the positive and negative slew rates.

Here is the image describtion:
```
The image consists of four sub-images labeled (a), (b), (c), and (d), each depicting different configurations or representations of an electronic circuit.

(a) The first sub-image shows a differential amplifier circuit with four MOSFET transistors labeled M1, M2, M3, and M4. The circuit is powered by a voltage source labeled V_DD at the top. The input voltage V_in is applied to the gate of M1. The source of M1 is connected to a current source labeled I_SS, which is grounded. The drain of M1 is connected to the source of M3, and the drain of M3 is connected to V_DD. Similarly, the drain of M2 is connected to the source of M4, and the drain of M4 is connected to V_DD. The output voltage V_out is taken from the drain of M4. There are two capacitors, C1 and C2, connected in series between V_out and ground, with a node labeled X between them.

(b) The second sub-image is a simplified small-signal model of the circuit. It shows an input voltage V_in applied to a voltage source V1, which is connected to a dependent voltage source A_vV1 in series with a resistor R_out. The output voltage V_out is taken across R_out. The capacitors C1 and C2 are connected in series between V_out and ground, with a node labeled X between them.

(c) The third sub-image is similar to the first one but highlights the current flow through the circuit. The current source I_SS is shown with an arrow indicating the direction of current flow towards the output V_out. The transistor M2 is shown in a lighter shade, indicating it is not the primary focus in this configuration.

(d) The fourth sub-image focuses on the transistor M2 and the current flow through it. The transistors M3 and M4 are shown in a lighter shade, indicating they are not the primary focus. The current source I_SS is shown with an arrow indicating the direction of current flow through M2 towards the output V_out. The capacitors C1 and C2 are connected in series between V_out and ground, with a node labeled X between them.

Overall, the image illustrates different aspects and configurations of a differential amplifier circuit, highlighting the components, current flow, and small-signal model.
```

Here is the image describtion:
```
The image provided is a text snippet that reads "Figure 9.73." It appears to be a label or caption typically found in academic or technical documents, indicating a specific figure or illustration referenced in the text. There is no actual image content or visual detail provided beyond this text label.
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
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams depict differential amplifier circuits with current mirror loads.

### Diagram (a):
1. **Transistors:**
   - There are eight MOSFET transistors labeled M1 to M8.
   - M1 and M2 are the input differential pair.
   - M3 and M4 are the load transistors for the differential pair.
   - M5 and M6 are the current mirror transistors.
   - M7 and M8 are the additional transistors in the current mirror configuration.

2. **Connections:**
   - The source of M1 and M2 are connected together and to a current source labeled \( I_{SS} \).
   - The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
   - The gates of M3 and M4 are connected to their respective drains.
   - The drain of M3 is connected to the source of M5, and the drain of M4 is connected to the source of M6.
   - The gates of M5 and M6 are connected together and to the drain of M5.
   - The drain of M5 is connected to the source of M7, and the drain of M6 is connected to the source of M8.
   - The gates of M7 and M8 are connected together and to the drain of M7.
   - The drains of M7 and M8 are connected to \( V_{DD} \).

3. **Capacitors:**
   - There are two capacitors labeled \( C_L \) connected to the output nodes of the circuit.

4. **Current:**
   - The current source \( I_{SS} \) is split into two equal parts, \( \frac{I_{SS}}{2} \), flowing through M5 and M6.

### Diagram (b):
1. **Transistors:**
   - Similar to diagram (a), but M2 is shown in a lighter shade, indicating it is not active in this configuration.

2. **Connections:**
   - The source of M1 is connected to the current source \( I_{SS} \).
   - The drain of M1 is connected to the source of M3.
   - The gate of M3 is connected to its drain.
   - The drain of M3 is connected to the source of M5.
   - The gates of M5 and M6 are connected together and to the drain of M5.
   - The drain of M5 is connected to the source of M7.
   - The gates of M7 and M8 are connected together and to the drain of M7.
   - The drains of M7 and M8 are connected to \( V_{DD} \).

3. **Capacitors:**
   - There is one capacitor labeled \( C_L \) connected to the output node of the circuit.

4. **Current:**
   - The current source \( I_{SS} \) is split into two equal parts, \( \frac{I_{SS}}{2} \), flowing through M5 and M6.

### Summary:
Both diagrams illustrate differential amplifier circuits with current mirror loads, but diagram (b) shows a simplified version with M2 inactive. The circuits use MOSFET transistors and capacitors to achieve amplification, with current sources providing the necessary biasing.
```

**Figure 9.74** Slewing in telescopic op amp.

It is also instructive to study the slewing behavior of a folded-cascode op amp with single-ended output [Fig. 9.75(a)]. Figures 9.75(a) and (b) depict the equivalent circuit for positive and negative input steps,

Here is the image describtion:
```
The image shows two circuit diagrams labeled (a) and (b), which appear to be different configurations of a differential amplifier with active loads. Both circuits are designed using MOSFET transistors and are powered by a supply voltage \( V_{DD} \).

### Circuit (a):
1. **Transistors:**
   - **M1 and M2:** These are the input differential pair transistors. M1 is shown in black, while M2 is shown in gray, indicating it might be part of a mirrored or complementary pair.
   - **M3 and M4:** These transistors form the active load for the differential pair.
   - **M5 and M6:** These transistors are part of the current mirror circuit.
   - **M7 and M8:** These transistors are connected to the sources of M5 and M6, respectively, and are grounded.
   - **M9 and M10:** These transistors are connected to the drain of M3 and M4, respectively, and are also connected to \( V_{DD} \).

2. **Currents:**
   - **I_SS:** The tail current source for the differential pair.
   - **I_P:** The current through the active load transistors M9 and M10.
   - **I_P - I_SS:** The current through the transistors M3 and M4.

3. **Nodes:**
   - **X and Y:** Intermediate nodes between the active load transistors and the differential pair.
   - **V_out:** The output node of the amplifier.
   - **C_L:** The load capacitance connected to the output node.

### Circuit (b):
1. **Transistors:**
   - **M1 and M2:** Similar to circuit (a), these are the input differential pair transistors, with M1 shown in gray and M2 in black.
   - **M3 and M4:** These transistors form the active load for the differential pair.
   - **M5 and M6:** These transistors are part of the current mirror circuit.
   - **M7 and M8:** These transistors are connected to the sources of M5 and M6, respectively, and are grounded.
   - **M9 and M10:** These transistors are connected to the drain of M3 and M4, respectively, and are also connected to \( V_{DD} \).

2. **Currents:**
   - **I_SS:** The tail current source for the differential pair.
   - **I_P:** The current through the active load transistors M9 and M10.
   - **I_P - I_SS:** The current through the transistors M3 and M4.

3. **Nodes:**
   - **X and Y:** Intermediate nodes between the active load transistors and the differential pair.
   - **V_out:** The output node of the amplifier.
   - **C_L:** The load capacitance connected to the output node.

### Differences:
- The primary difference between the two circuits is the placement and orientation of the input differential pair transistors M1 and M2. In circuit (a), M1 is on the left and M2 on the right, while in circuit (b), M1 is on the right and M2 on the left.
- The current source \( I_{SS} \) is connected differently in both circuits, affecting the overall current flow and potentially the performance characteristics of the amplifier.

Both circuits are designed to amplify differential signals with high gain and are commonly used in analog integrated circuits.
```

**Figure 9.75** Slewing in folded-cascode op amp.

respectively. Here, the PMOS current sources provide a current of *IP* , and the current that charges or discharges *CL* is equal to *ISS*, yielding a slew rate of *ISS/CL* . Note that the slew rate is independent of *IP* if *IP* ≥ *ISS*. In practice, we choose *IP* ≈ *ISS*.

In Fig. 9.75(a), if *ISS > IP* , then during slewing, *M*<sup>3</sup> turns off and *VX* falls to a low level such that *M*<sup>1</sup> and the tail current source enter the triode region. Thus, for the circuit to return to equilibrium after *M*<sup>2</sup> turns on, *VX* must experience a large swing, slowing down the settling. This phenomenon is illustrated in Fig. 9.76.

Here is the image describtion:
```
The image depicts a schematic diagram of a transistor circuit. The circuit includes three MOSFET transistors labeled M1, M3, and M9. 

- M1 is an NMOS transistor with its gate connected to an input signal, its source connected to a current source labeled Iss, and its drain connected to a node that connects to the drain of M9.
- M9 is a PMOS transistor with its source connected to a current source labeled Ip, its gate connected to the drain of M3, and its drain connected to the node X.
- M3 is an NMOS transistor with its drain connected to the gate of M9, its gate connected to node X, and its source connected to ground.

The current source Iss is connected to the source of M1 and to ground, providing a constant current. The current source Ip is connected to the source of M9, providing another constant current. The node X is a critical point in the circuit, connecting the drain of M9 and the gate of M3.

The circuit appears to be a part of an analog or mixed-signal design, possibly a current mirror or a differential amplifier stage, given the arrangement of the transistors and current sources. The waveform on the right side of the image suggests that the circuit is involved in signal processing, likely amplifying or modifying an input signal.
```

**Figure 9.76** Long settling due to overdrive recovery after slewing.

To alleviate this issue, two "clamp" transistors can be added as shown in Fig. 9.77(a) [9]. The idea is that the difference between *ISS* and *IP* now flows through *M*<sup>11</sup> or *M*12, requiring only enough drop in *VX* or *VY* to turn on one of these transistors. Figure 9.77(b) illustrates a more aggressive approach, where *M*<sup>11</sup> and *M*<sup>12</sup> clamp the two nodes directly to *VDD*. Since the equilibrium value of *VX* and *VY* is usually higher than *VDD* − *VTHN* , *M*<sup>11</sup> and *M*<sup>12</sup> are off during small-signal operation.

What trade-offs are encountered in increasing the slew rate? In the examples of Figs. 9.74 and 9.75, for a given load capacitance, *ISS* must be increased, and to maintain the same maximum output swing, all of the transistors must be made proportionally wider. As a result, the power dissipation and the input capacitance are increased. Note that if the device currents and widths scale together, *gmrO* of each transistor, and hence the open-loop gain of the op amp, remain constant.

How does an op amp leave the slewing regime and enter the linear-settling regime? Since the point at which one of the input transistors "turns on" is ambiguous, the distinction between slewing and linear settling is somewhat arbitrary. The following example illustrates the point.

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams depict a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).

### Diagram (a):
- **Transistors:**
  - M9 and M10 are PMOS transistors connected to the supply voltage \( V_{DD} \).
  - M11 and M12 are NMOS transistors forming the differential pair.
  - M3 and M4 are NMOS transistors connected to the sources of M11 and M12, respectively.
- **Connections:**
  - The drains of M9 and M11 are connected together and labeled as node X.
  - The drains of M10 and M12 are connected together and labeled as node Y.
  - The sources of M11 and M12 are connected to the drains of M3 and M4, respectively.
  - The sources of M3 and M4 are connected to ground.
  - The gates of M11 and M12 are cross-coupled, meaning the gate of M11 is connected to the drain of M12 and vice versa.

### Diagram (b):
- **Transistors:**
  - M9 and M10 are PMOS transistors connected to the supply voltage \( V_{DD} \).
  - M11 and M12 are NMOS transistors forming the differential pair.
  - M3 and M4 are NMOS transistors connected to the sources of M11 and M12, respectively.
- **Connections:**
  - The drains of M9 and M11 are connected together and labeled as node X.
  - The drains of M10 and M12 are connected together and labeled as node Y.
  - The sources of M11 and M12 are connected to the drains of M3 and M4, respectively.
  - The sources of M3 and M4 are connected to ground.
  - The gates of M11 and M12 are connected to the same nodes as in diagram (a), but the cross-coupling is shown more explicitly with additional lines connecting the gates to the opposite drains.

### Common Features:
- Both circuits are differential amplifiers with similar configurations.
- Both use PMOS transistors (M9, M10) as load devices and NMOS transistors (M11, M12) as the differential pair.
- Both circuits have NMOS transistors (M3, M4) acting as current sources or sinks.

### Differences:
- The main difference lies in the representation of the cross-coupling of the gates of M11 and M12. In diagram (a), the cross-coupling is shown with a single line crossing over, while in diagram (b), it is shown with more explicit connections.

These circuits are typically used in analog signal processing for amplifying differential signals.
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
The image consists of two circuit diagrams labeled (a) and (b), each depicting a different configuration of MOSFET transistors.

(a) The first circuit diagram shows a common-source amplifier with a current source load. The components and their connections are as follows:
- \( M_1 \) is an NMOS transistor with its source connected to ground and its gate connected to the input voltage \( V_{in} \).
- \( M_2 \) is a PMOS transistor with its source connected to the supply voltage \( V_{DD} \) and its gate connected to a bias voltage \( V_b \).
- The drain of \( M_1 \) is connected to the drain of \( M_2 \), forming the output node \( V_{out} \).
- A current source \( I_0 \) is shown connected between \( V_{DD} \) and the drain of \( M_2 \).
- A load capacitor \( C_L \) is connected between the output node \( V_{out} \) and ground.

(b) The second circuit diagram shows a common-source amplifier with an active load. The components and their connections are as follows:
- \( M_1 \) is an NMOS transistor with its source connected to ground and its gate connected to the input voltage \( V_{in} \).
- \( M_2 \) is a PMOS transistor with its source connected to the supply voltage \( V_{DD} \) and its gate connected to the drain of \( M_1 \).
- The drain of \( M_1 \) is connected to the drain of \( M_2 \), forming the output node \( V_{out} \).
- A load capacitor \( C_L \) is connected between the output node \( V_{out} \) and ground.

Both circuits are designed to amplify the input signal \( V_{in} \) and provide an output signal \( V_{out} \). The key difference between the two configurations is the type of load used: a current source load in (a) and an active load in (b).
```

**Figure 9.78** Slewing in (a) a simple CS stage and (b) a complementary CS stage.

Let us control *M*<sup>2</sup> in Fig. 9.78(a) by current mirror action, as depicted in Fig. 9.79(a), and ask how *Ib* must be controlled by *Vin*. Can *Ib* be derived from another common-source device [Fig. 9.79(b)]? No; as *Vin* jumps down in this circuit, *Ib decreases*. We must therefore include an additional signal inversion in the path controlling *Ib*. Alternatively, we can consider a differential topology, where both the input signal, *V* <sup>+</sup> *in* , and its inverted version, *V* <sup>−</sup> *in* , are available. Illustrated in Fig. 9.79(c), the idea is to control the bias current of *M*<sup>2</sup> by *V* <sup>−</sup> *in* and that of *M*<sup>4</sup> by *V* <sup>+</sup> *in* . For example, if *V* <sup>+</sup> *in* jumps down and *V* <sup>−</sup> *in* jumps up, then (1) *M*<sup>5</sup> draws less current from *M*8, lowering |*ID*4|, (2) *M*<sup>3</sup> draws more current, discharging its load capacitance, (3) *M*<sup>6</sup> draws more current from *M*7, raising |*ID*2|, and (4) *M*<sup>1</sup> draws less current, allowing its drain capacitance to be charged by *M*2.

The circuits of Figs. 9.78(b) and 9.79(c) are called "push-pull" stages as they turn the load current source into an "active" pull-up device. Loosely speaking, we also refer to them as "class-AB" amplifiers.<sup>8</sup>

<sup>7</sup>If *Vin* jumps *up*, *M*<sup>1</sup> must absorb both *I*<sup>0</sup> and the current flowing out of *CL* .

<sup>8</sup>By contrast, topologies with a constant bias current are called "class-A" amplifiers.

Here is the image describtion:
```
The image contains four different circuit diagrams labeled (a), (b), (c), and (d). Each diagram represents a different configuration of MOSFET-based amplifier circuits. Here is a detailed description of each:

(a) The first circuit diagram (a) shows a simple MOSFET amplifier. It consists of three MOSFETs labeled M1, M2, and M3. The input voltage \( V_{in} \) is applied to the gate of M1, which is connected to the ground. The drain of M1 is connected to the source of M2, and the gate of M2 is connected to the drain of M3. The source of M3 is connected to a bias current source \( I_b \). The output voltage \( V_{out} \) is taken from the drain of M2, and a load capacitor \( C_L \) is connected between \( V_{out} \) and ground. The circuit is powered by a supply voltage \( V_{DD} \).

(b) The second circuit diagram (b) is similar to (a) but includes an additional MOSFET M4. The input voltage \( V_{in} \) is applied to the gate of M4, which is connected to the source of M1. The rest of the configuration is similar to (a), with M2 and M3 forming a current mirror and the output taken from the drain of M2.

(c) The third circuit diagram (c) shows a differential amplifier configuration. It consists of eight MOSFETs labeled M1 to M8. The input voltages \( V_{in}^+ \) and \( V_{in}^- \) are applied to the gates of M5 and M6, respectively. The sources of M5 and M6 are connected to the drains of M1 and M3, respectively. The gates of M1 and M3 are connected to the drains of M7 and M8, respectively. The sources of M7 and M8 are connected to the supply voltage \( V_{DD} \). The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drains of M2 and M4, respectively. Load capacitors \( C_L \) are connected between the outputs and ground.

(d) The fourth circuit diagram (d) is another differential amplifier configuration with current sources. It consists of eight MOSFETs labeled M1 to M8 and two current sources labeled \( I_{SS1} \) and \( I_{SS2} \). The input voltages \( V_{in}^+ \) and \( V_{in}^- \) are applied to the gates of M5 and M6, respectively. The sources of M5 and M6 are connected to the current sources \( I_{SS2} \) and \( I_{SS1} \), respectively. The drains of M5 and M6 are connected to the sources of M1 and M3, respectively. The gates of M1 and M3 are connected to the drains of M7 and M8, respectively. The sources of M7 and M8 are connected to the supply voltage \( V_{DD} \). The output voltages \( V_{out1} \) and \( V_{out2} \) are taken from the drains of M2 and M4, respectively. Load capacitors \( C_L \) are connected between the outputs and ground.

Each circuit diagram represents a different configuration of MOSFET amplifiers, showcasing various ways to achieve amplification using MOSFETs and current mirrors.
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
The image depicts a schematic diagram of a differential amplifier circuit with a current mirror load. The circuit consists of multiple MOSFET transistors, capacitors, and a current source. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - **M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12**: These are MOSFET transistors. The specific type (NMOS or PMOS) is not explicitly indicated, but their arrangement suggests typical configurations used in differential amplifiers and current mirrors.
   - **M9 and M10**: These transistors form the input differential pair, with their gates connected to the input signals \( V_{in1} \) and \( V_{in2} \), respectively.
   - **M11 and M12**: These transistors are connected to a bias voltage \( V_b \) and are likely part of a current mirror or biasing network.
   - **M7 and M8**: These transistors are connected to the power supply \( V_{DD} \) and form part of the load for the differential pair.
   - **M1, M2, M3, M4, M5, M6**: These transistors are part of the output stage and current mirror configuration.

2. **Current Source:**
   - **I_SS**: This is a current source connected to the source terminals of M9 and M10, providing a constant current \( I_{SS} \) to the differential pair.

3. **Capacitors:**
   - **C_L**: There are two capacitors labeled \( C_L \) connected to the drains of M1 and M3, which are likely used for compensation or load purposes.

4. **Nodes and Connections:**
   - **P and Q**: These are nodes where the sources of M9 and M10 are connected to the current source \( I_{SS} \).
   - **X and Y**: These are nodes where the drains of M7 and M2, and M4 and M8, respectively, are connected. These nodes are part of the differential output stage.
   - The gates of M7 and M8 are connected to the drains of M2 and M4, respectively, forming a positive feedback loop typical in differential amplifiers with current mirror loads.

5. **Power Supply:**
   - **V_{DD}**: This is the positive power supply voltage connected to the drains of M7, M8, M4, and M2.

The circuit is a typical differential amplifier with a current mirror load, which is commonly used in analog integrated circuits for amplifying differential signals while providing high gain and common-mode rejection.
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
The image depicts a differential amplifier circuit using MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors). The circuit consists of four MOSFETs labeled M1, M2, M3, and M4, and a current source labeled Iss.

- M1 and M2 are the input transistors of the differential pair. The gates of M1 and M2 receive the differential input signals.
- The sources of M1 and M2 are connected together and to the current source Iss, which is connected to the ground.
- The drains of M1 and M2 are connected to the drains of M3 and M4, respectively.
- M3 and M4 are the load transistors. Their sources are connected to the supply voltage VDD.
- The output voltage Vout is taken from the drain of M2 (which is also the drain of M4).
- The node X is the common node between the drain of M1 and the drain of M3.

The circuit is designed to amplify the difference between the input signals applied to the gates of M1 and M2. The current source Iss sets the tail current for the differential pair, and the load transistors M3 and M4 provide the necessary load resistance for amplification.
```

**Figure 9.81** Supply rejection of differential pair with active current mirror.

#### ▲**Example 9.25**

Calculate the low-frequency PSRR of the feedback circuit shown in Fig. 9.82(a).

Here is the image describtion:
```
The image consists of two diagrams labeled as Figure 9.82, with parts (a) and (b).

**Figure 9.82 (a):**
- This is a schematic of a differential amplifier circuit.
- The circuit includes four MOSFET transistors labeled M1, M2, M3, and M4.
- The source of M1 and M2 are connected together and to a current source labeled Iss, which is connected to the ground.
- The gate of M1 is connected to an input voltage labeled Vin.
- The drain of M1 is connected to the source of M3, and the drain of M2 is connected to the source of M4.
- The gates of M3 and M4 are connected together at a node labeled X.
- The drains of M3 and M4 are connected to a supply voltage labeled VDD.
- The output voltage Vout is taken from the drain of M4.
- There are two capacitors, C1 and C2, connected in series between the output node and the ground, with a node labeled P between them.

**Figure 9.82 (b):**
- This is a small-signal equivalent circuit of the differential amplifier shown in part (a).
- The circuit includes a voltage source V1 connected to a current source labeled gm1V1, which is connected to the ground.
- There is a resistor labeled 1/gm3 connected between VDD and a node labeled X.
- A voltage source V4 is connected to a current source labeled gm4V4, which is connected to the ground.
- The node X is connected to the current source gm1V1 and to the voltage source V4.
- The node X is also connected to a current source labeled gm2V2, which is connected to the ground.
- The output voltage Vout is taken from a node connected to a resistor labeled ro4, which is connected to the ground.
- There are two capacitors, C1 and C2, connected in series between the output node and the ground, with a node labeled P between them.
- The voltage source V2 is connected to the node P.

Overall, the image shows a differential amplifier circuit and its small-signal equivalent model, highlighting the key components and their connections.
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

(a) The first circuit diagram shows a simple inverter. It consists of a single logic gate, represented by a triangle with a circle at its output, indicating an inverter. The input to the inverter is connected to a voltage source labeled \( V_{DD} \). The output of the inverter is labeled \( V_{out} \).

(b) The second circuit diagram is a more complex version of the first. It also features an inverter with its input connected to a voltage source labeled \( V_{DD} \). However, the output of the inverter, labeled \( V_{out} \), is connected to a network of capacitors. Specifically, the output is connected to a capacitor labeled \( C_1 \), which is in series with another capacitor labeled \( C_2 \). The other end of \( C_2 \) is connected to the ground.

In summary, diagram (a) shows a basic inverter circuit, while diagram (b) shows an inverter circuit with an additional capacitor network at the output.
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
The image depicts a schematic diagram of a telescopic operational amplifier (op-amp). The circuit consists of multiple MOSFET transistors arranged in a specific configuration to form the op-amp. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - There are eight MOSFET transistors labeled M1 through M8.
   - M1 and M2 are at the bottom of the circuit, connected to the input voltage \( V_{in} \) and the current source \( I_{SS} \).
   - M3 and M4 are connected above M1 and M2, respectively, with their gates connected to a bias voltage \( V_{b1} \).
   - M5 and M6 are connected above M3 and M4, respectively, with their gates connected to another bias voltage \( V_{b2} \).
   - M7 and M8 are at the top of the circuit, with their gates connected to a third bias voltage \( V_{b3} \).

2. **Connections:**
   - The source of M1 is connected to the current source \( I_{SS} \), which is grounded.
   - The drain of M1 is connected to the source of M3, and similarly, the drain of M2 is connected to the source of M4.
   - The drains of M3 and M4 are connected to the sources of M5 and M6, respectively.
   - The drains of M5 and M6 are connected to the sources of M7 and M8, respectively.
   - The drains of M7 and M8 are connected to the positive supply voltage \( V_{DD} \).
   - The output voltage \( V_{out} \) is taken from the common node between the drains of M5 and M6.

3. **Bias Voltages:**
   - \( V_{b1} \) is applied to the gates of M3 and M4.
   - \( V_{b2} \) is applied to the gates of M5 and M6.
   - \( V_{b3} \) is applied to the gates of M7 and M8.

4. **Labels:**
   - The figure is labeled as "Figure 9.84" with the caption "Noise in a telescopic op amp."

This configuration is typical for a telescopic op-amp, which is known for its high gain and low noise characteristics. The bias voltages \( V_{b1} \), \( V_{b2} \), and \( V_{b3} \) are used to set the operating points of the transistors to ensure proper amplification and performance of the op-amp.
```

Next, we study the noise behavior of the folded-cascode op amp of Fig. 9.85(a), considering only thermal noise at this point. Again, the noise of the cascode devices is negligible at low frequencies, leaving *M*1–*M*2, *M*7–*M*8, and *M*9–*M*<sup>10</sup> as potentially significant sources. Do both pairs *M*7–*M*<sup>8</sup> and *M*9–*M*<sup>10</sup> contribute noise? Using our simple rule, we change the gate voltage of *M*<sup>7</sup> by a small amount [Fig. 9.85(b)], noting that the output indeed changes considerably. The same observation applies to *M*8– *M*<sup>10</sup> as well. To determine the input-referred thermal noise, we first refer the noise of *M*7–*M*<sup>8</sup> to the

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b). Both diagrams appear to represent a type of analog circuit, likely a differential amplifier or a similar configuration, given the presence of multiple transistors and biasing elements.

### Diagram (a):
- **Transistors:**
  - There are 11 transistors labeled M1 through M11.
  - M1 and M2 are connected to the input voltage \( V_{in} \).
  - M3, M4, M5, and M6 form a differential pair with M3 and M4 connected to the bias voltage \( V_{b1} \) and M5 and M6 connected to the bias voltage \( V_{b2} \).
  - M7 and M8 are connected to the supply voltage \( V_{DD} \) and the bias voltage \( V_{b3} \).
  - M9 and M10 are connected to the ground and the bias voltage \( V_{b4} \).
  - M11 is connected to the ground and appears to be part of the input stage with M1 and M2.

- **Connections:**
  - The output voltage \( V_{out} \) is taken from the node between M5 and M6.
  - The circuit is powered by a supply voltage \( V_{DD} \) and has multiple bias voltages \( V_{b1} \), \( V_{b2} \), \( V_{b3} \), and \( V_{b4} \).

### Diagram (b):
- **Transistors:**
  - The transistor configuration is similar to diagram (a) with M1 through M11.
  - The main difference is the addition of a symbol between M7 and M8, which appears to be a current source or a voltage source symbol, indicating a controlled current or voltage source in the circuit.

- **Connections:**
  - The connections remain largely the same as in diagram (a), with the output voltage \( V_{out} \) taken from the same node.
  - The additional symbol between M7 and M8 suggests a modification in the biasing or current control mechanism in this version of the circuit.

### General Observations:
- Both diagrams depict a complex analog circuit with multiple transistors and biasing elements.
- The primary difference between the two diagrams is the inclusion of a controlled source in diagram (b), which may indicate a more precise control of current or voltage in that part of the circuit.
- The circuits are likely used for amplification purposes, given the differential pair configuration and the presence of multiple biasing transistors.

These diagrams are typical in analog circuit design, particularly in the design of operational amplifiers or other precision analog components.
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
The image depicts a schematic diagram of a differential amplifier circuit. Here is a detailed description of the components and their connections:

1. **Transistors:**
   - There are eight MOSFET transistors labeled M1 through M8.
   - M1 and M2 are the input differential pair transistors.
   - M3 and M4 are the load transistors for the differential pair.
   - M5 and M6 are the current mirror transistors.
   - M7 and M8 are the tail current source transistors.

2. **Power Supply:**
   - The circuit is powered by a supply voltage labeled V_DD at the top of the diagram.

3. **Connections:**
   - The gates of M1 and M2 are the differential input terminals, with M1 connected to V_in and M2 connected to a reference voltage.
   - The sources of M1 and M2 are connected together and to a current source labeled I_SS, which is connected to ground.
   - The drains of M1 and M2 are connected to the drains of M3 and M4, respectively.
   - The gates of M3 and M4 are connected together to a bias voltage labeled V_b.
   - The sources of M3 and M4 are connected to V_DD.
   - The drains of M3 and M4 are also connected to the gates of M5 and M6, respectively.
   - The sources of M5 and M6 are connected to the drains of M7 and M8, respectively.
   - The gates of M7 and M8 are connected to a bias voltage labeled V_b.
   - The sources of M7 and M8 are connected to ground.
   - The output voltages are taken from the drains of M5 and M6, labeled V_out1 and V_out2, respectively.

4. **Biasing:**
   - The bias voltage V_b is used to set the operating point of the transistors M3, M4, M7, and M8.

This differential amplifier circuit is designed to amplify the difference between the input signals applied to the gates of M1 and M2, providing differential outputs at V_out1 and V_out2. The current mirror formed by M5 and M6 ensures that the current through the differential pair is mirrored accurately, while the tail current source I_SS sets the total current through the differential pair.
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
The image depicts a schematic diagram of a differential amplifier circuit. The circuit consists of several MOSFET transistors and is labeled as Figure 9.87. Here is a detailed description of the components and their connections:

1. **Power Supply and Ground:**
   - The circuit is powered by a voltage source labeled \( V_{DD} \) at the top.
   - The ground symbol is shown at the bottom, connected to the current source \( I_{SS} \).

2. **Transistors:**
   - There are eight MOSFET transistors labeled \( M_1 \) to \( M_8 \).
   - \( M_1 \) and \( M_2 \) are the input differential pair transistors.
   - \( M_3 \) and \( M_4 \) are the load transistors for the differential pair.
   - \( M_5 \) and \( M_6 \) are the current mirror transistors.
   - \( M_7 \) and \( M_8 \) are the tail current source transistors.

3. **Connections:**
   - The gates of \( M_1 \) and \( M_2 \) are connected to the input signal \( V_{in} \).
   - The sources of \( M_1 \) and \( M_2 \) are connected together and to the current source \( I_{SS} \), which is set to 0.5 mA.
   - The drains of \( M_1 \) and \( M_2 \) are connected to the drains of \( M_3 \) and \( M_4 \), respectively.
   - The gates of \( M_3 \) and \( M_4 \) are connected to their respective drains, forming a current mirror configuration.
   - The sources of \( M_3 \) and \( M_4 \) are connected to \( V_{DD} \).
   - The drains of \( M_5 \) and \( M_6 \) are connected to \( V_{DD} \), and their sources are connected to the drains of \( M_3 \) and \( M_4 \), respectively.
   - The gates of \( M_5 \) and \( M_6 \) are connected to the drains of \( M_3 \) and \( M_4 \), respectively.
   - The gates of \( M_7 \) and \( M_8 \) are connected to a bias voltage \( V_b \).
   - The sources of \( M_7 \) and \( M_8 \) are connected to ground.

4. **Outputs:**
   - The output \( V_{out1} \) is taken from the drain of \( M_5 \).
   - The output \( V_{out2} \) is taken from the drain of \( M_6 \).

This differential amplifier circuit is designed to amplify the difference between the input signals applied to \( M_1 \) and \( M_2 \), with the outputs \( V_{out1} \) and \( V_{out2} \) providing the amplified differential signal.
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