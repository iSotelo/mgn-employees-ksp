import React from 'react';
import EmployeeForm from './EmployeeForm';

const AddEmployee = () => {
  const handleOnSubmit = (employee) => {
    console.log("Component:AddEmployee => employee: ", employee)
  };

  return (
    <React.Fragment>
      <EmployeeForm handleOnSubmit={handleOnSubmit} />
    </React.Fragment>
  );
};

export default AddEmployee;