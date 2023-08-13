import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Login} from "./component/login";
import {Signup} from "./component/signup";
import {Home} from "./component/Home";
import {Navigation} from './component/navigation';
import {Logout} from './component/logout';
function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/signup" element={<Signup/>}/>
            <Route path="/logout" element={<Logout/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;
