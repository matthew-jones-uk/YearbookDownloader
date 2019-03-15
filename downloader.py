import requests # to get pages
from bs4 import BeautifulSoup # to parse html

def get_photo_details(image_id, cookies):
    '''Get information of photo from photo page.
    Args:
        image_id (string): ID of photo to download.
        cookies (dictionary): Cookies to use, should contain session id.
    Returns:
        download_url, people (string, list): Direct image download url and list of tagged people.
    '''
    # image page url
    url = 'https://yearbook.com/s/photos/view/'+image_id
    # set timeout of 30 as website is sometimes slow
    response = requests.get(url, cookies=cookies, timeout=30)
    soup = BeautifulSoup(response.text, features='html.parser')
    # get main photo element
    element = soup.find('div', {'class': 'photo-view'})
    # get direct download url
    download_url = element.find('div', {'class': 'image-container'}).find('img')['src']
    people = list()
    try:
        # get first tagged person
        people.append(element.find('span', {'class': 'links'}).find('a').string)
        # get the rest of tagged people
        more_names = element.find('ul').find_all('a')
        for name in more_names:
            people.append(name.string)
    except AttributeError:
        # if no people are tagged
        pass
    # occasionally the direct url is something like /s/thumbnail/
    if '/s/photos/' in download_url:
        download_url = 'https://yearbook.com'+download_url
    return download_url, people

def get_raw_photo(url, cookies):
    '''Get raw photo from direct image link.
    Args:
        url (string): Direct image url.
        cookies (dictionary): Cookies to use, should contain session id.
    Returns:
        (string): Raw image from link
    '''

    response = requests.get(url, cookies=cookies, timeout=30)
    return response.content

def save_photo(raw_photo, filepath):
    '''Save raw photo to file as a jpeg.
    Args:
        raw_photo (string): The raw image to be saved.
        filepath (string): Filepath to save image to.
    '''
    # write image bytes
    with open(filepath, 'wb') as f:
        f.write(raw_photo)

def save_people(people, filepath):
    '''Save tagged people to csv.
    Args:
        people (list): List containing names of tagged people.
        filepath (string): Filepath to save image to.
    '''
    # manually form csv, probably needs to be cleaned
    with open(filepath, 'w') as f:
        for person in people:
            f.write(person+',')