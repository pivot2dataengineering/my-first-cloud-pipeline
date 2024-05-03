import pandas_gbq
import pandas as pd


# TODO: Set the project ID
project_id="my-data-pipelines-422215"

# TODO: Set the dataset ID
dataset_id="weather_data"

# TODO: Set the table ID
table_id="melbourne_weather_table"

table_schema = [
    {"name": "DATE", "type": "DATE"},
    {"name": "MAX_TEMP", "type": "FLOAT"},
    {"name": "MIN_TEMP", "type": "FLOAT"},
    {"name": "AVG_TEMP", "type": "FLOAT"},
    {"name": "TOTAL_PRECIPITATION", "type": "FLOAT"},
]

def upload_to_gbq(df: pd.DataFrame,
                  project_id: str = project_id,
                  dataset_id: str = dataset_id,
                  table_id: str = table_id,
                  table_schema: list = table_schema):

    pandas_gbq.to_gbq(
            dataframe=df,
            project_id=project_id,
            destination_table=f"{dataset_id}.{table_id}",
            if_exists='append',   # 'replace'
            table_schema=table_schema,
            progress_bar=True,
           )

if __name__ == '__main__':
    df = pd.DataFrame(
                    {'DATE': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'],
                    'MAX_TEMP': [10.4, 15.2, 18.3, 20],
                    'MIN_TEMP': [5, 10, 15, 20],
                    'AVG_TEMP': [12, 18, 24, 30],
                    'TOTAL_PRECIPITATION': [0.1, 0.2, 0.3, 9.9],
                   })
    upload_to_gbq(df)