## Amplifiers

Here is the image describtion:
```
The image is a simple, rectangular graphic with a black background. At the top of the image, the word "Module" is written in white, sans-serif font. Below the word "Module," there is a large, bold, white number "4" centered in the image. The overall design is minimalistic and straightforward, with a clear focus on the text and number.
```

# Amplifier Circuits

## Introduction to Impedance and Bandwidth Control.

#### What you'll learn in Module 4.

Section 4.0 Introduction to Impedance and Bandwidth Control.

• Recognise the need for changing the shape of an amplifier's frequency response.

Section 4.1 Input Compensation.

• Describe typical input correction circuits.

Section 4.2 Amplifier Controls.

• Describe typical tone control circuits.

Section 4.3 Amplifiers and Impedance.

• Describe typical circuits for controlling impedance.

Section 4.4 NFB Quiz.

 • Test your knowledge & understanding of impedance and tone control in audio amplifiers.

#### Modified Response Curves

Previous modules have concentrated on producing a flat frequency response over the required audio frequency range. It is sometimes necessary however, to modify the flat response of an audio amplifier by making

Here is the image describtion:
```
The image shows a close-up view of two control knobs on an audio device, likely an amplifier or a stereo system. The knob on the left is labeled "BASS" and the one on the right is labeled "TREBLE." Both knobs have a circular design with numerical markings around their edges, ranging from -5 to +5, indicating the level of adjustment for bass and treble frequencies. The background of the image is slightly blurred, and there is a partial view of an electronic circuit diagram at the bottom, featuring a transistor symbol labeled "Tr1." The overall image combines elements of audio control and electronic circuitry.
```

Here is the image describtion:
```
The image shows a combination of an electronic circuit diagram and a close-up view of audio input/output connectors. 

In the upper part of the image, there is a schematic representation of a circuit involving two transistors labeled Tr1 and Tr2. The transistors are depicted with the standard symbol for bipolar junction transistors (BJTs), with the base, collector, and emitter terminals clearly marked. The circuit also includes other standard electronic symbols, such as a resistor and a capacitor, indicating a simple amplifier or switching circuit.

Below the circuit diagram, there is a close-up photograph of several RCA connectors, which are commonly used for audio and video signals. The connectors are arranged in two rows, with the top row having red and white color-coded rings, and the bottom row having yellow rings. These connectors are typically used for stereo audio (red and white) and composite video (yellow). The labels below the connectors indicate their functions, with "MIC" for microphone input, and other symbols that might represent different audio or video inputs/outputs.

The image effectively combines the theoretical aspect of electronics (the circuit diagram) with the practical application (the connectors), illustrating the connection between circuit design and real-world hardware.
```

particular stages of the amplifier frequency dependent. This can be achieved by modifying either the response of one or more of the amplifier stages, or the response of a negative feedback path.

Fig. 4.0.1 shows (shaded green) stages where such modification will take place, the remaining stages having a flat response curve.

#### Modifying Input and Output Impedance.

The importance of an amplifier's input and output impedance is discussed in AC Theory Module 7, and using NFB to control impedance is described in Amplifiers Module 3.2.

Module 4.3 describes some other amplifier circuits that are commonly used to control the values of input and output impedances in amplifier circuits.

Here is the image describtion:
```
The image is a block diagram illustrating the process of controlling the response curve of an audio amplifier. The diagram is labeled "Fig. 4.0.1 Controlling the Response Curve of an Audio Amplifier."

The diagram consists of several blocks connected in series, each representing a different stage in the audio amplification process. The stages are as follows:

1. **Input Select**: This block is highlighted in green and is the first stage. It has multiple input options listed on the left side, including CD, TAPE, RADIO, PICK UP, MIC, and AUX. These inputs feed into the Input Select block.

2. **Pre-amp**: The second block in the series, labeled "Pre-amp," is not highlighted. It receives the selected input from the Input Select block.

3. **Voltage amp**: The third block, labeled "Voltage amp," also not highlighted, follows the Pre-amp block.

4. **Tone control**: The fourth block, highlighted in green, is labeled "Tone control." It receives the signal from the Voltage amp block.

5. **Power amp**: The fifth and final block, labeled "Power amp," is not highlighted. It receives the signal from the Tone control block and outputs it to a speaker, represented by a speaker icon on the right side of the block.

The diagram visually represents the flow of an audio signal through various stages of amplification and control, starting from the selection of the input source to the final output through a speaker.
```

AMPLIFIERS MODULE 04.PDF 1 © E. COATES 2007 -2012

### Module 4.1 Amplifier Input Compensation

Here is the image describtion:
```
The image is divided into two main sections. On the left side, there is a text box titled "What you'll learn in Module 4.1." Below this title, the text outlines the learning objectives for the module. It states that after studying this section, you should be able to:

- Recognize the need for changing the shape of an amplifier’s frequency response.
- Understand the operation of typical circuits for:
  - Input Compensation.
  - Line Level.
  - Phono De-emphasis.

On the right side of the image, there are two visual elements. The top part shows a simplified schematic diagram of a pre-amplifier with three input connections labeled AUX, PU, and TAPE. The bottom part of the right side displays a close-up image of a panel with multiple RCA connectors. The connectors are color-coded with red and white, and they are labeled with different input sources such as MIC, D, QO, and CD. The overall image appears to be part of an educational material related to audio electronics and amplifier circuits.
```

#### Input Compensation

Pre amplifiers are designed to increase the signal voltage amplitude of input devices to a level suitable for the input to a power amplifier. Pre-amplifiers often need a number of different inputs, each with a different gain and/or different input impedance. This is to ensure that each device connected to the various inputs provides (after pre-amplification) an output level sufficient to drive the input of a power amplifier and provide full power (when full volume is used) and minimum noise.

#### Line Level

This pre amplifier output is usually called 'Line level' and most amplifiers will have a line in and a line out socket, on PC sound cards these are normally coloured pale green and light blue respectively. The actual line level measured in volts varies between different types of equipment but is around 1Vpp on consumer equipment to 2.5Vpp on professional equipment. With some input devices such as CDs or radio tuners, little or no pre-amplification is needed but devices such as microphones, phono inputs and guitar pickups provide much lower signal levels and need specially adapted inputs to the preamplifier.

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage pre-amplifier with input compensation. The diagram includes various electronic components and their connections, which are detailed as follows:

1. **Inputs**: There are three input options labeled AUX, RADIO, and PHONO. These inputs are selectable via a switch labeled SW1a.

2. **Transistors**: The circuit features two transistors, labeled Tr1 and Tr2, which are the active components in the amplification stages.

3. **Resistors**: Several resistors are present in the circuit, labeled R1 through R9. These resistors are used for biasing the transistors and setting the gain of the amplifier stages.

4. **Capacitors**: The circuit includes multiple capacitors, labeled C1 through C6. These capacitors are used for coupling, bypassing, and filtering purposes within the circuit.

5. **Switches**: There are two switches, SW1a and SW1b. SW1a is used to select the input source, while SW1b appears to be part of the input compensation network.

6. **Power Supply**: The circuit is powered by a voltage source labeled Vcc, with a common ground (0V) reference.

7. **Output**: The output of the pre-amplifier is labeled "Output to Tone Controls," indicating that the signal is further processed by tone control circuitry.

8. **Additional Components**: There is a capacitor labeled C3 with a positive sign, indicating it is an electrolytic capacitor used for decoupling or filtering.

