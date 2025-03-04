import xml.etree.ElementTree as ET
from collections import defaultdict

def count_events_by_hour(input_file, target_event_id):
    tree = ET.parse(input_file)
    root = tree.getroot()

    event_count_by_hour = defaultdict(int)

    for event in root.findall('{http://schemas.microsoft.com/win/2004/08/events/event}Event'):
        event_id = event.find('{http://schemas.microsoft.com/win/2004/08/events/event}System').find('{http://schemas.microsoft.com/win/2004/08/events/event}EventID').text

        if event_id == target_event_id:
            time_created = event.find('{http://schemas.microsoft.com/win/2004/08/events/event}System').find('{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated').attrib['SystemTime']
            hour = time_created[:13]  
            event_count_by_hour[hour] += 1

    return event_count_by_hour

def generate_output(input_file, target_event_id):
    event_count_by_hour = count_events_by_hour(input_file, target_event_id)

    output_file = f"{target_event_id}_by_the_hour.txt"
    with open(output_file, 'w') as outfile:
        for hour, count in sorted(event_count_by_hour.items()):
            outfile.write(f"{hour}   {count}\n")

    print(f"Event ID {target_event_id} report saved as '{output_file}'.")

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    target_event_id = input("Enter the Event ID to analyze: ")
    
    generate_output(input_file, target_event_id)

