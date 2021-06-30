Install instructions

```python
cd biostar-central
virtualenv biostar --python=python3
source ./biostar/bin/activate
pip install -r conf/requirements.txt
pip install -r conf/pip_requirements.txt
```

Make a new postgres database
```
sudo -u postgres createdb biodb
```

Make a new postgres user (give superuser permission)
```
sudo -u postgres createuser --interactive
```

python ./manage.py makemigrations
pip install psycopg2-binary
python ./manage.py migrate
python ./manage.py runserver