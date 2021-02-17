Title: My Other Computer is a Racecar
status: draft

# My Other Computer Is a Racecar
_Experiments in building computers in very "not recomended" configurations

## T minus 3 months
Its early September 2019, and I have just come home from spending three months overseas living with my girlfriend. I spent an embarrasing amount of that time playing Factorio with her. Factorio is a wonderful game, not only for its engaging problem solving based sandbox gameplay and endless moddablity, allowing you to turn it into a unholy grindy hyper realistic industry simulator, but also because it is one of the few games that could actually run on the laptop I could take with me. My laptop is no slouch however, its a top of the line thinkpad from only a couple of years ago (It's still in warrenty), but I realised while trying to do development on it over the summer, that I really missed my desktop; not for the horsepower however, but the generally improved quality of life experiance of having a "full size" computer. I came home with two bad ideas stuck in my head:

  1. I don't really play 3D games anymore.
  2. I really would like a desktop computer that could fit in my hand luggage.

I realised that my current computer, a full tower monster with twin RX Vega GPU's was such a bad fit for how I actually used my desktop. My computer spent most of it's life bored, running firefox, VSCode, and KiCad. Why did I need a 1000W gaming monster boiling my room day and night for that? It was time to build a new PC. This saddened me a little as to meet my new portable, low power, dream I would have to give up my Vegas. To fund the new machine I would have to sell the old one. Has anyone mentioned CPUs depreciate like bricks?

If it wasn't for the stupid "T2" chip apple installed in the 2018 Mac Mini this would be a very short blog post. The at the time new release was very tempting, offerring 6 cores and up to 32GB of user upgradable ram. But that bloody T2 prevents the running of Linux, well if you want to use the internal SSD. I consider storage in a computer essential, so Apple are still a long way from ever getting any money from me. It was time to look at other options. So I outlined a list of requirements:

 - Minimum of 32GB of ram and 8 cores.
 - Small enough to fit in My rucksac.
 - 10Gb Ethernet
 - No laptop CPU's

The requirement for an 8 core CPU came from my existing desktop. At the time I was running an Intel i7 5930K that had cost me my firstborn child less than 3 years prior. Already I was unhappy how its Haswell architecture was aging, and laptop CPU's were starting to beat it in multithreaded benchmarks. As mentioned earlier I don't really game. When I put my Computer to work its CPU heavy tasks like compiling my huge Rust code bases, or sometimes running some sort of simulation or non accelerated render task. So 8 cores was a must. Ryzen 3000 had just launched and that looked like the best option. However it locked me into needing a video card in the system. But I also needed 10Gbit ethernet, naturally not a single ITX motherboard for x570 had this feature. 

I needed _two_ add in cards, in an _ITX system_! :shocked:

If I am honest from early days the design for the PC I would end up building was focused around the case. Ever since I entered the Enthusiast PC scene at 16 I had lusted over cases by a small Canadian firm called Lone Industries, and their latest rendition of their design, the L5, was very desirable. From early on in the design process I knew I wanted to push the L5 as far as was possible. The L5 is a very non traditional case. Its ITX compatible, but only has room for "low profile" add in cards. It also has no space for a Power supply, instead requiring you to select from a list of pre-aproved DC-DC converters, which receive power from an external PSU, like a laptop power brick. Naturally this makes everything more constrained. Getting power into the system is as much of a challenge as getting the heat back out. Despite the constraints, even from the product page it was clear there was room for activities in the L5, especially if traditional SATA storage was not needed.

Note to Editor: Image of the L5 here.

## T minus 2 months

With the challenge of this project in focus it was time to solve the problems and pick some parts. The first problem was getting 10Gbit in an ITX system. The L5 has two card slots, intended for double width GPUs, so there is mechanical space to fit a second add in card, but how do you get PCIe to it? With ever more advanced M.2 storage configurations being the latest craze vendors seem to be trying to force onto gamers who actually don't need it, EVERY modern ITX motherboard has 2 M.2 NVME slots. These are basically a PCIe x4 connector hiding in a storage format. Many of these boards put the second slot on the back of the board, and luckilly China makes adaptors for literally everything. The problem of putting 2 cards in an ITX motherboard can be solved for $15 including shipping, if you're willing to run a janky ribbon cable behind your motherboard to where the card will go.

-- Store pick of the adapter -- 

The sacrifice of the second card slot space, severly limited GPU options. Googling "fastest single slot half height GPU" will give you a lot of results on forums of other crazy people trying to build tiny desktops, for various reasons. The consensus among these people is (as of late 2019) the Nvidia P1000 is the fastest, but if you hate Nvidia, the AMD WX4100 is nearly as fast. This was going to be a linux workstation, so the WX was preferable. On top of that it was £50 cheaper. That might not sound like much but paying £300 for a GPU with the performance of a 1050 hurts. £250 for something that is literally a rebadged RX560 isn't much better. On the plus side it is bright blue. (I mean _bright_ blue!)

-- WX4100 --

Knowing this build was going to be truely unique and because of that GPU, rediculasly expensive no matter what I did (x570 pricing also wasn't helping), I decided to max the specs. If this thing was gonna break its budget, it was gonna do it in style. 32GB ram DIMMs had **just** become available (I have never preordered hardware before) and AMD's new R9 parts were sexy AF. £800 the specs were raised to 64GB of ram and a 12 core CPU.

I gritted my teeth as I ordered the parts. With the variety and obsurity of the parts in this build I had to order from 7 different suppliers. (including Lone directly for the case, and two eBay sellers) The parts for this came from all over the world. The DC-DC converter (something most PC's don't even have) came from Germany; the case came from Canada; the M.2 adapter was shipped from China Directly, and I am pretty sure the PSU "fell off a truck" destined for Dell UK.

# T minus 0 hours
_"what have I done?"_

It took over a month for all of the parts to arive. I had to test most of them individually. One faulty power converter was returned before the computer was even built. 

Turning the pile of parts into a working machine was a multi-part ordeal. The machine was peiced together as parts came in, carfully testing each part of the design like something I had engineered myself rather than slapped together from off the shelf parts. I had zero faith this would actually work. All the safety margins had been erroded away by pushing the envelope of the design. 

--- Tabletop test rig ---

The Case and the GPU arrived last. Squeezing it all into the case took hours the first time. (a year later I can strip down and rebuild the thing in about 20 mins) But it was worth it, the finished machine in its case was smaller than the box the motherboard shipped in. Powering it on for the first time was different; I have being building computers for years, and the usual anxiety of will it work was nothing compared to this. I knew it worked. I had tested it. But from the moment I powered it on I owned something that I had hacked into existance. It was (and at the time of writing I believe still is) unique!

-- Packed in the box --

-- Finished Build --

And oh was it fast!

# T plus 6 months
Its now May 2020. The machine prooved its usefulness at chistmas, being taken overseas in my hand luggage without issue. That said every time the TSA see it I do get a puzzled look. I haven't yet had to explain why I am carrying a homebuild computer around with me.

The other goal, a small low power desktop is also going well, I can leave the machine on 24/7 without it boiling the room I leave it in. However it's May 2020. I am trapped in a University Dorm room, during the first lockdown in the UK fcaused by the COVID-19 outbreak. My nearest neigbour is 3 buildings over on the university campus, and there's one feature of my old desktop I _really_ miss. 

My old rig didn't have two GPU's for crossfire, or OpenCL. The second GPU was an OVMF slave GPU, for passing through to a guest operating system in a VM. I could never get it working right with the Vega, however my 10Gbit ethernet card wasn't any use trapped in a dorm room, so I pulled it and went on eBay GPU hunting. My goal was to find the most powerful GPU that would fit, that also supported windows XP. I would use an XP VM to run some old games and kill some time during lockdown. The newest series of cards that supported XP from either chip manufacturer was the ATI Radeon HD 7000 series. I found a £15 HD7470 that was the sweet spot between performance, and "I am broke cos I built this bloody computer 6 months ago". The card I found was an old Dell OEM part, it seemed fitting, and would not be the last Dell part in this story.

-- Card --

Getting the card, the fun began. after installing ther GPU I found that it firmly did not work. Fustrated, I pulled the shiny new WX4100, and scratched it on the shitty £15 GPU's screws in the process. After testing with just the HD7470 I confirmed the GPU worked fine, and re-remembered how bad AMD linux drivers where pre AMDGPU. (The 7470 is a Turks-pro core, only supported by frglx. The less said about that driver the better.) Installing the WX4100 in the second slot actually resulted in a no-post. Debugging could have been long and fustrating but I am an electronic engineering student, and the culprit seemed pretty obvious to me.

V = IR

M.2 slots are not intended to drive PCIe cards, and with the addition of the length of ribbon cable, power delivery for the 15W network card must already have been pretty marginal. The adapter actually came with a short cable for providing additional power, however there was never room to plug it in; the GPU was in the way. These GPU's however pull a lot more power, up to 75W. With that much current demand, the voltage droop was just too much for the card to fire up. There was no choice. To continue I needed to plug in the additional power connector. But there was simply no room between the cards. I considered cutting the shroud of my beautiful WX4100, but no... if I had to butcher a part it should be the cheapest one in the system. I have a saying "you don't own something until you have taken a soldering iron to it". I _own_ my computer; after stripping down the entire system I carfully desoldered the connector. I now had a 12V hole and a Ground (0V) hole. The power converter has a connector to attach a GPU cable, but I didn't have the cable kit that came with it, and I couldn't get it (see lockdown) But I did have an old TFX power supply lying around I used for experiments. That had a 4 Pin CPU connector, which fit, the cable colours were even correct! Best of all it was a Dell part; it was perfect! I felt bad snipping the wires of my trusty old PSU but it needed to be done. I soldered this new connection to the adapter, and reassembled the machine, running the cables behind the motherboard and connecting the power converter.

Turning the resultant hacky mess on was the most nerve wracking thing I have ever done. If the connections were inverted, or shorted together, or I had screwed something else up, there were no safety fuses here. The entire computer would literally go up in very expensive smoke.

That thankfully didn't happen. And for extra credit the GPU now immediately worked. (the driver still sucked tho) What came next was the really annoying bit I should have tested first. Windows XP cannot boot from UEFI so cannot be supported by OMVF :facepalm:

I relented and what came next was a textbook installation of a Windows 7 OVMF guest with GPU passthrough on arch linux, followed by an evening of playing the Sims 2. Bored of that for the next 3 months my GPU was used to run Microsoft Word while I did my coursework. (A total waste)

# T plus 10 months.
The machine worked great over the summer. It went back overseas. (More funny looks from TSA agents) It came home. It learnt how to make music with me. Then one week after moving back to a University dorm: *Bang!*

I would love to say it went "bang" with a straight face. But truth is it didn't. It crashed whilst building a Linux Kernel, and after that could never hold up against a sustained CPU load again. What I feared all along had finally happened. My racecar of a computer had finally thrown a part. Sod's law states it has to be one of the exotic parts that is impossible to source during a global pandemic. I feared it was the power converter. And only one week after leaving for uni had to trapse home, broken computer in hand, hunting for debugging spares.
I hooked up a regular PSU in place of the converter, and accepted my fate as I fired up the machine to run a stress test.

But no. It shut down nearly immediately. Something else was wrong, but I had stripped it down to the bare board and parts needed to boot. I was sure it couldn't be the GPU, but swapped it anyway. Bad RAM couldn't reboot a system under CPU load. So that left two things. The motherboard or the CPU. 

Lets just say f*ck you Gigabyte! I ran a R9 3900X underclocked and undervolted in that board for 10 months. If your VRM can't survive that you shouldn't be building motherboards. Amazingly I have only ever had three PC components fail on me in my life. Two of them are gigabyte motherboards (The third was a Ryzen 1600 with the "SEGFAULT Bug" which was supposed to be impossible on R5's. I guess the CPU didn't like my nickname :shrug: ).

£300 later and the machine has a new Asus x570 board. Which runs quieter, and way more stable, at lower voltages too. I should have bought this a year ago. Thank god it wasn't the power converter. Those were out of stock everywhere.

# T plus 14 months.
I would say I am happy with the machine. Its not something I would reccomend anyone else attempt. The thing is crazy high maintainance, and the lack of GPU performance is a real sting in the tail when you do want to do something 3D. That said owning a 12 Core workstation that you can cram in a backpack has real productivity advantages, well until a global lockdown removes the need to anything to be portable.

I am still waiting for AMD to announce some small NAVI GPU's; Any day now right...   right?
