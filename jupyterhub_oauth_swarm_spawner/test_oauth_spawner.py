from unittest import TestCase
from unittest.mock import patch, PropertyMock, Mock

from tornado.ioloop import IOLoop
from tornado.testing import gen_test, AsyncTestCase

from .oauth_spawner import OAuthSpawner


class OAuthSpawnerTestCase(AsyncTestCase):

    def setUp(self):

        OAuthSpawner.__bases__ = (self.mock_SwarmSpawner_class(), )

        self.io_loop = IOLoop.instance()
        self.spawner = OAuthSpawner()


    def mock_SwarmSpawner_class(self):

        user = Mock()
        type(user).name = PropertyMock(return_value='dummy@globo.com')
        type(user).state = PropertyMock(return_value='state')

        swarm_spawner = Mock()
        swarm_spawner.return_value.start = Mock(return_value=('127.0.0.1', 9000))
        swarm_spawner.return_value.stop = Mock(return_value=None)

        type(swarm_spawner).user = PropertyMock(return_value=user)
        type(swarm_spawner).service_prefix = PropertyMock(return_value='prefix')
        type(swarm_spawner).service_owner = PropertyMock(return_value='owner')

        return swarm_spawner.__class__

    def test_service_user_env(self):

        env = {}
        self.spawner.user_env(env)
        self.assertEqual(env.get('USER'), 'dummy@globo.com')

    
    def test_make_preexec_fn(self):

        self.assertEqual(self.spawner.make_preexec_fn("NoOne"), None)

    def test_service_name(self):

        self.assertEqual(self.spawner.service_name, 'prefix-owner-dummy')
