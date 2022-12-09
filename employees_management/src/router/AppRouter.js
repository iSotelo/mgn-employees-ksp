import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from '../components/Header';
import AddEmployee from '../components/AddEmployee';
import UpdateEmployee from '../components/UpdateEmployee';
import EmployeesGrid from '../components/EmployeesGrid';
import BeneficiariesList from '../components/Beneficiaries'

const AppRouter = () => {
  return (
      <BrowserRouter>
        <div>
          <Header />
          <bt />
          <div className="main-content">
            <Routes>
              <Route index element={<EmployeesGrid />} />
              <Route path="add" element={<AddEmployee />}  />
              <Route path="update/:id" element={<UpdateEmployee />}  />
              <Route path="/beneficiaries" element={<BeneficiariesList />}  />
            </Routes>
          </div>
        </div>
      </BrowserRouter>
  );
};

export default AppRouter;