#Some code has been adapted from these sources:
#https://github.com/khaledimad/Explore-US-Bikeshare-Data/blob/c9cd87ded576bb284daa434187a51bfe9346aed8/bikeshare_2.py
#https://github.com/Aritra96/bikeshare-project/blob/ce9d6bb5416190587f212588de40fb43d0bc0752/bikeshare.py
#https://gitlab.com/tomjose1792/BikeShare-Project-Python/-/blob/c8399acf270415b19276a7de073d802dcc5dd17e/bikeshare.py

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Which city\'s data would you like to view: Chicago, New York City, or Washington?').lower()
        if city not in CITY_DATA:
            print('OOPS! \n Looks like that is not a valid input! Please try again from the three cities listed. \n Thank you :)')
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
"""Create a dictionary for months (keep getting hung up here)"""
months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
month = ''
while True:
    month = input('Please choose one month from January to June, or you may also choose \'all\' if you have no preference.').lower()
    if month not in months.keys():
        print('OOPS! \n Looks like that is not a valid input! Please try again from the months listed. \n Thank you :)')
        continue
    else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
day = ''
while True:
    day = input('Which day of the week would you like to view? \n Please choose one day from Sunday to Saturday, or you may choose \'all\' if you have no preference.').lower()
    if day in days:
        print('OOPS! \n Looks like that is not a valid input! Please try again from the days listed. \n Thank you :)')
        continue
    else:
        break

print('-'*40)
return city, month, day

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

#This section was copied from my code that was completed in
#Practice Problem #3 in the Project section, Concept #9
df = pd.read_csv(CITY_DATA[city])
"""Loads the data file into a dataframe"""

df['Start Time'] = pd.to_datetime(df['Start Time'])
"""Converts the Start Time column into datetime"""

df['month']  = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
"""Extracts month & day from Start Time to create two new columns"""

if month != 'all':
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = months.index(month) + 1
"""Filters by months/correspoding int."""

df = df[df['month'] == month]
"""Filters by month to create a new dataframe"""

if day != 'all':
    df = df[df['day_of_week'] == day]
"""Filters by day to create a new dataframe"""

return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

#This section was copied from my code that was completed in
#Practice Problem #1 in the Project section, Concept #5
print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

    # TO DO: display the most common month
popular_month = df['month'].mode()[0]
print(f'The most common month is: {popular_month}')

    # TO DO: display the most common day of week
popular_day = df['day_of_week'].mode()[0]
print(f'The most common day is: {popular_day}')

    # TO DO: display the most common start hour
df['hour'] = df['Start Time'].dt.hour
"""Need to extract hour(s) from the Start Time column to create its own 'hour' column, then we can proceed"""
popular_hour = df['hour'].mode()[0]
print(f'The most common hours is: {popular_hour}')

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

    # TO DO: display most commonly used start station
start_station = df['Start Station'].value_counts().idxmax()
"""The value_counts actually counts each start station, while the idxmax finds the value used the most"""
print(f'The most commonly used start station is: {start_station}')

    # TO DO: display most commonly used end station
end_station = df['End Station'].value_counts().idxmax()
"""The value_counts actually counts each end station, while the idxmax finds the value used the most"""
print(f'The most commonly used end stations is: {end_station}')

    # TO DO: display most frequent combination of start station and end station trip
combo_trip = df.groupby(['Start Station', 'End Station']).count()
"""The groupby function helps split the stations into a group of start and end to count the most popular combo"""
print(f'The most commonly used combination of the start station and end station in a trip is: {combo_trip}')

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

print('\nCalculating Trip Duration...\n')
start_time = time.time()

    # TO DO: display total travel time
total_travel_time = sum(df['Trip Duration'])
print('The total travel time is:', total_travel_time/3600, 'hours.')
"""[conversion]: 3600 (seconds) = 1 hour """

    # TO DO: display mean travel time
mean_travel_time = df['Trip Duration'].mean()
print('The mean travel time is:', mean_travel_time/60, 'minutes.')
"""[conversion]: 60 (seconds)  = 1 minute"""

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

#This section was copied from my code that was completed in
#Practice Problem #2 in the Project section, Concept #7

print('\nCalculating User Stats...\n')
start_time = time.time()

    # TO DO: Display counts of user types
user_types  = df['User Type'].value_counts()
df['User Type'] = df['User Type'].fillna('Not Found')
"""Will replace any NaN values"""
print(f'The user types are: {user_types}')

    # TO DO: Display counts of gender
gender_types = df['Gender'].value_counts()
df['Gender'] = df['Gender'].fillna('Not Found')
"""Will replace any NaN values"""
print(f'The gender types are: {gender_types}')

    # TO DO: Display earliest, most recent, and most common year of birth
#earliest birth year
earliest_dob = df['Birth Year'].min()
"""Min() finds the lowest number in the given data"""
df['Birth Year'] = df['Birth Year'].fillna('Not Found')
"""Will replace any NaN values"""
print(f'The earliest year of birth is: {earliest_dob}')

#most recent birth year
most_recent_dob = df['Birth Year'].max()
"""Max() finds the highest number in the given data"""
df['Birth Year'] = df['Birth Year'].fillna('Not Found')
"""Will replace any NaN values"""
print(f'The most recent year of birth is: {most_recent_dob}')

#most common birth year
most_common_dob = df['Birth Year'].value_counts().idxmax()
"""value_counts and idxmax will find the most repetitive year"""
df['Birth Year'] = df['Birth Year'].fillna('Not Found')
"""Will replace any NaN values"""
print(f'The most common year of birth is: {most_common_dob}')

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

def display_data(df):
    """Asks users if they want to see 5 lines at a time"""
    while True:
        answer = ['yes', 'no']
        choice = input('Would you like to view the trip data by 5 lines? Please respond with \'yes\' or \'no\'.').lower()
        if choice in answer == 'yes':
            start = 0
            end = 5
            data = df.iloc[start:end,:9]
            print(data)
        break
    else:
        print('OOPS! \n Looks like that is not a valid input! Please try again. \n Thank you :)')
    if choice == 'yes':
        while True:
            choice_2 = input('Would you like to view 5 more lines of trip data? Please respond with \'yes\' or \'no\'.').lower()
            if choice_2 in answer:
                if choice_2 == 'yes':
                    start += 5
                    end += 5
                    data = df.iloc[start:end, :9]
                    print(data)
                else:
                    break
            else:
                print('OOPS! \n Looks like that is not a valid input! Please try again. \n Thank you :)')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#Creating the dataset
df = sns.load_dataset('titanic') 
df=df.groupby('who')['fare'].sum().to_frame().reset_index()
#Creating the column plot 
plt.bar(df['who'],df['fare'],color = ['#F0F8FF','#E6E6FA','#B0E0E6']) 
#Adding the aesthetics
plt.title('Chart title')
plt.xlabel('X axis title')
plt.ylabel('Y axis title') 
#Show the plot
plt.show()