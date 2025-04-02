import React, { useState } from "react";

function MyForm() {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      setItems([...items, input]);
      setInput("");
    }
  };

  const handleRemove = (indexToRemove) => {
    setItems(items.filter((_, index) => index !== indexToRemove));
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Add Items to the List</h3>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter item"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>

      {items.length === 0 ? (
        <p>No items added yet.</p>
      ) : (
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              {item}{" "}
              <button onClick={() => handleRemove(index)}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MyForm;
