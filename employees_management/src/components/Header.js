import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

const Header = () => {
  return (
    <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Administración de empleados KSP</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/">Empleados</Nav.Link>
            {/* <Nav.Link href="/add">Registro de empleados</Nav.Link> */}
            <Nav.Link href="/beneficiaries">Beneficiarios</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
  );
};

export default Header;