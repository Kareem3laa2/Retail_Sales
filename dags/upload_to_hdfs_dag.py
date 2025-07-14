from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='retail_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    description="Upload local CSV to HDFS using bash script"
) as dag:

    upload_to_hdfs = BashOperator(
    task_id="upload_file",
    bash_command='docker exec retail_namenode \
                  hdfs dfs -mkdir -p /data/raw \
                  -put -f /data/Online_Retail.csv /data/raw',
)

