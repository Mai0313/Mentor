** Generated for: hspiceD
** Generated on: Dec 19 00:17:07 2024
** Design library name: TB_BGR
** Design cell name: tb_bgr_ref
** Design view name: schematic
.PARAM avss avdd


.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
+    HIER_DELIM=0
.LIB "/proj/phc_66061/cadence_test/TB_BGR/gpdk045_v_3_5/models/spectre/gpdk045.scs" mc

** Library name: BGR_Circuit
** Cell name: Opamp
** View name: schematic
.subckt Opamp avdd avss inm inp out
m8 out inp net4 avss g45n2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=6
m5 net3 inm net4 avss g45n2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=6
m2 net4 net1 avss avss g45n2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
m0 net1 net1 avss avss g45n2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
i3 net2 0 DC=10e-6
m14 net3 net3 avdd avdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
m11 net2 net2 avdd avdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
m13 net1 net2 avdd avdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
m12 out net3 avdd avdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=4
.ends Opamp
** End of subcircuit definition.

** Library name: gpdk045
** Cell name: resnsnpoly
** View name: schematic
.subckt resnsnpoly_pcell_0 b minus plus
r41 n41 minus b g45rnsnp w=segw l=segl
r40 n40 n41 b g45rnsnp w=segw l=segl
r39 n39 n40 b g45rnsnp w=segw l=segl
r38 n38 n39 b g45rnsnp w=segw l=segl
r37 n37 n38 b g45rnsnp w=segw l=segl
r36 n36 n37 b g45rnsnp w=segw l=segl
r35 n35 n36 b g45rnsnp w=segw l=segl
r34 n34 n35 b g45rnsnp w=segw l=segl
r33 n33 n34 b g45rnsnp w=segw l=segl
r32 n32 n33 b g45rnsnp w=segw l=segl
r31 n31 n32 b g45rnsnp w=segw l=segl
r30 n30 n31 b g45rnsnp w=segw l=segl
r29 n29 n30 b g45rnsnp w=segw l=segl
r28 n28 n29 b g45rnsnp w=segw l=segl
r27 n27 n28 b g45rnsnp w=segw l=segl
r26 n26 n27 b g45rnsnp w=segw l=segl
r25 n25 n26 b g45rnsnp w=segw l=segl
r24 n24 n25 b g45rnsnp w=segw l=segl
r23 n23 n24 b g45rnsnp w=segw l=segl
r22 n22 n23 b g45rnsnp w=segw l=segl
r21 n21 n22 b g45rnsnp w=segw l=segl
r20 n20 n21 b g45rnsnp w=segw l=segl
r19 n19 n20 b g45rnsnp w=segw l=segl
r18 n18 n19 b g45rnsnp w=segw l=segl
r17 n17 n18 b g45rnsnp w=segw l=segl
r16 n16 n17 b g45rnsnp w=segw l=segl
r15 n15 n16 b g45rnsnp w=segw l=segl
r14 n14 n15 b g45rnsnp w=segw l=segl
r13 n13 n14 b g45rnsnp w=segw l=segl
r12 n12 n13 b g45rnsnp w=segw l=segl
r11 n11 n12 b g45rnsnp w=segw l=segl
r10 n10 n11 b g45rnsnp w=segw l=segl
r9 n9 n10 b g45rnsnp w=segw l=segl
r8 n8 n9 b g45rnsnp w=segw l=segl
r7 n7 n8 b g45rnsnp w=segw l=segl
r6 n6 n7 b g45rnsnp w=segw l=segl
r5 n5 n6 b g45rnsnp w=segw l=segl
r4 n4 n5 b g45rnsnp w=segw l=segl
r3 n3 n4 b g45rnsnp w=segw l=segl
r2 n2 n3 b g45rnsnp w=segw l=segl
r1 n1 n2 b g45rnsnp w=segw l=segl
r0 plus n1 b g45rnsnp w=segw l=segl
.ends resnsnpoly_pcell_0
** End of subcircuit definition.

** Library name: gpdk045
** Cell name: resnsnpoly
** View name: schematic
.subckt resnsnpoly_pcell_1 b minus plus
r4 n4 minus b g45rnsnp w=segw l=segl
r3 n3 n4 b g45rnsnp w=segw l=segl
r2 n2 n3 b g45rnsnp w=segw l=segl
r1 n1 n2 b g45rnsnp w=segw l=segl
r0 plus n1 b g45rnsnp w=segw l=segl
.ends resnsnpoly_pcell_1
** End of subcircuit definition.

** Library name: BGR_Circuit
** Cell name: BGR_circuit
** View name: schematic
.subckt BGR_circuit v_bgr vdd vss
xi15 vdd vss inm inp net5 Opamp
q5 vss vss inp g45vpnp2 4 M=1
q4 vss vss net4 g45vpnp2 4 M=8
xr1 vss inm v_bgr resnsnpoly_pcell_0 segw=1.5e-6 segl=8e-6
xr4 vss inp net1 resnsnpoly_pcell_0 segw=1.5e-6 segl=8e-6
xr2 vss net4 inm resnsnpoly_pcell_1 segw=1.5e-6 segl=8e-6
r3 net2 vss 100e3
m0 vp1 net3 vss vss g45n2svt L=2e-6 W=4e-6 AD=600e-15 AS=600e-15 PD=8.3e-6 PS=8.3e-6 NRD=37.5e-3 NRS=37.5e-3 M=1
m1 net3 v_bgr vss vss g45n2svt L=2e-6 W=4e-6 AD=600e-15 AS=600e-15 PD=8.3e-6 PS=8.3e-6 NRD=37.5e-3 NRS=37.5e-3 M=1
m5 net1 vp1 vdd vdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=1
m12 v_bgr vp1 vdd vdd g45p2svt L=2e-6 W=8e-6 AD=1.2e-12 AS=1.2e-12 PD=16.3e-6 PS=16.3e-6 NRD=18.75e-3 NRS=18.75e-3 M=1
m14 net3 net2 vdd vdd g45p2svt L=2e-6 W=2e-6 AD=300e-15 AS=300e-15 PD=4.3e-6 PS=4.3e-6 NRD=75e-3 NRS=75e-3 M=1
m15 net2 net2 vdd vdd g45p2svt L=2e-6 W=2e-6 AD=300e-15 AS=300e-15 PD=4.3e-6 PS=4.3e-6 NRD=75e-3 NRS=75e-3 M=1
c0 vdd vp1 5e-12
viprb0 net5 vp1 DC=0
.ends BGR_circuit
** End of subcircuit definition.

** Library name: TB_BGR
** Cell name: tb_bgr_ref
** View name: schematic
v8 vss 0 DC=avss
v7 vdd 0 DC=avdd AC 1
c0 v_bgr 0 1e-12
xi18 v_bgr vdd vss BGR_circuit
.END
