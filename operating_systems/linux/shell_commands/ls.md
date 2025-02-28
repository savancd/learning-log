### ***ls*** Syntax is the **command** in Linux that lists directory content and files,
#### List information about the FILEs (the current directory by default).
#### Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.


> *List only the directories:*
```
ls -d */
```

> *It is used in the way:*
```
ls “option”
```


> Some of the options used with **ls** command:

> *Display detailed information about directories and files.*
```
ls -l
```

> *Detailed information, including all hidden files that are represented with a *.name*.*
```
ls -a
```
___
___

> ***d****rwxr-xr-x   3 root root  4096 May 23  2024 home*
>
>> First character indicates the type of the file ***d***
* d: directory
* -: regular file
* l: link
* c: character device
* b: block device

> *d***rwx***r-xr-x   3 root root  4096 May 23  2024 home*
* r: read permission(owner can modify content)
* w: write permission(owner can modify the content)
* x: execute permission(can access the directory)

> *drwx***r-x***r-x   3 root root  4096 May 23  2024 home*
* r: group members can view the content
* -: group members can't modify the content
* x: group member can access the directories

> *drwxr-x***r-x**   *3 root root  4096 May 23  2024 home*
* r: can view the content
* -: can't modify the content
* x: can access the directories

> *drwxr-xr-x*   **3** *root root  4096 May 23  2024 home*
* 3: number of links to the directory including the directory itself, it's parent and any subdirectories.

> *drwxr-xr-x*   3 ***root root***  4096 May 23  2024 home*
* root root: first one is owner of directory and second one is the group

> *drwxr-xr-x*   3 root root  ***4096*** May 23  2024 home*
* 4096 is the file size

> *drwxr-xr-x*   3 root root  4096 ***May 23  2024*** home*
* May 23  2024 is the date last time modified

> *drwxr-xr-x*   3 root root  4096 May 23  2024 ***home***
* home is the directory
___
___

> *Display one file per line:*
```
ls -1
```

> Combining options
```
ls -lah
```
* long listing, including hidden files, with human-readable size*


*  In the following example, specify multiple directories.
>
```
ls ~/IT/books/ /usr
```
>> /home/sava/IT/books/:
gameDev  hardware  linux  python

>> /usr:
bin  games  include  lib  lib64  libexec  local  sbin  share  src



> To list all directories without files in it, it's possible to use
command with additional filtering through ***grep***.
```
ls -R | grep ":$"
```
> The output will be:
* .:
* ./books:
* ./books/gameDev:
* ./books/hardware:
* ./books/linux:
* ./books/python:
* ./operating_systems:
* ./operating_systems/linux:
* ./operating_systems/linux/excercises:
* ./operating_systems/linux/playground:
* ./operating_systems/linux/shell_commands:
* ./operating_systems/windows:
* ./python:
* ./python/files:
* ./python/files/assignments:
* ./python/files/challenges:
* ./python/files/files:

___
___

> **To get a complete list of commands and help on the command for this or any other shell command**
>
>> --help
```
ls --help
```
___
___


| Option | Result | Description |
|:------:|:------:|:-----------:|
|  -a    |   --all    |      List all files even those with names that begin with period, which are normally not listed (hidden)       |
|  -A    |   --almost-all     | Like a ***-a*** option above except it does not list .(current_directory) ..and (parent_directory) |
|  -d    |   --directory     | When directory is specified  ***ls*** will list the content of the directory not the directory itself. Use this option in conjuction with the ***-l*** option to see the details about the directory rather then it's contents.  |
|  -F    |   --classify     |    This format will append an indicator character to the end of each listed name. A (/) forward slash if the name is directory   |
|  -h    |   --human-readable     |   In long format listings, display file sizes in human readable format rather in bytes.   |
|  -l    |        |   Display result in long format.    |
|  -r    |   --reverse     |   Display results in reverse order. Normally, ***ls*** display results in ascending alphabetical order.    |
|  -S      |        |    Sort results by file size.         |
|  -t      |        |    Sort by modification time.         |