The diagram is labeled "Fig. 4.1.1 Two Stage Pre-amp with Input Compensation," suggesting it is part of a larger document or textbook. The circuit is designed to amplify audio signals from different sources with input compensation to ensure consistent performance across various input types.
```

**Input Compensation** 

#### Phono Inputs

Inputs for phono cartridges used for playing legacy vinyl discs have an output of only a few millivolts and so need substantial amplification to reach line level. They also need the frequency response to be modified, due to the 'pre-emphasis' applied to these discs during recording.

Fig. 4.1.1 shows a two stage pre-amplifier circuit in which the negative feedback is applied via resistors selected by the input selector switch, allowing different gain levels to be set by choosing one of three resistors (R7, R8 or R9) which will form a potential divider with R3 to set the gain.

R9 (selected in the 'phono' position of SW1) also has capacitors connected in series and in parallel with it to form a frequency selective network. The phono input is designed to accept a low level input from a record pick up.

#### RIAA Pre-emphasis

Vinyl discs recorded to the RIAA (Recording Industry Association of America) standard have the high frequency end of their spectrum excessively amplified during the recording process and the lower frequencies reduced in amplitude. This has two main beneficial effects, firstly amplifying the higher frequencies gives a significant improvement in the signal to noise ratio. Vinyl discs are prone to surface noise in the form of a high frequency hiss; increasing the signal amplitude of the higher frequencies during recording makes the HF signal much louder than the hiss, then reducing the amplitude of the boosted high frequencies (the signal along with the hiss) back to a 'normal' level during playback, restores a level frequency response at the same time as reducing the hiss to a much lower level, greatly reducing the apparent surface noise.

A second advantage of reducing the amplitude of the lower frequencies during the recording of vinyl discs, is that it reduces the amount of side-to-side movement required by the groove-cutting stylus and so makes a narrower groove, this allows more information to be recorded on the same diameter disc.

The result of this pre-emphasis is the standard RIAA curve shown in Fig. 4.1.2. This curve governs the amount of pre-emphasis applied and so requires the amplifier to have a similar but opposite sloping 'de-emphasis' curve to produce a flat response.

Here is the image describtion:
```
The image is a graph that illustrates the frequency response curves associated with the RIAA (Recording Industry Association of America) equalization process used in vinyl record production and playback. The graph has a logarithmic frequency scale on the x-axis, ranging from 20 Hz to 20 kHz, and a decibel (dB) scale on the y-axis, ranging from -20 dB to +20 dB.

There are three curves depicted on the graph:

1. **RIAA Pre-emphasis during record (Green Curve)**: This curve shows the equalization applied during the recording process. It starts at +20 dB at 20 Hz and gradually decreases to -20 dB at 20 kHz. This pre-emphasis boosts the high frequencies and attenuates the low frequencies during recording.

2. **Pre-amplifier de-emphasis (Red Curve)**: This curve represents the equalization applied during playback by the pre-amplifier. It starts at -20 dB at 20 Hz and gradually increases to +20 dB at 20 kHz. This de-emphasis attenuates the high frequencies and boosts the low frequencies, effectively reversing the pre-emphasis applied during recording.

3. **Resultant response (Blue Line)**: This line represents the overall frequency response after both the pre-emphasis and de-emphasis have been applied. It is a flat line at 0 dB across the entire frequency range, indicating that the original frequency response of the audio signal is restored.

The graph visually demonstrates how the RIAA equalization process works to maintain the integrity of the audio signal from recording to playback.
```

**Fig. 4.1.2 RIAA Pre-Emphasis Curve** 

## Module 4.2 Amplifier Controls

What you'll learn in Module 4.2

**After studying this section, you should be able to:** 

Understand typical circuits used for tone control in audio amplifiers.

- Tone Control.
- Passive Bass Treble Control.
- Active Bass Treble Control.
- IC control of common amplifier functions.

Here is the image describtion:
```
The image shows a close-up view of two control knobs on an audio device, likely an amplifier or a stereo system. The knobs are labeled "BASS" and "TREBLE," indicating that they are used to adjust the bass and treble levels of the audio output.

The "BASS" knob is on the left side of the image. It is a circular knob with a metallic finish and a black face. The face of the knob has white markings and numbers ranging from -5 to +5, with 0 at the top center position, indicating the neutral setting. The numbers are evenly spaced around the circumference of the knob.

The "TREBLE" knob is on the right side of the image and is similar in design to the "BASS" knob. It also has a metallic finish with a black face and white markings. The numbers on the "TREBLE" knob also range from -5 to +5, with 0 at the top center position.

Both knobs are mounted on a metallic panel, which has a brushed metal texture. The labels "BASS" and "TREBLE" are printed in black above each respective knob. The overall design suggests a high-quality, possibly vintage, audio device.
```

#### Tone Control

Tone Control, shown in its most basic form in Fig. 4.2.1 provides a simple means of regulating the amount of higher frequencies present in the output signal fed to the loudspeakers. a simple method of achieving this is to place a variable CR network between the voltage amplifier and the power amplifier stages, The value of C1 is chosen to pass the higher audio frequencies, this has the effect of progressively reducing the higher frequencies as the variable resistor slider is adjusted towards the bottom end of the tone control, The minimum level of attenuation of the higher (treble) frequencies is limited by R1, which prevents C1 being connected directly to ground. As the circuit only reduces the high frequency content of the signal it could be called a simple Treble Cut control. The use of these simple circuits is normally restricted to guitar applications or inexpensive radios.

Here is the image describtion:
```
The image depicts a simple electronic circuit diagram, specifically a tone control circuit. Here is a detailed description of the components and their arrangement:

1. **Capacitor (C1)**: The circuit includes a capacitor labeled C1. It is positioned vertically and connected at the top to a horizontal line that represents the input signal. The other end of the capacitor is connected to a resistor.

2. **Resistor (R1)**: Below the capacitor, there is a resistor labeled R1. This resistor is also positioned vertically. The top end of the resistor is connected to the capacitor, and the bottom end is connected to a horizontal line that represents the output signal.

3. **Potentiometer (Tone Control)**: There is a potentiometer connected in parallel with the resistor R1. The wiper (adjustable middle terminal) of the potentiometer is connected to the output line, allowing for adjustment of the tone by varying the resistance.

4. **Input and Output**: The circuit has an input on the left side, connected to the top horizontal line, and an output on the right side, connected to the bottom horizontal line. The input and output lines are connected through the capacitor and resistor/potentiometer combination.

5. **Ground**: The bottom horizontal line is connected to the ground, providing a reference point for the circuit.

