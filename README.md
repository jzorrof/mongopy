# mongopy
## import data into collection
mongoimport --db test --collection restaurants --drop --file primer-dataset.json
To import data into a mongod instance running on a different host or port, specify the hostname or port by including the --host and the --port options
