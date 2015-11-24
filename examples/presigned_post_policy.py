# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 Compatible Cloud Storage, (C) 2015 Minio, Inc.
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

from datetime import datetime, timedelta

from minio import Minio
from minio import PostPolicy

__author__ = 'minio'

# find out your s3 end point here:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region

form = PostPolicy()
form.set_key('myobject')
form.set_bucket('mybucket')
expires_date = datetime.utcnow()+timedelta(days=10)
form.set_expires(expires_date)


client = Minio('https://<your-s3-endpoint>',
               access_key='YOUR-ACCESSKEYID',
               secret_key='YOUR-SECRETACCESSKEY')

print client.presigned_post_policy(form)