import HomePage from "../pages/home/HomePage";
import { RouteType } from "./config";
import CitasPageLayout from "../pages/changelog/citas/CitasPageLayout";
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import Citas from "../pages/changelog/citas/Citas";
import ChecklistOutlinedIcon from '@mui/icons-material/ChecklistOutlined';
import HomeSite from "../pages/home/HomeSite";
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';
import CalendarTodayOutlinedIcon from '@mui/icons-material/CalendarTodayOutlined';
import Inventory2OutlinedIcon from '@mui/icons-material/Inventory2Outlined';
import VerCitas from "../pages/changelog/citas/VerCitas";
import Productos from "../pages/inventario/productos";
import Inventario from "../pages/inventario/Inventario";
import InventarioPageLayout from "../pages/inventario/InventarioPageLayout";
import ListadeClientes from "../pages/clientes/ListadeClientes";
import Clientes from "../pages/clientes/Clientes";
import ClientesPageLayout from "../pages/clientes/ClientesPageLayout";
import Mascotas from "../pages/clientes/Mascotas";
import EmpleadosPage from "../pages/changelog/EmpleadosPage";
import UsuariosPage from "../pages/usuarios/UsuariosPage";
import ProveedoresPage from "../pages/proveedores/ProveedoresPage";
import InventoryOutlinedIcon from '@mui/icons-material/InventoryOutlined';
import SupportAgentOutlinedIcon from '@mui/icons-material/SupportAgentOutlined';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import PetsOutlinedIcon from '@mui/icons-material/PetsOutlined';
import BadgeOutlinedIcon from '@mui/icons-material/BadgeOutlined';
import VerifiedUserOutlinedIcon from '@mui/icons-material/VerifiedUserOutlined';
import LocalShippingOutlinedIcon from '@mui/icons-material/LocalShippingOutlined';

const appRoutes: RouteType[] = [
    {
        index: true,
        element: <HomePage />,
        state: "home"
    },
    {
        path: "/home",
        element: <HomeSite/>,
        state: "homesite",
        sidebarProps:{
            displayText: "Home",
            icon: <HomeOutlinedIcon/>
        }
    },
    {
        path: "/citas",
        element: <CitasPageLayout/>,
        state: "citas",
        sidebarProps: {
            displayText: "Citas",
            icon: <CalendarMonthOutlinedIcon/>
        },
        child: [
            {
                index: true,
                element: <Citas/>,
                state: "citas.index",
               
            },
            {
                path: "/citas/vercitas",
                element: <VerCitas/>,
                state: "citas.vercitas",
                sidebarProps:{
                    displayText: "Ver Citas",
                    icon: <CalendarTodayOutlinedIcon/>
                },
            },
            
        ]
    },
    {
        path: "/inventario",
        element: <InventarioPageLayout/>,
        state: "inventario",
        sidebarProps: {
            displayText: "Inventario",
            icon: <Inventory2OutlinedIcon/>
        },
        child: [
            {
                index: true,
                element: <Inventario/>,
                state: "inventario.index",
               
            },
            {
                path: "/inventario/productos",
                element: <Productos/>,
                state: "inventario.productos",
                sidebarProps:{
                    displayText: "Productos",
                    icon: <InventoryOutlinedIcon/>
                },
            },
            
            
        ]
    },
    {
        path: "/clientes",
        element: <ClientesPageLayout/>,
        state: "clientes",
        sidebarProps: {
            displayText: "Clientes",
            icon: <SupportAgentOutlinedIcon/>
        },
        child: [
            {
                index: true,
                element: <Clientes/>,
                state: "clientes.index",
               
            },
            {
                path: "/clientes/listadeclientes",
                element: <ListadeClientes/>,
                state: "clientes.listadeclientes",
                sidebarProps:{
                    displayText: "Lista de Clientes",
                    icon: <AccountCircleOutlinedIcon/>
                },
            },
            {
                path: "/clientes/mascotas",
                element: <Mascotas/>,
                state: "clientes.mascotas",
                sidebarProps:{
                    displayText: "Mascotas",
                    icon: <PetsOutlinedIcon/>
                },
            },
            
            
        ]
    },
    {
        path: "/empleados",
        element: <EmpleadosPage/>,
        state: "empleados",
        sidebarProps:{
            displayText: "Gestion de Empleados",
            icon: <BadgeOutlinedIcon/>
        }
    },
    {
        path: "/usuarios",
        element: <UsuariosPage/>,
        state: "usuarios",
        sidebarProps:{
            displayText: "Gestion de Usuarios",
            icon: <VerifiedUserOutlinedIcon/>
        }
    },
    {
        path: "/proveedores",
        element: <ProveedoresPage/>,
        state: "proveedores",
        sidebarProps:{
            displayText: "Gestion de Proveedores",
            icon: <LocalShippingOutlinedIcon/>
        }
    }
];

export default appRoutes;