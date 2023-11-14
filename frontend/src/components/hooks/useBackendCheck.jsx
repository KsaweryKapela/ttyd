import { useState, useEffect } from 'react';
import checkHealth from '../api/checkHealth';


const useBackendCheck = (checkInterval = 1000) => {
  const [backendReady, setBackendReady] = useState(false);

  useEffect(() => {
    const checkBackend = async () => {
      const isReady = await checkHealth();
      if (isReady) {
        setBackendReady(true);
      } else {
        setTimeout(checkBackend, checkInterval);
      }
    };

    checkBackend();
  }, [checkInterval]);

  return backendReady;
};

export default useBackendCheck;