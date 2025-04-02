import React from "react";
import "./Card.css";

function Card ({ Name, IDNum, CBalance }) {
    return (
        <div className="card">
            <img 
            src="https://cdn-icons-png.flaticon.com/512/7049/7049216.png" 
            width="200px"
            alt="Coins & Money Bag"
            class=""
            />
            <h1>{Name}</h1>
            <p>{IDNum}</p>
            <p>{CBalance}</p>
        </div>
    )
}
export default Card 