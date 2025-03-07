### Schmitt Triggers Circuits

Lecture 12 

# Effects of Positive Feedback

- From this circuit: *vo* = *Avi* and *vi* = *vf* – *vin* = *βvo* – *vin*
- Because of the positive feedback *vi* is no longer equal to zero (not a virtual ground)
- So as *vi* increases in the positive (negative) direction, increases in the positive (negative) direction.
- Because of the positive feedback, this will increase *vi* in the positive direction (negative) which will further increase *vo* which further increase *vi* and so on.
- When will this stop?

Here is the image describtion:
```
The image depicts a block diagram of a feedback control system. The system consists of the following components:

1. **Summing Junction (Σ)**: This is represented by a circle with a summation symbol (Σ) inside it. It has three input arrows and one output arrow. The inputs are labeled as follows:
   - \( V_{in} \): This is the input signal entering the summing junction from the left.
   - \( + \): This indicates that the input signal \( V_{in} \) is added.
   - \( + \): This indicates that the feedback signal \( \beta V_o \) is also added.

2. **Forward Path Gain Block (A)**: This is a rectangular block labeled "A". The output of the summing junction (\( V_i \)) is fed into this block. The output of this block is labeled \( V_{out} \).

3. **Feedback Path Gain Block (β)**: This is another rectangular block labeled "β". The output of the system (\( V_{out} \)) is fed into this block. The output of this block is labeled \( \beta V_o \), which is fed back into the summing junction.

4. **Output (V_{out})**: The output of the forward path gain block (A) is labeled \( V_{out} \) and is shown as the final output of the system.

The diagram illustrates a typical feedback loop where the output \( V_{out} \) is fed back through a feedback gain \( β \) and combined with the input \( V_{in} \) at the summing junction to form the input \( V_i \) to the forward path gain block \( A \).
```

- If we had infinite power, then never.
- However, we have limited power which is given by the amplifier's DC voltage supplies: +A, -A.
- If *vi* goes positive, then *vo* "instantaneously" grows to +A volts
- And if *vi* goes negative, then *vo* "instantaneously" grows to -A volts

## Hysteresis

*v*

*v*

