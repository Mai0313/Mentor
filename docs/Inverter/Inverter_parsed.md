# **CHAPTER 2**

# **SINGLE PHASE PULSE WIDTH MODULATED INVERTERS**

# **2.1 Introduction**

The dc-ac converter, also known as the inverter, converts dc power to ac power at desired output voltage and frequency. The dc power input to the inverter is obtained from an existing power supply network or from a rotating alternator through a rectifier or a battery, fuel cell, photovoltaic array or magneto hydrodynamic generator. The filter capacitor across the input terminals of the inverter provides a constant dc link voltage. The inverter therefore is an adjustable-frequency voltage source. The configuration of ac to dc converter and dc to ac inverter is called a dclink converter.

 Inverters can be broadly classified into two types, voltage source and current source inverters. A voltage–fed inverter (VFI) or more generally a voltage–source inverter (VSI) is one in which the dc source has small or negligible impedance. The voltage at the input terminals is constant. A current–source inverter (CSI) is fed with adjustable current from the dc source of high impedance that is from a constant dc source.

 A voltage source inverter employing thyristors as switches, some type of forced commutation is required, while the VSIs made up of using GTOs, power transistors, power MOSFETs or IGBTs, self commutation with base or gate drive signals for their controlled turn-on and turn-off.

 A standard single-phase voltage or current source inverter can be in the halfbridge or full-bridge configuration. The single-phase units can be joined to have three-phase or multiphase topologies. Some industrial applications of inverters are for adjustable-speed ac drives, induction heating, standby aircraft power supplies, UPS (uninterruptible power supplies) for computers, HVDC transmission lines, etc.

 In this chapter single-phase inverters and their operating principles are analyzed in detail. The concept of Pulse Width Modulation (PWM) for inverters is described with analyses extended to different kinds of PWM strategies. Finally the simulation results for a single-phase inverter using the PWM strategies described are presented.

## **2.2 Voltage Control in Single - Phase Inverters**

 The schematic of inverter system is as shown in Figure 2.1, in which the battery or rectifier provides the dc supply to the inverter. The inverter is used to control the fundamental voltage magnitude and the frequency of the ac output voltage. AC loads may require constant or adjustable voltage at their input terminals, when such loads are fed by inverters, it is essential that the output voltage of the inverters is so controlled as to fulfill the requirement of the loads. For example if the inverter supplies power to a magnetic circuit, such as a induction motor, the voltage to frequency ratio at the inverter output terminals must be kept constant. This avoids saturation in the magnetic circuit of the device fed by the inverter.

Here is the image describtion:
```
The image depicts a block diagram of a power conversion system. The system consists of three main components arranged in series:

1. **Battery or Rectifier**: This is the first component on the left side of the diagram. It serves as the source of DC power. The battery provides a steady DC voltage, while a rectifier converts AC voltage to DC voltage.

2. **Capacitor (Cd)**: Positioned in the middle of the diagram, this capacitor is labeled with the symbol "Cd" and has a voltage across it denoted as "Vd". The capacitor is used to smooth out the DC voltage, reducing any ripples or fluctuations that may be present.

3. **Inverter**: This is the third component, located to the right of the capacitor. The inverter converts the smoothed DC voltage into AC voltage. The output of the inverter is connected to the AC voltage terminals, which are represented by two lines extending to the right.

The overall function of this system is to convert DC voltage from a battery or rectifier into AC voltage, which can then be used to power AC devices. The capacitor plays a crucial role in ensuring that the DC voltage supplied to the inverter is stable and free of significant ripples.
```

Figure 2.1: Schematic for Inverter System

The various methods for the control of output voltage of inverters can be classified as:

- (a) External control of ac output voltage
- (b) External control of dc input voltage
	- (c ) Internal control of the inverter.

The first two methods require the use of peripheral components whereas the third method requires no external components. Mostly the internal control of the inverters is dealt, and so the third method of control is discussed in great detail in the following section.

# **2.2.1 Pulse Width Modulation Control**

The fundamental magnitude of the output voltage from an inverter can be controlled to be constant by exercising control within the inverter itself that is no external control circuitry is required. The most efficient method of doing this is by Pulse Width Modulation (PWM) control used within the inverter. In this scheme the inverter is fed by a fixed input voltage and a controlled ac voltage is obtained by

adjusting the on and the off periods of the inverter components. The advantages of the PWM control scheme are [10]:

- a) The output voltage control can be obtained without addition of any external components.
- b) PWM minimizes the lower order harmonics, while the higher order harmonics can be eliminated using a filter.

The disadvantage possessed by this scheme is that the switching devices used in the inverter are expensive as they must possess low turn on and turn off times, nevertheless PWM operated are very popular in all industrial equipments. PWM techniques are characterized by constant amplitude pulses with different duty cycles for each period. The width of these pulses are modulated to obtain inverter output voltage control and to reduce its harmonic content. There are different PWM techniques which essentially differ in the harmonic content of their respective output voltages, thus the choice of a particular PWM technique depends on the permissible harmonic content in the inverter output voltage.

# 2.2.2 **Sinusoidal-Pulse Width Modulation (SPWM)**

 The sinusoidal PWM (SPWM) method also known as the triangulation, sub harmonic, or suboscillation method, is very popular in industrial applications and is extensively reviewed in the literature [1-2]. The SPWM is explained with reference to Figure 2.2, which is the half-bridge circuit topology for a single-phase inverter.

Here is the image describtion:
```
The image depicts a simplified schematic of a half-bridge inverter circuit. Here is a detailed description of the components and their configuration:

1. **DC Voltage Source (Vd)**: On the left side of the circuit, there is a DC voltage source labeled \( V_d \). This source provides the input voltage for the inverter.

2. **Capacitors (C)**: The circuit includes two capacitors, each labeled \( C \). These capacitors are connected in series across the DC voltage source \( V_d \). The midpoint between the two capacitors is at half the voltage of the source, \( \frac{V_d}{2} \).

3. **Switches (S11 and S12)**: There are two switches, labeled \( S_{11} \) and \( S_{12} \), which are typically implemented using transistors (such as MOSFETs or IGBTs). Each switch has an associated anti-parallel diode, which is a common feature in power electronic circuits to handle reverse current.

4. **Output Voltage (Vo)**: The output voltage \( V_o \) is taken from the midpoint between the two switches. This point is connected to the load (not shown in the diagram).

5. **Connections**:
   - The positive terminal of the DC voltage source \( V_d \) is connected to the top terminal of the first capacitor and the drain of the upper switch \( S_{11} \).
   - The negative terminal of the DC voltage source \( V_d \) is connected to the bottom terminal of the second capacitor and the source of the lower switch \( S_{12} \).
   - The midpoint between the two capacitors is connected to the source of the upper switch \( S_{11} \) and the drain of the lower switch \( S_{12} \).

6. **Operation**: 
   - When \( S_{11} \) is closed (conducting) and \( S_{12} \) is open (non-conducting), the output voltage \( V_o \) is approximately \( +\frac{V_d}{2} \).
   - When \( S_{11} \) is open (non-conducting) and \( S_{12} \) is closed (conducting), the output voltage \( V_o \) is approximately \( -\frac{V_d}{2} \).
   - By switching \( S_{11} \) and \( S_{12} \) on and off alternately, an AC output voltage can be generated from the DC input voltage.

This half-bridge inverter is a fundamental building block in power electronics, used in applications such as motor drives, uninterruptible power supplies (UPS), and renewable energy systems.
```

