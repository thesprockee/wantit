# Wantit Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages wantit-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages wantit-env
cd wantit-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> wantit
```

### Install requirements ###
```bash
cd wantit
pip install -r requirements.txt
```

### Configure project ###
```bash
cp wantit/__local_settings.py wantit/local_settings.py
vi wantit/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
