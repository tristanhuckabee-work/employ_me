import { useDispatch, useSelector } from "react-redux";
import "./Main.css";
import TicketList from "../List_Ticket/TicketList";

function Main() {
    const dispatch = useDispatch()
    const current_user = useSelector(state => state.session.user);

    if (current_user) {
        return (
            <main>
                {(current_user.is_admin && (
                    <>
                        <TicketList />
                    </>
                )) || (
                        <>
                            <h2>My Sites</h2>
                            <TicketList />
                        </>
                    )}
            </main>
        )
    } else {
        return (
            <main>
                <h1>Hello Stranger!</h1>
            </main>
        )
    }
}

export default Main;