Figure 2.2: Schematic diagram for Half-Bridge PWM inverter.

 For realizing SPWM, a high-frequency triangular carrier wave is compared with a sinusoidal reference of the desired frequency. The intersection of and waves determines the switching instants and commutation of the modulated pulse. The PWM scheme is illustrated in Figure 2.3 a, in which *v* is the peak value of triangular carrier wave and *v* that of the reference, or modulating signal. The figure shows the triangle and modulation signal with some arbitrary frequency and magnitude. In the inverter of Figure 2.2 the switches and are controlled based on the comparison of control signal and the triangular wave which are mixed in a comparator. When sinusoidal wave has magnitude higher than the triangular wave the comparator output is high, otherwise it is low. *c v r v <sup>c</sup> v <sup>r</sup> v c* 12 *r* <sup>11</sup> *S S*

$$\mathbf{v}\_r \ge \mathbf{v}\_c \qquad \text{S}\_{11} \text{ is on } , \quad \mathbf{V}\_{out} = \frac{\mathbf{V}\_d}{\mathbf{2}} \tag{2.1}$$

and

$$\nu\_r \le \nu\_c \qquad S\_{12} \text{ is on } , \quad V\_{out} = -\frac{V\_d}{2} \tag{2.2}$$

Here is the image describtion:
```
The image consists of two subplots labeled (a) and (b), which appear to be related to a pulse-width modulation (PWM) process.

**Subplot (a):**
- The x-axis is labeled "Time (sec)" and ranges from 0 to 2 milliseconds (2 x 10^-3 seconds).
- The y-axis is labeled "Modulation Signal and Triangle" and ranges from -1 to 1.
- There are two waveforms plotted:
  - A triangular waveform (Vr) that oscillates between -1 and 1 with a high frequency.
  - A sinusoidal waveform (Vc) that oscillates between -1 and 1 with a lower frequency.
- The triangular waveform intersects the sinusoidal waveform at various points.

**Subplot (b):**
- The x-axis is labeled "Time (sec)" and ranges from 0 to 2 milliseconds (2 x 10^-3 seconds).
- The y-axis is labeled "Pulse Amplitude" and ranges from -0.2 to 1.2.
- The plot shows a series of rectangular pulses (PWM signal) with amplitude values of either 0 or 1.
- The width of the pulses varies, corresponding to the points where the triangular waveform intersects the sinusoidal waveform in subplot (a).

Overall, the image illustrates the process of generating a PWM signal by comparing a sinusoidal modulation signal with a high-frequency triangular carrier signal. The resulting PWM signal in subplot (b) has pulse widths that vary according to the amplitude of the sinusoidal modulation signal in subplot (a).
```

Figure 2.3: SPWM illustration (a) Sine-Triangle Comparison (b) Switching Pulses after comparison.

 The comparator output is processesed in a trigger pulse generator in such a manner that the output voltage wave of the inverter has a pulse width in agreement with the comparator output pulse width. The magnitude ratio of *c r v <sup>v</sup>* is called the modulation index ( ) and it controls the harmonic content of the output voltage waveform. The magnitude of fundamental component of output voltage is proportional to . The amplitude of the triangular wave is generally kept constant. The frequency–modulation ratio is defined as *mi mi <sup>c</sup> v mf*

$$m\_f = \frac{f\_t}{f\_m} \tag{2.3}$$

To satisfy the Kirchoff's Voltage law (KVL) constraint, the switches on the same leg are not turned on at the same time, which gives the condition

$$\mathbf{S}\_{11} + \mathbf{S}\_{12} = 1 \tag{2.4}$$

for each leg of the inverter. This enables the output voltage to fluctuate between 2 *Vd* and 2 *Vd* <sup>−</sup> as shown in Figure 2.4 for a dc voltage of 200 V.

Here is the image describtion:
```
The image is a plot of voltage versus time. The x-axis represents time in seconds, ranging from 0 to 2 milliseconds (2 x 10^-3 seconds). The y-axis represents voltage in volts, ranging from -100 V to 100 V. The plot shows a square wave signal, which alternates between 100 V and -100 V at regular intervals. The waveform has a high level at 100 V and a low level at -100 V, with sharp transitions between these levels. The signal appears to have a consistent period, indicating a regular and repeating pattern. The plot is drawn with a thick black line, making the waveform clearly visible against the grid background.
```

Figure 2.4: Output voltage of the Half-Bridge inverter.

#### **2.3 Single-Phase Inverters**

 A single-phase inverter in the full bridge topology is as shown in Figure 2.5, which consists of four switching devices, two of them on each leg. The fullbridge inverter can produce an output power twice that of the half-bridge inverter with the same input voltage. Three different PWM switching schemes are discussed in this section, which improve the characteristics of the inverter. The objective is to add a zero sequence voltage to the modulation signals in such a way to ensure the clamping of the devices to either the positive or negative dc rail; in the process of which the voltage gain is improved, leading to an increased load fundamental voltage, reduction in total current distortion and increased load power factor. In Figure 2.5, the top devices are assigned to be S11 and S21 while the bottom devices as S12 and S22, the voltage equations for this converter are as given in the following equations.

Here is the image describtion:
```
The image depicts a schematic diagram of a single-phase full-bridge inverter circuit. The key components and their arrangement are as follows:

1. **DC Voltage Source (Vd)**: On the left side of the diagram, there is a DC voltage source labeled \( V_d \). The positive terminal is at the top, and the negative terminal is at the bottom.

2. **Capacitors (C)**: The DC voltage source is connected to two capacitors, each labeled \( C \). These capacitors are connected in series, with the midpoint labeled as \( o \). The voltage across each capacitor is \( \frac{V_d}{2} \).

3. **Switches (S11, S12, S21, S22)**: There are four switches in the circuit, each represented by a transistor symbol with an anti-parallel diode. The switches are labeled \( S_{11} \), \( S_{12} \), \( S_{21} \), and \( S_{22} \).

   - **S11 and S12**: These switches are connected to the midpoint \( o \) and the positive terminal of the DC source. \( S_{11} \) is connected to point \( a \), and \( S_{12} \) is connected to the negative terminal of the DC source.
   - **S21 and S22**: These switches are connected to the midpoint \( o \) and the negative terminal of the DC source. \( S_{21} \) is connected to point \( a \), and \( S_{22} \) is connected to the positive terminal of the DC source.

4. **Output Terminals (a and b)**: The points \( a \) and \( b \) are the output terminals of the inverter. The voltage across these terminals is labeled \( V_{ab} \).

5. **Diodes**: Each switch has an anti-parallel diode, which allows current to flow in the opposite direction when the switch is off. These diodes are essential for handling the inductive loads and ensuring proper operation of the inverter.

The overall function of this circuit is to convert the DC voltage \( V_d \) into an AC voltage \( V_{ab} \) by appropriately switching the transistors \( S_{11} \), \( S_{12} \), \( S_{21} \), and \( S_{22} \). The switching sequence determines the polarity and magnitude of the output AC voltage.
```

