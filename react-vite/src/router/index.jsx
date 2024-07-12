import { createBrowserRouter, Navigate } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import Main from '../components/Main';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import Ticket_Page from '../components/PageTicket/PageTicket';

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
            path: `:ticket_id`,
            element: <Ticket_Page />
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