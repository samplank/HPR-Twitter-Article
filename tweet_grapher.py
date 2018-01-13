from pysmap import SmappCollection
import networkx as nx
from pysmap import networks
import io
import shutil

collection = SmappCollection('json', 'PhoneNumberData4/phoneTweets2017-05-03.json')
tweet_fields = ['id_str', 'retweeted_status.id_str', 'timestamp', 'text', 'lang']
user_fields = ['id_str', 'screen_name', 'location', 'description']
digraph = networks.retweet_network(collection, tweet_fields, user_fields)
nx.write_graphml(digraph, 'collection_retweets5_3.graphml')
