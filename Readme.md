1. Chnage the url in the templates/upload.html file in line 3 to "https://cheque-price.herokuapp.com/uploader"

2. make the main.py ready

3. make the Procfile ready

4. Make the requirements.txt by switching to virtual env - !virtualenv env or 
virtualenv env

5. upload the project to github

6. deploy on herokuapp.com
https://stackoverflow.com/questions/49469764/how-to-use-opencv-with-heroku


a. In heroku dashboard,
    goto your-app --> settings --> buildpacks --> add buildpacks --> https://github.com/heroku/heroku-buildpack-apt.git
    copy and paste this link --> add buildpack


b.1 Add an Aptfile in your project directory and add the below file

    libsm6
    libxrender1
    libfontconfig1
    libice6

    NOTE: Aptfile should not have any .txt or any other extension. Just like the Procfile

----------------------OR-------------------

b.2 in newer versions of OpenCV, you need only to list python3-opencv on the Aptfile, as seen in the docs.
    Hence, to get the latest ones, you just need python3-opencv in the Aptfile instead of the other libraries.

    python3-opencv