The overall function of this circuit is to control the tone of an audio signal by adjusting the potentiometer, which changes the frequency response of the circuit.
```

Here is the image describtion:
```
The image shows a text label that reads "Fig. 4.2.1 Simple Tone Control." This label likely refers to a figure in a document or book, specifically figure number 4.2.1, which is titled "Simple Tone Control." The text is in a bold, black font, and it appears to be a heading or caption for an accompanying diagram or illustration related to tone control in an audio or electronic context.
```

 In hi-fi amplifiers, tone control refers to the boosting or reduction of particular audio frequencies. This may be done to suit the preferences of the listener, not everyone perceives sound in exactly the same way, for example the frequency response of the human ear changes with age. The room or hall in which the sound is reproduced will also affect the nature of the sound. Many techniques are used to alter the sound, and in particular the frequency response of the amplifiers producing the sound. These range from simple RC filters, through passive and active frequency control networks to complex digital signal processing.

#### The Baxandall Tone Control Circuit

The circuit discussed here is an example of the Baxandall tone control circuit, illustrated in Fig. 4.2.2, which is an analogue circuit providing independent control of bass and treble frequencies; both bass and treble can be boosted or cut and with both controls at their mid positions, provides a relatively flat frequency response, as illustrated by the blue 'Level response' graph line in Fig. 4.2.5. The original design, proposed by P. J. Baxandall in 1952, used a valve (tube) amplifier and feedback as part of the circuit to reduce the

Here is the image describtion:
```
The image depicts a schematic diagram of a Baxandall Tone Control Circuit, which is used in audio applications to adjust the bass and treble frequencies. The circuit includes the following components and connections:

1. **Input and Output**: 
   - The input is on the left side of the circuit.
   - The output is on the right side of the circuit.

2. **Resistors**:
   - R1: 10K ohms, connected between the input and the junction of C1 and VR1.
   - R2: 1K ohms, connected between the junction of C2 and ground.
   - R3: 10K ohms, connected between the junction of C1 and C2 and the junction of C3 and VR2.

3. **Capacitors**:
   - C1: 22nF, connected between the junction of R1 and VR1 and the junction of R3 and C2.
   - C2: 220nF, connected between the junction of VR1 and R2 and the junction of R3 and C1.
   - C3: 2.2nF, connected between the junction of R3 and VR2 and the output.
   - C4: 22nF, connected between the junction of VR2 and ground.

4. **Variable Resistors (Potentiometers)**:
   - VR1: 100K ohms, labeled as "Bass," connected between the junction of C1 and C2 and ground.
   - VR2: 100K ohms, labeled as "Treble," connected between the junction of C3 and C4 and ground.

5. **Ground**:
   - The circuit has a ground connection at the bottom, labeled as "Gnd."

The circuit is designed to allow the user to adjust the bass and treble frequencies of an audio signal by varying the resistance of VR1 and VR2, respectively. The capacitors and resistors work together to filter and shape the frequency response of the audio signal.
```

considerable attenuation (about −20dB) introduced by the passive network, and to provide true bass and treble boost. There are still many variants of the circuit in use, both as active circuits (with amplification as originally proposed), and as passive networks without an incorporated amplifier. In passive variants of the Baxandall circuit, extra stages of amplification may be used to make up for the approximately −20bB attenuation caused by the circuit.

Read the original 1952 paper "Negative-Feedback Tone Control" by P. J. Baxandall B.Sc.(Eng.) published in "Wireless World" (Now Electronics World)

#### How the Baxandall Circuit Works.

With bass and treble controls set to maximum boost (both wipers at the top of resistors VR1 and VR2), and the inactive components greyed out, the circuit will look like Fig. 4.2.3. Both bass and treble potentiometers that may have either linear or logarithmic tracks depending on the circuit design, are much higher values than other components in the circuit, and so with the VR1 and VR2 wipers set to maximum resistance both potentiometers can be considered to be open circuit. Nor does C4

Here is the image describtion:
```
The image depicts an electronic circuit diagram for a bass and treble boost. The circuit includes various resistors, capacitors, and variable resistors (potentiometers) to adjust the bass and treble levels.

Here is a detailed description of the components and their connections:

1. **Input and Output:**
   - The circuit has an input terminal on the left and an output terminal on the right.

2. **Resistors:**
   - R1: 10K ohms, connected between the input and a junction point.
   - R2: 1K ohms, connected between a junction point and ground (Gnd).
   - R3: 10K ohms, connected between a junction point and another junction point leading to the output.

3. **Capacitors:**
   - C1: 22nF (nanofarads), connected in parallel with VR1 (variable resistor for bass).
   - C2: 220nF, connected in series with R2.
   - C3: 2.2nF, connected in parallel with VR2 (variable resistor for treble).
   - C4: 22nF, connected in series with VR2.

4. **Variable Resistors (Potentiometers):**
   - VR1: 100K ohms, labeled as "Bass," connected in parallel with C1.
   - VR2: 100K ohms, labeled as "Treble," connected in parallel with C3 and in series with C4.

5. **Ground (Gnd):**
   - The circuit has a ground connection at the bottom, which is connected to the negative terminal of the power supply.

6. **Power Supply:**
   - The circuit is powered by a 0V (ground) connection on both sides.

The circuit is designed to allow the user to adjust the bass and treble levels of an audio signal by varying the resistance of VR1 and VR2. The capacitors and resistors work together to filter and boost specific frequency ranges, enhancing the overall sound quality.
```

**Fig. 4.2.3 Maximum Bass & Treble Boost**

contribute to the operation of the circuit because of the high resistance of VR2, and C1 is effectively shorted out by the wiper of VR1 being at the top end of its resistance track.

The full bandwidth of signal frequencies is applied to the input from an amplifier having low output impedance, and the higher frequency components of the signal are fed directly to the output of the tone control circuit via the 2.2nF capacitor C3, which has a reactance of about 3.6KΩ at 20kHz but over 3.6MΩ at 20Hz, so blocks the lower frequencies.

The full band of frequencies also appear at the junction of R1 and C2, which together form a low pass filter with a corner frequency of around 70 to 75 Hz and so frequencies appreciably higher than this (the mid and high frequencies) are conducted to ground via R2.

Having R2 in series with C2 prevents the attenuation of the mid band frequencies exceeding about - 20dB. The lower frequencies are fed to the output via R3. Because R3 has quite a large value (to effectively isolate the effects of the two variable controls from each other, the input impedance (Zin) of the circuit following the tone control must be very high to avoid excessive signal loss due to the potential divider effect of R3 and the Zin of the following stage.

#### Bass and Treble Cut.

With the bass and treble controls both set to maximum cut (Fig. 4.2.4), the full bandwidth signal passes through R1 but with the slider of VR1 at the bottom end of its resistance track, C1/R2 now form a high pass filter having a corner frequency of around 7 to 7.5kHz so only frequencies appreciably higher than this are allowed to pass un-attenuated. The mid and higher frequencies are therefore fed to R3 and C4, which now form a low pass filter to progressively attenuate frequencies above about 70 Hz, the mid-band frequencies (about 600Hz) are reduced by approximately −20dB, and at 20kHz by as much as −43dB, as can be seen from the response curve in Fig 4.2.5.

Notice that although the circuit provides what is called bass boost and treble boost, with the passive version of the Baxandall circuit (with no amplification), all frequencies are in fact reduced.

The attenuation of the circuit at mid-band is typically around −20dB and with full 'boost' applied at either the low or high end of the bandwidth, attenuation at these frequencies would be around −1 to −3dB.

#### Active Baxandall Circuit

To overcome the substantial losses in the passive version of this circuit, which give a level response (with both controls at mid way setting) but at -20dB below the input voltage, it is common to incorporate an amplifier in the designs. Nowadays an op-amp would be a reasonable choice, with the Baxandall network forming a negative feedback loop to give the required gain figures over the necessary bandwidth. Various designs are possible with different values for resistors R1 to R4 and C1 to C4 in the network, depending to some extent on the output impedance of the previous, and input impedance of the following circuits.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a tone control circuit. Here is a detailed description of the components and their connections:

1. **Input and Output:**
   - The circuit has an input terminal on the left side and an output terminal on the right side.

2. **Resistors:**
   - R1: 10K ohms, connected between the input and a node that connects to C1 and R3.
   - R2: 1K ohms, connected between a node that connects to C2 and the ground (Gnd).
   - R3: 10K ohms, connected between the node that connects to C1 and the output.

3. **Capacitors:**
   - C1: 22nF (nanofarads), connected between the node that connects to R1 and R3, and another node that connects to C2 and R2.
   - C2: 220nF, connected between the node that connects to C1 and R2, and the ground.
   - C3: 2.2nF, connected between the output and a node that connects to VR2.
   - C4: 22nF, connected between the node that connects to C3 and VR2, and the ground.

4. **Variable Resistors (Potentiometers):**
   - VR1: 100K ohms, labeled as "Bass," connected in parallel with the input and the node that connects to C1 and R3.
   - VR2: 100K ohms, labeled as "Treble," connected in parallel with the output and the node that connects to C3 and C4.

5. **Ground (Gnd):**
   - The ground is represented by a symbol with three horizontal lines, and it is connected to the bottom of the circuit, providing a common return path for electric current.

6. **Voltage:**
   - The circuit operates with a 0V reference at both the input and output sides.

The circuit is designed to adjust the bass and treble frequencies of an audio signal, with VR1 controlling the bass and VR2 controlling the treble. The capacitors and resistors form filters that shape the frequency response of the signal passing through the circuit.
```