Figure 2.5: Schematic of a Single Phase Full-Bridge Inverter.

$$\frac{V\_d}{2}(S\_{11} - S\_{12}) = V\_{an} + V\_{no} = V\_{ao} \tag{2.5}$$

$$\frac{V\_d}{2}(S\_{21} - S\_{22}) = V\_{bn} + V\_{no} = V\_{bo} \tag{2.6}$$

$$V\_{ab} = V\_{an} - V\_{bn} \tag{2.7}$$

 The voltages and *V* are the output voltages from phases A and B to an arbitrary point n, *V* is the neutral voltage between point n and the mid-point of the DC source. The switching function of the devices can be approximated by the Fourier series to be equal to *Van bn no* (1<sup>+</sup> *<sup>M</sup>* ) <sup>2</sup> 1 where M is the modulation signal which when compared with the triangular waveform yields the switching pulses [19]. Thus from Equations 2.4, 2.5, and 2.6, the expressions for the modulation signals are obtained as

$$M\_{11} = \frac{\Im(V\_{\text{an}} + V\_{\text{no}})}{V\_d} \tag{2.8}$$

$$M\_{21} = \frac{\mathbf{2}(V\_{hn} + V\_{no})}{V\_d}.\tag{2.9}$$

Equations 2.8 and 2.9 give the general expression for the modulation signals for single-phase dc-ac converters. The various types of modulation schemes presented in the literature can be obtained from these equations using appropriate definition for , *V* and *V* . Making use of this concept different modulation schemes have been proposed some of which are explained in detail in the following sections. *Van bn no*

#### **2.3.1 SPWM With Bipolar Switching**

 In this scheme the diagonally opposite transistors S11, S22 and S21 and S12 are turned on or turned off at the same time. The output of leg A is equal and opposite to the output of leg B. The output voltage is determined by comparing the control signal, and the triangular signal, *V* as shown in Figure 2.6(a) to get the switching pulses for the devices , and the switching pattern is as follows. *Vr <sup>c</sup>*

$$V\_r > V\_c \quad , \quad \text{S}\_{11} \text{ is on } \implies V\_{ao} = \frac{Vd}{2} \text{ and } \text{S}\_{22} \text{ is on } \implies V\_{bo} = -\frac{Vd}{2}; \tag{2.10}$$

$$V\_r \le V\_c \quad , \quad \text{S}\_{12} \text{ is on } \implies V\_{ao} = -\frac{Vd}{2} \text{ and } \text{S}\_{21} \text{ is on } \implies V\_{ho} = \frac{Vd}{2}; \tag{2.11}$$

hence

$$V\_{bo}(t) = -V\_{ao}(t) \tag{2.12}$$

Here is the image describtion:
```
The image consists of three subplots labeled (a), (b), and (c), each displaying a different waveform over a time period of 0 to 0.02 seconds.

1. **Subplot (a):**
   - The y-axis is labeled "Sine-triangle."
   - The plot shows a combination of a sine wave and a triangle wave. The sine wave is a smooth, continuous curve that oscillates between -1 and 1. Superimposed on this sine wave is a high-frequency triangle wave, which creates a jagged, sawtooth-like pattern on top of the sine wave. The sine wave appears to have a lower frequency compared to the triangle wave.

2. **Subplot (b):**
   - The y-axis is labeled "S11/S22."
   - This plot displays a series of vertical lines that alternate between 0 and 1. The pattern is highly regular, with each line reaching either the maximum value of 1 or the minimum value of 0. The lines are closely spaced, indicating a high-frequency signal.

3. **Subplot (c):**
   - The y-axis is labeled "S12/S21."
   - Similar to subplot (b), this plot also shows a series of vertical lines alternating between 0 and 1. The pattern is again highly regular and closely spaced, indicating another high-frequency signal. The frequency and spacing of the lines appear to be similar to those in subplot (b).

All three subplots share the same x-axis labeled "Time (sec)," which ranges from 0 to 0.02 seconds. The time intervals are marked at 0.005, 0.01, and 0.015 seconds. The overall appearance suggests that the plots are likely representing different aspects or components of a signal or system over a very short time period.
```

Figure 2.6:Bipolar PWM (a) Sine-triangle comparison (b) Switching pulses for S11/S22 (c) Switching pulses for S12/S21

Here is the image describtion:
```
The image consists of three subplots, each displaying a different waveform over a short period of time (from 0.04 to 0.08 seconds). Here is a detailed description of each subplot:

1. **Top Subplot (a)**:
   - **Y-axis Label**: "modulation signal (mi sin(wet))"
   - **X-axis Label**: "Time (sec)"
   - **Waveform**: This plot shows a sinusoidal waveform that oscillates between -1 and 1. The waveform completes approximately one full cycle within the given time frame. The signal appears smooth and continuous, representing a typical modulation signal.

2. **Middle Subplot (b)**:
   - **Y-axis Label**: "Vab (V)"
   - **X-axis Label**: "Time (sec)"
   - **Waveform**: This plot displays a high-frequency switching signal, which is characteristic of a Pulse Width Modulation (PWM) signal. The waveform rapidly switches between approximately +100V and -100V. The density of the switching indicates a high-frequency operation, and the pattern of the switching appears to be modulated by the signal from the top subplot.

3. **Bottom Subplot (c)**:
   - **Y-axis Label**: "Load current (A)"
   - **X-axis Label**: "Time (sec)"
   - **Waveform**: This plot shows another sinusoidal waveform, similar in shape to the modulation signal in the top subplot. The amplitude of this waveform oscillates between -2A and 2A. This waveform represents the load current, which is smooth and continuous, indicating that the PWM signal has been filtered to produce a sinusoidal current.

Overall, the image illustrates the process of generating a sinusoidal load current using a modulation signal and a PWM signal. The modulation signal (a) is used to control the PWM signal (b), which in turn produces a filtered load current (c) that closely follows the shape of the modulation signal.
```

Figure 2.7: Bipolar PWM scheme (a) Modulation signal for leg 'a' (b) output line-line voltage (c) load current

The line-to-line voltage is given as in Equation 2.13.

$$V\_{ab}(t) = V\_{ao}(t) - V\_{bo}(t) = \mathcal{2}V\_{ao}(t) \tag{2.13}$$

The peak of the fundamental-frequency component in the output voltage is given as

$$V\_{ab} = m\_i V\_d \tag{2.14}$$

and

[10]

$$V\_d < V\_{ab} < \frac{4}{\pi} V\_d \qquad \qquad (m\_i \ge 1.0). \tag{2.15}$$

