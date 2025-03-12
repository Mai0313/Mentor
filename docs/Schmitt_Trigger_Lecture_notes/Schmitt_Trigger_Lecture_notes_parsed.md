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
The image depicts a block diagram of a feedback control system. Here is a detailed description of the components and their connections:

1. **Input Signal (\(v_{in}\))**: The system starts with an input signal labeled \(v_{in}\).

2. **Summing Junction (\(\Sigma\))**: The input signal \(v_{in}\) enters a summing junction, represented by a circle with a summation symbol (\(\Sigma\)) inside it. This junction has two inputs and one output. Both inputs are marked with a plus sign, indicating that they are added together.

3. **Intermediate Signal (\(v_i\))**: The output of the summing junction is labeled \(v_i\), which is the intermediate signal that goes into the next block.

4. **Amplifier Block (A)**: The intermediate signal \(v_i\) is fed into a block labeled \(A\), which represents an amplifier or a system with a gain factor \(A\). The output of this block is the output signal \(v_{out}\).

5. **Output Signal (\(v_{out}\))**: The output of the amplifier block is labeled \(v_{out}\), which is the output signal of the entire system.

6. **Feedback Path**: The output signal \(v_{out}\) is also fed back into the system through a feedback path.

7. **Feedback Block (\(\beta\))**: In the feedback path, the output signal \(v_{out}\) passes through a block labeled \(\beta\), which represents a feedback factor or a feedback network. The output of this block is \(\beta v_{out}\).

8. **Feedback Signal (\(\beta v_{out}\))**: The output of the feedback block (\(\beta v_{out}\)) is fed back into the summing junction (\(\Sigma\)).

In summary, the diagram represents a feedback control system where the input signal \(v_{in}\) is combined with the feedback signal \(\beta v_{out}\) at the summing junction. The resulting signal \(v_i\) is then amplified by a factor \(A\) to produce the output signal \(v_{out}\), which is partially fed back into the system through a feedback factor \(\beta\).
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
The image depicts a non-inverting Schmitt trigger circuit using an operational amplifier (op-amp) and its associated hysteresis characteristic. Here is a detailed description:

### Circuit Diagram:
1. **Operational Amplifier (Op-Amp)**:
   - The op-amp is represented by a triangle with the inverting input (-) at the top and the non-inverting input (+) at the bottom.
   - The output of the op-amp is connected to the right side of the triangle.

2. **Input Voltage (vin)**:
   - The input voltage \( v_{in} \) is applied to the non-inverting input (+) of the op-amp.

3. **Feedback Network**:
   - The feedback network consists of two resistors, \( R_1 \) and \( R_2 \).
   - The output voltage \( v_o \) is fed back to the inverting input (-) through resistor \( R_1 \).
   - The junction between \( R_1 \) and \( R_2 \) is connected to the inverting input (-) of the op-amp.
   - The other end of \( R_2 \) is connected to the ground.

4. **Voltage at Inverting Input (vi)**:
   - The voltage at the inverting input \( v_i \) is determined by the feedback network and is given by \( v_i = v_f - v_{in} \), where \( v_f \) is the feedback voltage.

5. **Feedback Voltage (vf)**:
   - The feedback voltage \( v_f \) is a fraction of the output voltage \( v_o \) and is given by \( v_f = \beta v_o \), where \( \beta \) is the feedback factor.

### Mathematical Analysis:
- The equations provided in the image describe the behavior of the circuit:
  1. \( v_{in} + v_i = v_f \)
  2. \( v_i = v_f - v_{in} \)
  3. \( v_f = \beta v_o \)
  4. \( v_i = 0.1v_o - v_{in} \)

### Conditions for Output Voltage (vo):
- For \( v_i > 0 \):
  - \( v_o = 10 \)
  - \( v_i = 0.1 \times 10 - v_{in} > 0 \Rightarrow 1 - v_{in} > 0 \Rightarrow 1 > v_{in} \)
  - Therefore, \( v_{in} < 1 \)

