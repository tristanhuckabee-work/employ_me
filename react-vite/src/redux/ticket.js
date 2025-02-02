const CREATE = 'tickets/new';
const GET_ALL = 'tickets/all';
const BY_ID = 'tickets/by_id';
const MINE = 'tickets/my_tickets';
const BY_SITE = 'tickets/by_site';
const BY_STATUS = 'tickets/by_status';
const EDIT_TICKET = 'tickets/edit';
const DELETE_TICKET = 'tickets/delete';

const createTicket = t => ({ type: CREATE, payload: t });
const getAllTickets = t => ({ type: GET_ALL, payload: t });
const ticketById = t => ({ type: BY_ID, payload: t });
const myTickets = t => ({ type: MINE, payload: t });
const ticketBySite = t => ({ type: BY_SITE, payload: t });
const ticketByStatus = t => ({ type: BY_STATUS, payload: t });
const updateTicket = t => ({ type: EDIT_TICKET, payload: t });
const deleteTicket = t => ({ type: DELETE_TICKET, payload: t });

export const create_ticket = () => async dispatch => {
    return;
}
export const get_all_tickets = () => async dispatch => {
    const res = await fetch('/api/tickets/all');
    const data = await res.json();

    if (res.ok) {
        dispatch(getAllTickets(data));
        return;
    }
    return data;
}
export const ticket_by_id = id => async dispatch => {
    const res = await fetch(`/api/tickets/${id}`);
    const data = await res.json();

    if (res.ok) {
        dispatch(ticketById(data));
        return;
    }
    return data;
}
export const ticket_by_site = (site_ids) => async dispatch => {
    let site_tickets = [];

    for (let id in site_ids) {
        const res = await fetch(`/api/tickets/by-site/${id}`);
        const data = await res.json();
        if (res.ok) {
            site_tickets = [...site_tickets, ...data.tickets];
        }
    }

    dispatch(ticketBySite(site_tickets));
    return;
}
export const ticket_by_status = () => async dispatch => {
    return;
}
export const update_ticket = () => async dispatch => {
    return;
}
export const delete_ticket = () => async dispatch => {
    return;
}

let initialState = {active: {}, complete: {}, current: null}
function ticketReducer(state = initialState, action) {
    let newState = { ...state };

    switch (action.type) {
        case CREATE:
            return newState;
        case BY_SITE:
            newState.active = {};
            newState.complete = {};
            action.payload.forEach(t => {
                newState[t.status][t.id] = t;
            })
            return newState;
        case GET_ALL:
            action.payload.forEach(t => {
                newState[t.status][t.id] = t;
            })
            return newState;
        case BY_ID:
            newState.current = action.payload;
            console.log('TICKET BY ID: ', newState);
            return newState;
        case MINE:
            return newState;
        case BY_STATUS:
            return newState;
        case EDIT_TICKET:
            return newState;
        case DELETE_TICKET:
            return newState;
        default:
            return state;
    }
}

export default ticketReducer;