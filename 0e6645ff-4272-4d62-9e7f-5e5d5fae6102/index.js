const crypto = require('crypto');
const alice = crypto.getDiffieHellman('modp5');
const bob = crypto.getDiffieHellman('modp5');

alice.generateKeys();
bob.generateKeys();

const alice_secret = alice.computeSecret(
    bob.getPublicKey(), null, 'hex'
);
const bob_secret = bob.computeSecret(
    alice.getPublicKey(), null, 'hex'
);

// alice_secret and bob_secret should be the same
console.log(alice_secret == bob_secret);