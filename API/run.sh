docker build -t bank_api:latest .
docker run -d --name bank_api -p 80:80 bank_api

curl -X 'POST'   'http://localhost/DevOps/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "message": "This is a test",
  "to": "Juan Perez",
  "from_": "Rita Asturia",
  "timeToLifeSec": 45
}'



docker login acrpichbank2.azurecr.io   ( acrpichbank2 /  dyi+y8lWx+4wTlfIjbptjPHMkScnZdNYQgIxlD8raD+ACRAqOfMk  )
docker build -t acrpichbank2.azurecr.io/bank_api:0.0.2 .
docker push acrpichbank2.azurecr.io/bank_api:0.0.2
