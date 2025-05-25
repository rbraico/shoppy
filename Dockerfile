FROM python:3.11-slim

# Imposta la directory di lavoro nel container
WORKDIR /shoppy

# Copia il contenuto del progetto
COPY . .

# Installa le dipendenze
RUN apt-get update && apt-get upgrade -y && \
    pip install --no-cache-dir -r requirements.txt

# Variabili d’ambiente
ENV DB_PATH=/config/stockhouse/stockhouse.db

# Espone la porta (diversa da StockHouse)
EXPOSE 9193

# Avvia con gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:9193", "wsgi:app"]
