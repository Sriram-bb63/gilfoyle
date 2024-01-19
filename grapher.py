import argparse
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from models import engine, Gilfoyle
from sqlalchemy.orm import sessionmaker
import pandas as pd
import seaborn as sns

Session = sessionmaker(bind=engine)
session = Session()


def fetch_data(from_date, to_date) -> list:
    data = session.query(Gilfoyle).filter(Gilfoyle.date>=from_date, Gilfoyle.date<=to_date).all()
    return data


def convert_to_dataframe(data):
    df = pd.DataFrame([{'sessionId': row.sessionId, 'DateTime': datetime.datetime.combine(row.date, row.time), 'ram': row.ram, 'battery': row.battery, 'temperature': row.temperature, 'rpm': row.rpm} for row in data])
    return df


def plot_subplots_seaborn(data):
    sns.set(style="darkgrid", font_scale=1.2)
    fig, ax = plt.subplots(4, 1, sharex=True, figsize=(15, 9))
    dateFormat = DateFormatter("%d-%m-%y \n %H:%M")

    ax[0].set_title("Memory Usage")
    sns.lineplot(ax=ax[0], x=data["DateTime"], y=data["ram"], color='blue', label="RAM Usage")
    ax[0].xaxis.set_major_formatter(dateFormat)
    ax[0].set(ylim=(0, 100))
    ax[0].set_ylabel("Memory (GB)")
    ax[0].legend()
    
    ax[1].set_title("Battery Level")
    sns.lineplot(ax=ax[1], x=data["DateTime"], y=data["battery"], color='green', label="Battery Level")
    ax[0].xaxis.set_major_formatter(dateFormat)
    ax[1].set(ylim=(0, 100))
    ax[1].set_ylabel("Battery Level (%)")
    ax[1].legend()

    ax[2].set_title("Core Temperature")
    sns.lineplot(ax=ax[2], x=data["DateTime"], y=data["temperature"], color='orange', label="Temperature")
    ax[0].xaxis.set_major_formatter(dateFormat)
    ax[2].set(ylim=(0, 100))
    ax[2].set_ylabel("Temperature (°C)")
    ax[2].legend()

    ax[3].set_title("Fan RPM")
    sns.lineplot(ax=ax[3], x=data["DateTime"], y=data["rpm"], color='red', label="Fan RPM")
    ax[0].xaxis.set_major_formatter(dateFormat)
    ax[3].set(ylim=(0, 5000))
    ax[3].set_xlabel("Date and Time")
    ax[3].set_ylabel("RPM")
    ax[3].legend()

    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Gilfoyle grapher')
    parser.add_argument('--from', '-f', dest='from_date', type=str, help='Start date in DD-MM-YYYY format')
    parser.add_argument('--to', '-t', dest='to_date', type=str, help='End date in DD-MM-YYYY format')
    parser.add_argument('--save', action='store_true', help='Save the report as ______')
    
    args = parser.parse_args()
    if args.from_date and args.to_date:
        from_date = datetime.datetime.strptime(args.from_date, '%d-%m-%Y').date()
        to_date = datetime.datetime.strptime(args.to_date, '%d-%m-%Y').date()
    else:
        from_date = datetime.datetime.today().date()
        to_date = datetime.datetime.today().date()

    actual_data = fetch_data(from_date, to_date)
    df_actual = convert_to_dataframe(actual_data)
    print(df_actual)
    plot_subplots_seaborn(df_actual)


if __name__ == '__main__':
    main()
