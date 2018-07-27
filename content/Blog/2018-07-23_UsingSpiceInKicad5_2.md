Title: Using SPICE in KiCAD 5 (Pt 2)
The latest version of KiCAD brings an interesting new feature; SPICE integration allows simulating your circuits straight from EESchema's schematic capture. SPICE is a powerful tool, which opens up many options for verifying your circuits. 

In this article we will cover modelling more complex circuits with SPICE, using an idealised op-amp as an example.

**Please note that this article references unstable features. KiCAD may (and probably will) change some details of how this works. I will try to update this article as that happens, but this article will not be 100% up to date**

**Prior Reading:** This article assumes you have read [part 1]({filename}./2018-07-09_UsingSpiceInKicad5.md) of this series, and the prior reading that recommends.

Modelling an Op-Amp
-------------------
When I was taught how to use SPICE on an overpriced degree course (and of course it was the Windows only, proprietary, LTSpice; do not use this!) I was taught how to simulate Passive components, and energy sources, nothing else.

It appears my education experience was not unique, resources on modelling active components get muddy, as I researched this article. The work below took many hours of patient research and filtering through message boards, while collecting of half-solutions into something working.

I would like to thank [masteringelectronicsdesign.com](https://masteringelectronicsdesign.com) who have a deep dive into the art of modelling components in SPICE from the simplistic, to the frankly absurdly complex. In this and following articles I will be referring to their work, from the context of KiCAD. If you want to catch up on pure SPICE modelling I strongly recommend you read through their [op-amp modelling tutorial series](https://masteringelectronicsdesign.com/buildi-an-op-amp-spice-model-from-its-datasheet/) (4 parts) 

In this article I will be using the most naive model of an op-amp possible. An ideal op-amp behaves like a voltage mirror; whatever voltage appears on the input pins is multiplied by the op-amp's gain and is presented on the output pins. Note I said pins, not pin. The traditional symbol we use to describe an op-amp is actually counter intuitive here. An op-amp's output is a voltage, and a voltage is measured relative between two points. In the case of a jellybean op-amp the output voltage is measured between the output pin and the negative supply rail. We can summarise this to the equation:

![A(Vin+ - Vin-) === Vout - Vss]({filename}./2018-07-23_UsingSpiceInKicad5_2_Equation.png)

*Where A is the op-amp's gain.* 

Spice describes this behaviour as a voltage controlled voltage source, or VCVS for short. Let's introduce the spice symbol for a VCVS (Yes SPICE has symbols). 

![VCVS symbol]() 

This symbol maps to our equation, so we can use it to model our op amp.

Getting started in KiCAD
------------------------
Firstly you'll need to build this circuit in EEschema. 
As last time, the resistors are "r" components and the connectors are "Conn_Coaxial". The only new component is the op-amp. Here we are using the LM386 symbol. You might be tempted to use the generic op-amp symbol, but it is not suitable for our purposes, as it does not have a negative supply pin which we need to map to our model. 

![circuit]() 

As before Annotate the schematic before continuing. 









