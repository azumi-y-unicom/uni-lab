import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";


import './App.css';
import Login from './pages/Login';
import Main from './pages/Main';



export class App extends React.Component {
  // ログイン画面風サンプル
  render() {
    return (
        <div className="App">
          <Router>
            <Switch>
              <Route path="/login">
                <Login />
              </Route>
              <Route path={["/", "/labs", "/deck"]} exact>
                <Main />
              </Route>
            </Switch>
          </Router>
        </div>
      )
  }
}

export default App;