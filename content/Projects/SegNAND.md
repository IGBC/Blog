Title: SegNAND
Tags: SegNAND, Synth, Audio
Category: Projects
Date: 2016-12-11

NAND based synthesizer for making artistically annoying noises
==============================================================

|             |                       |
|------------:|-----------------------|
|**Project:** | SegNAND               |
|**Language:**| Solder + Bread Boards |
|**Status:**  | Active Development    |
|**GitHub:**  | [github.com/IGBC/SegNAND](https://github.com/IGBC/SegNAND)|

SegNAND is a somewhat narcissisticly named analogue synthesizer project. Although it's name might be appropriate as like myself is does make loud and annoying noises; as well as periodically breaking anything it is plugged into.*

At the heart of this synthesizer is a 4093 schmitt-trigger input NAND gate. These digital logic gates combined with RC circuits create 4 square wave oscillators, with enable inputs. These are chained into two channels of tone generators modulated with low frequency oscillators. These two channels are are then mixed in the analogue domain.

Currently this exists only as a schematic and a single prototype on a breadboard.

![Schematic 1]({filename}/Projects/SegNAND-Schematic1.svg)
![Schematic 2]({filename}/Projects/SegNAND-Schematic2.svg)

*SegNAND Schematics*

The project is being developed with KiCAD and scraps of paper with *lots* of math on them. I am trying to only use open source tools during development, as there is no point in making a project open source if no one can open the project files.

The end goal of this project is to design a euro-rack synthesizer module from a single channel of the unit, featuring voltage control of the oscillator frequencies. A full two channel unit will be designed to fit on a standalone PCB.

This is my first synthesis project, but most certainly not my last. Eventually the design may be integrated with some of it's successors into single large programmable synthesizer PCB; however this is a long way off.

**It only caused the amplifier to shut down once, and I maintain that it was coincidence. On the otherhand I break things all the time.*


