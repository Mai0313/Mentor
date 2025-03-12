## Amplifiers

Here is the image describtion:
```
The image is a simple, black rectangular sign with white text. At the top of the sign, the word "Module" is written in a clear, sans-serif font. Below the word "Module," there is a large, bold number "4" centered on the sign. The overall design is minimalistic, with a high contrast between the black background and the white text, making the information easy to read.
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
The image shows a close-up view of two control knobs on an audio device, likely an amplifier or equalizer. The knobs are labeled "BASS" and "TREBLE," indicating that they are used to adjust the bass and treble frequencies of the audio output. Each knob has a scale ranging from -5 to +5, with a central position marked as 0. The knobs are metallic and have a sleek, polished appearance.

In the lower part of the image, there is a partial view of an electronic circuit diagram. The visible part of the diagram includes a symbol for a transistor, labeled "Tr1." The diagram is slightly blurred and appears to be overlaid or partially transparent, blending into the background of the image. The overall composition suggests a focus on audio equipment and electronic components.
```

Here is the image describtion:
```
The image consists of two main parts: a schematic diagram and a set of audio input/output connectors.

1. **Schematic Diagram:**
   - The upper part of the image shows a simple electronic circuit diagram.
   - The diagram includes two transistors labeled as Tr1 and Tr2. 
   - The transistors are represented by the standard symbol for bipolar junction transistors (BJTs), with the emitter, base, and collector terminals.
   - The transistors are connected in a configuration that suggests a basic amplifier or switching circuit.
   - There is also a symbol that looks like a resistor or a capacitor connected to the base of Tr1, indicating a component that influences the operation of the transistor.

2. **Audio Input/Output Connectors:**
   - The lower part of the image shows a panel with multiple RCA connectors.
   - The connectors are circular with a central pin and an outer ring, typical of RCA jacks used for audio and video signals.
   - The connectors are color-coded, with red and white indicating the right and left audio channels, respectively.
   - There are labels next to the connectors: "MIC" (microphone), "CD" (compact disc), and other symbols that are not fully visible in the image.
   - The connectors are arranged in rows, suggesting multiple input/output options for audio equipment.

Overall, the image combines an electronic circuit diagram with a practical application in audio equipment, illustrating the connection between theoretical electronics and real-world audio interfaces.
```

particular stages of the amplifier frequency dependent. This can be achieved by modifying either the response of one or more of the amplifier stages, or the response of a negative feedback path.

Fig. 4.0.1 shows (shaded green) stages where such modification will take place, the remaining stages having a flat response curve.

#### Modifying Input and Output Impedance.

The importance of an amplifier's input and output impedance is discussed in AC Theory Module 7, and using NFB to control impedance is described in Amplifiers Module 3.2.

Module 4.3 describes some other amplifier circuits that are commonly used to control the values of input and output impedances in amplifier circuits.

Here is the image describtion:
```
The image is a block diagram illustrating the process of controlling the response curve of an audio amplifier. The diagram is labeled as "Fig. 4.0.1 Controlling the Response Curve of an Audio Amplifier."

The diagram consists of several blocks connected in series, each representing a different stage in the audio amplification process. The blocks are as follows:

1. **Input Select**: This block is the first in the series and has multiple input options listed on the left side. The inputs include:
   - CD
   - TAPE
   - RADIO
   - PICK UP
   - MIC
   - AUX

2. **Pre-amp**: The second block in the series, labeled "Pre-amp," is responsible for initial amplification of the selected input signal.

3. **Voltage amp**: The third block, labeled "Voltage amp," further amplifies the signal to a higher voltage level.

4. **Tone control**: The fourth block, labeled "Tone control," allows for adjustment of the audio signal's frequency response, enabling control over bass, midrange, and treble frequencies.

5. **Power amp**: The fifth block, labeled "Power amp," amplifies the signal to a level suitable for driving a speaker.

6. **Speaker**: The final element in the series is a speaker icon, representing the output device that produces the audible sound.

The blocks "Input select" and "Tone control" are highlighted in green, indicating their importance in controlling the response curve of the audio amplifier. The other blocks are outlined in black. The signal flow is from left to right, starting from the input selection and ending at the speaker.
```

AMPLIFIERS MODULE 04.PDF 1 © E. COATES 2007 -2012

### Module 4.1 Amplifier Input Compensation

Here is the image describtion:
```
The image is a combination of text and graphics related to an educational module on amplifiers, specifically Module 4.1. 

On the left side of the image, there is a text box with the heading "What you'll learn in Module 4.1." Below this heading, the text reads: "After studying this section, you should be able to:" followed by two main points. The first point is "Recognise the need for changing the shape of an amplifier’s frequency response." The second point is "Understand the operation of typical circuits for:" which is followed by a bulleted list of three items: "Input Compensation," "Line Level," and "Phono De-emphasis."

On the right side of the image, there are two graphics. The upper graphic is a simple schematic diagram showing connections labeled "AUX," "PU," and "TAPE" leading into a block labeled "Pre-amplifier." The lower graphic is a photograph of a panel with multiple RCA connectors. The connectors are arranged in two rows, with the top row having red and white connectors and the bottom row having yellow and white connectors. The connectors are labeled "MIC," "O," "QO," and "CD."

The overall theme of the image is educational, focusing on the technical aspects of amplifiers and their frequency response, as well as the operation of related circuits.
```

#### Input Compensation

Pre amplifiers are designed to increase the signal voltage amplitude of input devices to a level suitable for the input to a power amplifier. Pre-amplifiers often need a number of different inputs, each with a different gain and/or different input impedance. This is to ensure that each device connected to the various inputs provides (after pre-amplification) an output level sufficient to drive the input of a power amplifier and provide full power (when full volume is used) and minimum noise.

#### Line Level

This pre amplifier output is usually called 'Line level' and most amplifiers will have a line in and a line out socket, on PC sound cards these are normally coloured pale green and light blue respectively. The actual line level measured in volts varies between different types of equipment but is around 1Vpp on consumer equipment to 2.5Vpp on professional equipment. With some input devices such as CDs or radio tuners, little or no pre-amplification is needed but devices such as microphones, phono inputs and guitar pickups provide much lower signal levels and need specially adapted inputs to the preamplifier.

