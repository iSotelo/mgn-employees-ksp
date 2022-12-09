import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';
import axios from 'axios';

const EmployeesForm = (props) => {

  // Employee State
  // seteamos la prop dependiendo si se va registrar o actualizar
  const [employee, setEmployee] = useState({
    name: props.employee ? props.employee.name : '',
    worker_position: props.employee ? props.employee.worker_position : '',
    salary: props.employee ? props.employee.salary : '',
    status: props.employee ? props.employee.status : '',
    hire_date: props.employee ? props.employee.hire_date : '',
    // image: props.employee ? props.employee.image : '',
  });

  // image state
  const [selectedImage, setSelectedImage] = useState(null);

  // Eroor State
  const [alertMsg, setAlertMsg] = useState('');
  const [alertVariant, setAlertVariant] = useState('');
  const { name, worker_position, salary, status, hire_date } = employee;

  const handleOnSubmit = (event) => {
    event.preventDefault();
    const values = [name, worker_position, salary, status, hire_date];
    let alertMsg = '';
    let alertVariant = '';

    // every permite validar que todos los valores del arreglo esten asignados
    const allFieldsFilled = values.every((field) => {
      const value = `${field}`.trim();
      return value !== '' && value !== '0';
    });

    if (allFieldsFilled) {
      const employee = {
        name,
        worker_position,
        salary,
        status: status === "2" ? false : true,
        hire_date: new Date(hire_date)
      };
      props.handleOnSubmit(employee);

      axios.post(
        "http://localhost:8000/employees/",
        employee
        ).then((response) => {
          console.log("Response data: ", response)
          
      });

      alertMsg = 'Se registro el empleado con éxito.';
      alertVariant = 'success';

    } else {
      alertMsg = 'Por favor complete todos los campos.';
      alertVariant = 'danger';
    }
    setAlertMsg(alertMsg);
    setAlertVariant(alertVariant)
  };


  // cambia el estado de la prop cuando cambia el atirbuto X
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case 'salary':
        if (value === '' || value.match(/^\d{1,}(\.\d{0,2})?$/)) {
          setEmployee((prevState) => ({
            ...prevState,
            [name]: parseFloat(value)
          }));
        }
        break;
      default:
        setEmployee((prevState) => ({
          ...prevState,
          [name]: value
        }));
    }
  };

  return (
    <div className="main-form">
      {alertMsg && <Alert key={alertVariant} variant={alertVariant}>{alertMsg}</Alert>}
      <Form onSubmit={handleOnSubmit}>
        <div className="row">
          <div className='col-md-6'>
            <Form.Group controlId="name">
              <Form.Label>Foto</Form.Label>
              <Form.Control
                className="input-control"
                type="file"
                name="profile_image"
                onChange={(event) => {
                  setSelectedImage(event.target.files[0]);
                }}
              />
            </Form.Group>
            {selectedImage && (
              <div>
                <img alt="not fount" width={"250px"} height={"350px"} src={URL.createObjectURL(selectedImage)}  className='img-fluid rounded'/>
                <br />
                <Button variant="light" onClick={()=>setSelectedImage(null)}>Limpiar</Button>
              </div>
            )}
          </div>
          <br />
          <div className='col-md-6'>
            <Form.Group controlId="name">
              <Form.Label>Nombre del empleado</Form.Label>
              <Form.Control
                className="input-control"
                type="text"
                name="name"
                value={name}
                placeholder="Introduzce el nombre del empleado"
                onChange={handleInputChange}
              />
            </Form.Group>
            <Form.Group controlId="worker_position">
              <Form.Label>Posición laboral</Form.Label>
              <Form.Control as="select"
                className="input-control"
                type="text"
                name="worker_position"
                value={worker_position}
                defaultValue=""
                placeholder="Introduzce el puesto desempeñado"
                onChange={handleInputChange}
              >
                <option selected>Seleccione una opción</option>
                <option>DESARROLLADOR</option>
                <option>CALIDAD QA</option>
                <option>ANALISTA DE SISTEMAS</option>
                <option>RH</option>
                <option>ESPECIALISTA DE DATOS</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="salary">
              <Form.Label>Salario</Form.Label>
              <Form.Control
                className="input-control"
                type="number"
                name="salary"
                value={salary}
                placeholder="Introduce el salario"
                onChange={handleInputChange}
              />
            </Form.Group>
            <Form.Group controlId="status">
              <Form.Label>Status</Form.Label>
              <Form.Control as="select"
                className="input-control"
                type="text"
                name="status"
                value={status}
                placeholder="Activo o inactivo"
                onChange={handleInputChange}
              >
                <option selected>Seleccione una opción</option>
                <option value="1">ACTIVO</option>
                <option value="2">INACTIVO</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="hire_date">
              <Form.Label>Fecha de contratación</Form.Label>
              <Form.Control
                className="input-control"
                type="date"
                name="hire_date"
                value={hire_date}
                placeholder="Fecha de contratación"
                onChange={handleInputChange}
              />
            </Form.Group>
          </div>
        </div>
        <br />
        <Button variant="primary" type="submit" className="submit-btn">
          Registrar
        </Button>
      </Form>
    </div>
  );
};

export default EmployeesForm;