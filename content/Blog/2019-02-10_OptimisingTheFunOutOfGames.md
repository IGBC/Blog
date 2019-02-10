title: Optimising the Fun out of Games
So I don't like admitting this, but I have been playing one of those cheaply produced android shovel ware games. [Calculator: The Game](https://play.google.com/store/apps/details?id=com.sm.calculateme) caught my attention from the myriad of games on the app store because I don't see many calculator games. As a self described "serious geek" I couldn't help but check it out, so I installed it.
![Game Screen Showing a calculator with up to 5 operation buttons with operator constants baked in.]({filename}/Blog/2019-02-10_OptimisingTheFunOutOfGames_1_Screenshot.png)


The game was OK, I guess. The fun wore off quickly and around level 15 I found myself stuck and bored with the game. I started jabbing combinations of buttons at random, and while idly clicking I had a realisation. The level had 3 possible buttons and was limited to 4 moves. I used my last hint to expose the first move, so there were only 3 unknown moves. the problem space what n^m ("n to the power m") where n is the number of buttons in the level and m is the number of moves allowed in the level. 

The problem space for this level was therefore 3³ which is 27 possible options for the solution. So I did what any bored math nerd would do while on their lunch break; I turned over the paper wrapper for my sandwich and started to write out the 27 options, this only took about 2 minutes. Then I started tapping them into the phone one after another. And behold the 5th combination worked. The whole process took less time than I spent staring at the level beforehand. 

![Wrapper With a rainbow table written on it]({filename}/Blog/2019-02-10_OptimisingTheFunOutOfGames_2_Napkin.jpg)

But I was out of hints, and the problem space for 3^4 is much bigger (81) if I was going to use this method to solve more levels and not go mad from the repetitive work I was going to need to automate it!

The initial build was about 45 lines of python. 

It took the starting value, the goal, and the number of moves allowed, alongside the text written on each button and calculated the result of each combination of button presses. It printed out the first combination that gave the goal. I used a recursive approach where each move was added to a list of past moves to create an operation stack. It's much simpler in code than in english.

With the script now able to do the heavy lifting I was able to power through the levels, but the game had other ideas! every 10 levels or so it introduced a new mechanic, on a new button, I had to teach my script how to calculate the result of. The first quirky button was the "<<" button. This would treat the number as a string and drop the rightmost character. I was reluctant to perform string operations on the number, else turn into a nightmare of undefined behaviour due to stray decimal point characters. 

I was able to solve the problem with this snippet:
```python
frac = current % 10
current = current - frac
current = current / 10
```

However when the game demanded all digits of a be converted to b I had to relent, and convert the number to a string. This inevitably caused issues with decimal points in the converted numbers and I was forced to clamp everything to an int. TLDR: since level 65 divide has been broken.

The code quality is abysmal so this isn't going on Github/lab. I will include a copy of the script uploaded here. I promise you it is out of date as I have to modify it every few levels. I leave using it to complete the game as an exercise to the reader 😈

[**Source Download**]({filename}/extra/gamesolver.py)

In the mean time I have gotten bored of the game again. I have essentially optimised the fun out of it, maybe I will finish it, but powering through the levels has turned back into a mindless task of entering the level into the computer and tapping the solution into the phone.

If only there was some way to automate that...

Till Next time; SEGFAULT out!
