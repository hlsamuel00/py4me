import urllib.request, urllib.parse
import json
from random import choice
from selection import selectFromList
from settings import *

# Initialize the dictionary needed for the http GET params
http_params = dict()
http_params['order_by'] = 'mal_id'
http_params['sort'] = 'asc'

# Determine the mood so we can select the genre
http_params['genres'] = choice(MOOD_DICT[selectFromList(MOOD_DICT, "What mood are we going for?")])[1]

# Determine if we should remove explicit recommendations
if BOOL_DICT[selectFromList(BOOL_DICT, "Does it need to be Safe for Work?")]:
    http_params['sfw'] = 'true'

# Determine the type of anime to watch
http_params['type'] = TYPE_DICT[selectFromList(TYPE_DICT, "What type of anime would you like?")]

# Determine if they want it still airing or complete (only for tv shows)
if http_params['type'] == 'tv':
    if BOOL_DICT[selectFromList(BOOL_DICT, "Do you want the show to be completed?")]:
        http_params['status'] = 'complete'

# Determine the rating the user prefers:
if BOOL_DICT[selectFromList(BOOL_DICT, "Do you have a specific rating you'd like to view?")]:
    http_params['rating'] = RATINGS_DICT[selectFromList(RATINGS_DICT, 'What rating would you like to view?')]

# Initialize the service_url variable for later use
service_url = "https://api.jikan.moe/v4/anime"

# Initialize the recommendations list and dictionary for quick lookup of MAL ID and Title for later use
all_recommendations = []

try:
    # Create variable to stop iteration
    add_info = True

    # Iterate while add_info is True. add_info is updated after each page is processed and whether there is another page of data to process
    while add_info:
        # Convert the url into a usable string for making the http request    
        url = f"{service_url}?{urllib.parse.urlencode(http_params)}" # -> max per page is 25

        # Initialize the data received from the response from the request and convert it to JSON
        response = urllib.request.urlopen(url).read().decode()
        j_son = json.loads(response)
        pagination = j_son['pagination']

        # Iterate through each anime received and add the title and specific ID to a dictionary for quicker reference, and the anime title to a list to prevent iterating through the dictionary twice. 
        all_recommendations += j_son['data']

        if add_info := pagination['has_next_page']:
            http_params['page'] = pagination['current_page'] + 1

except:
    pass

    
if len(all_recommendations) <= 15:
    print(f"It looks like we've got less than 15 recommended anime options for you!! How exciting!!")
else:
    print(f"It looks like we've got {len(all_recommendations)} recommendations, let's take a look to see if we can narrow our search!")

    while len(all_recommendations) > 15:
        pass


# recommendations_dict = dict()
# recommendations_list = []
        # for anime in j_son['data']:
        #     # title = anime['title']
        #     # malID = anime['mal_id']
        #     # recommendations_dict[title] = malID
        #     # recommendations_list.append(title)
        #     all_recommendations.append(anime)


