Title: So I tried Arch
Date: 
Tags: Linux, Arch Linux

Day 0: (04/05/17)
======

*Oh god, why is this so hard...?*

So the installer is just a shell. In theory this is a good idea, it gives you complete control from the moment the installer boots. I like that but it has it's drawbacks. Firstly the [Arch Linux installation guide](https://wiki.archlinux.org/index.php/Installation_guide) is arguably too in depth and makes the entire process seem more daunting than it really needs to be. Secondly there are several wide and gaping pits for both inexperienced users and Linux veterans to fall into. For example disk encryption has to be set up manually, completely manually. Have you ever heard of the "Discard" Keyword? No? Shame because it is an important part of setting up an encrypted file system on an SSD. 

**Recommendation:** Have someone on hand who has done this before to help you.

Once you get past the daunt of configuring your own OS nearly from scratch with basically no safety net the steps needed to complete the installation are nearly invariably the same, and surprisingly simple:

  - Wipe the disk 
  - Partition and format the disk
  - (Optionally) Set up crypto
  - Install the base system with pacstrap
  - generate an fstab
  - configure system settings (language, network, etc)
  - build kernel image
  - configure users
  - configure grub
  
After the last step you should have a functioning system that can be rebooted and logged into. Then you can install packages, connect to networks, etc. At this point I recommend you make a full system backup because that was the non scary part.

**Recommendation:** Back up your system after completing the steps above

The next part is only scary because if you slip up you risk destroying your previous work and having to spend hours either repairing it or starting again. Did I mention that previous bit took 3 hours? So without further hesitation move onto installing X, graphics drivers, then finally a desktop environment. 

**Recommendation:** Allot about 6 hours for the complete installation process, it took me from 10 pm to 4 am.

Day 2: (06/05/17)
======

*Yay I have a working computer... I hate it so much...*

So the desktop environment is installed and working. First time too. Even all of my peripherals are working correctly. This in it's self is a small miracle. I guess I got lucky. There is (again) however two problems. Firstly I installed the `gnome` and `gnome-extra` packages, after which I had to uninstall a strange variety of bloatware, including about ten games, three IDE's and a strange gui tool exclusively for reading GNOME API documentation. I still can't find the name of the package for the included database connection utility. 

**Recommendation:** learn from my experience and read carefully what meta packages are going to install.

The second "problem", although this is more of a matter of taste, is that the desktop environment comes completely configured, which means I am probably going to spend the next three weeks fiddling until I have GNOME in a state that I like.

I could at this point add a few remarks about my dislike of many GNOME design decisions, however this article is about Arch Linux not GNOME. Here instead I will just note that I may try some alternatives. 

Thankfully Graphics drivers are a different story. The system this anecdote is being written about is a small laptop fitted with a Nvidia GeForce 940MX. (See below for a review) Thankfully installing [Bumblebee](https://wiki.archlinux.org/index.php/Bumblebee) with the latest Nvidia binary driver was easy, as everything was correctly packaged and self configured. I had a functioning GPU accelerated driver before I even had an X server.

The Nvidia GeForce 940MX on Linux
=================================
The laptop my GPU is fitted into is no longer manufactured, however recently I noticed that this GPU is still being sold in up to date machines including the Lenovo Thinkpad T470p so I thought it was worth giving a review.

Full disclosure, the system is a 2GB GeForce 940MX coupled to an Intel i7 5500u with 8GB of DDR3. The card is coupled via a PCIe gen 2 4x link and the display output shares that bandwidth. Everything discussed below is using the internal 1920x1080 monitor that has a max refresh rate of 60Hz.

So first let's talk compatibility:
----------------------------------
 - **The open source nouveau driver:** Blacklist it! It can't initialise the card as it has no display outputs. This crashes the driver and leaves you with an annoying message, but an otherwise functioning machine.
 - **The Nvidia binary driver (`nvidia-35<something>`  tested on Ubuntu 16.04):** Don't install it! It WILL brick your OS and leave it in a state where not even the rescue terminal can save you. Just don't try it, it's ugly!
 - **Bumblebee is your friend:** [Bumblebee](https://wiki.archlinux.org/index.php/Bumblebee) is a project that wraps the Nvidia binary in a lot of cotton wool and magic, repackages it with it's own personal X server and then provides functionality to launch applications on a virtual screen in that X server and feed the image back to your window manager. **Find a distro that supports and packages this.** If you have a well packaged copy of Bumblebee you will have no problems with the card and a very enjoyable experience. 
 
Lets talk Bumblebee:
--------------------
So Bumblebee is a complex and quirky thing. Firstly when you install it you have to be vigilant about which version of the Nvidia driver is being packaged along with it. Newer drivers have better game support and are more likely to give you a good experience. If you are on Arch Linux then following the [instructions](https://wiki.archlinux.org/index.php/Bumblebee#Installing_Bumblebee_with_Intel.2FNVIDIA) will ensure that you always have the latest version. On Ubuntu you cannot be so confident. The first time I installed it I somehow got it to install 352, the latest packaged at the time; however I cannot remember how because six months later it insisted on installing the ancient 304 driver (which actually predates and does not support the 940MX).

Once installed Bumblebee remains quirky. For example there are 2 commands for passing applications to the GPU: `optirun` and `primusrun`. (It is noteworthy that the later is packaged separately in the `primus` package) Many applications do not work with both. For instance Steam games are typically more reliable with `primusrun`. `nvidia-settings` also becomes fun. the command on it's own can't connect to the GPU and `optirun nvidia-settings` can't find the display (makes sense as none is attached to the Nvidia GPU). The workaround is posted [here](https://wiki.archlinux.org/index.php/Bumblebee#General_usage).
