import csv

with open('Titanic.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)
    
    with open('newTitanic.csv','w') as new_csv_file:
        csv_writer=csv.writer(new_csv_file)
        
        for line in csv_reader:
            csv_writer.writerow(line)
            
            
with open('Titanic.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)
            
            
            