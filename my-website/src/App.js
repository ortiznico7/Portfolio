import "./styles.css";
import Card from "./Components/Card";

export default function App() {
  return (
    <div className="App">
      <Card Name="Credit Score" Description="Excellent!" />
      <Card Name="Money in Checking" Description="Excellent!" />
      <Card
        Name="Money in Saving"
        Description="We recommend you put some more money in your Saving account."
      />
      <Card
        Name="Investments"
        Description="We recommend you reach out to our investing team."
      />
    </div>
  );
}
