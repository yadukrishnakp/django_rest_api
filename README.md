# Time Slots

## Instruction

### Showing both Candidates and Interviewer
http://localhost:8000/
used to fetch details both candidates and interviewer. 


### Add both Candidates and Interviewer

http://localhost:8000/user_register/

example:
{
    "id": 7,
    "time_from": "09:00:00",
    "time_to": "14:00:00"
}

before add check availability of id
add available time duration of Interviewer and Candidates with using this query.


### Fetch available time slots between interviewer and candidates
http://localhost:8000/time_slots/1/2/

used to fetch available time slots between interviewer and candidates. in here candidates can also see available slots between interviewer. 

## Installation
pip3 install -r requirements.txt