Here is the image describtion:
```
The image is a schematic diagram of a two-stage pre-amplifier with input compensation. The diagram includes various components such as resistors, capacitors, transistors, and switches, which are interconnected to form the pre-amplifier circuit. Here is a detailed description of the components and their connections:

1. **Inputs**: There are three input options labeled AUX, RADIO, and PHONO. These inputs are connected to a switch labeled SW1a, which allows the user to select the desired input source.

2. **Capacitor C1**: This capacitor is connected in series with the selected input source to the base of the first transistor (Tr1).

3. **Resistors R1, R2, and R3**: 
   - R1 is connected between the base of Tr1 and the ground.
   - R2 is connected between the positive supply voltage (Vcc) and the collector of Tr1.
   - R3 is connected between the emitter of Tr1 and the ground.

4. **Transistor Tr1**: This is the first transistor in the circuit, with its base connected to the input through C1, its collector connected to R2, and its emitter connected to R3.

5. **Capacitor C4**: This capacitor is connected in parallel with R3, providing feedback and stabilization.

6. **Resistor R4**: This resistor is connected between the positive supply voltage (Vcc) and the collector of the second transistor (Tr2).

7. **Capacitor C2**: This capacitor is connected in series with the output of the second transistor (Tr2) to the tone controls.

8. **Transistor Tr2**: This is the second transistor in the circuit, with its base connected to the collector of Tr1 through R5, its collector connected to R4, and its emitter connected to R6.

9. **Resistor R5**: This resistor is connected between the collector of Tr1 and the base of Tr2.

10. **Resistor R6**: This resistor is connected between the emitter of Tr2 and the ground.

11. **Capacitor C3**: This capacitor is connected in parallel with R6, providing feedback and stabilization.

12. **Switch SW1b**: This switch is connected to the emitter of Tr2 and allows the user to select different compensation networks.

13. **Resistors R7, R8, and R9**: These resistors are part of the compensation network and are connected in series with the switch SW1b.

14. **Capacitors C5 and C6**: These capacitors are also part of the compensation network and are connected in parallel with the resistors R7, R8, and R9.

15. **Output**: The output of the pre-amplifier is taken from the collector of Tr2 through capacitor C2 and is labeled "Output to Tone Controls."

The circuit is designed to amplify audio signals from different input sources and provide a compensated output to the tone control stage. The use of transistors, resistors, and capacitors ensures proper amplification and stabilization of the audio signals.
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
The image is a graph that illustrates the frequency response curves associated with the RIAA (Recording Industry Association of America) equalization process used in vinyl record playback. The graph has the following features:

1. **Axes**:
   - The horizontal axis represents frequency, ranging from 20 Hz to 20 kHz.
   - The vertical axis represents decibels (dB), ranging from -20 dB to +20 dB.

2. **Curves**:
   - There are three distinct curves on the graph:
     - **Green Curve**: Labeled "RIAA pre-emphasis during record," this curve shows the equalization applied during the recording process. It starts at +20 dB at 20 Hz, gradually decreases to 0 dB around 1 kHz, and continues to decrease, reaching -20 dB at 20 kHz.
     - **Red Curve**: Labeled "Pre-amplifier de-emphasis," this curve represents the equalization applied during playback to counteract the pre-emphasis. It starts at -20 dB at 20 Hz, gradually increases to 0 dB around 1 kHz, and continues to increase, reaching +20 dB at 20 kHz.
     - **Blue Line**: Labeled "Resultant response," this line is flat at 0 dB across all frequencies, indicating that the combined effect of the pre-emphasis and de-emphasis results in a flat frequency response.

3. **Grid**:
   - The graph has a grid with vertical lines representing specific frequencies and horizontal lines representing specific dB levels, aiding in the visualization of the curves.

The purpose of the RIAA equalization is to improve the sound quality and playback of vinyl records by reducing noise and distortion. The pre-emphasis boosts high frequencies and attenuates low frequencies during recording, while the de-emphasis does the opposite during playback, resulting in a flat overall frequency response.
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
The image shows a close-up view of two control knobs on an audio device, likely an amplifier or a stereo system. The knobs are labeled "BASS" and "TREBLE," indicating that they are used to adjust the bass and treble frequencies of the audio output.

- The "BASS" knob is on the left side. It has a circular design with a metallic finish and a black face. The face of the knob is marked with numbers ranging from -5 to +5, with 0 at the top center position. The numbers are evenly spaced around the circumference of the knob, allowing for precise adjustments to the bass levels.

- The "TREBLE" knob is on the right side and has a similar design to the "BASS" knob. It also features a metallic finish and a black face with numbers ranging from -5 to +5, with 0 at the top center position. The numbers are evenly spaced around the knob, allowing for precise adjustments to the treble levels.

Both knobs appear to be part of a high-quality audio device, given their sturdy and polished appearance. The background of the device is a smooth, metallic surface, adding to the overall sleek and modern look of the equipment.
```

#### Tone Control

Tone Control, shown in its most basic form in Fig. 4.2.1 provides a simple means of regulating the amount of higher frequencies present in the output signal fed to the loudspeakers. a simple method of achieving this is to place a variable CR network between the voltage amplifier and the power amplifier stages, The value of C1 is chosen to pass the higher audio frequencies, this has the effect of progressively reducing the higher frequencies as the variable resistor slider is adjusted towards the bottom end of the tone control, The minimum level of attenuation of the higher (treble) frequencies is limited by R1, which prevents C1 being connected directly to ground. As the circuit only reduces the high frequency content of the signal it could be called a simple Treble Cut control. The use of these simple circuits is normally restricted to guitar applications or inexpensive radios.

Here is the image describtion:
```
The image depicts a simple electronic circuit diagram, specifically a tone control circuit. Here is a detailed description of the components and their connections:

1. **Capacitor (C1)**: The circuit includes a capacitor labeled C1. The capacitor is connected in series with the input signal. One terminal of the capacitor is connected to the input, and the other terminal is connected to one end of the resistor R1.

2. **Resistor (R1)**: The resistor R1 is connected in series with the capacitor C1. One end of the resistor is connected to the capacitor, and the other end is connected to the output.

3. **Variable Resistor (Tone Control)**: There is a variable resistor (potentiometer) connected in parallel with the resistor R1. This variable resistor is labeled "Tone" and is used to adjust the tone of the output signal. The wiper (adjustable middle terminal) of the potentiometer is connected to the output, while the other two terminals are connected across the resistor R1.

4. **Input and Output**: The circuit has designated points for input and output signals. The input is connected to the top terminal of the capacitor C1, and the output is taken from the junction between the resistor R1 and the wiper of the potentiometer.

5. **Ground**: The bottom terminal of the potentiometer is connected to the ground.

In summary, this circuit is a basic tone control circuit where the capacitor and resistor form a high-pass filter, and the potentiometer allows for adjustment of the tone by varying the resistance in parallel with R1. This configuration can be used to control the treble frequencies in an audio signal.
```

