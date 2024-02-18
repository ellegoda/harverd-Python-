from datetime import date
import inflect
import sys
def ageInminutes(dob_string):
    try:
        dob = date.fromisoformat(dob_string)
        today = date.today()
        nuber_of_minutes = abs((today - dob).days) * 24 * 60
        p = inflect.engine()
        return p.number_to_words(nuber_of_minutes, andword="").capitalize() + " minutes"
    except Exception as e:
        print("Invalid Date")
        sys.exit(1)

def main():
    dob_string = input("Date of Birth:")
    print(ageInminutes(dob_string))

if __name__ == "__main__":
    main()
