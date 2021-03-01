from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, name='id')
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


class Todo:
    def __init__(self, db_engine):
        session_temp = sessionmaker(bind=db_engine)
        self.session = session_temp()
        self.command = None

    def run(self):
        while True:
            print('\n')
            print("1) Today's tasks")
            print("2) Week's tasks")
            print('3) All tasks')
            print('4) Add task')
            print('0) Exit')
            self.command = input()

            if self.command == '1':
                self.print_today()
            elif self.command == '2':
                self.print_week()
            elif self.command == '3':
                self.print_all()
            elif self.command == '4':
                self.add_task()
            elif self.command == '0':
                print('\nBye!')
                break

    def print_all(self):
        print('\nAll tasks:')
        rows = self.session.query(Table).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for index, item in enumerate(rows, start=1):
                print(index, end='')
                print('. ', end='')
                print(item.string_field + '. ', end='')
                print(item.date_field.strftime('%d %b'))

    def add_task(self):
        print('Enter task')
        task = input()
        print('Enter deadline')
        deadline = input()
        new_row = Table(string_field=task, date_field=datetime.strptime(deadline, format('%Y-%m-%d')).date())
        self.session.add(new_row)
        self.session.commit()
        print('The task has been added!')

    def print_week(self):
        today = datetime.today()
        days_range = []
        days_object = []
        for d in range(today.weekday() + 1):
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
                    print(index, end='')
                    print('. ', end='')
                    print(item.string_field)

    def print_today(self):
        today = datetime.today()
        rows = self.session.query(Table).filter(Table.date_field == today.strftime('%Y-%m-%d')).all()
        print('\nToday ' + today.strftime('%d %b') + ':')
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for index, item in enumerate(rows, start=1):
                print(index, end='')
                print('. ', end='')
                print(item.string_field)


if __name__ == '__main__':
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    todo = Todo(engine)
    todo.run()
