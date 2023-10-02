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

# Determine the type of anime to watch (TV, Movie, TV-Special, etc.)
http_params['type'] = TYPE_DICT[selectFromList(TYPE_DICT, "What type of anime would you like?")]

# Determine if they want a completed anime (only for tv shows)
if http_params['type'] == 'tv':
    if BOOL_DICT[selectFromList(BOOL_DICT, "Do you want the show to be completed?")]:
        http_params['status'] = 'complete'

# Determine if we should remove explicit recommendations
if BOOL_DICT[selectFromList(BOOL_DICT, "Does it need to be Safe for Work?")]:
    http_params['sfw'] = 'true'

# Determine the rating the user prefers
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

        # Add the anime data received from each response to a list. 
        all_recommendations += j_son['data']

        # If there is another page, update the page in the HTTP parameters and make another call to get the rest of the information.
        if add_info := pagination['has_next_page']:
            http_params['page'] = pagination['current_page'] + 1
except:
    pass


print(f"It looks like we've got {len(all_recommendations)} anime recommendations for you!!")

if len(all_recommendations) > 15:
    print(f"Let's take a look to see if we can narrow our recommendations!")

    while len(all_recommendations) > 15:
        pass
    
    print(f"It looks like we're down to {len(all_recommendations)}!!")


# recommendations_dict = dict()
# recommendations_list = []
        # for anime in j_son['data']:
        #     # title = anime['title']
        #     # malID = anime['mal_id']
        #     # recommendations_dict[title] = malID
        #     # recommendations_list.append(title)
        #     all_recommendations.append(anime)


