# import json

# peoples_data = '''
#         {
#             "people" : [
#                         {
#                             "name": "mohan",
#                             "age": 21,
#                             "gender": "male",
#                             "qualification": "B.tech",
#                             "hobbies": ["crickert", "volley ball", "foot ball"],
#                             "languages_known": ["hindi", "englis", "telugu", "malayalam", "tamil", "kannada"],
#                             "email_Id": "mohan@gmail.com",
#                             "marital_status": false
#                         },
#                         {
#                             "name": "krishna",
#                             "age": 22,
#                             "gender": "Male",
#                             "qualification": "intermediate",
#                             "hobbies": ["crickert", "volley ball", "foot ball"],
#                             "languages_known": ["hindi", "englis", "telugu", "malayalam"],
#                             "email_Id": "krishna@gmail.com",
#                             "marital_status": true
#                         },
#                         {
#                             "name": "senam",
#                             "age": 23,
#                             "gender": "Male",
#                             "qualification": "10th",
#                             "hobbies": ["crickert", "volley ball", "foot ball"],
#                             "languages_known": ["hindi", "englis", "telugu"],
#                             "email_Id": "senam@gmail.com",
#                             "marital_status": null
#                         }
#                         ]
#         }
#         '''
# #data = json.loads(peoples_data)
# new_string = json.dumps(peoples_data,indent = 2)
# print(new_string)





# import json
# with open('data.json') as f:
#     new_data = json.load(f)

# for pupil in new_data['people']:
#     print(pupil['name'],pupil['age'],pupil['hobbies'],pupil['languages_known'])
    #del pupil['languages_known']
    
# print(new_data)

# with open('old_data.json','w') as f:
#     json.dump(new_data,f,indent = 2)
import re
pattern=re.compile("abc")
print(pattern)