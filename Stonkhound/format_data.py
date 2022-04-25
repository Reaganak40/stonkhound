import csv
from re import L

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
        if (formatted_data[i])[1] < (formatted_data[i-1])[1]:
            (formatted_data[i])[1] = 1.0
        else:
            (formatted_data[i])[1] = 0.0
    
    # "On this date you buy because a month from now you make profit"
    formatted_data.pop(0)
    features = get_features(ticker_symbol)

    final_data = []
    for dp in formatted_data:
        year = dp[0][2]
        for fp in features:
            if fp[0] == (int)(year - 1):
                final_data.append(fp + [dp[1]])
                final_data[-1].pop(0)
                break
    for dp in final_data:
        print(dp)
    return final_data


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
    with open('./data/{}/features.csv'.format(ticker_symbol, ticker_symbol)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                dp = row[0].split()
                if(len(dp) == 1):  # if csv is incorrectly read
                    dp = dp[0].split(',')

                for f in range(len(dp)):
                    dp[f] = dp[f].strip('"')
                    if("," in dp[f]):
                        temp = ""
                        for n in dp[f]:
                            if n != ',':
                                temp += n
                        dp[f] = temp

                    if(dp[f] == "––"):
                        dp[f] = 0.0
                    else:
                        if f == 0:
                            dp[f] = int(dp[f])
                        else:
                            dp[f] = float(dp[f])
                    data.append(dp)
                line_count += 1
        return data

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

# formats data for all given companies
def create_dataset():
    create_datapoint('dp1', format_data('aapl'))
    create_datapoint('dp2', format_data('dis'))
    create_datapoint('dp3', format_data('nke'))
    create_datapoint('dp4', format_data('jnj'))
    create_datapoint('dp5', format_data('msft'))
    create_datapoint('dp6', format_data('wba'))
    create_datapoint('dp7', format_data('hmc'))
    create_datapoint('dp8', format_data('abbv'))
    create_datapoint('dp9', format_data('intc'))
    create_datapoint('dp10', format_data('mcd'))
    create_datapoint('dp11', format_data('gpc'))
    create_datapoint('dp12', format_data('xom'))
    create_datapoint('dp13', format_data('afl'))
    create_datapoint('dp14', format_data('t'))
    create_datapoint('dp15', format_data('tgt'))
    create_datapoint('dp16', format_data('hrl'))
    create_datapoint('dp17', format_data('cvx'))
    create_datapoint('dp18', format_data('nue'))
    create_datapoint('dp19', format_data('pld'))
    create_datapoint('dp20', format_data('mdt'))















