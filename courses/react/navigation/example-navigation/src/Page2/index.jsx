import '../assets/style.css';
import logo from '../assets/images/react-logo.svg'
import { useNavigate } from 'react-router-dom';

function PageTwo() {
    const navigation = useNavigate();

    const handlerNextScreen = () => {
        navigation("/page-3")
    }

    return (
        <div className="page">
            <div className="page-container" style={{ backgroundColor: "darkGreen" }}>
                <h1>TELA 2</h1>
                <img src={logo} className="page-logo animation-2" alt="logo" />
                <button onClick={handlerNextScreen}>Próxima tela</button>
            </div>
        </div>
    );
}

export default PageTwo;