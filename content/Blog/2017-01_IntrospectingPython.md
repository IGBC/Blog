Title: Introspecting Python Functions
Date: 2017-02-19
Tags: PySketch, Sketches, Python, Scripts, Interpreter, Inspection, Programming

Toward the end of the [project article](/pysketch.html) for PySketch I pointed out that it would be more useful if it could detect which python modules you are using automatically, rather than guessing with a predefined list. Recently I have been working on this problem using Python's introspection engine.

Note that I am using python 3.5.2 that is packaged in Ubuntu 16.04*

I am just gonna say it now: *I do not want to parse Python source*, so lets go look at the introspection engine. 

Python uses the built in function `dir()` to do basic object inspection. In case you don't know in Python everything is expressed as an object, so `dir(True)` is valid code and it will return a list of attributes for the object:

```Python
>>> dir(True)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__',
 '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__',
 '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__',
 '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
 '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
 '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
 '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length',
 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

Most of the listed attributes are built in default attributes that we typically don't need to worry about, however we can find out which ones are common to all objects by creating an empty class:

```Python
>>> class Empty:
...     pass
... 
>>> e = Empty()
>>> dir(e)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__']
```

Everything you see here is part of Python's base object type, everything else is inherited. Most of these are handles to built in functions, provided so that the class can override them and/or respond to events. For example `__init__` should be familiar to anyone who has written a class in python before; it is the constructor, and it is provided for overriding from the base object definition.

So lets look at a sketch loaded with PySketch:
```
>>> import sketches
>>> loader = sketches.ModuleLoader("example.pys")
>>> s = loader.sketch
>>> dir(s)
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cleanup',
 'loop', 'setup'] 
```

As expected we have the same behaviour as in the class. Listed are the docstring, the file the module was loaded from, it's parent package, and the name for module. In all there is less here than I expected. We will politely ignore `__builtins__` as it exposes nothing useful for our goal. We also have the three functions we define in the sketch. Lets inspect the setup function of this sketch:

```Python
def setup():
    pin = 18
    clock = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(clock, GPIO.OUT)
    GPIO.output(pin, GPIO.High)
    time.sleep(1000)
    GPIO.output(pin, GPIO.Low)
```

*Original Code*

```Python
>>> f = s.setup
>>> dir(f)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
 '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
 '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__',
 '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

*`dir()` output*

I have stripped out the values populated in the empty class from above. While some of them may contain useful data I'm pretty sure most of them are useless inherited values which just allow Python to do it's thing; this is what we are left with:

```Python
>>> dir(f) # With the values present in Empty() from above removed 
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__',
 '__kwdefaults__', '__name__', '__qualname__']
```

*Ahh that's more manageable*

The meanings of all these cryptic attributes are tabulated below. The types were extracted from the python console with the `type()` command. :

