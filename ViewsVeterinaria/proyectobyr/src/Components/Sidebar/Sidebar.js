import React from 'react';
import './styles.css';
import SidebarItem from './SidebarItem';
import { faHome, faCalendar,faClipboard, faUsers, faUserTie, faUserPlus, faTruck } from '@fortawesome/free-solid-svg-icons';
import SidebarItemWithSubMenu from './SidebarItemWithSubMenu'; // Asegúrate de importar SidebarItemWithSubMenu
import SubmenuItem from './SubmenuItem';
import logo from '../../images/bobbieyrobin.png';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <SidebarItem icon={faHome} text="Inicio" onClick={() => { window.location.href = '/inicio'; }} />
      <SidebarItem icon={faCalendar} text="Citas" onClick={() => { window.location.href = '/citas'; }} />
      <SidebarItemWithSubMenu icon={faClipboard} text="Inventario">
        <SubmenuItem text="Ver Productos" onClick={() => { window.location.href = '/productos'; }} />
      </SidebarItemWithSubMenu>
      <SidebarItemWithSubMenu icon={faUsers} text="Clientes">
        <SubmenuItem text="Lista de Clientes" onClick={() => { window.location.href = '/clientes'; }} />
        <SubmenuItem text="Mascotas" onClick={() => { window.location.href = '/mascotas'; }} />
      </SidebarItemWithSubMenu>
      <SidebarItem icon={faUserTie} text="Gestión de Empleados" onClick={() => { window.location.href = '/empleados'; }} />
      <SidebarItem icon={faUserPlus} text="Gestión de Usuarios" onClick={() => { window.location.href = '/usuarios'; }} />
      <SidebarItem icon={faTruck} text="Gestión de Proveedores" onClick={() => { window.location.href = '/proveedores'; }} />
    </div>
  );
}

export default Sidebar;
