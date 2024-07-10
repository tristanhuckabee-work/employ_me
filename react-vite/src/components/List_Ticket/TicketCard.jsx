import { useDispatch, useSelector } from "react-redux";
import "./TicketList.css";
import { useEffect } from "react";
import { get_all_tickets, ticket_by_site } from "../../redux/ticket";

function TicketCard({ticket}) {
    console.log(ticket);
    return (
        <div className='ticket_card'>
            <div className='tpriority'>{ticket.priority}</div>
            <div className='ticket_details'>
                <h4>{ticket.title}</h4>
                <div className='tc_update_status'>
                    <p className={`tcus_${ticket.status}`}>{ticket.status}</p>
                    <p>{ticket.updated_at}</p>
                </div>
            </div>
        </div>
    )
}

export default TicketCard;