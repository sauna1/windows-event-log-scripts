import xml.etree.ElementTree as ET

def extract_events(input_file, event_id):
    output_file = "retrieved_events.xml"
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    matching_events = []
    in_event = False
    current_event = []
    
    for line in lines:
        if "<Event " in line:
            in_event = True
            current_event = [line]
        elif "</Event>" in line:
            current_event.append(line)
            in_event = False
            if any(f"<EventID>{event_id}</EventID>" in l for l in current_event):
                matching_events.extend(current_event)
        elif in_event:
            current_event.append(line)
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(matching_events)
    
    print(f"Extracted events have been saved to {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    event_id = input("Enter the Event ID to retrieve: ")
    extract_events(input_file, event_id)

