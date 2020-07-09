Devoloping software efficiently:
1. Time
2. Cost

soft -- Easily changeable & Easily understandable
ware -- Tool/Product
Hard -- Difficult to change
ware -- Product/Device

To satisfy the needs of the customers through the frequent updates

Effective_software: (time and cost)
cost/LOC -- cost to change the LOC(line of code)

A software will go through some feedback loops before final release

latency --

Making changes:
1. Finding the different places where we have to change the code
2. Don't break any functionality.
3. Core functionality of the software is coupled with database operations.

software has two characteristics -
1. structure - easy  to read and change
2. Behaviour - functionality




Clean Architecture:
clean architecture is a way of building best well structured software

1. Interactors
2. Storages
3.

lcsbjs
ignore adapters -- it is used for multiple apps
api_specs -- copy from fb post learning
conf --
constants --
	constants
	enums
	exceptions --

 dtos:
	ignore entities
storages :
	dto - storage related dto's

tests :
	ignore entities

utils:
	business logic








review session
1. After watching the screen we have to see what data we have to give.
2. Next what fields we have to give.
3. paginated results.
4. Next  note down the requests clearly whether it is required or not.
5. Note down the actions in the screen.
6. we have to ensure we are giving necessary information or not to frontend.
7. enums should be in CAPITAL SNAKE_CASE = "SNAKE_CASE".
8. Avoid nested dto's from storage implementation.
9. It is not a problem to send nested dto's to presenter.
10. Convert the dictionary into dto and pass to the interactor.(if the data contains more than three or more fields.).



1. validate every data  what we are taking from client.
2. set default values if the client is not given(limit and offset values).
3. Tests :
    1. test every bussiness logic in the interactor.
4. Models:
    1. maximum will cover on requirements.
        1. list down the entities.
        2. decide the realtions and map the relations.
        3. relation should be in between rows, but not in between tables.
        4.



from project_management_portal.models import (
    User,
    Task,
    State,
    Project,
    Workflow,
    Checklist,
    Transition,
)



# Create users with roles
# Assigning users to projects
# Create Workflows, States, Transitions, Checklists in transitions
p


# user
# def create_users():

    # users = [
    #     {
    #         'username': 'user_1',
    #         "name": "name_1",
    #         "is_admin": True,
    #         "profile_pic": "profile_pic_1"
    #     },
    #     {
    #         'username': 'user_2',
    #         "name": "name_2",
    #         "is_admin": False,
    #         "profile_pic": "profile_pic_2"
    #     }
    # ]

    # for user in users:
    #     User.objects.create(
    #         name=user['name'],
    #         is_admin=user['is_admin'],
    #         username=user['username'],
    #         profile_pic=user['profile_pic'])


# state
def create_states():

    states = [
        {
            "name": "TODO"
        },
        {
            "name": "Planning ELP"
        },
        {
            "name": "In Progress"
        },
        {
            "name": "Testing Completed"
        },
        {
            "name": "Self review Completed"
        },
        {
            "name": "To be reviewed"
        },
        {
            "name": "Completed"
        }
    ]

    for state in states:
        State.objects.create(name=state['name'])



# checklist
def create_checklists():

    checklists = [
        {
            "name": "I have followed all the objectives in this task by following ELP.",
            "is_mandatory": True
        },
        {
            "name": "I have maintained the clean code practices.",
            "is_mandatory": True
        },
        {
            "name": "I have completed the objectives as per the state.",
            "is_mandatory": True
        },
        {
            "name": "I agree above transition changes are done by me.",
            "is_mandatory": False
        }
    ]

    for checklist in checklists:
        Checklist.objects.create(name=checklist['name'],
                                 is_mandatory=checklist['is_mandatory'])




# transition
def create_transitions():

    checklist_obj_1 = Checklist.objects.get(id=1)
    checklist_obj_2 = Checklist.objects.get(id=2)
    checklist_obj_3 = Checklist.objects.get(id=3)
    checklist_obj_4 = Checklist.objects.get(id=4)

    list_of_checklist_objs = [
        checklist_obj_1,
        checklist_obj_2,
        checklist_obj_3,
        checklist_obj_4
    ]

    transitions = [
        {
            "name": "transition_1",
            "description": "description_1",
            "from_state": 1,
            "to_state": 2,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_2",
            "description": "description_2",
            "from_state": 1,
            "to_state": 3,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 4,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 5,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 2,
            "to_state": 3,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_2",
            "description": "description_2",
            "from_state": 2,
            "to_state": 4,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 2,
            "to_state": 5,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 2,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 2,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_2",
            "description": "description_2",
            "from_state": 3,
            "to_state": 4,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 3,
            "to_state": 5,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 3,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 3,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 4,
            "to_state": 5,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 4,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 4,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 5,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 5,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 6,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        }

    ]

    for transition in transitions:
        transition_obj = Transition.objects.create(
            name=transition['name'],
            description=transition['description'],
            from_state=transition['from_state'],
            to_state=transition['to_state']
        )

        transition_obj.checklist.set(transition['checklist'])


# workflow
def create_workflows():
    workflows = [
        {
            "name": "Agile",
            "states":
            "transitions":
        },
        {
            "name" = "workflow_2"
            "states":
            "transitions":
        },
        {
            "name" = "workflow_3"
            "states":
            "transitions":
        },
        {
            "name" = "workflow_4"
            "states":
            "transitions":
        },
        {
            "name" = "workflow_5"
            "states":
            "transitions":
        }
    ]

    for workflow in workflows:

        workflow_obj = Workflow.objects.create(
            name=workflow['name']
        )

        states
        transitions



# project
def create_projects():

    projects = [
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        },
        {
            "name":
            "created_by_id":
            "description":
            "workflow_type_id":
            "project_type":
            "assigned_to":
        }
        ]

    for project in projects:
        project_obj = Project.objects.create(
            name=project['name'],
            created_by_id=project['created_by_id'],
            description=project['description'],
            workflow_type_id=project['workflow_type_id'],
            project_type=project['project_type'],
            assigned_to = []
        )
# task
def create_tasks():

    tasks = [
        {
            "title":
            "description":
            "project_id":
            "issue_type":
            "state_id":
        },
        {
            "title":
            "description":
            "project_id":
            "issue_type":
            "state_id":
        },
        {
            "title":
            "description":
            "project_id":
            "issue_type":
            "state_id":
        },
        {
            "title":
            "description":
            "project_id":
            "issue_type":
            "state_id":
        },
        {
            "title":
            "description":
            "project_id":
            "issue_type":
            "state_id":
        }
        ]
