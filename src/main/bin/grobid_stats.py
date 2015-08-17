#!/usr/bin/env python2.7
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

import json
import os
from os.path import join, isfile

path = "grobid_json"
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]

numGrobid = 0
numFiles = 0
noGrobidFiles=[]
for f in onlyfiles:
    with open(os.path.join(path, f), 'r') as fd:
        jsonObj = json.load(fd)
        realJson = jsonObj[0]
        if "grobid:header_Class" in realJson:
            numGrobid += 1
        else:
            noGrobidFiles.append(os.path.join(path, f))

        numFiles += 1

print "Done processing."
print "Num Grobid: ["+str(numGrobid)+"]"
print "Num Files: ["+str(numFiles)+"]"
print "No Grobid: "+str(noGrobidFiles)
