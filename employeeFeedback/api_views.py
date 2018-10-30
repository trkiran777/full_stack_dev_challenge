from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from employeeFeedback.models import Employee


class EmployeeDetails(APIView):

    def post(self, request):
        data = request.DATA
        emp_email = data.get('employeeEmail')
        if Employee.objects.filter(empEmail=emp_email).exists():
            raise Exception("Employee already exists with this email")
        else:
            emp_name = data.get('employeeName')
            designation = data.get('designation')
            joining_date = data.get('joiningDate')
            joining_date = datetime.strptime(joining_date, '%Y-%m-%d')
            mobile_number = int(data.get('mobileNumber'))
            address = data.get('address')
            emp_id = 'EMP' + datetime.now().strftime('%y%m%d%H%M%S%f')
            employee = Employee(empId=emp_id,
                                empName=emp_name,
                                designation=designation,
                                joiningDate=joining_date,
                                mobileNumber=mobile_number,
                                empEmail=emp_email,
                                address=address)
            employee.save()

        return Response({"result": {}})

    def get(self, request):
        data = request.DATA
        return Response({ "result": {}})