import csv

# Escrevendo/Atualizando um arquivo CSV

fake_data_list = [
    ['col1;', 'col2', 'col3'],
    ['joã1o', 'value2', 'value3'],
    ['value1', 'value2', 'value3'],
    ['value1', 'value2', 'value3'],
]

fake_data_register = [
    {'name': 'joão', 'age': 20, 'email': 'joao@gmail.com'},
    {'name': 'joão', 'age': 20, 'email': 'joao@gmail.com'},
    {'name': 'joão', 'age': 20, 'email': 'joao@gmail.com'},
    {'name': 'joão', 'age': 20, 'email': 'joao@gmail.com'},
    {'name': 'joão', 'age': 20, 'email': 'joao@gmail.com'}
]

with open('fake_data.csv', 'w+', encoding='cp1252') as file:
    writer = csv.writer(file, delimiter=';') # Criando o objeto writer
    writer.writerow(fake_data_register[0].keys())
    for row in fake_data_register: # Maneira segura
        writer.writerow(row.values()) # Escrevendo cada linha
    # writer.writerows(fake_data_list) # Escrevendo todas as linhas
    
# Lendo um arquivo CSV

# with open('fake_data.csv', 'r', encoding='cp1252') as file:
#     reader = csv.reader(file, delimiter=';') # Criando o objeto reader
#     for row in reader: # Iterando sobre o objeto reader
#         print(row) # Printando cada linha

# Lendo e escrevendo um arquivo CSV

# with open('fake_data.csv', 'r+', encoding='cp1252') as file: # r+ -> read and write
#     writer = csv.writer(file, delimiter=';') # Criando o objeto writer
#     writer.writerow(fake_data_register[0].keys())
#     for row in fake_data_register: # Maneira segura
#         writer.writerow(row.values()) # Escrevendo cada linha
    # writer.writerows(fake_data_list) # Escrevendo todas as linhas

    # reader = csv.reader(file, delimiter=';') # Criando o objeto reader
    # for row in reader: # Iterando sobre o objeto reader
    #     print(row) # Printando cada linha
    
