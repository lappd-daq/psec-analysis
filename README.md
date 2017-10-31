# PSEC Analysis

Miles Lucas - Iowa State University

This code serves as a simple parsing tool for the PSEC data created by Dr. Eric Oberla's PSEC acdc-daq.

## Requirements

- Python 3.4+
- numpy
- matplotlib (only for plotting)

## Data Format

Eric's data output is laid out in a text file with the following format

|                            |   0   |     1      |   2-31   | 32       | k*32 + 1 | k*32 + (2-31) | k*32 + 32 |
| -------------------------: | :---: | :--------: | :------: | :--------: | :-----: | :----------: | :-------: |
|               **0 to 255** | Count |     0      | Ped data | 0        | 0 | Ped data | 0 |
| **256 to (n+1) x 256 - 1** | Count | Wraparound |   Data   | Metadata | Wraparound | Data | Metadata |

Where n is the event number and k is the board number

The metadata is stored in the 33rd column of each event and has the following values

Value | Name | Description
-: | :-: | :-
0 | count |
1 | aa |
2 | time |
3 | datetime |
4 | events |
7 | bin count rise |
8 | self trig settings 2 |
9 | sys coinc width |
10 | coinc num chips |
11 | coinc num chans |
12 | self trig settings |
13 | trig en |
14 | trig wait for sys |
15 | trig rate only |
16 | trig sign |
17 | use sma trig in |
18 | use coinc settings |
19 | use trig valid as reset |
20 | coinc window |
21 | reg self trig |
22 | counts of sys no local |
23 | sys trig count |
24 | resets from firmw |
25 | firmware version |
26 | self trig mask |
27 | dig timestamp lo |
28 | dig timestamp mid |
29 | dig timestamp hi |
30 | dig event count |
31 | event count |
32 | timestamp hi |
33 | timestamp mid |
34 |timestamp lo
35 | CC bin count |
36 | CC event count |
37 | CC timestamp lo |
38 | CC timestamp mid |
39 | CC timestamp hi |
40-44 | RO count | RO count for each chip
45-49 | RO target count | for each chip
50-54 | vbias | for each chip
55-59 | trigger threshold | for each chip
60-64 | RO DAC value | for each chip
70-99 | self trig scalar | for each ac channel
110 | time from valid to trig |
111 | firmware reset time |
112 | last coinc num chans |


## Usage

```python
In [1]: import Analysis as ana

In [2]: data = ana.load_data('data/test2.acdc.dat')

In [3]: ccTimeStampLo = data['Meta'].loc[0, 5, 37] # 0th board, 5th event

In [4]: print(ccTimeStampLo)
1617

In [5]: plot = ana.plot_event(data, board=0, event=25, channel=2)
```
