# pyotp-mfa
Python script to generate MFA OTP using pyotp module

## Prerequisite
 - Following python modules needs to be installed.
 - You can install the modules by running ```pip3 install <module_name> --user```

	1. pyotp
	2. time
	3. sys
	4. os
	5. termcolor 


# Usage

```
ubuntu@ubuntu1:~$ ./mfa.py 
Enter base32 secret key: <MFA SECRET KEY>

New OTP will be generated every 30 Seconds. Press Ctrl+C to exit

Current OTP is: 939953

Current OTP is: 247189


^CBye!
ubuntu@ubuntu1:~$ 
```
