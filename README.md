# Range-Kata-App

## Index
1. [Main](./main.py)
2. [How to Run Python File](#how-to-run-python-file)
3. [How we uploaded to Chocolatey](#how-we-uploaded-to-chocolatey)

## How to Run Python File

1. Check if you have the latest version of Python and pip installed in your computer.

2. In case you haven't installed Python or is not up to date, download and install the latest version of Python from this link: https://www.python.org/downloads/.

3. Also, Linux users can install latest version of python by writing in their terminal ```sudo apt install python3.X``` (being X the latest version).

4. To install pip, you only need to ```python -m pip install --upgrade pip``` or ```sudo apt install python3-pip``` depending on your Operating System.

5. After installation is completed, ```git clone``` this repository.

6. Then, all you have to do to init the software is to ```python main.py```, ```python3 main.py``` or ```pip3 main.py```. If you followed step 3 then ```python3 main.py``` should work for you.

## How we uploaded to Chocolatey


1. First, we installed Chocolatey using the guide from this link: https://chocolatey.org/install

2. Then, we opened Powershell in Administrator mode.

3. After that, we created a new package by ```choco new rangeoscarrafael```

4. Then, ```cd rangeoscarrafael```

5. Opened the current folder on **VSCode** by ```code .```

6. Deleted *ReadMe.md* and *_TODO.txt* from that folder. Then, inside tools folder we deleted *chocolateybeforemodify.ps1*, *chocolateyuninstall.ps1*, *LICENSE.txt* and *VERIFICATION.txt*.

7. We edited *package-name.nuspec* with the actual data of our project.

8. On tools folder, we edited *chocolateyinstall.ps1* to look like this:
```
$name = "rangeOscarRafael"
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$path = Join-Path $toolsDir 'main.exe'

Install-BinFile -name $name -path $path
```

9. In that moment, we needed to add the .exe of our app in the same folder as *chocolateyinstall.ps1*. For doing so we needed to install pyinstaller.  

10. In your powershell, type ```pip install pyinstaller```.  

11. The, convert the file .py to .exe with the following command: ```pyinstaller [filename].py```.  

12. And, as explained in previous step, we added our .exe file into tools folder.

13. To be able to create the package, we run the command ```choco pack```. It created an .nupkg file.  

14. If you want test that the package is working, you can install it in the same folder with ```choco install [package_id] -dv .```. 

15. If you want to Upload the package in chocolatey.org, you will need to create an [account](https://community.chocolatey.org/account/Register).  

16. At the end of the proccess, they will asign you a key that you should set in your terminal with   ```choco apikey -k [API_KEY_HERE] -source https://push.chocolatey.org/```. It will let then know wich user is trying to upload what package, by also giving an extra layer of security.    

17. Then, set the terminal in the location of your package. If you only have one .nupkg file in that destination, you can use the command ```choco push --source https://push.chocolatey.org/```.

Your package will be uploaded by this point. To be fully accesible, the page will create some tests in orther to confirm it's actually secure. By that moment you will have your package fully open and so anyone will be able to download it.
