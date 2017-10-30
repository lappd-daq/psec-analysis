import numpy as np
import pandas as pd
import os


PSEC_CELLS = 256
N_COLS = 32
N_CHS = 30

def load_data(filename):
    '''
    Parses the text file for PSEC analysis

    Arguments
    ---------
    filename: string
        the full path to the txt file containing the data

    num_events: int
        The number of events recorded in the data file. If this is too small, data will not be parsed and if it is too large, the parsing will reach EOF prematurely

    Returns
    -------
    data: 3d-array
        An array with the form [Channel, Event, Sample] containing the event data and metadata. There are 33 channels, the first 2 are timing values. The next 30 are data channels. The last channel is metadata. See form_metadata.cpp in Eric's source code for an explanation of the metadata. There are 'num_events' events. Each event has 256 samples.

    ped: 2d-array
        An array with the form [Channel, Sample] containing the pedestal data. The channel layout is the same as the data array and there are still 256 samples. Note that the 2nd and 33rd columns of this array are all zeros.
    '''
    raw = np.genfromtxt(filename)[:, 1:]
    n_events = int(len(raw) / PSEC_CELLS - 1)
    n_boards = int(len(raw.T) / N_COLS)

    indices = [range(n_boards), range(n_events), range(PSEC_CELLS)]
    ch_names = ['{:d}'.format(n+1) for n in range(N_CHS)]
    cols = ['Wrap', *ch_names, 'Meta']
    data = pd.DataFrame(index=pd.MultiIndex.from_product(indices, names=['Board', 'Event','Sample']), columns=cols)

    boards = np.array([raw.T[N_COLS * n:N_COLS * (n+1)] for n in range(n_boards)])
    for b, board in enumerate(boards):
        data.loc[b] = board[:, PSEC_CELLS:].T
        data.loc[b, ch_names] = data.loc[b, ch_names].values - np.tile(board[1:-1, :PSEC_CELLS], n_events).T

    return data

def plot_event(data, board, event, channel):
    '''
    Simple plot tool for quick use the data array

    Arguments
    ---------
    data: 3d-array
        The data array from the load_data command. See that documentation for more information

    ped: 2d-array
        The ped array from the load_data command. See that documentation for more information

    ch: int
        The channel to plot. Note: this is the actual data channel (eg channel 2 from the psec board would input 2) not the column of the data array.

    event: int, optional
        The event to plot (Default=0)
    '''

    import matplotlib.pyplot as plt
    import collections

    if not isinstance(board, collections.Iterable):
        board = [board]
    if not isinstance(event, collections.Iterable):
        event = [event]
    if not isinstance(channel, collections.Iterable):
        channel = [channel]

    plt.style.use('seaborn')
    plt.figure()
    plt.title('Board {}, Channel {}, Event {}'.format(board, channel, event))
    [[[plt.plot(data[str(ch)].loc[b, e].values, label='EBC ({},{},{})'.format(e, b, ch)) for ch in channel] for b in board] for e in event]
    plt.legend()
    plt.xlabel('Time (100 ps)')
    plt.ylabel('ADC Counts')
    plt.show()


if __name__=='__main__':
    pass
