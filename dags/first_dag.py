from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 

default_args = {
    'owner': 'Daulet',
    'retries': 1
}

with DAG(
    dag_id = 'my_script',
    default_args = default_args,
    start_date = datetime(2026,6,28),
    schedule_interval = '@daily',
) as dag:

    task1 = BashOperator(
        task_id = 'perv_zad',
        bash_command = 'echo "Privet"'
    )
    task2 = BashOperator(
        task_id = 'vro_zad',
        bash_command = 'date'
    )


    task1 >>task2