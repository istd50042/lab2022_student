# Lab 6: Diffie-Hellman Key Exchange

**Deadline: 1 July (2359)**

- [Lab 6: Diffie-Hellman Key Exchange](#lab-6-diffie-hellman-key-exchange)
  - [Objectives](#objectives)
  - [Part I: Implementing Square and Multiply](#part-i-implementing-square-and-multiply)
  - [Part II: Diffie-Hellman Key Exchange (DHKE)](#part-ii-diffie-hellman-key-exchange-dhke)
  - [Part III: Baby-Step Giant-Step Method](#part-iii-baby-step-giant-step-method)
  - [Submission](#submission)
    - [eDimension Submission](#edimension-submission)

## Objectives

* Implement Square-Multiply for large integer exponentiation
* Implement Diffie-Hellman Key Exchange
* Implement Shanks' Baby-step Giant-step method

## Part I: Implementing Square and Multiply

Implement square and multiply algorithm to exponentiate large integers efficiently in a computer.

To do exponentiation of <span style="font-family:serif"><i>y</i> = <i>a<sup>x</sup></i> mod <i>n</i></span>, we can use the following algorithm.

```python
square_multiply(a, x, n)
{
  y = 1
  # n_b is the number of bits in x
  for( i = n_b-1 downto 0 )
  {
    # square
    y = y^2 mod n
    # multiply only if the bit of x at i is 1
    if (x_i == 1) y = a*y mod n
  }
  return y
}
```

You are provided `primes_template.py` to use as a starting point. Save it as `primes.py` You will need `square_multiply` for the next section. (it is imported by `dhke_template.py` and `babygiant_template.py`)

## Part II: Diffie-Hellman Key Exchange (DHKE)

DHKE can be used to exchange keys between two parties through insecure channel. For this exercise, you will simulate a exchange of keys using the DHKE protocol, following by sending an encrypted message.

Create a Python script that enables you to do this. Use the provided `dhke_template.py` as a starting point. Submit it as `dhke.py`.

**Set-up**

* Choose a large prime `p`. You can go to [Wolfram Alpha](http://www.wolframalpha.com) and type in "prime closest to 2^80", or any other large number.
* Choose an integer `α` <span style="font-family:serif">∈ 2, 3, . . . , p−2</span>, which is a primitive element or generator in the group
* Save the values of `p` and `α`

**Key Generation**

* We need two sets of public and private keys to simulate the two parties in the key exchange
* Private keys (a, b)
  * Choose a random private key: <span style="font-family:serif">a = k<sub>pr,A</sub> ∈ 2, ... , p-2</span>
  * Choose **another** private key: <span style="font-family:serif">b = k<sub>pr,B</sub> ∈ 2, ... , p-2</span>
* Public keys (A, B)
  * Compute the first public key: <span style="font-family:serif">A = k<sub>pub,A</sub> ≡ α<sup>a</sup> mod p</span>
  * Compute the second public key: <span style="font-family:serif">B = k<sub>pub,B</sub> ≡ α<sup>b</sup> mod p</span>

**Compute Shared Keys**

Exchange your public keys and compute the shared keys: <span style="font-family:serif">k<sub>AB</sub> ≡ B<sup>a</sup> mod p</span>, or <span style="font-family:serif">k<sub>AB</sub> = k ≡ A<sup>b</sup> mod p</span>.

**Message**

Encrypt a message from you (A) using the shared key. You can use any method of encryption with the key. A suggestion is to use PRESENT with ECB mode from the previous lab, and encrypt a text message. Show that the other party (B) can decrypt the message.

Extend the end of the provided template file to print the plaintext, ciphertext to be sent by A, and then the decrypted plaintext by B. 

Answer the following questions as Q1 and Q2 in a text file `ans.txt`:

1. How could we perform the exchange of keys in the real world? Do we need a secure channel? Why or why not?
2. What is an advantage and a disadvantage of DHKE?

## Part III: Baby-Step Giant-Step Method

This section introduces one method for solving discrete logarithm problem from which DHKE is based upon, the [Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step).

An attacker can obtain the key if he can solve the discrete logarithm problem, basically find `x` in <span style="font-family:serif">α<sup>x</sup> = β</span>, where <span style="font-family:serif">1<=x<=p-1</span>. So `α`, `β` are the inputs, we want to find `x`.

We can also write the problem as <span style="font-family:serif">x = log<sub>α</sub> β</span>. 

To do this, the problem is written in a two-digit representation:

<span style="font-family:serif">x = x<sub>g</sub>m − x<sub>b</sub></span>

Where <span style="font-family:serif">0 ≤ x<sub>g</sub>, x<sub>b</sub></span>. In this way, we can write the exponentation as:

<span style="font-family:serif">β = α<sup>x</sup> = α<sup>x<sub>g</sub>m−x<sub>b</sub></sup></span>

Rearranging the terms, we get:

<span style="font-family:serif">βα<sup>x<sub>b</sub></sup> = α<sup>x<sub>g</sub>m</sup></span>

**Task 1**

Create a Python script to do the following:

* Calculate `m = ceiling(sqrt(|G|))`, i.e. size of the square root of the order of the finite cyclic group G, where group order is `p-1`.
* Baby-step phase: Compute and store into a file the values of <span style="font-family:serif">α<sup>x<sub>b</sub></sup>β</span>, where <span style="font-family:serif">0 ≤ x<sub>b</sub> < m</span>
* Giant-step phase: Compute and store into a file the values of <span style="font-family:serif">α<sup>m×x<sub>g</sub></sup></span>, where <span style="font-family:serif">0 ≤ x<sub>g</sub> < m</span>
* Check the two list and see if there is a match such that: <span style="font-family:serif">α<sup>x<sub>b</sub></sup>β = α<sup>m×x<sub>g</sub></sup></span>
* If a match is found, calculate <span style="font-family:serif">x = x<sub>g</sub>m − x<sub>b</sub></span>

Use the provided `babygiant_template.py` as a starting point. Submit it as `babygiant.py`.

**Task 2**

1. Try to attack DHKE with Baby-Step Giant-Steps method. Start with a key size of 16 bits. (a key with 16 bits has a small maximum value of 2^16, or 65536) Increase the number of bits (of the key) to break slowly, to increase the difficulty of the attack. Note where the attack fails or is too hard to execute. 
2. To avoid attack using Baby-Step Giant-Steps method, how many bits would you set the key be in DHKE protocol? How did you decide on this number? Answer as Q3 in `ans.txt`

**Attack Procedure**

As the attacker, we start with private keys (a, b) which are unknown, and the public keys (A, B) which are known. Our goal is to guess the shared keys correctly without knowledge of the private keys. 

1. We take `p` and `α` (from the setup step) and a public key as inputs to the Baby-Step Giant-Steps algorithm. The inputs should be `(α, β, p)`, where `β` is the public key of interest. 
2. Perform the Baby-Step Giant-Steps algorithm, allowing us to derive a guess of `x`.
3. To get the guess of shared key (of the public key and the unknown private key), we perform a square_multiply of the public key and our guess of `x`.
4. To check if this is correct, we compute the real shared key from the public and private key. (Obviously, the real attacker cannot do this, but you can to check the correctness in this exercise).

## Submission

### eDimension Submission

Submission ground rules:

* Please make sure to indicate your name and student ID in each of the graded submission files
* You are allowed to collaborate with **one** other student. If you choose to do so, both of your name/student ID should be indicated in the submission files. Both are still required to submit the files individually. 
* Except for within each pair of students that are collaborating, you are not allowed to share answers and solutions.

Lab 6 submission:
  
Upload a zip file with the following: file name format: lab6_name_studentid_cohortnumber (cohortnumber 0/1, 0 for thursday lab, 1 for friday lab)

Upload a **zip file** with the following:

* `primes.py`
* `dhke.py`
* `babygiant.py`
* `ans.txt`

**Deadline: 1 July(2359)**
