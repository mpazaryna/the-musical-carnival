# Python Virtual Environment

- https://towardsdatascience.com/virtual-environments-104c62d48c54
- https://realpython.com/python-virtual-environments-a-primer/

## What exactly is a virtual environment?

A virtual environment is a Python tool for dependency management and project isolation. They allow Python site packages (third party libraries) to be installed locally in an isolated directory for a particular project, as opposed to being installed globally (i.e. as part of a system-wide Python).

A virtual environment is just a directory with three important components:

- A site-packages/ folder where third party libraries are installed.
- Symlinks to Python executables installed on your system.
- Scripts that ensure executed Python code uses the Python interpreter and site packages installed inside the given virtual environment.

## Create the environment

```sh
% cd test-project/
% python3 -m venv venv/       # Creates an environment called venv/
```

## Activate

```sh
% source venv/bin/activate             
(venv) %                               # Fancy new command prompt
```

## Deactivate

When we’re done working on our project, we can exit the environment with

```sh
(venv) % deactivate
%                                    # Old familiar command prompt
```
