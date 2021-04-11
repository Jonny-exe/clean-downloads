# clean-downloads
This is a program to clean up your downloads directory by creating subdirs and 
moving every file which is created to an apropiated subdir depending on its extension.

For example a .pdf file will go to a docs folder and a .png will go to a media folder.
If an file extension is unknown it will go to a misc folder.

This has a single depency which can be installed by executing the following command.
`pip install -r requirements.txt`

To run this by default and in the background every time you boot your pc you can add this line
to your cronjobs `@reboot /the/path/to/the/file/main.py` by doing `crontab -e` and adding the line.

