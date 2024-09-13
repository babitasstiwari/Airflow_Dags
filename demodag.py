from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define default arguments
default_args = {
        'start_date':datetime(2024, 4, 16),
        'owner': 'airflow'
}

dag = DAG('BT_DAG_DO', default_args=default_args)
with dag: 
    task_1 = DummyOperator(task_id='fetch_stock_price_of_day')
    task_2 = DummyOperator(task_id='extract_closing_price_of_day')
    task_3 = DummyOperator(task_id='save_the_price_to_file')
    task_1 >> task_2 >> task_3  # Define dependencies 
    # task_2 is downstream of task_1
    # task_1 is upstream of task_2