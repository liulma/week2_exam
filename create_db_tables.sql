-- Create the database using another connection to my postgresql server
CREATE DATABASE assesment;

-- Connected with SQLTools to my new database and create table flights
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    flight_number varchar(10) NOT NULL,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    departure_airport varchar(100),
    destination_airport varchar(100)
);

-- Insert 3 rows of data to table flights
INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) VALUES 
('AA123', '2025-01-24 08:00:00', '2025-01-24 10:30:00', 'JFK International Airport', 'Los Angeles International Airport'),
('DL456', '2025-01-03 12:15:00', '2025-01-03 15:00:00', 'Atlanta Hartsfield-Jackson', 'Chicago OHare International Airport'),
('UA789', '2025-01-13 18:30:00', '2025-01-13 21:45:00', 'San Francisco International Airport', 'Miami International Airport');

-- Create table airline
CREATE TABLE airline (
    id SERIAL PRIMARY KEY,
    name varchar(100),
    flights_id int,
    CONSTRAINT fk_flights FOREIGN KEY(flights_id) REFERENCES flights(id)
);

-- Insert 6 rows matching each flight in a way that every flights table row now has an airline linked to it
INSERT INTO airline (name, flights_id) VALUES
('Finnair', 1),
('American Airline', 2),
('SAS', 3),
('Ryanair', 4),
('Lufthansa', 5),
('Norwegian', 6);