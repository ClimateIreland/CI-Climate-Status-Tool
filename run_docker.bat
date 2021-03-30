

echo "killing old docker processes"
docker-compose rm -fs

echo "building docker containers"
docker-compose up --build -d

echo "Dash is running on http://0.0.0.0:8080/"