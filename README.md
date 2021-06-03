# Random-In-Python

Check Out Jackie Wilson's video on Real Python about Generating Random Data in Python [here](https://realpython.com/courses/generating-random-data-python/)

Python provides the random module, witch is a Pseduo random number generator (PRNG)
Pseudo random means not actually random.
A true random number generator (TRNG) typically involves hardware.
L>Ex: rolling dice in real life
What makes the random module pseudo-random is that is it written in software
which can be seeded and implies deterministic qualities
L>We can recreate and predict the generated sequence of random values
Data generated from random are produced from a seed
The seed is like the starting point to get the random generation going
When you invoke the random methods, the random method had to come up with its
own seed--typically, your system time.
It then used that seed in an algorithm to generate the values.
Within the random module is also a method called random()
L>random.random generates a float equal to or greater than 0.0 but less than 
1.0. -> [0,1) -> 0<= n < 1.0
Under the hood, random uses an algorithm known as Mersenne Twister.
While it's convenient that the random module can seed off of system time,
sometimes you will want to repeat a random sequence for testing
L> For this purpose, there is the random.seed() method
Simple pass this method an integer argument and random will use that the seed.
You may also pass the seed method a string, bytes, or bytearray and those values
will be converted to an integer before seeding. 

If you only need a single random value or even a small sequence, standard library's
random is usually the faster and better option. 

NumPy is specialized for building large, multi-dimensional arrays. You can build random
statistical models with this library

PRNG's are good for simulation but not good for security.

How does randomness help secure data? -> It helps us hide it.

Crypotgraphically Secure Pseudo Random Number Generator
Achieves secure randomness through entropy(a choatic state that is difficult to predict
and usually found in nature) and size(computers can only compute numbers of a certain size)
L>secrets and uuid are modules in Python that provide CSPRNG
L>both modules get entropy from the operating system through
the os module's os.urandom() method.

secrets is basically a wrapper around os.urandom() method (see osRandomSecure.png)
secrets exports a handful of functions of generating random numbers, bytes, and strings.

See randomSecrets.png

Another module from the standard library is uuid -> universally unique Identifier
L>128 bits/ 16 bytes
Within the uuid module is a method called uuid4(), which is considered secure

uuid.uuid4() returns an object of the uuid class


Hashing is not random. It's an algorithm that produces one-way fixed-size string from a given input
L>A hash function will always produce the same string if given that same input
Its value is that it's not reversible and can be used to verify digital integrity
Some applications store hashes of user passwords so they can avoid storing plaintext passwords.
People put in password and that password gets hashed to some value in the data base.
A single hashing of the password is not secure enough for user passwords because it's trivial to 
generate what's known as a rainbow table (a look up guide for common words and their hashed equivalents)
L> to safe guard against this, it's common for systems to repeat, or salt, the hash.
Salting the hash means adding some extra data to the original before it's hashed
L>sometimes that salt is generated randomly, but hashing and randomness are not related.

Recap
PSL random (PRNG)
numpy.random (PRNG)
os.urandom() (CSPRGN)
secrets (SCPRNG)
uuid (SCPRNG)
