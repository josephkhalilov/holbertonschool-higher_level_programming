import os

def generate_invitations(template, attendees):
    # --------------------------
    # 1. Type Checks
    # --------------------------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # --------------------------
    # 2. Empty Template Check
    # --------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # --------------------------
    # 3. Empty Attendees Check
    # --------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --------------------------
    # 4. Process Each Attendee
    # --------------------------
    for index, person in enumerate(attendees, start=1):
        processed_text = template

        # Fill missing values with "N/A"
        name = person.get("name") if person.get("name") else "N/A"
        title = person.get("event_title") if person.get("event_title") else "N/A"
        date = person.get("event_date") if person.get("event_date") else "N/A"
        loc  = person.get("event_location") if person.get("event_location") else "N/A"

        # Replace placeholders
        processed_text = processed_text.replace("{name}", name)
        processed_text = processed_text.replace("{event_title}", title)
        processed_text = processed_text.replace("{event_date}", date)
        processed_text = processed_text.replace("{event_location}", loc)

        # --------------------------
        # 5. Write Output File
        # --------------------------
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as out_file:
                out_file.write(processed_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue

    print("Invitation files generated successfully.")
