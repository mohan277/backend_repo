

REQUEST_BODY_JSON = """
{
    "user_id": 1,
    "name": "string",
    "description": "string",
    "workflow_type": 1,
    "project_type": "Classic Software"
}
"""


RESPONSE_200_JSON = """
{
    "name": "string",
    "description": "string",
    "workflow_type": {
        "name": "string",
        "workflow_type_id": 1
    },
    "project_type": "Classic Software",
    "user": {
        "name": "string",
        "user_id": 1
    },
    "created_at": "2099-12-31 00:00:00"
}
"""

