import '../assets/style.css';
import logo from '../assets/images/react-logo.svg'
import { Link } from 'react-router-dom';

function PageThree() {
    return (
        <div className="page">
            <div className="page-container" style={{ backgroundColor: "brown" }}>
                <h1>TELA 3</h1>
                <img src={logo} className="page-logo animation-3" alt="logo"/>
                <Link to="/">
                <button>Tela inicial</button>
                </Link>
            </div>
        </div>
    );
}

export default PageThree;