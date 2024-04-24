
import sys
sys.path.append('../Matlab2Py/')

from mat_engine import Engine

import numpy as np
import random


def init_simulator(SIMULATION_PATH, model_name, simulation_type='normal', ):
    #Here you setup your simulation configuration & initalzie necessary variables 


    MODEL_PATH = f"{SIMULATION_PATH}{model_name}.slx"
    
    eng = Engine(model_path = MODEL_PATH, sim_path = SIMULATION_PATH, model_name = model_name, simulation_type='normal')
    eng.load_engine()
    #Run the simple_sim/init.m to initalize theta
    eng.run_engine_script('init')
    eng.set_simulation_mode(s_mode='Normal')

    if eng.sim_type == 'sparsesbs':
        # 1 second
        STEP_SIZE = 1
        eng.set_step_size(STEP_SIZE)  
    return eng

def run_simulation(eng, theta : list[3]):
    eng.set_param(block_path = "gau", value = random.randint(0, 1345), type = "seed", )
    eng.set_param(block_path = "theta", value = theta )
    eng.start_simulation()
    return eng.get_ws_value(attribute = 'out.simout')

def simulator(eng, inputs):
    return np.array([run_simulation(eng, theta) for theta in inputs]).squeeze()


if __name__ == '__main__':

    #DEBUG Section
    # Start MATLAB engine
    SIMULATION_PATH = 'simple_sim/'
    model_name = 'test'

    eng = init_simulator(SIMULATION_PATH=SIMULATION_PATH, model_name=model_name)
   
    for _ in range(5):


        print(simulator(eng, [[1, 5, random.randint(0,25)]]))

