# Docker

To build the docker container, you need to run the following command in the challenge directory:

```docker build -t booleanwonderland .``` 

To run the container, you use the following command:

```docker run -d -p 2222:22 --name booleanwonderland booleanwonderland``` 

Finally, to connect to the container by ssh and do the challenge, you run the following:

```ssh ctfuser@localhost -p 2222``` 

ctfuser's password is: `nowel`. 

# Challenge

To start the challenge, you need to go in the challenge directory and cat the README file there. It will say that you should run the following command:

```sudo python3 /root/booleanWonderland.py``` 

That way, the ctfuser can launch the challenge without being able to read the python script and see what's inside. 

The challenge is about boolean algebra and cryptography. You need to solve 3 boolean logic circuits to get the flag. There is a help command you can use in the challenge that will tell you what you can do to advance the challenge. Once you solve one circuit, you can see the next one and solve it then. Once you've solved the third one, the flag will be printed and the program will exit. 

# Solution 

For the first circuit, you only need to solve it by calling solveCircuit1 11000011.

For the second circuit, the wires are missing, so you need to call showCircuit2 with the right argument to show them and solve the circuit. The right argument is printed just after you solve the first circuit. It's a string that represents "cesarsalad" in 20-shifted cesar code. So calling showCircuit2 cesarsalad will reveal the wires. Then you can call solveCircuit2 00110011 to solve the second circuit.

For the third circuit, the wires are missing again. There is something printed after you solve the second circuit "ilikebooleanlogic cesar". When typing help, you see that to get the right argument for showCircuit3, you should lookup a certain website. This is a kattis problem about leapfrog encryption. Following the demonstration of the encryption algorithm in the problem's description, you can encrypt ilikebooleanlogic with the key cesar. The result is cbaiieglleoiolokn and when you give this as an argument to showCircuit3, the wires will appear. You then call solveCircuit3 00000001 to solve the last circuit and get the flag.
