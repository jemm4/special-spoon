# special-spoon

## Running it + Installs

- Install python: <https://www.python.org/downloads/>
- Create venv:

```bash
  python -m venv venv
```

- Activate venv:

```bash
source venv/Scripts/activate
```

- Install requirements:

```bash
pip install -r requirements.txt
```

- Install sqlite3: <https://www.sqlite.org/download.html>

- Create sqlite databse using create.sql schema:

```bash
sqlite3 sql/db.db < sql/create.sql
```

- Create .env for environment variables then add the following:

```text
DATABASE_PATH = path/to/db
DISCORD_TOKEN = TokenFromDiscord
```

- Run bot:

```bash
python bot.py
```
