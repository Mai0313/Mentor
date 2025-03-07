# Transactions Briefs

## **CMOS Schmitt** Trigger **Design**

#### I. **M.** Filanovsky and H. Bakes

*Abstnrct-CMOS* **Schmitt trigger design with given circuit thresholds is described. The approach is based on studying** *the* **transient from one stable state to another when the trigger is in linear operation. The trigger is subdivided into two subcircuits; each of them is considered as a passive load for** *the* **other. This allows the relations governing the deviations of the circuit thresholds from their given values to be obtained. The trigger device sizes are thus determined by the threshold tolerances.** 

#### I. INTRODUCTION

The CMOS Schmitt trigger [Fig. l(a)] is a well-known circuit. Yet, the design of this circuit has never been investigated in any detail. The circuit operation described in [I] gives a clue to some relationships between the device sizes in the circuit. However, the description is incomplete; it does not include the circuit behavior near the transition point from one stable state to another (it is simply stated that the transition is fast). **A** more detailed study given below introduces the additional relationships required to complete the design and choose all the device sizes.

In bipolar technology, p-n-p transistors are much slower than their n-p-n counterparts [2], and the bipolar prototype for the whole circuit of Fig. l(a) is not known. A bipolar Schmitt trigger includes an n-p-n differential pair loaded with a resistor. **As** a result, the circuit analysis is simplified, and one can find approximate *[3]-[5]* and exact [6]-[8] calculation of the threshold voltages of this reduced circuit.

Recently [9], the analysis of an NMOS Schmitt trigger with a linear resistive load was published. The circuit of Fig. I(a) includes two similar subcircuits **(MI,** Mz, **M3** and Mq, **Ms,** M6). Each of them is a highly nonlinear load for the other. However, as shown subsequently, at each transition point one subcircuit can be considered as a *linear* resistive load for the other. Then the approach of [9] becomes valid for the circuit of Fig. I(a) as well. The results of this analysis are given here. First, they are formulated **as** two equations relating the device sizes to given threshold voltages. Two additional equations describe the relation between the device parameters and the threshold voltage tolerances. Finally, two inequalities relating some specific currents of the subcircuits and providing some details of the trigger *U0* characteristic shape are given.

#### **11.** CURRENT-VOLTAGE SUBCIRCUIT CHARACTERISTICS

In the circuit of Fig. l(a), the bottom circuit MI, Mz, MS (which is called here the N-subcircuit), is loaded by the top circuit, Mq, **Ms,** Ms (P-subcircuit). **As** a result of the circuit symmetry, the inverse statement is also valid. To obtain the voltage-current characteristics of these nonlinear loads, one can take, for example, the N-subcircuit, apply a voltage source *V,* and calculate the source current I,, assuming a constant voltage *VG* at the gates of MI and *MZ* [Fig. 2(a)].

Manuscript received October 17, 1991; revised April 28, 1993. This paper was recommended by Associate Editor **W.** M. Dai.

I. M. Filanovsky is with the Department of Electrical Engineering, University of Alberta, Edmonton, Alberta, Canada.

H. Bakes is with ETH Hoenggerberg, Zurich, Switzerland. IEEE Log Number 921 1963.

Here is the image describtion:
```
The image consists of two parts labeled (a) and (b).

(a) The left part of the image is a schematic diagram of a CMOS circuit. The circuit includes six MOSFET transistors labeled M1, M2, M3, M4, M5, and M6. The transistors are arranged in a specific configuration to form a logic gate. The circuit also includes a current source labeled I0, and two voltage sources labeled VG and VDD. The output voltage is labeled VO. The transistors M1, M2, and M3 are connected in series, with M1 connected to ground. Transistors M4, M5, and M6 are also connected in series, with M6 connected to VDD. The gates of M1 and M4 are connected to VG, while the gates of M2 and M5 are connected to the output VO. The gate of M3 is connected to the source of M2, and the gate of M6 is connected to the source of M5.

(b) The right part of the image is a voltage transfer characteristic (VTC) curve. The graph plots the output voltage VO on the y-axis against the input voltage VG on the x-axis. The curve shows the relationship between the input and output voltages for the CMOS circuit. The graph includes several labeled points: VOL (output low voltage), VOH (output high voltage), VL (low input voltage threshold), VLi (input voltage at the lower transition point), VHi (input voltage at the higher transition point), and VH (high input voltage threshold). The curve indicates the regions where the output voltage transitions from high to low and vice versa as the input voltage varies from 0 to VDD. The dashed lines represent the ideal high and low output voltage levels (VOH and VOL), while the solid line represents the actual output voltage behavior.
```

