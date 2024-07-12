import { createBrowserRouter, Navigate } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import Main from '../components/Main';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Main />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "tickets",
        children: [
          {
            path: 'new',
            element: <h1>NEW TICKET FORM</h1>
          },
          {
            path: ':ticketId',
            element: <h1>TICKET</h1>
          },
          {
            path: '',
            element: <Navigate to='/' />
          }
        ],
      },
      {
        path: '*',
        element: <Navigate to='/' />
      }
    ],
  },
]);