Here is the image describtion:
```
The image shows a text label that reads "Fig. 4.2.1 Simple Tone Control." The text is in a bold, black font, and it appears to be a caption or title for a figure in a document, likely related to electronics or audio engineering. The figure number "4.2.1" suggests that it is part of a larger document or book, specifically from chapter 4, section 2, and it is the first figure in that section. The term "Simple Tone Control" indicates that the figure is likely related to a basic circuit or system used to adjust the tone or frequency response of an audio signal.
```

 In hi-fi amplifiers, tone control refers to the boosting or reduction of particular audio frequencies. This may be done to suit the preferences of the listener, not everyone perceives sound in exactly the same way, for example the frequency response of the human ear changes with age. The room or hall in which the sound is reproduced will also affect the nature of the sound. Many techniques are used to alter the sound, and in particular the frequency response of the amplifiers producing the sound. These range from simple RC filters, through passive and active frequency control networks to complex digital signal processing.

#### The Baxandall Tone Control Circuit

The circuit discussed here is an example of the Baxandall tone control circuit, illustrated in Fig. 4.2.2, which is an analogue circuit providing independent control of bass and treble frequencies; both bass and treble can be boosted or cut and with both controls at their mid positions, provides a relatively flat frequency response, as illustrated by the blue 'Level response' graph line in Fig. 4.2.5. The original design, proposed by P. J. Baxandall in 1952, used a valve (tube) amplifier and feedback as part of the circuit to reduce the

Here is the image describtion:
```
The image depicts a Baxandall Tone Control Circuit, which is a type of audio equalization circuit used to adjust the bass and treble frequencies of an audio signal. The circuit is composed of various resistors, capacitors, and variable resistors (potentiometers) arranged in a specific configuration to achieve tone control.

Here is a detailed description of the components and their connections:

1. **Input and Output:**
   - The circuit has an input terminal on the left side where the audio signal is fed into the circuit.
   - The output terminal is on the right side, where the processed audio signal is taken out.

2. **Resistors:**
   - **R1 (10K ohms):** Connected in series with the input signal.
   - **R2 (1K ohms):** Connected between the junction of C2 and the ground.
   - **R3 (10K ohms):** Connected in series with the output signal.

3. **Capacitors:**
   - **C1 (22nF):** Connected between the junction of R1 and VR1, and the junction of R3 and VR2.
   - **C2 (220nF):** Connected between the junction of VR1 and R2, and the ground.
   - **C3 (2.2nF):** Connected between the junction of R3 and VR2, and the output.
   - **C4 (22nF):** Connected between the junction of VR2 and the ground.

4. **Variable Resistors (Potentiometers):**
   - **VR1 (100K ohms, labeled as Bass):** Connected between the junction of R1 and C1, and the junction of C2 and R2. This potentiometer is used to adjust the bass frequencies.
   - **VR2 (100K ohms, labeled as Treble):** Connected between the junction of C1 and R3, and the junction of C3 and C4. This potentiometer is used to adjust the treble frequencies.

5. **Ground Connections:**
   - The circuit has multiple ground connections, indicated by the symbol (three horizontal lines) and labeled as "Gnd" or "0V." These are connected to the negative terminal or the ground of the power supply.

The Baxandall Tone Control Circuit allows for independent adjustment of bass and treble frequencies by varying the resistance of VR1 and VR2, respectively. This type of circuit is commonly used in audio equipment to enhance the listening experience by allowing users to tailor the sound to their preferences.
```

considerable attenuation (about −20dB) introduced by the passive network, and to provide true bass and treble boost. There are still many variants of the circuit in use, both as active circuits (with amplification as originally proposed), and as passive networks without an incorporated amplifier. In passive variants of the Baxandall circuit, extra stages of amplification may be used to make up for the approximately −20bB attenuation caused by the circuit.

Read the original 1952 paper "Negative-Feedback Tone Control" by P. J. Baxandall B.Sc.(Eng.) published in "Wireless World" (Now Electronics World)

#### How the Baxandall Circuit Works.

With bass and treble controls set to maximum boost (both wipers at the top of resistors VR1 and VR2), and the inactive components greyed out, the circuit will look like Fig. 4.2.3. Both bass and treble potentiometers that may have either linear or logarithmic tracks depending on the circuit design, are much higher values than other components in the circuit, and so with the VR1 and VR2 wipers set to maximum resistance both potentiometers can be considered to be open circuit. Nor does C4

Here is the image describtion:
```
The image is a schematic diagram of a tone control circuit, specifically designed for bass and treble adjustment. Here is a detailed description of the components and their connections:

1. **Input and Output:**
   - The circuit has an input terminal on the left side and an output terminal on the right side.

2. **Resistors:**
   - **R1**: 10K ohms, connected between the input terminal and a junction point that leads to the rest of the circuit.
   - **R2**: 1K ohms, connected between the junction point of C2 and ground (0V).
   - **R3**: 10K ohms, connected between the junction point of C2 and the output terminal.

3. **Capacitors:**
   - **C1**: 22nF (nanofarads), connected in series with the variable resistor VR1 (Bass control).
   - **C2**: 220nF, connected between the junction point of R1 and R2 and ground.
   - **C3**: 2.2nF, connected in series with the variable resistor VR2 (Treble control).
   - **C4**: 22nF, connected in parallel with VR2 and C3.

4. **Variable Resistors (Potentiometers):**
   - **VR1**: 100K ohms, labeled as "Bass," connected in series with C1 and between the input and the junction point of R1 and C2.
   - **VR2**: 100K ohms, labeled as "Treble," connected in series with C3 and between the output and the junction point of R3 and C4.

5. **Ground Connections:**
   - The circuit has multiple ground (0V) connections, ensuring proper grounding for the components.

6. **Signal Path:**
   - The input signal passes through R1 and splits into two paths: one through C1 and VR1 (Bass control) and the other through C2 and R2 to ground.
   - The signal then combines at the junction point of R2 and R3, passing through R3 to the output.
   - The treble control (VR2 and C3) is connected in parallel with the output, allowing adjustment of high frequencies.

This circuit allows for the adjustment of bass and treble frequencies in an audio signal, providing a means to boost or cut these frequencies as desired.
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
The image is a schematic diagram of an electronic circuit, specifically a tone control circuit. Here is a detailed description of the components and their connections:

1. **Input and Output:**
   - The circuit has an input terminal on the left side labeled "Input."
   - The output terminal is on the right side labeled "Output."

2. **Resistors:**
   - There are three resistors in the circuit:
     - R1: 10K ohms, connected between the input and the junction of C1 and R2.
     - R2: 1K ohms, connected between the junction of C1 and R1 and ground (0V).
     - R3: 10K ohms, connected between the junction of C1 and R2 and the output.

3. **Capacitors:**
   - There are four capacitors in the circuit:
     - C1: 22nF (nanofarads), connected between the junction of R1 and R2 and the junction of R3 and C4.
     - C2: 220nF, shown in a faded color, indicating it might be optional or part of a different configuration.
     - C3: 2.2nF, also shown in a faded color, indicating it might be optional or part of a different configuration.
     - C4: 22nF, connected between the junction of R3 and the output and ground (0V).

4. **Potentiometers:**
   - There are two potentiometers shown in faded color, indicating they might be optional or part of a different configuration:
     - VR1: 100K ohms, labeled "Bass," connected in parallel with C2.
     - VR2: 100K ohms, labeled "Treble," connected in parallel with C3.

5. **Ground:**
   - The circuit has a ground connection labeled "Gnd" at the bottom center, connected to the 0V line.

The circuit is designed to control the tone of an audio signal, with the potentiometers VR1 and VR2 allowing adjustment of bass and treble frequencies, respectively. The resistors and capacitors form a network that filters the audio signal to achieve the desired tone control.
```

