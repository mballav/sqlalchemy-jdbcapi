from __future__ import absolute_import
from __future__ import unicode_literals

import os
import re

from sqlalchemy.sql import sqltypes
from sqlalchemy import util, exc
from sqlalchemy_jdbcapi.base import MixedBinary, BaseDialect

from sqlalchemy.engine.default import DefaultDialect

class SalesforceJDBCDialect(BaseDialect, DefaultDialect):
    jdbc_db_name = "salesforce"
    jdbc_driver_name = "com.dbschema.salesforce.SalesforceJdbcDriver"

    def initialize(self, connection):
        super(SalesforceJDBCDialect, self).initialize(connection)

    def _driver_kwargs(self):
        return {}

    def create_connect_args(self, url):
        if url is None:
            return
        # dialects expect jdbc url e.g.
        # "jdbc:oracle:thin@example.com:1521/db"
        # if sqlalchemy create_engine() url is passed e.g.
        # "oracle://scott:tiger@example.com/db"
        # it is parsed wrong
        # restore original url
        s: str = str(url)
        # get jdbc url
        jdbc_url: str = s.split("//", 1)[-1]

        # schema_url = 'jdbc:calcite:schemaFactory=com.jdreamer.driver.web.WebDataSchemaFactory;case_sensitive=false;schema.name=test;schema.url=http://{}/datalake/;schema.tenantId=1;schema.catalog=demo'.format(jdbc_url)

        print(jdbc_url)

        # add driver information
        kwargs = {
            "jclassname": self.jdbc_driver_name,
            "url": jdbc_url,
            # pass driver args via JVM System settings
            "driver_args": []
        }
        return ((), kwargs)

dialect = SalesforceJDBCDialect
