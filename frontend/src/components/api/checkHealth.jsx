import defaultAxios from './defaultAxios';

async function checkHealth() {
    try {
        const response = await defaultAxios.get('/health');
        return response.status === 200;
    } catch (error) {
        console.error('Health check failed:', error);
        return false;
    }
}

export default checkHealth;