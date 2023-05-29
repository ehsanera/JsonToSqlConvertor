import json

def convert_json_to_sql(json_file, table_name):
    with open(json_file, 'r') as file:
        data = json.load(file)

    sql_statements = []
    for item in data:
        columns = ', '.join(item.keys())
        values = ', '.join([f"'{value}'" for value in item.values()])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        sql_statements.append(sql)

    return sql_statements

states_sql = convert_json_to_sql('states.json', 'state_table')
cities_sql = convert_json_to_sql('cities.json', 'city_table')

# Write the SQL statements to files
with open('states.sql', 'w') as file:
    file.write('\n'.join(states_sql))

with open('cities.sql', 'w') as file:
    file.write('\n'.join(cities_sql))
