curl -XDELETE "http://localhost:9200/fundempresa2"
curl -XPUT "http://localhost:9200/fundempresa2" -d'
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
               "filter": ["lowercase", "my_stemm", "my_synonym"]
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
