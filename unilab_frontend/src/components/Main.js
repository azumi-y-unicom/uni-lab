import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from "react-router-dom";
import Header from './Header';
import Users from './Users'

const sampeName = "ほげ";

const Main = (props) =>{
    return (
        <div>
            <Header />
            <Router>
            <Switch>
                <Route path="/" exact>
                    <div>Main</div>
                </Route>
                <Route path="/items" exact>
                    <div>items</div>
                </Route>
                <Route path="/users" exact>
                    <Users />
                </Route>
            </Switch>
        </Router>
{/* リダイレクト機能追加予定 */}
        </div>
    );
};
    
export default Main;