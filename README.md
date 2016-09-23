# Multiplot2D

## Description

Multiplot2D is a wrapper for the matplotlib library that simplifies the development of high quality plots for reports and papers. matplotlib is highly flexible and can do almost anything. However, it's wealth of features and somewhat difficult-to-remember interface make it cumbersome to produce the kinds of plots that are typically needed for dynamics and control work (i.e. figures with many subplots).

Multiplot2D wraps much of the most useful matplotlib functionality into an interface that tries to be consistent and intuitive. It also lends itself well to use in other applications that need to create figures and subplots automatically.

The goal of the Multiplot2D interface is to cover about 80% of use cases and minimize lines of code. For cases where especially fine grained control of subplots and figures is required, Multiplot2D can still be used to do most of the work because Multiplot2D offers access to the underlying subplots and figures that are stored inside the Multiplot2D interface. The full matplotlib library can then be applied to these underlying subplots and figures.

## Installation

We hope to have a Python pip package available soon.
In the meantime, here is how to install on Linux systems:

```bash
git clone https://github.com/dwhit15/Multiplot2D/tree/master
cd Multiplot2D
# add this directory to PYTHONPATH in ~/.bashrc
echo export PYTHONPATH=${PYTHONPATH}:"$(cd "$(dirname "$1")"; pwd)/$(basename "$1")" >> ~/.bashrc
source ~/.bashrc
```



## Documentation

The documenation is about 75% complete.
It is written inline the code using Sphinx.

We hope to have a page on [readthedocs](https://readthedocs.org/) soon.
