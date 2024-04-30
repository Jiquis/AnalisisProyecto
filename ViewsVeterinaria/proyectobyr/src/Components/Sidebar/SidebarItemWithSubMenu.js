import React, { useState } from 'react';
import SidebarItem from './SidebarItem';
import SubmenuItem from './SubmenuItem';
import './styles.css';

const SidebarItemWithSubMenu = ({ icon, text, onClick, submenus }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSubMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="sidebar-item" onClick={onClick}>
      <div className="sidebar-item-content" onClick={submenus ? toggleSubMenu : null}>
        <div className="sidebar-item-icon">{icon}</div>
        <div className="sidebar-item-text">{text}</div>
      </div>
      {isOpen && submenus && <div className="sidebar-submenu">{submenus}</div>}
    </div>
  );
};

export default SidebarItemWithSubMenu;