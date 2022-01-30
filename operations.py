from asyncio import events
import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
    f=open(events_json_file,'r+')
    d={
        'id': Event_ID
        'name':Event_Name
        'organizer':org
        'start date':Start_Date
        'start time':Start_Time
        'end date':End_Date
        'users registered':Users_Registered
        'capacity':Capacity
        'seats available':Availability
    }
    try:
        
        content=json.load(f)
        if d not in content:
            content.append(d)
           
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except JSONDecoderError:
        
        l1=[]
        l1.append(d)
        json.dump(l1,f)
    f.close()    

    

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    f=open(events_json_file,'r+')
    try:

        events=json.load(f)
        return events
    except:

        f.close()
        return False    

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    L1=[]
    f=open(events_json_file,'r+')
    try:

        events=json.load(f)

        for event in events:
            if event['id']==Event_ID:
                L1.append(event)
                f.close()
                return L1


def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    f=open(events_json_file,'r+')
    try:

        events=json.load(f)
        for event in events:

            if event['id']==event_id and event['organizer']==org:
                if detail_to_be_updated not in ['id','capacity']:
                    event[detail_to_be_updated]=updated_detail
                    f.seek(0)
                    f.truncate()
                    json.dump(events,f)
                    f.close()
                    return True
        f.close()
        return False
    except:
        f.close()
        return False                

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    f=open(events_json_file,'r+')
    try:

        events=json.load(f)
        c1=0
        for event in events:
            if event['id']==event_ID:
                break
            c+=1
        events.pop(c1)
        f.seek(0)
        f.truncate()
        json.dump(events,f)
        f.close()
        return True
    except:

        f.close()
        return False


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    f=open(events_json_file,'r+')
    try:

        events=json.load(f)
        for event in events:

            if event['id']==event_id and event['seat avail']>0 and Full_Name not in event['user registered'] :
                event['user registered'].append(Full_Name)
                event['seat available']-=1
                f.seek(0)
                f.truncate()
                json.dump(events,f)
                f.close()
                return True
        f.close()
        return False
    except:

        f.close()
        return False




def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    f=open(members_json_file,'r+')
    try:

        members=json.load(f)
        for member in members:
            if member['full name']==Full_Name:
                member['password']=new_password
                f.seek(0)
                f.truncate()
                json.dump(members,f)
                f.close()
                return True
        f.close()
        return False
    except:

        f.close()
        return False
                    

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