- For \( v_i < 0 \):
  - \( v_o = -10 \)
  - \( v_i = 0.1 \times (-10) - v_{in} < 0 \Rightarrow -1 - v_{in} < 0 \Rightarrow -1 < v_{in} \)
  - Therefore, \( v_{in} > -1 \)

### Hysteresis Characteristic:
- The image includes a graph showing the hysteresis characteristic of the circuit.
  - The x-axis represents the input voltage \( v_{in} \).
  - The y-axis represents the output voltage \( v_o \).
  - The graph shows that the output voltage \( v_o \) switches between 10 and -10, depending on the input voltage \( v_{in} \).
  - The switching thresholds are at \( v_{in} = 1 \) and \( v_{in} = -1 \).

### Conclusion:
- The hysteresis characteristic is highlighted in the image, indicating that the output voltage \( v_o \) depends on the history of the input voltage \( v_{in} \). This behavior is typical of a Schmitt trigger circuit, which provides noise immunity and a clear distinction between high and low states.
```

Here is the image describtion:
```
The image is a detailed explanation of an inverter circuit using an operational amplifier (op-amp). It includes both the circuit diagram and the mathematical analysis of its operation.

### Circuit Diagram:
- The circuit features an op-amp with its inverting input (-) connected to a voltage divider network consisting of resistors \( R_1 \) and \( R_2 \).
- The non-inverting input (+) of the op-amp is connected to the ground.
- The input voltage \( v_{in} \) is applied to the junction of the inverting input and the voltage divider.
- The output voltage \( v_o \) is taken from the output of the op-amp.
- The feedback voltage \( v_f \) is taken from the junction between \( R_1 \) and \( R_2 \) and is connected to the inverting input of the op-amp.

### Mathematical Analysis:
1. **Equations:**
   - The input voltage \( v_{in} \) and the feedback voltage \( v_f \) sum up to give the voltage at the inverting input \( v_i \):
     \[
     v_{in} + v_i = v_f
     \]
   - Rearranging the above equation:
     \[
     v_i = v_f - v_{in}
     \]
   - The feedback voltage \( v_f \) is proportional to the output voltage \( v_o \) by a factor \( \beta \):
     \[
     v_f = \beta v_o
     \]
   - Substituting \( v_f \) in the equation for \( v_i \):
     \[
     v_i = \beta v_o - v_{in}
     \]

2. **Case Analysis:**
   - For \( v_i > 0 \):
     - The output voltage \( v_o \) is at its positive saturation level \( A \):
       \[
       v_o = A
       \]
     - Substituting \( v_o \) in the equation for \( v_i \):
       \[
       v_i = \beta A - v_{in} > 0 \implies \beta A > v_{in}
       \]
     - Therefore, the condition for \( v_i > 0 \) is:
       \[
       v_{in} < \beta A
       \]

   - For \( v_i < 0 \):
     - The output voltage \( v_o \) is at its negative saturation level \( -A \):
       \[
       v_o = -A
       \]
     - Substituting \( v_o \) in the equation for \( v_i \):
       \[
       v_i = \beta (-A) - v_{in} < 0 \implies -\beta A < v_{in}
       \]
     - Therefore, the condition for \( v_i < 0 \) is:
       \[
       v_{in} > -\beta A
       \]

3. **Thresholds:**
   - The thresholds for the input voltage \( v_{in} \) to switch the state of the output voltage \( v_o \) are \( \pm \beta A \).

### Graph:
- The graph at the bottom right of the image shows the relationship between the input voltage \( v_{in} \) and the output voltage \( v_o \).
- The output voltage \( v_o \) switches between \( A \) and \( -A \) at the thresholds \( \beta A \) and \( -\beta A \), respectively.

