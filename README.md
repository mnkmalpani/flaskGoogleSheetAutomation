# flaskGoogleSheetAutomation

## Run it using gunicorn
### To run it locally
`gunicorn -w 3 "app:application"`
### To run it in background on a server
`nohup gunicorn -w 3 "app:application" --bind=<server-ip> > log.txt 2>&1 &`