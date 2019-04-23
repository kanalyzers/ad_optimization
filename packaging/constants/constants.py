#!/bin/bash
# Copyright 2018 Google Inc. All Rights Reserved.
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
"""Constants shared by preprocessing and modeling scripts."""


# Define the format of your input data as present in the CSV file

CSV_COLUMNS = ['C1','banner_pos','site_domain','site_category','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type','C15','C16','date','time','user_id','device_ip_count','device_id_count','user_count','user_hour_count','user_bagged'
]

CSV_COLUMN_DEFAULTS = [[0], [''], [0], [''], [0], [''], [''], [''], [''],
                       [''], [0], [0], [0], [''], [''], [0], [''], [0], [[0], [''], [0],]

LABEL_COLUMN = 'click'

LABELS = ['no click', 'yes click']