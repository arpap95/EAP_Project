/*
Create a new DataBase :
1. DataBase : EAP_Project
2. Create a New Schema. Name : project
*/



create table project.customers
(
	customer_id serial primary key,
	first_name varchar(255) not null,
	last_name varchar(255) not null ,
	mobile_number varchar(10) not null,
	email varchar (255) not null
);
CREATE INDEX customers_email ON project.customers (email);



create table project.appointments
(
	appointment_id serial primary key,
	customer_id int,
	appointment_date Date,
	start_time varchar(5),
	end_time varchar(5)
);

CREATE INDEX appointments_appointment_date ON project.appointments (appointment_date);


   CREATE TABLE project.hours (
    id SERIAL PRIMARY KEY,
    hour_slot TIME NOT NULL UNIQUE
);


INSERT INTO project.hours (hour_slot)
SELECT CAST(g AS TIME)
FROM generate_series(
    TIMESTAMP '2024-01-01 00:00:00',
    TIMESTAMP '2024-01-01 23:00:00',
    INTERVAL '1 hour'
) AS g;
