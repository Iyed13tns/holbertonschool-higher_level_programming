#!/usr/bin/env python3
import os
"""
Python function that generates personalized invitation files
from a template with placeholders and a list of objects.
"""


def generate_invitations(template_content, attendees):
    """
    function generating the documents
    Args:
        template_content : the template
        attendees: the list of attendees

    Retuns: nothing; just created the files
    """
    try:
        if not isinstance(template_content, str):
            raise TypeError("The template doesn't contain a string")

        if not isinstance(attendees, list):
            raise TypeError("The attendees is not a list")

        for attendee in attendees:
            if not isinstance(attendee, dict):
                raise TypeError("At least one"
                                " attendee does not have the correct information")

        if template_content == "":
            raise ValueError("Template is empty, no output files generated.")

        if attendees == []:
            raise ValueError("No data provided, no output files generated")
        try:
            i = 1
            for attendee in attendees:
                if attendee["name"]:
                    name = attendee["name"]
                else:
                    name = "N/A"
                if attendee["event_title"]:
                    event_title = attendee["event_title"]
                else:
                    event_title = "N/A"
                if attendee["event_date"]:
                    event_date = attendee["event_date"]
                else:
                    event_date = "N/A"
                if attendee["event_location"]:
                    event_location = attendee["event_location"]
                else:
                    event_location = "N/A"

                new_output = (template_content
                              .replace("{name}", name)
                              .replace("{event_title}", event_title)
                              .replace("{event_date}", event_date)
                              .replace("{event_location}", event_location))

                output_file_name = "output_" + str(i) + ".txt"
                i += 1

                if not os.path.exists(output_file_name):
                    with open(output_file_name, 'w') as new_file:
                        new_file.write(new_output)
                else:
                    raise FileExistsError("The file already exists")
        except:
            print("File generation issue")
    except:
        print("Invalid input")