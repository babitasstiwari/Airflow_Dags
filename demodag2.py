from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def create_response_instance():
    pass

def got_response():
    pass

def close_response_instance():
    pass

default_args = {
    'start_date': datetime(2024, 4, 16),
    'owner': 'airflow'
}

dag = DAG('BT_DAG_PO', default_args=default_args)
with dag: 
    task_1 = PythonOperator(task_id='Create_response_instance', python_callable=create_response_instance)
    task_2 = PythonOperator(task_id='Got_response', python_callable=got_response)
    task_3 = PythonOperator(task_id='Close_response_instance', python_callable=close_response_instance)
    task_1 >> task_2 >> task_3