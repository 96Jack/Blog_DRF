import axios from 'axios';

export default class UserService{
    login(username, password){
        console.log("go down", username, password);// ajax axios xmlhttprequest
        // TODO
        axios.post('/user/login',{
            username, password
        }).then(function (response){
            console.log(response);
        },function (error){
            console.log(error)
        });
        console.log('处理完了？')


    }
}
