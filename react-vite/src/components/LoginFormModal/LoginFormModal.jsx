import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };
  const demoLogin = async (e) => {
    e.preventDefault();

    let res = await dispatch(
      thunkLogin({
        email: 'dyung@demo.com',
        password: 'password'
      })
    )

    console.log(res)

    closeModal();
  }

  return (
    <div className='user_action_form'>
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <div className='uaf_input_group'>
          <input
            className='uaf_input'
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <label className={!email ? 'uaf_label' : 'uaf_label filled'}>
            Email
          </label>
          {/* {errors.email && <p id='uafl_email'>{errors.email}</p>} */}
        </div>
        <div className='uaf_input_group'>
          <input
            className='uaf_input'
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <label className={!password ? 'uaf_label' : errors.password ? 'uaf_label uafl_err' : 'uaf_label filled'}>
            Password
          </label>
          {errors.password && <p id='uafl_password'>{errors.password}</p>}
        </div>
        <button className='user_action_btn' type="submit">Log In</button>
      </form>
      <button className='user_action_btn' onClick={demoLogin}>Demo Log In</button>
    </div>
  );
}

export default LoginFormModal;
