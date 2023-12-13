import logging
from pathlib import Path

import mlflow
from pyspark.sql import SparkSession
from cwa.tasks.sample_etl_task import SampleETLTask
from cwa.tasks.sample_ml_task import SampleMLTask


def test_jobs(spark: SparkSession, tmp_path: Path):
    logging.info("Testing the ETL job")
    common_config = {"database": "default", "table": "sklearn_housing"}
    test_etl_config = {"output": common_config}
    etl_job = SampleETLTask(spark, test_etl_config)
    etl_job.launch()
    table_name = f"{test_etl_config['output']['database']}.{test_etl_config['output']['table']}"
    _count = spark.table(table_name).count()
    assert _count > 0
    logging.info("Testing the ETL job - done")

    logging.info("Testing the ML job")
    test_ml_config = {
        "input": common_config,
        "experiment": "/Shared/cwa/sample_experiment"
    }
    ml_job = SampleMLTask(spark, test_ml_config)
    ml_job.launch()
    experiment = mlflow.get_experiment_by_name(test_ml_config['experiment'])
    assert experiment is not None
    runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])
    assert runs.empty is False
    logging.info("Testing the ML job - done")


