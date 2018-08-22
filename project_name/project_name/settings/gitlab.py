from .test import *

import os


TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_DIR = os.path.join(BASE_DIR, '..')
TEST_OUTPUT_FILE_NAME = 'gitlab-tests.xml'
