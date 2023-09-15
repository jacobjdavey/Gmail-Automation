from quickstart import createService
from user import *
from label import *
from collections import Counter
import random
import json

def generateLabels(query):
    service = createService()
    list = retrieveMail(query)
    senderList = []
    nameList = []
    emailList = []

    for m_id in list:
        message = service.users().messages().get(userId='me', id=m_id).execute() #fetch the 
                                                                                 #message using API
        payload = message['payload'] # get payload of the message 
        header = payload['headers'] # get header of the payload

        for item in header: # getting the Sender
            if item['name'] == 'From':
                msg_from = item['value']
                senderList.append(msg_from)
                print(msg_from)
    cnt = Counter(senderList)
    occur = 30
    commonSenders = [x for x, y in cnt.items() if y > occur] #find all emails occuring more than 
                                                             #times

    for email in commonSenders: #create separate lists for names and emails
        print(email)
        try:
            msg_from_name = email.split(' <')[0] #retrieve only the display name
            nameList.append(msg_from_name)
            msg_from_email = email.split(' <')[1].split('>')[0] #retrieve the email
            emailList.append(msg_from_email)
        except:
            msg_from_name = msg_from_email.split('@')[0] #retrieve only the display name
            nameList.append(msg_from_name)
    
    for num in range(len(nameList)):
        name = nameList[num] #specify name of label
        email = emailList[num] #specify email
        list = retrieveMail('from: ' + email) #find emails

        try:
            newLabel = label(random.choice(hexList),name).createLabel() #create label
        except:
            print(name + " Already exists")

        labelId = user.find_labelid(name) #labelId
        labelMail(labelId, list) #add list of emails to label


generateLabels('from: jacob.j.davey@vanderbilt.edu') #test