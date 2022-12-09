import React from 'react';
import { Table,Button, Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import Moment from 'react-moment';

const EmployeesGrid = () => {
  const [employeesList, setEmployeesList] = React.useState([]);

  // obtiene el listado de empleados
  React.useEffect(() => {
    axios.get("http://localhost:8000/employees/?skip=0&limit=100").then((response) => {
      setEmployeesList(response.data);
    });
  }, []);

  return (
    <div>
      <Container>
        <Row>
          <Col><h3>Empleados</h3></Col>
          <Col md="auto"><Button href="/add" variant="primary">Registrar Empleado</Button></Col>
          <Col md="auto"><Button variant="success">Exportar</Button></Col>
        </Row>
      </Container>
      <div className="table-wrapper">
          <Table striped bordered hover>
              <thead>
                  <tr>
                      <th></th>
                      <th>ID</th>
                      <th>Nombre</th>
                      <th>Posición Laboral</th>
                      <th>Salario</th>
                      <th>Status</th>
                      <th>Fecha de contratación</th>
                      <th>...</th>
                  </tr>
              </thead>
              <tbody>
                {employeesList.length <= 0 && <span>No hay empleados registrados! </span>}
                {employeesList.length > 0 &&
                  employeesList.map((employee, i)=>{
                    return (
                    <tr>
                      <td><img alt="not fount" width={"150px"} height={"250px"} src="./default.webp"  className='img-fluid rounded'/></td>
                      <td>{employee.id}</td>
                      <td>{employee.name}</td>
                      <td>{employee.worker_position}</td>
                      <td>{employee.salary}</td>
                      <td>{employee.status ? "ACTIVO":"INACTIVO"}</td>
                      <td><Moment format="DD-MM-YYYY" date={employee.hire_date} /></td>
                      <td>
                        <Button variant="info" size="sm">Detalle</Button>{' '}
                        <Button href={`/update/${employee.id}`} variant="secondary" size="sm">Actualizar</Button>{' '}
                        <Button variant="danger" size="sm">Eliminar</Button>{' '}
                      </td>
                    </tr>
                    )
                  })
                }
              </tbody>
          </Table>
      </div>
    </div>
  );
};

export default EmployeesGrid;