CREATE TABLE airlines WITH (KAFKA_TOPIC = 'airlines_aggregate', KEY = 'AIRLINE', KEY_FORMAT = 'AVRO')
AS
  SELECT airline, country_name, fleet_average_age, date_founded, 
  count(*) as count
  FROM flight_data
  GROUP BY airline, country_name, fleet_average_age, date_founded;