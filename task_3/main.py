import sys
import re
from collections import Counter

# Function to parse a single log line
def parse_log_line(line: str) -> dict:
    # Pattern to match log lines
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'
    match = re.match(pattern, line.strip())
    
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    else:
        raise ValueError("Invalid log line format")

# Function to load and parse logs from a file
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if line.strip():  # Skip empty lines
                    parsed_log = parse_log_line(line)
                    if parsed_log:
                        logs.append(parsed_log)
                    else:
                        print(f"Warning: Failed to parse line {line_number}: {line.strip()}")
        return logs
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError:
        print(f"Error: Failed to read file '{file_path}'.")
        return []
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")
        return []

# Function to filter logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    # Using functional programming - filter function with lambda
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))

# Function to count logs by level
def count_logs_by_level(logs: list) -> dict:
    # Using collections.Counter for counting
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))

# Function to display log counts
def display_log_counts(counts: dict):
    if not counts:
        print("No data available for display.")
        return

    print("\nLog Level        | Count")
    print("-----------------|----------")

    # Sort by count in descending order, then by level name for consistent output
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for level, count in sorted_counts:
        print(f"{level.upper():<16} | {count}")


def display_filtered_logs(logs: list, level: str):
    if not logs:
        print(f"\nNo logs found for level '{level.upper()}'.")
        return

    print(f"\nLog details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_log_file> [log_level]")
        print("Example: python3 main.py path/to/logfile.log")
        print("Example: python3 main.py path/to/logfile.log error")
        sys.exit(1)
    
    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Load logs from file
    logs = load_logs(file_path)
    
    if not logs:
        print("Failed to load any log entries.")
        sys.exit(1)

    # Count log statistics
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    # If a filter level is specified, show details
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        display_filtered_logs(filtered_logs, filter_level)


if __name__ == "__main__":
    main()
    
# Example command to run the script:

# python3 main.py path/to/logfile.log

# python3 main.py path/to/logfile.log error