import csv
from re import L
import random
import numpy as np

# ======================================================================
# Function: format_data
# Date Modified: 4/26/2022
# Details: given a ticker_symbol stock, goes to folder that contains the 
# hisotrical data and condenses it to a datapoint
# ======================================================================
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

# ======================================================================
# Function: get_date
# Date Modified: 4/26/2022
# Details: Returns a 3-index array specifying date
# ======================================================================
def get_date(date_string):
    date = []
    stripped = date_string.split("/")
    for i in range(len(stripped)):
        date.append(int(stripped[i]))
    return date
# ======================================================================
# Function: get_close
# Date Modified: 4/26/2022
# Details: removes string parts of price to return float value
# ======================================================================
def get_close(close_string):
    stripped = close_string.strip()
    val = stripped.strip('$')
    return float(val)

# ======================================================================
# Function: get_features
# Date Modified: 4/26/2022
# Details: uses stock evaluation data to build array for features 
# of datapoint
# ======================================================================
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
                    dp = strip_between(dp[0], '"', ',')
                    dp = dp.split(',')


                for f in range(len(dp)):
                    dp[f] = dp[f].strip('"')
                    if("," in dp[f]):
                        temp = ""
                        for n in dp[f]:
                            if n != ',':
                                temp += n
                        dp[f] = temp

                    if(dp[f] == "––"):
                        dp[f] = np.NaN
                    else:
                        if f == 0:
                            dp[f] = int(dp[f])
                        else:
                            dp[f] = float(dp[f])
                    data.append(dp)
                line_count += 1
        return data

# ======================================================================
# Function: create_datapoint
# Date Modified: 4/26/2022
# Details: returns a full datapoint and writes dp to a csv
# ======================================================================
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
    return data

# ======================================================================
# Function: strip_between
# Date Modified: 4/26/2022
# Details: removes all refrences of char between given dilemeters
# ======================================================================
def strip_between(old_string, between, remove):
    nstr = ""
    temp_str = ""
    in_bound = False

    for c in old_string:
        if in_bound:
            if(c == between):
                temp_str = temp_str.replace(remove, "")
                temp_str += c
                nstr += temp_str
                in_bound = False
            else:
                temp_str += c
        else:
            nstr += c
            if(c == between):
                in_bound = True
                temp_str = ""
    return nstr


# ======================================================================
# Function: create_dataset
# Date Modified: 4/26/2022
# Details: creates a stock dataset build from historical data, where the 
# features include evaluation data, and labels identify if the price of 
# the stock will increase in a year
# ======================================================================
def create_dataset():
    dataset = []
    dataset += create_datapoint('dp1', format_data('aapl'))
    dataset += create_datapoint('dp2', format_data('dis'))
    dataset += create_datapoint('dp3', format_data('nke'))
    dataset += create_datapoint('dp4', format_data('jnj'))
    dataset += create_datapoint('dp5', format_data('msft'))
    dataset += create_datapoint('dp6', format_data('wba'))
    dataset += create_datapoint('dp7', format_data('hmc'))
    dataset += create_datapoint('dp8', format_data('abbv'))
    dataset += create_datapoint('dp9', format_data('intc'))
    dataset += create_datapoint('dp10', format_data('mcd'))
    dataset += create_datapoint('dp11', format_data('gpc'))
    dataset += create_datapoint('dp12', format_data('xom'))
    dataset += create_datapoint('dp13', format_data('afl'))
    dataset += create_datapoint('dp14', format_data('t'))
    dataset += create_datapoint('dp15', format_data('tgt'))
    dataset += create_datapoint('dp16', format_data('hrl'))
    dataset += create_datapoint('dp17', format_data('cvx'))
    dataset += create_datapoint('dp18', format_data('nue'))
    dataset += create_datapoint('dp19', format_data('pld'))
    dataset += create_datapoint('dp20', format_data('mdt'))
    dataset += create_datapoint('dp21', format_data('sbux'))
    dataset += create_datapoint('dp22', format_data('twtr'))
    dataset += create_datapoint('dp23', format_data('baba'))



    for d in dataset:
        print(d)
    
    # open the file in the write mode
    f = open('data/dataset/dataset.csv', 'w')

    # create the csv writer
    writer = csv.writer(f, lineterminator = '\n')

    # write a row to the csv file
    for dp in dataset:
        writer.writerow(dp)

    # close the file
    f.close()
    return dataset

# ======================================================================
# Function: get_dataset
# Date Modified: 5/1/2022
# Modified Details: Added sampling methods
# Details: returns a stock dataset build from historical data, where the 
# features include evaluation data, and labels identify if the price of 
# the stock will increase in a year
# ======================================================================
def get_dataset(sampling = "normal", impute="mean"):
    data = []
    # Get date and closing cost for each month
    with open('./data/dataset/dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            dp = row[0].split(",")
            for i in range(len(dp)):
                if(dp[i] == 'nan'):
                    dp[i] = np.NaN
                else:
                    dp[i] = float(dp[i])
            data.append(dp)
    impute_features = []
    for i in range(len(data[0])-1): # for each feature
        total = 0
        count = 0
        for dp in data:
            if(not np.isnan(dp[i])):
                if(impute == 'mean'):
                    total += dp[i]
                    count += 1
        if(impute == 'mean'):
            impute_features.append((total * 1.0) / count)
    
    # get rid of all nan data (imputation)
    for i in range(len(data)):
        for g in range(len(data[0])-1):
            if(np.isnan(data[i][g])):
                data[i][g] = impute_features[g]
    
    if(sampling == "undersampling"):
        n_1 = 0
        n_0 = 0
        type_min = 0
        remove_count = 0

        for dp in data:
            if(dp[-1] == 1.0):
                n_1 += 1
            elif(dp[-1] == 0.0):
                n_0 += 1
            else:
                print("faulty data!")
        if(n_1 > n_0):
            remove_count = n_1 - n_0
            type_min = 1.0
        else:
            remove_count = n_0 - n_1
            type_min = 0.0
        for i in range(remove_count):
            for g in range(len(data)):
                if data[g][-1] == type_min:
                    data.pop(g)
                    break
    if(sampling == "oversampling"):
        n_1 = 0
        n_0 = 0
        add_type = 0
        add_count = 0
        min_data = []

        for dp in data:
            if(dp[-1] == 1.0):
                n_1 += 1
            elif(dp[-1] == 0.0):
                n_0 += 1
            else:
                print("faulty data!")
        if(n_1 > n_0):
            add_count = n_1 - n_0
            add_type = 0.0
        else:
            add_count = n_0 - n_1
            add_type = 1.0
        # get all minority data points for oversampling
        for dp in data:
            if dp[-1] == add_type:
                min_data.append(dp)
        # add minority data until equals majority data
        for i in range(add_count):
            prev_dupe = [] # THIS IS NEEDED TO PREVENT MEMEORY DUPLICATION (BECAUSE PYTHON IS FOOKIN STUPID)
            dp = min_data[random.randint(0, len(min_data)-1)]
            for p in dp:
                prev_dupe.append(p)
            data.append(prev_dupe)
    return data















