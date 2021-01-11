# -*- coding:utf-8 -*-
import unittest
import warnings
import logging.config
from Common.ProjectPath.file_path import log_config_path

logging.config.fileConfig(log_config_path)


class StartEnd(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        logging.info('==' * 30 + '用例分割线' + '==' * 30)

    def tearDown(self):
        warnings.simplefilter("ignore", ResourceWarning)


if __name__ == '__main__':
    unittest.main()
