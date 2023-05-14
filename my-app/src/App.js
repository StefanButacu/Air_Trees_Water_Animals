import logo from './logo.svg';
import './App.css';
import {useState} from "react";
import axios from 'axios';
import Romania from './assets/romania.svg';
import Romania_HOT from './assets/ro_canicula.jpg';
import Romania_COLD from './assets/ro_ger.jpg';

const baseURL = "http://localhost:5000/predict"

function App() {

    const [month, setMonth] = useState(1)
    const [year, setYear] = useState(1950)
    const [prediction, setPrediction] = useState(undefined);

    const handlePredictButton = () => {
        axios.get(`${baseURL}?month=${month}&year=${year}`)
            .then(response => setPrediction(response.data))
            .catch(err => alert(err))
    }

    return (
        <div className="App">
            <header className="App-header">
                Metode de Inteligenta Artificiala in schimbarea climatica
            </header>

            <div style={{padding: "30px"}}>
                <img src={Romania} alt="Romania Logo" width={"20%"} height={"20%"}/>
                <div style={{padding: "10px"}}>
                    <label htmlFor={"month"}>Enter Month: </label>
                    <input id="month" type="number" max={"12"} value={month} onChange={(ev) => {
                        setMonth(parseInt(ev.target.value));
                    }}/>
                </div>
                <div>
                    <label htmlFor={"year"}>Enter Year: </label>
                    <input id="year" type="number" max={"2050"} value={year} onChange={(ev) => {
                        setYear(parseInt(ev.target.value))
                    }}/>
                </div>
                <button onClick={handlePredictButton}>
                    Predict
                </button>
            </div>
            {
                prediction ? (<div
                    style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}}>

                    Temperature change for Romania is {prediction}
                    {
                        prediction < 0 ? (<img src={Romania_COLD} width={"20%"} height={"20%"} alt={"COLD"}/>)
                            :
                            (<img src={Romania_HOT} width={"20%"} height={"20%"} alt={"COLD"}/>)
                    }

                </div>) : (<></>)
            }
        </div>
    )
}

export default App;
