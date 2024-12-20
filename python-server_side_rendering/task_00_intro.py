import os, sys

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template is not string")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)for attendee in attendees):
        print("Attendees is not list of dictionaries")

    if not template:
        print("Template is empty, no output files generated.")
        sys.exit()

    if not attendees:
        print("No data provided, no output files generated.")
        sys.exit()

    for index, attendee in enumerate(attendees, start=1):
        try:
        # dict method get() with two parameters
        # replace method returns a new string with the replacements
            new_template = template.replace("{name}", attendee.get("name", "N/A"))
            new_template = new_template.replace("{event_title}", attendee.get("event_title", "N/A"))
            new_template = new_template.replace("{event_date}", attendee.get("event_date", "N/A"))
            new_template = new_template.replace("{event_location}", attendee.get("event_location", "N/A"))

            file_name = f"output_{index}.txt"

            if os.path.exists(file_name):
                raise print("File already exists!")

            with open(file_name, 'w') as file:
                file.write(new_template)
        except Exception as error:
            print(f"{index}: {error}")
# TESTING
# # Define a sample template
# template = """
# Hello {name},

# You are invited to the {event_title} on {event_date} at {event_location}.

# We look forward to your presence.

# Best regards,
# Event Team
# """

# # Define a list of attendees
# attendees = [
#     {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
#     {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
#     {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
# ]

# # Call the function with the template and attendees list
# generate_invitations(template, attendees)
