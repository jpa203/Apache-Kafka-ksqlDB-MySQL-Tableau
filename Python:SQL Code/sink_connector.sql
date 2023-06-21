CREATE SINK CONNECTOR SINK_ELASTIC_ORDERS_01 WITH (
  'connector.class'                     = 'io.confluent.connect.elasticsearch.ElasticsearchSinkConnector',
  'topics'                              = 'ORDERS_ENRICHED',
  'connection.url'                      = 'http://elasticsearch:9200',
  'type.name'                           = '_doc'
  );