**Fig. 4.2.4 The Circuit with VR1 and VR2 at Minimum**

Here is the image describtion:
```
The image is a graph that displays the frequency response curves for different audio equalization settings. The x-axis represents frequency in Hertz (Hz), ranging from 10 Hz to 20,000 Hz (20K Hz), while the y-axis represents attenuation in decibels (dB), ranging from -50 dB to 0 dB.

There are four distinct curves on the graph, each representing a different equalization setting:

1. **Bass Boost (Red Curve)**: This curve starts at 0 dB attenuation at the lowest frequencies (around 10 Hz) and gradually decreases to around -20 dB attenuation as the frequency increases to around 1K Hz. It then continues to decrease further, reaching around -40 dB attenuation at the highest frequencies (20K Hz). This curve indicates an increase in the bass frequencies while attenuating the higher frequencies.

2. **Treble Boost (Red Curve)**: This curve starts at around -40 dB attenuation at the lowest frequencies (10 Hz) and gradually increases to around -20 dB attenuation as the frequency increases to around 1K Hz. It then continues to increase further, reaching 0 dB attenuation at the highest frequencies (20K Hz). This curve indicates an increase in the treble frequencies while attenuating the lower frequencies.

3. **Level Response (Blue Curve)**: This curve remains relatively flat across the entire frequency range, maintaining a consistent attenuation of around -20 dB from 10 Hz to 20K Hz. This curve represents a neutral or flat response, where no specific frequency range is boosted or cut.

4. **Bass Cut (Green Curve)**: This curve starts at around -40 dB attenuation at the lowest frequencies (10 Hz) and gradually increases to around -20 dB attenuation as the frequency increases to around 1K Hz. It then continues to increase further, reaching 0 dB attenuation at the highest frequencies (20K Hz). This curve indicates a reduction in the bass frequencies while maintaining the higher frequencies.

5. **Treble Cut (Green Curve)**: This curve starts at 0 dB attenuation at the lowest frequencies (10 Hz) and gradually decreases to around -20 dB attenuation as the frequency increases to around 1K Hz. It then continues to decrease further, reaching around -40 dB attenuation at the highest frequencies (20K Hz). This curve indicates a reduction in the treble frequencies while maintaining the lower frequencies.

Overall, the graph illustrates how different equalization settings can affect the frequency response of an audio signal, either by boosting or cutting specific frequency ranges.
```

Here is the image describtion:
```
The image is a text label that reads "Fig. 4.2.5 The Baxandall Modified Response Curve." The text is in a bold, black font and appears to be a caption or title for a figure in a document, likely a technical or academic paper. The figure number "4.2.5" suggests that it is part of a larger section or chapter, specifically the fourth chapter or section, and it is the fifth figure within the second subsection. The content of the figure itself is not visible in the image, only the caption is shown.
```

Here is the image describtion:
```
The image is a schematic diagram of a tone control circuit using an operational amplifier (op-amp). Here is a detailed description of the components and their connections:

1. **Input Section:**
   - The input signal enters the circuit through a capacitor labeled C5 with a value of 10µF. This capacitor is polarized, with the positive side connected to the input signal and the negative side connected to the rest of the circuit.

2. **Bass Control:**
   - A variable resistor (potentiometer) labeled VR1 with a value of 100K ohms is used for bass control.
   - Resistors R1 (10K ohms) and R2 (12K ohms) are connected in series with capacitors C1 (22nF) and C2 (220nF) to form a network that interacts with VR1 to adjust the bass frequencies.

3. **Treble Control:**
   - Another variable resistor (potentiometer) labeled VR2 with a value of 100K ohms is used for treble control.
   - Resistors R3 (10K ohms) and R4 (4.7K ohms) are connected in series with capacitors C3 (2.2nF) and C4 (22nF) to form a network that interacts with VR2 to adjust the treble frequencies.

4. **Operational Amplifier (Op-amp):**
   - The op-amp is the central component of the circuit, with its inverting input (-) connected to the tone control network and its non-inverting input (+) connected to ground through a capacitor labeled C6 with a value of 47µF.
   - The op-amp is powered by a positive voltage supply connected to its positive power pin and a ground connection to its negative power pin.

5. **Feedback Network:**
   - A resistor labeled R5 with a value of 100K ohms is connected between the output of the op-amp and its inverting input (-).
   - Another resistor labeled R6 with a value of 100K ohms is connected between the inverting input (-) and the junction of the tone control network.

6. **Output Section:**
   - The output of the op-amp is connected to the output terminal through a capacitor labeled C7 with a value of 10µF. This capacitor is also polarized, with the positive side connected to the op-amp output and the negative side connected to the output terminal.

7. **Ground Connections:**
   - The circuit has multiple ground connections, indicated by the 0V labels, ensuring proper grounding and stability of the circuit.

Overall, this circuit is designed to allow the user to adjust the bass and treble frequencies of an audio signal using the variable resistors VR1 and VR2, with the op-amp providing amplification and buffering of the signal.
```