- Assume that *β=R2 /*(*R1+R2*) *= 0.1* and *vo* levels are *+10* (for *vi* > 0) and *–10 V* (for *vi* < 0)*.*
- First, note that *vi = vf vin.* Now, let's assume *vo* = *+10 V* and therefore *vf* = *1 V* then as long as *vin* is less than *1 V*, then *vo* = *+10 V* (it's high state) since *vi* , the input to the comparator, will be > *0*. Once *vin*  surpasses 1, *vi < 0,* and the output will switch to *–10 V.*
- At this point, *vf* = -*1 V* and as long as the *vin >* -*1 V* , the output will stay in its low state, *-10 V*.
- Note that has the characteristic of being a flip-flop. If one pulses it with high (>1), then the output switches to a low and visa versa.

Here is the image describtion:
```
The image depicts an electronic circuit diagram and its corresponding mathematical analysis, focusing on a hysteresis characteristic. Here is a detailed description:

1. **Circuit Diagram**:
   - The main component is an operational amplifier (op-amp) represented by a triangle with a positive (+) and negative (-) input.
   - The non-inverting input (+) of the op-amp is connected to the ground.
   - The inverting input (-) is connected to a voltage divider network formed by resistors \( R_1 \) and \( R_2 \).
   - The input voltage \( v_{in} \) is applied to the junction of \( R_1 \) and \( R_2 \).
   - The output voltage \( v_o \) is fed back to the inverting input through \( R_1 \).
   - The feedback voltage \( v_f \) is taken from the junction of \( R_1 \) and \( R_2 \) and is given by \( v_f = \beta v_o \).

2. **Mathematical Analysis**:
   - The equations describe the relationship between the input voltage \( v_{in} \), the feedback voltage \( v_f \), and the output voltage \( v_o \).
   - The key equations are:
     - \( v_{in} + v_i = v_f \)
     - \( v_i = v_f - v_{in} \)
     - \( v_f = \beta v_o \)
     - \( v_i = 0.1v_o - v_{in} \)
   - For \( v_i > 0 \), \( v_o = 10 \):
     - \( v_i = 0.1 \times 10 - v_{in} > 0 \Rightarrow 1 - v_{in} > 0 \Rightarrow 1 > v_{in} \)
     - Therefore, \( v_{in} < 1 \).
   - For \( v_i < 0 \), \( v_o = -10 \):
     - \( v_i = 0.1 \times (-10) - v_{in} < 0 \Rightarrow -1 - v_{in} < 0 \Rightarrow -1 < v_{in} \)
     - Therefore, \( v_{in} > -1 \).

3. **Hysteresis Characteristic**:
   - The graph on the right side of the image shows the hysteresis loop.
   - The x-axis represents the input voltage \( v_{in} \), and the y-axis represents the output voltage \( v_o \).
   - The output voltage switches between +10 and -10 depending on the input voltage crossing the thresholds of +1 and -1, respectively.
   - This behavior is characteristic of hysteresis, where the output depends not only on the current input but also on the history of the input.

4. **Conclusion**:
   - The text at the bottom right of the image states, "This is characteristic is called hysteresis," emphasizing the hysteresis behavior of the circuit.

Overall, the image illustrates a hysteresis loop in an op-amp circuit with positive feedback, showing how the output voltage switches between two levels based on the input voltage crossing specific thresholds.
```

Here is the image describtion:
```
The image provided is a detailed description of an electronic inverter circuit, including its schematic diagram, mathematical analysis, and a graph illustrating its behavior.

1. **Title**: The image is titled "Inverter" at the top.

2. **Mathematical Analysis**:
   - The left side of the image contains a series of equations and logical steps that describe the behavior of the inverter circuit.
   - The equations start with the relationship between the input voltage (\(v_{in}\)), the intermediate voltage (\(v_i\)), and the feedback voltage (\(v_f\)).
   - The equations are as follows:
     - \(v_{in} + v_i = v_f\)
     - \(v_i = v_f - v_{in}\)
     - \(v_f = \beta v_o\)
     - \(v_i = \beta v_o - v_{in}\)
   - The analysis is divided into two cases based on the value of \(v_i\):
     - For \(v_i > 0\), \(v_o = A\)
       - This leads to the condition \(v_{in} < \beta A\).
     - For \(v_i < 0\), \(v_o = -A\)
       - This leads to the condition \(v_{in} > -\beta A\).
   - A note at the bottom mentions that \(\pm \beta A\) volts are the thresholds for when the circuit switches states.

3. **Schematic Diagram**:
   - The right side of the image shows the schematic diagram of the inverter circuit.
   - The circuit includes an operational amplifier (op-amp) with the following components:
     - Input voltage \(v_{in}\) connected to the non-inverting input (+) of the op-amp.
     - Feedback voltage \(v_f\) connected to the inverting input (-) of the op-amp through a resistor \(R_1\).
     - A feedback loop from the output \(v_o\) of the op-amp back to the inverting input (-) through a resistor \(R_2\).
     - Ground connections are indicated at various points in the circuit.

4. **Graph**:
   - Below the schematic diagram, there is a graph that plots the output voltage \(v_o\) against the input voltage \(v_{in}\).
   - The graph shows a piecewise linear relationship with two distinct regions:
     - For \(v_{in} < -\beta A\), \(v_o = -A\).
     - For \(v_{in} > \beta A\), \(v_o = A\).
   - The graph clearly indicates the threshold voltages \(\pm \beta A\) where the output switches between \(-A\) and \(A\).

Overall, the image provides a comprehensive explanation of the inverter circuit, including its theoretical analysis, practical implementation, and graphical representation of its behavior.
```

when the circuit switches states.

### Other Forms of Schmitt Triggers

• Non-inverting types

• Specified Thresholds

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) in a non-inverting configuration. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (Op-Amp)**: The op-amp is represented by a triangle with two input terminals and one output terminal. The non-inverting input is marked with a plus sign (+), and the inverting input is marked with a minus sign (-).

2. **Input Voltage Source**: On the left side of the diagram, there is an AC voltage source symbol, which is connected to the ground on one side and to a resistor \( R_1 \) on the other side.

3. **Resistors**:
   - **\( R_1 \)**: Connected between the AC voltage source and the node labeled \( V_i \).
   - **\( R_2 \)**: Connected between the output of the op-amp (\( V_o \)) and the inverting input of the op-amp.
   - **\( R_3 \)** and **\( R_4 \)**: Form a voltage divider network. \( R_3 \) is connected to a voltage source \( V_{ss} \) and \( R_4 \) is connected to the ground. The junction between \( R_3 \) and \( R_4 \) is connected to the non-inverting input of the op-amp.

4. **Currents and Voltages**:
   - **\( V_i \)**: The voltage at the inverting input of the op-amp.
   - **\( V_o \)**: The output voltage of the op-amp.
   - **\( i_2 \)**: The current flowing through resistor \( R_2 \).

5. **Ground Connections**: The circuit has multiple ground connections, indicated by the ground symbols.

The circuit appears to be a non-inverting amplifier configuration, where the input signal is applied to the non-inverting input of the op-amp, and the feedback network consists of resistors \( R_2 \) and \( R_1 \). The voltage divider formed by \( R_3 \) and \( R_4 \) sets a reference voltage at the non-inverting input.
```

Here is the image describtion:
```
The image contains two different circuit diagrams featuring operational amplifiers (op-amps).

1. **Top Circuit Diagram:**
   - This is a non-inverting amplifier configuration.
   - The input voltage \( V_{in} \) is connected to the non-inverting input (+) of the op-amp.
   - The inverting input (-) is connected to a voltage divider formed by resistors \( R_1 \) and \( R_2 \).
   - The output voltage \( V_o \) is fed back to the inverting input through resistor \( R_2 \).
   - The node between \( R_1 \) and \( R_2 \) is labeled \( V_i \).
   - The op-amp is powered by a dual power supply, though the power supply connections are not explicitly shown.

2. **Bottom Circuit Diagram:**
   - This is a comparator circuit with hysteresis (Schmitt trigger).
   - The input voltage \( V_{in} \) is connected to the inverting input (-) of the op-amp through resistor \( R_1 \).
   - The non-inverting input (+) is connected to a voltage divider formed by resistors \( R_2 \) and \( R_3 \), with \( R_2 \) connected to a reference voltage \( V_t \) and \( R_3 \) connected to ground.
   - The output voltage \( V_o \) is taken from the output of the op-amp.
   - The op-amp is powered by a dual power supply, indicated by the positive and negative voltage symbols at the output and input nodes.

Both circuits utilize operational amplifiers in different configurations to achieve amplification and comparison functions, respectively.
```

Here is the image describtion:
```
The image is a detailed diagram and explanation of a specific threshold circuit, likely an operational amplifier (op-amp) comparator with hysteresis. Here is a detailed description of the image:

1. **Circuit Diagram**:
   - The circuit features an operational amplifier (op-amp) with a non-inverting input (+) and an inverting input (-).
   - The non-inverting input is connected to a voltage divider formed by resistors \( R_2 \) and \( R_3 \), with a voltage \( v_t \) at the junction.
   - The inverting input is connected to the input voltage \( v_{in} \) through a resistor \( R_1 \).
   - The output voltage \( v_o \) is connected back to the non-inverting input through resistor \( R_3 \).
   - The circuit is powered by a supply voltage \( V_{SS} \).

2. **Equations and Analysis**:
   - The image includes several equations that describe the behavior of the circuit.
   - The input voltage \( v_i \) is defined as \( v_t - v_{in} \).
   - The output voltage \( v_o \) is \( +A \) when \( v_i > 0 \) and \( -A \) when \( v_i < 0 \).
   - The node equation at the non-inverting input is given, leading to the expression for \( v_t \).
   - The threshold voltages \( V_{t1} \) and \( V_{t2} \) are derived based on the circuit parameters and the supply voltage \( V_{SS} \).

3. **Graph**:
   - A graph is shown at the bottom left, plotting the output voltage \( v_{out} \) against the input voltage \( v_{in} \).
   - The graph illustrates the hysteresis behavior of the circuit, with two distinct threshold voltages \( V_{t1} \) and \( V_{t2} \).
   - The output switches between \( +A \) and \( -A \) as the input voltage crosses these thresholds.

4. **Text**:
   - The title "Specific Thresholds" is prominently displayed at the top.
   - The equations and explanations are provided in a step-by-step manner, detailing the derivation of the threshold voltages and the conditions for the output voltage.

Overall, the image provides a comprehensive explanation of a comparator circuit with hysteresis, including the circuit diagram, mathematical analysis, and graphical representation of its behavior.
```

0; 0; *i t in i o i o v v v v v A v v A* = − > = + < = −

From node at noninvering input:

$$\begin{aligned} \frac{\mathbf{v}\_{\prime}}{R\_{2}} + \frac{\mathbf{v}\_{\prime} - \mathbf{v}\_{o}}{R\_{3}} + \frac{\mathbf{v}\_{\prime} - \mathbf{V}\_{SS}}{R\_{1}} &= \mathbf{0} \\ \mathbf{v}\_{\prime} &= \frac{\frac{\mathbf{V}\_{o}}{R\_{3}} + \frac{\mathbf{V}\_{SS}}{R\_{1}}}{\frac{1}{R\_{2}} + \frac{1}{R\_{3}} + \frac{1}{R\_{1}}} = \frac{\frac{\mathbf{V}\_{o}}{R\_{3}} + \frac{\mathbf{V}\_{SS}}{R\_{1}}}{G\_{T}R\_{3}} = \frac{\mathbf{v}\_{o}}{G\_{T}R\_{3}} + \frac{\mathbf{V}\_{SS}}{G\_{T}R\_{1}} \\ \mathbf{v}\_{\prime} &= \frac{\mathbf{v}\_{o}}{G\_{T}R\_{3}} + \frac{\mathbf{V}\_{SS}}{G\_{T}R\_{1}} - \mathbf{v}\_{in} \\ \mathbf{v}\_{\prime} &= \frac{A}{G\_{T}R\_{3}} + \frac{\mathbf{V}\_{SS}}{G\_{T}R\_{1}} - \mathbf{v}\_{in} > 0; \mathbf{v}\_{in} < V\_{\prime 1} = \frac{A}{G\_{T}R\_{3}} + \frac{V\_{SS}}{G\_{T}R\_{1}} \\ \mathbf{v}\_{\prime} &= \frac{-A}{G\_{T}R\_{3}} + \frac{V\_{SS}}{G\_{T}R\_{1}} - \mathbf{v}\_{in} < 0; \mathbf{v}\_{in} > V\_{\prime 2} = \frac{-A}{G\_{T}R\_{3}} + \frac{V\_{SS}}{G\_{T}R\_{1}} \end{aligned}$$

30

## An Example

• Choose the 3 resistors to provide thresholds of *5*±*0.1 V* for output levels of ±*14.6 V*. 

Here is the image describtion:
```
The image consists of two main parts: a circuit diagram on the left and a set of equations on the right.

### Circuit Diagram:
- The circuit features an operational amplifier (op-amp) in a non-inverting configuration.
- The op-amp is represented by a triangle with the positive input (+) at the bottom and the negative input (-) at the top.
- The positive input of the op-amp is connected to a voltage source labeled \( v_t \) through a resistor \( R_3 \).
- The negative input of the op-amp is connected to a voltage source labeled \( v_i \) through a resistor \( R_2 \).
- The output of the op-amp is connected to a node that branches off to a resistor \( R_1 \) and a voltage source \( V_{SS} \).
- The resistor \( R_1 \) is connected to the positive supply voltage \( V_{SS} \).
- The voltage source \( v_{in} \) is connected to the ground.

### Equations:
- The equations describe the behavior of the circuit in the non-inverting mode.
- The first equation is a general expression for the non-inverting mode:
  \[
  \frac{V_t}{R_2} + \frac{V_t - V_{SS}}{R_1} + \frac{V_t - v_o}{R_3} = 0
  \]
- The second set of equations uses specific values for \( V_{SS} \), \( V_t \), and \( v_o \):
  - Using \( V_{SS} = 15V \), \( V_t = 5.1V \), and \( v_o = +14.6V \):
    \[
    \frac{5.1}{R_2} + \frac{5.1 - 15}{R_1} + \frac{5.1 - 14.6}{R_3} = \frac{5.1}{R_2} + \frac{9.9}{R_1} + \frac{9.5}{R_3} = 0
    \]
  - Using \( V_t = 4.9V \) for \( v_o = -14.6V \):
    \[
    \frac{4.9}{R_2} + \frac{4.9 - 15}{R_1} + \frac{4.9 + 14.6}{R_3} = \frac{4.9}{R_2} + \frac{10.1}{R_1} + \frac{19.5}{R_3} = 0
    \]

The image provides a detailed analysis of the circuit's behavior in the non-inverting mode, using specific voltage values to illustrate the calculations.
```

• We need to chose one of the 3 resistors. If we choose *R3= 1 M*, then *R1=20.55 k* and *R2 = 10.38 k*. If we chose resistors too small then may draw excessive amounts of current from our *15 V* supply and create a large power drain on the circuit. *\_* 

#### Example contintued

Here is the image describtion:
```
The image consists of two main parts: a set of mathematical expressions on the left and a graph on the right.

### Mathematical Expressions:
1. **First Expression:**
   - \( v_i = v_t - v_{in} \)
   - When \( v_i > 0 \); \( v_o = +14.6v \)
   - Therefore, \( v_i = v_t - v_{in} > 0 \)
   - This implies \( v_t > v_{in} \); or \( v_{in} < 5.1 \)

2. **Second Expression:**
   - \( v_i = v_t - v_{in} \)
   - When \( v_i < 0 \); \( v_o = -14.6v \)
   - Therefore, \( v_i = v_t - v_{in} < 0 \)
   - This implies \( v_t < v_{in} \); or \( v_{in} > 4.9 \)

### Graph:
- The graph is a plot of \( v_{out} \) versus \( v_{in} \).
- The vertical axis represents \( v_{out} \) with values +14.6 and -14.6 marked.
- The horizontal axis represents \( v_{in} \) with values +4.9 and +5.1 marked.
- The graph shows a piecewise function with two distinct horizontal lines:
  - For \( v_{in} < 4.9 \), \( v_{out} \) is +14.6.
  - For \( v_{in} > 5.1 \), \( v_{out} \) is -14.6.
- There is a transition between these two states, indicated by vertical lines at \( v_{in} = 4.9 \) and \( v_{in} = 5.1 \).

### Summary:
The image describes a system where the output voltage \( v_{out} \) switches between +14.6V and -14.6V based on the input voltage \( v_{in} \). The switching thresholds are at \( v_{in} = 4.9V \) and \( v_{in} = 5.1V \). The mathematical expressions explain the conditions under which the output voltage changes, and the graph visually represents this behavior.
```

#### Another Example

- What are the transfer characteristics for this circuit if R,=1k and R,= 2k and the thresholds levels are +10 V.
	- Vm = i(R1 + R2) + vg V = iR1 = in = " in = " = R1" = R1
	R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 vi = Vin -V = Vin -V = Vin - Lin - Yo R1 - R1 - R1 - R1 - R2 - R1 - R2 - R1 - R2 v; = Vin - - in - - in - - - Vin + - -For vg = + 10 V, v; > 0 v; = = V;n + = > 0; = V; > = = = ; V; > = 5 For v == 10 V, v; < 0 v; = = Vm + = = 0; = Vm < = = = = = Vm < 5

Here is the image describtion:
```
The image consists of two parts: an electronic circuit diagram and a graph.

1. **Electronic Circuit Diagram:**
   - The circuit features an operational amplifier (op-amp) with a non-inverting configuration.
   - The input voltage \( v_{in} \) is applied to the circuit through a voltage source symbol, which is connected to the ground.
   - A resistor \( R_1 \) is connected in series with the input voltage \( v_{in} \).
   - The voltage at the node between \( R_1 \) and the op-amp is labeled \( v_i \).
   - The op-amp has its non-inverting input (+) connected to the ground.
   - The inverting input (-) of the op-amp is connected to the node \( v_i \).
   - A feedback resistor \( R_2 \) is connected between the output \( v_o \) of the op-amp and the inverting input (-).
   - The current flowing through \( R_1 \) and \( R_2 \) is labeled \( i \).

2. **Graph:**
   - The graph is a plot of the output voltage \( v_o \) versus the input voltage \( v_{in} \).
   - The x-axis represents the input voltage \( v_{in} \) and ranges from -5 to +5.
   - The y-axis represents the output voltage \( v_o \) and ranges from -10 to +10.
   - The graph shows a piecewise linear relationship with saturation limits.
   - For \( v_{in} \) values between -5 and +5, the output voltage \( v_o \) is linearly dependent on \( v_{in} \).
   - When \( v_{in} \) exceeds +5, the output voltage \( v_o \) saturates at +10.
   - When \( v_{in} \) is less than -5, the output voltage \( v_o \) saturates at -10.
   - The graph indicates that the op-amp is operating in a configuration where it amplifies the input voltage within a certain range and saturates beyond that range.

Overall, the image illustrates a non-inverting op-amp circuit with a feedback resistor and its corresponding output voltage behavior as a function of the input voltage.
```

### Astable Multivibrators

- A switching oscillator or Astable Multivibrator can be formed from a Schmitt trigger as follows:
- Assume that output levels are ±A and the thresholds are ±A/2 since the feedback voltage = ½ *vo*.

Here is the image describtion:
```
The image consists of two main parts: a mathematical explanation and an electronic circuit diagram.

### Mathematical Explanation:
1. **Equations and Conditions:**
   - The first equation is \( v_i = v_t - v_{in} \).
   - When \( v_i > 0 \), \( v_o = A \); therefore, \( v_i = v_t - v_{in} > 0 \).
   - This implies \( v_t > v_{in} \) or \( v_{in} < \frac{A}{2} \).
   - The second equation is \( v_i = v_t - v_{in} \).
   - When \( v_i < 0 \), \( v_o = -A \); therefore, \( v_i = v_t - v_{in} < 0 \).
   - This implies \( v_t < v_{in} \) or \( v_{in} > -\frac{A}{2} \).

2. **Graph:**
   - The graph is a plot of \( v_o \) versus \( v_{in} \).
   - The y-axis represents \( v_o \) with values \( A \) and \(-A \).
   - The x-axis represents \( v_{in} \) with values \(\frac{A}{2}\) and \(-\frac{A}{2}\).
   - The graph shows a hysteresis loop, indicating a bistable system where the output \( v_o \) switches between \( A \) and \(-A \) based on the input \( v_{in} \).

### Electronic Circuit Diagram:
- The circuit is an operational amplifier (op-amp) configuration.
- **Components:**
  - A capacitor \( C \) connected to the input \( v_{in} \).
  - A resistor \( R \) connected in series with the capacitor.
  - The op-amp has a non-inverting input (+) and an inverting input (-).
  - The inverting input is connected to the junction of \( R \) and \( C \).
  - The non-inverting input is connected to a voltage divider formed by two resistors \( R_f \) connected to ground.
  - The output \( v_o \) of the op-amp is fed back to the inverting input through a feedback resistor \( R_f \).
  - The op-amp is powered by a dual power supply (positive and negative).

This circuit is likely a Schmitt trigger, which is used to convert an analog input signal into a digital output signal, exhibiting hysteresis as shown in the graph.
```

### Astable Multivibrators

- Assume that the output starts off at +A.
- The capacitor starts to charge to +A
- However, when it reaches +A/2, *vi =* 0 and the output switches to –A.
- The capacitor then charges to –A.
- However, when it reaches –A/2, *vi =0* and the output switches to +A
- And the capacitor charges to +A
- This process continues.

Here is the image describtion:
```
The image is a graph depicting a piecewise linear function, which appears to be a transfer characteristic of an electronic component or system. The graph is plotted on a Cartesian coordinate system with the horizontal axis labeled as \( V_{in} \) and the vertical axis labeled as \( V_o \).

Key features of the graph include:

1. The graph has four distinct linear segments:
   - A horizontal line at \( V_o = A \) for \( V_{in} \geq A/2 \).
   - A horizontal line at \( V_o = -A \) for \( V_{in} \leq -A/2 \).
   - A sloped line with a positive slope between \( V_{in} = -A/2 \) and \( V_{in} = A/2 \), passing through the origin.
   - Vertical lines at \( V_{in} = -A/2 \) and \( V_{in} = A/2 \) connecting the horizontal lines to the sloped line.

2. The graph is symmetric about the origin.

3. The point where the sloped line intersects the vertical axis (at \( V_{in} = 0 \)) is marked with a red dot, indicating a significant point on the graph.

4. The values on the axes are labeled with specific points:
   - \( V_{in} = -A/2 \) and \( V_{in} = A/2 \) on the horizontal axis.
   - \( V_o = -A \) and \( V_o = A \) on the vertical axis.

The graph represents a function where the output \( V_o \) is limited to a maximum value of \( A \) and a minimum value of \( -A \), with a linear relationship between \( V_{in} \) and \( V_o \) within the range of \( -A/2 \) to \( A/2 \).
```

Here is the image describtion:
```
The image depicts an electrical circuit diagram featuring an operational amplifier (op-amp) in a configuration that appears to be a band-pass filter. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (Op-Amp)**:
   - The op-amp is represented by a triangular symbol with the inverting input (-) at the top and the non-inverting input (+) at the bottom.
   - The output of the op-amp is on the right side of the triangle.

2. **Resistors**:
   - There are three resistors labeled \( R \) and \( R_f \).
   - Resistor \( R \) is connected in series with the capacitor \( C \) and the inverting input (-) of the op-amp.
   - Two resistors labeled \( R_f \) are connected in a feedback loop. One \( R_f \) is connected between the output of the op-amp and the inverting input (-), and the other \( R_f \) is connected from the inverting input (-) to the ground.

3. **Capacitor**:
   - The capacitor is labeled \( C \) and is connected between the input voltage \( v_i \) and the ground.

4. **Voltage Sources**:
   - The input voltage is labeled \( v_i \) and is applied to the left side of the circuit, connected to the capacitor \( C \).
   - The output voltage is labeled \( v_o \) and is taken from the output of the op-amp.

5. **Ground Connections**:
   - The circuit has multiple ground connections, indicated by the ground symbols. These are connected to the negative terminal of the capacitor \( C \), the bottom of the resistor \( R_f \), and the negative terminal of the output voltage \( v_o \).

6. **Connections**:
   - The input voltage \( v_i \) is applied to the capacitor \( C \), which is then connected to the resistor \( R \).
   - The resistor \( R \) is connected to the inverting input (-) of the op-amp.
   - The non-inverting input (+) of the op-amp is connected to the ground.
   - The output of the op-amp is connected to one end of the feedback resistor \( R_f \), and the other end of this resistor is connected to the inverting input (-).
   - Another feedback resistor \( R_f \) is connected from the inverting input (-) to the ground.

This configuration suggests a band-pass filter, where the combination of resistors and capacitors determines the frequency range that will be passed through the filter.
```

Here is the image describtion:
```
The image depicts two waveforms superimposed on the same graph. The vertical axis represents amplitude, marked with values +A, +A/2, -A/2, and -A. The horizontal axis represents time.

1. The first waveform is a black sinusoidal wave that oscillates smoothly between +A and -A. It crosses the horizontal axis at regular intervals, indicating zero amplitude at those points. The wave reaches its maximum positive amplitude (+A) and maximum negative amplitude (-A) symmetrically.

2. The second waveform is an orange square wave that alternates between +A and -A. The transitions between +A and -A are abrupt, creating a rectangular shape. The square wave maintains its amplitude at +A or -A for equal durations before switching to the opposite amplitude.

The sinusoidal wave and the square wave are aligned such that the square wave transitions occur at the points where the sinusoidal wave crosses the horizontal axis (zero amplitude). The sinusoidal wave appears to have a frequency that matches the frequency of the square wave, with each cycle of the sinusoidal wave corresponding to one complete cycle of the square wave.
```

## Timing Calculation

Here is the image describtion:
```
The image depicts a comparison between a square wave and a sine wave. Both waves are plotted on the same graph, sharing the same amplitude and period. 

Key features of the image include:

1. **Amplitude Levels**: 
   - The maximum positive amplitude is labeled as +A.
   - The midpoint positive amplitude is labeled as +A/2.
   - The midpoint negative amplitude is labeled as -A/2.
   - The maximum negative amplitude is labeled as -A.

2. **Square Wave**:
   - The square wave alternates between +A and -A.
   - It maintains a constant value of +A for half the period and then switches to -A for the other half.
   - The transitions between +A and -A are instantaneous (vertical lines).

3. **Sine Wave**:
   - The sine wave smoothly oscillates between +A and -A.
   - It crosses the zero amplitude level at the midpoint of each half-period.
   - The sine wave is continuous and smooth, unlike the abrupt changes in the square wave.

4. **Period (T)**:
   - The period of the waves is denoted by T.
   - A horizontal double-headed arrow indicates the length of one period (T) on the graph.

The graph effectively illustrates the differences in waveform shapes and transitions between a square wave and a sine wave, both having the same amplitude and period.
```

Start the timing calculation here

InitialCondition : ( ) 1 2 *v t K K e t RC c* = + −

$$\begin{aligned} \nu\_c(0) &= -\frac{A}{2} = K\_1 + K\_2 e^{-0/RC} = K\_1 + K\_2 \text{ (eqn.1)}\\ \text{Final condition :} \end{aligned}$$

$$\nu\_c(\infty) = +A = K\_1 + K\_2 e^{-\circ/RC} = K\_1 \text{ (eqn. 2)}$$

$$\begin{aligned} &\text{From eqns (1) and (2)}\\ &K\_1 = A\\ &K\_2 = -\frac{A}{2} - K\_1 = -\frac{3}{2}A \end{aligned}$$

$$\begin{aligned} \nu\_c(t) &= A(1 - \frac{3}{2}e^{-t/RC}) \\ \text{But} \\ \nu\_c(\frac{T}{2}) &= \frac{A}{2} = A(1 - \frac{3}{2}e^{-T/2RC}) \\ \therefore \, e^{-T/2RC} &= \frac{1}{3} \\ T &= 2RC \ln(3) \end{aligned}$$

## Homework

- Comparators and Schmitt Trigger Circuits – Problems: 12.8-9
- Astable Multivibrators
	- Problems: 12.14