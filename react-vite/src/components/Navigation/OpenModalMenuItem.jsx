import { useModal } from '../../context/Modal';

/**
 * Creates a modal based on values passed in.
 * @param {Function} modalComponent A functional React Component to render inside the modal
 * @param {String} itemText The text of the modal button
 * @param {Function} onItemClick optional: A function that will be called when the modal button is clicked
 * @param {Function} onModalClose optional: A function that will be called when the modal is closed
 */
function OpenModalMenuItem({modalComponent, itemText, onItemClick, onModalClose}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (typeof onItemClick === "function") onItemClick();
  };

  return (
    <button className='user_action_btn' onClick={onClick}>{itemText}</button>
  );
}

export default OpenModalMenuItem;
