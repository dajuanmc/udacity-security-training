"""
Go to the FTC Cybersecurity for Small Business website and review 
the topic areas under Protect Your Small Business. 
(Note that these apply to businesses of all types and sizes.)
For each of the topic areas, find the matching protection technique. 
Select the best way to protect the specific area.

"""

# store the techniques in a list
protection_techniques = ['protect equipment and paper files', 
                         'make smart security your business as usual',
                         'know what to do if you are scammed',
                         'put all agreements in writing and verify compliance',
                         'know how to connect remotely to the network'
                         ]


# store the topics in a list
topic_area = ['physical security',
              'cybersecurity basics',
              'tech support scams',
              'vendor security',
              'secure remote access'
    ]


# create a dictionary mapping topic area with protective technique

correct_matches = {
    topic_area[0] : protection_techniques[0],
    topic_area[1] : protection_techniques[1],
    topic_area[2] : protection_techniques[2],
    topic_area[3] : protection_techniques[3],
    topic_area[4] : protection_techniques[4]   
    }


# access answer to topic 5 (get the value for this topic)

print(correct_matches.get(topic_area[4])) # -> know how to connect remotely to the network
