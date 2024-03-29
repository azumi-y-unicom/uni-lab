import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from "react-router-dom";
import Header from '../components/Header';
import Users from '../components/Users'
import Labs from './Labs'
import Deck from './Deck'


const Main = (props) =>{
  return (
    <div className="win">
      <Header />
      <div className="main-veiw">
        <Router>
          <Switch>
            <Route path="/" exact>
              <div>Main</div>
            </Route>
            <Route path="/labs" exact>
              <Labs />
            </Route>
            <Route path="/deck" exact>
              <Deck />
            </Route>
          </Switch>
        </Router>
      </div>
    {/* リダイレクト機能追加予定 */}
    </div>
  );
};

export default Main;