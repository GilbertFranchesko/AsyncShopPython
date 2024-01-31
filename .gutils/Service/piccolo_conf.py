from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(config={
    "user": "postgres",
    "database": "postgres",
    "host": "db",
    "password": "qwerty_test",
    "port": 5432
})
