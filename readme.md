Running app locally by cloning repo

Step one - clone repository from github.
Step two - pip install flask.
Step three - create a database (recommened naming it veterinary_db or similar).
Step four - type 'psql -d (your-database-name) -f veterinary_db.sql' into the terminal. Make sure to use the name of the database you created.
Step five - type 'flask run'. If this command doesn't work try 'python3 -m flask run'.
Step six - the web-app will now be running locally using port 5000. Clicking the link created in the terminal will open the relevent page.
Step seven - enjoy and admire.

![HomePage](site_images/home_page.png)
![Pets](site_images/pets.png)
![Edit pet](site_images/edit_pet.png)
![Add pet](site_images/add_pet.png)