Here is the image describtion:
```
The image is a caption or label for a figure, specifically "Fig. 4.2.6." The description indicates that the figure is about an active tone control circuit. This circuit uses a Baxandall network and an operational amplifier (op-amp) with negative feedback (NFB). The Baxandall network is a type of tone control circuit commonly used in audio applications to adjust bass and treble frequencies. The use of an op-amp with negative feedback suggests that the circuit is designed to provide stable and precise control over the audio signal's frequency response.
```

With active circuits such as that shown in Fig. 4.2.6 the aim is to have the level response at 0dB so there is no gain and no loss due to the tone control circuit. The maximum amount of boost possible should not be sufficient to overload any stage following the tone control if distortion is to be avoided. The design of such control circuits is usually therefore, an integral part of the overall design of an amplifier system.

#### Tone Control ICs

In modern amplifiers the tendency is to use integrated circuit controls that may be operated by either digital or analogue circuitry. A simple solution for bass, treble, balance and volume control in analogue stereo amplifiers is offered by such chips as the LM1036 from Texas Instruments.

The block diagram and an application circuit is shown in Fig. 4.2.7. Each of the four controls is adjusted by applying a variable voltage of between 5.4V (which is supplied by pin 17 of the IC), and 0V. Half the voltage applied to the control pins 4, 9, 12 and 14 gives a level frequency response, central balance between left and right channels, and half volume.

The LM1036 also has provision for a loudness compensation switch. When 'on' this changes the action of the controls to boost the bass and treble frequencies when the volume is at a low setting. The purpose of this is to compensate for the fall off in the function of human hearing at high and low frequencies with quiet sounds.

Here is the image describtion:
```
The image consists of two main sections: a pin configuration diagram for a Dual-In-Line (DIP) and Small Outline (SO) package, and a detailed circuit diagram for an audio control IC, specifically the LM1036N.

### Pin Configuration Diagram:
- **Top View of the IC Package:**
  - The IC has 20 pins, with pin 1 starting at the top left and pin 20 at the top right.
  - The left side (pins 1 to 10) and the right side (pins 11 to 20) are labeled with their respective functions.

#### Left Side (Pins 1 to 10):
1. **Internal Supply Decouple**
2. **Input 1**
3. **Treble Capacitor 1**
4. **Treble Control Input**
5. **AC Bypass 1**
6. **Bass Capacitor 1**
7. **Loudness Compensation Control Input**
8. **Output 1**
9. **Balance Control Input**
10. **GND (Ground)**

#### Right Side (Pins 11 to 20):
11. **Vcc (Power Supply)**
12. **Volume Control Input**
13. **Output 2**
14. **Bass Control Input**
15. **Bass Capacitor 2**
16. **AC Bypass 2**
17. **Zener Voltage**
18. **Treble Capacitor 2**
19. **Input 2**
20. **GND (Ground)**

### Circuit Diagram:
- **Central Component:**
  - The central component is the LM1036N IC, which is a tone and volume control IC.
  - The IC is connected to various external components such as capacitors, resistors, and potentiometers.

#### Key Connections:
- **Inputs:**
  - Input 1 (pin 2) and Input 2 (pin 19) are connected to capacitors (0.47 µF and 0.01 µF respectively) and grounded.
  
- **Treble Control:**
  - Treble Capacitor 1 (pin 3) and Treble Capacitor 2 (pin 18) are connected to capacitors (10 pF each).
  - Treble Control Input (pin 4) is connected to a potentiometer for treble adjustment.

- **Bass Control:**
  - Bass Capacitor 1 (pin 6) and Bass Capacitor 2 (pin 15) are connected to capacitors (0.39 µF each).
  - Bass Control Input (pin 14) is connected to a potentiometer for bass adjustment.

- **Volume and Balance Control:**
  - Volume Control Input (pin 12) is connected to a potentiometer for volume adjustment.
  - Balance Control Input (pin 9) is connected to a potentiometer for balance adjustment.

- **Loudness Compensation:**
  - Loudness Compensation Control Input (pin 7) is connected to a switch for enabling/disabling loudness compensation.

- **Outputs:**
  - Output 1 (pin 8) and Output 2 (pin 13) are connected to capacitors (0.22 µF each) and resistors (47k ohms each).

- **Power Supply:**
  - Vcc (pin 11) is connected to a capacitor (10 nF) and the power supply.
  - Ground (pins 10 and 20) are connected to the ground.

- **Additional Components:**
  - Various capacitors and resistors are used for filtering and stabilization purposes.

Overall, the image provides a comprehensive view of the pin configuration and the detailed circuit connections for the LM1036N audio control IC, illustrating how it can be used to control treble, bass, volume, and balance in an audio system.
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
The image is a composite of electronic components and a schematic overlay. The background consists of various electronic parts, including a speaker, a microphone, a jack plug, and other miscellaneous components like resistors and capacitors. These components are arranged in a somewhat cluttered manner, giving the impression of a collection of parts typically found in an electronics workshop or a DIY project.

Superimposed on this background is a green schematic diagram. The diagram features a transistor symbol at its center, with connections indicating the flow of current through the circuit. The transistor is depicted with its three terminals: the base, collector, and emitter. The schematic also includes symbols for resistors and capacitors, which are connected to the transistor in a typical amplifier configuration.

The labels "Zin" and "Zout" are present, indicating the input and output impedances of the circuit. "Zin" is located near the microphone, suggesting it is the input to the circuit, while "Zout" is near the jack plug, indicating the output. The green lines of the schematic overlay connect these components, visually integrating the real-world parts with their symbolic representations in the circuit diagram.

Overall, the image effectively combines the physical components of an electronic circuit with their corresponding schematic symbols, providing a visual representation of how these parts are interconnected in an actual electronic device.
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
The image is a schematic diagram of an audio preamplifier circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a +12V DC supply.

2. **Transistors:**
   - There are two transistors in the circuit:
     - Tr1: 2N3819 (a JFET transistor)
     - Tr2: BC178 (a PNP bipolar junction transistor)

3. **Resistors:**
   - R1: 2.2MΩ (2.2 Megaohms)
   - R2: 8.2kΩ (8.2 Kilohms)
   - R3: 18kΩ (18 Kilohms)
   - R4: 120Ω (120 Ohms)
   - R5: 1.2kΩ (1.2 Kilohms)
   - R6: 10Ω (10 Ohms)

4. **Capacitors:**
   - C1: 0.47µF (microfarads)
   - C2: 10µF (microfarads)
   - C3: 100µF (microfarads)
   - C4: 4.7µF (microfarads)

5. **Variable Resistor:**
   - VR1: 10kΩ (10 Kilohms) potentiometer, labeled as "Volume"

6. **Connections:**
   - The input signal is connected to the gate of Tr1 through capacitor C1.
   - The source of Tr1 is connected to ground through resistor R4 and capacitor C2 in parallel.
   - The drain of Tr1 is connected to the base of Tr2 through resistor R2.
   - The collector of Tr2 is connected to the +12V supply through resistor R6 and capacitor C3 in parallel.
   - The emitter of Tr2 is connected to ground through resistor R5.
   - The output signal is taken from the emitter of Tr2 through capacitor C4 and the potentiometer VR1, which is used to adjust the volume.

7. **Ground:**
   - The circuit has a common ground (0V) connection.

This preamplifier circuit amplifies the input audio signal and allows for volume control through the potentiometer VR1. The capacitors are used for coupling and bypassing purposes, ensuring proper signal flow and stability.
```

