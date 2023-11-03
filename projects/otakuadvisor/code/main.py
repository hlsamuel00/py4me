import requests
import re
import time
from random import choice
from selection import selectFromList
from settings import *

class Recommendations:
    def __init__(self) -> None:
        self.recommendation_reference = {}


    def get_recommendations(self):
        # Initialize the dictionary needed for the http GET params and set the order by and sorting parameters 
        http_params = {
            'order_by': 'mal_id', 
            'sort': 'asc'
            }

        # Determine the mood so we can select the genre
        user_mood = selectFromList(MOOD_DICT, "What mood are we going for?")
        http_params['genres'] = choice(MOOD_DICT[user_mood])[1]

        # Determine the type of anime to watch (TV, Movie, TV-Special, etc.)
        http_params['type'] = TYPE_DICT[selectFromList(TYPE_DICT, "What type of anime would you like?")]

        # Determine if they want a completed anime (only for tv shows)
        if http_params['type'] == 'tv':
            if BOOL_DICT[selectFromList(BOOL_DICT, "Do you want the show to be completed?")]:
                http_params['status'] = 'complete'

        # Determine if we should remove explicit recommendations
        if sfw := BOOL_DICT[selectFromList(BOOL_DICT, "Does it need to be Safe for Work?")]:
            http_params['sfw'] = 'true'

        # Determine the rating the user prefers
        if BOOL_DICT[selectFromList(BOOL_DICT, "Do you have a specific rating you'd like to view?")]:
            http_params['rating'] = RATINGS_DICT[selectFromList(RATINGS_DICT, 'What rating would you like to view?')]

        # Initialize the service_url variable for later use
        url = "https://api.jikan.moe/v4/anime"

        # Initialize the recommendations list and dictionary for quick lookup of MAL ID and Title for later use
        all_recommendations = []

        try:
            # Create variable to stop iteration
            add_info = True

            # Iterate while add_info is True. add_info is updated after each page is processed and whether there is another page of data to process
            while add_info:
                print('Gathering data...')
                # Initialize the response received from the GET request with the http parameters
                response = requests.get(url, http_params)
                
                # Convert the response received into JSON and deconstruct the pagination and data
                pagination, data = response.json().values()

                # If there are more than 17 pages of anime that fit a particular parameter, we add themes to reduce the page count below 17.
                if (total_pages := pagination['last_visible_page']) > 17:
                    print(f'We have {total_pages * 25} recommendations! Let\'s pick a genre to help narrow the search.')

                    themes = THEME_DICT if sfw else NSFW_THEME_DICT
                    theme = selectFromList(themes, 'Which genre piques your interest?')
                    theme_id = themes[theme]

                    http_params['genres'] += f',{theme}'
                    continue

                # Add the anime data received from each response to a list. 
                for anime in data:
                    if anime['duration']:
                        raw_num = re.match(r'([^\s]+)', anime['duration']).group()
                        if raw_num.isdigit():
                            duration = int(raw_num)
                            anime['duration'] = duration
                    
                    all_recommendations.append(anime)

                # If there is another page, update the page in the HTTP parameters and make another call to get the rest of the information.
                if add_info := pagination['has_next_page']:
                    http_params['page'] = pagination['current_page'] + 1

                # Timeout to prevent overloading API with requests
                time.sleep(.40)
        except:
            print('We were unable to process the request at this time; please try again at a later time.')
            print(http_params)
            print(response.url)
            print(response.raise_for_status())
            quit()


        print(f"It looks like we've got {len(all_recommendations)} anime recommendations for you!!")


        if len(all_recommendations) > 15:
            print(f"Let's take a look to see if we can narrow our recommendations a bit more!")

            episode_min, episode_max = EPISODE_DICT[selectFromList(EPISODE_DICT,'About how long would you like to binge?')]
            all_recommendations = list(filter(lambda anime: not anime['episodes'] or episode_min <= anime['episodes'] <= episode_max, all_recommendations))
            
            print(f"It looks like we're down to {len(all_recommendations)}!!")

        for anime in all_recommendations:
            self.recommendation_reference[anime['title']] = anime['mal_id']

        print(http_params)



print(get_recommendations())


