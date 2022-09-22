import React from 'react';
import { Link } from 'react-router-dom';
import "../css/login.css"

export default class login extends React.Component{
    render() {
        return (<div className="login-page">
        <div className="form">
          <form className="register-form">
            <input type="text" placeholder="用户名称"/>
            <input type="text" placeholder="电子邮箱"/>
            <input type="password" placeholder="用户密码"/>
            <input type="password" placeholder="确认密码"/>
            <button>注册</button>
            <p className="message">已经注册，<Link to='/login'>请登录</Link></p>
          </form>
        </div>
      </div>
        );
    }
}