**Fig. 4.3.2 High Impedance JFET Input Stage** 

#### Operation

Because the input resistance of the JFET is extremely high, the input impedance of the circuit is approximately the value of R1, and as practically no current is flowing into the input, there is no potential across R1, therefore the gate of Tr1 is effectively at zero volts. To operate correctly, the gate of the N channel JFET must be more negative than the source, this is achieved by making the source of Tr1 positive. The signal applied to the gate will then vary the gate voltage and so vary the drain current through the JFET. The biasing of the JFET is set by R2 and R3. As JFET gain is not particularly high, extra gain is provided by the PNP transistor Tr2. The overall gain of the two-stage amplifier is set at approximately 11 by the negative feedback provided by R4 and R5.

#### Decoupling

In Fig 4.3.2, R3 is decoupled by C2 so that the bottom end of R4 is effectively at ground potential as far as AC is concerned, the value of C2 is not particularly large in this circuit, as the larger the value of electrolytic capacitor the more noise it will produce, and the aim of the circuit is to keep internally generated noise to a minimum. C1 and C4 coupling capacitors, (also relatively small values) provide isolation from any DC

Here is the image describtion:
```
The image is a schematic diagram illustrating a supply decoupling circuit, which is used to filter out AC noise from a DC power supply. The diagram includes the following components and labels:

1. **DC Supply with AC Noise**: This is the input power source that provides DC voltage but also contains unwanted AC noise.

2. **R6**: This is a resistor connected in series with the DC supply. The resistor helps to limit the current and works in conjunction with the capacitor to filter out the AC noise.

3. **C3**: This is a capacitor connected between the node after the resistor R6 and ground. The capacitor is designed to have a very low impedance (approximately 0 ohms) at the frequency of the AC noise, effectively shorting the AC noise to ground while allowing the DC component to pass through.

4. **DC Only to Circuit**: This label indicates the output of the decoupling circuit, which is the filtered DC voltage with the AC noise removed, supplied to the rest of the circuit.

The purpose of this supply decoupling circuit is to ensure that the DC voltage supplied to the circuit is clean and free from AC noise, which can interfere with the proper operation of electronic components. The combination of the resistor and capacitor forms a low-pass filter that attenuates high-frequency noise.
```

**(From Fig 4.3.2)** 

voltages present on any connected circuits. Using a very high value for R1 produces a high input impedance but the higher the value, the more prone the circuit will be to instability and oscillation. To prevent this possibility, effective decoupling from other circuits and the supply is necessary, decoupling here is provided by R6 and C3 as shown in Fig. 4.3.3.

Common emitter amplifiers generally have a medium to high output impedance, the value depending mainly on the value of load resistor in the final stage of amplification. Many typical transducers, such as loudspeakers, relays, motors etc. are inductive devices having a low impedance of only a few ohms.

Connecting such devices to the output of a voltage amplifier with a load resistance of several thousand ohms will result in poor impedance matching with practically the whole of the output being developed across the load resistor instead of across the load. One answer to this problem is to reduce the output impedance by using an emitter follower, which is a single transistor connected in common collector mode.

Here is the image describtion:
```
The image depicts a common collector transistor amplifier circuit, also known as an emitter follower. Here is a detailed description of the circuit components and their connections:

1. **Transistor**: The central component is an NPN bipolar junction transistor (BJT). The transistor has three terminals: the collector (top terminal), the base (left terminal), and the emitter (right terminal).

2. **Resistors**: 
   - **R1**: This resistor is connected between the base of the transistor and the positive supply voltage (Vcc) at the top of the circuit.
   - **R2**: This resistor is connected between the emitter of the transistor and ground (the bottom line of the circuit).

3. **Capacitor (C1)**: This capacitor is connected in series with the input signal. One end of the capacitor is connected to the input signal source, and the other end is connected to the base of the transistor.

4. **Connections**:
   - The **input signal** is applied to the base of the transistor through the capacitor C1.
   - The **output signal** is taken from the emitter of the transistor.
   - The collector of the transistor is directly connected to the positive supply voltage (Vcc).
   - The emitter is connected to ground through the resistor R2.

5. **Power Supply**: The circuit is powered by a DC voltage source connected between the top line (positive supply voltage, Vcc) and the bottom line (ground).

6. **Labels**: The image is labeled as "Fig. 4.3.4 Common Collector," indicating that this is a common collector configuration.

In this configuration, the input signal is applied to the base, and the output is taken from the emitter. The common collector amplifier is known for its high input impedance, low output impedance, and a voltage gain of approximately 1, making it suitable for impedance matching and buffering applications.
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
The image depicts a simple voltage regulator circuit using an NPN transistor in an emitter follower configuration. Here is a detailed description of the circuit components and their connections:

1. **Power Supply**:
   - The circuit is powered by a +12V unregulated supply, which is connected to the top of the circuit.

2. **Resistor (R1)**:
   - A resistor labeled R1 is connected between the +12V unregulated supply and the base of the NPN transistor. This resistor is used to limit the current flowing into the base of the transistor.

3. **Zener Diode**:
   - A Zener diode with a breakdown voltage of 5.6V is connected in reverse bias between the base of the transistor and ground (0V). The cathode of the Zener diode is connected to the base of the transistor, and the anode is connected to ground. The Zener diode is used to provide a stable reference voltage to the base of the transistor.

4. **NPN Transistor**:
   - The NPN transistor is the main active component in this circuit. The collector of the transistor is connected to the +12V unregulated supply, the base is connected to the junction of R1 and the Zener diode, and the emitter is connected to the load.

5. **Load**:
   - The load is connected between the emitter of the transistor and ground. The voltage across the load is the regulated output voltage of the circuit.

6. **Output Voltage**:
   - The regulated output voltage is labeled as +5V, which is the voltage across the load. This voltage is slightly less than the Zener diode voltage due to the base-emitter voltage drop (typically around 0.6V to 0.7V) of the transistor.

**Operation**:
- The +12V unregulated supply provides power to the circuit.
- The Zener diode maintains a constant voltage of 5.6V at the base of the transistor.
- The transistor's emitter voltage will be approximately 0.6V to 0.7V less than the base voltage due to the base-emitter junction voltage drop, resulting in an output voltage of around 5V.
- The emitter follower configuration ensures that the output voltage is regulated and stable, providing a constant +5V regulated supply to the load.

This circuit is commonly used to provide a stable and regulated voltage output from an unregulated power supply.
```

