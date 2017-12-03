curl -XDELETE "http://localhost:9200/test"
curl -XPUT "http://localhost:9200/test" -d'
{
   "settings": {
      "analysis": {
         "analyzer": {
            "merged_hyphens": {
               "tokenizer": "whitespace",
               "filter": [ "lowercase", "word_delim", "my_stemm"]
            },
            "x_fonetico": {
               "tokenizer": "whitespace",
               "filter": [ "lowercase", "word_delim", "my_stemm", "my_metaphone"]
            },
            "x_sinonimo" : {
               "tokenizer": "whitespace",
               "filter": [ "lowercase", "my_synonym"]
            }
         },
         "filter": {
            "word_delim": {
               "type": "word_delimiter",
               "catenate_words": true,
               "generate_word_parts": false,
               "generate_number_parts": false
            },
            "my_stemm": {
               "type": "stemmer",
               "language": "light_spanish"
            },
            "my_metaphone": {
               "type": "phonetic",
               "encoder": "beidermorse",
               "languageset": ["spanish"]
            },
            "my_synonym" : {
               "type" : "synonym",
               "synonyms_path" : "/tmp/sinonimos.txt"
            }
         }
      }
   },
   "mappings": {
      "test": {
         "properties": {
            "nombre": {
               "type": "string",
               "fields": {
                  "merged": {
                     "type": "string",
                     "analyzer": "merged_hyphens"
                  },
                  "fonetico": {
                     "type": "string",
                     "analyzer": "x_fonetico"
                  },
                  "sinonimo": {
                     "type": "string",
                     "analyzer": "x_sinonimo"
                  }
               }
            }
         }
      }
   }
}'

curl -XPUT "http://localhost:9200/test/test/1" -d'
{
    "nombre": "anti-emetic"
}'

curl -XPUT "http://localhost:9200/test/test/2" -d'
{
    "nombre": "antiemetic"
}'

curl -XPUT "http://localhost:9200/test/test/3" -d'
{
    "nombre": "anti emetic"
}'

curl -XPUT "http://localhost:9200/test/test/4" -d'
{
    "nombre": "Tienda de Musicales Bonito"
}'

curl -XPUT "http://localhost:9200/test/test/5" -d'
{
    "nombre": "Tienda de Musicales y bonitos"
}'

curl -XPUT "http://localhost:9200/test/test/6" -d'
{
    "nombre": "Tienda musical el bonitos"
}'

curl -XPUT "http://localhost:9200/test/test/7" -d'
{
    "nombre": "Almacen musicales saborosos y bonitos"
}'

curl -XPUT "http://localhost:9200/test/test/8" -d'
{
    "nombre": "musicales y asociados \"bonito\""
}'

curl -XPUT "http://localhost:9200/test/test/9" -d'
{
    "nombre": "musicales y casita"
}'

curl -XPUT "http://localhost:9200/test/test/10" -d'
{
    "nombre": "musicales y casa"
}'

curl -XPUT "http://localhost:9200/test/test/11" -d'
{
    "nombre": "musicales y casas"
}'

curl -XPUT "http://localhost:9200/test/test/12" -d'
{
    "nombre": "musicales y casitas"
}'

curl -XPUT "http://localhost:9200/test/test/13" -d'
{
    "nombre": "olas del brazil"
}'

curl -XPUT "http://localhost:9200/test/test/14" -d'
{
    "nombre": "alas del brazil"
}'

curl -XPUT "http://localhost:9200/test/test/15" -d'
{
    "nombre": "tiahuanacu tour"
}'

curl -XPUT "http://localhost:9200/test/test/16" -d'
{
    "nombre": "tiwanacu tour"
}'

curl -XPUT "http://localhost:9200/test/test/17" -d'
{
    "nombre": "radio qoyasuyo marca"
}'

curl -XPUT "http://localhost:9200/test/test/18" -d'
{
    "nombre": "barraca 100 años"
}'

curl -XPUT "http://localhost:9200/test/test/19" -d'
{
    "nombre": "barraca cien años"
}'

curl -XPUT "http://localhost:9200/test/test/20" -d'
{
    "nombre": "barraca 200 años"
}'

curl -XPUT "http://localhost:9200/test/test/21" -d'
{
    "nombre": "barraca doscientos años"
}'

curl -XPUT "http://localhost:9200/test/test/22" -d'
{
    "nombre": "barraca doscientos alojamiento"
}'

curl -XPUT "http://localhost:9200/test/test/23" -d'
{
    "nombre": "universal afeminado"
}'
