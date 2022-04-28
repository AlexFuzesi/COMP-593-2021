""" 
COMP 593 - Final Project

Description: 
  Downloads NASA's Astronomy Picture of the Day (APOD) from a specified date
  and sets it as the desktop background image.

Usage:
  python apod_desktop.py image_dir_path [apod_date]

Parameters:
  image_dir_path = Full path of directory in which APOD image is stored
  apod_date = APOD image date (format: YYYY-MM-DD)

History:
  Date        Author    Description
  2022-04-19  Alex Fuzesi   Initial creation
"""
from pprint import pprint
import sqlite3
from unittest import result
import requests
import json
import ctypes
import os 
import sys
from sys import argv, exit
from datetime import datetime, date
from hashlib import sha256
from os import path

def main():

    # Determine the paths where files are stored
    image_dir_path = get_image_dir_path()
    db_path = path.join(image_dir_path, 'apod_images.db')

    # Get the APOD date, if specified as a parameter
    apod_date = get_apod_date()

    # Create the images database if it does not already exist
    create_image_db(db_path)

    # Get info for the APOD
    apod_info_dict = get_apod_info(apod_date)


    # Download today's APOD
    image_url = apod_info_dict['url']
    image_msg = download_apod_image(image_url)
    image_sha256 = sha256(image_msg.content).hexdigest()
    image_size = len(image_msg.content)
    image_path = get_image_path(image_url, image_dir_path)

    # Print APOD image information
    print_apod_info(image_url, image_path, image_size, image_sha256)

    # Add image to cache if not already present
    if not image_already_in_db(db_path, image_sha256):
        save_image_file(image_msg, image_path)
        add_image_to_db(db_path, image_path, image_size, image_sha256)

    # Set the desktop background image to the selected APOD
    set_desktop_background_image(image_path)

def get_image_dir_path():
    """
    Validates the command line parameter that specifies the path
    in which all downloaded images are saved locally.

    :returns: Path of directory in which images are saved locally
    """
    if len(argv) >= 2:
        dir_path = argv[1]
        if path.isdir(dir_path):
            print("Images directory:", dir_path)
            return dir_path
        else:
            print('Error: Non-existent directory', dir_path)
            exit('Script execution aborted')
    else:
        print('Error: Missing path parameter.')
        exit('Script execution aborted')

def get_apod_date():
    """
    Validates the command line parameter that specifies the APOD date.
    Aborts script execution if date format is invalid.

    :returns: APOD date as a string in 'YYYY-MM-DD' format
    """    
    if len(argv) >= 3:
        # Date parameter has been provided, so get it
        apod_date = argv[2]

        # Validate the date parameter format
        try:
            datetime.strptime(apod_date, '%Y-%m-%d')
        except ValueError:
            print('Error: Incorrect date format; Should be YYYY-MM-DD')
            exit('Script execution aborted')
    else:
        # No date parameter has been provided, so use today's date
        apod_date = date.today().isoformat()
    
    print("APOD date:", apod_date)
    return apod_date

def get_image_path(image_url, dir_path):
    """
    Determines the path at which an image downloaded from
    a specified URL is saved locally.

    :param image_url: URL of image
    :param dir_path: Path of directory in which image is saved locally
    :returns: Path at which image is saved locally
    """
    dir_path = sys.path[0]
    image_dir = os.path.join(dir_path, 'images file')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)  

    if response.status_code == 200:
        with open('image_name.jpg', 'wb') as file:
            file.write(response.content)
        print('success')
    else:
        print('failed. Response code:', response.status_code)
    
    image_url = download_apod_image(image_url)
    image_path = os.path.join(image_dir, image_url + '.png')
    return "TODO"

def get_apod_info(date):
    """
    Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    :param date: APOD date formatted as YYYY-MM-DD
    :returns: Dictionary of APOD info
    """ 
    NASA_api_key = '8gh92IXYh5XJNwEMevt8TBecUwT7ZkT1jLECussK'  
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    apod_prams ={'api_key': NASA_api_key, 'date' : date}
    response = requests.get(URL_APOD, params= apod_info_dict)
    if response.status_code == 200:
        print('success')
        apod_info_dict = respones.json()
        return [p['date']for p in apod_info_dict['today']]
    else:
        print('failed. Response code:', response.status_code)
    return {"api_key": NASA_api_key}

