from idGetter import get_photo_ids
from downloader import get_photo_details, get_raw_photo, save_photo, save_people
from tqdm import tqdm
from os import listdir, chdir
from os.path import splitext

PHOTO_DIRECTORY = 'photos/'

# automatically move to photo directory
chdir(PHOTO_DIRECTORY)
# PHP session id that should be obtained from your login. They last a long time.
cookies = {
    'PHPSESSID': '',
}
# get all photo ids
ids = get_photo_ids(cookies)
print('Got', len(ids), 'ids')
downloaded_ids_extensions = listdir()
downloaded_ids = list()
# get ids that are already downloaded
for downloaded in downloaded_ids_extensions:
    downloaded_ids.append(splitext(downloaded)[0])
# iterate through each image id
for image_id in tqdm(ids):
    if image_id not in downloaded_ids:
        try:
            # get photo id details
            download_url, people = get_photo_details(image_id, cookies)
            # download raw image
            raw_image = get_raw_photo(download_url, cookies)
        except:
            print('Error with', image_id)
            # do not crash if error obtaining raw image or image details, instead skip.
            continue
        # save raw image and tagged people
        save_photo(raw_image, str(image_id+'.jpeg'))
        save_people(people, str(image_id+'.csv'))