ElGamal Cryptosystem

Implementation of the ElGamal public-key encryption, decryption and signature schemes, based on the discrete logarithm problem.

ElGamal is a public-key encryption system that enables anyone to encrypt messages for a recipient, but only the recipient (who holds the private key) can decrypt.

Why Learn ElGamal?

-Foundational: One of the first public-key encryption schemes (1985)
-Discrete Log: Demonstrates why discrete logarithm hardness matters
-ZK Connection: Forms basis for zero-knowledge protocols on discrete log
-MPC Relevance: Used in threshold cryptography schemes (e.g., threshold signatures)
-Homomorphic: Has additive homomorphic properties (useful in advanced protocols)


Common Mistakes: to Avoid the followings

-Reusing randomness: Each encryption must use fresh random r
-Small parameters: Use 2048+ bit primes in practice
-Not verifying parameters: Verify g is generator, p is prime
-Weak randomness: Use cryptographically secure RNG


The implementation presented here are for practice and illustration, therefore, we used small primes (and we assumed they are primes). In practice, one should avoid the common mistakes that we pointed out.
