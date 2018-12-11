import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='animal$$911',
    db='test')

cursor = mydb.cursor()

#Delete column 
sql_Delete_query = """DROP TABLE IF EXISTS test"""
cursor.execute(sql_Delete_query)


statement = '''
    CREATE TABLE test (Id INT PRIMARY KEY AUTO_INCREMENT, CountryCode VARCHAR(255), Country VARCHAR(255),SeriesCode VARCHAR(255),Indicators VARCHAR(255))
'''
cursor.execute(statement)

#country_code
#country
#series_code
#indicator
#year
#value


with open('mdg_export_trimmed.csv') as csvDataFile:
    csv_data = csv.reader(csvDataFile)
    i=4
    for row in csv_data:
        #print(row)
        statement = '''
            INSERT INTO test(CountryCode,Country,SeriesCode,Indicators)
            VALUES("%s", "%s", "%s", "%s") 
        ''' % (row[0],row[1], row[2],row[3]) 
        cursor.execute(statement)
#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")