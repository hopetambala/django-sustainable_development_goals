
USE unsdg;

/*
  Create a temp_goals_target table based on the goals-targets.csv

  Since I created mine from scratch and it was "relatively" small, I just used the import wizard
  on MySQL Workbench
*/




/*
  Create Goal Table
  This uses the temp table created from my custom CSV
*/

CREATE TABLE goal SELECT DISTINCT Goal FROM temp_goals_target

ALTER TABLE goal CHANGE Goal goal_name VARCHAR(255);


ALTER TABLE goal ADD goal_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST


/*
  Creates Targets Table
  This uses the temp table created from my custom CSV and the previously created goals table
*/

DROP TABLE IF EXISTS target;

CREATE TABLE IF NOT EXISTS target (   target_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,   target_name VARCHAR(255) NOT NULL UNIQUE,   goal_id INTEGER NULL,   PRIMARY KEY (target_id),   FOREIGN KEY (goal_id) REFERENCES goal(goal_id)     ON DELETE CASCADE ON UPDATE CASCADE );

INSERT IGNORE INTO target (
  target_name,
  goal_id
)
SELECT gt.Target, g.goal_id
  FROM temp_goals_target gt
       LEFT JOIN goal g
              ON TRIM(gt.Goal) = TRIM(g.goal_name)
WHERE TRIM(gt.Target) IS NOT NULL AND TRIM(gt.Target) != ''
ORDER BY gt.Target;




/* ############################*/
/* 
  Use the create_indicators_temp_table_from_csv.py 
  This creates the temp table that holds all the indicator values
*/
/* ############################*/

DELETE FROM temp_country_target_indicator
WHERE !Indicator_Value;


/*
  Create Indicator Value Type Table
  Uses the the temp_table from the python script and the previously created targets table
*/

DROP TABLE IF EXISTS indicator_value_type;

CREATE TABLE indicator_value_type SELECT DISTINCT Indicator FROM test.temp_country_target_indicator;

ALTER TABLE indicator_value_type CHANGE Indicator indicator_value_name VARCHAR(255);

ALTER TABLE indicator_value_type ADD indicator_value_type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST

/*
  Create Indicator Table 
  Uses previously created Target and Indicators Table Using the Relationship from the Goals-Targets CSV
*/
DROP TABLE IF EXISTS indicator;

CREATE TABLE IF NOT EXISTS indicator (   
	indicator_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,   
    target_id INT NOT NULL,   
    indicator_value_type_id INTEGER NOT NULL,   
    PRIMARY KEY (indicator_id),   
    FOREIGN KEY (target_id) REFERENCES target(target_id)
		  ON DELETE CASCADE ON UPDATE CASCADE,
	  FOREIGN KEY (indicator_value_type_id) REFERENCES indicator_value_type(indicator_value_type_id)
		  ON DELETE CASCADE ON UPDATE CASCADE);

INSERT IGNORE INTO indicator (
  target_id,
  indicator_value_type_id
)
SELECT t.target_id, ivt.indicator_value_type_id
  FROM temp_goals_target gt
    LEFT JOIN target t
        ON TRIM(gt.Target) = TRIM(t.target_name)
		LEFT JOIN indicator_value_type ivt
        ON TRIM(gt.Indicator) = TRIM(ivt.indicator_value_name)
WHERE TRIM(gt.Target) IS NOT NULL AND TRIM(gt.Target) != '' AND (gt.Indicator) IS NOT NULL AND TRIM(gt.Indicator) != ''
ORDER BY gt.Target;

/*
  Creates Final Country target Indicators Table

  This below code is so slow, it might not work
*/

DROP TABLE IF EXISTS country_target_indicator;

CREATE TABLE IF NOT EXISTS country_target_indicator (   
	country_target_indicator_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,   
	country_area_id INT (255) NOT NULL,  
  indicator_id INTEGER NOT NULL,
  countrycode VARCHAR(255),
  seriescode VARCHAR(255),
  year YEAR(4),
  indicator_value DECIMAL (11,2),
  PRIMARY KEY (country_target_indicator_id),   
  FOREIGN KEY (country_area_id) REFERENCES country_area(country_area_id)     
    ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (indicator_id) REFERENCES indicator(indicator_id)     
		ON DELETE CASCADE ON UPDATE CASCADE );

INSERT IGNORE INTO country_target_indicator (
  country_area_id,
  indicator_id,
  countrycode,
  seriescode,
  year,
  indicator_value
)
SELECT c.country_area_id, i.indicator_id, cti.CountryCode, cti.SeriesCode, cti.year, cti.Indicator_Value
	FROM temp_country_target_indicator cti
	LEFT JOIN indicator i
		ON (indicator_id)
			LEFT JOIN indicator_value_type ivt
				ON TRIM(cti.Indicator_value) = TRIM(ivt.indicator_value_name)
	   LEFT JOIN country_area c
			  ON TRIM(cti.Country) = TRIM(c.country_area_name)
	WHERE TRIM(c.country_area_id) IS NOT NULL