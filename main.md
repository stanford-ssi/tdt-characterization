# TdT Characterization Experiment
Written by *Michael Uttmark*
*Written:* 2/16/19 *Performed:* TBD

Procedure Purpose
=================

Characterize the rate of extension of ssDNA with varying nucleotide:DNA
ratios.

Overview
========

An array of samples will be tested with these conditions (dTTP:starting DNA molar ratio
(moles) by time of reaction):

|||1  | 2  |3   |4   |5   |6   |7   |8    |9    |10   |11   |12      |
|---|---|---|----|----|----|----|----|----|-----|-----|-----|-----|--------|
|||30s|45s |1min|2min|3min|5min|7min|10min|15min|20min|30min|Controls|
|A  | 2:1  |    |    |    |    |    |     |     |     |     |        |||
|B  | 3:1  |    |    |    |    |    |     |     |     |     |        |||
|C  | 5:1  |    |    |    |    |    |     |     |     |     |        |||
|D  | 7:1  |    |    |    |    |    |     |     |     |     |        |||
|E  | 10:1 |    |    |    |    |    |     |     |     |     |        |||
|F  | 15:1 |    |    |    |    |    |     |     |     |     |        |||
|G  | 20:1 |    |    |    |    |    |     |     |     |     |        |||
|H  | 40:1 |    |    |    |    |    |     |     |     |     |     ||H12|

Samples are addressed by their 96-well plate location (eg. H12, as marked).
They will be stopped with EDTA and sent to PAN. The most promising samples will be run on a gel for better resolution.

For PAN analysis, we will be sending in Terminal Deoxynucleotidyl Transferase extended samples with a concentration of 2ng/uL.

## Materials

-   100 uM "BS_Start" Oligonucleotide (Sequence: 5'-AGTTACCATGACCGTGTGCG-3')
-   100 uM "BS_Comp_8" Oligonucleotide (Sequence: 5'-AACGCACA-3')
-   100 uM "15mer" Oligonucleotide (Sequence: 5'-ATGGACATGGACTAC-3')
-   100 uM "90mer" Oligonucleotide (Sequence: 5'-AGTATT ... TAGACGTT-3')
-   Terminal Deoxynucleotidyl Transferase (20 U/uL)
-   dTTP (100 mM)
-   NEB Terminal Transferase Buffer (10X)
-   CoCl2 (10x)
-   RNAse Free Water
-   EDTA (0.5M)

## Dilutions
1. Dilute 39.1uL of BSStart (100uM, 6133Da) in 960.9uL of nuclease-free water for 1 mL of a 24 ng/uL (3.91 uM) working stock. Vortex well.
2. Dilute 50uL 100mM dTTP Stock in 4950 uL water for 5000uL of 1mM working stock. Vortex well.
4. Dilute 4.32 uL of 90-mer (AGTATT ... TAGACGTT, 100uM, 27786Da), 13.04 uL of 15Mer (ATGGACATGGACTAC, 100uM, 4601Da) and 12.56 uL of BS_Comp_8 (AACGCACA, 100uM, 2388Da) into 3970.08 uL Nuclease-Free water in a 15 mL tube. Vortex well before use. This is the DNA Control Solution, which is 3 ng/uL 90mer, 1.5 ng/uL 15mer, and .75 ng/uL BS_Comp_8 working stock. This will result in 1.0ng/uL, 0.5ng/uL and 0.25ng/uL final concentrations of 90nt, 15nt and 8nt control stands in samples sent to PAN.
5. Prepare a trough of a mixture of 600uL 10x NEB TdT Buffer and 600uL 10x CoCl2.

Procedure
=========

Prepare Plate
-------------

Into each well, pipette 6uL using a multichannel pipette from the TdT Buffer and CoCl2 mixture into each well except H12.

**Note:** Due to a small mistake, dTTP dilutes were added to the 96 well plate *before* buffer and CoCl2 mixtures. This should not make a difference, and we recommend that the original ordering be followed.

For each row, create the following dilutions of dTTP from 1mM working stock
prepared before:

|Row       |dTTP Working Stock (1mM)| Water     |
|----------|------------------------|-----------|
|A (2:1)   | 7.8uL                  | 992.2uL   |
|B (3:1)   | 11.7uL                 | 988.3uL   |
|C (5:1)   | 19.6uL                 | 980.4uL   |
|D (7:1)   | 27.37uL                | 972.6uL   |
|E (10:1)  | 39.1uL                 | 960.9uL   |
|F (15:1)  | 58.7uL                 | 941.3uL   |
|G (20:1)  | 78.2uL                 | 921.8uL   |
|H (40:1)  | 156.4uL                | 843.6uL   |

For each well in each row, pipette 10uL of the corresponding dTTP dilute (except H12).

For each column except for 12, and for control wells A12, C12, E12, and G12, pipette 4uL of Terminal Deoxynucleotidyl Transferase into each well (3 tubes). Multiple tubes of Terminal Deoxynucleotidyl Transferase will be added sequentially in row-major order, not pooled together. 
**Note:** The TdT in column 12 was added separately after all of the other tubes at 1:11pm and the control TdT reactions were stopped at 2:13pm. 

In wells B12, D12, and F12, pipette 4uL of Nuclease-Free water instead of TdT.

In wells A12, C12, E12, and G12, pipette 10uL of Nuclease-Free water instead of DNA.

## Begin Experiment
For each column of reactions except column 12, and for control wells B12, D12, and F12 in order of decreasing incubation time, begin by pipetting in 10uL of the DNA dilute prepared earlier into an entire column simultaneously using a multichannel pipette. Write down the time each column was started and stopped when time permits, and set a timer for the given reaction time. Wait until the allotted time for that column has elapsed and cease the reaction with 10uL of EDTA pipetted into the entire column (except H12) with a multichannel pipette.

Add 10 uL of EDTA to column 12 after all other wells have been inactivated/after inactivation of the shortest time reaction. 
**Note:** 1:11

## Controls
No Terminal Deoxynucleotidyl Transferase should be added to the controls in column 12. H12 must be left empty.

## Sending to PAN
In each well of a new 96 well plate, pipette 20uL of the DNA control solution. Pipette in 10uL from each corresponding well from the experimental plate (A1 to A1, H12 to H12 etc). Keep the experimental plate for running on a gel and submit the new plate to PAN for CE.

## Practical Addendum of Mishaps

B5 did not get nucleotides initially and this was fixed via a single channel pipetting.

