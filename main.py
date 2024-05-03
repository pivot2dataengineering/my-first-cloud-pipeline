from extract_transform import get_weather_data, parse_weather_data
from load import upload_to_gbq

# TODO: setting date ranges
start_date = "2024-04-01"
end_date = "2024-04-30"
# TODO: setting location
location = "Melbourne"

def etl_pipeline(
        start_date,
        end_date,
        location):
    # extract
    data = get_weather_data(start_date,
                            end_date,
                            location)
    # transform
    df = parse_weather_data(data,
                            start_date,
                            end_date)
    # load to bigquery
    upload_to_gbq(df)
    return "Operation: Successful"

if __name__ == '__main__':
    etl_pipeline(start_date,
                 end_date,
                 location)


