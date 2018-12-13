
USE unsdg;

/*
  Create a temp_goals_target table based on the goals-targets.csv.  You will use this to build:
    goal
    target
    indicator
*/



/*
  Create Goal Table
*/

CREATE TABLE goal SELECT DISTINCT Goal FROM goals_targets

ALTER TABLE goal CHANGE Goal goal_name VARCHAR(255);


ALTER TABLE goal ADD goal_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST


/*
  Creates Targets Table
*/

DROP TABLE IF EXISTS target;

CREATE TABLE IF NOT EXISTS target (   target_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,   target_name VARCHAR(255) NOT NULL UNIQUE,   goal_id INTEGER NULL,   PRIMARY KEY (target_id),   FOREIGN KEY (goal_id) REFERENCES goal(goal_id)     ON DELETE CASCADE ON UPDATE CASCADE );

INSERT IGNORE INTO target (
  target_name,
  goal_id
)
SELECT gt.Target, g.goal_id
  FROM goals_targets gt
       LEFT JOIN goal g
              ON TRIM(gt.Goal) = TRIM(g.goal_name)
WHERE TRIM(gt.Target) IS NOT NULL AND TRIM(gt.Target) != ''
ORDER BY gt.Target;

/*
  Create Indicator Value Type Table
*/

DROP TABLE IF EXISTS indicator_value_type;

CREATE TABLE indicator_value_type SELECT DISTINCT Indicator FROM test.country_target_indicator;

ALTER TABLE indicator_value_type CHANGE Indicator indicator_value_name VARCHAR(255);

ALTER TABLE indicator_value_type ADD indicator_value_type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST

/*
  Create Indicator Table based on previously created Target and Indicators Table Using the Relationships
  Found in Goals-Targets CSV
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
  FROM goals_targets gt
       LEFT JOIN target t
              ON TRIM(gt.Target) = TRIM(t.target_name)
		LEFT JOIN indicator_value_type ivt
              ON TRIM(gt.Indicator) = TRIM(ivt.indicator_value_name)
WHERE TRIM(gt.Target) IS NOT NULL AND TRIM(gt.Target) != '' AND (gt.Indicator) IS NOT NULL AND TRIM(gt.Indicator) != ''
ORDER BY gt.Target;