Since the voltage switches between two levels −*Vd* and *V* , the scheme is called the Bipolar PWM. The relationship between fundamental input and output voltage in the overmodulating region is given as [10]. *d*

$$V\_o = MV\_d \tag{2.16}$$

where

$$M = \frac{2m\_i}{\pi} (\sin^{-1}\alpha + \alpha\sqrt{1-\alpha^2}) \qquad \qquad , m\_i > 1$$

*mi* α=1/ .

For a full-bridge inverter with bipolar PWM scheme the output voltage is between

2 *Vd* <sup>−</sup> and 2 *Vd* . Figure 2.7 shows the modulation signal, output voltage, and the load current for bipolar modulation scheme on a single-phase inverter with an RL load of 10 Ω and 0.125H.

For the bipolar PWM switching scheme there is only one modulation signal and the switches are turned 'on' or turned 'off' according to the pattern given in Equations 2.10 and 2.11. The input dc voltage was 200 V and the modulation index (mi) was taken to be 0.8. The switching frequency for the carrier, which is the triangle, is 10 kHz.

#### **2.3.2 SPWM With Unipolar Switching**

In this scheme, the devices in one leg are turned on or off based on the comparison of the modulation signal *V* with a high frequency triangular wave. The devices in the other leg are turned on or off by the comparison of the modulation signal with the same high frequency triangular wave. Figure 2.8 and 2.9 show the unipolar scheme for a single –phase full bridge inverter, with the modulation signals for both legs and the associated comparison to yield switching pulses for both the legs. *r* −*Vr*

 In Figure 2.8 the simulation results show the sine triangle comparison, the switching pulses for S11 and S21 are shown. The switching for the other two devices is obtained as S12 = 1 – S11 and S22 = 1- S21. Figure 2.9 shows the phase voltages , lineto-line voltages obtained from a unipolar PWM scheme , also shown is the load current. The simulation was carried out for an RL load of R = 10Ω and L = 0.125H. The dc voltage is 200 V and the switching frequency is 10kHz. The modulation signal has a magnitude of 0.8, i.e mi = 0.8.

Here is the image describtion:
```
The image consists of three subplots labeled (a), (b), and (c), each displaying a different waveform or signal over a specific time interval from 0.04 seconds to 0.06 seconds.

(a) The first subplot, labeled "sine-trianglecomparison," shows two waveforms overlaid on each other. The thicker waveform appears to be a sine wave, characterized by its smooth, continuous oscillations between -1 and 1. The thinner waveform is a triangle wave, which has a linear rise and fall, creating a series of sharp peaks and troughs. The sine wave and triangle wave are compared over the same time interval, demonstrating their different shapes and periodicities.

(b) The second subplot, labeled "S11," displays a series of vertical lines that form a pattern resembling a pulse train or a square wave. The signal alternates between 0 and 1, with each pulse having a consistent width and spacing. This pattern is repeated over the entire time interval from 0.04 seconds to 0.06 seconds.

(c) The third subplot, labeled "S21," also shows a series of vertical lines similar to the second subplot. This signal also alternates between 0 and 1, forming a pulse train or square wave pattern. The pulses in this subplot appear to have a different width or spacing compared to the pulses in subplot (b), indicating a different frequency or duty cycle.

All three subplots share the same x-axis labeled "Time (sec)," indicating the time in seconds, and the y-axis labels vary according to the specific signal being displayed. The y-axis for subplot (a) is labeled "sine-trianglecomparison," while the y-axes for subplots (b) and (c) are labeled "S11" and "S21," respectively. The overall image provides a visual comparison of different types of waveforms and signals over a short time interval.
```

Figure 2.8: Unipolar PWM voltage switching scheme (a) Sine triangle comparison (b) switching pulses for S11 (c) switching pulses for S21.

Here is the image describtion:
```
The image consists of four subplots labeled (a), (b), (c), and (d), each displaying a different electrical signal over time. The x-axis of each subplot represents time in seconds, ranging from 0.04 to 0.06 seconds for the first three subplots and from 0.04 to 0.08 seconds for the fourth subplot. 

- Subplot (a) is labeled "Van (V)" on the y-axis and shows a high-frequency oscillating signal with a peak-to-peak voltage of approximately 200 V.
- Subplot (b) is labeled "Vbn (V)" on the y-axis and also displays a high-frequency oscillating signal similar to subplot (a), with the same peak-to-peak voltage of approximately 200 V.
- Subplot (c) is labeled "Vab (V)" on the y-axis and shows a signal that appears to be a combination of the signals in subplots (a) and (b). The signal has a peak-to-peak voltage of approximately 400 V and exhibits a pattern that changes around 0.05 seconds.
- Subplot (d) is labeled "Iab (A)" on the y-axis and displays a sinusoidal current signal with a peak current of approximately 5 A. The signal is smooth and continuous, unlike the high-frequency oscillations seen in the voltage signals of the previous subplots.

Overall, the image presents a detailed view of voltage and current waveforms in an electrical system, with the voltage signals showing high-frequency oscillations and the current signal displaying a sinusoidal pattern.
```

Figure 2.9: Unipolar PWM voltage switching scheme (a) phase voltage 'a' (b) phase voltage 'b' (c) line to line voltage Vab (d) load current

 The logic behind the switching of the devices in the leg connected to 'a' is given as

$$\begin{array}{rcl} V\_r > V\_c & : S\_{\text{ll}} \text{ is on and } V\_{\text{an}} = \frac{V\_d}{2} \end{array} \tag{2.17}$$

$$V\_r \le V\_c \quad \text{: } S\_{11} \text{ is on and } V\_{av} = -\frac{V\_d}{2} \tag{2.18}$$

and that in the leg connected to 'b' is given as

$$-V\_r \ge V\_c \quad \text{: } S\_{11} \text{ is on and } V\_{hn} = \frac{V\_d}{2} \tag{2.19}$$

$$-V\_r \le V\_c \; : \; S\_{11} \; \text{is} \; \text{on} \; \text{and} \; \; V\_{ln} = -\frac{V\_d}{2} \tag{2.20}$$

 Table 2.1 shows the switching state of the unipolar PWM and the corresponding voltage levels. It can be observed from the table that when the two top or the two bottom devices are turned on the output voltage is zero.

 In Unipolar switching scheme the output voltage level changes between either 0 to -*V* or from 0 to +*V* . This scheme 'effectively' has the effect of doubling the switching frequency as far as the output harmonics are concerned, compared to the bipolar- switching scheme. The voltage waveforms *V* and are 180o out of phase from each other as seen in Figure 2.10. The output voltage *V* is as shown in Figure 2.11 along with the load current. *d d an Vbn ab*

 Since the harmonic components at the switching frequency in and have the same frequency, this results in the cancellation of the harmonic component at the switching frequency in the output voltage. *Van Vbn*

