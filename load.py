import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','new york city','washington']
days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
months=['january','february','march','april','may','june']    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        pd.load(CITY_DATA[city])
        input('Which name of a city you want to analyze?')
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:         
        
         city = input('Which city do you want to explore? chicago, new york city or washington?\n' ).lower()
        
         if city not in cities:
            print("please choose one of these: chicago, new york city, washington ")
         else:
              break
    
         
    while True:     
         filter=input('would you like to filter by month, day, both or none?\n').lower()
         if filter not in(['month' , 'day' , 'both' , 'none']):
            print('please choose one of them:month, day, both or none?\n')
         else:
             break
            
    while True:
         if filter in (['month','both']):
              month=input('which month?\n').lower()
              if month not in months:
                 print('please enter one of those:january,february,march,april,may,june\n')
              else:
                   break
         else:
              month ='all'      
              break          
    while True:                       
         if filter in(['day', 'both']):
             day=input('ok then! now which day?\n').lower()
             if day not in days:
                 print('choose one of them:saturday,sunday,monday,tuesday,wensday,thursday,friday\n')         
             else:
                  break
         else:
             day ='all'
             break
# TO DO: get user input for day of week (all, monday, tuesday, ... sund
     
    
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
    
    df=pd.read_csv(CITY_DATA[city]) 
    
    
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    
    df['day']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
   
    if month != 'all':
       month=months.index(month)+1
       df =df[df['month']==month]   
    
            
    if day != 'all':
       
       df=df[df['day']==day.title()] 
    
    
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    month=df['month'].mode()[0]
    print("most popular month:",month)
    # TO DO: display the most common day of week
    
    day=df['day'].mode()[0]
    print("most common day of the week:",day)
    # TO DO: display the most common start hour
   
    popular_hour=df['hour'].mode()[0]
    print("most popular hour:",popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most popular start station:',popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most popular end station:',popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + ' '+'to'+' ' +df['End Station']).mode()[0]
    
    
    print('most frequent trip',popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    from datetime import timedelta as td
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=(pd.to_datetime(df['End Time'])-pd.to_datetime(df['Start Time'])).sum()
    print("total travel time:",total_travel_time)   
    
    days = total_travel_time.days
    seconds = total_travel_time.seconds %3600 %60
    
    hours= total_travel_time.seconds //3600 
    minutes= total_travel_time.seconds %3600 //60 
    
    print('{} days, {} hours , {} minutes, {} seconds'.format(days,hours,minutes,seconds))
    # TO DO: display mean travel time
 
    mean_travel_time=(pd.to_datetime(df['End Time'])-pd.to_datetime(df['Start Time'])).mean()
    days = mean_travel_time.days
    seconds = mean_travel_time.seconds %3600 %60
    
    hours= mean_travel_time.seconds //3600 
    minutes= mean_travel_time.seconds %3600 //60
    print("mean travel time is:",mean_travel_time)
    print('{} days, {} hours, {} minutes, {} seconds'.format(days,hours,minutes,seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(load_data('washington','may','all').shape[0] ==     load_data('washington','all','all').shape[0])

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        birth=df['Birth Year'].dropna().astype('int64')
        
        print("the most recent year is:", birth.max(), "the most earlist year :",birth.min(),"the most common year",birth.mode()[0])
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
       
    ask=input('do you want to display raw data?\n')
    if ask.lower() == 'yes':
       print('size',df.size)
       count=0
       while True:   
          print(df.iloc[count:count+5])
          ask_2=input('another 5 ?\n').lower()
          if ask_2 =='yes':
             count +=5
           
          else:
               break
       
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
