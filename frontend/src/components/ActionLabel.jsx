import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGear } from '@fortawesome/free-solid-svg-icons';

function ActionLabel({ label, backendReady }) {
  return (
    <>
    {backendReady ? label : "Loading Model "}
      {!backendReady && <FontAwesomeIcon icon={faGear} spin />}
    </>
  );
}

export default ActionLabel;
