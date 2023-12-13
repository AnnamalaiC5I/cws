import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from cwa.common import Task


class SampleMLTask(Task):
    
    def check_sum(self,a,b):
        print ("Working??")
        return (a+b)
    
    def launch(self):
        self.logger.info("Launching sample ML task")
        #mlflow.set_experiment(self.conf["experiment"])
        self.check_sum(5,6)
        self.logger.info("Sample ML task finished")

# if you're using python_wheel_task, you'll need the entrypoint function to be used in setup.py
def entrypoint():  # pragma: no cover
    task = SampleMLTask()
    task.launch()

# if you're using spark_python_task, you'll need the __main__ block to start the code execution
if __name__ == '__main__':
    entrypoint()
