import React, { useEffect, useState } from 'react';

function App() {
  const [members, setMembers] = useState([]);

  // Mengambil data member dari API
  useEffect(() => {
    fetch('http://127.0.0.1:5000/members')
      .then((response) => response.json())
      .then((data) => setMembers(data))
      .catch((error) => console.error('Error fetching members:', error));
  }, []);

  return (
    <div>
      <h1>Member List</h1>
      <ul>
        {members.length > 0 ? (
          members.map((member) => (
            <li key={member.id}>
              {member.name} - {member.email}
            </li>
          ))
        ) : (
          <li>No members found</li>
        )}
      </ul>
    </div>
  );
}

export default App;
