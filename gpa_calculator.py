import pandas as pd

NUMERIC_VALUE = {
    "HD": 7,
    "DI": 6,
    "CR": 5,
    "PS": 4,
    "FA": 0
}


def get_gpa(csv_file=None):
    if csv_file is None:
        raise ValueError("Please provide a CSV file path")

    weighted_grade_total = 0
    credit_total = 0
    
    df = pd.read_csv(csv_file)
    for ind in df.index:
        try:
            # for each course, get its grade and credit
            grade = df['Grade'][ind]
            credit = df['Credit points'][ind]

            # add to weighted grade and credit
            weighted_grade_total += NUMERIC_VALUE[grade] * credit
            credit_total += credit
        except KeyError:
            print("Invalid CSV format")
            return
    return weighted_grade_total / credit_total


print(get_gpa("test.csv"))
