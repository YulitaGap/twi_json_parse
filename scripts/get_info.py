import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_requirements():
    """
    (None)->(str,str)
    Returns inputted user name and name of data needed as strings.
    """
    user_name = input('Enter user name: ')
    needed_data = input('Choose data needed:'+'\n' + 'id' + '\n' 'id_str' + '\n' + 'name' + '\n'\
                        + '\n'+'screen_name''\n'+'location'+'\n'+'description'+'\n'+'url' + '\n'\
                        + 'entities' + '\n' + 'protected' + '\n' + 'followers_count'+'\n'\
                        + 'friends_count'+'\n' + 'listed_count'+'\n' + 'created_at'+'\n'\
                        + 'favourites_count'+'\n' + 'utc_offset'+'\n' + 'time_zone'+'\n' + 'geo_enabled' + '\n'\
                        + 'verified' + '\n' + 'statuses_count'+'\n' + 'lang'+'\n' + 'status' + '\n'\
                        + 'is_translator' + '\n' + 'contributors_enabled'+'\n' + 'is_translation_enabled'+'\n'\
                        + 'profile_background_color' + '\n' + 'profile_background_image_url'+'\n' + 'profile_background_image_url_https' + '\n' \
                        + 'profile_background_tile' + '\n' + 'profile_image_url' + '\n' + 'profile_image_url_https' + '\n' \
                        + 'profile_banner_url' + '\n' + 'profile_link_color'+ '\n' + 'profile_sidebar_border_color' + '\n' + 'profile_sidebar_fill_color'+'\n'\
                        + 'profile_text_color'+'\n' + 'profile_use_background_image' + '\n' + 'has_extended_profile' + '\n'\
                        + 'default_profile'+'\n' + 'default_profile_image' +'\n'\
                        + 'following' + '\n' + 'live_following'+'\n' + 'follow_request_sent'+'\n' + 'notifications'+'\n' + 'muting'+'\n'\
                        + 'blocking' + '\n' + 'blocked_by' + '\n' + 'translator_type' + '\n'\
                        + ' Print needed data here: ')
    return user_name, needed_data


def get_users_data(account):
    """
    (str)->(dict)
    Returns dictionary with information for user friends.
    """
    if len(account) > 1:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': account, 'count': '200'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js = json.loads(data)
        return js


def get_needed_data(friend_data, requirement):
    """
    (dict,str)->(dict)
    Returns dictionary with data required by user.
    Writes this data to a new json file.
    """
    output_data = {}
    for u in friend_data['users']:
        try:
            output_data[u['screen_name']] = u[requirement]
        except KeyError:
            print('Try to look for this data in other level of file ')
    output_file = open('js_part.json', 'w')
    json.dump(output_data, output_file)
    output_file.close()
    return output_data


if __name__ == '__main__':
    inputted = get_requirements()
    friends_data = get_users_data(inputted[0])
    print(get_needed_data(friends_data, inputted[1]))
