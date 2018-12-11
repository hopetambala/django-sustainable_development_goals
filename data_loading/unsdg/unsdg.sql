-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: unsdg
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `country_area`
--

DROP TABLE IF EXISTS `country_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `country_area` (
  `country_area_id` int(11) NOT NULL AUTO_INCREMENT,
  `country_area_name` varchar(100) NOT NULL,
  `m49_code` smallint(4) NOT NULL,
  `iso_alpha3_code` char(3) NOT NULL,
  `location_id` int(11) NOT NULL DEFAULT '1',
  `dev_status_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`country_area_id`),
  UNIQUE KEY `country_area_id` (`country_area_id`),
  UNIQUE KEY `country_area_name` (`country_area_name`),
  KEY `dev_status_id` (`dev_status_id`),
  KEY `country_area_fk_location_id` (`location_id`),
  CONSTRAINT `country_area_fk_location_id` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`) ON UPDATE CASCADE,
  CONSTRAINT `country_area_ibfk_4` FOREIGN KEY (`dev_status_id`) REFERENCES `dev_status` (`dev_status_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country_area`
--

LOCK TABLES `country_area` WRITE;
/*!40000 ALTER TABLE `country_area` DISABLE KEYS */;
INSERT INTO `country_area` VALUES (1,'Afghanistan',4,'AFG',14,1),(2,'Åland Islands',248,'ALA',17,2),(3,'Albania',8,'ALB',19,2),(4,'Algeria',12,'DZA',2,1),(5,'American Samoa',16,'ASM',24,1),(6,'Andorra',20,'AND',19,2),(7,'Angola',24,'AGO',4,1),(8,'Anguilla',660,'AIA',7,1),(9,'Antarctica',10,'ATA',1,NULL),(10,'Antigua and Barbuda',28,'ATG',7,1),(11,'Argentina',32,'ARG',9,1),(12,'Armenia',51,'ARM',15,1),(13,'Aruba',533,'ABW',7,1),(14,'Australia',36,'AUS',21,2),(15,'Austria',40,'AUT',20,2),(16,'Azerbaijan',31,'AZE',15,1),(17,'Bahamas',44,'BHS',7,1),(18,'Bahrain',48,'BHR',15,1),(19,'Bangladesh',50,'BGD',14,1),(20,'Barbados',52,'BRB',7,1),(21,'Belarus',112,'BLR',16,2),(22,'Belgium',56,'BEL',20,2),(23,'Belize',84,'BLZ',8,1),(24,'Benin',204,'BEN',6,1),(25,'Bermuda',60,'BMU',10,2),(26,'Bhutan',64,'BTN',14,1),(27,'Bolivia (Plurinational State of)',68,'BOL',9,1),(28,'Bonaire, Sint Eustatius and Saba',535,'BES',7,1),(29,'Bosnia and Herzegovina',70,'BIH',19,2),(30,'Botswana',72,'BWA',5,1),(31,'Bouvet Island',74,'BVT',9,1),(32,'Brazil',76,'BRA',9,1),(33,'British Indian Ocean Territory',86,'IOT',3,1),(34,'British Virgin Islands',92,'VGB',7,1),(35,'Brunei Darussalam',96,'BRN',13,1),(36,'Bulgaria',100,'BGR',16,2),(37,'Burkina Faso',854,'BFA',6,1),(38,'Burundi',108,'BDI',3,1),(39,'Cabo Verde',132,'CPV',6,1),(40,'Cambodia',116,'KHM',13,1),(41,'Cameroon',120,'CMR',4,1),(42,'Canada',124,'CAN',10,2),(43,'Cayman Islands',136,'CYM',7,1),(44,'Central African Republic',140,'CAF',4,1),(45,'Chad',148,'TCD',4,1),(46,'Chile',152,'CHL',9,1),(47,'China',156,'CHN',12,1),(48,'China, Hong Kong Special Administrative Region',344,'HKG',12,1),(49,'China, Macao Special Administrative Region',446,'MAC',12,1),(50,'Christmas Island',162,'CXR',21,2),(51,'Cocos (Keeling) Islands',166,'CCK',21,2),(52,'Colombia',170,'COL',9,1),(53,'Comoros',174,'COM',3,1),(54,'Congo',178,'COG',4,1),(55,'Cook Islands',184,'COK',24,1),(56,'Costa Rica',188,'CRI',8,1),(57,'Côte d\'Ivoire',384,'CIV',6,1),(58,'Croatia',191,'HRV',19,2),(59,'Cuba',192,'CUB',7,1),(60,'Curaçao',531,'CUW',7,1),(61,'Cyprus',196,'CYP',15,2),(62,'Czechia',203,'CZE',16,2),(63,'Democratic People\'s Republic of Korea',408,'PRK',12,1),(64,'Democratic Republic of the Congo',180,'COD',4,1),(65,'Denmark',208,'DNK',17,2),(66,'Djibouti',262,'DJI',3,1),(67,'Dominica',212,'DMA',7,1),(68,'Dominican Republic',214,'DOM',7,1),(69,'Ecuador',218,'ECU',9,1),(70,'Egypt',818,'EGY',2,1),(71,'El Salvador',222,'SLV',8,1),(72,'Equatorial Guinea',226,'GNQ',4,1),(73,'Eritrea',232,'ERI',3,1),(74,'Estonia',233,'EST',17,2),(75,'Eswatini',748,'SWZ',5,1),(76,'Ethiopia',231,'ETH',3,1),(77,'Falkland Islands (Malvinas)',238,'FLK',9,1),(78,'Faroe Islands',234,'FRO',17,2),(79,'Fiji',242,'FJI',22,1),(80,'Finland',246,'FIN',17,2),(81,'France',250,'FRA',20,2),(82,'French Guiana',254,'GUF',9,1),(83,'French Polynesia',258,'PYF',24,1),(84,'French Southern Territories',260,'ATF',3,1),(85,'Gabon',266,'GAB',4,1),(86,'Gambia',270,'GMB',6,1),(87,'Georgia',268,'GEO',15,1),(88,'Germany',276,'DEU',20,2),(89,'Ghana',288,'GHA',6,1),(90,'Gibraltar',292,'GIB',19,2),(91,'Greece',300,'GRC',19,2),(92,'Greenland',304,'GRL',10,2),(93,'Grenada',308,'GRD',7,1),(94,'Guadeloupe',312,'GLP',7,1),(95,'Guam',316,'GUM',23,1),(96,'Guatemala',320,'GTM',8,1),(97,'Guernsey',831,'GGY',18,2),(98,'Guinea',324,'GIN',6,1),(99,'Guinea-Bissau',624,'GNB',6,1),(100,'Guyana',328,'GUY',9,1),(101,'Haiti',332,'HTI',7,1),(102,'Heard Island and McDonald Islands',334,'HMD',21,2),(103,'Holy See',336,'VAT',19,2),(104,'Honduras',340,'HND',8,1),(105,'Hungary',348,'HUN',16,2),(106,'Iceland',352,'ISL',17,2),(107,'India',356,'IND',14,1),(108,'Indonesia',360,'IDN',13,1),(109,'Iran (Islamic Republic of)',364,'IRN',14,1),(110,'Iraq',368,'IRQ',15,1),(111,'Ireland',372,'IRL',17,2),(112,'Isle of Man',833,'IMN',17,2),(113,'Israel',376,'ISR',15,2),(114,'Italy',380,'ITA',19,2),(115,'Jamaica',388,'JAM',7,1),(116,'Japan',392,'JPN',12,2),(117,'Jersey',832,'JEY',18,2),(118,'Jordan',400,'JOR',15,1),(119,'Kazakhstan',398,'KAZ',11,1),(120,'Kenya',404,'KEN',3,1),(121,'Kiribati',296,'KIR',23,1),(122,'Kuwait',414,'KWT',15,1),(123,'Kyrgyzstan',417,'KGZ',11,1),(124,'Lao People\'s Democratic Republic',418,'LAO',13,1),(125,'Latvia',428,'LVA',17,2),(126,'Lebanon',422,'LBN',15,1),(127,'Lesotho',426,'LSO',5,1),(128,'Liberia',430,'LBR',6,1),(129,'Libya',434,'LBY',2,1),(130,'Liechtenstein',438,'LIE',20,2),(131,'Lithuania',440,'LTU',17,2),(132,'Luxembourg',442,'LUX',20,2),(133,'Madagascar',450,'MDG',3,1),(134,'Malawi',454,'MWI',3,1),(135,'Malaysia',458,'MYS',13,1),(136,'Maldives',462,'MDV',14,1),(137,'Mali',466,'MLI',6,1),(138,'Malta',470,'MLT',19,2),(139,'Marshall Islands',584,'MHL',23,1),(140,'Martinique',474,'MTQ',7,1),(141,'Mauritania',478,'MRT',6,1),(142,'Mauritius',480,'MUS',3,1),(143,'Mayotte',175,'MYT',3,1),(144,'Mexico',484,'MEX',8,1),(145,'Micronesia (Federated States of)',583,'FSM',23,1),(146,'Monaco',492,'MCO',20,2),(147,'Mongolia',496,'MNG',12,1),(148,'Montenegro',499,'MNE',19,2),(149,'Montserrat',500,'MSR',7,1),(150,'Morocco',504,'MAR',2,1),(151,'Mozambique',508,'MOZ',3,1),(152,'Myanmar',104,'MMR',13,1),(153,'Namibia',516,'NAM',5,1),(154,'Nauru',520,'NRU',23,1),(155,'Nepal',524,'NPL',14,1),(156,'Netherlands',528,'NLD',20,2),(157,'New Caledonia',540,'NCL',22,1),(158,'New Zealand',554,'NZL',21,2),(159,'Nicaragua',558,'NIC',8,1),(160,'Niger',562,'NER',6,1),(161,'Nigeria',566,'NGA',6,1),(162,'Niue',570,'NIU',24,1),(163,'Norfolk Island',574,'NFK',21,2),(164,'Northern Mariana Islands',580,'MNP',23,1),(165,'Norway',578,'NOR',17,2),(166,'Oman',512,'OMN',15,1),(167,'Pakistan',586,'PAK',14,1),(168,'Palau',585,'PLW',23,1),(169,'Panama',591,'PAN',8,1),(170,'Papua New Guinea',598,'PNG',22,1),(171,'Paraguay',600,'PRY',9,1),(172,'Peru',604,'PER',9,1),(173,'Philippines',608,'PHL',13,1),(174,'Pitcairn',612,'PCN',24,1),(175,'Poland',616,'POL',16,2),(176,'Portugal',620,'PRT',19,2),(177,'Puerto Rico',630,'PRI',7,1),(178,'Qatar',634,'QAT',15,1),(179,'Republic of Korea',410,'KOR',12,1),(180,'Republic of Moldova',498,'MDA',16,2),(181,'Réunion',638,'REU',3,1),(182,'Romania',642,'ROU',16,2),(183,'Russian Federation',643,'RUS',16,2),(184,'Rwanda',646,'RWA',3,1),(185,'Saint Barthélemy',652,'BLM',7,1),(186,'Saint Helena',654,'SHN',6,1),(187,'Saint Kitts and Nevis',659,'KNA',7,1),(188,'Saint Lucia',662,'LCA',7,1),(189,'Saint Martin (French Part)',663,'MAF',7,1),(190,'Saint Pierre and Miquelon',666,'SPM',10,2),(191,'Saint Vincent and the Grenadines',670,'VCT',7,1),(192,'Samoa',882,'WSM',24,1),(193,'San Marino',674,'SMR',19,2),(194,'Sao Tome and Principe',678,'STP',4,1),(195,'Sark',680,'',18,2),(196,'Saudi Arabia',682,'SAU',15,1),(197,'Senegal',686,'SEN',6,1),(198,'Serbia',688,'SRB',19,2),(199,'Seychelles',690,'SYC',3,1),(200,'Sierra Leone',694,'SLE',6,1),(201,'Singapore',702,'SGP',13,1),(202,'Sint Maarten (Dutch part)',534,'SXM',7,1),(203,'Slovakia',703,'SVK',16,2),(204,'Slovenia',705,'SVN',19,2),(205,'Solomon Islands',90,'SLB',22,1),(206,'Somalia',706,'SOM',3,1),(207,'South Africa',710,'ZAF',5,1),(208,'South Georgia and the South Sandwich Islands',239,'SGS',9,1),(209,'South Sudan',728,'SSD',3,1),(210,'Spain',724,'ESP',19,2),(211,'Sri Lanka',144,'LKA',14,1),(212,'State of Palestine',275,'PSE',15,1),(213,'Sudan',729,'SDN',2,1),(214,'Suriname',740,'SUR',9,1),(215,'Svalbard and Jan Mayen Islands',744,'SJM',17,2),(216,'Sweden',752,'SWE',17,2),(217,'Switzerland',756,'CHE',20,2),(218,'Syrian Arab Republic',760,'SYR',15,1),(219,'Tajikistan',762,'TJK',11,1),(220,'Thailand',764,'THA',13,1),(221,'The former Yugoslav Republic of Macedonia',807,'MKD',19,2),(222,'Timor-Leste',626,'TLS',13,1),(223,'Togo',768,'TGO',6,1),(224,'Tokelau',772,'TKL',24,1),(225,'Tonga',776,'TON',24,1),(226,'Trinidad and Tobago',780,'TTO',7,1),(227,'Tunisia',788,'TUN',2,1),(228,'Turkey',792,'TUR',15,1),(229,'Turkmenistan',795,'TKM',11,1),(230,'Turks and Caicos Islands',796,'TCA',7,1),(231,'Tuvalu',798,'TUV',24,1),(232,'Uganda',800,'UGA',3,1),(233,'Ukraine',804,'UKR',16,2),(234,'United Arab Emirates',784,'ARE',15,1),(235,'United Kingdom of Great Britain and Northern Ireland',826,'GBR',17,2),(236,'United Republic of Tanzania',834,'TZA',3,1),(237,'United States Minor Outlying Islands',581,'UMI',23,1),(238,'United States of America',840,'USA',10,2),(239,'United States Virgin Islands',850,'VIR',7,1),(240,'Uruguay',858,'URY',9,1),(241,'Uzbekistan',860,'UZB',11,1),(242,'Vanuatu',548,'VUT',22,1),(243,'Venezuela (Bolivarian Republic of)',862,'VEN',9,1),(244,'Viet Nam',704,'VNM',13,1),(245,'Wallis and Futuna Islands',876,'WLF',24,1),(246,'Western Sahara',732,'ESH',2,1),(247,'Yemen',887,'YEM',15,1),(248,'Zambia',894,'ZMB',3,1),(249,'Zimbabwe',716,'ZWE',3,1);
/*!40000 ALTER TABLE `country_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dev_status`
--

DROP TABLE IF EXISTS `dev_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dev_status` (
  `dev_status_id` int(11) NOT NULL AUTO_INCREMENT,
  `dev_status_name` varchar(25) NOT NULL,
  PRIMARY KEY (`dev_status_id`),
  UNIQUE KEY `dev_status_id` (`dev_status_id`),
  UNIQUE KEY `dev_status_name` (`dev_status_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dev_status`
--

LOCK TABLES `dev_status` WRITE;
/*!40000 ALTER TABLE `dev_status` DISABLE KEYS */;
INSERT INTO `dev_status` VALUES (2,'Developed'),(1,'Developing');
/*!40000 ALTER TABLE `dev_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intermediate_region`
--

DROP TABLE IF EXISTS `intermediate_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `intermediate_region` (
  `intermediate_region_id` int(11) NOT NULL AUTO_INCREMENT,
  `intermediate_region_name` varchar(100) NOT NULL,
  `sub_region_id` int(11) NOT NULL,
  PRIMARY KEY (`intermediate_region_id`),
  UNIQUE KEY `intermediate_region_id` (`intermediate_region_id`),
  UNIQUE KEY `intermediate_region_name` (`intermediate_region_name`),
  KEY `sub_region_id` (`sub_region_id`),
  CONSTRAINT `intermediate_region_ibfk_1` FOREIGN KEY (`sub_region_id`) REFERENCES `sub_region` (`sub_region_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intermediate_region`
--

LOCK TABLES `intermediate_region` WRITE;
/*!40000 ALTER TABLE `intermediate_region` DISABLE KEYS */;
INSERT INTO `intermediate_region` VALUES (1,'Caribbean',5),(2,'Central America',5),(3,'Channel Islands',10),(4,'Eastern Africa',15),(5,'Middle Africa',15),(6,'South America',5),(7,'Southern Africa',15),(8,'Western Africa',15);
/*!40000 ALTER TABLE `intermediate_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `planet_id` int(11) NOT NULL,
  `region_id` int(11) DEFAULT NULL,
  `sub_region_id` int(11) DEFAULT NULL,
  `intermediate_region_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `location_id` (`location_id`),
  KEY `planet_id` (`planet_id`),
  KEY `region_id` (`region_id`),
  KEY `sub_region_id` (`sub_region_id`),
  KEY `intermediate_region_id` (`intermediate_region_id`),
  CONSTRAINT `location_ibfk_1` FOREIGN KEY (`planet_id`) REFERENCES `planet` (`planet_id`) ON UPDATE CASCADE,
  CONSTRAINT `location_ibfk_2` FOREIGN KEY (`region_id`) REFERENCES `region` (`region_id`) ON UPDATE CASCADE,
  CONSTRAINT `location_ibfk_3` FOREIGN KEY (`sub_region_id`) REFERENCES `sub_region` (`sub_region_id`) ON UPDATE CASCADE,
  CONSTRAINT `location_ibfk_4` FOREIGN KEY (`intermediate_region_id`) REFERENCES `intermediate_region` (`intermediate_region_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,1,NULL,NULL,NULL),(2,1,1,8,NULL),(3,1,1,15,4),(4,1,1,15,5),(5,1,1,15,7),(6,1,1,15,8),(7,1,2,5,1),(8,1,2,5,2),(9,1,2,5,6),(10,1,2,9,NULL),(11,1,3,2,NULL),(12,1,3,3,NULL),(13,1,3,12,NULL),(14,1,3,13,NULL),(15,1,3,16,NULL),(16,1,4,4,NULL),(17,1,4,10,NULL),(18,1,4,10,3),(19,1,4,14,NULL),(20,1,4,17,NULL),(21,1,5,1,NULL),(22,1,5,6,NULL),(23,1,5,7,NULL),(24,1,5,11,NULL);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planet`
--

DROP TABLE IF EXISTS `planet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `planet` (
  `planet_id` int(11) NOT NULL AUTO_INCREMENT,
  `planet_name` varchar(50) NOT NULL,
  `unsd_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`planet_id`),
  UNIQUE KEY `planet_id` (`planet_id`),
  UNIQUE KEY `planet_name` (`planet_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planet`
--

LOCK TABLES `planet` WRITE;
/*!40000 ALTER TABLE `planet` DISABLE KEYS */;
INSERT INTO `planet` VALUES (1,'Earth','World');
/*!40000 ALTER TABLE `planet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `region` (
  `region_id` int(11) NOT NULL AUTO_INCREMENT,
  `region_name` varchar(100) NOT NULL,
  `planet_id` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`region_id`),
  UNIQUE KEY `region_id` (`region_id`),
  UNIQUE KEY `region_name` (`region_name`),
  KEY `region_fk_planet_id` (`planet_id`),
  CONSTRAINT `region_fk_planet_id` FOREIGN KEY (`planet_id`) REFERENCES `planet` (`planet_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES (1,'Africa',1),(2,'Americas',1),(3,'Asia',1),(4,'Europe',1),(5,'Oceania',1);
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_region`
--

DROP TABLE IF EXISTS `sub_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sub_region` (
  `sub_region_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_region_name` varchar(100) NOT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`sub_region_id`),
  UNIQUE KEY `sub_region_id` (`sub_region_id`),
  UNIQUE KEY `sub_region_name` (`sub_region_name`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `sub_region_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `region` (`region_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_region`
--

LOCK TABLES `sub_region` WRITE;
/*!40000 ALTER TABLE `sub_region` DISABLE KEYS */;
INSERT INTO `sub_region` VALUES (1,'Australia and New Zealand',5),(2,'Central Asia',3),(3,'Eastern Asia',3),(4,'Eastern Europe',4),(5,'Latin America and the Caribbean',2),(6,'Melanesia',5),(7,'Micronesia',5),(8,'Northern Africa',1),(9,'Northern America',2),(10,'Northern Europe',4),(11,'Polynesia',5),(12,'South-eastern Asia',3),(13,'Southern Asia',3),(14,'Southern Europe',4),(15,'Sub-Saharan Africa',1),(16,'Western Asia',3),(17,'Western Europe',4);
/*!40000 ALTER TABLE `sub_region` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-11 17:03:04
