from rest_framework import serializers

from .constants import EmployeeType

EMPLOYEE_TYPES_LIST = [employee_type.value for employee_type in EmployeeType]

class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None
                 ):
        self.employee_id = employee_id                  # UUID
        self.age = age                                  # INT
        self.date_of_joining = date_of_joining          # DATE
        self.last_logged_in = last_logged_in            # DATETIME
        self.salary_in_inr = salary_in_inr              # FLOAT
        self.employee_type = employee_type              # ENUM - Possible values MANAGER,TECHNICIAN,DEVELOPER,SALES_MEMBER
        self.first_name = first_name                    # CHAR
        self.last_name = last_name                      # CHAR
        self.is_retired = is_retired                    # BOOL
        self.is_best_employee = is_best_employee        # BOOL - Can be None as well


class Company(object):
    def __init__(self, name, registration_id):
        self.name = name                                # CHAR
        self.registration_id = registration_id          # UUID


class EmployeeWithCompanyDetails(Employee):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):
        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)
        self.company = company                          # Company class instance


class CompanyWithEmployeesDetails(Company):
    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees              # List of Employee class instances

class EmployeeSerializer(serializers.Serializer):
    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatField()
    employee_type = serializers.ChoiceField(EMPLOYEE_TYPES_LIST)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField(required=False)

    def create(self, validated_data):
        return Employee(**validated_data)


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    registration_id = serializers.UUIDField()

    def create(self, validated_data):
        return Company(**validated_data)

class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):
    company = CompanySerializer()

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company = Company(**company_data)
        employee_with_company_details_obj = EmployeeWithCompanyDetails(company=company, **validated_data)
        return employee_with_company_details_obj

class CompanyWithEmployeeDetailsSerializer(CompanySerializer):
    employees = EmployeeSerializer(many=True)

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        list_of_employees_objs = [Employee(**employee_data) for employee_data in employees_data]
        return CompanyWithEmployeesDetails(employees=list_of_employees_objs, **validated_data)


# Task 1
def serialize_employee_object(employee_object):
    serializer = EmployeeSerializer(employee_object)
    return serializer.data

# Task 2
def deserialize_data_to_employee_object(employee_data):
    serializer = EmployeeSerializer(data=employee_data)
    is_valid_serializer = serializer.is_valid()

    if is_valid_serializer:
        saved_object_of_employee = serializer.save()
        return saved_object_of_employee
    return serializer.errors


# Task 3
def serialize_list_of_employee_objects(list_of_employee_objects):
    serializer = EmployeeSerializer(list_of_employee_objects, many=True)
    list_of_dictionaries = serializer.data
    return list_of_dictionaries


# Task 4
def deserialize_data_to_list_of_employee_objects(employees_data):
    serializer = EmployeeSerializer(data=employees_data, many=True)
    is_valid_serializer = serializer.is_valid()
    if is_valid_serializer:
        list_of_saved_objects_of_employees = serializer.save()
        return list_of_saved_objects_of_employees
    return serializer.errors

# Task 5
def serialize_employee_with_company_object(employee_with_company_object):
    serializer = EmployeeWithCompanyDetailsSerializer(employee_with_company_object)
    return serializer.data


# Task 6
def deserialize_data_to_employee_with_company_object(employee_with_company_data):
    serializer = EmployeeWithCompanyDetailsSerializer(data=employee_with_company_data)
    is_valid_serializer = serializer.is_valid()
    if is_valid_serializer:
        list_of_saved_objects = serializer.save()
        return list_of_saved_objects
    return serializer.errors


# Task 7
def serialize_company_with_employees_object(company_with_employees_object):
    serializer = CompanyWithEmployeeDetailsSerializer(company_with_employees_object)
    return serializer.data


# Task 8
def deserialize_data_to_company_with_employees_object(company_with_employees_data):
    serializer = CompanyWithEmployeeDetailsSerializer(data=company_with_employees_data)
    is_valid_serializer = serializer.is_valid()
    if is_valid_serializer:
        list_of_saved_objects = serializer.save()
        return list_of_saved_objects
    return serializer.errors
