import os
import sys
import json
import csv

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote

class CSVReader(object):
 
  def __init__(self):
    return
    
  def find(self, text):
    try:
      with open('bothub/data.csv', 'r') as raw:
        lines = raw.readlines()
        wrapper = csv.reader(lines)
        description_text = []
        text = text.lower()
        for record in wrapper:
          key = record[0]
          defaultValue = record[1]
          description = record[2]
          if(key.lower().find(text) > -1 or description.lower().find(text) > -1):
            #print('key:', key, ' value:', value,' description',description)
            str = "key: {key} \ndefaultValue: {defaultValue}\n description: {description}".format(key=key, defaultValue=defaultValue, description=description)
            description_text.append(str)
          
        return  ",".join(description_text)
    except IOError as e:
      return 'Error:{}'.format(e)