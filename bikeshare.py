import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for city (chicago, new york city, washington).HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name:(Chicago , New York City , Washington ").lower()
        if city not in CITY_DATA:
            print("\nInvalid input try again\n")
            continue
        else:
            break

    while True:
        time = input("Select a filter as: month, day, all or none?").lower()
        if time == 'month':
            month = input("Select month as: January, Feburary, March, April, May or June?").lower()
            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            day = input("Select day as: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break

        elif time == 'all':
            month = input("Select month as: January, Feburary, March, April, May or June?").lower()
            day = input("Select day as: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
        elif time == 'none':#this means that we have to consider month as well as day
            month = 'all'
            day = 'all'
            break       
        else:
            input("Invalid input!!!!! Please type again: (month, day, all or none)")
            break

    print(city)
    print(month)
    print(day)
    print('-'*45)
    return (city, month, day)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])#converting string to datetime format
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nMost Frequent Times of Travel...\n')
    start_time = time.time()#returns time in seconds


    # display the most common month
    common_month = df['month'].mode()[0]#returns single value in the series
    print(common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour#extracting hour from start time column
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print('-'*45)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nMost Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print('-'*45)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print('-'*45)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Gender information is not present in the city.")


    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("Birth year information is not present in this city.")


    print('-'*45)

"""Asking 5 lines of the raw data and more, if they want"""
def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data(Yes/no)").lower()
        if answer not in ['yes', 'no']:
            answer = input("Invalid input please try again!!!!").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more(Yes or No)").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nType yes to continue or no to exit!!!!!\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
