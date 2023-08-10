class Person:
    name = None

    def greeting(self):
        print(f"I am {self.name}")


class Developer(Person):
    def do_job(self):
        print(f"I am writting code now...")


class Manager(Person):
    def manage(self):
        print('Deadline is coming, hurry up!')


class TeamLead(Developer, Manager):
    def manage(self):
        print('I am team lead.')
        super().manage()


if __name__ == '__main__':
    team_lead = TeamLead()
    team_lead.name = 'Bob'
    team_lead.greeting()
    team_lead.do_job()
    team_lead.manage()
