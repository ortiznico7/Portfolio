import React, { useState } from "react";

function MyForm() {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState("");

  // ✅ Handle form submit
  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      setItems([...items, input]);
      setInput("");
    }
  };

  // ✅ Handle remove button
  const handleRemove = (indexToRemove) => {
    setItems(items.filter((_, index) => index !== indexToRemove));
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Add Items to the List</h3>

      {/* ✅ Form */}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter item"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>

      {/* ✅ Conditional Rendering */}
      {items.length === 0 ? (
        <p>No items added yet.</p>
      ) : (
        <ul>
          {/* ✅ List Rendering with Event */}
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
