# ABM-Assignment2
In this assignment I modified the *Demographic Prisoner's Dilemma on a Grid Model*. <br><br>

The entities of the model are agents and grid cells, and each grid cell is dwelled by an agent. Each 
agent  has  a  binary  ‘move’  variable  and  a  continuous  ‘score’  variable.  The  user  can  select 
scheduling type from ‘sequential’, ‘random’, and ‘simultaneous’ from the GUI. In each step, each 
agent will copy the ‘move’ of the neighbor with the highest ‘score’, and the ‘score’ of the agent 
will be updated based on its ‘move’ and all its neighbor’s ‘move’.<br><br>

I altered how each agent decides next move. In the new setting, each agent knows their neighbors’ 
strategies,  and  they  are  able  to  calculate  the  possible  scores  they  can  get  with  the  two  different 
moves. I assume that the agents do not have a strategy and naively decide their moves based on 
their  neighbors’  current  move.  I  want  to  see  how  simplification  of  the  strategy  may  affect  the 
number of cooperating agents. This is done in **step()** in `agent.py`.<br><br>

`model.py` and `agent.py` are the files for the new model. `model_old.py` and `agent_old.py` are files for the original model. <br><br>
Batch run for the new model can be run with the command line code <br>`python run_batch.py`.<br><br>
Batch run for the new model can be run with the command line code <br>`python run_batch_old.py`.<br><br>
