FROM python:3.10-slim

# Setup working directory di dalam container
WORKDIR /opt/dagster/app

# Copy requirements & Install (biar cache-nya jalan)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Setup Environment Variables
ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV PYTHONPATH=/opt/dagster/app

# Bikin folder home & app
RUN mkdir -p $DAGSTER_HOME

# Copy file config dagster (Nanti kita bikin di langkah 5)
COPY dagster.yaml $DAGSTER_HOME/

# Copy seluruh kodingan kita ke dalam container
COPY . /opt/dagster/app

# Expose port UI Dagster
EXPOSE 3000

# Command default pas container nyala
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000", "-m", "dagster_project"]