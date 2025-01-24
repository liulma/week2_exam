import psycopg2
from config import config

# Insert a row of data into the flights table
def db_create_flight(flight_number: str, departure_time: str, arrival_time: str, departure_airport: str, destination_airport: str):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (flight_number, departure_time, arrival_time, departure_airport, destination_airport)) # Pass argument to executor
        con.commit() # Save the changes to database
        cursor.close()

        print("Succesfully created new flight: %s\n" % flight_number)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# Print out the flights table ordered by departure_time
def order_by_deptime():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = '''
        SELECT * FROM flights
        ORDER BY departure_time;
        '''
        cursor.execute(SQL)
        row = cursor.fetchall()
        cursor.close()

        print("Flights table ordered by departure_time:")
        for item in row:
            print(f"id: {item[0]}, flight number: {item[1]}, departure time: {item[2]}, arrival time: {item[3]}, departure airport: {item[4]}, destination airport: {item[5]}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# Print out the flights table ordered by airline in alphabetical order
def flights_by_airline():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = '''
        SELECT f.*
        FROM flights f
        JOIN airline a ON f.id = a.flights_id
        ORDER BY a.name;
        '''
        cursor.execute(SQL)
        row = cursor.fetchall()
        cursor.close()

        print("\nFlights table ordered by airline in alphabetical order:")
        for item in row:
            print(f"id: {item[0]}, flight number: {item[1]}, departure time: {item[2]}, arrival time: {item[3]}, departure airport: {item[4]}, destination airport: {item[5]}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# Remove a flight and the respective airline rows from both tables
def rmv_flight_airline(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = '''
        DELETE FROM airline WHERE flights_id = %s;
        DELETE FROM flights WHERE id = %s;
        ''' # If I would've been smart, I would've used ON DELETE CASCADE when creating the table.. :)
        cursor.execute(SQL, (id,id))

        if cursor.rowcount == 0:
            print(f"\nCouldn't delete, no flight or airline found with id {id}.")
        else:
            con.commit()
            print(f"\nFlight with id {id} and airline with flights_id {id} successfully deleted from table")

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
    db_create_flight('SW101', '2025-01-25 07:30:00', '2025-01-25 09:45:00', 'Dallas/Fort Worth International Airport', 'Denver International Airport')
    db_create_flight('BA202', '2025-01-15 11:00:00', '2025-01-15 14:15:00', 'London Heathrow Airport', 'New York JFK International Airport')
    db_create_flight('AF303', '2025-01-18 16:20:00', '2025-01-18 19:45:00', 'Charles de Gaulle Airport', 'Los Angeles International Airport')
    order_by_deptime()
    flights_by_airline()
    rmv_flight_airline(6)