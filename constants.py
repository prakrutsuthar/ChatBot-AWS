# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWVTVTUK7L"
aws_secret_access_key="E5UIAK8hjsF+u3+fcYCAeg6EyWDVBflxRMkJg6H+"
aws_session_token="FwoGZXIvYXdzEMn//////////wEaDNdezVywlUpQ1dRCjSLAAbvEdoBxq8ScoQ7pgO5EzoeXqtz7v8W7ThAegvQDpu6J99iGC/lGcaTSNK+v1x/sqzYsyBL8p+k8Cb9eIb16kO5zxk+WtHWk3VXg2c5BhDeteCA7SVPGpjtFoN7lf1iUk6SJpeqM58WbV5YHVgSUasMVc54XyE9Y8LbOAI71M1SZwLX3vgqbWO+VwqtqNjxfp8XZeDlilkohWBS/C3ZLwItWgMZQJs+bpoBAakqgTOAyJ8MuVFUgUg3duVo5kmsTnyi8+tWWBjItSSSpWHZmnzzHDEhy0Z7/G6MGH9qhVO7IGqTnGH2AfqU9Oa6y9W0NNI6RuVPl"
aws_userId="user2027430"

# Redis
redis_ttl = 20*60  #20 minutes

# For Crawlers
bucket_name = "crawled-unprocessed-data"

# For Model Creation and Deployment
model_output_folder = "./model/"
model_file_name = "rss_model.pkl"
corpus_file_name = "corpus.pkl"
metadata_file_name = "metadata.pkl"
top_document_count = 5

# Dynamo-DB Detailsce
table_name = "news_data"

# APIs
get_doc = "http://3.237.13.47/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"