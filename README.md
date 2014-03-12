## zgeist - link sharing platform

### Based On / Requirements

* python 2.7
* [webassets](http://webassets.readthedocs.org/en/latest/)
* sqlalchemy / alembic
* flask

### Installation / Development Environment

* (Fork/)Clone repository: `git clone https://github.com/geekosphere/zgeist.git`
* Install prerequisites:
     * python, pip/easy_install, postgresql
     * [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv),
     * [virtualenvwrapper](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenvwrapper) (`source /usr/bin/virtualenvwrapper.sh`, add to your `~/zshrc.local`),
     * [sass](http://sass-lang.com/) (`gem install sass`),
     * [bower](http://bower.io/) (`npm install bower`)
* Install bower packages: `bower install`
* `source /usr/bin/virtualenvwrapper.sh` 
* `mkvirtualenv zgeist`, later on you can switch to this env with: `workon zgeist`
* `pip install -r requirements.txt`
* Database setup:
    * `sudo su postgres`
    * `psql`
    * Execute: `CREATE ROLE myuser WITH LOGIN PASSWORD 'mypass';`
    * Execute: `CREATE DATABASE zgeist WITH OWNER myuser;`
    * Copy/Create a `conf/_local.yaml` configuration file with the database.uri variable replaced: `'postgres://myuser:mypass@localhost/zgeist'`
    * Init database scheme: `alembic upgrade head`
* Start app: `python wsgi.py`

### License

_zgeist_ is licensed under the [Affero General Public License](http://www.gnu.org/licenses/agpl-3.0.html), Version 3.

