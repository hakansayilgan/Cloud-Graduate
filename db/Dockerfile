# Use a MongoDB base image
FROM mongo:latest

# Set environment variables
# ENV MONGO_INITDB_ROOT_USERNAME=admin
# ENV MONGO_INITDB_ROOT_PASSWORD=supersecretpassword

# Expose MongoDB port
EXPOSE 27017

# Start MongoDB service
CMD ["mongod"]


## db.names.insertOne({ "name": "Hakan" })
# docker build -t hakansayilgan313/mongodb:v1 . --platform=linux/amd64