**IceCream**
============
This repository contains the source code of [silive.in](http://silive.in/), which is the official website of Software Incubator. This website imparts information about the members, projects done by the members and the clients of Software Incubator. 

## Getting Started
---
1. Clone the [repository](https://github.com/Software-Incubator/IceCream) from github link&nbsp; `https://github.com/Software-Incubator/Icecream`
2. Create a virtual environment \[see [windows](https://docs.djangoproject.com/en/2.2/howto/windows/) and [linux](https://dev.to/achiengcindy/-how-to-set-up-django-environment-in-linux-for-beginners-35am) to learn to create virtual environment]
3. Set the values of environment variables in base setting file

    `EMAIL_HOST_USER = your email id`

    `EMAIL_HOST_PASSWORD = password`

    `RECEIVER_EMAIL = any email id`

    `DEFAULT_FROM_EMAIL = your email id`

    `RECAPTCHA_PRIVATE_KEY = set credentials`

    `RECAPTCHA_PUBLIC_KEY = set credentials`

4. Activating virtual environment in terminal or cmd
5. Run these commands

    `cd Icecream\`

    `pip install -r requirements.txt`

    `python manage.py migrate`
    
    `python manage.py runserver`
