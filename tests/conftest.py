from unittest.mock import Mock, patch

import pytest


@pytest.fixture(scope='function')
def sprite():
    points = ((0, 0), (0, 100), (100, 0), (100, 100))
    return Mock(points=points)



@pytest.fixture(scope='session', autouse=True)
def create_directories(request):
    with patch('arcade.application.pyglet'):
        yield
