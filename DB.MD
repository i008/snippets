```sql

-- LIST DATABASES

SELECT datname FROM pg_database
WHERE datistemplate = false;


-- LIST TABLES IN CURRENT CONNECTION

SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;


-- DROP TABLES ONLY 

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


-- GET CURRENT RUNNING QUERIES

select * from pg_stat_activity where state = 'active';


-- TERMINATE ALL QUERIES 

SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'fortests'
  AND pid <> pg_backend_pid();
  
```
