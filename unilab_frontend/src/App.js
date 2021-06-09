import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";


import './App.css';
import Login from './components/Login';
import Main from './components/Main';



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
              <Route path={["/", "/users", "/items"]} exact>
                <Main />
              </Route>
            </Switch>
          </Router>
        </div>
      )
  }
}

export default App;