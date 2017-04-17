import logging as log
import MySQLdb.cursors
from scrapy.utils.project import get_project_settings
from twisted.enterprise import adbapi

SETTINGS = get_project_settings()

# Each matching item will go through this pipeline for further processing
class DBPipeline(object):
    def __init__(self):
        # DB connection
        self.dbpool = adbapi.ConnectionPool \
            ('MySQLdb',
             host=SETTINGS['DB_HOST'],
             user=SETTINGS['DB_USER'],
             passwd=SETTINGS['DB_PASSWD'],
             port=SETTINGS['DB_PORT'],
             db=SETTINGS['DB_DB'],
             charset='utf8',
             use_unicode=True,
             cursorclass=MySQLdb.cursors.DictCursor
             )

    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create record if doesn't exist.
        # all this block run on it's own thread
        # tx.execute("select * from sites where url = %s", (item['url']))
        # result = tx.fetchone()
        # if result:
        #     log.warn("Skipping %s, already in DB: " % item['url'])
        # else:
        tx.execute( \
            "INSERT INTO sites (url, title) "
            "VALUES (%s, %s)",
            (item['url'],
             item['title'])
        )
        log.info("New item saved: %s" % item['url'])

    def handle_error(self, e):
        log.error(e)