**Fig. 4.2.4 The Circuit with VR1 and VR2 at Minimum**

Here is the image describtion:
```
The image is a graph that illustrates the frequency response of an audio system, showing how different frequencies are attenuated or boosted. The x-axis represents the frequency in Hertz (Hz), ranging from 10 Hz to 20,000 Hz (20K Hz). The y-axis represents attenuation in decibels (dB), ranging from -50 dB to 0 dB.

There are four curves on the graph, each representing a different type of frequency adjustment:

1. **Bass Boost (Red Curve)**: This curve starts at 0 dB at low frequencies (around 10 Hz) and gradually decreases to -20 dB as the frequency increases, indicating a boost in bass frequencies.

2. **Treble Boost (Red Curve)**: This curve starts at -20 dB at low frequencies and gradually increases to 0 dB at high frequencies (around 20K Hz), indicating a boost in treble frequencies.

3. **Level Response (Blue Curve)**: This curve remains relatively flat at around -20 dB across all frequencies, indicating a neutral or flat response without any boost or cut.

4. **Bass Cut (Green Curve)**: This curve starts at -40 dB at low frequencies and gradually increases to -20 dB as the frequency increases, indicating a cut in bass frequencies.

5. **Treble Cut (Green Curve)**: This curve starts at -20 dB at low frequencies and gradually decreases to -40 dB at high frequencies, indicating a cut in treble frequencies.

The graph provides a visual representation of how an audio system can be adjusted to either boost or cut bass and treble frequencies, as well as maintain a flat level response.
```

Here is the image describtion:
```
The image is a text label that reads "Fig. 4.2.5 The Baxandall Modified Response Curve." This suggests that it is a figure caption, likely accompanying a graph or chart that illustrates the Baxandall Modified Response Curve, which is a concept related to audio signal processing and equalization. The text is in a bold, black font on a white background.
```

Here is the image describtion:
```
The image depicts a schematic diagram of an audio tone control circuit using an operational amplifier (op-amp). Here is a detailed description of the components and their connections:

1. **Input Section:**
   - The input signal enters the circuit through a capacitor labeled C5 with a value of 10µF. This capacitor is polarized, with the positive side connected to the input signal.

2. **Bass Control:**
   - A variable resistor (potentiometer) labeled VR1 with a value of 100K ohms is used for bass control.
   - The bass control circuit includes resistors R1 (10K ohms), R2 (12K ohms), and R3 (10K ohms).
   - Capacitors C1 (22nF) and C2 (220nF) are also part of the bass control network.

3. **Treble Control:**
   - Another variable resistor (potentiometer) labeled VR2 with a value of 100K ohms is used for treble control.
   - The treble control circuit includes resistors R4 (4.7K ohms) and R3 (10K ohms, shared with the bass control).
   - Capacitors C3 (2.2nF) and C4 (22nF) are part of the treble control network.

4. **Operational Amplifier (Op-amp):**
   - The op-amp is the central component of the circuit, providing amplification and tone control.
   - The non-inverting input (+) of the op-amp is connected to the junction of the input capacitor C5 and the tone control network.
   - The inverting input (-) is connected to the output through a feedback resistor R6 (100K ohms).

5. **Feedback Network:**
   - The feedback network includes resistor R6 (100K ohms) and capacitor C7 (10µF, polarized).
   - The feedback network is connected from the output of the op-amp to the inverting input (-).

6. **Power Supply Decoupling:**
   - Capacitor C6 (47µF, polarized) is connected between the power supply and ground to stabilize the power supply voltage.

7. **Output Section:**
   - The output signal is taken from the output of the op-amp.
   - The output is connected to a capacitor labeled C7 with a value of 10µF (polarized) to block any DC component.

8. **Ground Connections:**
   - The circuit has multiple ground connections, indicated by the symbol for ground (0V).

Overall, this circuit is designed to allow the user to adjust the bass and treble frequencies of an audio signal using the variable resistors VR1 and VR2, respectively. The op-amp amplifies the signal and provides the necessary tone adjustments based on the settings of the bass and treble controls.
```

Here is the image describtion:
```
The image is a caption or label for a figure, specifically labeled as "Fig. 4.2.6." The description provided indicates that the figure is about an active tone control circuit. This circuit utilizes a Baxandall network and an operational amplifier (op-amp) with negative feedback (NFB). The Baxandall network is commonly used in audio applications to adjust the bass and treble frequencies, and the op-amp with negative feedback is used to stabilize and control the gain of the circuit.
```

With active circuits such as that shown in Fig. 4.2.6 the aim is to have the level response at 0dB so there is no gain and no loss due to the tone control circuit. The maximum amount of boost possible should not be sufficient to overload any stage following the tone control if distortion is to be avoided. The design of such control circuits is usually therefore, an integral part of the overall design of an amplifier system.

#### Tone Control ICs

In modern amplifiers the tendency is to use integrated circuit controls that may be operated by either digital or analogue circuitry. A simple solution for bass, treble, balance and volume control in analogue stereo amplifiers is offered by such chips as the LM1036 from Texas Instruments.

The block diagram and an application circuit is shown in Fig. 4.2.7. Each of the four controls is adjusted by applying a variable voltage of between 5.4V (which is supplied by pin 17 of the IC), and 0V. Half the voltage applied to the control pins 4, 9, 12 and 14 gives a level frequency response, central balance between left and right channels, and half volume.

The LM1036 also has provision for a loudness compensation switch. When 'on' this changes the action of the controls to boost the bass and treble frequencies when the volume is at a low setting. The purpose of this is to compensate for the fall off in the function of human hearing at high and low frequencies with quiet sounds.

