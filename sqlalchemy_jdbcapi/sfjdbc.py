from __future__ import absolute_import
from __future__ import unicode_literals

import os
import re

from urllib.parse import unquote

from sqlalchemy.sql import sqltypes
from sqlalchemy import util, exc
from sqlalchemy_jdbcapi.base import MixedBinary, BaseDialect

from sqlalchemy.engine.default import DefaultDialect

class SalesforceJDBCDialect(BaseDialect, DefaultDialect):
    jdbc_db_name = "salesforce"

    # this is the classname for open-source jdbc driver from dbschema:
    # https://github.com/wise-coders/salesforce-jdbc-driver/
    #
    jdbc_driver_name = "com.dbschema.salesforce.SalesforceJdbcDriver"

    # Uncomment this line and comment the line above if you are using
    # the jdbc driver from CData. URL that you use with SQLAlchemy
    # remains the same for both the drivers.
    #jdbc_driver_name = "cdata.jdbc.salesforce.SalesforceDriver"

    def initialize(self, connection):
        super(SalesforceJDBCDialect, self).initialize(connection)

    def _driver_kwargs(self):
        return {}

    def create_connect_args(self, url):
        if url is None:
            return
        # dialects expect jdbc url e.g.
        # "jdbc:salesforce:User=<username>;Password=<password>;Security Token=<token>"
        # restore original url
        s: str = str(url)
        # get jdbc url
        jdbc_url: str = unquote(s.split("//", 1)[-1])

        # add driver information
        kwargs = {
            "jclassname": self.jdbc_driver_name,
            "url": jdbc_url,
            # pass driver args via JVM System settings
            "driver_args": []
        }
        return ((), kwargs)

dialect = SalesforceJDBCDialect
