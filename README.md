# python_last_dance
## Installation

To get started with the application you need to complete following steps:

- Install dependencies:

```shell
$ pip install -r requirements.txt
```

- Create `.env` file in root directory of the project and add there `SECRET_KEY` and `DB_URI` variables:

```
SECRET_KEY=your-secret-key
DB_URI=your-database-uri
```

- Create tables in your database:

```sql
CREATE TABLE NEWS(
	id VARCHAR PRIMARY KEY,
	url VARCHAR,
	heading VARCHAR,
	paragraph VARCHAR
)
```

- Run application:

```shell
$ python3 src/app.py
```

## Usage

In order to use the application, simply enter the name of the cryptocurrency in the text field and click on the search button.
