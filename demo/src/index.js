import React from 'react';
import {render} from 'react-dom';

import {
  BrowserRouter as Router,
  Link,
  Route,
  Switch
}from 'react-router-dom';

import login from './component/login';
import reg from './component/reg'

// function About(){
//   return <h2>About</h2>;
// }

function Home(){
  return <h2>Home</h2>;
}

class App extends React.Component{
  render(){
    return <Router>
      <div>
      <ul>
        <li><Link to='/'>主页</Link></li>
        <li><Link to='/login'>登录</Link></li>
        <li><Link to='/reg'>注册</Link></li>
        <li><Link to='/about'>关于</Link></li>
      </ul>
      <Switch>
      <Route path='/login' component={login}></Route>
      <Route path='/reg' component={reg}></Route>
      <Route path='/' component={Home}></Route>
      </Switch>
      </div>
    </Router>
  }
}


render(<App/>, document.getElementById('root'));



// import './App.css';
// import Product from './component/Product'
// import ProductDetails from './component/ProductDetails'

// import {
//   BrowserRouter as Router,
//   Routes,
//   Route
// } from "react-router-dom"

// function App(){
//   return (
//     <Router>
//       <Routes>
//         <Route path="/product/*" element={<Product/>}/>
//         <Route path="/product/:id" element={<ProductDetails/>}/>
//       </Routes>
//     </Router>
//   );
// }

// export default App;




// 
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
