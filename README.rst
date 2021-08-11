JDBC Connection for SQLAlchemy.
===============================
.. image:: https://img.shields.io/pypi/dm/sqlalchemy-jdbcapi.svg
        :target: https://pypi.org/project/sqlalchemy-jdbcapi/

The primary purpose of this dialect is to provide JDBC connection using provided driver(JAR).

Installation
------------

Installing the dialect is straightforward::

     python3 -m pip install sqlalchemy-jdbcapi


Usage
-----
Set an environment variable  `export CLASSPATH=<path>/ojdbc8.jar:<path>/postgresql-42.2.9.jre7.jar`

PostgressSQL::

    from sqlalchemy import create_engine
    create_engine('jdbcapi+pgjdbc://{}:{}@{}/{}'.format(username, password, <ip:host>', <database name>))

Oracle::

    create_engine("jdbcapi+oraclejdbc://username:password@HOST:1521/Database")

Salesforce::

    First, download the salesforce driver from https://github.com/wise-coders/salesforce-jdbc-driver/ and unzip its contents into a folder.

    Set environment variable 'export CLASSPATH=<path>/antlr-runtime-3.5.2.jar:<path>/commons-beanutils-1.9.4.jar:<path>/commons-collections-3.2.2.jar:<path>/commons-collections4-4.4.jar:<path>/commons-logging-1.2.jar:<path>/dbschema-salesforce-jdbc1.2.jar:<path>/force-partner-api-52.2.0.jar:<path>/force-wsc-52.2.0.jar:<path>/h2-1.4.200.jar:<path>/jackson-annotations-2.12.3.jar:<path>/jackson-core-2.12.3.jar:<path>/jackson-databind-2.12.3.jar:<path>/ST4-4.3.jar'
    where <path> is where you unzipped the contents of the binary zip file downloaded.

    create_engine("jdbcapi+sfjdbc://jdbc:dbschema:saleforce://username=lulu@yahoo.com;password=somepasswordwithtoken")

GenericJDBCConnection::

        Set an environment variable `JDBC_DRIVER_PATH`

Supported databases
-------------------

In theory every database with a suitable JDBC driver should work.

* SQLite
* Hypersonic SQL (HSQLDB)
* IBM DB2
* IBM DB2 for mainframes
* Oracle
* Teradata DB
* Netezza
* Mimer DB
* Microsoft SQL Server
* MySQL
* PostgreSQL
* many more...

Contributing
------------

Please submit `bugs and patches
<https://github.com/daneshpatel/sqlalchemy-jdbcapi/issues>`_.
All contributors will be acknowledged. Thanks!

Changelog
------------
- 1.2.2 - 2020-10-16
  - SSL Support from URL.
  
- 1.2.1 - 2020-09-9
  - Minor fix.

- 1.2.0 - 2020-09-1
  - Issue: PGarray not iterable.

- 1.1.0 - 2020-08-4
  - Initial release.
