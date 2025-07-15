FROM bitnami/spark:3.1.1

# Copy your custom jar into the Spark jars directory
COPY ./jars/postgresql-42.7.7.jar /opt/bitnami/spark/jars/