Overall, the image provides a comprehensive explanation of the inverter circuit, including the circuit diagram, mathematical derivation, and graphical representation of the input-output relationship.
```

when the circuit switches states.

### Other Forms of Schmitt Triggers

• Non-inverting types

• Specified Thresholds

Here is the image describtion:
```
The image depicts an operational amplifier (op-amp) circuit with several components connected to it. Here is a detailed description of the circuit:

1. **Operational Amplifier (Op-Amp)**: The op-amp is represented by a triangular symbol with two input terminals and one output terminal. The non-inverting input is marked with a "+" sign, and the inverting input is marked with a "-" sign. The output terminal is at the right side of the triangle.

2. **Resistors**:
   - **R1**: This resistor is connected between the input voltage source and the inverting input of the op-amp.
   - **R2**: This resistor is connected between the output of the op-amp and the inverting input, forming a feedback loop.
   - **R3** and **R4**: These resistors are connected in series between a voltage source \( V_{ss} \) and ground. The junction between R3 and R4 is connected to the non-inverting input of the op-amp.

3. **Voltage Sources**:
   - **Input Voltage Source**: This is an AC voltage source connected to the left side of the circuit, providing the input signal to the circuit.
   - **\( V_{ss} \)**: This is a DC voltage source connected to the series combination of R3 and R4.

4. **Ground Connections**: The circuit has multiple ground connections, indicated by the ground symbols. These are connected to the negative terminals of the voltage sources and one end of resistor R4.

5. **Currents and Voltages**:
   - **\( V_i \)**: This is the voltage at the inverting input of the op-amp.
   - **\( V_o \)**: This is the output voltage of the op-amp.
   - **\( i_2 \)**: This is the current flowing through resistor R2.

The circuit appears to be a configuration of an op-amp with feedback, possibly a non-inverting amplifier due to the feedback connection from the output to the inverting input and the input signal applied to the inverting input through R1. The non-inverting input is biased with a voltage divider formed by R3 and R4 connected to \( V_{ss} \).
```

Here is the image describtion:
```
The image consists of two different circuit diagrams, each featuring an operational amplifier (op-amp) in different configurations.

### Top Circuit Diagram:
1. **Components:**
   - **Operational Amplifier (Op-Amp):** The op-amp is depicted with the standard triangle symbol, with the inverting input (-) and non-inverting input (+) clearly marked.
   - **Resistors:** Two resistors, labeled \( R_1 \) and \( R_2 \), are present in the circuit.
   - **Voltage Source:** A sinusoidal voltage source labeled \( v_{in} \).

2. **Connections:**
   - The voltage source \( v_{in} \) is connected to the ground and to one end of resistor \( R_1 \).
   - The other end of \( R_1 \) is connected to the inverting input (-) of the op-amp.
   - The non-inverting input (+) of the op-amp is connected to the ground.
   - The output \( v_o \) of the op-amp is connected to one end of resistor \( R_2 \).
   - The other end of \( R_2 \) is connected back to the inverting input (-) of the op-amp, forming a feedback loop.

### Bottom Circuit Diagram:
1. **Components:**
   - **Operational Amplifier (Op-Amp):** Similar to the top diagram, the op-amp is shown with the inverting input (-) and non-inverting input (+) marked.
   - **Resistors:** Three resistors, labeled \( R_1 \), \( R_2 \), and \( R_3 \).
   - **Voltage Sources:** Two voltage sources, labeled \( v_{in} \) and \( v_t \).

2. **Connections:**
   - The voltage source \( v_{in} \) is connected to the ground and to one end of resistor \( R_1 \).
   - The other end of \( R_1 \) is connected to the inverting input (-) of the op-amp.
   - The non-inverting input (+) of the op-amp is connected to the ground.
   - The output \( v_o \) of the op-amp is connected to one end of resistor \( R_3 \).
   - The other end of \( R_3 \) is connected back to the inverting input (-) of the op-amp, forming a feedback loop.
   - Resistor \( R_2 \) is connected between the inverting input (-) of the op-amp and the voltage source \( v_t \), which is also connected to the ground.