Here is the image describtion:
```
The image consists of two main sections: a pin configuration diagram and a circuit schematic for the LM1036N integrated circuit, which is a tone and volume control IC.

### Top Section: Pin Configuration Diagram
This section shows the pin layout for the LM1036N in both Dual-In-Line (DIP) and Small Outline (SO) packages. The IC has 20 pins, each labeled with its function:

1. **Pin 1**: Internal Supply Decouple
2. **Pin 2**: Input 1
3. **Pin 3**: Treble Capacitor 1
4. **Pin 4**: Treble Control Input
5. **Pin 5**: AC Bypass 1
6. **Pin 6**: Bass Capacitor 1
7. **Pin 7**: Loudness Compensation Control Input
8. **Pin 8**: Output 1
9. **Pin 9**: Balance Control Input
10. **Pin 10**: Ground (GND)
11. **Pin 11**: Vcc (Power Supply)
12. **Pin 12**: Volume Control Input
13. **Pin 13**: Output 2
14. **Pin 14**: Bass Control Input
15. **Pin 15**: Bass Capacitor 2
16. **Pin 16**: AC Bypass 2
17. **Pin 17**: Zener Voltage
18. **Pin 18**: Treble Capacitor 2
19. **Pin 19**: Input 2
20. **Pin 20**: Ground (GND)

The internal block diagram shows the internal voltage supply, zener regulated voltage, and various control blocks for volume, bass, and treble.

### Bottom Section: Circuit Schematic
This section provides a detailed circuit schematic for the LM1036N. Key components and connections include:

- **Capacitors**: Various capacitors are connected to the pins, such as 0.01 µF, 0.47 µF, 10 µF, 0.39 µF, and 0.22 µF, which are used for filtering and coupling.
- **Resistors**: Several 47kΩ resistors are used for volume, bass, treble, and balance control.
- **Inputs and Outputs**: The inputs (Input 1 and Input 2) and outputs (Output 1 and Output 2) are clearly marked and connected to the respective pins.
- **Control Inputs**: The schematic includes connections for volume control, bass control, treble control, balance control, and loudness compensation.

The schematic shows how the external components are connected to the IC to achieve the desired tone and volume control functionalities. The connections are made to various pins as per the pin configuration diagram, ensuring proper operation of the IC in an audio application.
```

**Fig. 4.2.7 The LM1036 Audio Control IC** 

## Module 4.3 Amplifiers & Impedance

#### What you'll learn in Module 4.3

#### **After studying this section, you should be able to:**

Understand the advantages of controlling input and output impedance in amplifiers.

Understand typical circuits used to increase amplifier input impedance.

- JFET inputs.
- The Darlington Pair.
- Bootstrapping

Understand typical circuits used to reduce amplifier output impedance.

• Emitter Follower stages

Here is the image describtion:
```
The image is a composite of electronic components and a superimposed circuit diagram. The background consists of various electronic parts, including a speaker, a microphone, resistors, capacitors, and wires. These components are somewhat jumbled together, giving the impression of a collection of parts possibly used for assembling or repairing electronic devices.

Superimposed on this background is a green circuit diagram. The diagram includes symbols for electronic components such as resistors, transistors, and connections. The transistor symbol is prominently featured in the center, with its three terminals (base, collector, and emitter) clearly marked. The diagram also includes labels for "In" and "Out," indicating the input and output points of the circuit.

The overall effect of the image is a blend of physical electronic components and their schematic representations, illustrating the relationship between the tangible parts and their roles within an electronic circuit.
```

Amplifier Impedance

The input and output impedances of an amplifier are very important parameters that affect the overall gain in multi-stage amplifiers.

AC Theory Module 7.2 describes how correct matching reduces signal loss between the output of one amplifier and the input of the next in multi stage amplifiers. This section looks at practical methods of obtaining suitable input and output impedances where amplifiers interface with typical input and output devices such as microphones and loudspeakers.

Audio input sources, such as microphones; pick-ups, radio tuners etc. can have impedances ranging from a few hundred ohms to several thousand ohms. Where audio amplifier inputs may have to cater for a number of different input sources, switch selectable inputs to compensate for specific input devices, as described in Amplifiers Module 4.1.

The final (output) stage in a multi-stage amplifier has to drive a 'transducer', which will convert the electrical signal energy produced by the amplifier into some other useful form. For example the electrical waves produced by an audio amplifier will be converted into sound (air pressure) waves by a loudspeaker. A radio frequency (RF) amplifier in a transmitter may be used to drive an antenna (aerial), or a DC amplifier may be driving an electric motor or a relay. Any or all of these transducers may have quite low impedances and require considerable amounts of signal current or power, rather than large signal voltages to operate them. Therefore the output stage of an amplifier may need to have a low output impedance, much lower than would be possible using the common emitter voltage amplifiers described in Amplifiers Module 4.1 to 4.3.

This section describes some types of current and voltage amplifier circuits commonly used to modify input and output impedances. Power output stages are described in Amplifiers Module 5.

#### FET Input Stage

Where very high impedance and low noise is required in an amplifier input, it is common to use a field effect transistor (FET) in an amplifier's input stage. Very high input impedance is obtainable with JFETs as its gate is voltage, rather than current operated. Therefore the JFET takes hardly any current from the device connected to the amplifier input. Even higher input impedances are available where MOSFETs with insulated gate construction (IGFETs) are used. Although FETs generally have less voltage gain and less bandwidth than BJT transistors they also create much less internally generated noise, which makes them ideally suited for use in the early stages of an amplifier, where good signal to noise ratio is important.

Here is the image describtion:
```
The image depicts a schematic diagram of an electronic circuit, specifically a transistor-based audio amplifier. Here is a detailed description of the components and their connections:

1. **Input Section:**
   - The input signal enters the circuit through a capacitor labeled C1 with a value of 0.47µF. This capacitor is used for coupling, allowing AC signals to pass while blocking DC components.

2. **Transistor Tr1 (2N3819):**
   - The input signal is fed into the gate of a JFET transistor labeled Tr1 (2N3819).
   - The source of Tr1 is connected to ground through a resistor R4 (120Ω).
   - The drain of Tr1 is connected to the base of another transistor (Tr2) through a resistor R2 (8.2kΩ).

3. **Biasing Resistors:**
   - The gate of Tr1 is connected to ground through a resistor R1 (2.2MΩ).
   - The drain of Tr1 is also connected to a resistor R3 (18kΩ) which is connected to the +12V supply.

4. **Transistor Tr2 (BC178):**
   - The base of Tr2 is connected to the drain of Tr1 through R2.
   - The emitter of Tr2 is connected to ground through a resistor R5 (1.2kΩ).
   - The collector of Tr2 is connected to the +12V supply through a resistor R6 (10Ω).

5. **Capacitors:**
   - A capacitor C2 (10µF) is connected in parallel with R4.
   - A capacitor C3 (100µF) is connected between the +12V supply and ground.
   - A capacitor C4 (4.7µF) is connected from the collector of Tr2 to the output.

6. **Volume Control:**
   - A variable resistor (potentiometer) VR1 (10kΩ) is connected between the collector of Tr2 and the output. This potentiometer is used to control the volume of the output signal.

7. **Power Supply:**
   - The circuit is powered by a +12V DC supply, with the ground (0V) connected to the common ground of the circuit.

8. **Output Section:**
   - The output signal is taken from the wiper of the potentiometer VR1, which allows for adjustable volume control.

This circuit is designed to amplify an audio signal, with the JFET transistor Tr1 providing initial amplification and the bipolar junction transistor Tr2 providing further amplification. The capacitors are used for coupling and bypassing, while the resistors set the biasing and operating points of the transistors. The potentiometer VR1 allows for volume adjustment of the output signal.
```

