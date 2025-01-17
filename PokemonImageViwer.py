from email.mime import image
from tkinter import *
from tkinter import ttk
from library import download_image_from_url, set_desktop_background_image
from pokeapi import get_poke_list, get_pokemon_image_url
import os 
import sys
import ctypes



def main():

    #lets us make a dir called images 
    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)  
    
    # makes the frame of the program 
    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'pokemon.image.viewer'
    ctypes.windll.shell32.setCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'pokeball.ico'))
    root.rowconfigure(0, weight=1)
    root.minsize(500, 600)

    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)

    # puts a pokeball img on the task bar for the icon 
    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0 ,padx=10, pady=10)
    
    # get the list of names of all of the pokemon in a drop down menu 
    pokemon_list = get_poke_list()
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=0, column=0 ,padx=10, pady=10)

    def handle_poke_select(event):
         """"

    Gets the image path when savesd it tags the file with png on the end of it and diabales the button for being used . 

    :parm url: gets the url from the pokeapi.py file sowe can get the img 
    :parm name: pokemons name (or poke index)
    :parm path: adds png on to the end of the file so we can open it 
    """
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

        cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)
    
    def handle_btn_set_desktop():
             """"

    Sets the background of the home screen after the button is pressed  

    :parm name: pokemons name (or poke index)
    :parm path: adds png on to the end of the file so we can open it 
    """
    
        #Button of the program lets us set the desk top background with a click of a button 
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        set_desktop_background_image(image_path)
        
        #sets decktop background after button press
        btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command= handle_btn_set_desktop)
        btn_set_desktop.state(['disabled'])
        btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)
    
    
    root.mainloop()


main()

