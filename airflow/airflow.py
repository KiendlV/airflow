from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner" : "me",
    "retries" : 5,
    "retry_delay" : timedelta(minute=2)
}

with DAG(
    dag_id = "NASA_IMG_DAG",
    default_args=default_args,
    description = "DAG for getting img data and metadata",
    start_date= datetime(2024, 11, 3, 2),
    schedule_interval="@daily"
) as dag:   
    task1 = BashOperator(
        task_id = "NASA_TASK",
        bash_command="echo Hello world"
    )