Notice in Fig.4.3.5 that the Zener diode has a voltage rating of 5V6 (meaning 5.6volts), this will maintain the base of the transistor at that voltage, and the emitter of the transistor at 0.6V below the base voltage, will be maintained at 5 volts. A small current maintaining the base voltage at 5.6V is therefore able to accurately control a much larger current flowing through the collector and emitter.

The emitter follower circuit is also the basis of many push-pull class B and class AB power output amplifier stages described in Amplifiers Module 5

#### The Darlington Pair

The effect of a high input impedance is to reduce the input current to the amplifier. If the input current for a given input voltage is reduced by whatever method, the effect is to increase the input impedance. The emitter follower has a high input impedance, but this may be reduced to an unacceptable level by the presence of the base bias resistor.

However another circuit, the compound or Darlington pair shown in Fig. 4.3.6 can greatly increase input impedance. By using one emitter follower (Tr1) to drive another (Tr2) the overall current gain becomes the product of the individual gains, hfe1 x hfe2 and can be typically 1000 or more. This greatly reduces the signal current required by the base of Tr1 and thereby dramatically increases the input impedance.

Here is the image describtion:
```
The image contains a block of text discussing the use of Darlington pairs in electronic circuits. It mentions that Darlington pairs can be used in common emitter mode, as illustrated in a figure referenced as Fig. 4.3.7. The text also states that Darlington transistors are available in combined packages for both PNP and NPN types. These packages often include back electromotive force (emf) protection diodes, which are typically necessary when the Darlington configuration is employed as a high current gain output device for switching high current inductive loads.
```

Here is the image describtion:
```
The image depicts a two-stage transistor amplifier circuit. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - The circuit is powered by a DC voltage source labeled as +Vcc at the top of the diagram.
   - The ground (0V) is at the bottom of the diagram.

2. **Input Stage:**
   - The input signal is fed into the circuit through a capacitor labeled C1. This capacitor is used for coupling the AC input signal while blocking any DC component.
   - The input signal then goes to the base of the first transistor, labeled Tr1.

3. **First Transistor Stage (Tr1):**
   - Tr1 is an NPN transistor.
   - The base of Tr1 is connected to the input signal through capacitor C1.
   - The collector of Tr1 is connected to the +Vcc supply through a resistor labeled R1.
   - The emitter of Tr1 is connected to the ground (0V).

4. **Second Transistor Stage (Tr2):**
   - Tr2 is another NPN transistor.
   - The base of Tr2 is connected to the collector of Tr1, forming a direct coupling between the two transistors.
   - The collector of Tr2 is connected directly to the +Vcc supply.
   - The emitter of Tr2 is connected to the ground (0V) through a resistor labeled R2.

5. **Output Stage:**
   - The output signal is taken from the emitter of Tr2.
   - The output is labeled as "Output" and is connected to the junction between the emitter of Tr2 and resistor R2.

**Functionality:**
- The input signal is amplified in two stages. The first stage is provided by Tr1, and the second stage is provided by Tr2.
- The coupling capacitor C1 ensures that only the AC component of the input signal is passed to the base of Tr1.
- The amplified signal from the collector of Tr1 is directly fed to the base of Tr2, which further amplifies the signal.
- The final amplified output is taken from the emitter of Tr2, which is connected to the ground through resistor R2.

This configuration is known as a two-stage amplifier, and it is commonly used to achieve higher gain by cascading two transistor amplifiers.
```

**Fig. 4.3.6 The Emitter Follower Converted to a Darlington Pair**

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage transistor amplifier circuit. Here is a detailed description of the components and their connections:

1. **Transistors (Tr1 and Tr2)**: The circuit includes two NPN bipolar junction transistors (BJTs), labeled as Tr1 and Tr2. These transistors are connected in a configuration that suggests a direct-coupled amplifier.

2. **Resistors (R1 and R2)**: 
   - **R1** is connected between the collector of Tr1 and the positive supply voltage (+Vcc).
   - **R2** is connected between the collector of Tr2 and the positive supply voltage (+Vcc).

3. **Capacitor (C1)**: 
   - **C1** is connected in series with the input signal. It serves as a coupling capacitor, blocking any DC component of the input signal and allowing only the AC component to pass through to the base of Tr1.

4. **Input and Output**:
   - The **Input** is applied to the left side of the circuit, before the capacitor C1.
   - The **Output** is taken from the collector of Tr2.

5. **Power Supply**:
   - The circuit is powered by a positive supply voltage labeled as +Vcc.
   - The ground (0V) is connected to the emitters of both transistors, indicating a common ground for the circuit.

6. **Connections**:
   - The base of Tr1 is connected to the input signal through capacitor C1.
   - The collector of Tr1 is connected to the positive supply voltage (+Vcc) through resistor R1.
   - The emitter of Tr1 is connected to ground (0V).
   - The collector of Tr1 is also directly connected to the base of Tr2.
   - The collector of Tr2 is connected to the positive supply voltage (+Vcc) through resistor R2.
   - The emitter of Tr2 is connected to ground (0V).
   - The output signal is taken from the collector of Tr2.

