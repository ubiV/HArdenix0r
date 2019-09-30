**Hardenix0r**

Hardenix0r is a Python (3.6) script developed for hardening purpouses.

It's a WIP project so it will not run smoothly (yet).

It uses a json file (under ./data/$os.json) where all the scripts are stored. 
(pay attention to command injection though!)

Every command expects 2 kinds of responsens in order to determine it' applicability:

- String: It means that if the command returns "Yes", "1", "oooooh yeaaaah", the response will be matched exactly
- Regex: if the response is complex, you can add a regex to match the response you are interested in.

It must be executed privileged and...Sorry if it will break your computer.

Bye.