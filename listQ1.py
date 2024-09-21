# Program to create a list of names of people who attended a meeting and add a new name

attendees = ["Mucyo","Manzi"]

print("\nList of attendees:")
for attendee in attendees:
    print(attendee)

new_name = input("Enter the name of the new attendee: ")
attendees.append(new_name)

print("\nList of attendees:")
for attendee in attendees:
    print(attendee)
