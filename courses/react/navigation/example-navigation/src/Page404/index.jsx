import { Link } from "react-router-dom";

function Page404() {
    return (
        <div className="page">
            <div className="page-container" style={{ backgroundColor: "#282c34" }}>
                <h1>ERROR 404 - PÁGINA NÃO ENCONTRADA</h1>
                <Link to="/">
                    <button>Voltar a tela inicial</button>
                </Link>
            </div>
        </div>
    );
}

export default Page404;