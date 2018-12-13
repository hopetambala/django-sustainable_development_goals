import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='animal$$911',
    db='unsdg')

cursor = mydb.cursor()

#Delete column 
sql_Delete_query = """DROP TABLE IF EXISTS temp_country_target_indicator"""
cursor.execute(sql_Delete_query)


statement = '''
    CREATE TABLE temp_country_target_indicator (temp_country_target_indicator INT PRIMARY KEY AUTO_INCREMENT, CountryCode VARCHAR(255), Country VARCHAR(255), SeriesCode VARCHAR(255),Indicator VARCHAR(255),Indicator_Value VARCHAR(255), Year YEAR(4))
'''
cursor.execute(statement)

#country_code
#country
#series_code
#indicator
#year
#value

i=4
years = list(range(1990,2019))

for year in years:
    with open('mdg_export_trimmed.csv') as csvDataFile:
        csv_data = csv.reader(csvDataFile)
        next(csv_data, None)  # skip the headers

        
        data = []

        for row in csv_data:
            myInsert = (row[0],row[1],row[2],row[3],row[i],year)
            data.append(myInsert)
        i+=1

        statement = '''
            INSERT IGNORE INTO temp_country_target_indicator(CountryCode,Country,SeriesCode,Indicator,Indicator_Value,Year)
            VALUES(%s, %s, %s, %s,%s,%s) 
        '''
        cursor.executemany(statement,data)
        mydb.commit()
    print('Finished Year: ',year) 
mydb.commit()

#Get rid of empty rows
statement = '''
DELETE from temp_country_target_indicator WHERE !temp_country_target_indicator.Indicator_Value
'''

cursor.execute(statement)
cursor.close()
print("Done")