from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
        'owner': 'lim',
        'depends_on_past':False,
        'start_date': datetime(2025,4,12),
        'email_on_failure':False,
        'email_on_retry':False,
        'retires':1,
        'retry_delay':timedelta(minutes=5),
    }

dag = DAG(
        'hello_airflow_dag',
        default_args = default_args,
        description='my example',
        schedule_interval = timedelta(days=1),
        )

sentence = "hello airflow dag. fast campus lecture! We can do it."

def print_word(word):
    print(word)

prev_task = None
for i, word in enumerate(sentence.split()):
    task = PythonOperator(
            task_id = f'print_word_{i}',
            python_callable = print_word,
            op_kwargs = {'word':word},
            dag=dag
            )
    if prev_task:
        prev_task >> task

    prev_task = task

