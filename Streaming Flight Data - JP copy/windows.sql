CREATE TABLE hourly_data AS SELECT airline, count(*), COLLECT_LIST (flight->number) FROM flight_data
  WINDOW TUMBLING (SIZE 1 HOUR)
  GROUP BY airline HAVING COUNT(*) > 1; -- fixed-duration windown with no overlaps