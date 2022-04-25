import csv

def format_data(ticker_symbol):
    data = []
    # Get date and closing cost for each year
    with open('./data/{}/{}.csv'.format(ticker_symbol, ticker_symbol)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append([get_date(row[0]), get_close(row[1])])
                line_count += 1
    
    # Get one data point per month
    formatted_data = []
    year = (data[0])[0][2]
    current_index = 0

    for point in data:
        p_year = point[0][2]
        # month change
        if p_year != year:
            formatted_data.append(data[current_index-1])
        year = p_year
        current_index += 1
    for i in range(len(formatted_data)-1, 0, -1):
        f_date = ""
        f_date += str((formatted_data[i])[0][0]) + "/"
        f_date += str((formatted_data[i])[0][1]) + "/"
        f_date += str((formatted_data[i])[0][2])
        (formatted_data[i])[0] = f_date

        if (formatted_data[i])[1] < (formatted_data[i-1])[1]:
            (formatted_data[i])[1] = 1.0
        else:
            (formatted_data[i])[1] = 0.0
    # "On this date you buy because a month from now you make profit"
    formatted_data.pop(0)
    get_features(ticker_symbol)
    return formatted_data


def get_date(date_string):
    date = []
    stripped = date_string.split("/")
    for i in range(len(stripped)):
        date.append(int(stripped[i]))
    return date

def get_close(close_string):
    stripped = close_string.strip()
    val = stripped.strip('$')
    return float(val)


def get_features(ticker_symbol):
    data = []
    # Get date and closing cost for each month
    with open('./data/{}/features.csv'.format(ticker_symbol, ticker_symbol), errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])
                print(data[-1])
                line_count += 1

def create_datapoint(dp_name, data):
    # open the file in the write mode
    f = open('data/dataset/{}.csv'.format(dp_name), 'w')

    # create the csv writer
    writer = csv.writer(f, lineterminator = '\n')

    # write a row to the csv file
    for p in data:
        writer.writerow(p)

    # close the file
    f.close()

def create_dataset():
    create_datapoint('dp1', format_data('aapl'))