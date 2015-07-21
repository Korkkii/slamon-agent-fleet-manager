SLAMon Agent Fleet Manager (AFM)
================================

[![License][license]](http://www.apache.org/licenses/LICENSE-2.0)

[![Latest PyPI Version](https://badge.fury.io/py/slamon-afm.svg)](http://badge.fury.io/py/slamon-afm)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/slamon-afm.svg)](pypi)
[![Requirements Status][requirements_img]](requirements)

[![Build Status][ci_status]](https://travis-ci.org/Korkkii/slamon-agent-fleet-manager.svg?branch=separation)
[![Coverage Status][coveralls]](https://coveralls.io/github/Korkkii/slamon-agent-fleet-manager?branch=separation)
[![Code Health][codehealth]](https://landscape.io/github/Korkkii/slamon-agent-fleet-manager/separation)

$SLAMON_ROOT refers to the directory where the root of this repository lies

# Requirements
* python 3.4
* virtualenv

# Setting up
File slamon_afm/settings.py contains AFM settings in following format:
```
class Settings:
    port = 8080  # Port for the server

    database_name = 'slamon'  # Name of the psql database
    database_user = 'afm'  # Username to use for psql connection
    database_password = 'changeme'  # Password to use for psql connection
```

## Creating postgresql database
```
psql
postgres=# CREATE DATABASE slamon;
postgres=# CREATE DATABASE slamon_tests;
postgres=# CREATE USER afm WITH PASSWORD 'changeme';
postgres=# GRANT ALL PRIVILEGES ON DATABASE slamon TO afm;
postgres=# GRANT ALL PRIVILEGES ON DATABASE slamon_tests TO afm;
\q
```

To create needed tables:
```
cd $SLAMON_ROOT
python ./slamon_afm/admin.py --create-tables
```

To delete tables:
```
cd $SLAMON_ROOT
python ./slamon_afm/admin.py --drop-tables
```

## Creating python virtualenv and installing needed packages
```
cd $SLAMON_ROOT
virtualenv env
. env/bin/active
pip install -r requirements_afm.txt
```

# Running
## Running afm
After entering the virtual environment type in a terminal following:
```
cd $SLAMON_ROOT
export PYTHONPATH=`pwd`
python ./slamon_afm/afm.py
```
### Running tests
In virtual environment:
```
cd $SLAMON_ROOT
nosetests
```
or (if coverage report is also wanted)
```
cd $SLAMON_ROOT
nosetests --with-coverage --cover-package=slamon
```

[license]: https://img.shields.io/:license-Apache%20License%20v2.0-blue.svg
[ci_status]: https://travis-ci.org/Korkkii/slamon-agent-fleet-manager.svg?branch=separation
[coveralls]: https://coveralls.io/repos/Korkkii/slamon-agent-fleet-manager/badge.svg?branch=separation&service=github
[codehealth]: https://landscape.io/github/Korkkii/slamon-agent-fleet-manager/separation/landscape.svg?style=flat
[latest_version]: https://badge.fury.io/py/slamon-afm.svg
[pypi]: https://pypi.python.org/pypi/slamon-afm/
[requirements_img]: https://requires.io/github/Korkkii/slamon-agent-fleet-manager/requirements.svg?branch=separation
[requirements]: https://requires.io/github/Korkkii/slamon-agent-fleet-manager/requirements/?branch=separation
