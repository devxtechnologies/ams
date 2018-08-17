# Attendance Management System

This application represents attendance management system.

## Setup

1.  [Local Environment Setup](#local-environment-setup)
2.  [Runnig The Application](#running-the-application)
3.  [Apps](#apps)
4.  [Change Log](#change-log)

### Local environment setup

#### Create a virtual environment

1.  `virtualenv <env_name>`
2.  `source <env_name>/bin/activate`
3.  `deactivate` to deactivate.

#### Install requirements

1.  `pip install -r requirements.txt`

### Running the application

1.  Activate the environment `source <env_name>/bin/activate`
2.  Start the application `python manage.py runserver`
3.  Go to [localhost:8000/](localhost:8000)

### Apps

1.  [Main](#main)
2.  [Dashboard](#dashboard)

#### Main

1.  [InitialView](initialview)
2.  [AttendanceView](attendanceview)

##### InitialView (/attendance)

This view initialises the list of subjects available for the user and accepts the name of the subject that the attendance is being given for.

URL: [localhost:8000/attendance/](localhost:8000/attendance/)

##### AttendanceView (/attendance/entry)

This view lists the students for the selected subject and accepts the absentee list for that particular subject fot that particular hour.

URL: [localhost:8000/attendance/entry/](localhost:8000/attendance/entry/)

#### Dashboard

1.  [DashboardView](dashboardview)
2.  [LogView](logview)
3.  [ReportView](reportview)

##### DashboardView (/dashboard)

This view is the initial landing page of the dashboard. Some attendance statistics are displayed in this page along with some quick links.

URL: [localhost:8000/dashboard/](localhost:8000/dashboard/)

##### LogView (/dashboard/log)

This view initializes the list of subjects available for the user and accepts the name of the subject that the attendance is being given for.

URL: [localhost:8000/dashboard/log/](localhost:8000/dashboard/log/)

##### ReportView (/dashboard/report)

This view is to show all the changes that have been made to the existing attendance.

URL: [localhost:8000/dashboard/report/](localhost:8000/dashboard/report/)


### Management Commands

#### How to Use:

`python manage.py <command_name>`

#### Commands

`send_message_to_absentee` - Runs through all the absentee of that day and sends a message to their parents. 

(This is to be run as cron job in the production, every day at 4pm. For more information go [here](https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/) or [here](<https://medium.com/@bencleary/django-scheduled-tasks-queues-part-1-62d6b6dc24f8>))



### CHANGE LOG

#### 1.2 - (pending)

##### Added

-   Absentee confirm model
-   Absentee count and proper message

##### Changed

-   Default colour scheme

#### 1.1 - 07/AUG/2018

##### Added

-   Favicon added
-   Bug Fixes
-   Login page errors
-   Login/Logout URLs

#### 1.0 - 07/AUG/2018

##### Added

-   Color inversion toggle switch
-   LocalStorage
-   Moved to BitBucket
-   Select all button in attendance main

#### 1.1 (Beta) - 07/AUG/2018

##### Added

-   Department model
-   Main JS file

##### Changed

-   User Model
-   Teaches Model
-   Minor UI

#### 1.0 (Beta) - 26/JULY/2018

##### Added

-   Account Registration
-   Attendance Entry (Subject selection)
-   Attendance Main
-   SMS mixin
-   Dashboard UI