### Additional Details:
- Both diagrams show the op-amp powered by a dual supply voltage, indicated by the positive and negative signs near the op-amp symbol.
- The top diagram appears to be a simple inverting amplifier configuration, while the bottom diagram seems to be a more complex configuration, possibly a summing amplifier or a differential amplifier, given the additional resistor and voltage source.

Overall, the image provides a clear representation of two different op-amp circuit configurations, highlighting the connections and components involved in each.
```

Here is the image describtion:
```
The image is a detailed representation of a specific threshold circuit involving an operational amplifier (op-amp) and a set of resistors. The circuit diagram is accompanied by mathematical equations and a graph to explain the behavior of the circuit.

### Circuit Diagram:
1. **Components:**
   - **Operational Amplifier (Op-Amp):** The op-amp is depicted in the center of the circuit with its inverting (-) and non-inverting (+) inputs clearly marked.
   - **Resistors:** Three resistors are labeled as \( R_1 \), \( R_2 \), and \( R_3 \).
   - **Voltage Sources:** There are two voltage sources, \( V_{SS} \) and \( V_{in} \), connected to the circuit.
   - **Ground Connections:** The circuit has multiple ground connections, indicated by the ground symbols.

2. **Connections:**
   - \( R_1 \) is connected between the positive voltage source \( V_{SS} \) and the non-inverting input of the op-amp.
   - \( R_2 \) is connected between the inverting input of the op-amp and ground.
   - \( R_3 \) is connected between the output of the op-amp and the inverting input.
   - The input voltage \( V_{in} \) is applied to the inverting input through a connection to ground.

### Mathematical Equations:
The right side of the image contains a series of equations that describe the behavior of the circuit:

1. **Input Voltage Relation:**
   - \( v_i = v_t - v_{in} \)
   - \( v_i > 0; v_o = +A \)
   - \( v_i < 0; v_o = -A \)

2. **Node Equation at Non-Inverting Input:**
   - The equation is derived from Kirchhoff's Current Law (KCL) at the non-inverting input node:
     \[
     \frac{v_t + v_t - v_o + v_t - V_{SS}}{R_2} + \frac{v_o + V_{SS}}{R_3} + \frac{v_o + V_{SS}}{R_1} = 0
     \]

3. **Threshold Voltage \( v_t \):**
   - The threshold voltage \( v_t \) is derived and simplified:
     \[
     v_t = \frac{v_o + V_{SS}}{G_T R_3} = \frac{v_o + V_{SS}}{G_T R_1}
     \]
   - Where \( G_T = \frac{1}{R_2} + \frac{1}{R_3} + \frac{1}{R_1} \)

4. **Input Voltage \( v_i \):**
   - The input voltage \( v_i \) is expressed in terms of the output voltage \( v_o \) and the resistances:
     \[
     v_i = \frac{v_o + V_{SS}}{G_T R_3} - v_{in}
     \]
   - For \( v_i > 0 \):
     \[
     v_i = \frac{A + V_{SS}}{G_T R_3} - v_{in} > 0; v_{in} < V_{t1}
     \]
   - For \( v_i < 0 \):
     \[
     v_i = \frac{-A + V_{SS}}{G_T R_3} - v_{in} < 0; v_{in} > V_{t2}
     \]

### Graph:
The bottom left of the image shows a graph plotting \( v_{out} \) against \( v_{in} \):

- The y-axis represents the output voltage \( v_{out} \), ranging from \( -A \) to \( +A \).
- The x-axis represents the input voltage \( v_{in} \).
- The graph shows a hysteresis loop with two threshold voltages \( V_{t1} \) and \( V_{t2} \), indicating the points where the output switches between \( +A \) and \( -A \).

