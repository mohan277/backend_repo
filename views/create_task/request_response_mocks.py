

REQUEST_BODY_JSON = """
{
    "project": 1,
    "state": 1,
    "title": "string",
    "description": "string",
    "issue_type": "Task"
}
"""


RESPONSE_200_JSON = """
{
    "title": "string",
    "description": "string",
    "project": {
        "name": "string",
        "project_id": 1
    },
    "state": {
        "name": "string",
        "state_id": 1
    },
    "issue_type": "Task"
}
"""

