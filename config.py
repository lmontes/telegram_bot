#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path


class BotConfiguration():
  def __init__(self, filename):
    if not os.path.isfile(filename):
      self.valid = False
      return
    f = open(filename, "r")
    self.conf = json.loads(f.read())
    f.close()
    self.valid = True

  def value(self, key):
    return self.conf[key]
  
  def isValid(self):
    return self.valid
