import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='animal$$911',
    db='unsdg')

cursor = mydb.cursor()

#Delete table 
sql_Delete_query = '''DROP TABLE country_target_indicator'''
cursor.execute(sql_Delete_query)


statement = '''
CREATE TABLE IF NOT EXISTS country_target_indicator (   
	country_target_indicator_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,   
	country_area_id INT (255) NOT NULL,  
    indicator_id INTEGER NOT NULL,
    countrycode VARCHAR(255),
    seriescode VARCHAR(255),
    year YEAR(4),
    indicator_value VARCHAR(255),
    PRIMARY KEY (country_target_indicator_id),   
    FOREIGN KEY (country_area_id) REFERENCES country_area(country_area_id)     
		ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (indicator_id) REFERENCES indicator(indicator_id)     
		ON DELETE CASCADE ON UPDATE CASCADE );
'''
cursor.execute(statement)


numberOfcsvs = list(range(0,50))
for number in numberOfcsvs:
    with open('country_target_indicators_0.csv') as csvDataFile:
        csv_data = csv.reader(csvDataFile)
        next(csv_data, None)  # skip the headers
        
        data = []
        for row in csv_data:
            myInsert = (row[0],row[1],row[2],row[3],row[4],row[5])
            data.append(myInsert)
        statement = '''
            INSERT IGNORE INTO country_target_indicator(country_area_id,indicator_id,countrycode,seriescode,year,indicator_value)
            VALUES(%s, %s, %s, %s,%s,%s) 
        '''
        cursor.executemany(statement,data)
        mydb.commit()
        print("CSV: " + str(number)+ " done")
#Get rid of empty rows

#statement = '''
#    DELETE from temp_country_target_indicator WHERE !temp_country_target_indicator.Indicator_Value
#'''

#cursor.execute(statement)
cursor.close()
print("Done")