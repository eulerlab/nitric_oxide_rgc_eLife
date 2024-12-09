import numpy as np
from scipy.cluster.hierarchy import dendrogram
import scipy



def compute_interspike_intervals(spike_times, sampling_rate=20e+3):

    interspike_intervals = np.diff(spike_times)
    interspike_intervals = interspike_intervals.astype(np.float64)
    interspike_intervals = interspike_intervals / sampling_rate

    return interspike_intervals

def compute_number_of_rpv_spikes(spike_times, duration=2.0, sampling_rate=20e+3):
    
    isis = compute_interspike_intervals(spike_times, sampling_rate=sampling_rate)
    nb_isis = np.count_nonzero((isis <= 1e-3 * duration)&(isis>0))
    
    return nb_isis

def compute_refractory_period_violation(spike_times, duration=2.0, sampling_rate=20e+3):
    
    
    """
    spike_times : the spike times of the neuron to study
    duration : the duraiton of the refractory period, in ms
    sampling_rate : the sampling rate of the recording device
    """

    isis = compute_interspike_intervals(spike_times, sampling_rate=sampling_rate)
    nb_isis = len(isis)
    rpv = float(np.count_nonzero((isis <= 1e-3 * duration)&(isis>0))) / float(nb_isis) *100

    return rpv


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)
