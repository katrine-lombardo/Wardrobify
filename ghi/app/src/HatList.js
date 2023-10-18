import React, { useEffect, useState } from 'react';

function HatList() {

  const [hats, setHats] = useState([])
  const fetchData = async () => {
    const url = "http://localhost:8090/api/hats/";
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setHats(data.hats);
    }
  }


  async function handleClick(e) {
    const request = await fetch(`http://localhost:8090/api/hats/${e.target.id}`, {
    method: "DELETE",
    });

    const resp = await request.json();

    if (resp.deleted) {
      alert("Deleted Item");
      fetchData();
    } else {
      alert("Could Not Delete Item");
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  if (!hats) {
    return <div>Loading hats...</div>
  }


    return (
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Style</th>
            <th>Color</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {hats.map(hat => {
            return (
              <tr key={hat.id}>
                <td>{ hat.style }</td>
                <td>{ hat.color }</td>
                <td><button onClick={handleClick} id={hat.id} className="btn btn-danger">Delete</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }

  export default HatList;