**Fig. 4.3.2 High Impedance JFET Input Stage** 

#### Operation

Because the input resistance of the JFET is extremely high, the input impedance of the circuit is approximately the value of R1, and as practically no current is flowing into the input, there is no potential across R1, therefore the gate of Tr1 is effectively at zero volts. To operate correctly, the gate of the N channel JFET must be more negative than the source, this is achieved by making the source of Tr1 positive. The signal applied to the gate will then vary the gate voltage and so vary the drain current through the JFET. The biasing of the JFET is set by R2 and R3. As JFET gain is not particularly high, extra gain is provided by the PNP transistor Tr2. The overall gain of the two-stage amplifier is set at approximately 11 by the negative feedback provided by R4 and R5.

#### Decoupling

In Fig 4.3.2, R3 is decoupled by C2 so that the bottom end of R4 is effectively at ground potential as far as AC is concerned, the value of C2 is not particularly large in this circuit, as the larger the value of electrolytic capacitor the more noise it will produce, and the aim of the circuit is to keep internally generated noise to a minimum. C1 and C4 coupling capacitors, (also relatively small values) provide isolation from any DC

Here is the image describtion:
```
The image is a schematic diagram illustrating a supply decoupling circuit. The diagram is labeled as "Fig. 4.3.3 Supply Decoupling."

In the diagram:
- There is a DC supply line coming from the right side, labeled "From DC supply with AC noise."
- This line is connected to a resistor labeled "R6."
- After the resistor, the line splits into two paths:
  - One path continues horizontally to the left, labeled "DC only to circuit."
  - The other path goes vertically downward to a capacitor labeled "C3."
- The capacitor "C3" is connected to the ground.
- There is a note next to the capacitor that reads "Xc ≈ 0Ω at frequency of AC noise," indicating that the capacitor is designed to have a very low impedance at the frequency of the AC noise, effectively filtering it out.

The purpose of this circuit is to filter out AC noise from the DC supply, ensuring that only the DC component reaches the circuit. The capacitor "C3" shunts the AC noise to the ground, while the resistor "R6" helps in isolating the noise from the DC supply line.
```

**(From Fig 4.3.2)** 

voltages present on any connected circuits. Using a very high value for R1 produces a high input impedance but the higher the value, the more prone the circuit will be to instability and oscillation. To prevent this possibility, effective decoupling from other circuits and the supply is necessary, decoupling here is provided by R6 and C3 as shown in Fig. 4.3.3.

Common emitter amplifiers generally have a medium to high output impedance, the value depending mainly on the value of load resistor in the final stage of amplification. Many typical transducers, such as loudspeakers, relays, motors etc. are inductive devices having a low impedance of only a few ohms.

Connecting such devices to the output of a voltage amplifier with a load resistance of several thousand ohms will result in poor impedance matching with practically the whole of the output being developed across the load resistor instead of across the load. One answer to this problem is to reduce the output impedance by using an emitter follower, which is a single transistor connected in common collector mode.

Here is the image describtion:
```
The image depicts a schematic diagram of a common collector transistor amplifier circuit, also known as an emitter follower. The key components and their connections are as follows:

1. **Transistor**: The central component is an NPN transistor, represented by the standard symbol with the emitter, base, and collector terminals. The collector is connected to the positive supply voltage (Vcc), the base is connected to the input signal through a capacitor (C1) and a resistor (R1), and the emitter is connected to the output.

2. **Capacitor (C1)**: This capacitor is connected in series with the input signal. It serves as a coupling capacitor, allowing AC signals to pass through while blocking any DC component.

3. **Resistors (R1 and R2)**: 
   - **R1** is connected between the base of the transistor and the positive supply voltage (Vcc). It provides the necessary biasing for the transistor.
   - **R2** is connected between the emitter of the transistor and ground. It helps stabilize the operating point of the transistor and provides feedback.

4. **Input and Output**: 
   - The input signal is applied to the base of the transistor through the capacitor C1 and resistor R1.
   - The output is taken from the emitter of the transistor, which is also connected to the resistor R2.

The diagram is labeled as "Fig. 4.3.4 Common Collector," indicating that it is an example of a common collector configuration, which is known for providing a high input impedance, low output impedance, and a voltage gain of approximately one.
```

**or Emitter Follower** 

#### Common Collector Mode

This configuration uses the collector lead as the common connection for input and output. In the circuit (Fig. 4.3.4) the input to the transistor is connected between base and ground, and the output is connected across the load resistor between emitter and ground. Remember that with the collector connected directly to the supply, the collector is at ground potential as far as AC is concerned, because of the presence of large decoupling capacitors connected between supply and ground.

The common collector amplifier is called an emitter follower because the output, taken from the emitter is in phase with and 'follows' the input voltage at the base. In fact the base and emitter voltages are almost identical so the emitter follower has a voltage gain of 1 (in practice, slightly less) because of the 100% negative feedback created by the emitter load resistor not being decoupled, as would be the normal case in a common emitter amplifier. This causes the full amplitude of the output signal to be fed back to the base, giving a closed loop gain β of 1.

The emitter follower is therefore of no use as a voltage amplifier. It does however, have other very useful properties. Its current gain is large, and approximately equals the current gain (hfe) of the transistor. The input impedance of the circuit is high, 100KΩ or more being typical, although this will depend to some extent on the value of the base bias resistor R1 in Fig. 4.3.4, which is in parallel with the input resistance of the transistor, but this shunting effect can be reduced by 'Bootstrapping'. The output impedance of the circuit is very low, typically in the region of 50Ω. Because of its use in matching relatively high output impedance voltage amplifiers to low impedance loads, the emitter follower may also be called a 'Buffer Amplifier'.

#### The Emitter Follower as a Voltage Regulator

Another use for the emitter follower is as a voltage regulator, and is useful in power supplies where a small voltage can be used to regulate a large current., as shown in Fig. 4.3.5. This circuit ensures that the regulated 5 volt supply remains at the correct voltage even if the 12 volt supply changes. An accurate five volts is also maintained for a range of currents drawn by the circuit being supplied. Regulation can be achieved just using a resistor and Zener diode combination but much higher currents can be handled when an emitter follower is used.

Here is the image describtion:
```
The image depicts a circuit diagram labeled "Fig. 4.3.5 Emitter Follower Voltage." The circuit is designed to provide a regulated +5V supply from an unregulated +12V supply using a transistor and a Zener diode.

Here are the key components and their connections in the circuit:

1. **+12V Unregulated Supply**: This is the input voltage source for the circuit, providing an unregulated 12V.

2. **Resistor (R1)**: Connected in series with the +12V unregulated supply. The other end of the resistor is connected to the base of the transistor.

3. **Transistor**: The transistor is the main active component in the circuit. It has three terminals:
   - **Base**: Connected to the junction between the resistor (R1) and the Zener diode.
   - **Collector**: Connected directly to the +12V unregulated supply.
   - **Emitter**: Provides the regulated +5V output and is connected to the load.

4. **Zener Diode (5V6)**: The Zener diode is connected in reverse bias between the base of the transistor and ground. It is labeled as "5V6," indicating a Zener voltage of 5.6V.

5. **Load**: The load is connected to the emitter of the transistor, which provides the regulated +5V supply. The other end of the load is connected to ground.

6. **Ground**: The ground symbol is used to indicate the common return path for the circuit.

The circuit works as follows:
- The +12V unregulated supply is applied to the collector of the transistor.
- The Zener diode maintains a constant voltage of 5.6V at the base of the transistor.
- The emitter voltage of the transistor will be approximately 0.6V less than the base voltage due to the base-emitter junction voltage drop, resulting in a regulated output of around 5V at the emitter.
- This regulated +5V is then supplied to the load.

Overall, the circuit is an emitter follower configuration that uses a Zener diode to stabilize the base voltage of the transistor, thereby providing a regulated output voltage.
```

