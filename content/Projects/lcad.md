Title: L-CAD
Status: Draft
Tags: L-CAD, C, IDE, Logic
Category: Projects
Date: 2016-07-09

Open Source Logic IDE
=====================

|             |                    |
|------------:|--------------------|
|**Project:** | L-CAD              |
|**Language:**| C                  |
|**Status:**  | Active Development |
|**GitHub:**  | [github.com/IGBC/L-CAD](https://github.com/IGBC/L-CAD)|

L-CAD, which is short for Logic-CAD for the record, is a  crazy idea thought up in a tent during the Chaos Communication Camp 2015 and inspired by a desire to work with FPGA's to develop... 

*Huh...?*

...Well that was two years ago now; I can't remember what I wanted to develop anymore. To be honest I think I deserve some sort of procrastination award for the thought process of *"I want to develop something with FPGA's, I think I'll go write an IDE"*! 

More seriously the L-CAD project is motivated by the crappyness of proprietary FPGA IDE's. These IDE's are actually so bad that they significantly raise the barrier to entry for developing with FPGA's. The problems with them range from hilariously bad installers, to licensing issues. The biggest problem I have faced is that **none** of them work on Linux, and I **really** don't want to do development work on a Windows PC. 

Most FPGA IDE's in some form or another accept VHDL input. [The United States Air Force can be thanked for that.](https://en.wikipedia.org/wiki/VHDL#Standardization) This gives 3rd party tools a common interface to provide source to. So while the compilation and upload of firmware to FPGA'S is usually proprietary, and also a horrible experience, L-CAD can be used to perform the logic synthesis and simulation, then output VHDL for compiler ingestion.

The project is quite ambitious, it is to include a full time accurate Boolean logic simulation as well as a user interface for visualising and drawing logic systems. The interface will also feature a full tool bench, for logic analysis and an IO control module to allow interfacing with GPIO controllers (like found on the Raspberry Pi), to allow users to hook their projects up to electronics without even having to buy an FPGA first.

Current Status:
---------------

Development has started on the simulation and IO components. Currently there is a working demo for the Raspberry Pi that allows the user to load a logic system from file and connect it to inputs and outputs on the Raspberry Pi's GPIO. However there has been no progress on the UI. It has been decided that the UI will be built in GTK, however I have no experience with UI design, so progress is slow. If you would like to help get in touch.

