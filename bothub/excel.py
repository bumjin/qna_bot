import os
import sys
import json
import openpyxl

class ExcelReader(object):
 
  def __init__(self):
    return
    
  def find(self, text):
    try:
      # 엑셀 파일 열기
      filename = "bothub/handydef.xlsx"
      book = openpyxl.load_workbook(filename)

      # 맨 앞의 시트 추출하기
      sheet = book.worksheets[0]

      # 시트의 각 행을 순서대로 추출하기
      #data = []
      description_text = []
      for record in sheet.rows:
        key = record[0].value
        defaultValue = record[1].value
        description = record[2].value

        if key == None: continue
        if defaultValue == None: defaultValue = ""
        if description == None: description = ""
        #print (key, defaultValue, description)

        if(key.lower().find(text) > -1 or 
            description.lower().find(text) > -1):
            #print('key:', key, ' defaultValue:', defaultValue,' description',description)
            #data.append([key, record[1].value], record[2].value)
            str = "key: {key} \ndefaultValue: {defaultValue}\ndescription: {description}".format(key=key, defaultValue=defaultValue, description=description)
            description_text.append(str)
          
      return  ",".join(description_text)
    except IOError as e:
      return 'Error:{}'.format(e)