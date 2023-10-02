# Choice Settings:
#-------------------------
# Option Dictionaries
MOOD_DICT: dict[str,list[tuple[str,str]]] = {
             'happy': 
                   [('Comedy', '4'), ('Fantasy', '10'), ('Slice of Life', '36')], 
             'sad/emotional': 
                    [('Drama', '8'), ('Boys Love', '28'), ('Girls Love', '26')], 
             'adventurous': 
                    [('Action', '1'), ('Adventure', '2'), ('Sports', '30'), ('Sci-Fi', '24')],
             'chill': 
                    [('Slice of Life', '36'), ('Gourmet', '47')],
             'curious/intellectual': 
                    [('Mystery', '7'), ('Supernatural', '37'), ('Suspense', '41'), ('Sci-Fi', '24')],
             'romantic': 
                    [('Romance', '22'), ('Boys Love', '28'), ('Girls Love', '26')],
             'scared/suspenseful': 
                    [('Horror', '14'), ('Suspense', '41')],
             'action-packed': 
                    [('Action', '1'), ('Sports', '30')],
             'inspirational': 
                    [('Award Winning', '46'), ('Sports', '30'), ('Sci-Fi', '24')],
             'a little weird':
                    [('Avant Garde', '5'), ('Fantasy', '10'), ('Supernatural', '37')],
             'you choose':
                    [('Action', '1'), ('Adventure', '2'), ('Avant Garde', '5'), ('Award Winning', '46'), ('Boys Love', '28'), ('Comedy', '4'), ('Drama', '8'), ('Fantasy', '10'), ('Girls Love', '26'), ('Gourmet', '47'), ('Horror', '14'), ('Mystery', '7'), ('Romance', '22'), ('Sci-Fi', '24'), ('Slice of Life', '36'), ('Sports', '30'), ('Supernatural', '37'), ('Suspense', '41')]
            }

TYPE_DICT: dict[str, str] = {
             'tv show': 'tv',
             'tv special': 'special',
             'movie': 'movie',
             'direct-to-video anime': 'ova',
             'web anime': 'ona',
             'you choose': 'random'
            }

STATUS_DICT: dict[str, str] = { 
             'completed': 'complete', 
             'still airing': 'airing',
             'you choose': 'random'
            }

RATINGS_DICT: dict[str, str] = {
    'G - All Ages': 'g', 
    'PG - Children': 'pg',
    'PG-13 - Teens 13 or older': 'pg13',
    'R - 17+ (violence & profanity)': 'r17',
    'R+ - Mild Nudity': 'r',
    'Rx - Hentai': 'rx'
}

BOOL_DICT: dict[str, str] = {
    'yes': True,
    'not necessarily': False
}








#==============================================================================================================
# Genres
# Action, Adventure, Avant Garde, Award Winning, Boys Love, Comedy, Drama, Fantasy, Girls Love, Gourmet, Horror, Mystery, Romance, Sci-Fi , Slice of Life, Sports, Supernatural, Suspense

# Genre Dictionary:
# genre_dict = {
#               'Action': '1', 'Adventure': '2', 'Avant Garde': '5', 'Award Winning': '46', 'Boys Love': '28', 
#               'Comedy': '4', 'Drama': '8', 'Fantasy': '10', 'Girls Love': '26', 'Gourmet': '47', 
#               'Horror': '14', 'Mystery': '7', 'Romance': '22', 'Sci-Fi': '24', 'Slice of Life': '36', 
#               'Sports': '30', 'Supernatural': '37', 'Suspense': '41'
#               }


# Themes
# Adult Cast, Anthropomorphic, CGDCT, Childcare , Combat Sports , Crossdressing , Delinquents , Detective, Educational, Gag Humor, Gore, Harem, High Stakes Game , Historical, Idols(Female), Idols(Male), Isekai, Iyashikei, Love Polygon , Magical Sex Shift , Mahou Shoujo, Martial Arts, Mecha, Medical , Military, Music, Mythology, Organized Crime , Otaku Culture , Parody, Performing Arts, Pets , Psychological, Racing, Reincarnation, Reverse Harem , Romantic Subtext , Samurai, School, Showbiz , Space, Strategy Game, Super Power, Survival , Team Sports, Time Travel, Vampire, Video Game, Visual Arts , Workplace

# Theme Dictionary
# theme_dict = {
#               'Ecchi': '9', 'Erotica': '49', 'Hentai': '12', 'Adult Cast': '50', 'Anthropomorphic': '51', 
#               'CGDCT': '52', 'Childcare': '53', 'Combat Sports': '54', 'Crossdressing': '81', 
#               'Delinquents': '55', 'Detective': '39', 'Educational': '56', 'Gag Humor': '57', 'Gore': '58', 
#               'Harem': '35', 'High Stakes Game': '59', 'Historical': '13', 'Idols (Female)': '60', 
#               'Idols(Male)': '61', 'Isekai': '62', 'Iyashikei': '63', 'Love Polygon': '64', 
#               'Magical Sex Shift': '65', 'Mahou Shoujo': '66', 'Martial Arts': '17', 'Mecha': '18', 
#               'Medical': '67', 'Military': '38', 'Music': '19', 'Mythology': '6', 'Organized Crime': '68', 
#               'Otaku Culture': '69', 'Parody': '20', 'Performing Arts': '70', 'Pets': '71', 
#               'Psychological': '40', 'Racing': '3', 'Reincarnation': '72', 'Reverse Harem': '73', 
#               'Romantic Subtext': '74', 'Samurai': '21', 'School': '23', 'Showbiz': '75', 'Space': '29', 
#               'Strategy Game': '11', 'Super Power': '31', 'Survival': '76', 'Team Sports': '77', 
#               'Time Travel': '78', 'Vampire': '32', 'Video Game': '79', 'Visual Arts': '80', 
#               'Workplace': '48', 'Josei': '43', 'Kids': '15', 'Seinen': '42', 'Shoujo': '25', 'Shounen': '27'
#               }