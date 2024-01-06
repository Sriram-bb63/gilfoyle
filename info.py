import argparse
import datetime
import matplotlib.pyplot as plt

# Function to simulate fetching data from a database
def fetch_data(start_date, end_date):
    # Replace this with actual database query logic
    # Simulating data for demonstration purposes
    data = {
        'dates': [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)],
        'values': [i * 10 for i in range((end_date - start_date).days + 1)]
    }
    return data

# Function to create and display a line graph
def create_graph(dates, values):
    plt.plot(dates, values)
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Graph of Values Over Time')
    plt.show()

# Function to aggregate values
def aggregate_values(values):
    return sum(values)

# Function to save the graph and aggregated result as a report
def save_report(dates, values, aggregated_value):
    # Replace this with actual saving logic
    # Simulating saving graph as an image and creating a report
    plt.plot(dates, values)
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Graph of Values Over Time')
    plt.savefig('report_graph.png')
    
    with open('report.txt', 'w') as file:
        file.write(f'Aggregated Value: {aggregated_value}')

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Data Analysis Script')
    parser.add_argument('--from', '-f', dest='start_date', type=str, help='Start date in DD-MM-YYYY format')
    parser.add_argument('--to', '-t', dest='end_date', type=str, help='End date in DD-MM-YYYY format')
    parser.add_argument('--save', action='store_true', help='Save the report (graph and aggregated result)')
    
    # Parse command line arguments
    args = parser.parse_args()
    start_date = datetime.datetime.strptime(args.start_date, '%d-%m-%Y').date()
    end_date = datetime.datetime.strptime(args.end_date, '%d-%m-%Y').date()

    # Fetch data from the database
    data = fetch_data(start_date, end_date)

    # Create and display the graph
    create_graph(data['dates'], data['values'])

    # Aggregate values
    aggregated_value = aggregate_values(data['values'])

    # Save report if --save flag is provided
    if args.save:
        save_report(data['dates'], data['values'], aggregated_value)
        print('Report saved successfully.')
    else:
        print(f'Aggregated Value: {aggregated_value}')

if __name__ == '__main__':
    main()
