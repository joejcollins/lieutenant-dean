""" python test-unittest.py """

import unittest
import mock
from freezegun import freeze_time
import responses
import tasks

class TestTasks(unittest.TestCase):
    
    @responses.activate
    @freeze_time('2018-05-01T02:30:00')
    @mock.patch('tasks.os.makedirs')
    @mock.patch('tasks.os.path.exists', return_value=False)
    @mock.patch('tasks.open', new_callable=mock.mock_open)
    def test_fetch_data(self, mock_open, mock_path_exists, mock_makedirs):
        responses.add(responses.GET, 'http://some-url', body='0,1,2\n3,4,5', status=200)
        task = tasks.fetch_data.s(url='http://some-url').apply()
        self.assertEqual(task.status, 'SUCCESS')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'http://some-url/')
        mock_makedirs.assert_called_once_with('./data')
        mock_open.assert_called_once_with('./data/20180501T023000000000', 'w')

if __name__ == '__main__':
    unittest.main()