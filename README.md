# PSEC Analysis

Miles Lucas - Iowa State University

This code serves as a simple parsing tool for the PSEC data created by Dr. Eric Oberla's PSEC acdc-daq.

## Requirements

- Python 3.4+
- numpy
- matplotlib

## Data Format

Eric's data output is laid out in a text file with the following format

![dat file format](http://i.imgur.com/6io2RbH.png)

## Usage

```
In [1]: import Analysis as ana

In [2]: data, ped = ana.load_data('data/test.acdc.dat', 50)

In [3]: ccTimeStampLo = data[32, :, 37]

In [4]: print(ccTimeStampLo)
[ 1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.
  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.
  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.
  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.
  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.  1617.]

In [5]: plot = ana.plot_event(data, ped, 2, event=25)
```
