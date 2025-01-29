import numpy as np
import matplotlib.pyplot as plt

circle_for_lif = "LIF\circle_for_lif.py"
events_of_fire = "LIF\events_of_fire.py"

def neurons_for_stoch():
    
    class Struct:
        def __init__(self, col, raw):
            self.col = col
            self.raw = raw
            self.neuron_wmat = []
    
    class Neuron:
        def __init__(self):
            self.firid = []
            self.Aptime = []
    
    dns = 6
    neuron_num = dns * dns
    sir = 0
    cr = 6
    
    struct_of_each_neuron = []
    
    for i in range(dns):
        for g in range(dns):
            sir += 1
            # str_of_each_neuron[sir]["col"] = i
            # str_of_each_neuron[sir]["raw"] = g
            """
            struct_of_each_neuron.append({
                "col": i,
                "raw": g
            })
            """
            struct = Struct(i, g)                       # creating a Struct object with
            struct_of_each_neuron.append(struct)        # appending the Struct object to the list
            
    neuron = [Neuron() for _ in range(16)]      # creating a list of 16 Neuron objects
    
    rand_neuron = 5
    size = neuron_num // 2                  # ensuring that size is an int for creating the neuron_wmat list
    neuron_wmat = np.zeros((size, size))
    th_w = 0.5
    init = 1
    
    for i in range(neuron_num):
        for g in range(neuron_num):
            if i == g:
                struct_of_each_neuron[i].neuron_wmat[g] = 0
            else:
                neuron_wmat[i][g] = np.random.rand()
                if (neuron_wmat[i][g] > th_w):
                    struct_of_each_neuron[i].neuron_wmat[g] = neuron_wmat[i][g]
                else:
                    struct_of_each_neuron[i].neuron_wmat[g] = 0
    
    inc = 15
    loop = 0       
    dt = 0.01
    num = np.random.randint(1, neuron_num // 2)
    new_neurons = np.random.sample(range(neuron_num), round(num/2))     # produces a list of unique random integers
    firsts = new_neurons.copy()
    neurons = new_neurons.copy()
    dist = np.array((neuron_num, neurons.shape[1]))
    
    for ai in range(neuron_num):
        for ah in range(neurons.shape[1]):
            dis1 = abs(struct_of_each_neuron[ai].col - struct_of_each_neuron[neurons[0, ah]].col)   # neurons is a numpy array
            dis2 = abs(struct_of_each_neuron[ai].raw - struct_of_each_neuron[neurons[0, ah]].raw)
            dist[ah, ai] = dt * (dis1 + dis2) + 10
    
    exceed_thr = 0
    if (len(neurons) > 5):
        all_neurons_spike = np.zeros((neuron_num, 2))
        spike_time = 0
        zmap = np.zeros((dns, dns))
        zmap[new_neurons] = 1
        plt.imshow(zmap)
        exec(open(circle_for_lif).read())   # exec() mimics the MATLAB script logic
        exec(open(events_of_fire).read())
    else:
        haaaa = 1