Fig. *1.* CMOS Schmitt trigger and its transfer characteristic

Here is the image describtion:
```
The image consists of three parts labeled (a), (b), and (c).

(a) The first part is a circuit diagram. It includes three MOSFET transistors labeled M1, M2, and M3. The circuit is powered by a voltage source labeled V_DD. The gate of M1 is connected to a voltage source labeled V_G. The source of M1 is connected to the ground. The drain of M1 is connected to the source of M2. The gate of M2 is connected to the drain of M1. The drain of M2 is connected to the source of M3. The gate of M3 is connected to the drain of M2. The drain of M3 is connected to V_DD. There is a current source labeled I_O connected between the drain of M2 and the ground. The output voltage V_O is taken from the drain of M2.

(b) The second part is a graph showing the relationship between the output current I_O and the output voltage V_O. The x-axis represents the output voltage V_O, and the y-axis represents the output current I_O. The graph shows a piecewise linear relationship with different regions labeled V_OS, V_OT, V_OC, and V_DD. The current I_O starts at zero, increases linearly, reaches a constant value I_ON, and then decreases back to zero.

(c) The third part is another graph showing the relationship between the output current I_O and the output voltage V_O for a specific gate voltage V_G = V_H. The x-axis represents the output voltage V_O, and the y-axis represents the output current I_O. The graph shows two curves: one solid and one dashed. The solid curve represents the current I_O for the high gate voltage V_G = V_H, while the dashed curve represents the current I_O for a lower gate voltage. The graph shows regions labeled I_ONH, I_OPH, V_OL, and V_DD. The difference between the two curves is labeled as ΔI. The current I_O starts at zero, increases, reaches a peak, and then decreases back to zero.
```

Fig. 2. N-subcircuit driven by a voltage source: (a) circuit; (b) current-voltage characteristic; (c) superposition of N- and P-subcircuit characteristics.

When the voltage *V,* is very small, transistor **M3** will be *off,* and MI and MZ are in the triode mode of operation. The current I, is equal to

$$I\_o = 2k\_1(V\_G - V\_{TN})V\_N \tag{1}$$

if one considers transistor **Mi,** or

$$I\_o = 2k\_2(V\_G - V\_N - V\_{TN})(V\_o - V\_N) \tag{2}$$

