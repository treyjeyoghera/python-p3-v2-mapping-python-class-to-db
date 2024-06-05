#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

ipdb.set_trace()
https://moringa.instructure.com/courses/704/assignments/50679?module_item_id=108093#:~:text=ipdb%3E%20%20Department.create_table()

ipdb>  CURSOR.execute("PRAGMA table_info(departments)").fetchall()