### Summary:
The image provides a comprehensive explanation of a specific threshold circuit using an op-amp, including the circuit diagram, mathematical derivations, and a graphical representation of the output behavior. The equations and graph illustrate how the circuit responds to different input voltages, switching the output between two distinct levels based on the threshold conditions.
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
1. **Operational Amplifier (Op-Amp)**:
   - The op-amp is depicted as a triangle with the standard symbols for the inverting input (-) and the non-inverting input (+).
   - The inverting input (-) is connected to a node where three resistors meet.
   - The non-inverting input (+) is connected to a voltage source labeled \( v_i \).

2. **Resistors**:
   - **\( R_1 \)**: Connected between the positive supply voltage \( V_{SS} \) and the node at the inverting input of the op-amp.
   - **\( R_2 \)**: Connected between the node at the inverting input of the op-amp and a voltage source \( V_t \).
   - **\( R_3 \)**: Connected between the node at the inverting input of the op-amp and the output of the op-amp \( v_o \).

3. **Voltage Sources**:
   - **\( V_{SS} \)**: The positive supply voltage connected to the top of \( R_1 \).
   - **\( V_t \)**: A voltage source connected to the bottom of \( R_2 \).
   - **\( v_{in} \)**: The input voltage connected to the non-inverting input of the op-amp.

### Equations:
The equations on the right side of the image describe the behavior of the circuit in the non-inverting mode of the op-amp.

1. **General Equation**:
   \[
   \frac{V_t}{R_2} + \frac{V_t - V_{SS}}{R_1} + \frac{V_t - v_o}{R_3} = 0
   \]
   This equation represents the sum of currents at the node where the resistors \( R_1 \), \( R_2 \), and \( R_3 \) meet, assuming the ideal op-amp condition where the input current is zero.

2. **Specific Case 1**:
   Using \( V_{SS} = 15V \) and \( V_t = 5.1V \) for \( v_o = +14.6V \):
   \[
   \frac{5.1}{R_2} + \frac{5.1 - 15}{R_1} + \frac{5.1 - 14.6}{R_3} = \frac{5.1}{R_2} + \frac{9.9}{R_1} + \frac{9.5}{R_3} = 0
   \]

3. **Specific Case 2**:
   Using \( V_t = 4.9V \) for \( v_o = -14.6V \):
   \[
   \frac{4.9}{R_2} + \frac{4.9 - 15}{R_1} + \frac{4.9 + 14.6}{R_3} = \frac{4.9}{R_2} + \frac{10.1}{R_1} + \frac{19.5}{R_3} = 0
   \]

These equations are used to analyze the behavior of the op-amp circuit under different conditions of the output voltage \( v_o \).
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
- The graph is a plot of \( v_{out} \) (output voltage) versus \( v_{in} \) (input voltage).
- The vertical axis represents \( v_{out} \) with values marked at +14.6 and -14.6.
- The horizontal axis represents \( v_{in} \) with values marked at +4.9 and +5.1.
- The graph shows a piecewise function with two distinct horizontal lines:
  - For \( v_{in} < 4.9 \), \( v_{out} \) is at +14.6.
  - For \( v_{in} > 5.1 \), \( v_{out} \) is at -14.6.
- There is a vertical transition between these two horizontal lines at \( v_{in} = 4.9 \) and \( v_{in} = 5.1 \).

### Summary:
The image illustrates the behavior of an output voltage \( v_{out} \) in response to an input voltage \( v_{in} \). The output voltage switches between +14.6V and -14.6V depending on whether the input voltage is below 4.9V or above 5.1V, respectively. The mathematical expressions provide the conditions for these transitions, and the graph visually represents this piecewise function.
```

#### Another Example

- What are the transfer characteristics for this circuit if R,=1k and R,= 2k and the thresholds levels are +10 V.
	- Vm = i(R1 + R2) + vg V = iR1 = in = " in = " = R1" = R1
	R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 = R1 vi = Vin -V = Vin -V = Vin - Lin - Yo R1 - R1 - R1 - R1 - R2 - R1 - R2 - R1 - R2 v; = Vin - - in - - in - - - Vin + - -For vg = + 10 V, v; > 0 v; = = V;n + = > 0; = V; > = = = ; V; > = 5 For v == 10 V, v; < 0 v; = = Vm + = = 0; = Vm < = = = = = Vm < 5

Here is the image describtion:
```
The image consists of two parts: an electronic circuit diagram at the top and a graph at the bottom.

