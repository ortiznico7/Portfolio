import React from 'react'
import "./styles.css";
import Card from "./Components/card";
import ReactDOM from "react-dom";
import MyForm from "./MyForm";

function App() {
  return (
    <div className="App">
      <Card Name="Nico" IDNum="06902" CBalance="$90,000"/>
      <Card Name="Kei" IDNum="06903" CBalance="$45,902"/>
      <Card Name="Shay" IDNum="06904" CBalance="$93,293"/> 
      <Card Name="Kat" IDNum="06905" CBalance="52,384"/>
      <Card Name="Dorian" IDNum="06906" CBalance="$66,666"/> 
      <Card Name="Lorraine" IDNum="06907" CBalance="$34,288"/>
      <Card Name="Maria" IDNum="06908" CBalance="$9,203"/>
      <MyForm />
    </div>
  );
}


export default App