# -*- coding: utf-8 -*-

import os
from os.path import join


def get_image_path():
        for root, dirs, files in os.walk('/home/dean/Desktop/Django_apps/Django_Proj/myapp/login/static/images'):
            #debug information, just to get an idea how walk works.
            #currently we are traversing over all files with any extension
          #  print "Current directory:", root
           # print "Sub directories:", dirs
            #print "Files:", files

            for file in files:
               # if file.startswith(self.title):
                #now we have found the desired file.
                #value of file: "myimagetitle.jpg" <-- no path info
                #value of root: "/home/yourhome/gallery/static/images/myalbum"
                #we want to use this information to create a url based on our static path, so we need only the path sections past "static"
                #we can achieve this like so (just one way)
                mypath = os.sep.join(os.path.join(root, file).split(os.sep)[4:])

                #yields: /images/myalbum/myimagetitle.jpg


                print(mypath)
               # return mypath


get_image_path()
