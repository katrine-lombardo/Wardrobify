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


  async function handleClick(e, hatId) {
    const request = await fetch(`http://localhost:8090/api/hats/${hatId}`, {
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
            <th>Image</th>
            <th>Location</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {hats.map(hat => {
            return (
              <tr key={hat.id}>
                <td>{ hat.style }</td>
                <td>{ hat.color }</td>
                <td>
                    <img src={ hat.picture_url } className="img-thumbnail" style={{height:"50px", width:"50px"}}/>
                </td>
                <td>{ hat.location }</td>
                <td><button onClick={(e) => handleClick(e, hat.id)} id={hat.id} className="btn btn-danger">Delete</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }

  export default HatList;
