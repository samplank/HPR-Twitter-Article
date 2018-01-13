import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import json
import mpld3

def nom_mentions(infile, nominee):
    ctr = 0
    with open(infile, 'r') as data_file:
        for line in data_file:
        	try:
        		json_line = json.loads(line)
        		if nominee in json_line['text']:
        			ctr += 1
        	except:
        		pass

    return(ctr)

data_path = os.chdir("PhoneNumberData3")
current = os.getcwd()
files = os.listdir(current)

# nom_list = ['Sessions','Flynn','Gorsuch','Trump']
# color_list = ['b','r']

# useful list -> ['Russia','Trumpcare','MuslimBan']

nom_list = ['Sessions','Flynn','Gorsuch','Trump']
color_list = ['b','r','g','k']

# fig = plt.axes()
for nom, color in zip(nom_list, color_list):
    mention_counts = []
    dates = []
    for n in files:
        date_string = n[11:-5]
        dt_string = dt.strptime(date_string, '%Y-%m-%d')
        dates.append(dt_string)
        mention_count = nom_mentions(n, nom)
        mention_counts.append(mention_count)
    # print(dates)
    # print(mention_counts)
    plt.plot(dates, mention_counts, color)
    # fig.plot(dates, mention_counts, color)

plt.legend(nom_list)
# fig.legend(nom_list)
plt.title('Phone Number Tweets by Names')
plt.legend(nom_list)
# fig.set_title('Phone Number Tweets by Names')
mpld3.display(plt)
# plt.show()
