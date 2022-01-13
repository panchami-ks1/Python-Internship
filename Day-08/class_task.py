class students:
    student_id='1001'
    student_name='steve'
    student_record={'name':'steve','phone':'99999','guardian':'thomas'}
    student_profile={'id':'1001','name':'steve'}
    student_report={'id':'1001','examid':'cs01'}

    def login(self,id,name):
        if(self.student_id==id)and(self.student_name==name):
            print('Login Successful')

        else:
            print('Invalid Id and name')

    def registration (self,name,phone,guardian):
        if((name==self.student_record['name'])or(phone==self.student_record['phone']))and(guardian==self.student_record['guardian']):
            print('Record exists')
        else:
            print('Registration done')

    def report(self,id,exam_id):
        if(id==self.student_report['id']) and(exam_id==self.student_report['examid']):
            print('Report generated')
        else:
            print("No report present")

    def profile(self,id,name):
        if(id==self.student_profile['id']) and (name==self.student_profile['name']):
            print('Student profile found')
        else:
            print('No profile found with given ID')


obj=students()
# obj.login('1002','steve')
#obj.registration('steve','99999','thomas')
# obj.report('1001','cs01')
# obj.profile('1001','steve')