| 11 S | 12 S | 21 S | 22 S | VAn | VBn | Vo<br>=VAn<br>−VBn |
|------|------|------|------|-----|-----|--------------------|
|      |      |      |      |     |     |                    |
| ON   | -    | -    | ON   | Vd  | 0   | Vd                 |
|      |      |      |      |     |     |                    |
| -    | ON   | ON   | -    | 0   | Vd  | -Vd                |
|      |      |      |      |     |     |                    |
| ON   | -    | ON   | -    | Vd  | Vd  | 0                  |
|      |      |      |      |     |     |                    |
| -    | ON   | -    | ON   | 0   | 0   | 0                  |
|      |      |      |      |     |     |                    |

Table 2.1. Switching state of the unipolar PWM and the corresponding voltage levels.

The fundamental component of the output voltage is given as

$$V\_o = m\_i V\_d \tag{2.21}$$

$$V\_d < V\_o < \frac{4}{\pi} V\_d \qquad \qquad (m\_i > 1.0). \tag{2.22}$$

#### **2.3.3 SPWM With Modified Bipolar Switching Scheme (MBPWM)[14]**

In the inverter employing the bipolar switching scheme, switches are operated in such a way that during the positive half of the modulation signal one of the top devices in one of the switching leg is kept on and the two other switching devices in the other leg are PWM operated, and during the negative half of the modulation signal one of the bottom switching device is kept on continuously while the other two switching devices in the other leg are PWM operated. The output voltage is determined by comparing the control signal and the triangular wave. Vr The switching pattern along with the sine-triangle comparison is as shown in Figure 2.10. The switching pattern for positive values of modulating signal *V* is as given *<sup>m</sup>*

 *V* > *V* , is on (2.23) *<sup>r</sup> <sup>c</sup>* <sup>21</sup> *S* and *V* <*V* , is on . *<sup>r</sup> <sup>c</sup>* <sup>22</sup> *S* (a) (b) (c)

Here is the image describtion:
```
The image consists of two subplots, labeled (d) and (e), which display time-domain signals. Both subplots have a similar layout and style, with the x-axis representing time in seconds (sec) and the y-axis representing the signal amplitude.

1. **Subplot (d):**
   - The y-axis is labeled "S21."
   - The x-axis ranges from 0.04 to 0.05 seconds.
   - The signal appears to be a square wave oscillating between 0 and 1.
   - The waveform has a high frequency, with multiple cycles occurring within the 0.01-second time window shown.

2. **Subplot (e):**
   - The y-axis is labeled "S22."
   - The x-axis also ranges from 0.04 to 0.05 seconds.
   - Similar to subplot (d), the signal is a square wave oscillating between 0 and 1.
   - The frequency of the waveform in subplot (e) appears to be slightly higher than that in subplot (d), as there are more cycles within the same time window.

Both subplots are likely part of a larger analysis or study, given their similar formatting and the specific time window chosen for display. The signals are likely related to each other, possibly representing different channels or measurements in a time-domain analysis.
```

Figure 2.10: Modified bipolar PWM (a) Sine-triangle comparison (b), (c), (d), and (e) switching pulses for devices S11, S12, S21 and S22.

Here is the image describtion:
```
The image consists of two graphs, labeled (a) and (b), which are plotted against time on the x-axis, ranging from 0.04 to 0.08 seconds.

Graph (a) is a plot of voltage (Vab) in volts (V) versus time (sec). The y-axis ranges from -100 V to 100 V. The voltage waveform appears to be a high-frequency square wave, alternating between approximately +100 V and -100 V. The waveform shows distinct periods of high and low states, with rapid transitions between these states.

Graph (b) is a plot of current (Iab) in amperes (A) versus time (sec). The y-axis ranges from -2 A to 2 A. The current waveform is a smooth sinusoidal wave, starting at -2 A at 0.04 seconds, peaking at around +2 A at approximately 0.055 seconds, and then returning to -2 A by 0.08 seconds. The sinusoidal wave completes one full cycle within the given time frame.

Overall, the image shows a high-frequency square voltage waveform and a corresponding sinusoidal current waveform over the same time period.
```

Figure 2.11: Modified bipolar PWM scheme (a) line-to-line voltage (b) load current The switching pattern for negative values of the modulating signal *V* is given as *<sup>m</sup>*

*V* < *V* , is on (2.24) *<sup>r</sup> <sup>c</sup>* <sup>21</sup> *S*

and *V* > *V* , is on . *<sup>r</sup> <sup>c</sup>* <sup>22</sup> *S*

 The output voltage is given as *V* (*t*) *V* (*t*) *V* (*t*) *<sup>o</sup>* = *An* − *Bn* , as shown in Figure 2.11. The load current is also shown in the same plot. The RL load has an R = 10 Ω and L = 0.125H. The modulation signal for the sine-triangle comparison is 0.8. The switching pattern for the Modified Bipolar Switching Scheme is as given in Table 2.2.

| 11 S | 12 S | 21 S | 22 S | VAn | VBn | =VAn<br>−VBn<br>Vo |  |  |
|------|------|------|------|-----|-----|--------------------|--|--|
| ON   | -    | -    | ON   | Vd  | 0   | Vd                 |  |  |
| -    | ON   | ON   | -    | 0   | Vd  | -Vd                |  |  |
| ON   | -    | ON   | -    | Vd  | Vd  | 0                  |  |  |
| -    | ON   | -    | ON   | 0   | 0   | 0                  |  |  |

Table 2.2. Switching state of the modified bipolar PWM and the corresponding voltage.

From Table 2.2 it can be observed that when the two top or the two bottom devices are turned on the output voltage is zero.

 In the modified bipolar switching scheme the output voltage level changes between either 0 to -*V* or from 0 to +*V* . Since the sign of the modulation signal decides the switching pattern the analysis of this switching scheme is complex. The relationship between input and output voltage is given as [14], *d d*

$$V\_o = mV\_d$$

$$\text{(2.2S)}$$

