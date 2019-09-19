# Save The Bird

> This is a simple game developed using pygame. Aim is to save the bird for maximum possible time. You control the little bird. You can make it climb by pressing the up arrow, or by pressing space bar. Don't crash into any pipes! For every pipe you pass without colliding, you get one point.



<p align="center">
  <img src="https://user-images.githubusercontent.com/35782113/65266081-554ab680-dae0-11e9-9d8d-932b910f2e9b.gif">
</p>



## Example 

&nbsp;

[![Playing the Save the Bird Game ](https://user-images.githubusercontent.com/35782113/65266082-554ab680-dae0-11e9-857c-421cdb875e24.gif)]()
&nbsp;

&nbsp;

------

## Table of Contents 

- [Save The Bird](#save-the-bird)
  * [Example](#example)
  * [Table of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Clone](#clone)
    + [Running the Save The Bird](#running-the-save-the-bird)
  * [Building the Windows installer](#building-the-windows-installer)
    + [Using pyinstaller](#using-pyinstaller)
  * [History](#history)
  * [Playing the Game](#playing-the-game)
  * [Usage](#usage)
  * [Executable](#executable)
  * [To-do](#to-do)
  * [Documentation](#documentation)
    + [Making the layout of the Save The Bird](#making-the-layout-of-the-save-the-bird)
  * [Tests](#tests)
  * [Contributing](#contributing)
  * [FAQ](#faq)
  * [Support](#support)
  * [Donations](#donations)
  * [License](#license)


------

## Getting Started

### Prerequisites

Although, I used the following software (with their corresponding versions) to run this program, "Save The Bird" should be able to run with any version of Python 3 +. We need the following packages to run this program:

- Python 3.7.4 (This program should work fine with any installation of Python3+. Although, I used Python 3.7.4)

- pygame==1.9.6 (apt-get install pygame or pip install pygame)

  

### Clone

- Clone this repo to your local machine using `https://github.com/rajenderk18/Save-The-Bird.git`

### Running the Save The Bird

You can run the program by following the below commands:

```
$ git clone https://github.com/rajenderk18/Save-The-Bird.git
$ cd Save-The-Bird
$ chmod +x Save-The-Bird.py
$ ./Save-The-Bird.py

```

or run the Save-The-Bird.py using python in terminal or command prompt using below command:

```
python Save-The-Bird.py
```

##### Running the game using command-prompt:

![Running the game using command prompt ](https://user-images.githubusercontent.com/35782113/65267161-78766580-dae2-11e9-9b06-1d0e43ac775e.gif)



------

## Building the Windows installer

### Using pyinstaller

I use the pyinstaller for building the window installer for the "Save The Bird". You can install the pyinstaller by using the following command:

```
pip install pyinstaller
```

You will need pip to install the pyinstaller. After installing the pyinstaller, you have to run this command to create the window installer (.exe file) for the game:

```
pyinstaller --onefile -w Save-The-Bird.py
```

When the command executed completely, you will see two folders (build and dist) in the folder of your project. Build folder contains the binary of your "Save The Bird" game and you don't need them. Your installer (.exe file) is in the dist folder. Double click on it to check whether it is running or not. If it does not work, that means it is not able to find the required files like images, logo, icon, etc. In this case, you just have to copy the exe file and paste it outside the dist folder. Now it should work without any problem.

### Using CX_FREEZE

This is another method of creating the single executable for the game. 

 **cx_Freeze** is straightforward to use and its documentation is very clear. Here are the steps that should be performed before building executable:

1. ***Place all of your code files in one folder.*** 
2. ***Correct any now-faulty import statements.*** 
3. (Optional) If you're using an icon, you can keep icon file in a separate icon folder. This just makes the final package look cleaner, as you don't have two items with the same icon creating confusion. But as this program has only one icon and one image, so I keep both in the same folder as the code.
4. ***Test your program*** once you've tweaked your imports and the structure is all set. If not: debug time.
5. ***Create a Python script named setup.py*** ***in your folder*****.** This script is the easiest way to compile with cx_Freeze, and contains all of the instructions necessary to get your file in the format you want.
6. ***Make sure cx_Freeze is installed.*** I just did pip install cx_Freeze in the console.

#### Writing setup.py:

Open your favorite text editor/IDE, and write something like the following into it (every line is essential):

```python
import sys
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                      #"packages": [ "os", "shutil", "subprocess", "getpass", "time", "os.path"],
                     #"excludes": ['tkinter'],
                     "include_files": [
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                         'bird.ico', 'assets/']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Save The Bird",
      version="1.0",
      description="Save The Bird",
      options={"build_exe": build_exe_options},
      executables=[Executable("Save-The-Bird.py", targetName='Save-The-Bird.exe',
			    icon='bird.ico',
			    copyright='Copyright (C) Rajender Kumar 2019', base=base)])
```

#### Creating the Package:

Open the console to your setup.py's directory and run the following command: 

```
python setup.py build
```

This will run the script to create your packaged program. It will create a new directory in the same directory as setup.py called 'build'. Inside of 'build', you'll find another folder with a name that starts with 'exe.' and ends with an identifier for the platform that distutils uses. Inside of that folder, you will find the contents of your package -- the .dlls, the folders, and your beloved .exe. You can further use NSIS to make a single installer file from these files.

------

## History

"Save The Bird" is the clone of famous mobile game- "Flappy Bird".  Save the game is developed with "pygame" while flappy bird was developed for android and iphones. Flappy Bird is developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company dotGears. The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them. Nguyen created the game over the period of several days, using a bird protagonist that he had designed for a cancelled game in 2012.

The game was released in May 2013 but received a sudden rise in popularity in early 2014. Flappy Bird received poor reviews from some critics, who criticized its high level of difficulty, plagiarism in graphics and game mechanics, while other reviewers found it addictive. At the end of January 2014, it was the most downloaded free game in the App Store for iOS. During this period, its developer said that Flappy Bird was earning **$50,000 a day** from in-app advertisements as well as sales.

Flappy Bird was removed from both the App Store and Google Play by its creator on February 10, 2014, due to guilt over what he considered to be its addictive nature and overuse. The game's popularity and sudden removal caused phones with it pre-installed to be put up for sale for high prices over the Internet. Games similar to Flappy Bird became popular on the iTunes App Store in the wake of its removal, and both Apple and Google have removed games from their app stores for being too similar to the original. The game has also been distributed through unofficial channels on multiple platforms.

In August 2014, a revised version of Flappy Bird, called Flappy Birds Family, was released exclusively for the Amazon Fire TV. Bay Tek Games also released a licensed coin-operated Flappy Bird arcade game.



------



## Playing the Game

Flappy Bird is a side-scrolling mobile game featuring 2D retro style graphics. The objective is to direct a flying bird, who moves continuously to the right, between sets of obstacles (these obstacles can be  pipe, knife, swords, and pillars). If the player touches any obstacles, they lose. Flying bird briefly flaps upward each time that the player press "UP ARROW" key; if the "UP ARROW" key is not pressed, Flying bird falls because of gravity; each pair of obstacles that bird navigates between earns the player a single point.

There is no variation or evolution in game-play throughout the game, as the obstacles always have the same gap between them and there is no end to the running track, having only the flap and ding sounds and the rising score as rewards.



## Usage 

#### Playing the game:

![Playing The game](https://user-images.githubusercontent.com/35782113/65266870-e8382080-dae1-11e9-8bbf-b071cccf9c38.gif)



#### Flying bird die when he collide with any obstacles or touch the ground:



![Bird Died on collision](https://user-images.githubusercontent.com/35782113/65266083-554ab680-dae0-11e9-86de-c62f65913b3c.gif)



#### Different birds and background used in the game:



![Different birds used in the game](https://user-images.githubusercontent.com/35782113/65266080-554ab680-dae0-11e9-8c03-03faff33df6c.gif)



## Executable

#### Version: v0.1

You can download the executable for window from here: <a href="https://github.com/rajenderk18/Save The Bird/releases/download/0.1/Save The Bird.exe">Save-The-Bird-v01.exe</a>

## To-do

- [x] New obstacles introduced (knife, swords, pillars, pipes, stones etc.)
- [x] New birds introduced(i.e. American Robin, Skuas, Osprey, Eagle, Bald Eagle, Blue Jay, Swallow, heron ).
- [x] New background introduced
- [ ] Implementation of level and selection logic for levels.
- [ ] Need to implement the logic to remember the highest score for players.
- [ ] need to work on Full-screen version. 

## Documentation 

### Making the layout of the Save The Bird

For making the layout of the Save The Bird, I used the screen size of 458*812 which gave the user same feeling as he is playing on the phone. I used 30 frame per seconds to gave the user a feeling that they are playing a live game while in actual, there are only images blitted on the screen. Game screen consists of a base and a background. Our flying bird is positioned right in the middle vertically and toward left horizontally in the screen. Obstacles comes from the right and move towards left. Each obstacle comes in pair and there is some space (called offset in code) between the pair from which bird can pass. Movement of obstacles give the illusion that bird is moving toward right while in realty, bird is at same position at all the time. Every time player start the game, he see random bird and random obstacles. When the flying bird passes 1 pair of obstacle, his score is increased by one and displayed on the screen. 

## Tests

This program is successfully tested on Window 10, Mac, and Ubuntu 16.04.

------

## Contributing

If interested, you can contribute by following the given step:

1. Fork it using `https://github.com/rajenderk18/Save-The-Bird.git`
2. Create your feature branch (git checkout -b my-new-feature) 🔨🔨🔨
3. Commit your changes (git commit -am 'Added <xyz> feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request 🔃

------

## FAQ

**How to install the Save The Bird?**

- See Installation.

**I have a questions that is not answered here!**

- In case you have a question that this F.A.Q. does not cover, please contact us here with your question!

------

## Support

Reach out to me at one of the following places!

- Website at <a href="http://KumarRajender.com" target="_blank">`KumarRajender.com`</a>
- Email me: [rajenderk18@gmail.com](mailto:rajenderk18@gmail.com)

&nbsp;

------

## Donations

- If you think this little game is useful to you, then it's a good reason to do a donation.
- Your gratitude and financial help will motivate me to continue improving this and work on many other open-source project.
- I dedicated a lot of free time to this project and do not intend to show any ads because ads kind of suck.
- If you like my little game, please consider donating so I can continue working on it.

&nbsp;**How you can donate**
You can donate via:



|                         Payment Link                         |        If image link not working, click on these link        |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <a href="https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217312-24a6e400-c112-11e9-9eef-cc1a0bf69747.jpg" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> | <a href="https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton">Paypal</a> |
| <a href="https://www.patreon.com/bePatron?u=23393229" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217315-253f7a80-c112-11e9-8aed-aa70e001c3d9.png"></a> | <a href="https://www.patreon.com/bePatron?u=23393229">Patron</a> |
| <a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63219307-f8548d00-c13c-11e9-809d-0c531dc1f0d2.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> | <a href="https://www.buymeacoffee.com/rajenderk18">BuymeaCoffee</a> |
| <img src="https://user-images.githubusercontent.com/35782113/63689899-360a8300-c7d9-11e9-858a-2a014c73e87b.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > 1Hfu2yC7LH1nqQTdZxcRcgpYBjn6b5fD5j | <img src="https://user-images.githubusercontent.com/35782113/63795081-34bc8180-c8d1-11e9-8c4d-8a709c33a83f.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >1Hfu2yC7LH1nqQTdZxcRcgpYBjn6b5fD5j |
| <img src="https://user-images.githubusercontent.com/35782113/63795072-3423eb00-c8d1-11e9-9313-272ef36735d6.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > qq2nhtkytapezz9px0xh9vegyjutpka5asavxf0s8n | <img src="https://user-images.githubusercontent.com/35782113/63795080-34bc8180-c8d1-11e9-9d66-c8c300b601e7.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >qq2nhtkytapezz9px0xh9vegyjutpka5asavxf0s8n |
| <img src="https://user-images.githubusercontent.com/35782113/63689897-360a8300-c7d9-11e9-9640-d2493b872f9f.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >0x727C0AC1f216Cc2b83680E4FD37A9A0f14c62Dd5 | <img src="https://user-images.githubusercontent.com/35782113/63795079-34bc8180-c8d1-11e9-9ff2-17fce1c74fc5.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >0x727C0AC1f216Cc2b83680E4FD37A9A0f14c62Dd5 |
| <img src="https://user-images.githubusercontent.com/35782113/63795074-34bc8180-c8d1-11e9-880d-d76c1955c2a9.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" > MA32LZ7Gr3C7Ccp7R1NhB63QogvCf5yePR | <img src="https://user-images.githubusercontent.com/35782113/63795076-34bc8180-c8d1-11e9-9a1a-700333b800b4.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" >MA32LZ7Gr3C7Ccp7R1NhB63QogvCf5yePR |

&nbsp;

&nbsp;

<p align="center">
  <a href="https://www.paypal.com/webapps/shoppingcart?flowlogging_id=71de0a21b6cb7&mfid=1568207919162_71de0a21b6cb7#/checkout/openButton" target="_blank">
  <img width="300" height="125" src="https://user-images.githubusercontent.com/35782113/63217310-24a6e400-c112-11e9-9fb6-2d7f6ec2f143.jpg">
    </a>
</p>

**Other ways you can help me**

- Do you have a Youtube Channel? a Blog? anything similar? Promote Save The Bird!
- Thank you for considering to donate



------

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://github.com/rajenderk18/Panther-Calculator/blob/master/LICENSE)**
- Copyright 2019 © <a href="http://KumarRajender.com" target="_blank">Rajender Kumar</a>.