def print_apod_info(image_url, image_path, image_size, image_sha256):
    """
    Prints information about the APOD

    :param image_url: URL of image
    :param image_path: Path of the image file saved locally
    :param image_size: Size of image in bytes
    :param image_sha256: SHA-256 of image
    :returns: None
    """   
    print("The url of the APOD file is: " + image_url)
    print("The path of the image file is: " + image_path)
    print("The size of the image file is: " + image_size)
    print("The SHA-256 of the image is: " + image_sha256)
    return #TODO

def download_apod_image(image_url):
    """
    Downloads an image from a specified URL.

    :param image_url: URL of image
    :returns: Response message that contains image data
    """
    print(R"Downloading imgaefrom URL...", end='')
    response = requests.get(image_url)

    if response.status_code == 200:
        with open('image_name.jpg', 'wb') as file:
            file.write(response.content)
        print('success')
    else:
        print('failed. Response code:', response.status_code)


    return "TODO"

def save_image_file(image_msg, image_path):
    """
    Extracts an image file from an HTTP response message
    and saves the image file to disk.

    :param image_msg: HTTP response message
    :param image_path: Path to save image file
    :returns: None
    """
    api_key = "8gh92IXYh5XJNwEMevt8TBecUwT7ZkT1jLECussK"
    
    image_url = "https://api.nasa.gov/planetary/apod?api_key=" + str(api_key)
    
    if response.status_code == 200:
        print('success')
        return respones.json()    
    else:
        print('failed. Response code:', response.status_code)
    return #TODO

def create_image_db(db_path):
    """
    Creates an image database if it doesn't already exist.

    :param db_path: Path of .db file
    :returns: None
    """
    #connect to db_path at the top 
    myConnection = sqlite3.connect(db_path)
    myCursor = myConnection.cursor()

    apodCreatTable = """ CREATE TABLE IF NOT EXISTS apod_image(
                           id integer PRIMARY KEY,
                           path text NOT NULL,
                           sha256 text NOT NULL,
                           size integer NOT NULL,
                           downloaded_at datetime NOT NULL
                         );"""
    myCursor.execute(apodCreatTable)
    myCursor.commit()
    myCursor.close()

    return #TODO

def add_image_to_db(db_path, image_path, image_size, image_sha256):
    """
    Adds a specified APOD image to the DB.

    :param db_path: Path of .db file
    :param image_path: Path of the image file saved locally
    :param image_size: Size of image in bytes
    :param image_sha256: SHA-256 of image
    :returns: None
    """
    myConnection = sqlite3.connect(db_path)
    myCursor = myConnection.cursor()

    addImageQuery = """INSERT INTO apod_image (Path,
                         FileSize,
                         SHA-256,
                         DateDownloaded)
                    VALUSE (?, ?, ?, ?);"""

    Imagedownloaded = (image_path,
                       image_size,
                       image_sha256,
                       datetime.now())
                       
    myCursor.execute(addImageQuery, Imagedownloaded)

    myCursor.commit()
    myCursor.close()

                       
    return #TODO

def image_already_in_db(db_path, image_sha256):
    """
    Determines whether the image in a response message is already present
    in the DB by comparing its SHA-256 to those in the DB.

    :param db_path: Path of .db file
    :param image_sha256: SHA-256 of image
    :returns: True if image is already in DB; False otherwise
    """ 
    myConnection = sqlite3.connect(db_path)
    myCursor = myConnection.cursor()

    selectStatement = """SELECT SHA-256 FROM Image
                         WHERE image_sha256 == SHA-256;"""


    myCursor.execute(selectStatement)
    results = myCursor.fetchall()
    pprint(results)

    myConnection.close


    return True #TODO

def set_desktop_background_image(image_path, image_dir):
    """
    Changes the desktop wallpaper to a specific image.

    :param image_path: Path of image file
    :returns: None
    """
    ctypes.windll.user32.SystemParameterInfoW(20, 0, image_path, 0)
    image_path = os.path.join(image_dir, image_path + '.png')
    set_desktop_background_image(image_path)

    return #TODO

main()