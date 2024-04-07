"""
Author: Davis Nguyen

Trip class uses Date class to keep track of a travel
schedule for one person.
"""

# Import the Date class.
from date import Date

class Trip:
    """
    Class called "Trip" that keeps track of the travel schedule for
    an employee whose job requires frequent travel.
    """

    def __init__(self, destination, depdate, duration):
        """
        Constructor that initializes the three trip instance
        attributes: destination, depdate, and duration.

        destination: the destination city of the trip(a string).
        depdate: the date on which the person departs on the trip(Date object).
        duration: the duration of the trip(integer >= 1).
        """

        # Instance attributes for destination, depdate, and duration.
        self.__dest = destination
        self.__dep = depdate
        self.__dur = duration

    def setDestination(self, destination):
        """
        Method that sets the trip destination to a given string value.

        destination: a string value representing a destination of a trip.
        """
        self.__dest = destination

    def setDeparture(self, depdate):
        """
        Method that sets the trip departure date to a given Date value.

        depdate: a Date object value representing a trip departure date.
        """
        self.__dep = depdate

    def setDuration(self, duration):
        """
        Method that sets the trip duration to a given integer value.

        duration: an integer value representing the duration of a trip.
        """
        self.__dur = duration

    def destination(self):
        """
        Method that returns the destination of the trip.
        """
        return self.__dest

    def departure(self):
        """
        Method that returns the departure date of the trip.
        """
        return self.__dep

    def duration(self):
        """
        Method that returns the duration of the trip.
        """
        return self.__dur

    def arrival(self):
        """
        Method that returns the arrival date for the trip. The return
        value is a Date object.
        """
        return self.__dep + self.__dur

    def overlaps(self, other):
        """
        Method that returns True if the trips self and other overlap and
        False otherwise. Two trips overlap if the dates of travel(departure
        and arrival) of one trip overlap with the dates of travel of the other.

        self: a Trip object
        other: a second Trip object
        """

        # Create lists to be added to for the dates in the two trips.
        date1_list = []
        date2_list = []

        # Create variables for the departure dates of the two trips to be added to.
        date1 = self.departure()
        date2 = other.departure()

        # Loop that iterates through the duration of the first trip and adds
        # every date within the trip to the date1 list.
        for i in range(self.duration()+1):
            date1_list.append(date1)
            date1 += 1 # Add 1 to get the next day of the trip.

        # Loop that iterates through the duration of the second trip and adds
        # every date within the trip to the date2 list.
        for i in range(other.duration()+1):
            date2_list.append(date2)
            date2 += 1 

        # For loop that checks if any date in the date1 list is in the
        # date2 list. If the date is in both lists, that means they overlap,
        # so return True.
        for date in date1_list:
            if date in date2_list:
                return True
            
        # For loop that checks if any date in the date2 list is in the
        # date1 list. If the date is in both lists, that means they overlap,
        # so return True.
        for date in date2_list:
            if date in date1_list:
                return True

        # If the for loops finish and no similar dates are found in both lists,
        # then the trips do not overlap, so return False.
        return False

    def containsweekend(self):
        """
        Method that returns True if the trip contains at least one day of a
        weekend(Saturday or Sunday) and False otherwise.
        """

        # Set a variable for the departure date of the trip to be added to.
        date = self.departure()

        # Loop that iterates through the duration of the trip.
        for i in range(self.duration()+1):

            # If the current day of the trip is a weekend, return True.
            if date.day_of_week() == "Sunday" or date.day_of_week() == "Saturday":
                return True

            # If the current day is not a weekend, add 1 to get the next day
            # and check again until the loop finishes.
            date += 1 

        # If the loop finishes and no weekends were found, then the trip does not
        # contain a weekend, so return False.
        return False

    def __str__(self):
        """
        Method that returns the trip details in a neatly formatted way. The trip
        details include the destination, the duration of the trip, the departure
        date(with the day of week), and the arrival date(with the day of week).
        """
        destination = "Destination: " + self.destination() + "\n"
        duration = "Duration: " + str(self.duration()) + " days\n"
        departure = "Departure: {}, {}\n".format(self.departure().day_of_week(), self.departure())
        arrival = "Arrival: {}, {}\n".format(self.arrival().day_of_week(), self.arrival())

        return destination + duration + departure + arrival

    def __repr__(self):
        """
        Method that returns a suitable string representation of the trip.
        """
        return str(self)
