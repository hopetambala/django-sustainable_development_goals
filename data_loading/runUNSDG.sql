
USE unsdg;




CREATE TABLE goal SELECT DISTINCT Goal FROM goals_targets


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
              ON TRIM(gt.Goal) = TRIM(g.Goal)
WHERE TRIM(gt.Target) IS NOT NULL AND TRIM(gt.Target) != ''
ORDER BY gt.Target;

SELECT * from target