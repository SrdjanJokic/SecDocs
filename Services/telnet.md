# Telnet Service

Common Ports: 23 TCP

## About

Telnet is a client/server application protocol that provides access to virtual terminals of remote systems on local area networks or the Internet. Telnet transmits all information including usernames and passwords in plaintext so it is not recommended for security-sensitive applications

## Exploits

### Misconfiguration (Blank Password)

#### Conditions

Certain users (usually root) have been allowed to login with a blank password.

#### How To

```shell
telnet {ip}     # Connect to target IP via telnet
```

User is then prompted to input their username and password. For username, we can try some of the common usernames: admin, administrator and root. If neither of those work, we can use a [list](../Other/Resources.md#lists) of common usernames to attempt to brute-force the username. For password, we, of course, specify a blank password.

if the telnet server was incorrectly configured, we'll have access to its contents.

## Common Commands

| Command | About                                                                      |
|---------|----------------------------------------------------------------------------|
| ls      | Lists files in the current directory                                       |