### Circuit Diagram:
1. **Components:**
   - **Operational Amplifier (Op-Amp):** The op-amp is depicted as a triangle with a positive (+) and negative (-) input terminal. The positive terminal is connected to the ground.
   - **Resistors:** There are two resistors, \( R_1 \) and \( R_2 \).
   - **Voltage Source:** There is an AC voltage source labeled \( v_{in} \).

2. **Connections:**
   - The AC voltage source \( v_{in} \) is connected to one end of resistor \( R_1 \).
   - The other end of \( R_1 \) is connected to the inverting input (-) of the op-amp and also to one end of resistor \( R_2 \).
   - The other end of \( R_2 \) is connected to the output \( v_o \) of the op-amp.
   - The non-inverting input (+) of the op-amp is connected to the ground.
   - The output \( v_o \) is shown as a black dot.

3. **Current Flow:**
   - The current \( i \) flows through \( R_1 \) and \( R_2 \).

### Graph:
1. **Axes:**
   - The horizontal axis represents the input voltage \( v_i \).
   - The vertical axis represents the output voltage \( v_o \).

2. **Scale:**
   - The horizontal axis is marked at -5 and +5.
   - The vertical axis is marked at -10 and +10.

3. **Plot:**
   - The graph shows a piecewise linear relationship between \( v_i \) and \( v_o \).
   - For \( v_i \) values less than -5, \( v_o \) is at -10.
   - For \( v_i \) values between -5 and +5, \( v_o \) changes linearly with \( v_i \).
   - For \( v_i \) values greater than +5, \( v_o \) is at +10.

4. **Arrows:**
   - There are arrows indicating the direction of the plot.
   - The plot starts at (-5, -10), moves vertically up to (-5, +10), then horizontally to (+5, +10), and finally vertically down to (+5, -10).

### Summary:
The circuit diagram represents an op-amp configuration with feedback resistors \( R_1 \) and \( R_2 \). The graph below it shows the output voltage \( v_o \) as a function of the input voltage \( v_i \), indicating a piecewise linear relationship with saturation limits at -10 and +10 volts.
```

### Astable Multivibrators

- A switching oscillator or Astable Multivibrator can be formed from a Schmitt trigger as follows:
- Assume that output levels are ±A and the thresholds are ±A/2 since the feedback voltage = ½ *vo*.

Here is the image describtion:
```
The image consists of two main parts: a mathematical analysis on the left and an electronic circuit diagram on the right.

### Left Side: Mathematical Analysis
1. **Equations and Conditions:**
   - The first equation is \( v_i = v_t - v_{in} \).
   - It states that when \( v_i > 0 \), the output voltage \( v_o = A \). Therefore, \( v_i = v_t - v_{in} > 0 \).
   - This implies \( v_t > v_{in} \) or \( v_{in} < \frac{A}{2} \).

2. **Graph:**
   - A graph is shown with \( v_{in} \) on the x-axis and \( v_o \) on the y-axis.
   - The graph is a hysteresis loop with two horizontal lines at \( v_o = A \) and \( v_o = -A \).
   - The vertical lines intersect the x-axis at \( v_{in} = \frac{A}{2} \) and \( v_{in} = -\frac{A}{2} \).

3. **Further Equations and Conditions:**
   - The second equation is again \( v_i = v_t - v_{in} \).
   - It states that when \( v_i < 0 \), the output voltage \( v_o = -A \). Therefore, \( v_i = v_t - v_{in} < 0 \).
   - This implies \( v_t < v_{in} \) or \( v_{in} > -\frac{A}{2} \).

