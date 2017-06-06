Title: So I tried Arch
Date: 2017-06-04
Tags: Linux, Arch Linux

This article documents my experiences getting to grips with Arch Linux over the first month of using it. I installed it on my day to day laptop and used it nearly exclusively. My uses include normal web stuff, gaming, and software development. As Linux Distros are a rather contentious topic I would like to remind users that these thoughts are based exclusively on my experiences over the last month, and not necessarily always after reading the manual. (Lets face it, when you are in a hurry you don't always have time to read the wiki.) Note that many of my remarks below are more opinion than fact and in places quite candid.

Day 0: (04/05/17)
======

*Oh god, why is this so hard...?*

So the installer is just a shell. In theory this is a good idea, it gives you complete control from the moment the installer boots. I like that but it has it's drawbacks. Firstly the [Arch Linux installation guide](https://wiki.archlinux.org/index.php/Installation_guide) is arguably too in depth and makes the entire process seem more daunting than it really needs to be. Secondly there are several gaping pits for both inexperienced users and Linux veterans to fall into. For example disk encryption has to be set up manually, completely manually. Have you ever heard of the "Discard" Keyword? No? Shame because it is an important part of setting up an encrypted file system on an SSD. 

**Recommendation:** If you're doing this for the first time, have someone on hand who has done this before to help you.

Once you get past the daunt of configuring your own OS nearly from scratch, with basically no safety net, the steps needed to complete the installation are nearly invariably the same, and surprisingly simple:

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

The second "problem", although this is more of a matter of taste, is that the desktop environment comes completely unconfigured, which means I am probably going to spend the next three weeks fiddling until I have GNOME in a state that I like.

I could at this point add a few remarks about my dislike of many GNOME design decisions, however this article is about Arch Linux not GNOME. Here instead I will just note that I may try some alternatives. 

Thankfully Graphics drivers are a different story. The system this anecdote is being written about is a small laptop fitted with a Nvidia GeForce 940M. (See an upcoming article for a review) Thankfully installing [Bumblebee](https://wiki.archlinux.org/index.php/Bumblebee) with the latest Nvidia binary driver was easy, as everything was correctly packaged and self configured. I had a functioning GPU accelerated driver before I even had an X server.

Week 2: (17/05/17)
=======

*Why won't this f***cking printer work*

So far everything has been working fine with the Arch installation. Gnome is a f*cking nightmare but that's normal. This is a blog post about Arch not Gnome so I won't get into that. But now it is time to print something. Everyone knows printers only work if you sacrifice a goat, and everyone knows its worse on Linux.

The problem comes when you consider the Arch way of packaging things; installing CUPS does not configure anything, leaving you fumbling through wiki and man pages desperate for some simple step by step guide on how to make it work. 

I would love to provide one however after much confusion, deadlines pressing, and doubt that the printer even worked I relented and handed my laptop to someone who knew what they were doing. After 30 minutes of frantic black magic he declared he didn't know why it didn't work. At that point and no point again since a piece of paper shot out of the printer containing my document. 

The printer has since returned to it's coma.

**Recommendation:** Set up your printer drivers *before* you need to print something.

Week 4: (04/06/17)
=======

*Working with the AUR and closing remarks.*

Lets start with the AUR. The AUR is something that makes little sense to me. It's principle and reason to exist are clear enough; the problem I find with its implementation. Many people I have discussed this with make comparisons to PPA's on Ubuntu, however I find this to be a poor comparison. Firstly PPA's simply provide an alternate repository source for .deb package files; the AUR provides something more comparable to a PIP sdist package. AUR packages must be built by the end-user, and at the end of the build process the user is left with a local package install-able by pacman.

This leads to my second issue with the AUR, it has not been integrated into the core Arch packaging system, namely pacman. Again comparing with Ubuntu PPA's, PPA's are checked for updates by apt. The AUR gives you a local package, and thus pacman cannot check for an update. In isolation these design decisions make a moderate amount of sense, from a security or simplicity standpoint; but from the end user view I am left scratching my head, as the user experience creates a firm division, leaving user repositories as definite second class citizens in the system. 

There are wrappers and managers that seek to improve this situation, however unsurprisingly none of these are made available in the main pacman repositories; to me this shows a firm stance of hostility toward user packages from the Arch core development community. I found that this has soured what has largely been a positive experience from Arch. There are a lot of people that tell me this is by design and that I simply don't understand the underlying decisions. This is probably true, but ultimately I am writing this from the prospective of an end user, where such reasons matter less than the end result.

**Final remarks:**
For the last month, with the exception of few quirks, Arch has been a reliable Linux platform. I have had numerous issues with my system over the last weeks, however all of them can be traced to the gnome desktop environment I am using. Arch provides a high degree of control of your system, providing you are willing to accept systemD at the core. For me personally I am willing to overlook the issues I raised about AUR to keep that level of control, and the well packaged core. However one thing I cannot look past is Gnome. That gets uninstalled tonight. 

There are many things I left undiscussed here, and I may revisit this topic, or amend this article later, however for now I will leave one trick I did not yet try. [This](https://gist.github.com/XenGi/39c1e8b023fe5bee7c924258367cd633) is the Arch kernel update survival kit, which keeps your system running properly after a kernel update.

