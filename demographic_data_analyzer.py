import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # People with and without advanced education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage with salary >50K
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # People who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Percentage of rich among those who work fewest hours
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # Country with highest percentage of >50K earners
    country_percentage = (
        df[df['salary'] == '>50K']['native-country'].value_counts()
        / df['native-country'].value_counts()
    ) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentag
