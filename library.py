import requests
import ctypes

def set_desktop_background_image(image_path):
     """"
     Sets the desk top background 

    :parm ctypes: sets the background setting the windll system parameter info
      
    """
    #this is how we sewt the desktop background
    ctypes.windll.user32.SystemParameterInfoW(20, 0, image_path, 0)


def download_image_from_url(image_url, save_path):
     """"

    Gets gets the image from the url opens the file and saves it

    :parm response: used to get the reposnes from the image_url
    :parm file: used to the save the image to disk 
    :returns
    """
    print("Downloading image from url...", end='')

    response = requests.get(image_url)

    if response.status_code == 200:
        with open('image_name.jpg', 'wb') as file:
            file.write(response.content)
        print('success')
    else:
        print('failed. Response code:', response.status_code)



