import React, { useState } from 'react';
import { getFirestore, collection, addDoc } from 'firebase/firestore';

const firestore = getFirestore();
const usersCollection = collection(firestore, 'users');

function SignUp() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addDoc(usersCollection, { name, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Name:</label>
      <input
        type="text"
        id="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br />
      <label htmlFor="email">Email:</label>
      <input
        type="email"
        id="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <br />
      <button type="submit">Sign Up</button>
    </form>
  );
}

export default SignUp;