### Right Side: Electronic Circuit Diagram
1. **Components:**
   - The circuit includes an operational amplifier (op-amp) represented by a triangle with a positive (+) and negative (-) input.
   - A capacitor \( C \) is connected to the inverting input (-) of the op-amp.
   - A resistor \( R \) is connected in series with the capacitor \( C \).
   - The non-inverting input (+) of the op-amp is connected to ground.
   - The output voltage \( v_o \) is taken from the output of the op-amp.
   - There is a feedback loop from the output of the op-amp to the inverting input (-) through a resistor \( R_f \).
   - Another resistor \( R_f \) is connected from the inverting input (-) to ground.

2. **Connections:**
   - The input voltage \( v_{in} \) is applied at the junction between the capacitor \( C \) and the resistor \( R \).
   - The output voltage \( v_o \) is connected back to the inverting input (-) through the feedback resistor \( R_f \).

### Summary
The image illustrates the behavior of a comparator circuit with hysteresis, showing the conditions under which the output voltage \( v_o \) switches between \( A \) and \( -A \) based on the input voltage \( v_{in} \). The circuit diagram on the right represents a typical configuration for such a comparator, with feedback resistors and a capacitor to introduce hysteresis.
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
The image depicts a transfer characteristic curve of a nonlinear device, likely a comparator or a Schmitt trigger. The graph is plotted with the input voltage \( V_{in} \) on the horizontal axis and the output voltage \( V_o \) on the vertical axis.

Key features of the graph include:

1. **Axes and Labels**:
   - The horizontal axis is labeled \( V_{in} \).
   - The vertical axis is labeled \( V_o \).

2. **Voltage Levels**:
   - The output voltage \( V_o \) can take on two distinct values: \( A \) and \( -A \).
   - The input voltage \( V_{in} \) has two critical points at \( -A/2 \) and \( A/2 \).

3. **Behavior of the Curve**:
   - For \( V_{in} \) less than \( -A/2 \), the output voltage \( V_o \) is at \( -A \).
   - As \( V_{in} \) increases and crosses \( -A/2 \), the output voltage \( V_o \) jumps to \( A \).
   - The output remains at \( A \) until \( V_{in} \) exceeds \( A/2 \), at which point the output voltage \( V_o \) drops back to \( -A \).

4. **Hysteresis**:
   - The graph shows a hysteresis loop, indicating that the output voltage depends not only on the current input voltage but also on the previous state of the input voltage.
   - This is evident from the fact that the transition from \( -A \) to \( A \) occurs at \( -A/2 \) and the transition from \( A \) to \( -A \) occurs at \( A/2 \).

5. **Red Dot**:
   - There is a red dot at the point where \( V_{in} = 0 \) and \( V_o = A \), highlighting a specific operating point on the graph.

Overall, the image represents a typical hysteresis curve for a device like a Schmitt trigger, which is used to provide noise immunity and a clean digital output from a noisy input signal.
```

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) in a specific configuration. Here is a detailed description of the components and their connections:

1. **Operational Amplifier (Op-Amp)**:
   - The op-amp is represented by a triangular symbol with the apex pointing to the right.
   - The inverting input (marked with a minus sign, -) is at the top left of the triangle.
   - The non-inverting input (marked with a plus sign, +) is at the bottom left of the triangle.
   - The output is at the right side of the triangle.

2. **Resistors**:
   - There are three resistors in the circuit, labeled as \( R \) and \( R_f \).
   - One resistor \( R \) is connected between the inverting input of the op-amp and a node that connects to a capacitor \( C \) and the output of the op-amp.
   - Two resistors \( R_f \) are connected in series between the output of the op-amp and the non-inverting input. The junction between these two resistors is connected to the ground.

3. **Capacitor**:
   - A capacitor \( C \) is connected between the node that connects to the resistor \( R \) and the ground.

4. **Voltage Sources**:
   - The input voltage \( v_i \) is applied across the capacitor \( C \).
   - The output voltage \( v_o \) is taken from the output of the op-amp.

5. **Ground Connections**:
   - The non-inverting input of the op-amp is connected to the ground through the two series resistors \( R_f \).
   - The capacitor \( C \) is connected to the ground on one side.
   - The output voltage \( v_o \) is referenced to the ground.

In summary, the circuit appears to be a type of active filter or integrator using an operational amplifier, resistors, and a capacitor. The configuration suggests that the op-amp is used to process the input signal \( v_i \) and produce an output signal \( v_o \) based on the values of the resistors and the capacitor.
```

