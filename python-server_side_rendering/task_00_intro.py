import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template is not string")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)for attendee in attendees):
        print("Attendees is not list of dictionaries")

    if not template:
        print("Template is empty, no output files generated.")

    if not attendees:
        print("No data provided, no output files generated.")

    for index, attendee in enumerate(attendees, start=1):
        try:
        # dict method get() with two parameters
        # replace method returns a new string with the replacements
            new_template = template.replace("{name}", attendee.get("name", "N/A"))
            new_template = new_template.replace("{event_title}", attendee.get("event_title", "N/A"))
            new_template = new_template.replace("{event_date}", attendee.get("event_date", "N/A"))
            new_template = new_template.replace("{event_location}", attendee.get("event_location", "N/A"))

            # file_name = f"output_{index}.txt"
            # if os.path.exists(file_name):
            #     print("File already exists!")

            # with open("file_name", 'w') as file:
            #     file.write(new_template)
            file_name = f"output_{index}.txt"
            print(f"Generating file: {file_name}")  # Log file generation
            with open(file_name, 'w') as file:
                file.write(new_template)
                print(f"File {file_name} written successfully")
        except Exception as error:
            print(f"{index}: {error}")
