import pytest
from data import *

if __name__ == "__main__":
    pytest.main(['-v', '--tb=short', '--cov=./', '--cov-report=html', '--alluredir=allure-results'])