import React, { useEffect, useState } from "react";

function ShoeList() {
  const [shoes, setShoes] = useState([]);
  const fetchData = async () => {
    const url = "http://localhost:8080/api/shoes/";
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setShoes(data.shoes);
    }
  };

  async function handleClick(e, shoeId) {
    const response = await fetch(
      `http://localhost:8080/api/shoes/${e.shoeId}`,
      {
        method: "DELETE",
      }
    );
    if (response.ok) {
      alert("Delete Item");
      fetchData();
    } else {
      alert("Could Not Delete Item");
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  if (!shoes) {
    return <div>Loading shoes...</div>;
  }

  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Photo</th>
          <th>ID</th>
          <th>Model Name</th>
          <th>Bin</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {shoes.map((shoe, index) => {
          return (
            <tr key={index}>
              <td>
                <img
                  src={shoe.picture_url}
                  className="img-thumbnail"
                  style={{ height: "70px", width: "70px" }}
                />
              </td>
              <td>{shoe.id}</td>
              <td>{shoe.model_name}</td>
              <td>{shoe.bin.closet_name}</td>
              <td>
                <button
                  onClick={(e) => handleClick(e, shoe.id)}
                  className="btn btn-danger"
                >
                  Delete
                </button>
              </td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default ShoeList;
