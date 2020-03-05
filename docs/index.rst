.. pyramco documentation master file, created by
   sphinx-quickstart on Thu Mar  5 05:30:57 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

$pyramco
========

$A complete Python wrapper class for the RAMCO AMS API.


Make requests easier:

    import pyramco
    
    # get metadata for the Contact entity:
    
    pyramco.get_entity_metadata('Contact')


    # fetch the first and last name of the Contact with ContactID 123456:

    pyramco.get_entity('Contact', 1232456, (FirstName, LastName))


Features
--------

- Supports all RAMCO API functions
- Automatically handles streamtoken/multi-part requests
- Improved error handling and incorporated additional explanation language to errors
- Works everywhere Python does!

Installation
------------

Install $pyramco by running:

    pip install pyramco


Requires the requests module: https://pypi.org/project/requests/

Your RAMCO API key should be set as an environment variable: RAMCO_API_KEY

pyramco accesses this variable as: os.environ['RAMCO_API_KEY']

Contribute
----------

- Issue Tracker: https://github.com/mansard/pyramco/issues
- Source Code: https://github.com/mansard/pyramco

Support
-------

If you are having issues, please let me know:
pyramco@mansard.net


License
-------

The project is licensed under the MIT license.
https://github.com/mansard/pyramco/blob/master/LICENSE


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
