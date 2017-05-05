Title: Video-games on the terminal
Date: 2017-02-20
Tags: Gamedev, Gaming, Terminal, Java, Programming 

So a couple of weeks ago I was thinking about game development and asked myself the question "Why does no one make text mode games anymore?" After about twenty minutes of sketching together some old discarded ideas a game idea was born. The game is based around having a conversation with the player, however this article is not about the game, instead I want to discuss the framework I built to make a text mode game.

50% of game development is picking the right language/framework combination. C++ and Java are both strong choices for developing games. I write C++ at work at the moment, so I picked Java just because I felt like I could use a change. Unfortunately this is a text mode game, so there's no framework ready to go here, it's time to write our own. Thankfully this is a text mode game so the only thing we need to provide is input and output handling. 

Let the Problems Begin
----------------------
So first thing's first; we want colour. Is colour handling standardised on modern terminals? Kinda. Does that mean you know what colour your're gonna get? ... NO. So there are several standards for colour on the terminal, Xterm256 and ANSI are the most common on UNIX, do those work on Windows? No. So lets use ANSI as that is the most widely supported, and I care more about deploying to UNIX than Windows. (I mentioned this is a terminal game right?) Cool, problem solved? ... NO... Terminal profiles are a thing. If you don't know, terminal profiles are customisation's you can make to your terminal emulator to choose custom fonts, __colours,__ font sizes, etc. Yea I can't fix that. Lets use ANSI anyway, at least it will generate colours in a way the user will expect.

For input reading a string from the terminal just isn't good enough for a video game. We need a menu system for traversing context, and some way for the game to control the prompt issued to the player. If we're logging the action happening on stdout we need a way to wipe these menu's from the terminal again. Dealing with these problems in reverse order: ANSI codes to the rescue; we can easily wipe anything we want from the terminal as long as we accurately track how many lines of text we output. By controlling colour we can create intuitive prompts that become part of the user's input, without it becoming confusing why it cannot be edited.

So lastly... Menus. Making menus that can be navigated with the keyboard requires capturing the raw keyboard input. Without a window framework in Java this is __impossible__. I am not exaggerating; the JVM will not return any text from stdin to the program until the return key is pressed under any circumstances. Even with modern Java utilities that allow "raw" access to `System.console` no data is sent until the user presses return. Foreign function interfaces come to the rescue here. A great library I found [here](http://www.source-code.biz/snippets/java/RawConsoleInput/) (LGPL) wraps the C standard lib to provide a C stdin and allow raw access to it. The downside is that now our lovely portable Java executable has native code in it... Yay. It also now has a dependency to a library called JNA provided by Sun. 

We're balls deep now. To fix the JNA dependency, and native code enter our build system: Gradle. Gradle is magic. It just fixed it and now the JNA and it's native dependencies are all packaged into the Jar, and available for most common platforms, including ARM and Windows. 

So it Works. How Does it Feel?
------------------------------
Well for starter's development is a little uncomfortable. Eclipse and Gradle don't get along too nicely, making it easier to just build from the terminal with `gradle build`. Eclipse's integrated console also can't handle escape sequences, so all testing has to be done in a real terminal emulator. This leads to the bigger problem: there are literally hundreds of terminal emulators in existence, so being able to verify the game's functionality across even a reasonable subset of them is a mammoth task. I haven't even tried to test compatibility with VT100 compatible hardware terminals.

The game's feel however is very unique. I am too young to remember DOS console games, or even older classics, however seeing a full game running in the 80 by 60 characters of my modern gnome terminal fills me with a nostalgia for a time when computers, and maybe also the world, were simpler. But maybe that's just me. It's actually surprisingly immersive, even in the little demo I made. 

<img src="/Blog/2017-02-20_WritingAGameForTheTerminal-TerminalGame01.png" style="margin: auto; display: block; width: 100%;  max-width: 600px;" /> 

It isn't without very hard limitations though. For instance while immersive any game written with this will be very limited in it's use of visuals to control the experience. Audio is possible but could go against the original idea of it being a text mode game. The other downside is that it is harder for the end user to enjoy. Today players are used to clicking on a binary and playing. With this however the player must open the jar file in a terminal. Debugging terminal incompatibilities would also be very frustrating for the user, which might explain why all text games released today usually have some sort of game window.

<img src="/Blog/2017-02-20_WritingAGameForTheTerminal-TerminalGame02.png" style="margin: auto; display: block; width: 100%;  max-width: 600px;" /> 

Limitations aside though I think this is kinda cute and I don't plan on porting my game to have a window during any time soon. Once it reaches production that might have to change though. However I am heavily biased I wrote the damn thing.

As for this framework's future, I'll probably extend it a bit and throw it on Github.

__ - Segfault__ 

_Oh and if you even mention nCurses I will hurt you._


