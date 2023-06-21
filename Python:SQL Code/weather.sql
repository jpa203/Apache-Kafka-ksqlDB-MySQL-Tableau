 create stream timeseries_stream WITH (KAFKA_TOPIC='timeseries', KEY_FORMAT='JSON') 
 as select TIMESTAMPTOSTRING(rowtime, 'dd/MMM HH:mm:ss') as landtime, 
 flight->number, country_name, population from flight_data emit changes;
