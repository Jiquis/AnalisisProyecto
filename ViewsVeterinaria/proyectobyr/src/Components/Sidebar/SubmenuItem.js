import React, { useState } from 'react';

const SubmenuItem = ({ text, children }) => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleSubMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className={`submenu ${isOpen ? 'open' : ''}`} onClick={toggleSubMenu}>
            <div>{text}</div>
            <div className="submenu-items">{isOpen && children}</div>
        </div>
    );
};

export default SubmenuItem;
