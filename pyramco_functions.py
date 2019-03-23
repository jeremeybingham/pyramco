import json
import requests
import config
import pyramco

# pyramco functions
## a library of useful functions to extend pyramco
## functions in this file use only base ramco fields

### fetch_profile
# accepts a Contact GUID, fetches member info to populate a "profile" page
# add or remove Contact fields as needed

def fetch_profile(guid):
    profile_data = pyramco.get_entity('Contact', guid,'ContactId,\
address1_city,\
cobalt_password,\
cobalt_username,\
Contact_Annotation/FileName,\
Contact_Annotation/DocumentBody,\
donotbulkemail,\
donotemail,\
emailaddress1,\
firstname,\
lastname,\
mobilephone,\
parentcustomerid,\
ramco_lastcoedate,\
ramco_nrdsid,\
ramco_nrdsmembertype,\
ramco_nrdsprimaryassociation,\
ramco_primaryassociationid')
    committees = pyramco.get_entities('cobalt_committeemembership','cobalt_CommitteePositionId,cobalt_committeemembershipid',filters=f'statuscode<eq>533470000 AND cobalt_ContactId<eq>{guid}')
    return(profile_data,committees)