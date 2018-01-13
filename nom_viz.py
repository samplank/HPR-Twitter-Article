import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.font_manager as fm
import json
import mpld3
from mpld3 import plugins
from mpld3.utils import get_id
import collections

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

fig, ax = plt.subplots(figsize=(14,5))

# font2 = fm.FontProperties(fname='GothamHTF-Book.otf')
# hfont = {'fontname':'Helvetica'}
# fig.title('Phone Number Tweets by Name',**hfont)

# font1 = fm.FontProperties(fname='GothamHTF-Black.otf')
# font2 = fm.FontProperties(fname='GothamHTF-Book.otf')
data_path = os.chdir("PhoneNumberData4")
current = os.getcwd()
files = os.listdir(current)
# nom_list = ['Sessions','Flynn','Gorsuch','Trump']
# color_list = ['b','r']

# useful list -> ['Russia','Trumpcare','MuslimBan']

nom_list = ['Russia','Trumpcare', 'MuslimBan']
color_list = ['#435A8B','#374A72','#2B3A59']
# color_list = ['#1F2940','#435A8B','#2B3A59']
# nom_list = ['Russia','Trumpcare','MuslimBan']
alphas =[1.0,0.75, 0.5]
# alphas =[1.0,0.8,0.3]


# fig, ax = plt.subplots(figsize=(14,5))
# ax.set_title('Phone Number Tweets by Name',fontweight='bold', fontsize=20, fontproperties = font1)

for nom, color, al in zip(nom_list, color_list, alphas):
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
#     plt.plot(dates, mention_counts, color)
    ax.plot(dates, mention_counts, color, linewidth=3.0, alpha=al)
    # line_connections.append(ax.plot(dates, mention_counts, color))

# plt.legend(nom_list)
# fig.legend(nom_list)
# plt.title('Phone Number Tweets by Names')
# ax.set_title('Phone Number Tweets by Name',fontweight='bold', fontsize=20, fontproperties = font1)
legend = ax.legend(nom_list, loc='upper right', frameon=False, framealpha=0.0)
# interactive_legend = plugins.InteractiveLegendPlugin(line_connections, nom_list)
# plugins.connect(fig, interactive_legend)
# mpld3.display(plt)
data_path = os.chdir("..")
mpld3.save_html(fig, "nom_viz2.html")