if one considers **MS.** Here *k,* = *0.5(pL,C,,)(W/L),,* as usual [IO], and *VTN* is the threshold voltage of n-channel transistors. For pchannel transistors, one has to use *pLp* and *VTP.* It is assumed in (1) and (2) that *VG* > *VTN.* For the triode mode of operation, *VN* (< *VTN* and the last equation can be simplified to

$$I\_o = 2k\_2(V\_G - V\_{TN})(V\_o - \stackrel{\cdot}{V}\_N). \tag{3}$$

From **(1)** and (3), one obtains that

$$V\_N = V\_O \frac{k\_2}{k\_1 + k\_2} \tag{4}$$

$$I\_o = \frac{2k\_1k\_2(V\_G - V\_{TN})}{k\_1 + k\_2} V\_o. \tag{5}$$

1057-7122/94\$04.00 *0* 1994 IEEE

and

From (5) one can find that

$$R\_{LN} = \left[\frac{\partial I\_o}{\partial V\_o}\right]^{-1} = \frac{k\_1^{-1} + k\_2^{-1}}{2(V\_G - V\_{TN})}.\tag{6}$$

It is seen from (4) and (6) that, in this part of the subcircuit operation, transistors **M1** and **MZ** may be considered as a series connection of two resistors.

When *V,* increases, **M:!** enters into saturation (pinch-off). Then *I,*  is determined, depending on the considered transistor, or by

$$I\_o = 2k\_1[V\_G - V\_{TN} - (V\_N/2)]V\_N \tag{7}$$

or X

$$I\_o = k\_2 (V\_G - V\_N - V\_{TN})^2. \tag{8}$$

From (7) and (8) one can find that

$$I\_o = 2k\_1[V\_G - V\_{TN} - (V\_N/2)]V\_N\tag{7}$$

$$I\_o = k\_2(V\_G - V\_N - V\_{TN})^2.\tag{8}$$

(8) one can find that

$$V\_N = (V\_G - V\_{TN})\left(1 - \sqrt{\frac{k\_1}{k\_1 + k\_2}}\right)\tag{9}$$

$$\text{hence on } V\_G.\text{ This means (First, 201) that can be written}$$

and does not depend on *V,.* This means [Fig. 2(b)] that when the voltage *V,* achieves the value of

$$V\_{oS} = V\_G - V\_{TN} \tag{10}$$

the current I, becomes constant and equal to

$$I\_{oN} = \frac{k\_1 k\_2}{k\_1 + k\_2} (V\_G - V\_{TN})^2. \tag{11}$$

Yet, an additional increase of *V,* will gradually introduce some changes. When *V,* achieves the value of

$$V\_{\bullet T} = V\_G - (V\_G - V\_{TN})\sqrt{\frac{k\_1}{k\_1 + k\_2}}\tag{12}$$

then transistor **M3** will be turned on, *V.* starts to increase again, and the current *I,* is diminishing. When *V,* becomes equal to

$$V\_{oC} = V\_G + (V\_G - V\_{TN})\sqrt{k\_1/k\_3} \tag{13}$$

transistor **M2** will be completely turned off and I, becomes equal to zero. At this instant, voltage *VN* will be equal to *VG* - *VTN* and **MI**  is entering into saturation. Transistor **MI** cames the current

$$J\_N = k\_1 (V\_G - V\_{TN})^3 \tag{14}$$

which is completely intercepted by **M3.** Additional increase of 1: up to *VDD* does not bring any changes and completes the current-voltage characteristic of the N-subcircuit.

Now the design problem can be formulated graphically [Fig. 2(c)]. Assuming that the trigger transition from one stable state to another takes place when the gate voltage has a required threshold value (say, *VH),* and allowing a current AI to flow at this instant in the transistors **MI, Mz, M3,** and **M4,** one has to find and superimpose the current-voltage characteristics of the two subcircuits so that only one unstable intersection point exists. A similar condition is then applied for another transition point, characterized by another required threshold voltage *VL.* However, an attempt to obtain the device parameters from this direct approach gives an intractable system of nonlinear equations [the characteristics shown in Fig. 2(b) and (c) are simplifying approximations] and should be abandoned. Yet, the characteristics shown in Fig. 2(c) help to extend the approach [9] based on investigation of the trigger behavior near the transition point and to apply it to the circuit of Fig. l(a). In addition, these characteristics allow provision of two inequalities useful in the trigger design. Finally, they help to clarify some details observed in the experimental transfer characteristics [ 11.

#### **111. THRESHOLDS, TRANSITION, AND TRIGGER DESIGN**

As mentioned earlier, the operation of the **CMOS** Schmitt trigger is known [l]. We will follow this description, modifying and interrupting it at appropriate points to obtain the results necessary for trigger design.

Assume that the voltage *VG* in Fig. l(a) is zero. Then transistors **M1** and **Mz** are off. Transistors **M4** and **Ms** are in the linear mode of operation, but the voltage drop at each is zero because the current in **M4** and **Ms** is equal to the current in **M1** and **M:!.** The output voltage *V,* is equal to *VDD* (or *high).* Transistor **M3** is on (its drain and gate have the same voltage of *VDD)* but it also does not carry any current.

When *VG* rises above *VTN.* transistor **M1** turns on and starts to conduct. The current of **M1** is determined by (14). It is completely intercepted by **M3,** and the condition of the transistors in the Psubcircuit does not change. However, the potential *V,* is starting to decrease.

The trigger operation starts when the voltage *VG* arrives at the value of *VH~.* At this point, due to simultaneous increase of VG and decrease of **Kv,** transistor **Mz** turns on. It is not difficult to see that if in (13) one substitutes *VDD* instead of *V0c* (the gate of **M3** is still at *VDD)* and *VH~* instead of *VG,* one obtains the required relationship between the transistor parameters to start the triggering operation. It can be rewritten as

$$\frac{k\_1}{k\_3} = \left(\frac{V\_{DD} - V\_{Hi}}{V\_{Hi} - V\_{TN}}\right)^2. \tag{15}$$

By the same reasoning, one obtains that the condition

$$\frac{k\_4}{k\_6} = \left(\frac{V\_{Li}}{V\_{DD} - \dot{V}\_{Li} - |V\_{TP}|}\right)^2 \tag{16}$$

should be satisfied to start the triggering operation when the input voltage becomes equal to *VL~.* 

The voltages *VH~* and *VL~* are considered [l] as true thresholds of the **CMOS** Schmitt trigger. However, in effect, *VH~* and *VL~* mark only the beginning of the triggering operation. The real triggering [Fig. l(b)] occurs at close but different voltages *VH* and *VL.* The difference depends on choice of the parameters *kz* and *ks,* and can be estimated as follows.

The transition from one stable state to another in the Schmitt trigger is, indeed, very fast, and one can consider that during it the trigger input voltage does not change and stays at *VH* for the considered transition of the output voltage from *high* to *low.* When **M2** is turned on, the trigger starts to operate as a linear circuit with positive feedback. Transistors **M4** and **M5** are, in accordance with the P-subcircuit voltage-current characteristic, in a linear mode of operation, and the trigger can be represented as the linear circuit shown in Fig. 3(a). Transistor **MI** carries the current

$$I\_{NH} = k\_1 (V\_H - V\_{TN})^2 \approx k\_1 (V\_{Hi} - V\_{TN})^2. \tag{17}$$

The trigger load is

$$R\_{LP} = \frac{k\_4^{-1} + k\_5^{-1}}{2(V\_{DD} - V\_{Hi} - |V\_{TP}|)}\tag{18}$$

which is analogous to (6). The small-signal model for this part of trigger operation is shown in Fig. 3(b). The loop-transfer function for this circuit is

$$A\_L = \frac{g\_{m3} R\_{LP} (g\_{m2} r\_{o1} + 1)}{(g\_{m2} + g\_{m3}) r\_{o1} + 1}.\tag{19}$$

Here **T,,~** is the output impedance of **MI,** which, as follows from the previous operation, is operating in the saturation region. At the instant of the output voltage jump from *high* to *low,* this looptransfer

Here is the image describtion:
```
The image consists of two circuit diagrams labeled (a) and (b).

(a) The first diagram (a) shows a transistor circuit with three MOSFETs labeled M1, M2, and M3. The circuit is connected to a power supply voltage V_DD at the top. The source of M1 is connected to ground, and its gate is connected to a voltage source V_H. The drain of M1 is connected to the source of M2. The gate of M2 is connected to the drain of M1. The drain of M2 is connected to a resistor labeled R_LP, which is also connected to V_DD. The source of M3 is connected to the drain of M2, and its gate is connected to the same node. The drain of M3 is connected to another resistor labeled R_LP, which is also connected to V_DD. The output voltage V_O is taken from the drain of M3. The currents through the circuit are labeled as ΔI, NH, and NH - ΔI.

(b) The second diagram (b) is a small-signal equivalent circuit of the first diagram. It shows two dependent current sources, each represented by a circle with an arrow inside. The first current source is labeled g_m2 * v_gs2, and the second is labeled g_m3 * v_gs3. The voltage v_gs2 is applied between the gate and source of the first current source, and v_gs3 is applied between the gate and source of the second current source. The output voltage V_O is taken from the node where the two current sources meet. There is also a resistor labeled r_o1 connected to ground from the source of the first current source.

Overall, the image depicts a transistor circuit and its small-signal equivalent model, highlighting the relationships between the various components and the resulting output voltage.
```

Fig. 3. CMOS Schmitt trigger during transition: (a) equivalent circuit and (b) small-signal model.

function becomes equal to unity. Assuming **g-2~~1** >> 1 (which is usually satisfied), this gives the condition of transition

$$\frac{R\_{LP}}{(g\_{m2}^{-1} + g\_{m3}^{-1} + (r\_{o1}g\_{m2}g\_{m3})^{-1}} = 1.\tag{20}$$

The current of **MI** at this instant is divided between **M2** and **M3** into two parts *AI* and *INH* - *AI* so that the transconductance of the corresponding transistors are

$$g\_{m2} = 2\sqrt{\Delta I k\_2} \tag{21}$$

$$g\_{m3} = 2\sqrt{(\overline{I\_{NH} - \Delta I})k\_3} \approx 2\sqrt{I\_{NH}k\_3}.\tag{22}$$

The analysis shows that the last term in the denominator of (20) can be discarded as well and one can use the simplified transition condition

$$g\_{m2}^{-1} + g\_{m3}^{-1} \approx R\_{L,P.} \tag{23}$$

If (21) and (22) are substituted in (23), and (17) and (18) are used as well, then

$$
\Delta I = k\_2^{-1} \left[ \frac{k\_4^{-1} + k\_5^{-1}}{V\_{DD} - V\_{Hi} - |V\_{TP}|} - \frac{1}{(V\_{Hi} - V\_{TN})\sqrt{k\_1 k\_3}} \right]^{-2} \cdot \tag{24.37}
$$

This value depends on *k2* and **ks.** It allows one to estimate the difference between VH and *VH,.* Indeed, when the transition starts one has the input voltage of *VH,,* transistor **Mz** has zero current, transistor **M3** carries the current of *INH.* and the trigger output voltage is equal to *VDD.* Just before the output voltage jump, one has the input voltage of *VH,* transistor **M2** has the current of *AI,*  **M3** carries the current of *INN* - *AI,* and the output voltage drops to *VDD* - *AIRLP.* Using these conditions, it is easy to find that

$$
\Delta R\_{LP}.\text{ Using these conditions, it is easy to find that}
$$

$$
\Delta V\_H = V\_H - V\_{Hi} \approx \sqrt{\frac{\Delta I}{k\_2}} - \Delta IR\_{LP}.\tag{25}
$$

If transistor Ma is very wide one can use the approximation

$$
\Delta I \approx \frac{(V\_{DD} - V\_{Hi} - |V\_{TP}|)^2}{k\_2 (k\_4^{-1} + k\_5^{-1})^2}.\tag{26}
$$

Then, if in (25) the term *AIRLP* is neglected [indeed, it should be much less than *lVOs* 1 for the P-subcircuit, otherwise the model of Fig. 3(a) is not valid] and (26) is substituted in (25), one obtains

$$
\Delta V\_H \approx \frac{V\_{DD} - V\_{Hi} - |V\_{TP}|}{\frac{k\_2}{k\_4} + \frac{k\_2}{k\_4}}.\tag{27}
$$

Similarly, considering the transition of the output voltage from low to high, one finds that

$$
\Delta V\_L = V\_L - V\_{Li} \approx -\frac{V\_{Li} - V\_{TN}}{\frac{k\_5}{k\_2} + \frac{k\_5}{k\_1}}.\tag{28}
$$

The values given by (27) and (28) can be considered **as** the worst case deflections of the thresholds. It is seen from (27) and (28) that, to reduce *AVH* and *[AV,/,* the ratio *kz/ks* should be kept constant and each of **k2/k4** and **k5/kl** should be increased simultaneously.

Equations (17) and (18) together with (27) and (28) provide necessary information for the **CMOS** Schmitt trigger design. The exact values *VH* and *VL* of the threshold voltages are of paramount importance in all multivibrator applications of Schmitt triggers [11]-[13].

In the design practice, it is difficult to achieve P- and N- subcircuits with the shape of their voltage-current characteristics, as shown in Fig. 2(c) (for a given *VG* voltage). Usually (to reduce the value of *AI* for less power dissipation at high-frequency operation) one of them has the shape shown by the dotted line. In this case, one obtains the second stable intersection point of the voltage-current characteristics, and the output voltage after transition drops to *Vo~*  (in the opposite transition it will go to *Vo~).* This results in the experimentally observed [ 11 "tails" of the transfer characteristics [Fig. l(b)]. The output voltage arrives to zero value when the voltage *VG*  becomes close to the value of *VDD* - *~VTP* I (in the opposite transition it arrives to VDD when *VG* drops below *VTN).* To make the transfer characteristic more rectangular and reduce the tails (fortunately, one simultaneously reduces *AI* as well), the condition [Fig. 2(c)]

$$I\_{oPH} \ll I\_{oNH} \tag{29}$$

should be satisfied for the transition from high to low. The current io^^ in (29) can be calculated using (1 1) and *VH* as *VG.* This gives

$$I\_{oNH} \approx \left(\frac{k\_1 k\_2}{k\_1 + k\_2}\right) (V\_H - V\_{TN})^2 \tag{30}$$

and, in a similar way,

$$I\_{oPH} \approx \left(\frac{k\_5 k\_4}{k\_5 + k\_4}\right) (V\_{DD} - V\_H - |V\_{TP}|)^3. \tag{31}$$

Of course, near another transition point, the condition

$$I\_{oPL} \gg I\_{oNL} \tag{32}$$

should be satisfied. Here

$$I\_{oPL} \approx \left(\frac{k\_5 k\_4}{k\_5 + k\_4}\right) (V\_{DD} - V\_L - |V\_{TP}|)^2 \tag{33}$$

and

$$
\langle \cdots \rangle \sim \langle \cdots \rangle
$$

$$
I\_{oNL} \approx \left(\frac{k\_1 k\_2}{k\_1 + k\_2}\right) (V\_L - V\_{TN})^2. \tag{34}
$$

Conditions (29) and (32) are easily satisfied for the triggers with a wide loop of the transfer characteristic. However, it is difficult to satisfy them in the triggers of a narrow hysteresis loop.

#### **IV. EXAMPLE**

Assume that it is required to design a Schmitt trigger with the threshold values of *VH,* = 3.8 V and *VLI* = 1.8 V. The circuit should operate with *VDD* = 5 V. The circuit is realized in the **CMOS**  process with device transconductance parameters of *(pnC0,)/2* = *16.2 PAN'* and *(ppC0,)/2* = 7.2 *PAN'.* The device threshold voltages are *VTN* = 0.55 V and *~VTP~* = *0.60 V* (these process parameters are typical for **SACMOS** 3-p m process technology [14], and the example under discussion was designed as part of a humiditysensitive multivibrator realized in this technology).

Substituting the values of *VDD, VH;,* and *VTN* in (16), one finds that **k3/k1** = 7.33. If one takes *(W/L)1* = *(6/6),* where both the width and length are in microns, then one has to choose the closest rounded values of *(W/L)3* = *(44/6).* Notice that it is impossible

~

to choose the device MS of minimal geometry, as is suggested in **[l].** The chosen device geometries give **kl** = 16.2 *pAN2* and **k3** = 118.8 *PAN'.* 

Using the values of *VDD, VL~,* and *IC\$PI* one obtains from (17) that **k~/k4** = 2.09. If one takes **(W/L)4** = (14/6) (this gives **kq** = 16.8 *pAN2)* then **ks** = **35.1** *pAN2* and *(W/L)6* = (29/6).

If one takes **kz** = **3kl** = 48.6 *pAN2* and **ks** = **5k4** = <sup>84</sup> *pAN2* then one can take, for example, *(W/L)2* = (18/6) and *(W/L)s* = (70/6). Using the previously chosen device parameter values, one finds from (27) and (28) that **AVH** = 0.17 V and *AVL* = -0.18 V. Thus the trigger changes states at **1'H** = **3.97 <sup>V</sup>**and *VL* = 1.62 V, the values that are different from *VH~* and *VL~.*  The difference can be reduced if the width of the devices is increased. These results were verified using the ESPICE [ **151** simulation program and were observed later in experimental circuits.

Finally, one can find from (30) and (31) that *Io.w~* = 142.1 *pA*  and *Iop~* = 2.6 *pA.* Thus, (29) is satisfied. Similar calculations using (33) and **(34)** give *I0p~* = 108.2 *pA* and io^^ = **13.9 pA** and (32) is, hence, satisfied as well. The difference between *Iop~* and *Io"*  allows to see in simulations a small "tail" after the transition from low to high.

# v. CONCLUSIONS AND DISCUSSION

The design of a CMOS Schmitt trigger can be completed if the detailed circuit operation near the transition points is analyzed. This analysis gives true thresholds and allows one to evaluate the difference between the thresholds and the initial points of transitions (which are incorrectly considered and specified as thresholds). The voltage-current characteristics of the trigger subcircuits allow one to specify the conditions to make the trigger transfer characteristic more rectangular. The analysis is valid if the fabrication technology allows using the square-law characteristics of MOS devices.

#### REFERENCES

- D. A. Hodges and H. G. Jackson, *Analysis and Design of Digital Integrated Circuits.* New York: McGraw-Hill, 1983.
- P. R. Gray and R. G. Meyer, *Analysis and Design of Analog Integrated Circuits,* 2nd ed. New York: Wiley, 1984.
- J. G. Goaling, *Electronics: Models, Analysis and Systems.* New York: Marcel Dekker, 1982.
- H. Taub and D. Schilling, *Digital Integrated Electronics.* New York: McGraw-Hill, 1977.
- L. **Strauss,** *Wave Generation and Shaping.* New York: Wiley, 1970.
- H. U. Lauer, "Comments on 'Accurate determination of threshold levels of a Schmitt trigger,"' *IEEE Trans. Circ. Syst.,* vol. 34, pp. 1252-1253, 1987.
- *S.* C. Dutta Roy, "Comments on 'Accurate determination of threshold levels of a Schmitt trigger,' " IEEE *Trans. Circ. Syst.,* vol. CAS-33, pp. 734-735, 1986.
- C. J. F. Ridden, "Accurate determination of threshold levels of a Schmitt trigger," *IEEE Trans. Circ. Syst.,* vol. CAS-32, pp. 969-970, 1985.
- M. J. *S.* Smith, "On the circuit analysis of the Schmitt trigger," *IEEE*  J. *Solid-state Circ.,* vol. 23, pp. 292-294, 1988.
- R. Gregorian and G. C. Temes, *Analog MOS Integrated Circuits for Signal Processing.*  New York: Wiley, 1986.
- J. F. Kukielka and R. G. Meyer, "A high-frequency temperature-stable monolithic VCO," *IEEE* J. *Solid-state Circ.,* vol. SC-16, pp. 639-647, 1981.
- I. M. Filanovsky and I. G. Finvers, "A simple nonsaturated CMOS multivibrator," IEEE J. *Solid-state Circ.,* vol. 23, pp. 289-292, 1988.
- I. M. Filanovsky, "Stability of oscillation frequency of ECL-based multivibrator," *Int. J. Electronics,* vol. 68, pp. 829-837, 1990.
- C. Bleiker, "Electrical parameters of the SAC3 LVLVNV processes," Faselec Technical Note FZV-3- **10-5** 11646, Faselec AG, Zurich, 1988.
- *ESPICE Reference Manual,* Philips Co., Delft, The Netherlands, 1989.

# **An Analytical Model for the Transient Response of CMOS Class** AB **Operational Amplifiers**

Dima D. Shulman and Jian Yang

**Abstruct4n analytical study of the transient response of a CMOS class**  *AB* **opamp operating in a voltage follower configuration is presented. As with class A opamps, we identify nonlinear and linear regions of operation corresponding to slewing and settling periods in the transient response. But in contrast with class** *A* **opamps, it is shown that the feedback configuration should be considered for the entire duration of the transient response. It is shown that doublets (pole-zero pairs) have significant impact on the transient response of the class AB opamps in both nonlinear and linear regions of operation. One result is that in order to prevent overshoot in the transient response due to the doublets, the pole of the double should be located at a frequency higher than about four times the unity-gain bandwidth. The proposed analytical model is valid for any location of the doublets. It agrees well with the results of HSPICE computer simulations, and has the advantage over the latter of providing circuit designers with a clear relationship between the design goals and the device parameters.** 

#### I. INTRODUCTION

The period of time in which an opamp settles to a given percentage of the output voltage is one of its most important features. It consists of slewing and settling periods [l]. The minimization of each is necessary in order to achieve the optimal transient response. The slewing of an opamp is associated with its nonlinearities. In class **A** opamps, it is due to the limited supply of current to charge a compensation capacitor. The main feature of a class *AB* opamp, such as the one shown in Fig. **1,** is the ability to deliver a large output current during the transient *[2],* thus reducing slewing. For example, Castello and Gray analyzed a class *AB* opamp, whose output current changes **45** times from 2 *pA* in the steady-state to 90 *pA* peak value during the transient [3]. Nevertheless, class **AB** opamps exhibit slewing. This is because the drastic variations in the current during the transient are associated with nonlinearities of MOSFET's. In this paper, we investigate analytically the transient response of class **AB** opamps during the slewing and settling periods. We show that doublets (pole-zero pairs) affect the transient response significantly in the both periods. The effect of doublets in class **A** bipolar opamps was shown by Kamath *et* al. to degrade amplifier performance **[l].**  Kamath *et* al. have not discussed, however, the effect of doublets on the slewing period. But our earlier simulations of class *AB* opamps have shown that as a result of changing the doublet parameters, the shape of the voltage transient response during the slewing period is significantly modified **[4].** Furthermore, the analysis by Kamath *er*  al. was limited to the case of a closely spaced doublet inside the unity-gain bandwidth (UGB). This assumption is justified for bipolar opamps, in which doublets appear at low frequencies as a result of capacitive bypass of lateral p-n-p transistors having poor frequency response *[5].* In CMOS class **AB** opamps, doublets are caused by the level shifters that are biasing the input stage (see Fig. **1).** In CMOS technology, the frequency response of the level shifters can be changed by altering the biasing current and geometry of MOS

Manuscript received October 9, 1992; revised May 7, 1993. This work was supported in part by a grant from the Natural Sciences and Engineering Research Council of Canada. This paper was recommended by Associate Editor D. J. Allstot.

The authors are with the Department of Electrical Engineering, University of British Columbia, Vancouver, B.C., Canada V6T 124. IEEE Log Number 9210961.

## 0157-7122/94\$04.00 *0* 1994 IEEE