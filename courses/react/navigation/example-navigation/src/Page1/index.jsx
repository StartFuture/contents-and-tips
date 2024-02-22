import '../assets/style.css';
import logo from '../assets/images/react-logo.svg'
import { Link } from 'react-router-dom';

function PageOne() {
    return (
        <div className="page">
            <div className="page-container" style={{ backgroundColor: "#282c34" }}>
                <h1>TELA 1</h1>
                <img src={logo} className="page-logo animation-1" alt="logo" />

                <Link to="/page-2">
                    <button>Próxima tela</button>
                </Link>
            </div>
        </div>
    );
}

export default PageOne;