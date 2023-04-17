import csv
from testpages.models import Records

def run():
    file = open("C:/Users/sumey/software/Web/django_online_shopping/onlineShopping/postgresTest/testpages/scripts/100_sales_Records.csv")
    read_file = csv.reader(file)
    
    # #optional
    # Records.objects.all().delete() #  Records.objects.all().delete() deletes the previous values present in the table.
    
    count=1 #  To avoid the first row of the csv file
    
    for record in read_file:
        if count==1:
            pass
        else:
            print(record) #  Optional
            Records.objects.create(region=record[0], country=record[1], item_type=record[2], sales_channel=record[3])
        count+=1