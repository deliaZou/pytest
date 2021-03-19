#!/usr/bin/env python
#coding=utf-8
import yaml

with open("test.yaml") as f:
    print(yaml.safe_load(f))
