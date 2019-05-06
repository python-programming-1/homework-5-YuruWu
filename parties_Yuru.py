import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    del bar_list[0]
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)



def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough= {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}
    # write code here to find the noisiest city and borough and their respective metrics

    city_call={} #count number of calls for every city
    borough_call={} #count number of calls for every borough
    for bar_dict in data:

        city_call.setdefault(bar_dict['city'], 0)  
        city_call[bar_dict['city']] = int(bar_dict['num_calls']) + city_call[bar_dict['city']] 
        borough_call.setdefault(bar_dict['borough'], 0)  
        borough_call[bar_dict['borough']] = int(bar_dict['num_calls']) + borough_call[bar_dict['borough']]        

   
    current_city = None
    current_borough=None
    current_max_city=0
    current_max_borough=0
    for key,value in city_call.items():
        if value > current_max_city:
            current_max_city = value
            current_city=key
    for k,v in borough_call.items():
        if v > current_max_borough:
            current_max_borough = v
            current_borough=k
    noisiest_city_and_borough['city']=current_city
    noisiest_city_and_borough['borough']=current_borough
    noisiest_city_and_borough['num_city_calls']=current_max_city
    noisiest_city_and_borough['num_borough_calls']=current_max_borough

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics
    city_call={} #count number of calls for every city
    borough_call={} #count number of calls for every borough
    for bar_dict in data:

        city_call.setdefault(bar_dict['city'], 0)  
        city_call[bar_dict['city']] += int(bar_dict['num_calls'])
    
        borough_call.setdefault(bar_dict['borough'], 0)  
        borough_call[bar_dict['borough']] += int(bar_dict['num_calls'])
   
    current_city = None
    current_borough=None
    current_min_city=float('Inf')
    current_min_borough=float('Inf')
    for key,value in city_call.items():
        if value < current_min_city:
            current_min_city = value
            current_city=key
    for key,value in borough_call.items():
        if value < current_min_borough:
            current_min_borough = value
            current_borough=key
    quietest_city_and_borough['city']=current_city
    quietest_city_and_borough['borough']=current_borough
    quietest_city_and_borough['num_city_calls']=current_min_city
    quietest_city_and_borough['num_borough_calls']=current_min_borough
    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
