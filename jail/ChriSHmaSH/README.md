# ChriSHmaSH

# Concept

This is a hard challenge. You will fall into a jail that is uppercasing all the commands you give to it and on top of that, the path have been mmodified so you do not have access to the `/bin` folder. You have to find a way to write the command in lowercase but also preprending a path on top of them to make them run. __Bruteforcing is not part of the plan__.

# How to run
Just spin up the container by building the image in a simple docker compose file, forwarding the port 22 to whatever available host port (see the docker compose file provided).

# Solution

## Step 1: Environment variables
You should have guessed that you can get out of that using common environment variables. `env` command will not work so you have to fully assume some variables can be there, you cat test the environment variable by playing around with the shell:

```
Santa-shell> $USER
/bin/sh: 1: bauble: not found
```
Then you have to rely on errors provided by `sh` to see if a variable is existing or not (trying with non existing variables will not return any error). By this time you should look at the most common variable used in operating systems: PATH.

```
Santa-shell> $PATH
/bin/sh: 1: /usr/local/bin:/usr/bin:/usr/games:/bin/anothersh: not found
```
As you can see the $PATH variable does not contain `/bin` but something unusual: `/bin/anothersh` that could be interesting

## Step 2: Shell parameter expansion
The second thing that should come to your mind is "okay, I can now generate lowercases using environment variables, now I have to find a way to manipulate them so they can make what I want and eventually form the string /bin/bash, /bin/sh or whatever shell that will be executed as a command and could get me out of here". So you have to know about shell parameter expansion. BUT THERE'S A CATCH ! The jail we are using is using `sh` as a subshell, not `bash`, and while `bash` have a full extensive shell parameter expansion where you can slice strings, replace them etc. `sh` does not. So you have to find about shell parameter expansions that are POSIX compliant. You might ending up knowing or learning that `sh` only support the following shell parameters expansions: 
- `${var#pattern}`: Removes the shortest match of pattern as a prefix.
- `${var##pattern}`: Removes the longest match of pattern as a prefix.
- `${var%pattern}`: Removes the shortest match of pattern as a suffix.
- `${var%%pattern}`: Removes the longest match of pattern as a suffix.

Here is how you could experiment:
```
Santa-shell> ${PATH%%:*}
/bin/sh: 1: /usr/local/bin: Permission denied
```
here we just cut out the string to be the first path of $PATH

So now you have to figure out a way to remove prefix or suffix of let's say $PATH, by the way you might be tempted to remove all the prefix of $PATH to try to use "/bin/anothersh" which seems to be another shell. But there is also another catch, you cannot really write a pattern made out of strings as they will also get uppercased. This is where you have to think about wildcards and characters that does not have any uppercasing such as dots, slashes, undescores, etc. On top of that you may also find that you can use the wildcards "*" (every characters) and "?" a single character. 

## Step 3: anothersh

So you finally come up with this pattern to cut $PATH and it works:
```
Santa-shell> ${PATH##/*/?????:}               
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
(it is not that simple, but you are on the right track,
here's a hint, there is a symlink to bash in /usr/local/bin)
```

It is actually a decoy to attract your attention with a hint inside. As deep as you could be in this challenge, you know know that you should find a way to execute `bash` as you now know its location.

## Step 4: breaking the jail

After a bit of mindbreaking you might end up with something like this:
- Cutting the first part of $PATH with `${PATH%%:*}`
- The username is baulbe and it hasn't been randomly choosen, you can extract "ba" using `${USER%%????}`
- Finally you need the string `sh`, how convenient is it that \$PATH end up by that string ? `${PATH##/*/*/*/*/*/*/*/*/???????}`  

So you need to assemble everything into a nice string:
``${PATH%%:*}/${USER%%????}${PATH##/*/*/*/*/*/*/*/*/????????}``
And:
```
Santa-shell> ${PATH%%:*}/${USER%%????}${PATH##/*/*/*/*/*/*/*/*/???????}
bauble@8d458b13600c:~$
```
You broke the jail. As written in the statement, the flag will be in the home directory
```
bauble@8d458b13600c:~$ cat flag.txt 
CONGRATULATIONS
Unless you found a shortcut, this was a tough one. 

Here is your well deserved flag:
flag{WHY_4RE_Y0U_S0_L0UD_?}
```

The patterns might be shortten and not unique as a solution, everyone can come with their workaround to assemble the playload. 



