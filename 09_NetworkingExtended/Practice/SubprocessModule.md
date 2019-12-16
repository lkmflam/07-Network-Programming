Subprocess Module
The subprocess module allows us to:

spawn new processes
connect to their input/output/error pipes
obtain their return codes
It offers a higher-level interface than some of the other available modules, and is intended to replace the following functions:

os.system()
os.spawn*()
os.popen*()
popen2.*()
commands.*()
We cannot use UNIX commands in our Python script as if they were Python code. For example, echo name is causing a syntax error because echo is not a built-in statement or function in Python. So, in Python script, we're using print name instead.

To run UNIX commands we need to create a subprocess that runs the command. The recommended approach to invoking subprocesses is to use the convenience functions for all use cases they can handle. Or we can use the underlying Popen interface can be used directly.
