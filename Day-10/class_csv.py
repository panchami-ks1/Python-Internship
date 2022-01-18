import csv


class students:
    student_id = '1001'
    student_name = 'steve'
    student_record = [['name', 'phone', 'guardian'],
                      ['steve', '9999', 'thomas'], ['ann', '8888', 'francis']]

    student_profile = """ id,name
                        1001,steve
                        1002,ann
                     """
    student_report = [['id', 'examid'],
                      ['1001', 'cs01'], ['1002', 'cs01']]

    def login(self, id, name):
        if (self.student_id == id) and (self.student_name == name):
            print('Login Successful')

        else:
            print('Invalid Id and name')

    def registration(self, name, phone, guardian):
        with open('csvFiles/record.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.student_record)
        with open('csvFiles/record.csv', 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)

            for x in reader:
                if (name or phone) and (guardian) in x:
                    print('Record exists')
                    break
                else:
                    print('Registration done')
                    break

    def report(self, id, exam_id):
        with open('csvFiles/report.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.student_report)
        with open('csvFiles/report.csv', 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)

            for x in reader:
                if id and exam_id in x:
                    print('Report generated')
                    break
                else:
                    print("No report present")
                    break

    def profile(self, id, name):
        fp = open('csvFiles/profile.csv', 'w')
        fp.write(self.student_profile)
        with open('myfiles/data.csv', 'r') as fpr:
            data = fpr.readlines()
            for x in data:
                if id and name == x:
                    print('Student profile found')
                    break
                else:
                    print('No profile found with given ID')
                    break


obj = students()
obj.login('1002','steve')
obj.registration('steven', '999990', 'thomas')
obj.report('1001','cs01')
obj.profile('1001', 'steve')
