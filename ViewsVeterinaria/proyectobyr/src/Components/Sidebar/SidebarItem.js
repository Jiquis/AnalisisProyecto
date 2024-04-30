import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'; // Importa FontAwesomeIcon aquí
import './styles.css';
import SubmenuItem from './SubmenuItem';

const SidebarItem = ({ icon, text, onClick, submenus }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSubMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="sidebar-item" onClick={onClick}>
      <div className="sidebar-item-content" onClick={submenus ? toggleSubMenu : null}>
        <div className="sidebar-item-icon">
          <FontAwesomeIcon icon={icon} /> {/* Renderizar el icono de FontAwesome */}
        </div>
        <div className="sidebar-item-text">{text}</div>
      </div>
      {isOpen && submenus && <div className="sidebar-submenu">{submenus}</div>}
    </div>
  );
};

export default SidebarItem;
