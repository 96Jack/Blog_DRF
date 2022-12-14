import React from 'react';
import { Link } from 'react-router-dom';
import "../css/login.css"
import UserService from '../service/user';


const service = new UserService();

export default class Login extends React.Component{
  render(){
    return <Log_in service={service}/>; 
  }
}

class Log_in extends React.Component{
    handleClick(event){
        event.preventDefault(); //阻止提交
        console.log('clicked')
        const [username, password] = event.target.form;
        // console.log(username.value, password.value);
        this.props.service.login(username.value, password.value);
      }
    render() {
        return (<div className="login-page">
        <div className="form">
          <form className="login-form">
            <input type="text" placeholder="用户名"/>
            <input type="password" placeholder="密码"/>
            <button onClick={this.handleClick.bind(this)}>登录</button>
            <p className="message">还未注册? <Link to='/reg'>请注册</Link></p>
          </form>
        </div>
      </div>
        );
    }
}