Here is the image describtion:
```
The image is a logo for Texas Instruments, a well-known technology company. The logo consists of two main elements: a graphic symbol and the company name.

1. **Graphic Symbol**: On the left side of the logo, there is a stylized representation of the state of Texas. Within this outline, there are the letters "T" and "I" arranged in a way that they overlap and integrate with the shape of Texas. The design is simple and modern, using clean lines and a monochromatic color scheme.

2. **Company Name**: To the right of the graphic symbol, the words "TEXAS INSTRUMENTS" are written in a bold, serif font. The text is in uppercase letters, which gives it a strong and professional appearance. The color of the text matches the graphic symbol, maintaining a cohesive look.

Overall, the logo is clean, professional, and easily recognizable, reflecting the company's long-standing reputation in the technology and electronics industry.
```

*Jaskaran Atwal*

[www.ti.com](https://www.ti.com)

## **Design Goals**

| Supply |     | Oscillator Frequency |
|--------|-----|----------------------|
| Vcc    | Vee | f                    |
| 5V     | 0V  | 1MHz                 |

#### **Design Description**

The oscillator circuit generates a square wave at a selected frequency. This is done by charging and discharging the capacitor, C1 through the resistor, R1. The oscillation frequency is determined by the RC time constant of R<sup>1</sup> and C1, and the threshold levels set by the resistor network of R2, R3, and R4. The maximum frequency of the oscillator is limited by the toggle rate of the comparator and the capacitance load at the output. This oscillator circuit is commonly used as a time reference or a supervisor clock source.

Here is the image describtion:
```
The image depicts an electronic circuit diagram featuring an operational amplifier (op-amp) configuration. Here is a detailed description of the components and their connections:

1. **Power Supply:**
   - A DC voltage source labeled as Vcc 5V is shown, providing the positive supply voltage (V+) to the circuit.

2. **Resistors:**
   - There are four resistors in the circuit:
     - R1 with a resistance of 6.8kΩ.
     - R2 with a resistance of 20kΩ.
     - R3 with a resistance of 20kΩ.
     - R4 with a resistance of 20kΩ.

3. **Capacitor:**
   - A capacitor labeled C1 with a capacitance of 100pF is connected in the circuit.

4. **Operational Amplifier:**
   - The op-amp used in the circuit is a TLV3201.
   - The non-inverting input (+) of the op-amp is connected to the junction of resistors R2 and R3.
   - The inverting input (-) of the op-amp is connected to the junction of resistor R1 and capacitor C1.
   - The output (Vo) of the op-amp is connected to one end of resistor R4.

5. **Connections:**
   - The positive supply voltage (V+) is connected to the top of resistors R2 and R4, and also to the positive power supply pin of the op-amp.
   - The other end of resistor R2 is connected to the non-inverting input (+) of the op-amp.
   - The other end of resistor R3 is connected to the ground.
   - The other end of resistor R4 is connected to the output (Vo) of the op-amp.
   - The other end of resistor R1 is connected to the inverting input (-) of the op-amp.
   - The other end of capacitor C1 is connected to the ground.
   - The node labeled Vc is connected to the junction of resistor R1 and capacitor C1.

This circuit appears to be a comparator or a similar configuration using the TLV3201 op-amp, with feedback and biasing resistors to set the operating point and behavior of the circuit.
```

#### **Design Notes**

- 1. Comparator toggle rate and output capacitance are critical considerations when designing a high-speed oscillator.
- 2. Select C1 to be large enough to minimize the errors caused by stray capacitance.
- 3. If using a ceramic capacitor, select a COG or NPO type for best stability over temperature.
- 4. Select lower value resistors for the R2, R3, R4 resistor network to minimize the effects of stray capacitance.
- 5. Adjust R2, R3, and R4 to create a duty cycle other than 50%.

## **Design Steps**

1. When R2 = R3 = R4, the resistor network sets the oscillator trip points of the non-inverting input at one-third and two-thirds of the supply.

Here is the image describtion:
```
The image is a logo for Texas Instruments, a well-known technology company. The logo consists of several elements:

1. **Icon**: On the left side, there is a red graphic that combines the letters "t" and "i" in a stylized manner. The letters are integrated into the shape of the state of Texas, which is also in red.

2. **Text**: To the right of the icon, the words "Texas Instruments" are written in a bold, black font. "Texas" is positioned above "Instruments," and both words are aligned to the left.

3. **Website**: Below the company name, the website URL "www.ti.com" is displayed in a smaller, black font.

The overall design is clean and professional, with a clear emphasis on the company's name and its association with the state of Texas.
```

2. When the output is high, the upper trip point is set at two-thirds of the supply to bring the output back low.

$$\mathbf{V\_o = V\_s(\frac{\mathcal{R\_3}}{(\mathcal{R\_2} \| \mathcal{R\_4}) + \mathcal{R\_3}}) = \frac{2}{3}\mathbf{V\_s = 3.33\mathbf{V}}$$

3. When the output is low, the lower trip point is set at one-third of the supply to bring the output back high.

$$\mathbf{V\_o} = \mathbf{V\_s} \left( \frac{\mathbf{R\_3} \| \mathbf{R\_4}}{(\mathbf{R\_3} \| \mathbf{R\_4}) + \mathbf{R\_2}} \right) = \frac{1}{3} \mathbf{V\_s} = 1.67 \mathbf{V}$$

4. The timing of the oscillation is controlled by the charging and discharging rate of the capacitor C1 through the resistor R1. This capacitor sets the voltage of the inverting input of the comparator. Calculate the time to discharge the capacitor.

Vc = Vi e ‐ t R1C1 1.67 3.33 = e ‐ t R1C1 t = 0.69R1C1

5. Calculate the time to charge the capacitor.

$$\begin{aligned} \mathbf{V\_{i}} &= \mathbf{V\_{c}} \left( \mathbf{1} \text{-e}^{\frac{\mathbf{t}}{\mathbf{RC}}} \right) \\\\ \mathbf{1.67} &= 3.33 \left( \mathbf{1} \text{-e}^{\frac{\mathbf{t}}{\mathbf{RC}}} \right) \\\\ \frac{1.67}{3.33} &= \text{e}^{\frac{\mathbf{t}}{\mathbf{RC}}} \\\\ \mathbf{t} &= 0.69 \mathbf{R\_{1}C\_{1}} \end{aligned}$$

6. The time for the capacitor to charge or discharge is given by 0.69R1C1. With a target oscillator frequency of 1 MHz, the time to charge or discharge should be 500ns.

0.69R1C1 = 500ns

R1C1 = 724ns

7. Select C1 as 100pF and R1 as 6.8kΩ (the closest real world value).

Here is the image describtion:
```
The image is a logo for Texas Instruments, a well-known technology company. The logo consists of a red graphic element on the left side, which is a stylized representation of the state of Texas with the letters "ti" integrated into it. To the right of the graphic, the words "TEXAS INSTRUMENTS" are written in a bold, black font. Below the company name, the website URL "www.ti.com" is displayed in a smaller, black font. The overall design is clean and professional, reflecting the company's branding.
```

# **Design Simulations**

### **Transient Simulation Results**

Here is the image describtion:
```
The image is a graph that displays two waveforms over a period of 5 seconds. The x-axis represents time in seconds, ranging from 0.00 to 5.00 seconds, while the y-axis represents the output, ranging from 0.00 to 5.00 units.

There are two distinct waveforms shown on the graph:

1. A green waveform that appears to be a square wave. This waveform alternates between a high value of 5.00 units and a low value of 0.00 units. The transitions between high and low values are very sharp, indicating a typical square wave pattern. The square wave has a period of approximately 1 second, meaning it completes one full cycle (high to low and back to high) every second.

2. A red waveform that appears to be a triangular wave. This waveform gradually increases from 0.00 units to a peak value of around 3.00 units and then decreases back to 0.00 units. The triangular wave has a period of approximately 1 second, similar to the square wave, but it has a more gradual rise and fall compared to the sharp transitions of the square wave.

The graph shows these two waveforms superimposed over each other, with the square wave maintaining a consistent high and low pattern, while the triangular wave smoothly oscillates between its peak and trough values.
```

#### **Design References**

See circuit spice simulation file, [SBOMAO3.](https://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=sbomao3&fileType=zip)

#### **Design Featured Comparator**

| TLV3201     |              |  |
|-------------|--------------|--|
| Vss         | 2.7V to 5.5V |  |
| VinCM       | Rail-to-rail |  |
| tpd         | 40ns         |  |
| Vos         | 1mV          |  |
| VHYS        | 1.2mV        |  |
| Iq          | 40µA         |  |
| Output Type | Push-Pull    |  |
| #Channels   | 1            |  |
| TLV3201     |              |  |

#### **Design Alternate Comparator**

| TLV7011     |              |  |
|-------------|--------------|--|
| Vss         | 1.6V to 5.5V |  |
| VinCM       | Rail-to-rail |  |
| tpd         | 260ns        |  |
| Vos         | 0.5V         |  |
| VHYS        | 4mV          |  |
| Iq          | 5µA          |  |
| Output Type | Push-Pull    |  |
| #Channels   | 1            |  |
| TLV7011     |              |  |

# **Trademarks**

All trademarks are the property of their respective owners.

Here is the image describtion:
```
The image features the logo and branding of Texas Instruments, a well-known technology company. On the right side of the image, there is a red logo that combines the letters "TI" with the shape of the state of Texas. To the right of the logo, the text "TEXAS INSTRUMENTS" is written in bold, black, uppercase letters. Below this text, the company's website "www.ti.com" is displayed in smaller, black text. On the left side of the image, the word "Trademarks" is written in italicized, black text. The background of the image is white, providing a clean and professional look.
```

# **IMPORTANT NOTICE AND DISCLAIMER**

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to [TI's Terms of Sale](https://www.ti.com/legal/terms-conditions/terms-of-sale.html) or other applicable terms available either on [ti.com](https://www.ti.com) or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2024, Texas Instruments Incorporated