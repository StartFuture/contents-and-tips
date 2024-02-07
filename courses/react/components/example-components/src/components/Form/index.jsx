import './assets/style.css'

function Form() {
    return (
        <>
            <div className="session_grid">
                <div className="forms_container">
                    <h1>
                        Nos informe mais sobre você :)
                    </h1>

                    <form className="input_forms">
                        <input type="text" id="name" name="name" required placeholder="Nome completo" />

                        <input type="email" id="email" name="email" required placeholder="E-mail" />

                        <button>
                            Prosseguir
                        </button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default Form;