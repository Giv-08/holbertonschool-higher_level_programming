import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template is not string")

    if not isinstance(attendees, list) and not all(isinstance(attendee, dict)for attendee in attendees):
        raise TypeError("Attendees is not list of dictionaries")

    if not template:
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

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
                raise ValueError("File already exists!")

            with open("file_name", 'rw') as file:
                file.write(new_template)

        except Exception as error:
            raise ValueError("{attendee[i]}: {error}")
