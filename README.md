HW2-Stat157
===========

This is the repository shared by Tay, Disi, and Hong for Homework 2 within the class Stat 157, Fall 2013

===========

#Before you run the notebook

Before you run ipython notebook, you must install&update packages.
This can be done by following command after you command vagrant ssh.

    sudo pip install python-dateutil --upgrade
    sudo easy_install --upgrade pytz
    sudo apt-get build-dep python-lxml
    sudo easy_install --upgrade scipy
    sudo easy_install --upgrade matplotlib
    sudo easy_install --upgrade statsmodels
    sudo apt-get install libgeos-3.3.3 python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-mpltoolkits.basemap-doc
    
Then run the notebook from your machine with this command:

    ipython notebook --no-browser --ip=0.0.0.0 --script --pylab=inline
