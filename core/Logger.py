import os
from datetime import datetime
from loguru import logger

# 暂时写死
log_path = "/Users/goin/Python-FastAPI"
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_file = '{0}/nebula_{1}_log.log'.format(log_path, datetime.now().strftime("%Y-%m-%d"))

logger.add(log_file, rotation="12:00", retention="1 days", enqueue=True)
