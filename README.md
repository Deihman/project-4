# UOCIS322 - Project 4 #

Author:     Calvin Stewart

Contact:    clownvant@icloud.com
        or
            cstewar2@uoregon.edu

## Overview ##

A reimplementation of RUSA ACP controle time calculator with Flask and AJAX. 

When running, it will load a page mimicking the RUSA's ACP controle time calculator, but better. Choose a brevet distance and a date and time, then input the checkpoint distance in miles or km into the appropriate box. The backend `flask_brevets.py` will then grab the input data using Flask and return the output data as a JSON object through AJAX. The page will dynamically load the appropriate open and close times for each checkpoint you specify.

## How to run ##

In the `./brevets` directory, use the following command to build the image, replacing `myimage` with your preferred image name. This will build the image using resources in the `./brevets` directory.

```
docker build -f Dockerfile -t myimage .
```

To run the image, use the following command, replacing `myimage` with your image's name. The -p option forwards the docker's internal port `5000` to localhost's port `5001`. Replace the localhost port as needed to avoid conflict.

```
docker run -p 5001:5000 myimage
```

To see the webpage, open up a browser and go to `localhost:5001` replacing `5001` with your chosen port. 
