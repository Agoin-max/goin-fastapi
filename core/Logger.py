import os
from datetime import datetime
from loguru import logger

# 日志目录
log_path = os.getcwd() + "/loggers"
if not os.path.exists(log_path):
    os.mkdir(log_path)

# log_file = '{0}/nebula_{1}_log.log'.format(log_path, datetime.now().strftime("%Y-%m-%d"))
log_file = '{0}/nebula.log'.format(log_path)

# logger.add(log_file, rotation="00:00", retention="1 days", enqueue=True)
logger.add(log_file)
