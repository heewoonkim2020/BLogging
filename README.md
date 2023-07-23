# BLogging
Better Logging for Python

## About
So, what is **BLogging**? It is basically a much better logging module than the preinstalled `logging` module. It supports **colors, timestamps, custom formats**, and much more! The colors work best on the iTerm2 Terminal, so keep that in mind.

## Installation
Follow the steps below to install BLogging globally on your global environment, or a virtual environment like `conda` or `pyenv`.   
    
**Type the following commands in your terminal:**     
1. `pyenv activate [VIRTUALENV-NAME]` or `conda activate [VIRTUALENV-NAME]` to make sure you are in the right environment for your project. You can skip this and go to step 2 immediately if you do not use a virtualenv or venv for your projects.     
2. If you are using a virtualenv or on Windows, type this command: `pip install git+https://github.com/heewoonkim2020/blogging`. If not, and you are on Linux or Unix, you may have to replace `pip` with `pip3` from the command above. If that doesn't work as well, try replacing `pip` or `pip3` with `python3 -m pip`.
3. In your project, add the following code:
   ```py
   from blogging import Logger, CustomFormat
   # your modules here
   example_logger = CustomFormat.example_format()
   logger = Logger(format=example_logger)

   logger.info('Hello world!')
   logger.warn('Uh oh, something bad will happen.')
   print(1 / 0)
   ```
4. That's all steps completed! Check the **Wiki** for more information.