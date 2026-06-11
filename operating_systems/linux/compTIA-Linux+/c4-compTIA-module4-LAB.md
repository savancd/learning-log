
[!NOTE]
- This is the LAB following the course preparation  by HowToNetwork YouTube channel, for CompTIA Linux+ certification 

# CompTIA Linux+
## This is LAB Excercises for Module 4 



**Scenario:** A company has three deparments. Development, HR, and information systems **(IS)**
with a list three employees in each depament. New server has arrived, and a structure of directories and files must be created according to the followind


a: Each department must have a directory in the root **/**.
---

Create respective directories at the **root level**

```bash
$ sudo mkdir NAME
```



b: Each department must have a group
---

	
Create a required groups:

```bash
$ groupadd NAME-OF-THE_GROUP
```

With **cat /etc/group** you can check are the groups created.

Output:

```bash
development:x:1001:
hr:x:1002:
IS:x:1003:
```

c: Each employee must have an account and belong to the proper group
---


Next is to add users:

```bash
$ sudo adduser dev1
``` 

Add user to the group he belongs:

```bash
$ sudo usermod -G development dev1
```

Next step is to create all other users as well to place them in respective groups they belong. Just repeat previous steps in creating users and adding them to the groups.


After adding all user and adding them to the groups, you can check it with:

```bash
cat /etc/group

# Output will be
development:x:1001:dev1,dev2,dev3
hr:x:1002:hr1,hr2,hr3
IS:x:1003:is1,is2,is3
```


d: Files can be created only in these directories by users that belong to the corresponding group. Files can be only removed by the owner.
---



Creating or removing files from a directory is established by creating rules and permissions on directory and not on the files.   
It need to be changed that is not a **root** ownership, it should be on group:

```bash
drwxr-xr-x   2 root root  4096 May 25 17:47 development
drwxr-xr-x   2 root root  4096 May 25 17:47 hr
drwxr-xr-x   2 root root  4096 May 25 17:47 IS
```

Because we are just changing group that owns the directory and not a user, we do not need to define a user.   

Example how we can assign the group:

[!NOTE]
- Because we don't need to add a user, we can just add a **(:)** in front of directory name.

```bash
$ sudo chown :development /development/
``

As well other ones need to do the same:

```bash
$ sudo chown :hr /hr/
$ sudo chown :IS /IS/
```

Now check do those directories belong to the respective groups.

```bash
$ ls -ld /development/ /hr /IS
```

Output:

```bash
# In the following examples you can see how those directories now belong to the groups
$ drwxr-xr-x 2 root IS          4096 May 25 17:47 /IS
$ drwxr-xr-x 2 root development 4096 May 25 17:47 /development
$ drwxr-xr-x 2 root hr          4096 May 25 17:47 /hr
```

Now the permissions need to be done and to give them right permissions so only the ones who belong to the group can write in it.

```bash
$ sudo chmod g+w /development /hr /IS
```

Now in the following example you can see the difference and that they have right to write in it.

```bash
drwxrwxr-x 2 root IS          4096 May 25 17:47 /IS
drwxrwxr-x 2 root development 4096 May 25 17:47 /development
drwxrwxr-x 2 root hr          4096 May 25 17:47 /hr
```

To prevent that some other user can not delete and remove some file that is created by another user we need to add **-t** at the permissions.

Example:

```bash
# With +t we are limiting persmisions only on owner of the file that he can remove the file
$ chmod +t /development
```

Before adding the **-t**:

```bash
$ drwxrwxr-x 2 root development 4096 May 25 18:47 /development/
```

After adding **-t**:

```bash
$ drwxrwxr-t 2 root development 4096 May 25 18:47 /development/
```

Now you can see difference on the file permissions with extra **-t** at the end.
When you now try as some other user to remove the file you gonna get an error:

```bash
$ rm -rf dev1.txt 
rm: cannot remove 'dev1.txt': Operation not permitted
```


e: Make sure that files created in the directories belong to the apropriate deparment group.
---


This we need to make sure it's not happening, because **development** group is the one that owns that directory. That means that any file created inside must be owned by the same group.


```bash
$ ls -l /development/
total 0
-rw-rw-r-- 1 dev1 dev1 0 May 25 18:47 dev1.txt
```

Now it need to be forced to be owned by directory.

```bash
$ sudo chmod g+s /development/
```

With next command you can check is everything ok now.   
The **s** means that group owns the directory and the files belongs to that directory belongs to the same group.  


```bash
$ ls -ld /development/
drwxrwsr-t 2 root development 4096 May 25 18:47 /development/
```

Now when we create new file as some user, we gonna see that it belongs to the gpoup.

```bash
$ ls -l
total 0
-rw-rw-r-- 1 dev1 development 0 May 25 19:21 dev1_test2.txt
```

In previous example now you can see that file is owned by the **dev1** user and the group that owns the directory.



Now everything that is setup for the **development** directory, must be done for other two directories **IS and hr**.
























