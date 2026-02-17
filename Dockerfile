FROM python:3.10-slim

# Set the working directory within the container
WORKDIR /opt/dagster/app

# Copy dependency list and install to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Configure Environment Variables for Dagster orchestration
ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV PYTHONPATH=/opt/dagster/app

# Ensure required directories exist for Dagster metadata and application
RUN mkdir -p $DAGSTER_HOME

# Copy the Dagster configuration file to the defined home directory
COPY dagster.yaml $DAGSTER_HOME/

# Copy the entire project source code into the container
COPY . /opt/dagster/app

# Expose the Dagster UI default port
EXPOSE 3000

# Default command to launch the Dagster development server
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000", "-m", "dagster_project"]