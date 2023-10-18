import React, { useEffect, useState } from "react";

function HatForm() {
  const [locations, setLocations] = useState([]);
  const [formData, setFormData] = useState({
    fabric: "",
    style: "",
    color: "",
    picture_url: "",
    location: "",
  });
  const fetchData = async () => {
    const url = "http://localhost:8100/api/locations";
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setLocations(data.locations);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = "http://localhost:8090/api/hats/";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(formData),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(url, fetchConfig);

    if (response.ok) {
      setFormData({
        fabric: "",
        style: "",
        color: "",
        picture_url: "",
        location: "",
      });
    }
  };
  const handleFormChange = (e) => {
    const value = e.target.value;
    const inputName = e.target.name;
    setFormData({
      ...formData,
      [inputName]: value,
    });
  };

  return (
    <div className="container">
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Create A New Hat</h1>
            <form onSubmit={handleSubmit} id="create-hat-form">
              <div className="form-floating mb-3">
                <input
                  value={formData.style}
                  onChange={handleFormChange}
                  placeholder="Style"
                  required
                  type="text"
                  name="style"
                  id="style"
                  className="form-control"
                />
                <label htmlFor="style">Style</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  value={formData.fabric}
                  onChange={handleFormChange}
                  placeholder="Fabric"
                  required
                  type="text"
                  name="fabric"
                  id="fabric"
                  className="form-control"
                />
                <label htmlFor="fabric">Fabric</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  value={formData.color}
                  onChange={handleFormChange}
                  placeholder="Color"
                  required
                  type="text"
                  name="color"
                  id="color"
                  className="form-control"
                />
                <label htmlFor="color">Color</label>
              </div>
              <div className="mb-3">
                <select
                  value={formData.location}
                  onChange={handleFormChange}
                  required
                  name="location"
                  id="location"
                  className="form-select"
                >
                  <option value="">Choose A Location</option>
                  {locations.map((location) => {
                    return (
                      <option key={location.id} value={location.id}>
                        {location.closet_name}
                      </option>
                    );
                  })}
                </select>
              </div>
              <div className="form-floating mb-3">
                <input
                  value={formData.picture_url}
                  onChange={handleFormChange}
                  placeholder="Picture_URL"
                  required
                  type="url"
                  name="picture_url"
                  id="picture_url"
                  className="form-control"
                />
                <label htmlFor="picture_url">Image URL</label>
              </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HatForm;
