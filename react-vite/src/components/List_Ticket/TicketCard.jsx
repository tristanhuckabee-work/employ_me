import { useDispatch, useSelector } from "react-redux";
import "./TicketList.css";
import { useEffect } from "react";
import { get_all_tickets, ticket_by_site } from "../../redux/ticket";

function TicketCard({ticket}) {

    const format_date = (date) => {
        let dates = {
            'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
            'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
            'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'
        }
        let res = date.split(' ');
        return `${dates[res[2]]}/${res[1]}/${res[3]}`
    }

    return (
        <div className='ticket_card'>
            <div className='tpriority'>{ticket.priority}</div>
            <div className='ticket_details'>
                <h4>{ticket.title}</h4>
                <div className='tc_update_status'>
                    <p className={`tcus tcus_${ticket.status}`}>{ticket.status}</p>
                    <p>{format_date(ticket.updated_at)}</p>
                </div>
            </div>
        </div>
    )
}

export default TicketCard;