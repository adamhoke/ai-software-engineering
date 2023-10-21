# Create database
CREATE DATABASE tododb;

# Create user with password
CREATE USER todouser WITH PASSWORD 'todopassword';

# Set default encoding, tsearch2 (for full-text search) and timezone
ALTER ROLE todouser SET client_encoding TO 'utf8';
ALTER ROLE todouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE todouser SET timezone TO 'UTC';

# Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE tododb TO todouser;

# Exit PostgreSQL command line
\q
