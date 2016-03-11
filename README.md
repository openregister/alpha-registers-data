# Registry register data

The data for the
[registry register](http://registry.openregister.org),
[register register](http://register.openregister.org),
[field register](http://field.openregister.org)
and
[datatype register](http://datatype.openregister.org)
is currently maintained as individual yaml files in the [data](data/) directory.

# Testing

[![Build Status](https://travis-ci.org/openregister/registry-data.svg?branch=master)](https://travis-ci.org/openregister/registry-data)

The shape of the registers and links between the data can be tested by running `make`
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 registry-data
    $ workon registry-data
    $ make init

    $ make
