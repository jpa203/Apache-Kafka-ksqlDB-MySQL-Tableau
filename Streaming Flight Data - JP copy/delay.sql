SET 'auto.offset.reset'='earliest'; -- consume from the beginning 

create stream delay_analysis as  -- create stream
select 
flight->icao as flight_icaco, -- selected nested json data
airline,
departure->airport as departure_airport, 
CAST((UNIX_TIMESTAMP(departure->actual) - UNIX_TIMESTAMP(departure->scheduled)) as int)/60000 as time_difference,
CASE -- calculate delay, on time and early departure 
    WHEN CAST((UNIX_TIMESTAMP(departure->actual) - UNIX_TIMESTAMP(departure->scheduled)) as int)/60000 > 0 THEN 'Delay'
    WHEN CAST((UNIX_TIMESTAMP(departure->actual) - UNIX_TIMESTAMP(departure->scheduled)) as int)/60000 < 0 THEN 'Early Departure'
    ELSE 'On Time'
    END AS dep_delay
FROM flight_data; -- from another stream


