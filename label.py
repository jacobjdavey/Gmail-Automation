from quickstart import create_service
from user import *

user = user() #create user profile
service = create_service() #build API
hexList = ['#000000','#434343','#666666','#999999','#cccccc','#efefef','#f3f3f3','#ffffff','#fb4c2f','#ffad47','#fad165','#16a766','#43d692','#4a86e8','#a479e2','#f691b3','#f6c5be','#ffe6c7','#fef1d1','#b9e4d0','#c6f3de','#c9daf8','#e4d7f5','#fcdee8','#efa093','#ffd6a2','#fce8b3','#89d3b2','#a0eac9','#a4c2f4','#d0bcf1','#fbc8d9','#e66550','#ffbc6b','#fcda83','#44b984','#68dfa9','#6d9eeb','#b694e8','#f7a7c0','#cc3a21','#eaa041','#f2c960','#149e60','#3dc789','#3c78d8','#8e63ce','#e07798','#ac2b16','#cf8933','#d5ae49','#0b804b','#2a9c68','#285bac','#653e9b','#b65775','#822111','#a46a21','#aa8831','#076239','#1a764d','#1c4587','#41236d','#83334c', '#464646','#e7e7e7','#0d3472','#b6cff5','#0d3b44','#98d7e4','#3d188e','#e3d7ff','#711a36','#fbd3e0','#8a1c0a','#f2b2a8','#7a2e0b','#ffc8af','#7a4706','#ffdeb5','#594c05','#fbe983','#684e07','#fdedc1','#0b4f30','#b3efd3','#04502e','#a2dcc1','#c2c2c2','#4986e7','#2da2bb','#b99aff','#994a64','#f691b2','#ff7537','#ffad46','#662e37','#ebdbde','#cca6ac','#094228','#42d692','#16a765']

class label:

    def __init__(self,color,name): #construct a label with color and name
        self.hexColor = color
        self.hexText = '#ffffff'
        self.name = name

    def createLabel(self): #create a label in gmail with given specs
        param = {'color': {'backgroundColor': self.hexColor,'textColor': self.hexText},
                 'name': self.name,'labelListVisibility': 'labelShow',
                 'messageListVisibility' : 'show', 'type': 'user'}
        
        return (service.users().labels().create(userId='me',body=param).execute())

def retrieveMail(query):
    allIds = []
    for x in range (20):
        emails = service.users().messages().list(userId='me', q=query, maxResults=50, 
                                                fields='messages/id').execute()
        message_ids = [msg['id'] for msg in emails.get('messages', [])]
        allIds.extend(message_ids)

    return allIds

def labelMail(label_ids, ids): #label given list of emails with given list of labels
    
    labelBody = {
        'addLabelIds': label_ids,
         'ids': ids
    }

    service.users().messages().batchModify(userId='me', body=labelBody).execute()