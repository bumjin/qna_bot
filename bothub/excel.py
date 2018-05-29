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
      #filename = "bothub/handydef.xlsx"
      filename = "bothub/HANDY_GW8_Approval_ini_20180119.xlsx"
      book = openpyxl.load_workbook(filename)

      description_text = []
      # 맨 앞의 시트 추출하기
      sheetNames = ['globals.properties', 'jhomscfg.xml'] #book.sheetnames
      for sheetName in sheetNames:
        sheet = book[sheetName] 
        
        for record in sheet.rows:
          key = record[0].value
          availableValues = record[1].value
          description = record[2].value
          defaultValue = record[3].value

          if key == None: continue
          if availableValues == None: availableValues = ""
          if description == None: description = ""
          if defaultValue == None: defaultValue = ""
          #print ("key=",key)
          #print ("availableValues=",availableValues)
          #print ("description=",description)
          #print ("defaultValue=",defaultValue)

          if(key.lower().find(text) > -1 or 
              description.lower().find(text) > -1):
              #print('key:', key, ' defaultValue:', defaultValue,' description',description)
              #data.append([key, record[1].value], record[2].value)
              str = '\r\n--------------------------' + sheet.title + '--------------------------------------\r\n'
              str += "key: {key} \ndefaultValue: {defaultValue}\ndescription: {description}".format(key=key, defaultValue=defaultValue, description=description)
              str += '\r\n----------------------------------------------------------------------------------\r\n'
              description_text.append(str)
          
      return  ",".join(description_text)
    except IOError as e:
      return 'Error:{}'.format(e)