#!/bin/bash
# 1. Limpiamos el entorno temporal
rm -rf tempdir
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# 2. Creamos el Dockerfile con la sintaxis estricta
echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install --progress-bar off flask" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo 'CMD ["python3", "/home/myapp/sample_app.py"]' >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp .

# 3. Limpiamos contenedores anteriores para que Jenkins no falle por conflictos
docker stop samplerunning || true
docker rm samplerunning || true

# 4. Ejecutamos forzando explícitamente el comando de arranque
docker run -t -d -p 9999:8080 --name samplerunning sampleapp python3 /home/myapp/sample_app.py
