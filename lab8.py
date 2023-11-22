from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Створення бази даних та об'єкта базового класу
Base = declarative_base()
engine = create_engine('sqlite:///lab8.db', echo=True)

# Визначення класу моделі для доходів
class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    source = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now)

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сеансу для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# CRUD операції
def create_income(amount, source):
    income = Income(amount=amount, source=source)
    session.add(income)
    session.commit()

def read_incomes():
    incomes = session.query(Income).all()
    return incomes

def update_income(income_id, new_amount, new_source):
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        income.amount = new_amount
        income.source = new_source
        session.commit()

def delete_income(income_id):
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        session.commit()

# Приклад використання
create_income(1000, 'Salary')
create_income(500, 'Freelance')
incomes = read_incomes()
print("All Incomes:")
for income in incomes:
    print(f"{income.id} - {income.amount} from {income.source} on {income.date}")

update_income(1, 1200, 'New Salary')
incomes = read_incomes()
print("\nUpdated Incomes:")
for income in incomes:
    print(f"{income.id} - {income.amount} from {income.source} on {income.date}")

delete_income(2)
incomes = read_incomes()
print("\nIncomes after deletion:")
for income in incomes:
    print(f"{income.id} - {income.amount} from {income.source} on {income.date}")
