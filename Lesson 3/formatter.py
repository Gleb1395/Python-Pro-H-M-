def format_records(records: list):
    formatted_records = [f'{record[0]} ---> {record[1]:.2f}' for record in records]
    return '<br>'.join(formatted_records)


def transform_time(times: list):
    transformation_time = [f'{time[0]} ---> {time[1]} --->{time[2]:.2f}' for time in times]
    return '<br>'.join(transformation_time)
