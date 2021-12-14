#!/bin/bash

cd $(dirname $0)

KIVY_ENV=".kivy_env"

if [ ! -d $KIVY_ENV ] ; then
    python3 -m venv $KIVY_ENV
    source $KIVY_ENV/bin/activate
    pip3 install --upgrade pip setuptools | tail -n 1
    pip3 install -r app/mac/requirements.txt | tail -n 1
else
    source $KIVY_ENV/bin/activate
fi

cd app
python3 main.py