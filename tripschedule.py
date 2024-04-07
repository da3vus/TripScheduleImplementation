"""
Author: Davis Nguyen

TripSchedule class uses Date class and Trip class to
store trips in a schedule for one person.

Note: No two trips can overlap with each other. This means
the dates where a person is traveling on one trip cannot overlap
with the dates they are traveling on another.
Also, a person cannot depart on a trip on the same day they return
from another trip.
"""

# Import the Trip and Date classes.
from trip import Trip
from date import Date

class TripSchedule:
    """
    Class called "TripSchedule" that stores a collection of trips that form
    the trip schedule for one person.
    """

    def __init__(self):
        """
        Constructor that creates an empty trip schedule for trips to be
        added to.
        """

        # The schedule will be represented as a list.
        self.__schedule = []

    def insert(self, new_trip):
        """
        Method that adds a new trip to the schedule if it does not conflict
        with existing ones.

        new_trip: a Trip object to be added to the trip schedule.
        """

        # Iterate through the trips in the schedule and see if the new trip
        # conflicts with any other trips.
        for trip in self.__schedule:

            # If the new trip's departure date is the same day as the arrival date
            # of another trip, this creates a conflict, so raise an exception.
            if trip.departure() == new_trip.arrival() or trip.arrival() == new_trip.departure():
                raise Exception("Departure date is the same as arrival date of other trips.")

            # If the new trip overlaps with any of the other trips, this creates
            # a conflict, so raise an exception.
            if new_trip.overlaps(trip):
                raise Exception("Trips overlap.")

        # If there are no conflicts, add the new trip to the schedule.
        self.__schedule.append(new_trip)

    def delete(self, trip):
        """
        Method that deletes a trip from the schedule.

        trip: a Trip object in the schedule to be removed.
        """
        self.__schedule.remove(trip)

    def __len__(self):
        """
        Method that returns the length of the trip schedule(the total number
        of trips in the schedule). This overloads the len() function.
        """
        return len(self.__schedule)

    def __getitem__(self, j):
        """
        Method that returns the j-th trip in the schedule. This overloads
        the index operator.

        j: an index value used for the trip schedule list.
        """

        # Raise an index error if j is out of the list index range.
        if j >= len(self.__schedule):
            raise IndexError
        
        return self.__schedule[j]

    def __iter__(self):
        """
        Method that creates an iterator for a trip schedule. It returns a new
        trip schedule iterator object using the TripScheduleIterator class.
        """
        return TripScheduleIterator(self.__schedule) 

    def search(self, keyword):
        """
        Method that searches the schedule by keyword. If the keyword is an
        integer from 1 to 12(inclusive), all trips in the schedule that start
        in that month are printed out. Otherwise, the keyword is assumed to be
        a destination string value and all trips in the schedule with that
        destination are printed out. The trips are printed out sorted in order
        by departure date.

        keyword: a value that can either be an integer or a string.
        """

        # Create a list for the final sorted schedule that will add the sorted trips.
        sorted_schedule = []

        # If the keyword is an integer, create a list key_trips that has all
        # trips whose month matches with keyword.
        if type(keyword) is int:
            key_trips = list(filter(lambda x: x.departure().month() == keyword, self.__schedule))

        # If the keyword is a string, create a list key_trips that
        # has all trips whose destination matches with keyword.
        else:
            key_trips = list(filter(lambda x: x.destination() == keyword, self.__schedule))

        # Create a list of the sorted departure dates for each trip in key_trips.
        departure_list = sorted([trip.departure() for trip in key_trips])

        
        # For loop that iterates through each departure date in the departure_list.
        # These dates will help sort the trips themselves into the final
        # sorted schedule.
        for date in departure_list:

            # For each trip in the key_trips list, if the trip's departure date
            # is equal to the departure date in the departure_list, then add the
            # trip to the sorted schedule in its correct order.
            for trip in key_trips:
                if trip.departure() == date:
                    sorted_schedule.append(trip)
        
        # Print each trip in the final sorted schedule.
        for trip in sorted_schedule:
            print(trip)

    def available(self, month, year):
        """
        Method that returns a list of all available dates in month of year.
        Available dates are dates on which there is no travel scheduled.

        month: an integer between 1 and 12 representing a month.
        year: an integer representing a year.
        """

        # List of the number of days in each month.
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the year of the date is a leap year, change the number of days
        # in February to 29 in the month days list.
        if Date(month, 1, year).year_is_leap():
            monthdays[1] = 29

        # Create a list of all the available dates to be added to.
        available_dates = []

        # Create a list of all the dates for each trip, day to day.
        date_list = []

        # Iterate through each trip in the schedule and add each date in the
        # trip to the date_list.
        for trip in self.__schedule:
            date = trip.departure()
            for i in range(trip.duration()+1):
                date_list.append(date)
                date += 1 # Add 1 to the date to get the next day in the trip.

        # Iterate through each day in the given month.
        for day in range(1,monthdays[month-1]+1):

            # For each day in the month, set a Date object of the current date
            # in the iteration.
            new_date = Date(month, day, year)

            # If the current date is not in the date_list, that means the current
            # date is not a date of travel, so it is available and add it to
            # the available dates list.
            if new_date not in date_list:
                available_dates.append(new_date)

        # When the loops end, return the final list of available dates in month of year.
        return available_dates

    def weekend_travel(self, yr):
        """
        Method that returns a list of all trips in year yr that involve
        weekend travel. The list stores the trips in sorted order by departure date.

        yr: an intger representing a year.
        """

        # Create a list for the sorted trips in the schedule by departure date.
        sorted_schedule = []

        # Create a list of sorted departure dates for all trips.
        departure_list = sorted([trip.departure() for trip in self.__schedule])

        # Create a list of all the departure dates in the year yr for all trips.
        year_dates = [dep for dep in departure_list if dep.year() == yr]

        # Iterate through each departure date in the year_dates list.
        for date in year_dates:

            # For each trip in the schedule, if the trip's departure date
            # is equal to the departure date in the year_dates list, then
            # add the trip to the sorted schedule in its correct order.
            for trip in self.__schedule:
                if trip.departure() == date:
                    sorted_schedule.append(trip)

        # Using the final sorted schedule of trips by departure date, return a
        # new list of sorted trips that contain weekends.
        return [trip for trip in sorted_schedule if trip.containsweekend()]

    def earliest(self):
        """
        Method that returns the trip in the schedule that has the earliest
        departure date of all the trips.
        """

        # Create a list of sorted departure dates for all trips.
        departure_list = sorted([trip.departure() for trip in self.__schedule])

        # For each trip in the schedule, if the trip's departure date matches
        # the first departure date in the departure_list, then that is the first
        # trip in the schedule, so return it.
        for trip in self.__schedule:
            if trip.departure() == departure_list[0]:
                return trip

    def last(self):
        """
        Method that returns the trip in the schedule that has the latest
        departure date of all the trips.
        """

        # Create a list of sorted departure dates for all trips.
        departure_list = sorted([trip.departure() for trip in self.__schedule])

        # For each trip in the schedule, if the trip's departure date matches
        # the final departure date in the departure_list, then that is the last
        # trip in the schedule, so return it.
        for trip in self.__schedule:
            if trip.departure() == departure_list[-1]:
                return trip

    def sortbydeparture(self):
        """
        Method that sorts all the trips in the schedule by their departure dates.
        """

        # Create a list for the final sorted schedule.
        sorted_schedule = []

        # Create a list of sorted departure dates for all trips.
        departure_list = sorted([trip.departure() for trip in self.__schedule])

        # For loop that iterates through each departure date in the departure_list.
        for date in departure_list:

            # For each trip in the schedule, if the trip's departure date
            # is equal to the departure date in the departure_list, then add the
            # trip to the sorted schedule in its correct order.
            for trip in self.__schedule:
                if trip.departure() == date:
                    sorted_schedule.append(trip)

        # Set the original schedule equal to the final sorted schedule, showing
        # the sorted trips by departure date.
        self.__schedule = sorted_schedule

    def __str__(self):
        """
        Method that returns a string representation of the trip schedule.
        """

        # Turn all the trips in the schedule to strings using the map function
        # and then join the strings together using join() method.
        return "\n".join(map(str, self.__schedule))    

    def __repr__(self):
        """
        Method that returns a suitable string representation of a trip schedule.
        """
        return str(self)


class TripScheduleIterator:
    """
    Class called "TripScheduleIterator" that will be used as an iterator
    for the TripSchedule class.
    """
    
    def __init__(self, schedule):
        """
        Constructor that creates attributes of the trip schedule and an
        index value to find a specific trip.
        """
        self.__sched = schedule
        self.__idx = 0

    def __next__(self):
        """
        Method that returns the next trip in the trip schedule.
        """

        # If the index attribute is less than the length of the schedule, that
        # means it can be iterated through. Otherwise, raise a StopIteration to
        # indicate that it is done iterating through the schedule.
        if self.__idx < len(self.__sched):

            # The current trip in the iteration is the trip in the schedule at
            # the current value of the index attribute.
            current_trip = self.__sched[self.__idx]

            # After the current trip is determined, add 1 to the index attribute
            # to get the next trip in the iteration.
            self.__idx += 1

            # Return the current trip in the iteration.
            return current_trip
        else:
            raise StopIteration

        


