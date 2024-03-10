def format_records(records: list):
    formatted_records = [f'{record[0]} ---> {record[1]:.2f}' for record in records]
    return '<br>'.join(formatted_records)


def transform_time(times: list):
    transformation_time = [f'{time[0]} ---> {time[1]} --->{time[2]:.2f}' for time in times]
    return '<br>'.join(transformation_time)

def format_for_stutus_city(records: list):
    formatted = [f'{record[0]} - {record[1]} - {record[2]}' for record in records]
    return ' '.join(formatted)