This configuration is typical for a two-stage amplifier where the first transistor amplifies the input signal, and the second transistor further amplifies the signal. The direct coupling between the two transistors allows for a higher gain and better frequency response.
```

**Fig. 4.3.7 The Darlington Pair with Common Emitter Output**

Darlington amplifiers are also available in integrated circuit form, such as the ULN2803, which contains eight high current, Darlington amplifiers with open collector outputs, for interfacing between TTL (5V) logic circuits and high current/high voltage (up to 500mA and 50V) devices. When pin 10 is connected to +V each output is diode protected for driving inductive loads against back e.m.f.

#### Bootstrapping

Bootstrapping (Using positive feedback to feed part of the output back to the input, but without causing oscillation) is a method of apparently increasing the value of a fixed resistor as it appears to A.C. signals, and thereby increasing input impedance. A basic bootstrap amplifier is shown in Fig. 4.3.8 where capacitor CB is the 'Bootstrap Capacitor', which provides A.C. feedback to a resistor in series with the base. The value of CB will be large, about 10 x the lowest frequency handled x the value of the series resistor (10ƒminR3).

Here is the image describtion:
```
The image consists of two distinct diagrams, each labeled as "Fig. 4.3.8" but representing different electronic components and configurations.

1. **Top Diagram: The Darlington Integrated Circuit ULN2803**
   - This diagram shows the internal structure of the ULN2803 integrated circuit.
   - The ULN2803 is an 8-channel Darlington transistor array.
   - The diagram depicts 8 input pins on the top side, labeled "8 Inputs."
   - Corresponding to each input, there are 8 protected output pins on the bottom side, labeled "8 Protected Outputs."
   - Each input is connected to the base of a Darlington pair of transistors.
   - The emitters of all the transistors are connected to a common ground (0V).
   - The collectors of the transistors are connected to the output pins.
   - Each output is protected by a diode, which is connected between the output pin and a common positive voltage rail (+V).
   - The ULN2803 is labeled in the middle of the diagram.

2. **Bottom Diagram: Bootstrapping Applied**
   - This diagram illustrates a bootstrapping circuit applied to a transistor.
   - The circuit includes a transistor with its collector connected to the output.
   - The base of the transistor is connected to the input through a resistor labeled R1.
   - Another resistor, R3, is connected between the base and the collector of the transistor.
   - A capacitor, labeled C_B, is connected between the base and the output.
   - A resistor, R2, is connected between the base and ground.
   - The input signal is applied to the base of the transistor through R1.
   - The output is taken from the collector of the transistor.
   - The bootstrapping technique is used to improve the performance of the transistor circuit by providing positive feedback through the capacitor C_B.

Overall, the image provides a detailed view of the ULN2803 Darlington transistor array and a bootstrapping circuit applied to a transistor, highlighting the components and connections involved in each configuration.
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
The image appears to be a section of a document or a PDF file. The top part of the image shows a header with the text "AMPLIFIERS MODULE 04.PDF" on the left side. In the center, there is the number "13," which likely indicates the page number. On the right side, there is a copyright notice that reads "© E. COATES 2007 - 2012." The background is white, and the text is in black. The overall layout suggests that this is a technical or educational document related to amplifiers.
```

Here is the image describtion:
```
The image depicts a simple electronic circuit diagram. Here is a detailed description of the components and their arrangement:

1. **Input and Output**: The circuit has an input on the left side and an output on the right side.

2. **Capacitor (C1)**: The input signal first passes through a capacitor labeled C1. This capacitor is connected in series between the input and the rest of the circuit.

3. **Resistor (R1)**: After the capacitor, the signal encounters a resistor labeled R1. This resistor is connected in series with the capacitor.

4. **Variable Resistor (VR1)**: Below the resistor R1, there is a variable resistor (potentiometer) labeled VR1. The variable resistor is connected in parallel with the resistor R1. The wiper (adjustable part) of the variable resistor is connected to the ground (0V).

5. **Ground (0V)**: The bottom of the variable resistor VR1 is connected to the ground, which is marked as 0V.

6. **Figure Label**: The diagram is labeled as "Fig. 4.4.1".

The circuit appears to be a simple RC (resistor-capacitor) network with a variable resistor for adjusting the output signal. The capacitor C1 blocks any DC component of the input signal, allowing only the AC component to pass through. The combination of R1 and VR1 forms a voltage divider, which can be adjusted to vary the output signal level.
```

#### 6.

Which of the following features does the circuit illustrated in Fig. 4.4.2 possess?

- a) High voltage gain and very high input impedance.
- b) Low voltage gain and very high output impedance.
- c) High current gain and very high input impedance.
- d) Low current gain and very high output impedance.

Here is the image describtion:
```
The image depicts a schematic diagram of a two-stage transistor amplifier circuit. Here is a detailed description of the components and their connections:

1. **Transistors (Tr1 and Tr2)**: The circuit includes two NPN bipolar junction transistors (BJTs) labeled Tr1 and Tr2. These transistors are connected in a common-emitter configuration.

2. **Capacitor (C1)**: There is a capacitor labeled C1 connected to the input of the circuit. This capacitor is used for coupling the input signal to the base of the first transistor (Tr1) while blocking any DC component.

3. **Resistor (R1)**: A resistor labeled R1 is connected between the positive supply voltage (+Vcc) and the base of the first transistor (Tr1). This resistor provides the necessary biasing for the base of Tr1.

4. **Resistor (R2)**: Another resistor labeled R2 is connected between the emitter of the second transistor (Tr2) and ground (0V). This resistor is used for biasing and stabilizing the second transistor (Tr2).

5. **Power Supply (+Vcc)**: The circuit is powered by a DC voltage source labeled +Vcc. This supply is connected to the collector of both transistors (Tr1 and Tr2).

6. **Input and Output**: The input signal is applied to the left side of the circuit, where it passes through capacitor C1 to the base of Tr1. The output signal is taken from the emitter of the second transistor (Tr2) and is labeled as "Output."

7. **Ground (0V)**: The ground or 0V reference point is shown at the bottom of the circuit. It is connected to the emitter of Tr1 and one end of resistor R2.

The circuit operates as follows:
- The input signal is coupled through capacitor C1 to the base of Tr1.
- Tr1 amplifies the signal, and the amplified signal is then fed to the base of Tr2.
- Tr2 further amplifies the signal, and the final amplified output is taken from the emitter of Tr2.

This configuration is known as a two-stage amplifier, where each transistor stage provides amplification, resulting in a higher overall gain.
```

#### 7.

Refer to Fig 4.4.3. If the real value of R3 is 33KΩ and the open loop gain of the emitter follower amplifier (AO) is 0.98, what will be the apparent value R3B of R3 due to the bootstrapping

- a) 1.65MΩ
- b) b) 2.35MΩ
- c) c) 3.27MΩ
- d) d) 230.5KΩ

Now check your answers at:

http://www.learnabout-electronics.org/Amplifiers/amplifiers44.php