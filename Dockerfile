FROM python:3.11-slim-bookworm

# Imposta la directory di lavoro nel container
WORKDIR /shoppy

# Copia il contenuto del progetto
COPY . .

# Installa le dipendenze
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y gcc build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

# Variabili d’ambiente
ENV DB_PATH=/config/sqlite_db/stockhouse.db

# Espone la porta (diversa da StockHouse)
EXPOSE 9193

# Avvia con gunicorn
#CMD ["gunicorn", "-b", "0.0.0.0:9193", "wsgi:app"]

# Copia lo script e rendilo eseguibile.
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Comando di avvio
CMD [ "sh", "/run.sh" ]
