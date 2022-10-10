 ______                   __             ____        __
/\__  _\                 /\ \__         /\  _`\     /\ \__
\/_/\ \/     ___     ____\ \ ,_\    __  \ \ \L\ \___\ \ ,_\
   \ \ \   /' _ `\  /',__\\ \ \/  /'__`\ \ \ ,__/ __`\ \ \/
    \_\ \__/\ \/\ \/\__, `\\ \ \_/\ \L\.\_\ \ \/\ \L\ \ \ \_
    /\_____\ \_\ \_\/\____/ \ \__\ \__/.\_\\ \_\ \____/\ \__\
    \/_____/\/_/\/_/\/___/   \/__/\/__/\/_/ \/_/\/___/  \/__/

# InstaPot
An Instagram mass reporter tool, made with love by M0bl3y.

# Warning
<pre>tested on python 3.9.7</pre>

- **The earlier version of this script is only compatible at WINDOWS operating system. So you need to install python version 3 manually first before using this script (the Linux version is under development).**

- **Make sure you have verified sock puppets account, and also make sure the 2FA is disabled on that accounts.**

### Chrome Driver
Make sure your chromedrive.exe has same version with your current Chrome browser (you can check and download it from: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)). And place the **.exe** file inside the **/engine** directory.

# Installation
```git clone https://github.com/erzaf/instapot```

Dont forget to install the dependencies:

```pip install -r requirements.txt```

# Usage

**FIRST**:
Make sure you have added your sock puppets account username and password inside the **creds.csv** file with the format below:
(separated by ";" between username and password)

```
username1;password1
username2;password2
```
You can add as much as you have.

Then you are ready using this script by:
```python instapot.py <target_username>```

Example:
```python instapot.py abangtukangbaso```

# How it works

This script is run based on the Chromium driver, its automate the manual way of reporting. The default timeout of each execution is 30-60 seconds, if you got timeout, you might have a s*cks internet connection.

# What's next?

The next version of this script maybe is about using the proxy lists to avoid the rate limitation from the META. But it might depends on the sponsor lol xD