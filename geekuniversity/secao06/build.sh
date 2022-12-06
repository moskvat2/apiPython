docker build -t apipython:v1 .
docker run -dit --name apipython --rm -p8000:8000 local/apipython:v1