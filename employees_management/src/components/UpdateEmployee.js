import React from 'react';
import {
  useParams
} from "react-router-dom";

const UpdateEmployee = () => {
  const { id } = useParams();
  console.log("From UpdateEmployee: ", id)
  return (
    <React.Fragment>
      <h1>Update employee with ID {id}</h1>
    </React.Fragment>
  );
};

export default UpdateEmployee;