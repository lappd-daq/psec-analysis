import numpy as np
import pandas as pd
import os


PSEC_CELLS = 256
N_COLS = 32
N_CHS = 30

def load_data(filename, save_data=False):
    '''
    Parses the text file for PSEC analysis

    Arguments
    ---------
    filename: string
        the full path to the text file containing the data

    save_data: boolean (optional)
        If set to True, it will save the loaded data frame into 'filename.xlsx' (default=False)

    Returns
    -------
    data: DataFrame
        A pandas dataframe using a multiindex with levels (board, event, sample) and columns for each channel plus wrap
        constant and metadata. For example, to get the data from channel 2 on board 0 for events 3 through 5, you would
        call data['2'].loc[0, 3:5]

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

    if save_data:
        data.to_excel(filename + '.xlsx')

    return data

def plot_event(data, board, event, channel):
    '''
    Simple plot tool for quick use of the data DataFrame. Lists can be used to plot, but all the data will be on the
    same plot.

    Arguments
    ---------
    data: DataFrame
        The data frame from the load_data command. See that documentation for more information

    board: int or list
        The board/s to plot

    event: int or list
        The event/s to plot

    channel: int or list
        The channel/s to plot


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
