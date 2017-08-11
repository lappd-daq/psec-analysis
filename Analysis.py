import matplotlib.pyplot as plt
import numpy as np
import os

NUM_SAMPLES = 256
NUM_COLS = 33

def load_data(filename, num_events):
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
    data = np.genfromtxt(filename)
    ped = data[:NUM_SAMPLES].T

    channel_data = [[
            data[NUM_SAMPLES * (i + 1):(i + 2) * NUM_SAMPLES, ch]
         for i in range(num_events)
        ] for ch in range(NUM_COLS)]

    return (np.asarray(channel_data), ped)

def plot_event(data, ped, ch, event=0):
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

    plt.style.use('seaborn')
    plt.figure()

    plt.plot(data[ch + 1, event] - ped[ch+1], label='Evt:{}'.format(event))
    plt.legend()
    plt.title('Channel:Event | {}:{}'.format(ch, event))
    plt.xlabel('Time (100 ps)')
    plt.ylabel('ADC Counts')
    plt.gca().invert_yaxis()
    plt.show()


if __name__=='__main__':
    pass
