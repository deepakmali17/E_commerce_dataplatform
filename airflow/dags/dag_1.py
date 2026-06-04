from airflow.sdk import dag, task
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from pendulum import datetime
from pathlib import Path
import sys

AIRFLOW_HOME = Path("/opt/airflow")

print(AIRFLOW_HOME)

if str(AIRFLOW_HOME) not in sys.path:
    sys.path.insert(0, str(AIRFLOW_HOME))

@dag(
    dag_id="databricks_airflow_dag",
    schedule="5 * * * *",
    start_date=datetime(year=2026, month=6,day=3),
    catchup = False
)
def databricks_airflow_dag():
    ingestion_job = DatabricksRunNowOperator(
        task_id = "ingestion_job",
        databricks_conn_id = "databricks_default",
        job_id="1006954515064088"
    )

    transformation_job = DatabricksRunNowOperator(
        task_id = "transformation_job",
        databricks_conn_id = "databricks_default",
        job_id="417931534570679"
    )

    order_detail_job = DatabricksRunNowOperator(
        task_id = "gold_later_order_detail_jobjob",
        databricks_conn_id = "databricks_default",
        job_id="1095575216919616"
    )

    ingestion_job >> transformation_job >> order_detail_job

databricks_airflow_dag()
