"""
Author: Davis Nguyen

Date class implements calendar dates which can be used for things
such as keeping track of a travel schedule.
"""

class Date():
    """
    Class called "Date" that implements calendar dates occurring on or
    after January 1, 1800.
    """

    # Class attribute that represents the smallest value allowed for instances
    # of the Date class. It is also the minimum year.
    min_year = 1800

    # Class attribute that represents the day of week on January 1 of the year
    # min_year.
    dow_jan1 = "Wednesday"

    def __init__(self, month=1, day=1, year=min_year):
        """
        Constructor that sets the values of the month, day, and year attributes
        of the date. It also checks for the validity of the date.

        month: the number of the inputted month, set to 1 as default value.
        day: the number of the inputted day, set to 1 as default value.
        year: the number of the inputted year, set to min_year as default value.
        """

        # Sets the values for the month, day, and year attributes of the date.
        self.__mth = month
        self.__dy = day
        self.__yr = year

        # List of the number of days in each month.
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the month is a wrong input, raise an exception for an invalid month.
        if 12 < month or month < 1:
            raise Exception("Invalid Month")

        # If the year is a wrong input, raise an exception for an invalid year.
        if year < self.min_year:
            raise Exception("Invalid Year")

        # If the year is a leap year, change the amount of days of February in the
        # list of month days to 29. Check for leap year using year_is_leap method.
        if self.year_is_leap():
            days_in_month[1] = 29

        # If the day is a wrong input, raise an exception for an invalid day.
        if day < 1 or day > days_in_month[month - 1]:
            raise Exception("Invalid Day")

    def month(self):
        """
        Method that returns the month of the date.
        """
        return self.__mth

    def day(self):
        """
        Method that returns the day of the date.
        """
        return self.__dy

    def year(self):
        """
        Method that returns the year of the date.
        """
        return self.__yr

    def year_is_leap(self):
        """
        Method that returns True if the year of the date is a leap year
        and False otherwise.
        """

        # If the year is a multiple of 400 and 100, then it is a leap
        # year and the method returns True.
        if (self.__yr % 400 == 0) and (self.__yr % 100 == 0):
            return True

        # If the year is a multiple of 4 and not a multiple of 100,
        # then it is a leap year and the method returns True.
        elif (self.__yr % 4 == 0) and (self.__yr % 100 != 0):
            return True

        # If the above cases are not True, then the year is not a leap
        # year, and the method returns False.
        else:
            return False

    def daycount(self):
        """
        Method that returns the total number of days from
        the start date January 1, 1800 to the date inputted by the user.
        """

        # List of the number of days in each month.
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the year of the date is a leap year, change the number of days
        # in February to 29 in the days in month list.
        if self.year_is_leap():
            days_in_month[1] = 29

        # Set a variable for the day count which will be added to and returned.
        day_count = 0

        # Create a Date object for the start date.
        start_date = Date(1, 1, self.min_year)
        
        # While loop that adds the days in each year from the start date to
        # the input date.
        while start_date.year() < self.year():

            # Add 365 to the day count since there are 365 days in a year.
            day_count += 365

            # If the year is a leap year, add 1 to the day count because leap
            # years have 1 extra day.
            if start_date.year_is_leap():
                day_count += 1
                
            # Add 1 to the year of the Date object to iterate through the next year.
            start_date = Date(1, 1, start_date.year() + 1)

        # While loop that adds the days in each month from the start date to
        # the input date.
        while start_date.month() < self.month():

            # Add the amount of days in a month to the day count.
            day_count += days_in_month[start_date.month() - 1]

            # Add 1 to the month of the Date object to iterate through the next month.
            start_date = Date(start_date.month() + 1, 1, start_date.year())

        # Add the date's days onto the day count.
        day_count += self.day()

        # Return the day count after the loops finish adding all the days.
        return day_count

    def day_of_week(self):
        """
        Method that returns the day of the week of the date.
        """
        
        # List of string names of the days of week.
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Count variable that counts days in a week to keep track of what
        # day of the week the day is on.
        count_days = 0

        # Save the index of the default day of the week in a variable. This uses
        # the day_names list which contains each day of the week.
        dow_index = day_names.index(self.dow_jan1)

        # Iterate through the day count of the date. As each day passes, add
        # 1 to the count variable. When the for loop ends, the number in the
        # count variable represents the day of the week the date is on.
        for i in range(0, self.daycount() - 1):
            count_days += 1

            # When the count variable reaches 7, that means it has been a full
            # week, so reset the count to 0 to start a new week.
            if count_days == 7:
                count_days = 0

        # If the count is 0, this means it has been 7 days or 1 week, so the
        # day of week is the start day, which in this case, is Wednesday.
        if count_days == 0:
            return day_names[dow_index]

        # If the count is 1, it has been 1 day after the start, which in
        # this case, is Thursday.
        if count_days == 1:
            return day_names[(dow_index + 1) % 7]

        # If the count is 2, it has been 2 days after the start, which in
        # this case, is Friday.
        if count_days == 2:
            return day_names[(dow_index + 2) % 7]

         # If the count is 3, it has been 3 days after the start, which in
        # this case, is Saturday.
        if count_days == 3:
            return day_names[(dow_index + 3) % 7]

        # If the count is 4, it has been 4 days after the start, which in
        # this case, is Sunday.
        if count_days == 4:
            return day_names[(dow_index + 4) % 7]

        # If the count is 5, it has been 5 days after the start, which in
        # this case, is Monday.
        if count_days == 5:
            return day_names[(dow_index + 5) % 7]

        # If the count is 6, it has been 6 days after the start, which in
        # this case, is Tuesday.
        if count_days == 6:
            return day_names[(dow_index + 6) % 7]

    def nextday(self):
        """
        Method that returns the date of the following/next day.
        """

        # List of the number of days in each month.
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Create variables of the month, day, and year of the date that will be changed.
        new_day = self.__dy
        new_month = self.__mth
        new_year = self.__yr

        # If the year of the date is a leap year, change the number of days
        # in February to 29 in the days in month list. 
        if self.year_is_leap():
            days_in_month[1] = 29

        # If adding 1 to the day is greater than the amount of days in the current month,
        # that means it is a new month, so add 1 to the month and set the day to 0.
        if (new_day + 1) > days_in_month[new_month-1]:
            new_month += 1
            new_day = 0

            # If the month is greater than 12, that means it is a new year, so add 1 to
            # the year and set the month to 1 to indicate it is now January.
            if new_month > 12:
                new_month = 1
                new_year += 1

        # After the if statements, add 1 to the day to have the next day of the date.
        new_day += 1

        # Return a Date object of the date of the following/next day.
        return Date(new_month, new_day, new_year)

    def prevday(self):
        """
        Method that returns the date of the previous day.
        """

        # If the date is the start date of January 1, 1800, raise an Exception
        # because the date does not have a previous day.
        if self.__mth == 1 and self.__dy == 1 and self.__yr == self.min_year:
            raise Exception("January 1, 1800 does not have a previous day.")

        # List of the number of days in each month.
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the year of the date is a leap year, change the number of days
        # in February to 29 in the days in month list.
        if self.year_is_leap():
            days_in_month[1] = 29

        # Create variables of the month, day, and year of the date that will be changed.
        new_day = self.__dy
        new_month = self.__mth
        new_year = self.__yr

        # If subtracting 1 to the day is zero, that means it is a new month, so subtract
        # 1 from the month. 
        if (new_day - 1) == 0:
            new_month -= 1

            # If the month is zero, that means it is going back a year, so subtract 1
            # from the year and set the month to 12 to indicate it is now December.
            if new_month == 0:
                new_month = 12
                new_year -= 1

            # When it is a new month, set the day equal to the amount of days of the month.
            new_day = days_in_month[new_month-1] + 1

        # After the if statements, subtract 1 from the day to have the previous day of the date.
        new_day -= 1

        # Return a Date object of the date of the previous day.
        return Date(new_month, new_day, new_year)

    def __add__(self, n):
        """
        Method that returns the date that occurs n days after the date self.

        n: an integer
        """

        # Create a Date object of the inputted date that will be changed.
        new_date = Date(self.__mth, self.__dy, self.__yr)

        # Use a for loop to iterate through n days.
        for i in range(n):

            # As the loop iterates, call the nextday method onto the date to add a day.
            new_date = new_date.nextday()

        # Return the Date object of the new date n days after the inputted date.
        return new_date

    def __sub__(self, n):
        """
        Method that returns the date that occurs n days before the date self.

        n: an integer
        """
        
        # If the date is the start date of January 1, 1800, raise an Exception
        # because the date does not have a previous day.
        if self.__mth == 1 and self.__dy == 1 and self.__yr == self.min_year:
            raise Exception("January 1, 1800 does not have previous days.")

        # Create a Date object of the inputted date that will be changed.
        new_date = Date(self.__mth, self.__dy, self.__yr)

        # Use a for loop to iterate through n days.
        for i in range(n):

            # As the loop iterates, call the prevday method onto the date to subtract a day.
            new_date = new_date.prevday()

        # Return the Date object of the new date n days before the inputted date.
        return new_date

    def __lt__(self, other):
        """
        Method that returns True if the self date comes before the other date.
        This is done by overloading the less than (<) operator.

        self: a first date
        other: a second date
        """
        return self.daycount() < other.daycount()

    def __eq__(self, other):
        """
        Method that returns True if the self date is the same as the other date.
        This is done by overloading the equal to (==) operator.

        self: a first date
        other: a second date
        """
        return self.__yr == other.__yr and self.__mth == other.__mth and self.__dy == other.__dy

    def __le__(self, other):
        """
        Method that returns True if the self date comes before or is the same as the
        other date. This is done by overloading the less than or equal to (<=) operator.

        self: a first date
        other: a second date
        """
        return self.daycount() <= other.daycount()

    def __gt__(self, other):
        """
        Method that returns True if the self date comes after the other date.
        This is done by overloading the greater than (>) operator.

        self: a first date
        other: a second date
        """
        return self.daycount() > other.daycount()

    def __ge__(self, other):
        """
        Method that returns True if the self date comes after or is the same as the
        other date. This is done by overloading the greater than or equal to (>=) operator.

        self: a first date
        other: a second date
        """
        return self.daycount() >= other.daycount()

    def __ne__(self, other):
        """
        Method that returns True if the self date is not the same as the other date.
        This is done by overloading the not equal to (!=) operator.

        self: a first date
        other: a second date
        """
        return self.__yr != other.__yr or self.__mth != other.__mth or self.__dy != other.__dy

    def __str__(self):
        """
        Method that returns a printable(i.e.,string) representation of the date.
        """
        
        # List of string names of each month.
        month_names = ["January", "February", "March", "April", "May", "June", "July"
            , "August", "September", "October", "November", "December"]
        
        return month_names[self.__mth - 1] + " " + str(self.__dy) + ", " + str(self.__yr)

    def __repr__(self):
        """
        Method that also returns a string representation of the date.
        """
        return str(self)


