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

1. We

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

9. And, as explained in previous step, we added our .exe file into tools folder.