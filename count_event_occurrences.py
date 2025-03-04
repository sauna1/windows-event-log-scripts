import re

def count_event_id_occurrences():
    input_file = input("Enter the input file name: ")
    event_id = input("Enter the Event ID to count: ")
    
    event_id_pattern = re.compile(f'<EventID>{event_id}</EventID>')
    count = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if event_id_pattern.search(line):
                    count += 1
        
        print(f"Event ID {event_id} occurred {count} times.")
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")

if __name__ == "__main__":
    count_event_id_occurrences()

