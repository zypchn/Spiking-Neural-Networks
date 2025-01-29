import time

def circle_for_lif(exceed_thr, loop, new_neurons, neuron):
    
    class SysActivity:
        def __init__(self, neuron, new_neurons):
            self.neuron = neuron
            self.new_neurons = new_neurons
    
    dns = 6        
    sys_activity = [SysActivity() for _ in range(6)]
            
    while exceed_thr > 0 and loop < 6:
        neurons = new_neurons
        sys_activity[loop].neuron = neuron
        sys_activity[loop].new_neurons = new_neurons
        loop = loop + 1
        see_act_map()
        time.sleep(4)
        events_of_fire()