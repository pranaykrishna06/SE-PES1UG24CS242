
from datetime import datetime


def format_visitor_name(name):
    """Formats a full name as Surname, Given names."""
    if not isinstance(name, str):
        return ""

    parts = name.split()

    if not parts:
        return ""

    return parts[-1].title() + ', ' + ' '.join(parts[:-1]).title()


def parse_group_ages(text):
    """Parses space-separated ages into a list of integers."""
    if not isinstance(text, str):
        return []

    try:
        return [int(age) for age in text.split()]
    except ValueError:
        return []


def parse_visit_date(text):
    """Parses a valid YYYY-MM-DD date."""
    if not isinstance(text, str):
        return None

    try:
        date = datetime.strptime(text.strip(), '%Y-%m-%d')

        if date.strftime('%Y-%m-%d') != text.strip():
            return None

        return date.year, date.month, date.day

    except ValueError:
        return None


def main():
    print("==== Running format_visitor_name ====")
    value = input("Enter a visitor's full name (e.g. asha rao): ")
    print("Name on ticket:", format_visitor_name(value))

    print("\n==== Running parse_group_ages ====")
    value = input("Enter the ages in the group separated by spaces (e.g. 34 12 70): ")
    print("Group ages:", parse_group_ages(value))

    print("\n==== Running parse_visit_date ====")
    value = input("Enter the visit date as YYYY-MM-DD (e.g. 2026-11-05): ")
    print("Visit date (year, month, day):", parse_visit_date(value))


if __name__ == "__main__":
    main()
