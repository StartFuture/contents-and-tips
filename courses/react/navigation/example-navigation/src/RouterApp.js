import { BrowserRouter, Route, Routes } from "react-router-dom";
import PageOne from './Page1'
import PageTwo from './Page2'
import PageThree from './Page3'
import Page404 from './Page404'

function RouterApp() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" Component={PageOne}/>
                <Route path="/page-2" Component={PageTwo}/>
                <Route path="/page-3" Component={PageThree}/>
                <Route path="*" Component={Page404}/>
            </Routes>
        </BrowserRouter>
    );
}

export default RouterApp;