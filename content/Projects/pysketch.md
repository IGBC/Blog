Title: PySketch
Status: Draft
Category: Projects
Tags: PySketch, Sketches, Python, Scripts
Date: 2016-06-17

Arduino Style Sketches in Python
================================

|             |                               |
|------------:|-------------------------------|
|**Project:** | PySketch ("Sketches" on PYPI) |
|**Language:**| Python 3                      |
|**Status:**  | Finished (Mostly)             |
|**GitHub:**  | [github.com/IGBC/PySketch](https://github.com/IGBC/PySketch)|

Pysketch (which takes the name "sketches" on PyPI; pysketch was taken by an abandoned drawing app) is a rapid prototyping framework for minimizing the amount of python needed to be written to automate small tasks. It was inspired while working with the Raspberry Pi to develop tests for hardware during my day job.

The Problem:
------------
While working with the Raspberry Pi and python to develop tests for hardware during my day job, I found that most test scripts consisted of the same structure: 

 - Set up the GPIO pins.
 - Do the test until I press `^C`. 
 - Free everything and terminate cleanly.

 One of the first things I realised was that these sort of tests were much easier to code with Arduino. The only two problems with that are: a) I didn't have an Arduino available, b) Arduinos suck. 
 
 To be fair Arduinos don't suck for everything but they are more suited for the classroom than a hardware testing platform inside a hectic business. First of all Arduinos don't have networking. Some do, but you have to program your own network stack, which is less than convenient for hacking out a quick test. With the Raspberry Pi you also have the advantage of being able to launch tests from the command line, with the Arduino you must recompile and upload a new sketch to the device every time you want to change test. There are also other advantages to using the Pi but you get the idea. So why would it be easier with an Arduino? The IDE.

The Arduino IDE from a UX standpoint is possibly one of the single worst tools I have ever used, rivalled only by MS Paint from Windows XP and Eclipse JDT 3.0. However what makes the Arduino IDE so unique is what it hides from the user. Arduino is programmed in C, however the simplest example from the IDE "Blink" is only 9 lines of code:

``` C
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```
*This code was sourced from [arduino.cc](https://www.arduino.cc/en/Tutorial/Blink).*


No one who is familiar with C will believe that this code in isolation will compile, let alone configure a microcontroller; therefore we can conclude that the IDE is hiding code from the user. The most obvious things missing are `#include` statements, needed to load Arduino's GPIO library. Arduino offers the "import" keyword, however it's behaviour is a little different. The next and most important change is how the main function has been replaced with two functions `setup()` and `loop()`. This masking effectively removes the user's control over how the program flows. 

This nine line program hides enough of the complexity of setting up the AVR core (a daunting task for most developers) that the Arduino is actually marketed toward children. So, how do we do the same task in python?

``` Python
import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,50):
        blink(11)  
GPIO.cleanup()
```
*This code was sourced from [RPiBlog](https://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html).*

While this code doesn't look much more complicated and is only 4 lines longer; it contains several additional *'gotcha's'* to catch you out while rushing through development of a test script:

**Imports:** Forgetting them is annoying, and makes you want to hurt your computer.

**Main loop:** Included a main loop? Is it in the right place? Will it turn into spaghetti code? 
  
```Python
if __name__ == "__main__" # WTF, now I'm even more confused
```
**Code structure:** This is probably the biggest point. Code that is rushed has no structure; sorry to the blogger who wrote the above example, but your code is a perfect representation of this. In python there are a hundred ways to code a setup procedure and a main loop. Developers in a hurry (Remember that everyone says at least once in their life "*I'll just make a quick python script*" and regrets it later) typically do not take time to carefully consider how to structure their quick and dirty script, and they certainly won't create detailed documentation explaining the flow of the program or how it's supposed to work. The ugly brick of an example above exemplifies a journalist on a deadline:  crappy code structure; no flexibility; minimal commenting.

In the real world eventually someone (possibly you) will have to come and maintain that script. With poor structure and no documentation they're going invest a lot of time re-learning the how the previous developer was thinking when he rushed out his ugly script.

The Conclusion:
---------------
That crappy Arduino IDE is better than Python, Vanilla C, or even in the right circumstances BASH. Arduino takes the complexities of software development from the user leaving them with just the tools needed to write a simple script quickly and well enough that anyone can understand it.

The Solution:
-------------
How can we reproduce this in python? Thankfully python has a powerful introspection engine, making it one of the most suited languages for this task. Firstly lets keep in mind that we don't want to modify any of the python language, simply provide a framework to allow the developer to focus their efforts. With this in mind it  makes sense to use python as the language for the framework. 

Firstly we need to build in python a runtime which loads the desired code file into the python VM and then executes functions from it. Thankfully with the help of a little bit of googling you can find that the module loader from the python runtime is exposed. This loader can be given a file (although unfortunately not a string) and will return to a loaded module ready to use and scarily possibly already executing code behind your back.

To match the behaviour of Arduino we need to handle imports for the user. PySketch does this very crudely; it loads a list of commonly used modules from a list and inserts them as fields into the sketch module. This has downsides, for example if you have a global variable called `time` in your sketch you will find that if it used to be `4` its now `types.ModuleType`. (always assign values to global variables in `setup()` to get around this.)

Once that is handled we need to construct a main loop that controls the program flow. Here we deviate from Arduino, by adding a `cleanup()` function. This accounts for the fact that the scripts are running on a PC not a microcontroller and that the system doesn't enter reset when the script ends. `cleanup()` allows for the freeing of resources and letting the developer put everything back how they found it. The main loop in pysketch behaves similar to this:

```Python
sketch = load_sketch(filename)
sketch.setup();
try:
    while True:
        sketch.loop(); 
except KeyboardInterrupt:
    print("Exiting") # If the user makes it stop, then stop.
except:
    raise # Any other error must be sent to the user.
finally:
    sketch.cleanup();
```

*Note this is a simplification and not the actual code from PySketch.*

And that's it; that's enough to make it work, but there are some things we can do to make it more useful. Firstly we can make the sketch loader support `#!` interpreter definitions, allowing sketches to really behave like scripts. This thankfully is as easy as making the loader take the file name as it's first argument, then adding `#!/usr/bin/python3` to the first line of the loader. This is functionality for free as the loader already had both of these things. 

The next useful thing we can do is allow the script to take arguments from the command line. This is where Python's introspection engine comes in handy again. We can use it to analyse the setup function and determine how many arguments it takes. Once we know this we can read in parameters from the command line, if there are too few we can throw an error, if there are too many then we can truncate the excess. This means that the script writer can just add arguments to the setup function without having to worry about passing the command line or checking enough parameters where provided.

That's everything that was written into PySketch. For intimate technical details please read the source on [Github](https://github.com/IGBC/PySketch), its relatively self explanatory and has lots of comments. The project is technically finished, but there are still some features I would like to play with and I would like to make the code generally better structured.

Ideas for the future:
------------------------

- Add some way of intelligently handling global variables.
- Add Python3.5 type support to the argument parser.
- Add a system for intelligently guessing which libraries are needed.
- Add some security features - Uphill battle.
- Improve Error Handing. 
- Improve Code Quality.
