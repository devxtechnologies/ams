# Attendance Management System


This application represents attendance management system.

## Setup


1. [Local Environment Setup](#local-environment-setup)
2. [Runnig The Application](#running-the-application)
3. [Changelog](#changelog)

## Local environment setup

### Create a virtual environment


1. `virtualenv <env_name>`
2. `source <env_name>/bin/activate`
3. `deactivate` to deactivate.

### Install requirements


1. `pip install -r requirements.txt`

## Running the application


1. Activate the environment `source <env_name>/bin/activate`
2. Start the application `python manage.py runserver`

## CHANGELOG

### 1.1 - 07/AUG/2018

#### Added
* Favicon added
* Bug Fixes
* Login page errors
* Login/Logout URLs


### 1.0 - 07/AUG/2018

#### Added
* Color inversion toggle switch
* LocalStorage
* Moved to BitBucket
* Select all button in attendance main


### 1.1 (Beta) - 07/AUG/2018

#### Added
* Department model
* Main JS file

#### Changed
* User Model
* Teaches Model
* Minor UI

### 1.0 (Beta) - 26/JULY/2018

#### Added
* Account Registration
* Attendance Entry (Subject selection)
* Attendance Main
* SMS mixin
* Dashboard UI
