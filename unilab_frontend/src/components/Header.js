import { Navbar, Nav, NavDropdown } from 'react-bootstrap'

export const getOnMessage= (e) =>{
  e.preventDefault();
  alert("Now At Work");
}

export const getOnLogout= (e) =>{
  e.preventDefault();
  alert("Coming Soon!!");
}

const Header = (props) =>{
  return (
    <Navbar className="bg-unilab  mr-auto" variant="light">
      <Navbar.Brand href="/" className="">UniLab</Navbar.Brand>
      <Nav className="mr-auto">
        <Nav.Link href="/">ホーム</Nav.Link>
        <Nav.Link href="/items">ファイル管理</Nav.Link>
        <NavDropdown title="管理者機能" id="collasible-nav-dropdown">
          <NavDropdown.Item href="/users">ユーザー管理</NavDropdown.Item>
          <NavDropdown.Divider />
        </NavDropdown>
      </Nav>
      <Nav className="nav-right">
        <NavDropdown title="＜ユーザー名＞" id="collasible-nav-dropdown">
          <NavDropdown.Item onClick={getOnMessage}>アカウント設定</NavDropdown.Item>
          <NavDropdown.Divider />
          <NavDropdown.Item onClick={getOnLogout}>ログアウト</NavDropdown.Item>
        </NavDropdown>
      </Nav>
    </Navbar>
  );
};
  
export default Header;