| Symbol:          | Type:          | Value: |
|------------------|----------------|--------|
|`__annotations__` | dict           | Dictionary containing function annotations as defined in [PEP-3107](https://www.python.org/dev/peps/pep-3107/#accessing-function-annotations). Not To be confused with function decorators. |
|`__call__`        | method-wrapper | "Pointer" to the function executable; can be called, can be overridden |
|`__closure__` 	   | NoneType       | If you understand function closures you will understand this; I don't. |
|`__code__`        | class 'code'   | Class wrapping the code the function calls |
|`__defaults__`    | NoneType       | Contains the default values for positional and keyword arguments. (Not accessible in the interpreter) |
|`__get__`         | method-wrapper | Function that returns it's parent (the defined function) for rebinding to objects |
|`__globals__`     | dict           | Dictionary of the scope the function was declared in |
|`__kwdefaults__`  | NoneType       | Contains the default values for keyword only arguments. (Not accessible in the interpreter) |
|`__name__`        | string         | Literally the token written after 'def' |
|`__qualname__`    | string         | Qualified name for the function, providing a name aware of scope and nesting. See [PEP-3155](https://www.python.org/dev/peps/pep-3155/) |

Unfortunately for us most of these attributes are metadata and scope; little of it relates to the contents of the function call. Therefore the only attribute of any real interest to us is `__code__`.

```Python
>>> dir(f.__code__)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount',
 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars',
 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
```

*Output from inspecting `__code__` object*

```Python
>>> dir(f.__code__) # With the values present in Empty() from above removed 
['co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags',
 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize',
 'co_varnames']

# Oh look all the __*__ values evaporated
```

*Output from inspection of the code object with the base attributes removed*

If we strip attributes we find in the empty class again we end up with a code object that contains only fields relevant to a method. While a lot of these can be worked out with context I think it's best to refer to the documentation here. Unfortunately the python documentation is notoriously bad and despite some exhaustive searching the closest I could find to official documentation for the `__code__` class comes from the "inspect" module documentation, which can be found [here](https://docs.python.org/3.5/library/inspect.html). This information was incomplete, however I was able to fill in the blanks using [this](https://stackoverflow.com/a/16123158) stack overflow answer. The types were extracted from the python console with the `type()` command.


| Symbol:          | Type: | Value: |
|------------------|-------|--------|
|co_argcount       | int   | number of arguments (not including * or ** args) |
|co_cellvars       | tuple | tuple containing names of local variables referenced by nested functions |
|co_code 	       | bytes | string of raw compiled bytecode |
|co_consts         | tuple | tuple of constants used in the bytecode |
|co_filename       | str   | name of file in which this code object was created |
|co_firstlineno    | int   | number of first line in Python source code |
|co_flags          | int   | bitmap of flags about the object |
|co_freevars       | tuple | tuple containing the names of free variables |
|co_kwonlyargcount | int   | number of keyword-only arguments |
|co_lnotab         | bytes | encoded mapping of line numbers to bytecode indices |
|co_name 	       | str   | name with which this code object was defined |
|co_names          | tuple | tuple of names of local variables |
|co_nlocals        | int   | number of local variables |
|co_stacksize      | int   | virtual machine stack space required |
|co_varnames       | tuple | tuple of names of arguments and local variables |

Only two of these are interesting: "co_names" and "co_varnames". Despite their vague definitions in the documentation from testing I haven't seen a variable show up in both varnames and names. "co_varnames" appears to be variables locally defined within the function whereas "co_names" are tokens used with a global scope. So when searching for modules used their values are going to fall into "co_names".

There is however a problem; "co_names" is completely ungrouped with the order determined by the order tokens are used in the source. For example look at the "co_names" field for our setup function:

```Python
>>> f.__code__.co_names
('GPIO', 'setmode', 'BCM', 'setup', 'OUT', 'output', 'High', 'time', 'sleep', 'Low')
>>>
>>> f.__code__.co_varnames
('pin', 'clock')

```

*The output of "co_names" is completely useless*

This problem is made worse by the fact that these tokens are completely uninspectable (they are just strings). Yes it's objects all the way down in python, but we've reached the bottom of the pile. The "co_code" attribute is actually the bytecode that is directly fed to the virtual machine when the function is called. The code is already compiled at this point, but apparently not linked (again see the stack overflow answer above) so the tokens don't lead to other objects, they're just strings. So the question is... *Now What?*

This method has revealed the tokens used in the function, so theoretically these tokens could be one by one attempted to be imported by the PySketch interpreter, skipping them if they are not found; however this is a pretty crappy hack. There are some possible further routes to explore, exploiting either the ImportLib or PIP, however as this article has been waiting to be published for nearly a month I think I will for now have to accept defeat. 

Stay tuned for the next instalment of _"Why won't the f*cking interpreter let me do that???!!!"_

__ - SEGFAULT__

_*I think it's 16.04; I'm using Linux mint 18 which uses the Ubuntu apt repos._

