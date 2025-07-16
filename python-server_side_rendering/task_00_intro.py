import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return


    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return


    for index, attendee in enumerate(attendees, start=1):

        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )


        output_file = f"output_{index}.txt"


        try:
            with open(output_file, 'w') as file:
                file.write(invitation)
            print(f"Generated: {output_file}")
        except Exception as e:
            print(f"Error writing to file {output_file}: {e}")