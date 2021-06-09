const onLogin = (e) =>{
    e.preventDefault();
    alert("Comming Soon");
};

const Login = () =>{
    return (
        <div><div className="login-inner-frame">
            <h1>Hoge Login</h1>
            <form method="post"  onSubmit={onLogin}>
                <div className="login-area">
                    <div className="input-area"><input type="text" id="" name="userId" placeholder="ユーザーID"/></div>
                    <div className="input-area"><input type="password" id="" name="password" placeholder="パスワード"/></div>
                    <div style={{textalign:'left'}}>Todo：チェックボックス</div>
                </div>
                <div className="login-area"><button type="submit">Login</button></div>
            </form>
        </div></div>
    );
};

export default Login;