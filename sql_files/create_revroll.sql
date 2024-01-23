DROP TABLE IF EXISTS customers;
CREATE TABLE customers (customer_id integer, preferred_name varchar(50), PRIMARY KEY (customer_id));
\copy customers FROM '../synthetic_datasets/revroll/customers.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS installers;
CREATE TABLE installers (installer_id integer, name varchar(50), PRIMARY KEY (installer_id));
\copy installers FROM '../synthetic_datasets/revroll/installers.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS installs;
CREATE TABLE installs (install_id integer, order_id integer, installer_id integer, install_date date, PRIMARY KEY (install_id));
\copy installs FROM '../synthetic_datasets/revroll/installs.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (order_id integer, customer_id integer, part_id integer, quantity integer, PRIMARY KEY (order_id));
\copy orders FROM '../synthetic_datasets/revroll/orders.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS parts;
CREATE TABLE parts (part_id integer, name varchar(50), price numeric, PRIMARY KEY (part_id));
\copy parts FROM '../synthetic_datasets/revroll/parts.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS install_derby;
CREATE TABLE install_derby (derby_id integer, installer_one_id integer, installer_two_id integer, installer_one_time integer, installer_two_time integer, PRIMARY KEY (derby_id));
\copy install_derby FROM '../synthetic_datasets/revroll/install_derby.csv' DELIMITER ',' CSV HEADER NULL AS ''
