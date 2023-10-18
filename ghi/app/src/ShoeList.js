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
  useEffect(() => {
    fetchData();
  }, []);

  if (!shoes) {
    return <div>Loading shoes...</div>;
  }

  async function loadData() {
    const request = await fetch("http://localhost:8080/api/shoes/");
    const resp = await request.json();

    setShoes(resp.Shoes);
  }

  async function handleClick(e) {
    const id = e.target.id;
    const request = await fetch("http://localhost:8080/api/shoes/", {
      method: "DELETE",
    });

    const resp = await request.json();
    console.log(e.target);

    if (resp.delete) {
      alert("Delete Item");
    } else {
      alert("Could Not Delete Item");
    }
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
        {shoes.map(shoe => {
          return (
            <tr key={shoe.id}>
              <td>{ shoe.picture_url }</td>
              <td>{ shoe.id }</td>
              <td>{ shoe.model_name }</td>
              <td>{ shoe.bin }</td>
              <td><button onClick={handleClick} id={shoe.id} className="btn btn-danger">Delete</button></td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default ShoeList;
