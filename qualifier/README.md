# Project Title:Loan qualifier

Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.
loan quailifier
It is the real truth of the world that most of us do not have enougn financial to buy whatever we desired, so that this project all about qualifying loans to get enough financial power to buy we what to buy. Based on monthly income, current monthly debt, credit score, loan amount and home value or item value , the loan qualifier will find banks or financial institutes which sort out qualifying loans available by linking to specific csv file. 
The main problem that inspire to me create this project is to filfull the way to find all available banks and financial istitutes to qualify for loans based their financial status which stated above.
The main contribution of the project for user is user will find out qualifying loans which eligible loans for the specified input and find out all available qualifying loans.



## Technologies

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.
The progrmming langauges used for this specific project is python 3.7.10('dev':conda) and operating system conda dev environment , while other CLI 



## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.
open terminal for mac or gitbash for windows and install the followwing CLI.
conda activate dev
pip install fire
pip install questionary
pip install pytest
![image](images/image2.png)

## Examples

This section should include screenshots, code blocks, or animations showing how your project works.

![image](images/image1.png)

"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    save_qualifying_loans = (qualifying_loans, "w")
    header = ("Lender","Max Loan Amount", "Max LTV", "Max DTI","Min Credit Score","Interest Rate")
    with open ('output_path', "w") as csv_file:
          csvwriter = csv.writer(csv_file, delimiter = " , ")
          csvwriter.writerow(header)
          for rows in qualifying_loans:
            csvwriter.writerow(rows)
            return rows


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)


## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

To use this project the above programming languages and data  should available;
![image](images/image1.png)
![image](images/image3.png)


## Contributors

In this section, list all the people who contribute to this project; since you may want to be reached by recruiters or potential collaborators, include your contact e-mail, and optionally your LinkedIn or Twitter profile.
Abiy T. Mekuria : abiym46.net@gmail.com or solebeli24@gmail.com
Khaled Karman: FinTech instructor
Venkata  :(TA)
Amanda Robinson :(TA)


## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify others what they can and can not do with your source code and files. Use this section to include the licence you want to use.
# License and copyright

Abiy T. Mekuria FinTech UCB Bootcomp
licensed under the [MIT license](license/License).