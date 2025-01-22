docker build -t my-ngix .
docker run -p 8081:80 my-ngix

for un priv 
docker run -p 8081:8080 my-ngix