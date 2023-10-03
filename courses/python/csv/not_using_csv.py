fake_data_list = [
    ['col1;', 'col2', 'col3'],
    ['value1', 'value2', 'value3'],
    ['value1', 'value2', 'value3'],
    ['value1', 'value2', 'value3'],
]

with open('fake_data.csv', 'w', encoding='utf-8') as file:
    for row in fake_data_list:
        file.write(f'{row[0]};{row[1]};{row[2]}\n') # Maneira não segura
    
