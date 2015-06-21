# Minimal Object Storage Library, (C) 2015 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest import TestCase

import mock
from nose.tools import raises

from minio import minio
from .minio_mocks import MockResponse

__author__ = 'minio'


class ListBuckets(TestCase):
    @mock.patch('requests.get')
    def test_prefix_is_string(self, mock_request):
        mock_request.return_value = MockResponse('GET', 'http://localhost:9000/hello', {}, 200)
        client = minio.Minio('http://localhost:9000')
        client.list_buckets(prefix='1234')

    @mock.patch('requests.get')
    @raises(TypeError)
    def test_prefix_fails_on_non_string(self, mock_request):
        mock_request.return_value = MockResponse('GET', 'http://localhost:9000/hello', {}, 200)
        client = minio.Minio('http://localhost:9000')
        client.list_buckets(prefix=1234)

    @mock.patch('requests.get')
    def test_recursive_is_boolean(self, mock_request):
        mock_request.return_value = MockResponse('GET', 'http://localhost:9000/hello', {}, 200)
        client = minio.Minio('http://localhost:9000')
        client.list_buckets(recursive=True)

    @mock.patch('requests.get')
    @raises(TypeError)
    def test_recursive_fails_on_non_boolean(self, mock_request):
        mock_request.return_value = MockResponse('GET', 'http://localhost:9000/hello', {}, 200)
        client = minio.Minio('http://localhost:9000')
        client.list_buckets(recursive='Hello')

    @mock.patch('requests.get')
    def test_make_bucket_works(self, mock_request):
        mock_request.return_value = MockResponse('GET', 'http://localhost:9000/hello', {}, 200)
        client = minio.Minio('http://localhost:9000')
        client.list_buckets()
