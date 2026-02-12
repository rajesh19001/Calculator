"""
Birthday Calculator - Calculate your age in various time units
Author: M. Rajesh
"""

from datetime import datetime, timedelta
import calendar

def calculate_age_details(birth_date):
    """Calculate detailed age information from birth date"""
    
    # Current date and time
    now = datetime.now()
    
    # Calculate difference
    age_delta = now - birth_date
    
    # Years calculation
    years = now.year - birth_date.year
    if (now.month, now.day) < (birth_date.month, birth_date.day):
        years -= 1
    
    # Months calculation
    months = now.month - birth_date.month
    if now.day < birth_date.day:
        months -= 1
    if months < 0:
        months += 12
    
    # Days calculation (remaining days in current month)
    if now.day >= birth_date.day:
        days = now.day - birth_date.day
    else:
        # Get days in previous month
        prev_month = now.month - 1 if now.month > 1 else 12
        prev_year = now.year if now.month > 1 else now.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days = days_in_prev_month - birth_date.day + now.day
    
    # Total calculations
    total_days = age_delta.days
    total_hours = total_days * 24 + now.hour - birth_date.hour
    total_minutes = total_hours * 60 + now.minute - birth_date.minute
    total_seconds = total_minutes * 60 + now.second - birth_date.second
    
    # Weeks
    total_weeks = total_days // 7
    
    # Next birthday calculation
    next_birthday = datetime(now.year, birth_date.month, birth_date.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, birth_date.month, birth_date.day)
    
    days_to_birthday = (next_birthday - now).days
    
    # Next milestone ages
    next_milestone = ((years // 10) + 1) * 10
    years_to_milestone = next_milestone - years
    
    return {
        'years': years,
        'months': months,
        'days': days,
        'total_days': total_days,
        'total_weeks': total_weeks,
        'total_hours': total_hours,
        'total_minutes': total_minutes,
        'total_seconds': total_seconds,
        'next_birthday': next_birthday,
        'days_to_birthday': days_to_birthday,
        'next_milestone': next_milestone,
        'years_to_milestone': years_to_milestone,
        'birth_date': birth_date
    }

def get_zodiac_sign(month, day):
    """Get zodiac sign based on birth date"""
    zodiac_signs = {
        (3, 21, 4, 19): "Aries ♈",
        (4, 20, 5, 20): "Taurus ♉",
        (5, 21, 6, 20): "Gemini ♊",
        (6, 21, 7, 22): "Cancer ♋",
        (7, 23, 8, 22): "Leo ♌",
        (8, 23, 9, 22): "Virgo ♍",
        (9, 23, 10, 22): "Libra ♎",
        (10, 23, 11, 21): "Scorpio ♏",
        (11, 22, 12, 21): "Sagittarius ♐",
        (12, 22, 1, 19): "Capricorn ♑",
        (1, 20, 2, 18): "Aquarius ♒",
        (2, 19, 3, 20): "Pisces ♓"
    }
    
    for (start_month, start_day, end_month, end_day), sign in zodiac_signs.items():
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return "Unknown"

def get_day_of_week(date):
    """Get the day of the week for a given date"""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[date.weekday()]

def display_results(age_info):
    """Display the age information in a formatted way"""
    
    birth_date = age_info['birth_date']
    
    print("\n" + "="*70)
    print(" 🎂 BIRTHDAY CALCULATOR - YOUR LIFE IN NUMBERS 🎂".center(70))
    print("="*70 + "\n")
    
    # Birth Information
    print("📅 BIRTH INFORMATION:")
    print(f"   Birth Date: {birth_date.strftime('%B %d, %Y')}")
    print(f"   Born on: {get_day_of_week(birth_date)}")
    print(f"   Zodiac Sign: {get_zodiac_sign(birth_date.month, birth_date.day)}")
    
    print("\n" + "-"*70 + "\n")
    
    # Current Age
    print("🎈 CURRENT AGE:")
    print(f"   {age_info['years']} Years, {age_info['months']} Months, and {age_info['days']} Days")
    
    print("\n" + "-"*70 + "\n")
    
    # Detailed Time Lived
    print("⏰ TIME YOU'VE LIVED:")
    print(f"   📆 Total Days:      {age_info['total_days']:,} days")
    print(f"   📅 Total Weeks:     {age_info['total_weeks']:,} weeks")
    print(f"   🕐 Total Hours:     {age_info['total_hours']:,} hours")
    print(f"   ⏱️  Total Minutes:   {age_info['total_minutes']:,} minutes")
    print(f"   ⏲️  Total Seconds:   {age_info['total_seconds']:,} seconds")
    
    print("\n" + "-"*70 + "\n")
    
    # Next Birthday
    print("🎉 NEXT BIRTHDAY:")
    print(f"   Date: {age_info['next_birthday'].strftime('%B %d, %Y')}")
    print(f"   Day: {get_day_of_week(age_info['next_birthday'])}")
    print(f"   Days until: {age_info['days_to_birthday']} days")
    print(f"   You'll turn: {age_info['years'] + 1} years old")
    
    print("\n" + "-"*70 + "\n")
    
    # Fun Facts
    print("💡 FUN FACTS:")
    print(f"   🎯 Next milestone age: {age_info['next_milestone']} (in {age_info['years_to_milestone']} years)")
    print(f"   🌍 You've experienced approximately {age_info['years']} New Year's Eve celebrations")
    print(f"   🎂 You've had {age_info['years']} birthday cakes (hopefully!)")
    print(f"   💤 You've slept approximately {age_info['total_days'] // 3:,} days (assuming 8 hours/day)")
    print(f"   💓 Your heart has beaten approximately {age_info['total_seconds'] * 70:,} times (at 70 bpm)")
    
    # Age in different units (alternative view)
    print("\n" + "-"*70 + "\n")
    print("📊 YOUR AGE IN ALTERNATIVE UNITS:")
    print(f"   If measured in months: {age_info['years'] * 12 + age_info['months']} months old")
    print(f"   If measured in weeks: {age_info['total_weeks']:,} weeks old")
    print(f"   If measured in days: {age_info['total_days']:,} days old")
    print(f"   If measured in hours: {age_info['total_hours']:,} hours old")
    
    print("\n" + "="*70 + "\n")

def get_birth_date():
    """Get birth date from user input"""
    while True:
        print("\n🎂 Enter your birth date:")
        print("-" * 40)
        
        try:
            year = int(input("Year (e.g., 2000): "))
            month = int(input("Month (1-12): "))
            day = int(input("Day (1-31): "))
            
            # Optional: time of birth
            include_time = input("\nDo you know your birth time? (y/n): ").lower()
            
            if include_time == 'y':
                hour = int(input("Hour (0-23): "))
                minute = int(input("Minute (0-59): "))
                second = int(input("Second (0-59, or 0 if unknown): "))
                birth_date = datetime(year, month, day, hour, minute, second)
            else:
                birth_date = datetime(year, month, day)
            
            # Validate date
            if birth_date > datetime.now():
                print("\n❌ Error: Birth date cannot be in the future!")
                continue
            
            return birth_date
            
        except ValueError as e:
            print(f"\n❌ Invalid input! Please enter valid numbers. Error: {e}")
            continue

def main():
    """Main function to run the birthday calculator"""
    
    print("\n" + "="*70)
    print(" 🎉 WELCOME TO BIRTHDAY CALCULATOR 🎉".center(70))
    print("="*70)
    print("\n Calculate your age in years, months, days, hours, minutes, and seconds!")
    
    # Get birth date from user
    birth_date = get_birth_date()
    
    # Calculate age details
    age_info = calculate_age_details(birth_date)
    
    # Display results
    display_results(age_info)
    
    # Option to calculate for another date
    while True:
        again = input("\nWould you like to calculate another birthday? (y/n): ").lower()
        if again == 'y':
            birth_date = get_birth_date()
            age_info = calculate_age_details(birth_date)
            display_results(age_info)
        else:
            print("\n✨ Thank you for using Birthday Calculator! ✨\n")
            break

if __name__ == "__main__":
    main()
