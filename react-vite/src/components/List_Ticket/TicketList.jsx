import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { FaPlusCircle } from "react-icons/fa";
import { get_all_tickets, ticket_by_site } from "../../redux/ticket";
import TicketCard from "./TicketCard";
import "./TicketList.css";

function TicketList() {
    const dispatch = useDispatch()
    const navigate = useNavigate();
    const current_user = useSelector(state => state.session.user);
    const site_ids = current_user?.sites?.map(site => {
        return site.site.id;
    });

    useEffect(() => {
        if (current_user.is_admin) {
            dispatch(get_all_tickets());
        } else {
            dispatch(ticket_by_site(site_ids));
        }
    }, [dispatch, current_user])

    const tickets = useSelector(state => state.tickets);

    const ticket_comp = (ts) => {
        let res = [];

        for (let t in ts) {
            res.push(<TicketCard ticket={ts[t]} />)
        }

        return res;
    }

    return (
        <div className='ticket_list'>
            <div className="tl_header">
                <h3>Tickets</h3>
                <span onClick={() => navigate('/tickets/new')}>
                    <FaPlusCircle size={28} />
                    <p>New Ticket</p>
                </span>
            </div>
            <div className='tl_list'>
                {ticket_comp(tickets?.active)}
                {ticket_comp(tickets?.complete)}
            </div>
        </div>
    )
}

export default TicketList;