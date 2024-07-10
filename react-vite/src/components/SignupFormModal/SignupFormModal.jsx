import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

    const serverResponse = await dispatch(
      thunkSignup({
        email,
        username,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <div className="user_action_form">
      <h1>Sign Up</h1>
      {errors.server && <p>{errors.server}</p>}
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
          {errors.email && <p>{errors.email}</p>}
        </div>
        <div className='uaf_input_group'>
          <input
            className='uaf_input'
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <label  className={!email ? 'uaf_label' : 'uaf_label filled'}>
            Username
          </label>
          {errors.username && <p>{errors.username}</p>}
        </div>
        <div className='uaf_input_group'>
          <input
            className='uaf_input'
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <label className={!password ? 'uaf_label' : 'uaf_label filled'}>
            Password
            </label>
          {errors.password && <p>{errors.password}</p>}
        </div>
        <div className='uaf_input_group'>
          <input
            className='uaf_input'
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
          <label className={!confirmPassword ? 'uaf_label' : 'uaf_label filled'}>
            Confirm Password
          </label>
          {errors.confirmPassword && <p>{errors.confirmPassword}</p>}
        </div>
        <button className='user_action_btn' type="submit">Sign Up</button>
      </form>
    </div>
  );
}

export default SignupFormModal;