where ) <sup>4</sup> 0.5( π *m* = *mi* + ( *mi* <1.0 ) . (2.26)

Thus from the above equation it can be observed that the fundamental component of the voltage as obtained from the MBPWM is the maximum when compared to the other switching schemes even in the linear modulation region; that is when the modulation index is less than unity.

#### **2.3.4 Generalized Carrier-based PWM**

In the inverter shown in Figure 2.5, the output voltage and the input current are given as

$$0.05V\_d \left(S\_{11} - S\_{12}\right) = V\_{ao} = V\_{an} + V\_{no} \tag{2.27}$$

$$0.0 \, S V\_d (S\_{21} - S\_{22}) = V\_{ho} = V\_{ho} + V\_{no} \tag{2.28}$$

$$I\_d = I\_a \left( S\_{11} - S\_{21} \right) \tag{2.29}$$

$$V\_{ab} = V\_{an} - V\_{bn} \,. \tag{2.30}$$

The voltages *V* and *V* are the output voltages from phases 'a' and 'b' to a arbitrary point while *V* is the neutral voltage between the point 'n' and the mid-point of the DC source. The generalized carrier-based PWM scheme is obtained by defining the quantity using the concept of q-d Space Vector representation. A special q-d reference frame transformation to transform the two phase voltages to orthogonal q-d voltage components is defined as *an no bn Vno*

$$V\_q = 0.5(V\_{an} + V\_{bn})\tag{2.31}$$

$$V\_d = 0.5(V\_{an} - V\_{bn})\tag{2.32}$$

where and are the q-axis and the d-axis voltages in an orthogonal coordinate system. The q-d voltages for each of the possible switching instant are shown in Table 2.3. *Vq Vd*

| 11 S | 21 S | Vao            | Vbo            | Vq                    | Vd             |
|------|------|----------------|----------------|-----------------------|----------------|
| -    | -    | −<br>0.<br>5Vd | −<br>0.<br>5Vd | −<br>0<br>5Vd<br>−Vno | 0              |
| -    | ON   | −<br>0.<br>5Vd | 0<br>5Vd       | −Vno                  | −<br>0.<br>5Vd |
| ON   | -    | 0<br>5Vd       | −<br>0.<br>5Vd | −Vno                  | 0<br>5Vd       |
| ON   | ON   | 0<br>5Vd       | 0<br>5Vd       | 0.<br>5Vd<br>−Vno     | 0              |

Table 2.3. Switching state of the generalized carrier based PWM scheme.

 Figure 2.12 also shows the space vector representation of the output phase voltages. To synthesize a given reference output voltage *V* or equivalently *V* , the four vectors shown in the figure are averaged over one switching period for the inverter *ab* \* *qd*

$$\left(V\_{qd}\right)^{\*} = \mathbf{t}\_a V\_{qda} + \mathbf{t}\_b V\_{qdb} + \mathbf{t}\_c V\_{qdc} + \mathbf{t}\_d V\_{qdd} \tag{2.33}$$

where are the normalized times for which the averaging vector spent in each of the four quadrants. The normalized times should satisfy the condition that . The normalized times *t* can be expressed as some equivalent time t *<sup>a</sup> <sup>b</sup> <sup>c</sup> <sup>d</sup> t* ,*t* ,*t* ,*t ta* + *tb* +*tc* + *td* =1 *<sup>c</sup> <sup>d</sup>* , *t* o such that

$$t\_c + t\_d = t\_o \tag{2.34}$$

or equivalently *t* can be written as *t <sup>c</sup> <sup>d</sup>* ,*t <sup>c</sup> <sup>o</sup>* =γ*t* which implies *td <sup>o</sup>* =(1− γ )*t* , γ ∈[0 1] so Equation 2.33 can be written as

$$\left(V\_{qd}\right)^{\*} = \mathbf{t}\_a V\_{qda} + \mathbf{t}\_b V\_{qdb} + \mathbf{\mathcal{H}}\_o V\_{qdc} + (1 - \mathbf{\mathcal{y}}) \mathbf{t}\_o V\_{qdd} \tag{2.35}$$

Here is the image describtion:
```
The image is a diagram featuring a set of coordinate axes with vectors labeled at each of the four cardinal directions. The diagram appears to be related to a mathematical or engineering context, possibly involving vector analysis or control systems.

1. **Axes**:
   - The diagram has a central origin point with two perpendicular axes intersecting at this point.
   - The horizontal axis extends to the left and right, while the vertical axis extends upwards and downwards.

2. **Vectors and Labels**:
   - **Top Vector**: 
     - Positioned along the positive vertical axis.
     - Labeled as \(\left[\frac{V_d}{2} - V_{no}, 0\right] = f_{qda}\).
   - **Right Vector**: 
     - Positioned along the positive horizontal axis.
     - Labeled as \(\left[-V_{no}, \frac{V_d}{2}\right] = f_{qdc}\).
   - **Bottom Vector**: 
     - Positioned along the negative vertical axis.
     - Labeled as \(\left[-V_{no}, -\frac{V_d}{2}\right] = f_{qdb}\).
   - **Left Vector**: 
     - Positioned along the negative horizontal axis.
     - Labeled as \(\left[-V_{no}, -\frac{V_d}{2}\right] = f_{qdd}\).

3. **Additional Vector**:
   - There is an additional vector labeled \(f_{qd}^*\) that is not aligned with the primary axes.
   - This vector is positioned in the first quadrant, indicating a direction that is both positive in the horizontal and vertical components.

4. **Arrows**:
   - Each vector is represented by an arrow pointing away from the origin in the direction specified by the coordinates.

5. **Coordinate Notation**:
   - The coordinates for each vector are given in square brackets, indicating the components along the horizontal and vertical axes respectively.

6. **Subscripts and Variables**:
   - The variables \(V_d\) and \(V_{no}\) are used in the coordinates, suggesting they are parameters or constants relevant to the context of the diagram.
   - The subscripts \(qda\), \(qdc\), \(qdb\), and \(qdd\) are used to differentiate between the different vectors.

Overall, the diagram is a clear representation of vectors in a two-dimensional plane, with specific labels and coordinates indicating their direction and magnitude relative to the origin.
```

Figure 2.12: Space vector representation of the voltages in a single-phase inverter.

 The time is the actual time which the vector spends in the null state that is when either both the top or both the bottom devices are off or on at the same time. This time is split in to two time periods such that *ot ta* +*tb* +*to* =1; let *t* then *<sup>a</sup> <sup>b</sup> <sup>x</sup>* +*t* = *t <sup>a</sup> <sup>x</sup> t* = ξ *t* and so *<sup>b</sup> <sup>x</sup> t* = (1−ξ )*t* , where ξ∈[0,1]and γ ∈[0,1]. The quantities *t* re the normalized times (with respect to the switching period of the converter). Solving Equation 2.33 we can get the expression for the zero sequence voltage *V* in terms of other known quantities as *<sup>a</sup> <sup>b</sup> <sup>o</sup> t* ,*t no* , a

$$W\_{no} = 0.5V\_d(2\gamma - 1) - \frac{-V\_q \stackrel{\*}{V}\_d(2\tilde{\xi} - 1)}{V\_d(2\tilde{\xi} - 1) - 2V\_d} \tag{2.34}$$

Equations 2.8, 2.9, along with 2.34 constitute the generalized discontinuous PWM scheme for the single-phase inverter. An infinite number of possibilities for the discontinuous PWM exist depending on the choice of ξ and γ.

#### **2.4 Bipolar and Modified Bipolar PWM Schemes with Zero Sequence Voltage**

In the PWM modulation scheme with bipolar voltage switching, the diagonally opposite switching devices are switched as switch pairs resulting in an output voltage switching between -*V* and . The zero sequence voltage expression for the bipolar schemes is given as, *<sup>d</sup> Vd* =0.5 (2γ −1) *Vno Vd* as the q-axis voltage is zero (refer Equations 2.31 and 2.32). If γ is so chosen so as to locate the zero sequence voltage to be centered about the peak of the modulation signal, we can achieve higher fundamental component of the load voltage and less switching because the effect of the zero sequence is to increase the modulation signal to more than unity. In which case the comparison of the triangle and the modulation signal would yield continuous 'on' or 'off' of the switching device for a long period of time as when compared to the regular sine triangle comparison.

# **2.5 Implementation of the Bipolar and the Modified bipolar PWM Schemes for an RL load**

The single-phase inverter in the full-bridge topology has been simulated in Matlab/Simulink for a RL load with R = 10Ω and L = 0.05 H. The modulation signals (for a modulation index of 0.8) for the switching devices have been obtained from the TMSLF2407, Texas Instruments DSP. Figure 2.13 shows the simulation result of bipolar PWM with the zero-sequence voltage while without the zero sequence was already shown in Figures 2.8 and 2.9. The simulation results for the modified bipolar PWM scheme with the zero-sequence voltage are as shown in Figures 2.14. In the

Here is the image describtion:
```
The image consists of five subplots labeled (a) through (e), each displaying a different signal over a time interval from 0.04 to 0.06 seconds. Here is a detailed description of each subplot:

(a) The first subplot shows a modulation signal. The signal varies between approximately -2 and 2 units. It starts at around 1.5, decreases to -2, then increases to 2, and finally decreases again towards 0. The signal has a smooth, continuous waveform with some sharp transitions.

(b) The second subplot displays the signals S11 and S22 over time. These signals are binary, alternating between 0 and 1. The transitions between 0 and 1 are very frequent, indicating a high-frequency switching pattern. The pattern changes slightly around 0.05 seconds.

(c) The third subplot shows the signals S12 and S21 over time. Similar to subplot (b), these signals are also binary and alternate between 0 and 1 with high frequency. The switching pattern is slightly different from that in subplot (b) and also changes around 0.05 seconds.

(d) The fourth subplot presents the voltage Vab in volts (V). The voltage alternates between approximately -100V and 100V, indicating a high-frequency switching pattern similar to the signals in subplots (b) and (c). The pattern changes around 0.05 seconds.

(e) The fifth subplot shows the current Iab in amperes (A). The current waveform is a smooth sinusoidal signal, varying between approximately -5A and 5A. The sinusoidal nature of the current indicates a continuous and periodic signal.

Overall, the image depicts various electrical signals, including modulation, binary switching signals, voltage, and current, over a short time interval. The binary signals and voltage exhibit high-frequency switching, while the modulation signal and current have smoother waveforms.
```

simulation the dc voltage was assumed to be 200 V and the modulation index to be 0.8.

Figure 2.13: Bipolar PWM scheme (a) modulation signal (b) &(c) switching pulses S11/S22 and S21/S12 respectively.

Here is the image describtion:
```
The image consists of seven subplots labeled (a) through (g), each displaying a different signal or waveform over a time interval from 0.04 seconds to 0.06 seconds. Here is a detailed description of each subplot:

(a) Modulation Signal:
- The first subplot shows a modulation signal that varies between approximately -1 and 2. The signal has a non-linear, piecewise shape with distinct segments that include both smooth curves and sharp transitions.

(b) S11 Signal:
- The second subplot displays a binary signal labeled S11. This signal alternates between 0 and 1. It starts at 1, drops to 0 at around 0.045 seconds, rises back to 1 at around 0.05 seconds, and drops to 0 again at around 0.055 seconds.

(c) S12 Signal:
- The third subplot shows another binary signal labeled S12. This signal also alternates between 0 and 1. It starts at 0, rises to 1 at around 0.045 seconds, drops back to 0 at around 0.055 seconds.

(d) S21 Signal:
- The fourth subplot presents a high-frequency binary signal labeled S21. This signal rapidly switches between 0 and 1, creating a series of vertical lines. The signal has periods of high-frequency switching interspersed with periods where it remains at 0.

(e) S22 Signal:
- The fifth subplot shows another high-frequency binary signal labeled S22, similar to S21. It also rapidly switches between 0 and 1, with periods of high-frequency switching and periods where it remains at 0.

(f) Vab (Voltage) Signal:
- The sixth subplot displays a voltage signal labeled Vab (V). This signal oscillates between approximately -100 V and 100 V. The waveform consists of high-frequency oscillations with distinct segments where the voltage remains constant for short periods.

(g) Iab (Current) Signal:
- The seventh subplot shows a current signal labeled Iab (A). This signal varies smoothly between approximately -3 A and 3 A, forming a sinusoidal waveform.

Overall, the image depicts various signals that are likely part of an electrical or electronic system, showing how different components or stages of the system behave over a short time interval.
```

Figure 2.14: Modified bipolar PWM scheme (a) modulation signal (b), (c), (d) & (e) switching pulses S11, S12, S21 and S22 (f) line-to-line voltage (g) load current.

# **2.6 Experimental Results**

The experimental results for the above schemes tested in simulation are presented in Figures 2.15, 2.16, 2.17, and 2.18 for both bipolar and the modified bipolar PWM strategy with and without the zero-sequence voltage. The RL –load has an R = 10Ω and L = 0.05H. Table 2.4 shows the comparison between the four modulation schemes.

Table2.4: Comparative experimental results for the various modulation schemes

| Modulation Scheme        | VRMS  | IRMS   | Vf    | If    | VTHD  | ITHD   | IPEAK | PF    |
|--------------------------|-------|--------|-------|-------|-------|--------|-------|-------|
|                          |       |        |       |       |       |        |       |       |
| Bipolar                  | 49.6  | 1.6965 | 48    | 1.694 | 25    | 1.87   | 2.479 | 0.407 |
|                          |       |        |       |       |       |        |       |       |
| Bipolar with Vno         | 56.34 | 1.948  | 55    | 1.949 | 21.8  | 1.25   | 2.769 | 0.407 |
|                          |       |        |       |       |       |        |       |       |
| ModifiedBipolar          | 62.5  | 2.158  | 59.97 | 2.148 | 30.79 | 10.507 | 3.228 | 0.397 |
|                          |       |        |       |       |       |        |       |       |
| ModifiedBipolar with Vno | 65.59 | 2.284  | 63.39 | 2.281 | 26.51 | 8.763  | 3.395 | 0.402 |

Here is the image describtion:
```
The image is a screenshot of an oscilloscope display, which shows three different waveforms on three separate channels. Here are the details:

1. **Channels and Waveforms:**
   - **Channel 1 (Ch1)**: Displayed in blue, with a vertical scale of 100 V per division. The waveform appears to be a noisy signal with a high amplitude, occupying the top portion of the screen.
   - **Channel 2 (Ch2)**: Displayed in green, with a vertical scale of 100 mV per division. This waveform is a sinusoidal signal with some noise, occupying the middle portion of the screen.
   - **Channel 3 (Ch3)**: Displayed in purple, with a vertical scale of 500 mV per division. This waveform is a clean sinusoidal signal, occupying the bottom portion of the screen.

2. **Time Scale:**
   - The horizontal time scale is set to 4.00 ms per division.

3. **Markers and Measurements:**
   - There are two vertical cursors (orange) on the screen, indicating a time difference of 160.000 µs between them.
   - The voltage level for Channel 1 is indicated as -328 V.

4. **Additional Information:**
   - The oscilloscope is in "Stop" mode, meaning it is not currently acquiring new data.
   - The date and time at the bottom right corner indicate "23 Oct 2002, 13:11:28."

5. **General Observations:**
   - The waveform on Channel 1 is significantly noisier compared to the other two channels.
   - Channel 2 shows a sinusoidal waveform with some noise superimposed on it.
   - Channel 3 shows a clean sinusoidal waveform with no visible noise.

The display provides a clear comparison of the three different signals being measured, with distinct characteristics for each channel.
```

Figure 2.15: Bipolar switching scheme, starting from top (1) the load voltage (2) the load current (3) modulation signal with mi = 0.8.

Here is the image describtion:
```
The image is a screenshot of an oscilloscope display showing three different waveforms on three channels. Here are the details:

1. **Channels and Waveforms**:
   - **Channel 1 (Ch1)**: Displayed in blue, with a vertical scale of 100 V per division. The waveform appears to be a square wave with a high amplitude, reaching up to approximately 330 V.
   - **Channel 2 (Ch2)**: Displayed in green, with a vertical scale of 100 mV per division. The waveform is a sinusoidal wave with a lower amplitude compared to Channel 1.
   - **Channel 3 (Ch3)**: Displayed in purple, with a vertical scale of 500 mV per division. The waveform is also sinusoidal but with a different phase and amplitude compared to Channel 2.

2. **Time Scale**:
   - The horizontal scale is set to 4.00 ms per division, indicating the time base for the waveforms.

3. **Cursors**:
   - There are two vertical cursors (T1 and T2) placed on the screen, with a time difference (ΔT) of 160.000 µs between them. This is used to measure the time interval between two points on the waveforms.

4. **Additional Information**:
   - The oscilloscope is a Tektronix model, as indicated by the "Tek" logo at the top left.
   - The date and time at the bottom right corner show "23 Oct 2002, 13:03:06".
   - The frequency of Channel 1 is indicated as 330 V, which seems to be a mislabeling or an error, as it should typically show frequency in Hz.

5. **Waveform Characteristics**:
   - The waveform on Channel 1 is a high-amplitude square wave.
   - The waveform on Channel 2 is a low-amplitude sinusoidal wave.
   - The waveform on Channel 3 is another sinusoidal wave with a different amplitude and phase compared to Channel 2.

Overall, the image shows a detailed view of three different electrical signals being analyzed simultaneously on an oscilloscope.
```

 Figure 2.16: Bipolar switching scheme with zero sequence voltage, (1) load voltage (2) the load current (3) modulation signal.

Here is the image describtion:
```
The image is a screenshot of an oscilloscope display, which shows multiple waveforms overlaid on a grid. The oscilloscope is a Tektronix model, as indicated by the "Tek" logo in the top left corner. The display is in a stopped state, as indicated by the "Stop" label next to the logo.

There are four channels displayed, each with different voltage scales and waveforms:

1. **Channel 1 (Ch1)**: This waveform is displayed in blue and has a voltage scale of 100 V per division. The waveform appears to be a distorted sine wave with significant noise or high-frequency components superimposed on it. The peak-to-peak voltage is quite high, as indicated by the scale.

2. **Channel 2 (Ch2)**: This waveform is displayed in green and has a voltage scale of 100 mV per division. The waveform is a cleaner sine wave compared to Channel 1, with less noise and a lower amplitude.

3. **Channel 3 (Ch3)**: This waveform is displayed in purple and has a voltage scale of 1.00 V per division. The waveform is a square wave with a duty cycle that appears to be around 50%. The transitions between high and low states are sharp, indicating a digital signal.

4. **Channel 4 (Ch4)**: This waveform is displayed in light green and has a voltage scale of 500 mV per division. The waveform is a smooth sine wave with a lower amplitude compared to Channel 1 and Channel 2.

The time base for the oscilloscope is set to 4.00 ms per division, as indicated at the bottom of the screen. The horizontal cursor (T) is set to 160.000 µs, which is displayed in orange at the bottom of the screen.

The date and time are displayed at the bottom right corner of the screen, showing "23 Oct 2002" and "13:37:28".

Overall, the image shows a complex set of waveforms with different characteristics, likely representing different signals in an electronic circuit or system.
```

 Figure 2.17: Modified bipolar switching scheme,(1) load voltage (2) load current (3) modulation signal for one leg (4) modulation signal for the other leg with mi= 0.8

Here is the image describtion:
```
The image is a screenshot of an oscilloscope display, which shows multiple waveforms overlaid on a grid. The oscilloscope is a Tektronix model, as indicated by the "Tek" logo in the top left corner. The display is divided into four channels, each represented by a different color and labeled as Ch1, Ch2, Ch3, and Ch4.

1. **Channel 1 (Ch1)**: 
   - Color: Blue
   - Scale: 100 V/div
   - The waveform is a high-frequency signal with a rectangular shape, indicating a series of pulses or a digital signal.

2. **Channel 2 (Ch2)**:
   - Color: Green
   - Scale: 100 mV/div
   - The waveform is a sinusoidal signal, which appears to be a clean sine wave.

3. **Channel 3 (Ch3)**:
   - Color: Purple
   - Scale: 1.00 V/div
   - The waveform is a square wave, characterized by its sharp transitions between high and low states.

4. **Channel 4 (Ch4)**:
   - Color: Light Green
   - Scale: 500 mV/div
   - The waveform is a triangular wave, with a linear rise and fall.

The time base for the oscilloscope is set to 4.00 ms/div, as indicated at the bottom center of the display. The horizontal axis represents time, while the vertical axis represents voltage for each channel.

There are also two vertical cursors (T and t) on the display, which are used to measure the time interval between two points on the waveforms. The time difference between these cursors is shown as 160.000 µs.

The date and time at the bottom right corner indicate that the screenshot was taken on 23 October 2002 at 13:30:12.

Overall, the image shows a combination of different types of waveforms (rectangular, sinusoidal, square, and triangular) being measured simultaneously on an oscilloscope.
```

 Figure 2.18: Modified bipolar switching scheme with zero sequence voltage (1) load voltage (2) load current (3) modulation signal for one leg (4) modulation signal for the other leg with mi = 0.8 and zero sequence added.

 Thus the discontinuous PWM modulation for the same reference output voltage gives higher rms voltages and currents, improved power factor, better voltage, and current total harmonic distortion factor, that is a low value for current and voltage THD.

 It would appear that the modified bipolar discontinuous PWM scheme is the best modulation method with the highest output voltage among all while the bipolar discontinuous PWM scheme gives the best performance in terms of current purity. It is concluded that the discontinuous PWM modulation methodology results in improved output voltage magnitude and high waveform fidelity in some cases while in others the current purity is enhanced when compared to the classical modulation schemes.

 One important realization by using the modulation schemes with the zerosequence voltages added is that the switching losses are reduced. The switching devices are PWM operated in which at every switching period instant the devices are turned 'on'or 'off'. The advantage of using PWM method for operating the switching devices is to reduce the output harmonics, but the cost to buy this advantage is paid off for the switching losses, but with the zero-sequence added the switching per device is reduced and hence the switching losses are reduced.