from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta



# create a model class that describes the table in the database.
# the Table class should inherit from the DeclarativeMeta class that is returned by declarative_base()

Base = declarative_base()
class Table(Base):
    __tablename__ = 'task' # specifies the table name in the database
    id = Column(Integer, primary_key=True)
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.string_field


class Todo:
    def __init__(self, db_engine):
        # create a session to access the database and store data in it.
        session_temp = sessionmaker(bind=db_engine)
        self.session = session_temp()
        self.command = None

    # main
    def run(self):
        while True:
            print('\n')
            print("1) Today's tasks")
            print("2) Week's tasks")
            print('3) All tasks')
            print('4) Missed tasks')
            print('5) Add task')
            print('6) Delete task')
            print('0) Exit')
            self.command = input()

            if self.command == '1':
                self.print_today()
            elif self.command == '2':
                self.print_week()
            elif self.command == '3':
                self.print_all()
            elif self.command == '4':
                self.print_missed()
            elif self.command == '5':
                self.add_task()
            elif self.command == '6':
                self.delete_task()
            elif self.command == '0':
                print('\nBye!')
                break

    # print all tasks in database
    def print_all(self):
        print('\nAll tasks:')

        # get all tasks
        rows = self.session.query(Table).order_by(Table.date_field).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for index, item in enumerate(rows, start=1):
                print(str(index) + '. ' + item.string_field + '. ' + str(item.date_field.day)
                      + ' ' + item.date_field.strftime('%b'))


    def add_task(self):
        print('Enter task')
        task = input()
        print('Enter deadline')
        deadline = input()

        # add new row to the table
        new_row = Table(string_field=task, date_field=datetime.strptime(deadline, format('%Y-%m-%d')).date())
        self.session.add(new_row)
        self.session.commit()
        print('The task has been added!')


    def print_week(self):
        today = datetime.today()
        days_range = []
        days_object = []
        for d in range(7):
            someday = today + timedelta(days=d)
            days_object.append(someday.date())
            days_range.append(someday.strftime('%Y-%m-%d'))
        rows = self.session.query(Table).filter(Table.date_field.in_(days_range)).order_by(Table.date_field).all()
        for day in days_object:
            print(day.strftime('\n%A %d %b'), end='')
            print(':')
            new_rows = list(filter(lambda x: str(x.date_field) == str(day), rows))
            if len(new_rows) == 0:
                print('Nothing to do!')
            else:
                for index, item in enumerate(new_rows, start=1):
                    print(str(index) + '. ' + item.string_field)


    def print_today(self):
        today = datetime.today()
        rows = self.session.query(Table).filter(Table.date_field == today.strftime('%Y-%m-%d')).all()
        print('\nToday ' + today.strftime('%d %b') + ':')
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for index, item in enumerate(rows, start=1):
                print(str(index) + '. ' + item.string_field)


    def print_missed(self):
        rows = self.session.query(Table).filter(Table.date_field < datetime.today().date()).all()
        if len(rows) == 0:
            print('Nothing is missed!')
        else:
            for index, item in enumerate(rows, start=1):
                print(str(index) + '. ' + item.string_field + ' ' + str(item.date_field))


    def delete_task(self):
        task_dict = {}
        print('\nChoose the number of the task you want to delete:')
        rows = self.session.query(Table).order_by(Table.date_field).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for index, item in enumerate(rows, start=1):
                task_dict[index] = item.string_field
                print(str(index) + '. ' + item.string_field + '. ' + str(item.date_field.day)
                      + ' ' + item.date_field.strftime('%b'))
        task = task_dict[int(input())]
        delete_rows = self.session.query(Table).filter(Table.string_field == task).all()
        if len(delete_rows) == 0:
            print('Nothing to delete!')
        
        # delete row in the table
        self.session.delete(delete_rows[0])
        self.session.commit()
        print('The task has been deleted!')


if __name__ == '__main__':
    # create the database file.
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')

    # create a table in the database file
    Base.metadata.create_all(engine)

    todo = Todo(engine)
    todo.run()
