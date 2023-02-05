# Server Message Block Protocol (SMB)

Common Ports: 445 TCP

## About

SMB protocol provides shared access to files, printers and serials ports between endpoints on a network. It's usually running on a Windows machine. Since SMB usually runs on Application or Presentation layers of the OSI model, it relies on lower-level protocols for transport. It's most commonly paired with NetBIOS over TCP/IP and is the reason why we'll usually see both protocols with open ports when scanning the target.

For security reasons, SMB requires clients to provide credentials in order to execute CRUD operations on a share. 

## Exploits

### Misconfiguration (Anonymous/Guest Login)

Regardless of the fact that SMB provides a secure way of interacting with its shared, it's possible for the admin to misconfigure it and allow anonymous/guest logins.

#### Conditions

Admin enabled (or didn't disable) anonymous login.

#### How To

```shell
sudo apt-get install smbclient      # Client for interacting with SMB
smbclient -L {ip}                   # List shared of the specified host
```

If the authentication is required, we'll be prompted to input a username and/or password. Since SMB always requires a username for a connection to be established it will passthrough our local username to avoid errors within the connection. If the SMB has been misconfigured, we will see a list of shares on the host.

```
Enter password:
    ShareName   Type    Comment
    ---------   ----    -------
    ADMIN$      Disk    Admin shares for access to all other shares
    C$          Disk    Admin share for C:\
    IPC$        IPC     Inter-process communication (not part of system)
    MyShare     Disk    
```

Usually, shared with a '$' sign in them have been automatically created and are most likely correctly configured by default. In the sample above, "MyShare" seems to be human-made. We'll attempt to connect to the share with empty credentials.

```shell
smbclient \\\\{ip}\\MyShare
```

If the SMB was incorrectly configured, we'll have anonymous/guest access to its contents.

## Common Commands

| Command | About                                                                      |
|---------|----------------------------------------------------------------------------|
| help    | Displays the help screen                                                   |
| exit    | Closes the connection                                                      |
| ls      | Lists files in the current directory                                       |
| get     | Downloads the specified file to the location where connection started from |
| cd      | Changes directory to the specified path                                    |