Notice in Fig.4.3.5 that the Zener diode has a voltage rating of 5V6 (meaning 5.6volts), this will maintain the base of the transistor at that voltage, and the emitter of the transistor at 0.6V below the base voltage, will be maintained at 5 volts. A small current maintaining the base voltage at 5.6V is therefore able to accurately control a much larger current flowing through the collector and emitter.

The emitter follower circuit is also the basis of many push-pull class B and class AB power output amplifier stages described in Amplifiers Module 5

#### The Darlington Pair

The effect of a high input impedance is to reduce the input current to the amplifier. If the input current for a given input voltage is reduced by whatever method, the effect is to increase the input impedance. The emitter follower has a high input impedance, but this may be reduced to an unacceptable level by the presence of the base bias resistor.

However another circuit, the compound or Darlington pair shown in Fig. 4.3.6 can greatly increase input impedance. By using one emitter follower (Tr1) to drive another (Tr2) the overall current gain becomes the product of the individual gains, hfe1 x hfe2 and can be typically 1000 or more. This greatly reduces the signal current required by the base of Tr1 and thereby dramatically increases the input impedance.

Here is the image describtion:
```
The image contains a block of text discussing the use of Darlington pairs in electronic circuits. It mentions that the Darlington pair can be used in common emitter mode, as illustrated in a figure referred to as Fig. 4.3.7. The text also notes that Darlington transistors are available in combined packages for both PNP and NPN types. These packages include back electromotive force (emf) protection diodes, which are typically necessary when the Darlington configuration is employed as a high current gain output device for switching high current inductive loads.
```

Here is the image describtion:
```
The image depicts a basic electronic circuit diagram featuring a two-stage transistor amplifier. Here is a detailed description of the components and their connections:

1. **Input**: The input signal is fed into the circuit from the left side, indicated by the label "Input."

2. **Capacitor (C1)**: The input signal first passes through a capacitor labeled "C1." This capacitor is used for coupling, allowing AC signals to pass while blocking DC components.

3. **Resistor (R1)**: After the capacitor, the signal encounters a resistor labeled "R1." This resistor is connected to the base of the first transistor (Tr1) and is used to set the biasing of the transistor.

4. **Transistor (Tr1)**: The first transistor, labeled "Tr1," is an NPN transistor. The base of Tr1 is connected to the junction of C1 and R1. The emitter of Tr1 is connected to the ground (0V), and the collector is connected to the power supply rail (+Vcc) through a direct connection.

5. **Transistor (Tr2)**: The second transistor, labeled "Tr2," is also an NPN transistor. The base of Tr2 is connected to the collector of Tr1. The emitter of Tr2 is connected to the ground (0V), and the collector is connected to the power supply rail (+Vcc) through a direct connection.

6. **Resistor (R2)**: The output signal is taken from the collector of Tr2 through a resistor labeled "R2." This resistor is connected between the collector of Tr2 and the ground (0V).

7. **Output**: The output signal is labeled "Output" and is taken from the junction of the collector of Tr2 and resistor R2.

8. **Power Supply**: The circuit is powered by a DC voltage source labeled "+Vcc" at the top, with the ground (0V) at the bottom.

In summary, this circuit is a two-stage amplifier with capacitive coupling at the input, two NPN transistors in a common-emitter configuration, and resistive load at the output. The design allows for amplification of the input signal, with the output taken from the second transistor's collector.
```

**Fig. 4.3.6 The Emitter Follower Converted to a Darlington Pair**

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage transistor amplifier circuit. Here is a detailed description of the components and their connections:

1. **Transistors (Tr1 and Tr2)**: The circuit includes two NPN transistors labeled Tr1 and Tr2. These transistors are connected in a configuration that allows for amplification of the input signal.

2. **Resistors (R1 and R2)**: There are two resistors in the circuit. R1 is connected between the collector of Tr1 and the positive supply voltage (+Vcc). R2 is connected between the collector of Tr2 and the positive supply voltage (+Vcc).

3. **Capacitor (C1)**: A capacitor labeled C1 is connected in series with the input signal. This capacitor is used for coupling the input signal to the base of the first transistor (Tr1), blocking any DC component and allowing only the AC signal to pass through.

4. **Input and Output**: The input signal is applied to the left side of the circuit, before the capacitor C1. The output signal is taken from the collector of the second transistor (Tr2).

5. **Power Supply**: The circuit is powered by a positive voltage supply labeled +Vcc and a ground connection labeled 0V.

6. **Connections**:
   - The input signal passes through capacitor C1 and is fed to the base of Tr1.
   - The emitter of Tr1 is connected to ground (0V).
   - The collector of Tr1 is connected to resistor R1, which is then connected to +Vcc.
   - The base of Tr2 is connected to the collector of Tr1.
   - The emitter of Tr2 is connected to ground (0V).
   - The collector of Tr2 is connected to resistor R2, which is then connected to +Vcc.
   - The output signal is taken from the collector of Tr2.

This configuration is typical for a common-emitter amplifier stage, where the first transistor amplifies the input signal, and the second transistor further amplifies the signal to provide a higher gain.
```

**Fig. 4.3.7 The Darlington Pair with Common Emitter Output**

Darlington amplifiers are also available in integrated circuit form, such as the ULN2803, which contains eight high current, Darlington amplifiers with open collector outputs, for interfacing between TTL (5V) logic circuits and high current/high voltage (up to 500mA and 50V) devices. When pin 10 is connected to +V each output is diode protected for driving inductive loads against back e.m.f.

#### Bootstrapping

Bootstrapping (Using positive feedback to feed part of the output back to the input, but without causing oscillation) is a method of apparently increasing the value of a fixed resistor as it appears to A.C. signals, and thereby increasing input impedance. A basic bootstrap amplifier is shown in Fig. 4.3.8 where capacitor CB is the 'Bootstrap Capacitor', which provides A.C. feedback to a resistor in series with the base. The value of CB will be large, about 10 x the lowest frequency handled x the value of the series resistor (10ƒminR3).

Here is the image describtion:
```
The image consists of two diagrams labeled as Fig. 4.3.8. 

The first diagram is titled "The Darlington Integrated Circuit ULN2803." It shows a schematic representation of the ULN2803 integrated circuit. The circuit has 8 inputs on the top side, labeled 1 through 8, and 8 protected outputs on the bottom side, also labeled 1 through 8. Each input is connected to a Darlington pair transistor configuration, which is represented by two transistors in series with a diode. The outputs are protected, likely indicating the presence of flyback diodes to protect against voltage spikes. The left side of the diagram is connected to 0V (ground), and the right side is connected to +V (positive voltage supply).

