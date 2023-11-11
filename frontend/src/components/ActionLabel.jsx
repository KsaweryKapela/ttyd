import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';

function ActionLabel({ label, backendReady }) {
  return (
    <>
    {backendReady ? label : "Loading Model "}
      {!backendReady && <FontAwesomeIcon icon={faSpinner} spin />}
    </>
  );
}

export default ActionLabel;
