import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import FormsTest from './pages/FormsTest';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/formTest" exact component={FormsTest} />
      </Switch>
    </Router>
  );
}

export default App;