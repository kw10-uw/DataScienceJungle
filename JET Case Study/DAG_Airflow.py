import time
from datetime import datetime
from airflow.models.dag import DAG 
from airflow.decorators import task 
from airflow.utils.task_group import TaskGroup
import pandas as pd 
from sqlalchemy import create_engine
import requests


@task 
def getcomicAPI():
    