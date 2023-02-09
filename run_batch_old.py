from model_old import PdGrid
from mesa.batchrunner import FixedBatchRunner
import pandas as pd

fixed_parameters = {
	'height': 50,
	'width': 50,
}

schedule_types = list(PdGrid.schedule_types.keys())

parameters_list = [{"payoffs": 0.5, "schedule_type": schedule_types[0]},
                   {"payoffs": 0.5, "schedule_type": schedule_types[1]},
                   {"payoffs": 0.5, "schedule_type": schedule_types[2]},
                   {"payoffs": 0.9, "schedule_type": schedule_types[0]},
                   {"payoffs": 0.9, "schedule_type": schedule_types[1]},
                   {"payoffs": 0.9, "schedule_type": schedule_types[2]},
                   {"payoffs": 1, "schedule_type": schedule_types[0]},
                   {"payoffs": 1, "schedule_type": schedule_types[1]},
                   {"payoffs": 1, "schedule_type": schedule_types[2]},
                   {"payoffs": 1.6, "schedule_type": schedule_types[0]},
                   {"payoffs": 1.6, "schedule_type": schedule_types[1]},
                   {"payoffs": 1.6, "schedule_type": schedule_types[2]}]

batch_run = FixedBatchRunner(PdGrid, parameters_list, fixed_parameters, iterations=5, max_steps = 50)

batch_run.run_all()

ordered_dict = batch_run.get_collector_model()

step_dict = {'payoffs':[], 'schedule_type':[], 'cooperating_agents':[]}
for key, value in ordered_dict.items():
    for i in value['Cooperating_Agents']:
        step_dict['payoffs'].append(key[0])
        step_dict['schedule_type'].append(key[1])
        step_dict['cooperating_agents'].append(i)

step_df = pd.DataFrame(step_dict)
step_df.to_csv('PdGrid_model_step_batch_run_data_old.csv')
