import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { ticket_by_id } from "../../redux/ticket";
import "./PageTicket.css";

function Ticket_Page() {
    const dispatch = useDispatch();
    const { ticket_id } = useParams();

    useEffect(() => {
        dispatch(ticket_by_id(ticket_id));
    }, [dispatch, ticket_id]);
    const ticket = useSelector(state => state?.tickets[ticket_id]);
    console.log(ticket);
    const format_date = (date) => {
        let dates = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        let res = date.split(' ');
        return `${dates[res[2]]}/${res[1]}/${res[3]}`
    }
    const format_images = () => {
        if (ticket?.images.length) {
            return (
                <span>
                    <h3>IMAGES</h3>
                    <button>ADD IMAGE</button>
                </span>
            )
        }
        return (
            <span>
                <h3>NO IMAGES</h3>
                <button>ADD IMAGE</button>
            </span>
        )
    }

    if (ticket) {
        return (
            <div id='ticket_page'>
                <div id="ticket_details">
                    <div id="td_header">
                        <span>
                            <h2>
                                {ticket?.title} <span style={{ 'color': 'var(--on-background)' }}>-</span> {ticket?.site?.name}
                            </h2>
                            <span id='tdh_options'>
                                <button className="tedit_btn">EDIT</button>
                                <button className="tdelete_btn">DELETE</button>
                            </span>
                        </span>
                        <span>
                            <p id='tdh_bot' style={{ 'margin-bottom': '10px' }}>
                                <strong>last updated on</strong> {format_date(ticket?.updated_at)} - <span className="secondary">{ticket?.status}</span>
                            </p>
                            <p><strong>created by</strong> {ticket?.owner?.first_name} {ticket?.owner?.last_name}</p>
                        </span>
                    </div>
                    <div id="td_images">{format_images()}</div>
                    <p><strong>Description:</strong> {ticket?.description}</p>
                </div>
                <aside id='ticket_notes'>
                    <h2>Progress Log</h2>
                </aside>

            </div>
        )
    }
}

export default Ticket_Page;