Here is the image describtion:
```
The image shows a graphical representation of two waveforms: a sinusoidal wave and a square wave. 

1. **Sinusoidal Wave (Black Curve)**:
   - The sinusoidal wave is a smooth, continuous wave that oscillates above and below the horizontal axis.
   - It has a peak amplitude of +A and a trough amplitude of -A.
   - The wave crosses the horizontal axis at regular intervals, indicating zero amplitude at those points.
   - The wave reaches its maximum positive amplitude (+A) and maximum negative amplitude (-A) symmetrically around the horizontal axis.
   - The wave also passes through points at +A/2 and -A/2, which are marked by dotted horizontal lines.

2. **Square Wave (Orange Curve)**:
   - The square wave alternates between two levels: +A and -A.
   - It has a sharp transition between these two levels, creating a rectangular shape.
   - The square wave remains at +A for a certain period, then abruptly drops to -A, stays there for an equal period, and then jumps back to +A.
   - This pattern repeats periodically.
   - The transitions of the square wave align with the zero-crossings and peaks of the sinusoidal wave.

3. **Axes and Labels**:
   - The vertical axis represents the amplitude of the waves, with labels at +A, +A/2, -A/2, and -A.
   - The horizontal axis represents time, though it is not explicitly labeled.
   - The dotted horizontal lines at +A/2 and -A/2 help to indicate the intermediate amplitude levels of the sinusoidal wave.

Overall, the image illustrates the relationship between a sinusoidal wave and a square wave, showing how the square wave can be seen as a simplified, binary version of the sinusoidal wave, switching between its maximum and minimum values.
```

## Timing Calculation

Here is the image describtion:
```
The image depicts a comparison between a square wave and a sine wave. Here are the detailed observations:

1. **Square Wave**:
   - The square wave alternates between two levels: +A and -A.
   - The wave maintains the +A level for half of its period (T/2) and then switches to the -A level for the remaining half of the period (T/2).
   - The transitions between +A and -A are instantaneous, creating a sharp, rectangular shape.

2. **Sine Wave**:
   - The sine wave smoothly oscillates between +A and -A.
   - It reaches its maximum value of +A and minimum value of -A gradually, following a sinusoidal pattern.
   - The sine wave crosses the zero level at the midpoint of each half-period (T/2).

3. **Amplitude**:
   - Both waves have the same amplitude, denoted as A.
   - The amplitude levels are marked on the vertical axis as +A, +A/2, -A/2, and -A.

4. **Period (T)**:
   - The period of the waves is denoted by T, which is the time it takes for one complete cycle of the wave to occur.
   - The period is indicated by a horizontal arrow spanning one complete cycle of the square wave.

5. **Waveform Comparison**:
   - The square wave is shown as a series of horizontal lines at +A and -A with vertical transitions between these levels.
   - The sine wave is shown as a smooth, continuous curve that oscillates between +A and -A.

6. **Horizontal and Vertical Axes**:
   - The horizontal axis represents time.
   - The vertical axis represents the amplitude of the waves.

In summary, the image illustrates the differences in shape and behavior between a square wave and a sine wave, both having the same amplitude and period.
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