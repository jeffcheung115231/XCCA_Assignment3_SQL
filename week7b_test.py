import pytest
import pandas as pd
from week7 import *

def test_5():
	d = {'WORKER_TITLE': ['Accountant',  'Assistant Manager',  'Sales Manager',  'Supply Chain Manager',  'Operations Manager',  'Lead Engineer',  'Senior Engineer',  'Salesperson',  'Manager',  'Financial Analyst',  'Software Developer',  'Marketing Associate',  'Operations Supervisor',  'Marketing Specialist',  'Sales Manager',  'Customer Service Representative',  'CEO',  'Salesperson'], 'FIRST_NAME': ['David',  'Michael',  'Tom',  'James',  'Ivan',  'John',  'John',  'Kevin',  'Jane',  'Lisa',  'Charles',  'Zachary',  'Lily',  'Emma',  'Samantha',  'Melissa',  'Jessica',  'Frank'], 'SALARY': [950000,  90000,  90000,  85000,  80000,  80000,  80000,  80000,  75000,  75000,  72000,  72000,  70000,  68000,  68000,  65000,  60000,  33000]}
	ans =pd.DataFrame(data=d)
	ans = ans[["WORKER_TITLE","FIRST_NAME" ,"SALARY"]]
	assert all( question5() == ans)

def test_6():
	d = {'WORKER_TITLE': ['Assistant Manager', 'Sales Manager', 'Operations Manager', 'Lead Engineer', 'Senior Engineer', 'Salesperson', 'Manager', 'Financial Analyst', 'Software Developer', 'Marketing Associate', 'Marketing Specialist', 'Sales Manager'], 'FIRST_NAME': ['Michael', 'Tom', 'Ivan', 'John', 'John', 'Kevin', 'Jane', 'Lisa', 'Charles', 'Zachary', 'Emma', 'Samantha'], 'SALARY': [90000, 90000, 80000, 80000, 80000, 80000, 75000, 75000, 72000, 72000, 68000, 68000]}
	ans = pd.DataFrame(data =d)
	ans = ans[["WORKER_TITLE","FIRST_NAME" ,"SALARY"]]
	assert all(question6() == ans)

def test_7():
	d = { "DEPARTMENT":["Sales"], "No_Of_Workers":[4]}
	ans = pd.DataFrame(data =d)
	ans = ans[["DEPARTMENT","No_Of_Workers"]]
	assert all(question7() == ans)
