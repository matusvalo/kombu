from __future__ import absolute_import, unicode_literals

import pytest
import kombu

from .common import BasicFunctionality


@pytest.fixture()
def connection(request):
    return kombu.Connection('sqla+sqlite:///testdb.sqlite')


@pytest.mark.env('sqlalchemy')
class test_SqlAlchemyBasicFunctionality(BasicFunctionality):
    pass
