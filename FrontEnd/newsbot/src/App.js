import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./Pages/MainPage";
import Admin from "./Pages/Admin";
import Table from "./Pages/Table";


export default function App() {
  return (
      <Routes>
        <Route path="/" element={<MainPage />}/>
        <Route path="/admin" element={<Admin/>} />
        <Route path="/table" element={<Table/>} />
      </Routes>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);