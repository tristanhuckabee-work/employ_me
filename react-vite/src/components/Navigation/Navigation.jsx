import { useState, useEffect, useRef } from "react";
import { NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { FaUserCircle } from 'react-icons/fa';
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import "./Navigation.css";

function Navigation() {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const current_user = useSelector(store => store.session.user);

  const admin_panel = () => {
    if (current_user.is_admin) {
      return (
        <>
          <p>Admin</p>
          <h3>All Clients</h3>
          <h3>All Employees</h3>
          <h3>All Sites</h3>
          <h3>All Tickets</h3>
        </>
      )
    } else {
      let site_comp = current_user.sites.map(site => {
        return (
          <div className='uoud_site_card'>
            <h4 className={site.role == 'Manager' ? 'primary' : null}>{site.site.name}</h4>
          </div>
        )
      })
      return (
        <>
          <h3>My Sites</h3>
          <div className='uoud_sites'>
            {site_comp}
          </div>
        </>
      )
    }
  }

  const logout = e => {
    e.preventDefault();
    dispatch(thunkLogout());
    setShowMenu(false);
  }
  console.log(showMenu)
  if (current_user) {
    return (
      <>
        <nav>
          <h1><NavLink id="logo" exact to="/">employ me</NavLink></h1>
          <div id='user_actions'>
            <FaUserCircle size={28} className="user_icon" onClick={() => setShowMenu(!showMenu)} />
          </div>
        </nav>
        {/* {showMenu && ( */}
        <div id={showMenu ? 'user_options' : 'offscreen_menu'}>
          <div id='uo_user_details'>
            <h2 className='primary'>{current_user.last_name}, {current_user.first_name}</h2>
            <p style={{'margin-bottom':'10px'}}>{current_user.email}</p>
            {admin_panel()}
          </div>
          <button onClick={logout}>Log Out</button>
        </div>
        
      </>
    );
  } else {
    return <nav>
      <h1><NavLink id="logo" exact to="/">employ me</NavLink></h1>
      <div id='user_actions'>
        <OpenModalMenuItem
          itemText="Log In"
          modalComponent={<LoginFormModal />}
        />
        <OpenModalMenuItem
          itemText="Sign Up"
          modalComponent={<SignupFormModal />}
        />
      </div>
    </nav>
  }
}

export default Navigation;
