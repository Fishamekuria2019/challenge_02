# Import pathlib
import csv
from os import write
from pathlib import Path
from sys import path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    list_to_write = [
    [1,2,3,4,5,6]]
   
    assert fileio.save_csv(path('../data/qualifying_loans.csv'))

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    file_path = Path('../data/daily_rate_sheet.csv')
    bank_data = fileio.load_csv(file_path)
    current_credit_score = 750
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
def test_save_csv():
    csvpath = Path("./data/qualifying_loans.csv")
    fileio.save_csv(csvpath,[[1, 2, 3, 4, 5, 6]])
    assert csvpath.exists()


