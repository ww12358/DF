# -*- coding:utf-8 -*-
import logging

logger = logging.getLogger('ftpuploader')
hdlr = logging.FileHandler('./log/error.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)