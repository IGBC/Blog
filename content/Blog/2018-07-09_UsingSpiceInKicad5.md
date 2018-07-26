title: Using SPICE in KiCAD 5 (Pt 1)
The latest version of KiCAD brings an interesting new feature; SPICE integration allows simulating your 
circuits straight from EESchema's schematic capture. SPICE is a powerful tool, which opens up many options 
for verifying your circuits. Here I will only cover the details for getting started with a common use case, 
verifying the operation of a filter, but it will cover all of the peculiars of how KiCAD interfaces with 
SPICE.

**Please note that this article references unstable features. KiCAD may (and probably will) change some 
details of how this works. I will try to update this article as that happens, but this article will not be 
100% up to date**

**Prior Reading:** This article assumes that you are familiar with using KiCAD for schematic capture (drawing 
a schematic into the computer in a way it can understand), and many concepts of analogue electronics, namely 
filters. A limited understanding of Circuit simulations may also be helpful.


Installation
------------
Installation on Linux is simple-ish. The features we need have not made it into KiCAD-Stable yet, so we need 
to install the git packages. We also need to install the ngspice system package. Compiling KiCAD will take a 
while. I suggest getting a cup of tea.
### Archlinux
If you're on arch congratulations, just install the following packages:

  * kicad-scripting-git (AUR)
  * kicad-footprints-git (AUR)
  * kicad-packages3d-git (AUR)
  * kicad-symbols-git (AUR)

Note this will require the uninstallation of your existing KiCAD. 

See here for [installing AUR packages](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages) but I recommend you install an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)

### Ubuntu 18.04 
*TODO spin up a VM and make it work*

### MacOS / Windows
On both of these platforms you will need to configure a C++ development environment from scratch. Both KiCAD 
and ngspice support Darwin and Windows, so you will need to follow the instructions for building them, and 
then correctly insert the ngspice binary into your path. I am not familiar with these platforms, so can't 
really help. 

You're on your own. 

How This Works
--------------
Before we get started a word on how this actually works, which should help with troubleshooting later. 

KiCAD has no understanding of how your circuit actually works. It is only interested in how components are 
connected together. You will have seen this first hand, with meaningless ERC errors if you've ever tried to 
use a Raspberry Pi to power a board.

Similarly SPICE has no understanding of the real world. It does not understand what a 74HC00 Quad NAND Gate 
is, nor does it understand what a op-amp is. In fact it does not even understand connectors. The only thing 
SPICE understands are atomic* analogue components, additionally all components are modelled as ideal. 

SPICE sees the circuit provided as physically ideal, there are no parasitic resistances, or capacitances, or 
inductances. It is however aware of the effect of temperature on resistors (and nominally operates at 27°C). 

Typically a spice simulation will have additional components added to model the non-ideal properties of the 
circuit, E.G. the ESR of capacitors. However the schematic in KiCAD directly maps components to footprints 
for placement on the final PCB. This leaves us a tricky problem to solve, we'll get to the solution later, 
but it is important to keep this in mind if you are getting unexpected results. 

_Editors note: inductors are particularly problematic as an ideal inductor is physically impossible, and can 
appear to create energy from nowhere. If your passive circuit is creating significant positive gain that is a 
telltale sign you have an incorrectly modelled inductor._

__*__ In this case "atomic" means they cannot be simplified any further without changing their electrical 
characteristics. A resistor is a resistor, a capacitor is a capacitor, an op-amp is typically several dozen 
matched transistor pairs, with some laser cut resistors thrown in for good measure.

Getting Started
---------------
Open KiCAD in the traditional way. You'll want to create a new empty project first, then open it in EESchema.

To start with draw out the following circuit. The components used are normal resistors and capacitors from 
the device library. The connectors used are Conn_Coaxial from the Connector Library. It is important to label 
every node you are interested in simulating, to make them easier to find later. The GND node will inherit 
it's name from the power symbol.

Lastly you need to annotate the schematic before continuing. 

![Schematic Used for this Tutorial]({filename}/Blog/2018-07-09_Might_as_well_404)

This is a single pole low pass filter. We can visualise it's output with an AC frequency sweep. Lets do this 
now.

  1. Start by Selecting Tools -> Simulator From inside EESchema. 
  2. You'll  be met with a simulation window Click "Settings"
  3. From the settings window select "AC"
  4. Enter 1000, 10, 10000 for Number of points, start / stop frequencies. 
  5. Tick both Check boxes, and click OK.

You are now ready to run the simulation. Note that the simulation settings are lost if you close the 
simulator window, however the simulation will reload the schematic every time the run button is clicked.

You may now click the run button. 

You probably now have an error that looks something like this 
```
Circuit: KiCad schematic
Error on line 3 :
j1 /in 0 conn_coaxial
Unable to find definition of model  - default assumed
Error on line 4 :
j2 /out 0 conn_coaxial
Unable to find definition of model  - default assumed
```

Ignore that for a second and click "Add Signals", then select "V(/OUT)" and click OK. 

![Expected False Output]({filename}/Blog/2018-07-09_Might_as_well_404)

I will assume you know how to read one of these graphs. If you don't its called a 
[Bode Plot](https://en.wikipedia.org/wiki/Bode_plot), and you will need to learn how to read them 
before continuing. You might have just noticed that the line is flat, and that we have no output at all. 
Counter-intuitively this issue has nothing to do with the error below, but the solution to both problems is 
the same. 

I mentioned earlier that SPICE doesn't understand components like connectors. Well KiCAD has naively fed the 
connectors to the simulation*, which created the error `j1 /in 0 conn_coaxial Unable to find definition of 
model  - default assumed` This error is benign, as the simulation is assuming 
the component has no effect on the circuit. This is usually true; however in our case J1 is actually driving 
the circuit. So for the purposes of simulation we need to replace the connector with a voltage source. 

  1. Return to EESchema (Don't close the simulation window)
  2. Edit J1 (press E on it because the simulator has overridden the current tool)
  3. Add a field (the "+" button) called "Spice_Primitive" with the value "V"
  4. Add a field (the "+" button) called "Spice_Netlist_Enabled" with the value "Y"
  5. Add a field (the "+" button) called "Spice_Model" with the value "ac 1"
  6. Click "OK" 

What you have just done is told KiCAD to export J1 as a voltage source with a 1V AC output.

Now return to the simulator window and click run again.

![Expected Correct Output]({filename}/Blog/2018-07-09_Might_as_well_404)

Eureka!

But we still have that pesky error message. We can't trust the results of a simulation with warnings. To 
clear that warning Return to EESchema and add "Spice_Netlist_Enabled" as "N" to J2. Then Rerun the 
simulation. 

Our Graph is showing us that we have a cut-off frequency of 500Hz and a rejection ratio of about 19dB per 
decade. 

Now is the time to play around with the schematic and experiment with values, add new components and see how 
the graph responds.

__*__ Something I hope they will fix with a library update.

Troubleshooting
---------------
###I have no symbol libraries! HELP!
In eeschema do:

  - go to Preferences -> Manage Symbol Libraries
  - if the table is empty or low on entries click Browse Libraries.
  - navigate to /usr/share/kicad/library
  - select everything (crtl-a) 
  - click open - the table should now be filled
  - Click OK, and then try to place a symbol
