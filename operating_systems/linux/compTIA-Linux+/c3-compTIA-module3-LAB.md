
<h1 align="center">CompTIA Module 3</h1>

> This is a practice LAB for a module 3 where is practiced user management

##  Q3


-  Creating one group with 3 new users to be created. 
-  Add those 3 users into the group
-  Define one user as a Admin of the group


<h2 align="center"> Add new user</h2>

```bash
$ sudo adduser
```

>  **sudo** means that to add user you must have admin privileges or as a **root** user to be

Now I need to add those users into group  

```bash
$ test-group
```

```bash
# Add users into group
$ usermod -G test-group user-test1
```

```bash
# With this next line we can check did user belong to the group
$ id user-test1
``

```bash
# By printing with "cat /etc/group" you can check do those users now belong to the group
$ test-group:x:1001:user-test1,user-test2,user-test3
```
<h2 align="center">Add Admin to the group</h2>


You can check options for setting up admin of the group with a command:

```bash
$ sudo gpasswd --help
```

It's gonna print onto the screen:

```bash
Usage: gpasswd [option] GROUP

Options:
  -a, --add USER                add USER to GROUP
  -d, --delete USER             remove USER from GROUP
  -h, --help                    display this help message and exit
  -Q, --root CHROOT_DIR         directory to chroot into
  -r, --remove-password         remove the GROUP's password
  -R, --restrict                restrict access to GROUP to its members
  -M, --members USER,...        set the list of members of GROUP
  -A, --administrators ADMIN,...
                                set the list of administrators for GROUP
Except for the -A and -M options, the options cannot be combined.
```

```bash
# With this command you can add Admin of the group
$ gpasswd -A user-test1 test-group
```

Adding a user as a Admin of the Group.   

1: They can:

- They can add and remove users from a Group
- Access files and directories that grant group read/write/execute permissions on the group
- Create new files that inherit the directory's group
- Edit, delete and or execute files permited by the group 
- Run processes that rely on group membership for access control

2 They Cannot: 

- Modify files that only Root or other user can access 
- Change ownership of files to other users
 

<h2 align="center">Add 4th user</h2>


With next command you can check options in useradd and what must be placed in line of code to make a new user.


```bash
$ sudo useradd --help
```


```bash
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]

Options:
      --badname                 do not check for bad names (DEPRECATED)
  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
      --btrfs-subvolume-home    use BTRFS subvolume for home directory
  -c, --comment COMMENT         GECOS field of the new account
  -d, --home-dir HOME_DIR       home directory of the new account
  -D, --defaults                print or change default useradd configuration
  -e, --expiredate EXPIRE_DATE  expiration date of the new account
  -f, --inactive INACTIVE       password inactivity period of the new account
  -F, --add-subids-for-system   add entries to sub[ud]id even when adding a system user
  -g, --gid GROUP               name or ID of the primary group of the new
                                account
  -G, --groups GROUPS           list of supplementary groups of the new
                                account
  -h, --help                    display this help message and exit
  -k, --skel SKEL_DIR           use this alternative skeleton directory
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -m, --create-home             create the user's home directory
  -M, --no-create-home          do not create the user's home directory
  -N, --no-user-group           do not create a group with the same name as
                                the user
  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
  -p, --password PASSWORD       encrypted password of the new account
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             login shell of the new account
  -u, --uid UID                 user ID of the new account
  -U, --user-group              create a group with the same name as the user
  -Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
      --selinux-range SERANGE   use a specific MLS range for the SELinux user mapping

```

Important is to mention that every command must be placed inside a line of code when making new user in this way.  


```python
# -c, --comment COMMENT         GECOS field of the new account
# -b, --base-dir BASE_DIR       base directory for the home directory of the
# -k, --skel SKEL_DIR           use this alternative skeleton directory
# -d, --home-dir HOME_DIR       home directory of the new account
# -m, --create-home             create the user's home directory
```


```bash
# Example
$ sudo useradd -c "user-test4" -b /home/user-test4 -d /home/user-test4 -m -k /etc/skel user-test4
```



```bash
# You can check the directory of the user to see is it ther and created
$ ls -la /home/user-test4/


# Example what you should get printed on the terminal screen
total 20
drwx------ 2 user-test4 user-test4 4096 May 24 18:51 .
drwxr-xr-x 7 root       root       4096 May 24 18:51 ..
-rw-r--r-- 1 user-test4 user-test4  220 Jul 30  2025 .bash_logout
-rw-r--r-- 1 user-test4 user-test4 3526 Jul 30  2025 .bashrc
-rw-r--r-- 1 user-test4 user-test4  807 Jul 30  2025 .profile
```


<h2 align="center">Users passwords</h2>


Define the same user password for the multiple users. Show their hashed passwords. And are those hashes the same and why?!


With next command you can change the users password:

```bash
$ passwd user-test1

# On the screen you will get output
New password:
Retype new password:
passwd: password updated successfully
```

Hashed passwords you can check in:

```bash
$ cat /etc/shadow
```

Hash will always be the same, unless you are using encription key. If you are using key for encription then passwords will be the same.


<h2 align="center">Lock users account</h2>

There is different ways of locking users account.   
One of the ways is to use:

```bash
$ sudo passwd -l user-test1
```

Output:

```bash
passwd: password changed.
```


Some other way to lock users account:

```bash
$ sudo usermod -L user-test1
```

If you want to unlock it, you can with following example:

```bash
$ sudo usermod -U user-test1
```



<2 align="center">Password expiration</h2>

Define user password exporation date.   
With a following line you can check how to do it:  


```bash
$ sudo chage --help
```

Output:

```bash
Usage: chage [options] LOGIN

Options:
  -d, --lastday LAST_DAY        set date of last password change to LAST_DAY
  -E, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
  -h, --help                    display this help message and exit
  -i, --iso8601                 use YYYY-MM-DD when printing dates
  -I, --inactive INACTIVE       set password inactive after expiration
                                to INACTIVE
  -l, --list                    show account aging information
  -m, --mindays MIN_DAYS        set minimum number of days before password
                                change to MIN_DAYS
  -M, --maxdays MAX_DAYS        set maximum number of days before password
                                change to MAX_DAYS
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
  -W, --warndays WARN_DAYS      set expiration warning days to WARN_DAYS

```


Set expiration date **(YYYY-MM-DD)**:

```bash
$ sudo chage -E 2026-07-5 user-test1
```



























