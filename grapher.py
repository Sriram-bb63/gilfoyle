import argparse
import datetime
import matplotlib.pyplot as plt
from models import engine, Gilfoyle
from sqlalchemy.orm import sessionmaker
import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

def fetch_data(from_date, to_date):
    data = session.query(Gilfoyle).filter(Gilfoyle.date>=from_date, Gilfoyle.date<=to_date).all()
    data = pd.DataFrame.from_records([row.to_dict() for row in data])
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
    parser = argparse.ArgumentParser(description='Gilfoyle grapher')
    parser.add_argument('--from', '-f', dest='from_date', type=str, help='Start date in DD-MM-YYYY format')
    parser.add_argument('--to', '-t', dest='to_date', type=str, help='End date in DD-MM-YYYY format')
    parser.add_argument('--save', action='store_true', help='Save the report as ______')
    
    # Parse command line arguments
    args = parser.parse_args()
    from_date = datetime.datetime.strptime(args.from_date, '%d-%m-%Y').date()
    to_date = datetime.datetime.strptime(args.to_date, '%d-%m-%Y').date()

    # Fetch data from the database
    data = fetch_data(from_date, to_date)

    # Create and display the graph
    create_graph(data)

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