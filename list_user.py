#!/usr/bin/env python
from sys import stdin
import json
import base64

report = json.loads(stdin.read())
table = base64.b64decode(report["Content"]).splitlines()
head = table[0].split(",")
table = table[1:]

for row in iter(table):
    user = dict(zip(head, row.split(",")))
    print "%s %s" % (user["access_key_1_last_rotated"], user["access_key_2_last_rotated"])
