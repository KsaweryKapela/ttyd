import axios from 'axios';

const default_axios = axios.create({
        baseURL: 'http://localhost:5003',
        headers: {
            'Content-Type': 'application/json',
        },
    })

export default default_axios