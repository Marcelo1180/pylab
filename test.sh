curl -XDELETE "http://localhost:9200/test"
curl -XPUT "http://localhost:9200/test" -d'
{
   "settings": {
      "analysis": {
         "analyzer": {
            "merged_hyphens": {
               "tokenizer": "whitespace",
               "filter": ["lowercase", "word_delim", "my_stemm"]
            },
            "x_fonetico": {
               "tokenizer": "keyword",
               "filter": ["lowercase", "word_delim", "my_stemm", "my_metaphone"]
            },
            "x_sinonimo" : {
               "tokenizer": "whitespace",
               "filter": ["lowercase", "my_synonym"]
            },
            "x_numero" : {
               "tokenizer": "keyword",
               "filter": ["lowercase"]
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
                  },
                  "numero": {
                     "type": "string",
                     "analyzer": "x_numero"
                  }
               }
            },
            "objeto_principal": {
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

# curl -XPUT "http://localhost:9200/test/test/1" -d'
# {
#     "nombre": "Restaurant Condorito",
#     "ciiu": "1020",
#     "objeto_principal": "servicio de restaurant y peluqueria",
#     "estado": "MA"
# }'
#
# curl -XPUT "http://localhost:9200/test/test/2" -d'
# {
#     "nombre": "Ferreteria Condorito",
#     "ciiu": "0090",
#     "objeto_principal": "ferreteria y consultoria en construccion",
#     "estado": "MA"
# }'
#
# curl -XPUT "http://localhost:9200/test/test/3" -d'
# {
#     "nombre": "Estética Condorito",
#     "ciiu": "0050",
#     "objeto_principal": "venta de productos higienicos y servicio de estetica y belleza",
#     "estado": "MA"
# }'


curl -XPUT "http://localhost:9200/test/test/1" -d'
{
    "nombre": "anti-emetic",
    "ciiu": "0124",
    "objeto_principal": "La tecnologia de antiemetic es una organizacion mundial sin fines de lucro",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/2" -d'
{
    "nombre": "antiemetic",
    "ciiu": "0124",
    "objeto_principal": "La tecnologia de antiemetic es la mas especializada en el mundo de reparacion de tecnologias",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/3" -d'
{
    "nombre": "anti emetic",
    "ciiu": "0124",
    "objeto_principal": "Reparacion de Televisores",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/4" -d'
{
    "nombre": "Tienda de Musicales Bonito",
    "ciiu": "1014",
    "objeto_principal": "Venta y reparacion de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/5" -d'
{
    "nombre": "Tienda de Musicales y bonitos",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/6" -d'
{
    "nombre": "Tienda musical el bonitos",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/7" -d'
{
    "nombre": "Almacen musicales saborosos y bonitos",
    "ciiu": "1013",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/8" -d'
{
    "nombre": "musicales y asociados \"bonito\"",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/9" -d'
{
    "nombre": "musicales y casita",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/10" -d'
{
    "nombre": "musicales y casa",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/11" -d'
{
    "nombre": "musicales y casas",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
}'

curl -XPUT "http://localhost:9200/test/test/12" -d'
{
    "nombre": "musicales y casitas",
    "ciiu": "1014",
    "objeto_principal": "Venta de instrumentos musicales y cosas de otros rubros",
    "estado": "MA"
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

curl -XPUT "http://localhost:9200/test/test/24" -d'
{
    "nombre": "barraca el ciego"
}'

curl -XPUT "http://localhost:9200/test/test/25" -d'
{
    "nombre": "universidad siglo veinte"
}'

curl -XPUT "http://localhost:9200/test/test/26" -d'
{
    "nombre": "universidad siglo xx"
}'

curl -XPUT "http://localhost:9200/test/test/27" -d'
{
    "nombre": "universidad siglo x"
}'
