import requests # to get pages
from bs4 import BeautifulSoup # for html parsing

def get_photo_ids(cookies, perPage=1000000):
    '''Go to the main recent image page and ask for certain amount of images.
    Args:
        cookies (dictionary): Cookies to use, should contain session id.
        perPage (int, optional): Defaults to 1000000. Amount of images to get, defaults to a high
                                 value so that hopefully all images are automatically found.
    Returns:
        ids (list): List of image ids.
    '''
    # parameters for api search query
    params = (
        ('orderBy', 'date'),
        ('orderDir', 'desc'),
        ('page', '1'),
        ('perPage', perPage),
    )
    # set timeout of 30 as website is sometimes slow
    response = requests.get('https://yearbook.com/s/photos/', params=params, cookies=cookies, timeout=30)
    # parse html
    soup = BeautifulSoup(response.text, features='html.parser')
    # elements from search response containing image ids
    elements = soup.find_all('div', {'data-photo-id': True})
    ids = list()
    for element in elements:
        # get image id from each element
        ids.append(element['data-photo-id'])
    return ids
