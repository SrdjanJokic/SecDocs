# FTP Service

Common Ports: 21 TCP, 22 TCP (if through SSH)

## About

File Transfer Protocol (FTP) is a standard communications protocol to transfer computer files from a server to a client on a computer network. If the server is configured to do so, anonymous connections are allowed. For secure transmissions that protects user credentials, FTP is usually paired with SSL/TLS (FTPS) or SSH File Transfer Protocol (SFTP) is used instead. In that case, instead of being ported through port 21, it's ported through port 22 (SSH). Additionally, port 80 is usually open for the Web Server.

## Exploits

### Misconfiguration (Anonymous Login)

#### Conditions

Admin enabled (or didn't disable) anonymous login

#### How To

```shell
$ sudo apt install ftp -y   # Fetch the latest version of FTP
$ ftp {ip}                  # Connect to specified IP
```

User is then prompted to input their username and password. We'll use:
- username: anonymous
- password: {anything}

If the FTP Server was incorrectly configured, we'll have anonymous access to its contents.

## Common Commands

| Command | About                                                                      |
|---------|----------------------------------------------------------------------------|
| help    | Displays the help screen                                                   |
| bye     | Closes the FTP connection                                                  |
| ls      | Lists files in the current directory                                       |
| get     | Downloads the specified file to the location where connection started from |