The second diagram is titled "Bootstrapping applied." It shows a basic transistor circuit with bootstrapping. The circuit includes a transistor with its collector connected to the output and its emitter connected to ground. The base of the transistor is connected to the input through a resistor labeled R1. There is another resistor, R2, connected between the base and ground. A capacitor, labeled C_B, is connected between the base and the output. Additionally, there is a resistor, R3, connected in parallel with the capacitor C_B. This configuration is used to improve the performance of the transistor by providing positive feedback through the capacitor, which helps to maintain a higher input impedance and improve the frequency response of the circuit.

Overall, the image provides a detailed view of the ULN2803 Darlington transistor array and a bootstrapping circuit used to enhance transistor performance.
```

**to an Emitter Follower** 

Although positive feedback is being used, which would normally cause an amplifier to oscillate, the voltage gain of the emitter follower is less than 1, which prevents oscillation.

In Fig. 4.3.8 the base of the emitter follower is biased from a potential divider via R3. By feeding the output waveform back to the left hand side of R3 the voltage at this end of R3 is made to rise and fall in phase with the input signal at the base end of R3.

Because the output waveform of the emitter follower is a slightly less amplitude than the base waveform (due to the less than 1 gain of the transistor) there will be a very small signal current waveform across R3. Such a small current waveform suggests a very small current is flowing; therefore the resistance of R3 must be very high, much higher than in fact it is. The input impedance of the amplifier has therefore been increased.

The effective A.C. value of R3 is increased by R3 ÷ (1 −Ao) where Ao is the open loop gain of the amplifier.

For example a 47KΩ resistor with bootstrapping would appear to be:

$$\text{The \text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet}\text{\textbullet} = \text{R3}^\circ, = \frac{\text{R3}}{(1 - \text{R3}^\circ)}$$

So if AO = 0.98 the apparent value of R3 would be 47 x 10<sup>3</sup> ÷ (1- 0.98) = 2,35MΩ

The main drawback of this method of increasing input impedance compared with other methods is that the use of positive feedback is likely to increase noise and distortion.

## Amplifier Circuits Module 4.4 Amplifier Circuits Quiz 4

Try our quiz, based on the information you can find in Amplifier Circuits Module 4. You can check your answers at:

http://www.learnabout-electronics.org/Amplifiers/amplifiers44.php

#### 1.

What would be the function of the control circuit shown in Fig. 4.4.1 in an audio amplifier?

- a) Volume.
- b) Balance.
- c) Treble boost.
- d) Tone.

#### 2.

What is the purpose of RIAA de-emphasis in an audio pre-amplifier?

- a) To provide correct impedance matching on a MIC input.
- b) To provide D to A conversion on a CD input.
- c) To provide frequency correction on a PHONO input.
- d) To provide level correction on a line level output.

#### 3.

When the bass and treble controls in a Baxandall passive tone control circuit are set at their mid point, what will be the approximate voltage gain of the tone control circuit?

a) -3dB b) -6dB c) -20dB d) -40dB

#### 4.

Complete the following sentence: Compared with a bipolar transistor, using a JFET transistor in the input stage of an audio amplifier instead of a bipolar transistor provides...

- a) ...higher input impedance and reduced signal to noise ratio.
- b) ...higher input impedance and increased signal to noise ratio.
- c) ...higher gain and increased signal to noise ratio.
- d) ...higher gain and reduced signal to noise ratio.

#### 5.

Bootstrapping in an amplifier circuit refers to which of the following techniques?

- a) Using positive feedback to increase the apparent input impedance of the amplifier.
- b) Using negative feedback to increase the apparent input impedance of the amplifier.
- c) Using negative feedback to reduce the apparent output impedance of the amplifier.
- d) Using positive feedback to increase the stability of the amplifier.

Here is the image describtion:
```
The image appears to be a header or a title section from a document. It includes the following details:

- The title "AMPLIFIERS MODULE 04.PDF" is written in uppercase letters on the left side.
- The number "13" is centered, likely indicating the page number.
- On the right side, there is a copyright notice that reads "© E. COATES 2007 - 2012."

The text is black on a white background, and there is a thin horizontal line above the text, separating it from the rest of the document.
```

Here is the image describtion:
```
The image depicts a simple electronic circuit diagram. The circuit includes the following components and connections:

1. **Input and Output Terminals**: The circuit has an input terminal on the left side and an output terminal on the right side.

2. **Capacitor (C1)**: There is a capacitor labeled C1 connected between the input and the output terminals. The capacitor is represented by two parallel lines, indicating its function as a component that stores electrical energy.

3. **Resistor (R1)**: Below the capacitor, there is a resistor labeled R1. The resistor is depicted as a rectangular block, which is a common symbol for resistors in circuit diagrams.

4. **Variable Resistor (VR1)**: Below R1, there is a variable resistor labeled VR1. This component is also represented as a rectangular block, but it has an arrow pointing to it, indicating that it is adjustable.

5. **Ground Connection (0V)**: The bottom of the circuit is connected to a ground symbol, labeled as 0V, indicating that this point is at zero volts or ground potential.

6. **Figure Label**: The diagram is labeled as "Fig. 4.4.1" to identify it within a larger set of figures or a document.

The circuit appears to be a simple RC (resistor-capacitor) filter with an adjustable resistor, which could be used to control the filtering characteristics. The input signal passes through the capacitor and the resistors before reaching the output, with the ground connection providing a reference point for the circuit.
```

#### 6.

Which of the following features does the circuit illustrated in Fig. 4.4.2 possess?

- a) High voltage gain and very high input impedance.
- b) Low voltage gain and very high output impedance.
- c) High current gain and very high input impedance.
- d) Low current gain and very high output impedance.

Here is the image describtion:
```
The image depicts an electronic circuit diagram, specifically a two-stage transistor amplifier. Here is a detailed description of the components and their connections:

1. **Transistors (Tr1 and Tr2)**: The circuit includes two NPN transistors labeled Tr1 and Tr2. The emitter of Tr1 is connected to the ground (0V), and its collector is connected to the base of Tr2. The emitter of Tr2 is also connected to the ground (0V).

2. **Resistors (R1 and R2)**: 
   - R1 is connected between the collector of Tr1 and the positive supply voltage (+Vcc).
   - R2 is connected between the collector of Tr2 and the ground (0V).

3. **Capacitor (C1)**: C1 is connected in series with the input signal. One end of C1 is connected to the input terminal, and the other end is connected to the base of Tr1.

4. **Power Supply**: The circuit is powered by a positive voltage supply labeled +Vcc, which is connected to the top of R1 and the collector of Tr2.

5. **Input and Output**:
   - The input signal is fed into the circuit through the capacitor C1.
   - The output signal is taken from the collector of Tr2.

6. **Ground (0V)**: The ground symbol is used to indicate the common return path for electric current, connected to the emitters of both transistors and one end of R2.

The diagram is labeled as "Fig 4.4.2," indicating it is part of a larger set of figures, likely from a textbook or technical document. The circuit is a common configuration for amplifying an input signal using two stages of transistor amplification.
```

#### 7.

Refer to Fig 4.4.3. If the real value of R3 is 33KΩ and the open loop gain of the emitter follower amplifier (AO) is 0.98, what will be the apparent value R3B of R3 due to the bootstrapping

- a) 1.65MΩ
- b) b) 2.35MΩ
- c) c) 3.27MΩ
- d) d) 230.5KΩ

Now check your answers at:

http://www.learnabout-electronics.org/Amplifiers/amplifiers44.php