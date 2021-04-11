# python3-read-file
**Description**

This is a simple application to read data from a text file then save them into a mysql table

**Requirement**

1) Python 3
2) sudo apt-get install python3-mysql.connector


**MySql Table**

`CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `address_line_1` varchar(99) NOT NULL,
  `address_line_2` varchar(99) DEFAULT NULL,
  `postcode` varchar(9) NOT NULL,
  `when_created` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1`

This is test
