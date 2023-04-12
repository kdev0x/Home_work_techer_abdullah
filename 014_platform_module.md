# Platform module
platform showes you youre operating system (OS) and python version and the hardware you are using
there a lot of command yet we will focuse on now is the platform command, the platfortm command showes you the platform you are using
## Example
```python
import platform
print(platform.platform())
``` 
## this will output youre full OS
yet some times you will not need al of that information so you could use the system command
## Example
```python
print(paltform.system())
```
### Somtimes you don't care about the OS and you want the hardeware you could use the matchine command
## Example
```python
print(paltform.machine())
``` 
## this will output youre matchine type
what if you want the proccer you could use the processor command
## Example
```python
print(paltform.processor())
``` 
### what if you dont care about the devise and what information about the version of python you are usiing you could use the implementaion command
## Example
```python
print(paltform.python_implementaion)
```
### this will output the version of python that you are using
some times you dont want the python version as a string you want it as a tuple you could use the version_tuple command
### Example
```python
 print(platform.python_version_tuple())
```
### this will output he python version not as a string yet as a tuple

