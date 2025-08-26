# Employees backend application

Adatbázis elindítása:

- Podman esetén a `docker` helyett `podman` szót kell írni.

```shell
docker run -d -e POSTGRES_DB=employees -e POSTGRES_USER=employees -e POSTGRES_PASSWORD=employees -p 5432:5432 --name employees-postgres postgres
```

Virtuális környezet létrehozása:

```script
python -m venv venv
```

Ha nem aktivál automatikusan a VS Code, akkor

```script
venv\Scripts\activate
```

Függőségek feltelepítése:

```script
pip install -r requirements.txt
```

Backend futtatása:

```script
fastapi dev app/main.py
```
