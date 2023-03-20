# Misc Checklist

## Description

Misc Penetration Testing usually involves using [netcat](../Tools/netcat.md) to communicate with the given IP and solve a special question. These questions are usually very simple and possibly involve writing python scripts to solve.

## Checklist

For now, we don't differentiate these based on difficulty as most of them don't require high knowledge of penetration testing, rather just some common sense and basic scripting knowledge

### Quick maths

There are many many variations of this, but they usually ask you to solve dozens or hundreds of math questions in impossibly short time. Since we (most likely) can't compute hundreds of very complex math operations in our heads in a matter of seconds, we have to write a Python script.

```python
from pwn import *

# IP of the machine we're talking with
machine_ip = '192.168.0.1'

# Port of the machine we're talking with
machine_port = 80

# Number of questions needed to solve before flag is sent
amount_to_solve = 500              

# Introductory text ending before math question is displayed. Here, we say that after two new lines are sent, we immediately get a line where we parse out numbers and operations
pre_question_delimiter = b':\n\n'

# Ending character on the question line. Here, it would be the equal in "2 + 2 - 1 ="
question_suffix = b'='

# Reads the final output until { is read; outputs the rest. Keep in mind that this skips over any words before it, so if the flag was in format CTF{fl4g_1s_h3r3} or something like that, words "CTF" will be omitted. It's probably easy to use something other than recvuntil to solve this...
flag_prefix = b'{'

def main():
    # Open a session on ip:port
    p = remote(machine_ip, machine_port)

    # Iterate through all questions until a flag gets sent
    for i in range(amount_to_solve):
        # Receive until the line with actual math
        p.recvuntil(pre_question_delimiter)

        # Extract the question out of the line
        question = p.recvuntil(question_suffix)[:-1].strip()

        # Extract the info, solve it and cast it into an int 
        solution = int(util.safeeval.expr(question))

        # Send the line to host
        p.sendline(str(solution).encode())

        # Log for convenience
        log.info('Question {} -> {} = {}'.format(i, question.decode(), solution))

    # Receive flag start
    write(p.recvuntil(flag_prefix)
    log.success(p.recvline())

if __name__ == '__main__':
    main()

```